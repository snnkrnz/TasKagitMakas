import random

secim = int(input("\nSeçimini yap \n1 = Taş\n2 = Kağıt\n3 = Makas\n"))

bot = int(random.choice("123"))

if secim < 1 or secim > 3:
    print("Hatalı giriş. 1, 2 veya 3'ü seçmelisin.")
elif secim == 1 and bot == 3:
    print("\nSeçimin: ", secim ,"\nBotun seçimi: ", bot ,"\nKAZANDIN!\n")
elif secim == 2 and bot == 1:
    print("\nSeçimin: ", secim ,"\nBotun seçimi: ", bot ,"\nKAZANDIN!\n")
elif secim == 3 and bot == 2:
    print("\nSeçimin: ", secim ,"\nBotun seçimi: ", bot ,"\nKAZANDIN!\n")
elif secim == bot:
    print("\nBerabere\n")
else:
    print("\nSeçimin: ", secim ,"\nBotun seçimi: ", bot ,"\nBOT KAZANDI!\n")
