class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #edge case
        if not nums:
            return 0
            
        #convert to hash set
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num -1 not in num_set:
                current_num = num
                current_length = 1

                while current_num +1 in num_set:
                    current_num+=1
                    current_length+=1
                max_length = max(max_length,current_length)
        return max_length

if __name__ == "__main__":
    long_sequence = Solution()
    nums = [1,5,4,7,5,7,1]
    print(long_sequence.longestConsecutive(nums))