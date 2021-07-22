from . import Node
from collections import defaultdict
# Use defaultdict and initialize all values to default Node
# Then update Node in the loop
def copyRandomList(self, head: 'Node') -> 'Node':
    d = defaultdict(lambda: Node(0))
    # if a node's next/random is None
    d[None] = None
        
    cur = head
    while cur:
        d[cur].val = cur.val
        d[cur].next = d[cur.next]
        d[cur].random = d[cur.random]
        cur = cur.next

    return d[head]

# First loop:  Insert a Node's copy next to the Node (interweave)
# Second loop: Set copied Nodes' random to original Nodes' random's next
# Third loop:  Transform copied Nodes into a linked list 
def copyRandomList(self, head: 'Node') -> 'Node':
    if head is None:
        return None
    curr = head
    while curr:
        insertNode = Node(curr.val, curr.next, None)
        curr.next = insertNode
        curr = curr.next.next
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    res = head.next
    while res.next:
        res.next = res.next.next
        res = res.next
    return head.next