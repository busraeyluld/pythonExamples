# listelere benzer fakat indexler yarine keylerle erişilir. Key, herhangi bir sayı veya string yapısında olabilir. (key-value pairs)
#syntax    d = {'key1': 1, 'key2': 2, 'key3': 3}
resident = {"puffin": 104, "sloth": 105, "burmese python": 106} # sakinler ve oda numaralarını gösteren bir sözlük
print(resident["puffin"])   # puffin key'ini kullanarak bu key'in değerine eriştik
#listeler gibi sözlükler de değişebilir yapıdadır. Yani yeni key-value pairs ekleyebiliriz....
#syntax    dict_name['new_key'] = new_value
menu = {}   #empty dictionary
menu["chicken alfredo"] = 14.50     # oluşturduğumuz boş sözlüğe yeni key-value çifti ekledik
print(menu)
#yeni çiftler ekleyelim
menu["mantı"] = 30
menu["pilaki"] = 12
menu["salata"] = 15
print(menu)

print("menümüzde %d tane yiyecek vardır" % (len(menu)))
print("------")
#dictionary'den eleman silmek
#syntax     del dict_name['key_name']
zoo_animals = {"unicorn": "cotton candy house",
               "sloth": "rainforest exhibit",
               "bengal tiger": "jungle house",
               "atlantic puffin": "arctic exhibit",
               "rockhopper penguin": "arctic exhibit"
               }
print(zoo_animals)
#bu sözlükten unicorn elemanını silelim
del zoo_animals["unicorn"]
print(zoo_animals)
print(len(zoo_animals))

#sözlük elemanlarının değerlerini değiştirmek..
#örneğin bengal tiger'ın bulunduğu konum california zoo olsun.
zoo_animals["bengal tiger"] = "california zoo"
print(zoo_animals)  #çıktıda jungle house yerine california zoo görünecek artık, diğer elemanlar aynı kaldı

#bir sözlük farklı veri tiplerinden oluşabilir.
my_dict = {"fish": ["c", "a", "r", "p"],
           "cash": -4483,
           "luck": "good"
           }
print(my_dict["fish"][0])   #bu sözlükteki fish key'inin içindeki listede yer alan c harfine erişmek istedik
print("------")

inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
# bu sözlüğe yeni bir key ekleyelim ve key değeri bir liste olsun (bu key bir liste barındırsın.
inventory["burlap bag"] = ["apple", "small ruby", "three-toed sloth"]
print(inventory)
inventory["pouch"].sort()       #syntax  dict_name["list_key_name"].method()
print(inventory)
# inventory sözlüğüne pocket adında key ekle ve değer olarak bir liste döndürsün.
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print(inventory)
print("------")

# sözlüklerde for döngüsü
# syntax   for item in dict_name:
                #print (dict_name[item])
d = {"foo": "bar"}
for item in d:
    print(d[item])

webster = {
    "aardvark": "a star of a popular cartoon show",
    "baa": "the sound goat makes",
    "carpet": "goes on the floor",
    "dab": "a small amount"
    }
# for loop ile webster sözlüğündeki elemanları yazdır
for item in webster:
    print(webster[item])
print()
print()

first_dict = {"a": 1, "b": 2}
second_dict = {"a": 2, "b": 4}
for key in first_dict:
    print("first diction: %s" % first_dict[key])
    print("second diction: %s" % first_dict[key])
# BASİT PROJE
#bir manavımız var ve ürünlerimizin fiyatlarını ve stoklarını görmek istiyoruz.
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# tüm varlığı yazdırsın
for fruit in prices:
    print (fruit)
    print("fiyatlar: %s" % (prices[fruit]))
    print("stok miktarları: %s" % (stock[fruit]))
    print()
    print()
# tüm ürünlerimiz satılırsa ne kadar para kazanacağımızı hesaplayalım
total_price = 0
for fruit in prices:
    print(prices[fruit] * stock[fruit])
    total_price = total_price + (prices[fruit] * stock[fruit])
    print("toplam gelir: " , total_price)
def compute_bill(fruit):
    total = 0
    for item in fruit:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
            return total
        print(total)



