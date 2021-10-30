p = int(input())
d = int(input())
s = int(input())
dfloor = d // p
dceil = (d + p - 1) // p
sfloor = s // p
sceil = (s + p - 1) // p
# dceil*sceil - minimalni broj plocica koje pokrivaju oblast
# dfloor*sfloor - maksimalni broj plocica koje su sadrzane u oblasti
brojSecenihPlocica = (dceil * sceil) - (dfloor * sfloor)
povrsinaPokrivenaSecenimPlocicama = (d*s) - (dfloor*p*sfloor*p)
print(brojSecenihPlocica)
print(povrsinaPokrivenaSecenimPlocicama)
