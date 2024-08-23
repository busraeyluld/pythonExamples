name = "aslı"
surname = "sütçüoğlu"
age = 27
id_number = 3676834
residency = "istanbul"
nationality = "türkiye"
print("adım %s %s %s yaşındayım. %s'da yaşıyorum" % (name, surname, age, residency))

shopping_list = ["laptop", "headset", "second monitor", "mousepad", "USB drive"]
print("alınacaklar: ", shopping_list)
# slice list for mandatory items
mandatories = shopping_list[0:3]  # [:3]
# slice list for optional items
optionals = shopping_list[3:5]  # [3:]
print("gerekli olanlar:", mandatories, ";", "isteğe bağlı olanlar:", optionals)

limit = 5000  # ne kadar harcamamız gerektiğini bilmek için şirketin verdiği miktar
# her bir alınacak için bir fiyat listesi oluşturalım ve bunun için herbirinin fiyatını bulacağımız bir dictionary oluşturalım
price_sheet_dict = {"laptop": 2500, "headset": 750, "second monitor": 1000, "mousepad": 250, "USB drive": 500}

# shopping functions
shopping_cart = []


def add_to_cart(item_name, quantity):
    total_amount = 0
    total_amount = price_sheet_dict[item_name] * quantity * 1.18  # ürün fiyatı
    shopping_cart.append(total_amount)
    return total_amount


def checkout():
    total_amount = sum(shopping_cart)
    remaining_amount = limit - total_amount
    if total_amount <= limit:
        print("harcanan miktar:", total_amount, "ve kalan miktar:", remaining_amount)
    else:
        print("limiti aştınız, aşılan miktar:", abs(limit - total_amount))


add_to_cart("laptop", 2)
add_to_cart("headset", 1)
checkout()
