import random

class MathGame1:
    def _init_(self):
        self.correct_answer = 0

    def play(self):
        while True:
            sayi1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            sayi2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            print(f"{sayi1} x {sayi2} = ?")
            result = int(input("Çarpım sonucunu girin: "))

            if result == -1:
                break

            if result == (sayi1 * sayi2):
                self.correct_answer += 1
                print("Doğru!")
            else:
                print(f"Yanlış! Doğru cevap: {sayi1 * sayi2}")

        # Oyun sona erdikten sonra sonuçlara değerlendirin
        if self.correct_answer >= 8:
            print("Pekiyi")
        elif self.correct_answer >= 6:
            print("İyi")
        elif self.correct_answer >= 4:
            print("Orta")
        else:
            print("Zayıf")

# Oyunu başlat
game = MathGame1()
game.play()