import datetime


class Araba :
    def __init__(self,model,fiyat):
        self.model = model
        self.fiyat = fiyat
    def arabaBilgi(self):
        print("aracın modeli:", self.model, "\n", "aracın fiyatı:", self.fiyat)
        return (datetime.datetime.now()) #tarih döndürmek için datetime sınıfı import edilmeli
class Kamyon(Araba): #burada parametre kısmına superclass adını yazarak Kamyon adlı classı, Araba classının subclassı yaptık. Artık Araba classının tüm özellik ve metotlarına erişebiliriz bu classda da.
    def __init__(self,model,fiyat,renk):
      self.model = model
      self.fiyat = fiyat
      self.renk = renk


k1 = Kamyon(2020,120000,"kırmızı") #Kamyon subclassından k1 adı ile nesne oluşturduk ve özelliklerini belirledik.
#aşağıda k1 nesnesi için özelliklere eriştik
print(k1.model)
print(k1.fiyat)
print(k1.renk)
print()
print(k1.arabaBilgi()) #burada arabaBilgi() metodu Araba classı altında tanımlanmıştı ve k1 nesnesi ise Kamyon sınıfında tanımlanmıştı. Ama Kamyon sınıfı Araba sınıfının alt sınıfı olup üst sınıfın özelliklerine erişebildiği için
# k1 nesnesi ile arabaBilgi() metoduna erişebiliyoruz.

### self.model = model ve self.fiyat = fiyat nesnelerine zaten Araba classının özellikleri olduğundan ve Kamyon subclassı da Araba superclassının özelliklerine erişebildiği için kodu şöyle düzenleyebiliriz:
#def __init__(self, model,fiyat,renk):
    #Araba.__init__(self,model,fiyat)
    #self.renk = renk