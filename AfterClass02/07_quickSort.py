# 递归
# def quick_sort(array, left, right):
# 	if left >= right:
# 		return
# 	low = left
# 	high = right
# 	key = array[low]
# 	while left < right:
# 		while left < right and array[right] > key:
# 			right -= 1
# 		array[left] = array[right]
# 		while left < right and array[left] <= key:
# 			left += 1
# 		array[right] = array[left]
# 	array[right] = key
# 	quick_sort(array, low, left - 1)
# 	quick_sort(array, left + 1, high)
#
def qsort(arr):
	if len(arr)<2:
		return arr
	else:
		p = arr[0]
		more = [i for i in arr[1:] if i>=p]
		less = [i for i in arr[1:] if i<p]
		return qsort(less)+[p]+qsort(more)


arr = [1,3,2,4,5]
print(qsort(arr))
# 非递归

def quick_sort_other(array, l, r):
    '''
    算法导论里的思想
    i表示[l,i]都比pivot小
    j依次遍历元素
    '''
    if l >= r:
        return
    stack = [l,r]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high <= low:
            continue
        pivot = array[high]
        i = low - 1 ###初始值是-1
        for j in range(low,high+1):
            ###如果小于pivot， 则交换，交换的目的是保证[l,i]都比pivot小
            if array[j] <= pivot:
                i += 1
                t = array[i]
                array[i] = array[j]
                array[j] = t
        stack.extend([low, i-1, i + 1, high])
    return array

try:
	while True:
		num = list(map(int, input().split()))
		num = num[1:]
		num = quick_sort_other(num,0,len(num)-1)
		count = 0
		for i in num:
			print(i, end=' ')
			count += 1
			if count == len(num):
				print(end='\n')
except EOFError:
	pass
#-------------------------------------------------------------------
#递归
# def quick_sort(L):
#     return q_sort(L, 0, len(L) - 1)
#
# def q_sort(L, left, right):
#     if left < right:
#         pivot = Partition(L, left, right)
#
#         q_sort(L, left, pivot - 1)
#         q_sort(L, pivot + 1, right)
#     return L
#
# def Partition(L, left, right):
#     pivotkey = L[left]
#
#     while left < right:
#         while left < right and L[right] >= pivotkey:
#             right -= 1
#         L[left] = L[right]
#         while left < right and L[left] <= pivotkey:
#             left += 1
#         L[right] = L[left]
#
#     L[left] = pivotkey
#     return left
#
# L = [5, 9, 1, 11, 6, 7, 2, 4]
#
# arr = [1, 3, 5, 4, 2]
# quick_sort(arr, 0, 4)
# print(arr)
