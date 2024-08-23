#önce metotlarımızı tanımlarız
def go_for_a_walk():
    print("go out")
def find_fine_restaurant():
    print("find a good restaurant and have a lunch")
    return True
def eat_sandvich():
    print("eat a sandvich")
def go_theatre():
    print("buy a ticket")
    return True
def go_shopping():
    print("buy something")
#sonra değişkenimizi tanımlarız, kullanıcıdan(bir cihaz örn) gelen termometre değeri
the_weather = float(input("thermometer: "))
#şimdi koşullarımızı oluşturabiliriz
if the_weather >= 25:
    go_for_a_walk()
    if find_fine_restaurant():
      print("have lunch")
    else:
        eat_sandvich()
else:
    if True:
        go_theatre()
        print("watch it")
    else:
        go_shopping()

    def selamlama(isim):
            print("Sayın",isim,"restoranımıza hoşgeldiniz")
            while True:
                ad=input("adınızı girin:")
                if (ad=="dur"):
                    break
                    selamlama(ad)

