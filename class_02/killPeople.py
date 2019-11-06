def kill(s):
	i = 1
	sum = 0
	while True:
		cur = i*i
		if cur+sum>s:
			return i-1
		else:
			sum+=cur
			i+=1

num = int(input())
for x in range(num):
	s = int(input())
	result=kill(s)
	print(result)