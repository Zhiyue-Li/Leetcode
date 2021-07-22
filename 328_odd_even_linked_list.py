from . import ListNode
def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return head
    odd = head
    even = head.next
    evenHead = even
    while even and even.next:
        odd.next = even.next
        even.next = odd.next.next
        odd = odd.next
        even = even.next
    odd.next = evenHead
    return head