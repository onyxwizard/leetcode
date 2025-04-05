#448. Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        missing_element = []  # Initialize an empty list to store the missing numbers
        
        # Step 1: Mark the presence of each number by negating the value at its corresponding index
        # For each number in the array, use its value as an index (after adjusting by -1) 
        # and negate the number at that index to indicate the value has been "seen"
        for elem in nums:
            index = abs(elem) - 1  # Convert the current number to its 0-based index (1-based numbers need -1)
            nums[index] = -abs(nums[index])  # Negate the value at that index, using abs() to handle already negated numbers
        
        # Step 2: Identify missing numbers by finding positive values
        # After marking, any index with a positive value means that index+1 was never "seen" in the array
        for index in range(len(nums)):
            if nums[index] > 0:  # If the value at this index is positive, the number (index + 1) is missing
                missing_element.append(index + 1)  # Add the missing number (index is 0-based, so +1 adjusts it)
        
        return missing_element  # Return the list of missing numbers
    
if __name__ == "__main__":
    missing_element = Solution()
    array = [4,3,2,7,8,2,3,1]
    print(missing_element.findDisappearedNumbers(array))