print("vítejte v aplikaci pro výpočet obvodu obdelníku")

a = input("zadejte proměnu a:")
b = input("zadejte proměnu b:")

a = int(a)
b = int(b)

if a>0 and b>0:
    vysledek = a*2+b*2
    print("vysledek je", vysledek)
else:
    print("nejde")