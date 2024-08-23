masa_no = 0 #başlangıç değeri atanmalıdır ilk başta koşul ve döngü ifadeleri için
liste_evening = ["ali","can","miray","zeynep"]
liste_tomorrow = ["bahar","talat"]
isim = input("Adınızı girin:")
if isim == "ali":
    masa_no = 5
if isim == "can":
    masa_no = 7
if isim == "miray":
    masa_no = 2
if isim == "zeynep":
    masa_no = 10
if isim in liste_evening:
    print("rezervasyonunuz bu akşam, masa numarası: ",masa_no)
elif isim in liste_tomorrow:
    print("rezervasyonunuz yarın akşam, masa numarası: ",masa_no)
elif isim not in liste_evening and liste_tomorrow:
    print("rezervasyonunuz bulunmamaktadır.")