salesperson = ["jack", "jim", "rachel", "dave", "jenny"] #çalışan listesi
salesperson_revenue = {} # her çalışanın getirdiği kazancı tutan ve içine değer eklenecek boş sözlük
def enter_revenue(salesperson_name,revenue):  #kazançları kaydeden fonksiyon
    salesperson_revenue[salesperson_name] = revenue #çalışan ismine göre kazancı ekleme veya güncelleme
    print(salesperson_revenue)#güncel sözlüğü ekrana yazdır

enter_revenue("jack", 500)#jack isimli çalışanın getirdiği kazancı ekleme
enter_revenue("dave", 50)
print("güncel liste: ", salesperson_revenue)


#burada kullanıcı tarafından girilen çalışanın getirdiği kazancı almak için

while True:
    employee_name = input("çalışan adını girin..(çıkmak için'quit' yazın)..")
    if employee_name in salesperson:
        revenue = float(input("bu isim için kazancı girin.."))
        salesperson_revenue[employee_name] = revenue
        print("güncel liste: ", salesperson_revenue)

    if employee_name not in salesperson:
        print("isim bulunamadı, başka bir çalışanın ismini girin..")

    if employee_name == "quit":
        print("programdan çıkılıyor..")
        break
