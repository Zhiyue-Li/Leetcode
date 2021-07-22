from . import ListNode
# Store nodes in array
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    nodes = [dummy]
    while head is not None:
        nodes.append(head)
        head = head.next
    nodes[-n-1].next = nodes[-n].next
    return dummy.next

# Two pointers, n steps between two pointers
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pt = dummy
    for _ in range(n):
        head = head.next
    while head is not None:
        pt = pt.next
        head = head.next
    pt.next = pt.next.next
    return dummy.next