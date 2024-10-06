#print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
#print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║   HESAP MAKİNESİ    ║"); print("║                     ║")
print("║  1-Toplama          ║"); print("║  1-Çarpma           ║")
print("║  1-Çıkarma          ║")
print("║  1-Bölme            ║")
print("║  3-üst alma         ║")
print("║  4-                 ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

secim = input() # input ile string veri alınır.
#secim = int(input()) # input ile alınanı integera(tamsayı) çevirme

print(secim,"seçtiniz.")
if secim == "1" :
    print("1 seçtiniz, toplama yapılacak.")
if secim == "2" :
    print("2 seçtiniz, çarpma yapılacak.")

"""
Bu gün yapacaklarımız:
    - maça gitcez
    - film izlicez

Alınacaklar:
    Makarna
    Soğan
"""
