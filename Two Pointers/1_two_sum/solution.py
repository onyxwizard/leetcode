from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen =  defaultdict(int)
        for index in range(0,len(nums)):
            sub = target-nums[index]
            if sub in seen:
                return [seen[sub],index]
            seen[nums[index]] = index

if __name__ == "__main__":
    two_sum = Solution()
    print(two_sum.twoSum(nums=[2,7,11,15],target=9))