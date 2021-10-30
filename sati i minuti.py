from typing import MutableMapping


sat1=int(input())
min1=int(input())
sat2=int(input())
min2=int(input())
minz1=sat1*60+min1
minz2=sat2*60+min2

mmax=max(minz1, minz2)
mmin=min(minz1, minz2)

vreme=(mmax-mmin)
s=vreme//60
m=vreme%60
print(s, m)
