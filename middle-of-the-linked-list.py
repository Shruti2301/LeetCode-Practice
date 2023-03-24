#Given the head of a singly linked list, we want to return the middle node of the linked list. If there are two middle nodes, we want to return the second middle node.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize length and temp pointer
        length = 0
        temp = head
        
        # Traverse the linked list and count the number of nodes
        while temp:
            length += 1
            temp = temp.next
            
        # Calculate the index of the middle node(s)
        middle = length // 2
        
        # Traverse the linked list again to find the middle node(s)
        i = 0
        while i < middle:
            head = head.next
            i += 1
        
        # Return the middle node(s)
        return head
