# 计数排序，时间复杂度为O(N)，用空间换时间
# 要排序数组a，创建存储数组b和辅助数组c，长度为max[a]-min[a]+1，遍历数组a，将a[index]-min[a]看成数组c的下标，来统计a中值的个数记录在c中，即c[a[index]-min[a]] += 1
# 最后对c数组进行累加，c[i] = c[i]+c[i-1]，所得c的值-1就是对应a值在b的最终位置


def CountingSort(arr):
    #检查入参类型
    if not isinstance(arr,(list)):
        raise TypeError('error para type')
    #获取arr中的最大值和最小值
    maxNum=max(arr)
    minNum=min(arr)
    #以最大值和最小值的差作为中间数组的长度,并构建中间数组，初始化为0
    length=maxNum-minNum+1
    tempArr=[0 for i in range(length)]
    #创建结果List，存放排序完成的结果
    resArr=list(range(len(arr)))
    #第一次循环遍历
    for num in arr:
        tempArr[num-minNum]+=1
    #第二次循环遍历
    for j in range(1,length):
        tempArr[j]=tempArr[j]+tempArr[j-1]
    #第三次循环遍历
    for i in range(len(arr)-1,-1,-1):
        resArr[tempArr[arr[i]-minNum]-1]=arr[i]
        tempArr[arr[i]-minNum]-=1
    return resArr


# arr = list(map(int, input().split()))
# countSort(arr[1:])
try:
	while True:
		num = list(map(int, input().split()))
		num = num[1:]
		num = CountingSort(num)
		count = 0
		for i in num:
			print(i, end=' ')
			count += 1
			if count == len(num):
				print(end='\n')
except EOFError:
	pass

