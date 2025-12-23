📑 Dijital Görüntü İşleme: Akıllı Belge Tarayıcı

Bu proje, görüntü işleme algoritmaları kullanarak fiziksel belgelerin dijital ortama aktarılmasını sağlayan bir Smart Document Scanner uygulamasıdır. 
Standart bir kamera çekimindeki yamuklukları ve arka plan gürültülerini temizleyerek profesyonel bir tarama çıktısı üretir.

🎯 Projenin Amacı

Perspektif hatası içeren (açılı çekilmiş) belgeleri, dijital görüntü işleme teknikleri ile normalize ederek sanki bir masaüstü tarayıcıdan geçirilmiş gibi dikey, 
düz ve temiz bir forma dönüştürmektir.


🛠 Kullanılan Teknolojiler ve Yöntemler

PythonProjenin ana programlama dili.
OpenCVSegmentasyon, morfoloji ve geometrik dönüşümler.
NumPyMatris işlemleri ve koordinat sıralama matematiği.
GrabCutNesneyi (belge) arka plandan ayıran segmentasyon algoritması.

📖 Uygulama İş Akışı (Pipeline)

Uygulama temel olarak 5 aşamadan oluşmaktadır:

1-Ön İşleme (Rescaling): Bellek yönetimini optimize etmek ve algoritmaların işlem süresini kısaltmak için görüntü ölçeklendirilir.

2-Segmentasyon (GrabCut): Kullanıcı müdahalesine gerek kalmadan, görüntüdeki ön plan (belge) ve arka plan (zemin) birbirinden ayrıştırılır.

3-Morfolojik Filtreleme: MORPH_CLOSE ile maskedeki boşluklar doldurulur, MORPH_OPEN ile kenar pürüzleri giderilir.

4-Kontur ve Köşe Tespiti: Belgeyi temsil eden en geniş poligon bulunur. Bulunan koordinatlar; Sol Üst, Sağ Üst, Sağ Alt ve Sol Alt şeklinde matematiksel olarak sıralanır.

5-Perspektif Dönüşümü: getPerspectiveTransform ve warpPerspective fonksiyonları kullanılarak 2D düzleme aktarım (Homografi) gerçekleştirilir.

🚀 Kurulum ve Çalıştırma
1. Gereksinimlerin Yüklenmesi
Sisteminizde Python yüklü olmalıdır. 
Ardından terminale şu komutu yazarak gerekli kütüphaneleri kurabilirsiniz:


    pip install opencv-python numpy

2. Uygulamanın Başlatılması
Proje klasöründeyken şu komutu çalıştırın (Varsayılan olarak belge1.jpg okunacaktır):


    python belge_tarayici.py


📈 Çıktı Analizi

Program başarılı bir şekilde çalıştığında şu çıktıları üretir:

Tespit Penceresi: Orijinal görüntü üzerinde belgenin konumunu yeşil konturlar ile gösterir.

Sonuç Penceresi: Kesilmiş, düzeltilmiş ve dikey forma getirilmiş son belge görüntüsü.

Kayıt: İşlenen sonuç otomatik olarak taranan_belge.jpg adıyla yerel dizine kaydedilir.
