from . import ListNode
import heapq
# Sort all nodes' value in a list then transform into a linked list
def mergeKLists(self, lists: list[ListNode]) -> ListNode:
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    for i in sorted(nodes):
        point.next = ListNode(i)
        point = point.next
    return head.next


# Heapq (Priority Queue)
def mergeKLists(self, lists):
    h = [(l.val, idx) for idx, l in enumerate(lists) if l]
    heapq.heapify(h)
    head = cur = ListNode(None)
    while h:
        val, idx = heapq.heappop(h)
        cur.next = ListNode(val)
        cur = cur.next
        node = lists[idx] = lists[idx].next
        if node:
            heapq.heappush(h, (node.val, idx))
    return head.next


# Merge with divide and conquer
def mergeKLists(self, lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None

def merge2Lists(self, l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next
    if not l1:
        point.next=l2
    else:
        point.next=l1
    return head.next