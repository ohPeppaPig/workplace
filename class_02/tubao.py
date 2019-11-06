def outerTrees(points):
	n = len(points)
	if n < 3: return points
	pts = sorted(set(points), key=lambda a: (a.x, a.y))

	cross = lambda o, a, b: (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

	low = []
	for p in pts:
		while len(low) > 1 and cross(low[-2], low[-1], p) < 0:
			low.pop()
		low.append(p)

	up = []
	for p in reversed(pts):
		while len(up) > 1 and cross(up[-2], up[-1], p) < 0:
			up.pop()
		up.append(p)

	return list(set(low[:-1] + up[:-1]))

num = int(input())
for x in range(num):
	a = int(input())
	lis = [[0 for i in range(2)]for j in range(a)]
	arr = list(map(int,input().split()))
	for i in range(a):
		for j in range(2):
			lis[i][j] = arr[i+j]

	result = outerTrees(lis)
	print(result)