s=int(input())
d=int(input())
c=(d-s)/4
if(c*10)%10==0:
    print("da")
if(c*10)%10>0:
    print("ne")

#resenje 2
s=int(input())
d=int(input())
if(d-s)%4==0:
    print("DA")
else:
    print("NE")