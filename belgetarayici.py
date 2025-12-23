import cv2
import numpy as np

def sirala_koseler(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0], rect[2] = pts[np.argmin(s)], pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1], rect[3] = pts[np.argmin(diff)], pts[np.argmax(diff)]
    return rect

def perspektif_duzelt(image, pts):
    rect = sirala_koseler(pts)
    (tl, tr, br, bl) = rect

    w = max(int(np.linalg.norm(br - bl)), int(np.linalg.norm(tr - tl)))
    h = max(int(np.linalg.norm(tr - br)), int(np.linalg.norm(tl - bl)))

    dst = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    return cv2.warpPerspective(image, M, (w, h))

def belge_bul(image):
    h, w = image.shape[:2]
    scale = 400.0 / max(h, w)
    small = cv2.resize(image, None, fx=scale, fy=scale)
    sh, sw = small.shape[:2]

    # GrabCut
    margin = 10
    rect = (margin, margin, sw - 2*margin, sh - 2*margin)
    mask = np.zeros((sh, sw), np.uint8)
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)

    cv2.grabCut(small, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Temizle
    kernel = np.ones((5, 5), np.uint8)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernel)
    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)

    # Kontur
    cnts, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return None

    cnt = max(cnts, key=cv2.contourArea)
    if cv2.contourArea(cnt) < sh * sw * 0.15:
        return None

    box = cv2.boxPoints(cv2.minAreaRect(cnt))
    return (np.intp(box) / scale).astype(np.float32)

def main(image_path):
    print("BELGE TARAYICI")

    image = cv2.imread(image_path)
    if image is None:
        print("Hata: Görüntü okunamadı!")
        return

    corners = belge_bul(image)
    if corners is None:
        print("Belge bulunamadı!")
        return

    print("Belge bulundu!")

    # Göster
    result = image.copy()
    cv2.drawContours(result, [corners.astype(np.intp)], -1, (0, 255, 0), 3)

    warped = perspektif_duzelt(image, corners)

    scale = 600.0 / image.shape[0]
    cv2.imshow("Tespit", cv2.resize(result, None, fx=scale, fy=scale))
    cv2.imshow("Sonuc", cv2.resize(warped, None, fx=600.0/warped.shape[0], fy=600.0/warped.shape[0]))

    cv2.imwrite("taranan_belge.jpg", warped)
    print("Kaydedildi: taranan_belge.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "belge4.jpg")