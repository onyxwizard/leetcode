from collections import defaultdict
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor

if __name__ == "__main__":
    uniq = Solution()
    nums = [1,5,4,7,5,7,1]
    print(uniq.singleNumber(nums))