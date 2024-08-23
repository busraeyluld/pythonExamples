#generic import
# math adında, pek çok değişken ve fonsiyon içeren bir python modülü vardır. Bu modüle veya başka modüllere
#erişmek için import keyword kullanılır.
import math
print(math.sqrt(36))
print(math.factorial(5))
from math import sqrt   #burada sadece sqrt fonksiyonunu import ettik bu yüzden math. ifadesine gerek yok
print(sqrt(25))
from math import factorial  #burada sadece factorial fonksiyonunu import ettik bu yüzden math. ifadesine gerek yok
print(factorial(4))

#universal import
#bir modüldeki tüm fonksiyon ve değişkenlere erişmek için
#everything = dir(math)  #bir nesnenin veya modülün içindeki niteliklerin (değişkenler, fonksiyonlar, sınıflar vb.) bir listesini döndürmek için kullanılır.
#print(everything)
#maximum adında bir liste oluşturalım
maximum = [1,4,5,7,2]
print(max(maximum))
print(min(maximum))
figures = [-42,25,144,32]
print(abs(figures[0]))
print(sqrt(figures[2]))

print(type("hi everyone"))
print(type(6.2))
print(type(23435425))

import mymodule
print(mymodule.greet("busra"))

