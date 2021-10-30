x=int(input())
h=x//1000
s=(x//100)%10
d=(x//10)%10
j=x%10
najveci=max(h,s,d,j)
najmanji=min(h,s,d,j)
s1=h+s+d+j-najveci-najmanji
print(s1)

