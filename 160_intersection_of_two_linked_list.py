from . import ListNode

# Approach 1: Hash Table
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    nodes = set()
    while headA:
        nodes.add(headA)
        headA = headA.next
    while headB:
        if headB in nodes:
            return headB
        headB = headB.next
    return None

# Approach 2: Two Pointers
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pA = headA
    pB = headB

    # If no intersection, both pA and pB equal None at the same time and break
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA


# # Approach 3: Only works when all node values are positive
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pA = headA
    res = None
    while headA is not None:
        headA.val *= -1
        headA = headA.next
    while headB is not None:
        if headB.val < 0:
            res = ListNode(-headB.val)
            break
        headB = headB.next
    while pA is not None:
        pA.val *= -1 if pA.val < 0 else 1
        pA = pA.next

    return res