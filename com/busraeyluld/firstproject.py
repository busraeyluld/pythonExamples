#print("Ogrenci Bilgilerini Kaydetme Programı")

#adi = input("Ogrenci adini giriniz: ")
#soyadi = input("Ogrenci soyadini giriniz: ")
#yas = input("Ogrenci yasini giriniz: ")
#numara = input("Ogrenci numarasini giriniz: ")
#keyword args
#print("Programming","Essentials","in",sep="***",end="...")
#print("Python")
#escape karakter
print('"I\'m"'"\n"'"\"learning"\"'"\n"'"\"\"Python\"\"\"')

user_input = input("bir dize girin: ")

if user_input.isupper():
    print("yes spatiphyllum is the best plant ever")
else:
    print("no I want a big one")

print()

list_store = []
def addElements(a,b):
    c = a * b
    list_store.append(c)
    print(list_store)

addElements(3,4)
addElements(2,3)
