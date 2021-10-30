import math
p = int(input())
d = int(input())
s = int(input())
dfloor = math.floor(d / p)
dceil = math.ceil(d / p)
sfloor = math.floor(s / p)
sceil = math.ceil(s / p)
brsecenih=dceil*sceil-dfloor*sfloor
print(brsecenih)
p=d*s-dfloor*p*sfloor*p
print(p)