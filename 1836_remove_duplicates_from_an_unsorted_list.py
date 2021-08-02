from . import ListNode
from collections import defaultdict
# Store all node values in a counter
# Loop through the counter, create nodes using value count == 1, link nodes together
def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
    d = defaultdict(int)
    while head:
        d[head.val] += 1
        head = head.next
    dummy = ListNode(0, None)
    curr = dummy
    for n, c in d.items():
        if c == 1:
            node = ListNode(n, None)
            curr.next = node
            curr = curr.next
    return dummy.next