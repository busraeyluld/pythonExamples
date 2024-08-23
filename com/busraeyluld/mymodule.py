def greet(name):
    return print("hello", name)
#oluşturduğumuz bu metot başka bir programda import edilerek kullanılabilir.
#şimdi aynı şekilde import etmek üzere bir metot tanımlayıp modules.py uzantılı dosyada bu metodu import edip kullanalım
def dikdortgen_alani():
    u = int(input("dikdörtgenin uzun kenarını girin.."))
    k = int(input("dikdörtgenin kısa kenarını girin.."))

    return print("dikdörtgenin alanı:",k * u, "cm2")

