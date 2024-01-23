print("vítejte v aplikaci pro výpočet obsahu kruhu")

r = input("zadej proměnu pro poloměr")

r = int(r)

if r>0:
    vysledek = 3.14*(r*r)
    print("vysledek je",vysledek)
else:
    print("nejde")