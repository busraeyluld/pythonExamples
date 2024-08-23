#tek satırlık fonksiyonlarda geçerli
def dolar (TL): #bu ifade dolar = lambda TL: TL/18 ifadesine eşittir.
    return TL/18
TL = int(input("Türk Lirası giriniz:"))
print(TL, "Türk Lirası = ",dolar(TL),"Dolar")