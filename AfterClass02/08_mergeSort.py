# import math
#
#
# def mergeSort(arr):
# 	if len(arr) < 2:
# 		return arr
# 	middle = math.floor(len(arr) / 2)  #取中
# 	left, right = arr[0:middle], arr[middle:] #分割数组left right
# 	return merge(mergeSort(left), mergeSort(right))
#
# def merge(left, right):
# 	result = [] #辅助数组
# 	while left and right: #比较两边数组元素
# 		if left[0] <= right[0]:
# 			result.append(left.pop(0))
# 		else:
# 			result.append(right.pop(0));
# 	while left:
# 		result.append(left.pop(0))
# 	while right:
# 		result.append(right.pop(0));
# 	return result

#非递归
def merge(seq, low, mid, high):
    left = seq[low: mid]
    right = seq[mid: high]
    k = 0
    j = 0
    result = []
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    result += left[k:]
    result += right[j:]
    seq[low: high] = result

def merge_sort(seq):
    i = 1 # i是步长
    while i < len(seq):
        low = 0
        while low < len(seq):
            mid = low + i #mid前后均为有序
            high = min(low+2*i,len(seq))
            if mid < high:
                merge(seq, low, mid, high)
            low += 2*i
        i *= 2

try:
	while True:
		num = list(map(int, input().split()))
		num = num[1:]
		merge_sort(num)
		count = 0
		for i in num:
			print(i, end=' ')
			count += 1
			if count == len(num):
				print(end='\n')
except EOFError:
	pass
