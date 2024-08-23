#superclassın özelliklerinin subclasslara miras olarak aktarılmasıdır. Böylece subclass superclassın özelliklerini taşır
class Araba :
    def __init__(self,model,fiyat):
        self.model = model
        self.fiyat = fiyat
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

### self.model = model ve self.fiyat = fiyat nesnelerine zaten Araba classının özellikleri olduğundan ve Kamyon subclassı da Araba superclassının özelliklerine erişebildiği için kodu şöyle düzenleyebiliriz:
def __init__(self, model,fiyat,renk):
    Araba.__init__(self,model,fiyat)
    self.renk = renk