def solution(a1,a2):
	len1 = len(a1)
	len2 = len(a2)
	res = []
	for i in range(len2):
		ret = 0
		for j in range(len1):
			if a1[j]%a2[i]==0:
				ret+=1
		res.append(ret)
	return res


num = int(input())
for i in range(num):
	a,b=map(int,input().split())
	a1 = list(map(int,input().split()))
	a2 = list(map(int,input().split()))
	res = solution(a1,a2)
	# count = 0
# 	# for j in res:
# 	# 	if j != res[-1]:
# 	# 		print(j, end=' ')
# 	# 	# count += 1
# 	# 	# if count == len(res):
# 	# 	else:
# 	# 		print(j)
# 	# 		# print(end='\n')
	for j in range(len(res)):
		if j != len(res)-1:
			print(res[j],end=' ')
		else:
			print(res[j])
