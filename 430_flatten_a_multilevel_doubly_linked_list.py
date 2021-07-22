from . import Node
# Approach 1: List
def flatten(self, head: 'Node') -> 'Node':
    continueNodes = []
    p = head
    while p:
        if p.child:
            if p.next:
                continueNodes.append(p.next)
            p.child.prev = p
            p.next = p.child
            p.child = None
        elif p.next is None and continueNodes:
            n = continueNodes.pop(-1)
            n.prev = p
            p.next = n
        p = p.next
    return head

# Approach 2: DFS by stack
def flatten(self, head):
    if not head:
        return

    pseudoHead = Node(0,None,head,None)
    prev = pseudoHead

    stack = []
    stack.append(head)

    while stack:
        curr = stack.pop()

        prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)
 
        if curr.child:
            stack.append(curr.child)
            # don't forget to remove all child pointers.
            curr.child = None

        prev = curr
    # detach the pseudo head node from the result.
    pseudoHead.next.prev = None
    return pseudoHead.next
