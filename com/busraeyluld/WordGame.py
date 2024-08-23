import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
user_due = 3 #kullanıcının oyunda 3 tahmin hakkını tanımladık
word_length = 6 #pcnin oluşturduğu kelimenin 6 harfli olmasını istiyoruz.
pc_word = "".join(random.choice(letters) for i in range(word_length)) #burada join() metodunu kullanarak letters listesindeki harflerle 6 harfli rastgele kelime oluşturduk

while True:
    user_guess = input("ingilizce karakterde bir harf söyleyin") #kullanıcıdan harf tahmin etmesini istedik
    if user_guess not in pc_word: #eğer kullanıcının tahmin ettiği harf pcnin oluşturduğu kelimenin içinde yoksa
        user_due -= 1 #kullanıcının hakkı 1 azalıyor
        print("kalan hakkınız:", user_due)

    if user_due == 0: #eğer kullanıcının hakkı biterse
        print("oyun sona erdi, bilemediniz")
        print("bilgisayarın seçtiği kelime:", pc_word)
        break #oyundan çıkılıyor
    if user_guess in pc_word: #eğer kullanıcı doğru tahminde bulunursa
        print("bildiniz..")
        print("bilgisayarın seçtiği kelime:", pc_word)
        break #yine döngüden oyundan çıkılıyor





