class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)
        
        # Step 1: Build a max-heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
            
        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Move max element to the end
            heapify(i, 0)  # Heapify the reduced heap
            
        return nums