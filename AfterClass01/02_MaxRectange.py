def solution(heights):
	res = 0
	n = len(heights)
	for i in range(n):
		left_i = i
		right_i = i
		while left_i >= 0 and heights[left_i] >= heights[i]:
			left_i -= 1
		while right_i < n and heights[right_i] >= heights[i]:
			right_i += 1
		res = max(res, (right_i - left_i - 1) * heights[i])
	return res

# def maxRecFromBottom(height):
#     stack = []
#     maxArea = 0
#     for n in range(len(height)):
#         while len(stack) and height[n] <= height[stack[-1]]:
#             m = stack.pop()
#             if len(stack) == 0:
#                 k = -1
#             else:
#                 k = stack[-1]
#             curArea = (n - k - 1) * height[m]
#             maxArea = max(maxArea, curArea)
#         stack.append(n)
#     # 结算栈中剩余的
#     while len(stack):
#         m = stack.pop()
#         if len(stack) == 0:
#             k = -1
#         else:
#             k = stack[-1]
#         curArea = (len(height) - k - 1) * height[m]
#         maxArea = max(maxArea, curArea)
#     return maxArea

nums = int(input())
for i in range(nums):
    a, b = map(int, input().split())
    maxArea = 0
    lis = []
    for j in range(a):
        lis.append(list(map(int, input().split())))  # 构建矩阵二维列表
    height = [0 for x in range(b)]
    # 遍历矩阵，求出列高度
    for j in range(a):
        for k in range(b):
            if lis[j][k] == 0:
                height[k] = 0
            else:
                height[k] += 1
        maxArea = max(solution(height), maxArea)  # 每求出一行高度，就比较一次
    print(maxArea)
