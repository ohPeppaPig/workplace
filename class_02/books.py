def copyBooks( pages, k):
	# write your code here
	if pages == None or len(pages) == 0:
		return 0
	start, end = max(pages), sum(pages)
	while start + 1 < end:
		mid = (start + end) // 2
		if getCopyer(pages, mid) > k:
			start = mid
		else:
			end = mid
	if getCopyer(pages, start) <= k:
		return start
	else:
		return end

def getCopyer(pages, limit):
	copyer, sumVal = 1, 0
	for i in pages:
		if sumVal + i > limit:
			copyer += 1
			sumVal = 0
		sumVal += i
	return copyer

num = int(input())
for x in range(num):
	s = int(input())
	arr = list(map(int,input().split()))
	a = int(input())
	result = copyBooks(arr,a)
	print(result)