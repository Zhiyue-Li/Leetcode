from . import ListNode
def reverseList(self, head: ListNode) -> ListNode:
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    head = prev_node
    return head