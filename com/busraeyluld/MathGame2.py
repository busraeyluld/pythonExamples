import random
print("10 soruluk mtematik testine hoşgeldiniz..")
skor = 0
for a in range(10):
    i = random.randint(1,10) #
    x = random.randint(1,10) #iki sayının çarpımı için olan değişken
    soru = "{} * {} =".format(i,x)

    dogru_cevap = i * x
    kullanici_cevap = input(soru)


    if int (kullanici_cevap == dogru_cevap):
        skor += 1

print("doğru cevap sayısı:", dogru_cevap)

if skor > 8:
    print("pekiyi")
elif skor > 6:
    print("iyi")
elif skor > 4:
    print("orta")
else:
    print("daha çok çalış")