class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        #early exit
        if n ==1:
            return 0
        
        #find the beginning break
        start = 0
        while start < n-1 and nums[start] <= nums[start+1]:
            start+=1
        #check the array is sorted
        if start == n-1:
            return 0
        
        #find the ending  break
        end = n-1
        while end > 0 and nums[end-1] <= nums[end]:
            end-=1
        
        #find the min and max
        min_val,max_val = float("inf"),float("-inf")
        for i in range(start,end+1):
            min_val = min(min_val,nums[i])
            max_val = max(max_val,nums[i])
        
        
        #extend boundry
        while start>0 and nums[start-1]>min_val:
            start-=1
        
        while end<n-1 and nums[end+1] < max_val:
            end+=1
        
        return end-start+1

if __name__ == "__main__":
    short_sequence = Solution()
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(short_sequence.findUnsortedSubarray(nums))