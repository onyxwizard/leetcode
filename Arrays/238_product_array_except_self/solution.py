class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1]*n
        
        prefix = 1
        for pre in range(n):
            answer[pre] *= prefix
            prefix *= nums[pre]
        
        postfix = 1
        for post in range(n-1,-1,-1):
            answer[post]*=postfix
            postfix*=nums[post]
        
        return answer
                
        