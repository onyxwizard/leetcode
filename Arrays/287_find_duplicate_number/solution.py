class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle using Floyd's Tortoise and Hare
        tortoise = hare = nums[0]
        
        # Move tortoise one step and hare two steps until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the entry point of the cycle (duplicate number)
        tortoise = nums[0]  # Reset tortoise to the start
        while tortoise != hare:
            tortoise = nums[tortoise]  # Move both pointers one step at a time
            hare = nums[hare]
        
        return hare  # The meeting point is the duplicate number