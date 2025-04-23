class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Edge case: If k <= 1, no subarray can have a product less than k
        if k <= 1:
            return 0
        
        left, right = 0, 0
        count = 0
        product = 1
        
        # Iterate through the array with the right pointer
        while right < len(nums):
            print(nums[left:right])
            # Expand the window by multiplying the current number
            product *= nums[right]
            
            # Shrink the window from the left until the product is valid (< k)
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            # Count all valid subarrays ending at `right`
            count += (right - left + 1)
            
            # Move the right pointer to expand the window
            right += 1
        
        return count

# Test the solution

obj = Solution()
print(obj.numSubarrayProductLessThanK([10,5,2,6],100))