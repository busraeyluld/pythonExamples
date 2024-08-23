class Araba():
    def __init__(self,model,marka,renk): #değişkenleri başlatmak için metot, ifade
        self.model = model
        self.marka = marka
        self.renk = renk
    def aracBilgisi(self): #metot parametre almasa bile self keywordü yazılmalıdır
        print("araç markası:", self.marka)
        print("araç modeli:", self.model)
        print("araç rengi:", self.renk) ##böylece araç bilgilerini(kaç tane varsa) tek bir metot ile yazdırabiliriz
    #tabii ki nesnemizi oluşturmalıyız ve metotlar çağırılırken class dışında çağrılmalıdır!!
taksi = Araba("opel", 2022, "siyah")
taksi.aracBilgisi()

###sınıf metotları
#fonksiyonlar direkt çağrılırken metotlar nesne adı.metot adı şeklinde çağrılırlar
#self keywordü metot çağrılırken kullanılmaz sadece nesne oluştururken o sınıfın nesnesine işaret etmek için kullanılırlar.
kamyon = Araba(2010,"MAN","kırmızı") #Araba sınıfından bir nesne daha ürettik
kamyon.aracBilgisi()
#bir nesnenin sahip olduğu metot ve özelliklerini görmek
print(dir(taksi))
#__ ifadesi python a ait metotlar olduklarını söyler