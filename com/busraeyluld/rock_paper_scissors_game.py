import random

options_for_pc = ["taş", "kağıt", "makas"]
pc_choice = random.choice(options_for_pc)  # pc seçimi için

while True:
    user_choice = input("taş, kağıt veya makas seçeneklerinden birini seç: ")
    print("bilgisayarın seçimi: ", pc_choice)
    print("seçiminiz: ", user_choice)
    if pc_choice == user_choice:
        print("yeniden seçim yapınız")
        continue
        pc_choice = random.choice(options_for_pc)

    elif pc_choice == "taş" and user_choice == "makas":
        print("taş makası ezer, kazanan PC!")
    elif pc_choice == "taş" and user_choice == "kağıt":
        print("kağıt taşı sarar, kazanan sensin!")
    elif pc_choice == "kağıt" and user_choice == "makas":
        print("makas kağıdı keser, kazanan sensin!")
    elif pc_choice == "kağıt" and user_choice == "taş":
        print("kağıt taşı sarar, kazanan PC!")
    elif pc_choice == "makas" and user_choice == "kağıt":
        print("makas kağıdı keser, kazanan PC!")
    elif pc_choice == "makas" and user_choice == "taş":
        print("taş makası ezer, kazanan sensin!")
    else:
     print("lütfen geçerli seçim yapın")
    break



