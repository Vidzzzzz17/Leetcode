# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        while curr.next:
            nxt = curr.next
            
            # Check for local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - prev_cp)
                
                prev_cp = index
            
            prev = curr
            curr = nxt
            index += 1
            
        if first_cp == prev_cp:
            return [-1, -1]
            
        return [min_dist, prev_cp - first_cp]