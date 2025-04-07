class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor_result = 0
        
        # XOR all the numbers in the array
        for num in nums:
            xor_result ^= num
        
        # XOR all numbers in the range [0, n]
        for i in range(len(nums) + 1):
            xor_result ^= i
        
        # The final result is the missing number
        return xor_result

if __name__ == "__main__":
    miss = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(miss.missingNumber(nums))