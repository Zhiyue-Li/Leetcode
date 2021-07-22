from . import ListNode
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head
        
    res = None   
    prev = None
    tail = None
    ptr = head
    curr = head
    # count is used to track length of group
    count = 0

    while ptr:
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        if count == k:
            while count > 0:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count -= 1
            if not res:
                res = prev
            if tail:
                tail.next = prev
            tail = head
            head = curr
            prev = None
    if tail:
        tail.next = head
        
    return res

# Given head and k, reverse k nodes start from head
def reverseLinkedList(self, head, k):
    new_head, ptr = None, head
    while k:
        next_node = ptr.next
        ptr.next = new_head
        new_head = ptr
        ptr = next_node
        k -= 1
    return new_head
                
    
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
    ptr = head
    ktail = None
    
    # Head of the final, moified linked list
    new_head = None
        
        # Keep going until there are nodes in the list
    while ptr:
        count = 0
            
        # Start counting nodes from the head
        ptr = head
            
        # Find the head of the next k nodes
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we counted k nodes, reverse them        
        if count == k:
                
            # Reverse k nodes and get the new head
            revHead = self.reverseLinkedList(head, k)
                
            # new_head is the head of the final linked list
            if not new_head:
                new_head = revHead
                
            # ktail is the tail of the previous block of 
            # reversed k nodes
            if ktail:
                ktail.next = revHead
                    
            ktail = head 
            head = ptr
        
    # attach the final, possibly un-reversed portion
    if ktail:
        ktail.next = head
        
    return new_head if new_head else head