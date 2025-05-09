class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        left,right = 0,len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left]**2
                left+=1
            else:
                res[i] = nums[right]**2
                right-=1
        return res

obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
