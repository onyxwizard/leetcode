class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #My Approach
        freq = {0:0,1:0,2:0}
        for elem in nums:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem]+=1
        
        idx = 0
        for key,val in freq.items():
            print(key,val)
            if val>0:
                for i in range(val):
                    nums[idx] = key
                    idx+=1
        return nums
                

#Expected Approach
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

nums = [2,0,2,1,1,0]
obj = Solution()
print(obj.sortColors(nums))