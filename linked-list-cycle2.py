# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dictionary to store visited nodes and initialize answer node
        visited = dict()
        answer = None
        
        # Traverse the linked list
        while head:
            # If the current node has already been visited, it's the start of the cycle
            if head in visited:
                answer = head
                break
            # Otherwise, add it to the visited dictionary and continue traversing
            else:
                visited[head] = 1
            head = head.next
        
        # Return the answer node, if found
        return answer
