# 判断一个链表是否为回文结构，时间复杂度为O(N),空间复杂度为O（1）

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def isPalindromel(head):
    if head is None or head.next is None:
        return True
    n1 = head
    n2 = head
    while n2.next is not None and n2.next.next is not None:  # 查找中间节点
        n1 = n1.next    # n1 ->中点
        n2 = n2.next.next   # n2->尾部
    n2 = n1.next     # n2->右边第一个节点
    n1.next = None
    while n2 is not None:   # 反转右半区
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    n3 = n1   # 保存最后一个节点，待会还原时需要
    n2 = head   # n2->左边第一个节点
    res = True
    while n1 is not None and n2 is not None:    # 检查回文
        if n1.value != n2.value:
            res = False
            break
        n1 = n1.next    # 左边到中部
        n2 = n2.next    # 右边到中部
    n1 = n3.next    # n1->右部倒数第二个节点
    n3.next = None
    while n1 is not None:   # 恢复链表
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2
    return res


nums = int(input())
for n in range(nums):
    arr = list(input().split())
    head = Node(arr[1], None)
    cur = head
    for i in range(2, len(arr)):
        tem = Node(arr[i], None)
        cur.next = tem
        cur = tem
    # print("true" if isPalindromel(head) is True else "false")
    print(isPalindromel(head))
