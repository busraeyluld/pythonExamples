a = int(input("taban girin:"))
b = int(input("üs girin:"))
def ustel(a,b): #a taban b üs
    if b == 0:
        return 1
    else:
        return a*ustel(a,b-1)

print(ustel(a,b))