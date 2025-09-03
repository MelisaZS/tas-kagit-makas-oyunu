# -*- coding: utf-8 -*-

import tkinter as tk
import random
from tkinter import messagebox

# Puanlar
oyuncu_puan = 0
bilgisayar_puan = 0

def oyna(secim):
    global oyuncu_puan, bilgisayar_puan
    
    secenekler = ["Taş", "Kağıt", "Makas"]
    bilgisayar = random.choice(secenekler)
    
    if secim == bilgisayar:
        sonuc = "Berabere!"
    elif (secim == "Taş" and bilgisayar == "Makas") or \
         (secim == "Kağıt" and bilgisayar == "Taş") or \
         (secim == "Makas" and bilgisayar == "Kağıt"):
        sonuc = "Kazandın! 🎉"
        oyuncu_puan += 1
    else:
        sonuc = "Kaybettin 😢"
        bilgisayar_puan += 1
    
    # Ekranı güncelle
    etiket_bilgisayar.config(text=f"Bilgisayarın seçimi: {bilgisayar}")
    etiket_sonuc.config(text=sonuc)
    etiket_puan.config(text=f"Sen: {oyuncu_puan}  |  Bilgisayar: {bilgisayar_puan}")
    
    # 5 puana ulaşan kazanır
    if oyuncu_puan == 5 or bilgisayar_puan == 5:
        kazanan = "Sen kazandın! 🏆" if oyuncu_puan == 5 else "Bilgisayar kazandı! 🤖"
        messagebox.showinfo("Oyun Bitti", kazanan)
        resetle()

def resetle():
    global oyuncu_puan, bilgisayar_puan
    oyuncu_puan = 0
    bilgisayar_puan = 0
    etiket_bilgisayar.config(text="Bilgisayarın seçimi: -")
    etiket_sonuc.config(text="Sonuç: -")
    etiket_puan.config(text="Sen: 0  |  Bilgisayar: 0")

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Taş Kağıt Makas Oyunu")
pencere.geometry("450x450")
pencere.config(bg="#ececec")

# Başlık
etiket_baslik = tk.Label(
    pencere, text="🎮 Taş Kağıt Makas 🎮", 
    font=("Arial", 20, "bold"), bg="#ececec", fg="darkblue"
)
etiket_baslik.pack(pady=15)

# Puan tablosu
etiket_puan = tk.Label(
    pencere, text="Sen: 0  |  Bilgisayar: 0", 
    font=("Arial", 14, "bold"), bg="#ececec"
)
etiket_puan.pack(pady=10)

# Bilgisayar seçimi
etiket_bilgisayar = tk.Label(
    pencere, text="Bilgisayarın seçimi: -", 
    font=("Arial", 12), bg="#ececec"
)
etiket_bilgisayar.pack(pady=10)

# Sonuç
etiket_sonuc = tk.Label(
    pencere, text="Sonuç: -", 
    font=("Arial", 16, "bold"), fg="blue", bg="#ececec"
)
etiket_sonuc.pack(pady=10)

# Butonlar
frame = tk.Frame(pencere, bg="#ececec")
frame.pack(pady=30)

buton_tas = tk.Button(
    frame, text="✊ Taş", width=12, height=2, bg="lightgrey", 
    font=("Arial", 12, "bold"), command=lambda: oyna("Taş")
)
buton_tas.grid(row=0, column=0, padx=15)

buton_kagit = tk.Button(
    frame, text="✋ Kağıt", width=12, height=2, bg="lightblue", 
    font=("Arial", 12, "bold"), command=lambda: oyna("Kağıt")
)
buton_kagit.grid(row=0, column=1, padx=15)

buton_makas = tk.Button(
    frame, text="✌️ Makas", width=12, height=2, bg="lightcoral", 
    font=("Arial", 12, "bold"), command=lambda: oyna("Makas")
)
buton_makas.grid(row=0, column=2, padx=15)

# Reset butonu
buton_reset = tk.Button(
    pencere, text="🔄 Oyunu Sıfırla", width=18, height=2, bg="orange", 
    font=("Arial", 11, "bold"), command=resetle
)
buton_reset.pack(pady=20)

# Pencereyi çalıştır
pencere.mainloop()

