def insertSort(num):
	lenth = len(num)
	for i in range(1, lenth):
		key = num[i]
		j = i - 1
		while j >= 0 and key < num[j]:
			num[j + 1] = num[j]
			j -= 1
		num[j + 1] = key


# n = int(input())
# for x in range(n):
# 	num = list(map(int, input().split()))
# 	num = num[1:]
# 	insertSort(num)
# 	count = 0
# 	for i in num:
# 		print(i, end=' ')
# 		count += 1
# 		if count == len(num):
# 			print(end='\n')

	# print(" ".join(str(num)))


try:
	while True:
		n = int(input())
		for x in range(n):
			num = list(map(int, input().split()))
			num = num[1:]
			insertSort(num)
			count = 0
			for i in num:
				print(i, end=' ')
				count += 1
				if count == len(num):
					print(end='\n')

except EOFError:
	pass
