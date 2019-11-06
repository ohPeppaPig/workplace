def countingSort(arr):  # the elements in the array are all integers
    maximum, minimum = max(arr), min(arr)
    countArr = [0] * (maximum - minimum + 1)
    for i in arr: # record the number of times of every element in the array
        countArr[i - minimum] += 1
    for i in range(1, len(countArr)): # calculate the position of every element
        countArr[i] += countArr[i-1]
    targetArr = [None] * len(arr)
    for i in range(len(arr)-1, -1, -1): # reverse-order traversal is for the stability
        countIndex = arr[i] - minimum
        targetArr[countArr[countIndex] - 1] = arr[i]
        countArr[countIndex] -= 1
    return targetArr





try:
	while True:
		num = list(map(int, input().split()))
		num = num[1:]
		num = countingSort(num)
		count = 0
		for i in num:
			print(i, end=' ')
			count += 1
			if count == len(num):
				print(end='\n')
except EOFError:
	pass
