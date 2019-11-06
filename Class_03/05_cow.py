def solution(n):
	if n==1:
		return 1
	if n==2:
		return 2
	else:
		return solution(n-1)%(pow(10,9)+7)+solution(n-2)%(pow(10,9)+7)
# def Fibonacci(n):
#     #初始列表
#     res = [0,1,2]
#     #临界条件：列表长度最大为n
#     while len(res)<=n:
#         res.append(res[-1]+res[-2]) #依次计算末尾两个数的和加入列表
#     return res[n]%(pow(10,9)+7)



num = int(input())
for i in range(num):
	n = int(input())
	res = solution(n)
	print(res)