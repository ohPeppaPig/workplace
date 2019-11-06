# 冒泡
def bobo(num):
	for i in range(len(num)):
		for j in range(0, len(num) - i - 1):
			if num[j] > num[j + 1]:
				num[j], num[j + 1] = num[j + 1], num[j]


# while True:
#
# 	num = list(map(int, input().split()))
# 	num = num[1:]
# 	bobo(num)
# 	count = 0
# 	for i in num:
# 		print(i, end=' ')
# 		count += 1
# 		if count == len(num):
# 			print(end='\n')
# 	# while num is not None:
# 	# 	print()


try:
	while True:
		num = list(map(int, input().split()))
		num = num[1:]
		bobo(num)
		count = 0
		for i in num:
			print(i, end=' ')
			count += 1
			if count == len(num):
				print(end='\n')
except EOFError:
	pass
