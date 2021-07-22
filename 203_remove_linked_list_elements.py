from . import ListNode
def removeElements(self, head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
        else:
            p = p.next
    return dummy.next