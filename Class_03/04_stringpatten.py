# a  = input().split(',')
# res=a[0].index(a[1])
# print(res)

# def solution(a1,a2):
# 	return a1.index(a2)
#
#
#
#
# num = int(input())
# for i in range(num):
# 	a = input().split(',')
# 	res = solution(a[0],a[1])
# 	print(res)
# Python3 program for Naive Pattern
# Searching algorithm
def search(pat, txt):
	M = len(pat)
	N = len(txt)
	res = []
	# A loop to slide pat[] one by one */
	for i in range(N - M + 1):
		j = 0

		# For current index i, check
		# for pattern match */
		while (j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1

		if (j == M):
			# print(i)
			res.append(i)
	# Driver Code
	return res


num = int(input())
for i in range(num):
	a = input().split(',')
	res = search(a[1], a[0])
	# print(res)
	for j in range(len(res)):
		if j != len(res) - 1:
			print(res[j], end=' ')
		else:
			print(res[j])
