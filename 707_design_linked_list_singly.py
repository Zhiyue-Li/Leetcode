class ListNode:

    def __init__(self, value):
        """
        Initialize your data structure here.
        """
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length or index < 0:
            return -1
        
        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node.value
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        node = self.head
        for _ in range(index):
            node = node.next
        to_add = ListNode(val)
        to_add.next = node.next
        node.next = to_add
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length or index < 0:
            return
        
        node = self.head
        for _ in range(index):
            node = node.next
        node.next = node.next.next
        self.length -= 1 if self.length > 0 else 0
