num = int(input())
for x in range(num):
	a,b,c = map(int,input().split())
	s =1
	while b!=1:
		if b%2==1:
			s = s*a
			s = s%c
			b-=1
		else:
			a = a*a
			a = a%c
			b = b/2
	print((s*a)%c)

