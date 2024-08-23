#deger1 = int(input("Ilk sayiyi giriniz: "))
#deger2 = int(input("Ikinci sayiyi giriniz: "))
#toplam = deger1 + deger2
#print("toplam", toplam)
# Degerlerin ataması yapılırken input icindeki ifade bir string yapısı olarak yazildigi
#icin toplam olarak ifade edilen çıktı 60 yerine 2634 seklinde yan yana string ifadelerin
#birlesmesiyle olusmustur. Int icerisinde input ifadeyi yazarsak string ifade integer olarak
#python'a tanıtılmıs olur.
print("-------")
#lists
# değiştirilebilir veri yapılarıdır
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
print(zoo_animals)
#sloth'u hyena ile değiştir
zoo_animals[2] = "hyena"
print(zoo_animals)

print("-------")

suitcase =[]
suitcase.append("sunglasses")
suitcase.append("book")
suitcase.append("notebook")
suitcase.append("pencil")
print(suitcase)

list_lenght = len(suitcase)
print("bu listenin eleman sayısı:", list_lenght)
print("There are %d items in the suitcase." % list_lenght)
#string formatting: bir değişkeni string ile beraberyazdırmak istersek stringleri + ile birleştirmekten daha iyi bir yol var.
#string sonrası & operatörünün kullanımı ile string ve değişkeni birleştirebiliriz. bu operatör stringlerde %s; intergerlar için %d halini alır ve değişken adı sonra yazılır
name = "mike"
print("hello %s" % (name))
# %s ifadesi, parantez içindeki değişken sayısı kadar olmalıdır
print("hayatta en hakiki mürşit %s %s" %("ilimdir","fendir"))

name1 = "alex"
quest = "teaching python"
number = 4
print("so your name is %s, your quest is %s and your favourite number is %d" % (name1,quest,number))

g = "golf"
h = "hotel"
no = 123345
print("adres: %s %s %d" % (g,h,no))

#list slices: bazen bir listenin belli bir elemanına veya belli bir parçasına erişmek isteriz.
letters = ['a', 'b', 'c', 'd', 'e']
wanted_slice = letters[1:3] #ilki dahil ikincisi hariç
print(wanted_slice)
print(letters)

bag = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
print(bag[0:2]) #ilk 2 elemana erişim için
print(bag[2:4]) #üçüncü ve dördüncü elemana erişim için
print(bag[4:6]) #son iki elemana erişim için

animals = "catdogfrog"
for_cat = animals[:3]
for_dog = animals[3:6]
for_frog = animals[6:10]
print("%s %s %s" % (for_cat, for_dog, for_frog))

animals2 = ["ant", "bat", "cat"]
print(animals2[2])  #listenin ikinci indexindeki elemana erişmek
print(animals2.index("bat"))    #listedeki herhangi bir elemanın (burada bat elemanı hangi indexte?) hangi indexte yani sırada bulunduğunu öğrenmek
animals2.insert(1,"dog")    #listenin 1.indexine dog elemanını eklemek istiyorum. Belirttiğimiz indexe eleman ekler
print(animals2)
animals2.append("bird") #her zaman bir listenin en sonuna eleman ekler yani listenin sıralamasını değiştirmeden listeyi genişletir
print(animals2)
print(len(animals2))
animals2.sort() #liste elemanlarını alfabetik olarak sıralar
print(animals2)
print("--------")
animals3 = ["aardwark", "badger", "duck", "emu", "fennec fox"]
find_duck_index = animals3.index("duck")    #duck elemanının hangi indexte olduğunu bulmak istiyorum
print(find_duck_index)
animals3.insert(find_duck_index, "cobra")   #find_duck_index'in (duck elemanının) bulunduğu indexe cobra elemanını ekliyorum,böylece insert ile elemanları sağa kaydırıyorum
print(animals3)
animals3.remove("emu")
print(animals3)
print("--------")

# listelerde for döngüsü
# syntax   for değişken_adı in list_name:
                 #yapılacakları yaz
my_list = [1, 9, 3, 8, 5, 7]
for num in my_list: #num yerine başka bir isim de verilebilir.
    print(2 * num)  #anlamı: my_list listesindeki her bir num(eleman)ı 2 ile çarparak yazdır
my_list.sort()  #liste elemanlarını küçükten büyüğe sıralar
print(my_list)
print("--------")
start_list = [5, 3, 1, 2, 4]
square_list = []    #boş liste oluşturdum
for item in start_list: #start_listteki her eleman(item ile belirttim) için
    square_list.append(item ** 2)   #start_listteki her elemanın karesini alarak o elemanları square_list listesine ekle
    square_list.sort()  #oluşturduğumuz,genişlettiğimiz square_list listesini küçükten büyüğe sırala
    print(square_list)  #son haliyle square_list listesini yazdır

# a = ["list", "of", "some", "sort"]
# for x in a:
    # a listesindeki her x (eleman) için yapılacaklar

for item in [1, 3, 20]:
    print (item * 2)       # çıktı: 2,6,40
# bir liste oluşturalım ve for loop ile listedeki çift sayıları yazdıralım
l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
for numbers in l:
    if numbers % 2 == 0:
        print(numbers)

# ^^^^^^^^^tek parametre alan bir fonksiyon tanımlayalım ve belirtilen stringin kaç kez geçtiğini yazdırsın.^^^^^^^^^^
def fizz_count(list_x):     # bu fonksiyon parametre olarak bir liste alır ve alacak
    count = 0
    for item in list_x:
        if item == "fizz":
            count += 1
    return count

def fizz_count(list_x = ["fizz", "buzz", "izz","tuzz","fizz","fizz"]):
    count = 0
    for item in list_x:
        if item == "fizz":
            count += 1
            return count
        print(count)

# string looping
# stringler aslında karakterleri eleman olarak alan liste yapılarıdır. Bu yüzden listelerdeki gibi elemanlarına karakterlerine erişebiliriz.
for letter in "codecademy":
    print(letter)

print("-------")

word = "programming is fun"
for letter in word:
    if letter == 'm':   # sadece m karakterini yazdırmak istiyoruz
        print(letter)