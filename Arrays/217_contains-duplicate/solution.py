class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #Approach 1 Hash set
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

if __name__ == "__main__":
    duplicate = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(duplicate.containsDuplicate(nums))