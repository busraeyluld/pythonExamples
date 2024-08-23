x = 'B'
y = 'T'
z = ' K'
print("'",x,y,z,"'")
print(type(x))
i=0
j=0
i=i+j #ifadesinin kısa hali: i+=j
#değişken içeriklerini birbirlerine aktarma
b=0
c=5
b,c=c,b
print(b)
print(c)
#aşağıdaki işlemde x kaç çıkar?
t=20+15-10 #t=25 çıkar
x=t/4+7 #25/4+7
print(x)
#python dilindeki keywordleri yazdıran kodlar
import keyword
print(keyword.kwlist)
#d kaç olur?
l=40
m=str(l) + "5"
print(m)

#sep() çıktıdaki karakterler arasına ayraç koyar
print("b","t","k")
print("b","t","k",sep="^")

a="btk"
b=2
c=4
print(b*c)
print(a*b)

#print içindeki karakterlerin alt satıra geçmemesi için ve/veya hemen yanına noktalama eklemek için
#end=('')
print("yaşınız?")
print("yaşınız?",end=('...'))
yas = input()
print("yaşınız:",yas)

#\n: yeni satıra geçmek için
print("merhaba\nnasılsın")

#fonksiyon örneği, dikdörtgen tarlanın alanı
u = int(input("uzun kenarı girin:"))
k = int(input("kısa kenarı girin"))
def alan(u,k):
    alan = u * k
    return alan
def cevre(u,k):
    cevre = (u + k)*2
    return cevre
print("tarlanın çevresi", cevre(u,k),"ve","tarlanın alanı", alan(u,k))

#lokal değişken; fonksiyonlarda tanımlanan değişkenler, global değişken; tüm programlarda yani diğer
#fonksiyonlarda da kullanılabilen değişkenler
def topla():
    a = 5 #lokal değişken
    b = 6 #lokal değişken, sadece bu fonksiyon çağrıldığında ulaşılır
    return a + b
print(topla())
#print(a)
#print(b) bunlar hata verir
#hata vermemesi için: global ile tanımlanmalı
#def topla():
    #global a
    #global b
    #a = 5
    #b = 6
    #return a + b
#print(topla())
#print(a)
#print(b) bu kez hata vermez çünkü global olarak tanımlandı
#veya fonksiyon dışında tanımlanmalı
def topla(): #bu kısım fonksiyon
    return a + b #bu kısım fonksiyon
a = 5 #fonksiyon dışında
b = 6 #fonksiyon dışında
print(topla())
print(a)
print(b)






