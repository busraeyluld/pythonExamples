#parametresiz bir fonksiyonun hata vermemesi için pass kelimesini kullanabiliriz
#ve kod boyunca sonradan tanımlayabiliriz
#veya return kısmını boş bırakabiliriz. Bu durumlarda çıktımız none olur
def topla(num_1,num_2):
    return num_1 + num_2
def carp():
    pass
def bol():
    pass
def cikar():
    pass


def carp():
    return
def bol():
    return
def cikar():
    return

num_1 = 7
num_2 = 9
print(topla(num_1,num_2))
print(carp())
print(bol())
print(cikar())
