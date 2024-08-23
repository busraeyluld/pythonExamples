import random
liste = ["python","print","random","while","choice"]
kelime = random.choice(liste)
adam = ['''
+---------+
 o        |
/|\       |
 /\       |
          |
        ---- ''','''
+---------+
 o        |
/|\       |
 /        |
          |
        ---- ''','''
+---------+
 o        |
/|\       |
          |
          |
        ---- ''','''
+---------+
 o        |
/|        |
          |
          |
        ---- ''','''
+---------+
 o        |
/         |
          |
          |
        ---- ''','''
+---------+
 o        |
          |
          |
          |
        ---- ''','''
+---------+
          |
          |
          |
          |
        ---- ,''']

dogru_harf = []  #dharf ve yharf için önce boş bir liste oluşturduk böylece kullanıcının girdiği harfleri bu listelere ekleyebilelim
yanlis_harf = []
hak = len(adam)  #adam asılana kadar kullanıcının tahmin hakkı var

while hak > 0: #burada oyun süresince gerçekleşecek eylemleri yazacağız çünkü kullanıcı hakkı sıfırlanmayana kadar
    out = ""
    for h in kelime:
        if h in dogru_harf: #kelimenin uzunluğu kadar tire oluşturacak, her doğru bilmede tirelerden biri silinecek yerine doğru bilinen harf konulacak
            out += h    #kullanıcı doğru harf tahmin ettiyse o harf konulacak
        else:
            out += "_" #kullanıcı yanlış tahmin ettiyse tire konulacak
    if out == kelime:   #doğru tahminse while döngüsünden çıkmak için
        break
    print("kelime: ", out)
    print(adam[hak - 1])    #her yanlış cevapta bir eksiğini çizdirir
    girilen_harf = input()
    if girilen_harf in dogru_harf or girilen_harf in yanlis_harf:
        print(girilen_harf, "zaten girildi")
    elif girilen_harf in kelime:
        print("doğru harf")
        dogru_harf.append(girilen_harf) #doğru harf listesine eekliyoruz
    else:
        print("yanlış harf")
        hak -= 1    #yanlış harf girdiği için hakkını bir azaltıyoruz
        yanlis_harf.append(girilen_harf) #yanlış harf listesine ekliyoruz

if hak != 0:
    print("tebrikler, kazandınız, kelimeniz:", kelime)
else:
    print("maalesef kaybettiniz, kelimeniz:", kelime, "idi")