#0'dan 10'a kadar sayıp tek sayıları ekrana yazdıran while döngüsü yaratın
x = 0
while x < 11:
    x += 1
    if x % 2 == 0:
        print("çift sayılar: ", x)

#Program, bir e-posta adresindeki karakterleri dolaşsın, @ sembolüne ulaştığında döngüden çıksın
#ve tek satırda olacak şekilde @ sembolünden önceki parçayı yazdırsın
for character in "john.smith@pythoninstitute.org":

    print(character, end="")
    if character == "@":
        break

#Program rakam karakter dizisi üzerinde iterasyon yapıp, her 0 karakterini x ile değiştirsin
#ve değiştirilmiş karakter dizisini ekrana yazdırsın
for digit in "0165031806510":
    if digit == "0":
        new = digit.replace("0", "x")
        print(new, end="")
