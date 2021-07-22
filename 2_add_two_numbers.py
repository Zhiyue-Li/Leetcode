from . import ListNode
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    i = 0
    res = ListNode(0)
    p = res
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        s = i + v1 + v2
        i = s // 10
        p.next = ListNode(s % 10)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        p = p.next
    if i:
        p.next = ListNode(i)
    return res.next