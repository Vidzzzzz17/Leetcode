class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Dummy node handles edge cases like removing the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move `fast` n + 1 steps ahead so the gap between fast and slow is n + 1
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast hits the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Skip the n-th node from the end
        slow.next = slow.next.next
        
        return dummy.next
        