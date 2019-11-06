# 将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。
# 方法一：利用栈结构，时间复杂度为O(N),空间复杂度为O(K)
# 方法二：不用栈结构，在原链表上进行调整，用变量记录每一组开始的第一个节点和最后一个节点，然后逆序调整，同时注意对第一组节点的特殊处理，因为要改变头结点


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverseKNode(head, k):
    if k < 2:
        return head
    cur = head
    start = None  # 记录即将逆序的这组的开头（逆序后为最后一个）
    pre = None  # 记录上一组的结尾
    nextNode = None  # 记录正在遍历的下一个
    count = 1
    while cur is not None:
        nextNode = cur.next
        if count == k:
            start = head if pre is None else pre.next
            head = cur if pre is None else head   # 逆序第一组时要换头结点
            reverse(pre, start, cur, nextNode)  # 逆序
            pre = start
            count = 0
        count += 1
        cur = nextNode
    return head


def reverse(left, start, end, right):
    pre = start
    cur = start.next
    nextNo = None
    while cur != right:
        nextNo = cur.next
        cur.next = pre
        pre = cur
        cur = nextNo
    if left is not None:    # 连接上一组
        left.next = end
    start.next = right  # 连接下一组


nums = int(input())
for n in range(nums):
    arr = list(input().split())
    leng = int(arr[0])
    k = int(arr[-1])
    head = Node(arr[1], None)
    cur = head
    for i in range(2, len(arr) - 1):    # 构建链表
        tem = Node(arr[i], None)
        cur.next = tem
        cur = tem
    head = reverseKNode(head, k)
    cur = head
    while cur is not None:
        if cur.next is not None:
            print(cur.value, end=' ')
        else:
            print(cur.value)
        cur = cur.next

