import time
import random

while True:
    decision = input("Akarod használni a jelszó generátort? y/n ")
    if decision == 'y':
        length = int(input("Jelszó hosszúsága: "))
        print("Gábor Generálja a jelszavat...")
        s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p = ''
        for i in range(0, length, 1):
            p += s[random.randint(0, len(s))]
        time.sleep(3)
        print(p)
    else:
        break
