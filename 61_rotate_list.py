from . import ListNode
# Make list to circular, find the new head, then break the circle
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head:
        return None
    l = 1
    curr = head
    while curr.next:
        l += 1
        curr = curr.next
    curr.next = head
    for _ in range(l - k % l - 1):
        head = head.next
    res = head.next
    head.next = None
    return res