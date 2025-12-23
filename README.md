Dijital Görüntü İşleme: Akıllı Belge Tarayıcı ve Perspektif Düzeltme
Bu proje, bir fotoğraf içerisindeki belgeyi otomatik olarak tespit eden, arka plandan ayıran ve perspektif açısını düzelterek belgeyi dijital bir tarama haline getiren bir görüntü işleme uygulamasıdır.

📌 Projenin Amacı
Düşük açıyla veya yamuk çekilmiş belge fotoğraflarının, görüntü işleme algoritmaları kullanılarak sanki bir tarayıcıdan çıkmış gibi dikey ve düzgün bir forma getirilmesini sağlamaktır.

🛠 Kullanılan Teknikler ve Kütüphaneler
Proje Python diliyle geliştirilmiş olup şu kütüphaneleri kullanır:

OpenCV: Görüntü segmentasyonu, morfolojik işlemler ve perspektif dönüşümleri için.

NumPy: Matris hesaplamaları ve köşe koordinatlarının matematiksel analizi için.

📖 Uygulama Adımları
Rescaling (Ölçeklendirme): İşlem hızını artırmak ve GrabCut algoritmasını verimli çalıştırmak için görüntü boyutları optimize edilir.

GrabCut Segmentasyonu: Belgeyi (ön plan) masa veya zeminden (arka plan) ayırmak için iteratif bir bölütleme işlemi uygulanır.

Morfolojik Filtreleme: Segmentasyon sonrası oluşan pürüzleri temizlemek için MORPH_CLOSE (Kapama) ve MORPH_OPEN (Açma) işlemleri uygulanır.

Kontur ve Köşe Tespiti: Temizlenen maske üzerindeki en büyük dörtgen yapı bulunur ve köşe noktaları (Sol Üst, Sağ Üst, Sağ Alt, Sol Alt) matematiksel olarak sıralanır.

Perspektif Dönüşümü: getPerspectiveTransform ve warpPerspective fonksiyonları ile kağıt üzerindeki yamukluk giderilerek nihai sonuç elde edilir.

🚀 Kurulum ve Kullanım
Gereksinimler
Sistemde Python yüklü olmalıdır. Gerekli kütüphaneleri şu komutla yükleyebilirsiniz:

pip install opencv-python numpy

Çalıştırma
Dosyayı terminal üzerinden şu şekilde çalıştırabilirsiniz:

python belge_tarayici.py

📈 Beklenen Çıktılar
Program çalıştığında iki aşamalı bir sonuç üretir:

Tespit Ekranı: Orijinal resim üzerinde belgenin sınırlarının yeşil hatla çizildiği ekran.

Sonuç Ekranı: Belgenin kesilmiş, düzeltilmiş ve taranmış hali. Ayrıca bu sonuç otomatik olarak taranan_belge.jpg adıyla kaydedilir.