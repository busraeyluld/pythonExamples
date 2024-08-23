#girilen string ifadelerin çift indexteki elemanlarını büyük harfle, tek indexteki elemanlarını küçük harfle değiştir
before = "hi my name is john and i am learning python"
def change_size(string):
    new_string = "" #oluşturacağımız yeni strig ifadesini atamak için boş bir string değişkeni oluşturduk
    for string_index in range(len(before)): #before stringinin uzunluğu kadar her bir indexinde dönsün
        if string_index % 2 == 0: #eğer çift indexe gelirse o indexteki elemanı büyük harf yapsın
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)

change_size(before) #kodu çalıştırmak için change_size fonksiyonu before u argüman/parametre olarak alarak çağrılmalıdır