from . import ListNode
def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head