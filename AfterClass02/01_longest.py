# def longestCommonSequence(str_one, str_two, case_sensitive=True):
# 	"""
# 	str_one 和 str_two 的最长公共子序列
# 	:param str_one: 字符串1
# 	:param str_two: 字符串2（正确结果）
# 	:param case_sensitive: 比较时是否区分大小写，默认区分大小写
# 	:return: 最长公共子序列的长度
# 	"""
# 	len_str1 = len(str_one)
# 	len_str2 = len(str_two)
# 	# 定义一个列表来保存最长公共子序列的长度，并初始化
# 	record = [[0 for i in range(len_str2 + 1)] for j in range(len_str1 + 1)]
# 	for i in range(len_str1):
# 		for j in range(len_str2):
# 			if str_one[i] == str_two[j]:
# 				record[i + 1][j + 1] = record[i][j] + 1
# 			# elif record[i + 1][j] > record[i][j + 1]:
# 			#     record[i + 1][j + 1] = record[i + 1][j]
# 			# else:
# 			#     record[i + 1][j + 1] = record[i][j + 1]
# 			else:
# 				record[i + 1][j + 1] = max(record[i + 1][j], record[i][j + 1])
# 	return record[-1][-1]
#
#
# if __name__ == '__main__':
# 	# 字符串1
# 	s1 = "BDCABA"
# 	# 字符串2
# 	s2 = "ABCBDAB"
# 	# 计算最长公共子序列的长度
# 	res = longestCommonSequence(s1, s2)
# 	# 打印结果
# 	print(res)  # 4
#
# n = int(input())
# for x in range(n):
# 	arr1 = input()
# 	arr2 = input()
# 	LCS(arr1, arr2)

#---------------------------------------------------------------------------------------
# 最长公共子序列：给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


# 生成矩阵dp，dp最右下角的值代表最长公共子序列的长度
def getdp(str1, str2):
    dp = [[0] * len(str2) for x in range(len(str1))]
    dp[0][0] = 1 if str1[0] == str2[0] else 0 # 首元素相等
    for i in range(1, len(str1)): # str2首元素与str1各元素比较 确定dp行列边界值
        dp[i][0] = max(dp[i - 1][0], 1 if str1[i] == str2[0] else 0)
    for i in range(1, len(str2)): # str1首元素与str2各元素比较 确定dp行列边界值
        dp[0][i] = max(dp[0][i - 1], 1 if str1[0] == str2[i] else 0)
        # 正常的动态规划
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp #此处返回一个dp数组


# 通过dp求最长公共子序列
def lcse(str1, str2, l1, l2, dp, index, lcse_str, all):
    # index是最长公共子序列的长度；lcse_str存放正在遍历的子序列；all存放最终的最长公共子序列
    while index > 0:
        # 本题要输出全部的子序列所以当dp[l1][l2] == dp[l1][l2 - 1] and dp[l1][l2] == dp[l1 - 1][l2]
        # 需要递归的访问两个
        if l1 > 0 and l2 > 0 and dp[l1][l2] == dp[l1][l2 - 1] and dp[l1][l2] == dp[l1 - 1][l2]:
            # 必须先判断l1和l2大于0，否则列表可能越界到-1
            # 满足上面判断条件，这说明有两条路径，应分别进行求解
            lcse(str1, str2, l1 - 1, l2, dp, index, lcse_str, all)
            lcse(str1, str2, l1, l2 - 1, dp, index, lcse_str, all)
            return
        elif l1 > 0 and dp[l1][l2] == dp[l1 - 1][l2]:   # 上移
            l1 -= 1
        elif l2 > 0 and dp[l1][l2] == dp[l1][l2 - 1]:   # 左移
            l2 -= 1
        else:   # 不满足上面所有条件，说明dp[l1][l2]大于dp[l1-1][l2]和dp[l1][l2-1]，此时该点为公共点
            lcse_str = str1[l1] + lcse_str
            index -= 1
            l1 -= 1
            l2 -= 1
    all.add(lcse_str)   # 把公共子序列添加到all集合，使用集合可以避免重复


nums = int(input())
for n in range(nums):
    str1 = input()
    str2 = input()
    all_lcse = set() # 此处为set集合用于去重复
    dpMatrix = getdp(str1, str2)
    lcse(str1, str2, len(str1) - 1, len(str2) - 1, dpMatrix, dpMatrix[len(str1) - 1][len(str2) - 1], "", all_lcse)
    lis = []
    for i in all_lcse:  # 题目要求按字典顺序输出，则先把集合转化为列表，再进行排序后输出
        lis.append(i)
    lis.sort()
    for i in lis:
        print(i)


