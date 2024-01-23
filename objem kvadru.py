print("vítejte v aplikaci pro výpočet objemu kvádru")
a = input("zadejte proměnu a:")
b = input("zadejte proměnu b:")
c = input("zadejte proměnu c:")

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0 and c>0:
    vysledek = a*b*c
    print("vysledek je", vysledek)
else: 
    print("nelze")