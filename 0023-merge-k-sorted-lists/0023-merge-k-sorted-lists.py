import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        min_heap = []
        
        # Push the head of each list into the heap
        for i, l in enumerate(lists):
            if l:
                # Store (val, index, node) to avoid direct comparison of ListNode objects
                heapq.heappush(min_heap, (l.val, i, l))
                
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            # If there's a next node in the same list, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next