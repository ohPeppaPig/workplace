# hanoi（N）= 3* hanoi(N-1) +2

def hanoi(num):
	if num == 1:
		return 2
	else:return 3* hanoi(num-1) +2


num = int(input())
for x in range(num):
	n = int(input())
	result = hanoi(n)
	print(result)