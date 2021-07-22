from . import Node
def insert(self, head: 'Node', insertVal: int) -> 'Node':
    if head is None:
        head = Node(insertVal, None)
        head.next = head
        return head
        
    prev, curr = head, head.next
        
    while True:
        if prev.val <= insertVal <= curr.val:
            break
        elif prev.val > curr.val:
            if insertVal >= prev.val or insertVal <= curr.val:
                break
        prev, curr = prev.next, curr.next
        if prev == head:
            break
    prev.next = Node(insertVal, curr)
    return head