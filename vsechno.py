print("vítejte v aplikaci pro výpočet vzorečků obdelníku/kvádru")

print("Pro výpočet objemu zadejte 1.")
print("Pro výpočet obvodu zadejte 2.")
print("Pro výpočet obashu zadejte 3.")
print("pro ukončení zadejte 4.")

volba = input("Zadejte vaši volbu: ")

if volba == "1":
     a = int(input("Zadejte stranu a: "))
     b = int(input("Zadejte stranu b: "))
     c = int(input("Zadejte stranu c: "))

     if a>0 and b>0 and c>0:
          výsledek = a*b*c
          print("Objem kvádru je: ", výsledek, " litrů")
     else:
          print("co to delas")
elif volba == "2":
     a = int(input("Zadejte stranu a: "))
     b = int(input("Zadejte stranu b: "))

     if a>0 and b>0:
          výsledek = 2*a+2*b
          print("oobvod obdelníku je:", výsledek, " cm")
     else:
        print("co to delas")
elif volba == "3":
     a = int(input("Zadejte stranu a: "))
     b = int(input("Zadejte stranu b: "))
     if a>0 and b>0:
          výsledek = a*b
          print("obsah obdelníku je:", výsledek, " m2")
     else:
          print("co delas kamo")
