    Bu Python kodu bir notepad uygulaması oluşturur.Tkinter modülü kullanılarak GUI arayüzü oluşturulmuştur.

    Kullanıcı metin yazıp düzenleyebilir, dosya açabilir, kaydedebilir ve yazı tipi ayarlarını değiştirebilir. Uygulama içerisinde "File", "Edit", "Format" ve "Help" adında dört menü seçeneği mevcuttur. "File" menüsü dosya açma, kaydetme ve uygulamayı kapatma seçeneklerini içerirken, "Edit" menüsü kesme, kopyalama, yapıştırma ve geri alma seçeneklerini içerir. "Format" menüsü yazı tipi boyutunu ve stilini değiştirme seçeneklerini sunar. "Help" menüsünde ise uygulama hakkında bilgi yer almaktadır.

     Kod, sınıf yapısı kullanılarak yazılmıştır ve metin dosyasını okumak ve yazmak için Python'ın standart kütüphaneleri olan os ve tkinter.filedialog modülleri kullanılmıştır. Kod içerisinde ayrıca hata kontrolü de yapılmaktadır.

Kod içerisinde tanımladığım fonksiyonlar:

    __init__(self, **kwargs) : Notepad sınıfının yapıcı fonksiyonudur ve bu sınıftan bir örnek oluşturulduğunda ilk olarak çağrılır. Pencere boyutlarını, menü çubuğunu ve düzenleyiciyi ayarlar.

    __quitApplication(self) : Notepad uygulamasını sonlandıran fonksiyondur.

    __showAbout(self) : Uygulama hakkında bilgi veren bir mesaj kutusu gösterir.

    __openFile(self) : Dosya açma işlemini gerçekleştiren fonksiyondur.

    __newFile(self) : Yeni bir dosya oluşturur.

    __saveFile(self) : Düzenlenen dosyayı kaydeder.

    __cut(self) : Seçili metni keser.

    __copy(self) : Seçili metni kopyalar.

    __paste(self) : Kopyalanan metni yapıştırır.

    __undo(self) : Yapılan son değişikliği geri alır.

    __setFont(self) : Yazı tipi stilini ve boyutunu ayarlar.