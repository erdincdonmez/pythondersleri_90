meyveler = ["Elma","Muz","Nar","Dut"]
çorbalar = ["Tarhana","Mercimek","Yayla"]

print(meyveler)
print(*meyveler)
print(*meyveler, sep = ",")
print(*meyveler, sep = "\n")

print("Van","Muş","Çan","Bor")
print("Van","Muş","Çan","Bor",sep=" ")
print("Van","Muş","Çan","Bor",sep="-")

print("Van","Muş","Çan","Bor", end="")
print("Van","Muş","Çan","Bor",sep="-", end="")
print("şehirler")

# end parametresi print ile yazdıktan sonra ne yapılacağını belirtir.
# sep seperate parametresi print ile birden çok ifade arasında nelerin olacağını ifade eder.