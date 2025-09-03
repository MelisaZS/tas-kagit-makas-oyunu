# -*- coding: utf-8 -*-

import random

# Puanlar
oyuncu_puan = 0
bilgisayar_puan = 0

print("🎮 Taş Kağıt Makas Oyununa Hoşgeldiniz! 🎮")
print("İlk 5 puana ulaşan taraf kazanır.")
print("-"*40)

while oyuncu_puan < 5 and bilgisayar_puan < 5:
    oyuncu = input("Taş, Kağıt, Makas seç: ").lower()
    
    # Geçersiz giriş kontrolü
    if oyuncu not in ["taş", "kağıt", "makas"]:
        print("Geçersiz seçim! Lütfen 'taş', 'kağıt' veya 'makas' yaz.")
        continue

    bilgisayar = random.choice(["taş", "kağıt", "makas"])
    print(f"Bilgisayarın seçimi: {bilgisayar}")

    # Sonucu belirle
    if oyuncu == bilgisayar:
        print("Berabere!")
    elif (oyuncu == "taş" and bilgisayar == "makas") or \
         (oyuncu == "kağıt" and bilgisayar == "taş") or \
         (oyuncu == "makas" and bilgisayar == "kağıt"):
        print("Kazandın! 🎉")
        oyuncu_puan += 1
    else:
        print("Kaybettin 😢")
        bilgisayar_puan += 1

    # Skor tablosu
    print(f"Skor: Sen {oyuncu_puan} - {bilgisayar_puan} Bilgisayar")
    print("-"*40)

# Oyun sonucu
if oyuncu_puan == 5:
    print("🏆 TEBRİKLER! Oyunu kazandın! 🏆")
else:
    print("🤖 Bilgisayar oyunu kazandı!")

