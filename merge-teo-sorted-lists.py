# Given the heads of two sorted linked lists, merge the two lists into a single sorted list.
# The resulting list should be made by splicing together the nodes of the first two lists.

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node and a reference to it for the current node
        dummy = cur = ListNode(0)
        
        # Continue the loop while both lists are not empty
        while l1 and l2:
            # Check which value is smaller between the two lists
            if l1.val < l2.val:
                # If the value from l1 is smaller, add it to the current node and move l1 to the next node
                cur.next = l1
                l1, cur = l1.next, cur.next
            else:
                # If the value from l2 is smaller, add it to the current node and move l2 to the next node
                cur.next = l2
                l2, cur = l2.next, cur.next
                
        # If either of the lists still has nodes, add them to the end of the merged list
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        # Return the merged list, starting from the first node after the dummy node
        return dummy.next
