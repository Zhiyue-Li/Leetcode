from . import ListNode
# Approach 1: Two pointers, reverse first half of the list, then compare
def isPalindrome(self, head: ListNode) -> bool:
    prev = None
    curr = head
    fast = head.next
    # Fast moves twice as curr, so curr is at half of the list when the loop terminate
    while fast and fast.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        fast = fast.next.next
    # Even number of nodes, loop one more time
    if fast:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # Odd number of nodes, move curr to next
    else:
        curr = curr.next
    while curr:
        if curr.val != prev.val:
            return False
        curr = curr.next
        prev = prev.next
    return True

# Approach 2: Store nodes' values in list, then compare list and reversed list
def isPalindrome(self, head: ListNode) -> bool:
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    return nodes == nodes[::-1]