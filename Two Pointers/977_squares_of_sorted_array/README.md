# 977. Squares of a Sorted Array 🧮

## Problem Description 📝

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 🔢

### Example 1: 🌟

**Input:**  
`nums = [-4,-1,0,3,10]`

**Output:**  
`[0,1,9,16,100]`

**Explanation:**  
After squaring, the array becomes `[16,1,0,9,100]`.  
After sorting, it becomes `[0,1,9,16,100]`. ✨

### Example 2: 🌟

**Input:**  
`nums = [-7,-3,2,3,11]`

**Output:**  
`[4,9,9,49,121]`

**Explanation:**  
After squaring, the array becomes `[49,9,4,9,121]`.  
After sorting, it becomes `[4,9,9,49,121]`. ✨



## Constraints ⚖️

- `1 <= nums.length <= 10^4`  
- `-10^4 <= nums[i] <= 10^4`  
- `nums` is sorted in **non-decreasing order**.  



## Follow Up 💡

Squaring each element and sorting the new array is very trivial, could you find an **O(n)** solution using a different approach? 🤔



## Approach and Solution 🛠️

### Approach:

The key observation here is that the input array is already sorted, but it may contain negative numbers. When we square these numbers, their relative order changes because smaller negative numbers (e.g., `-4`) become larger when squared (e.g., `16`). To solve this efficiently, we can use a **two-pointer approach**.

- Use two pointers: one starting at the beginning (`left`) and one at the end (`right`) of the array.
- Compare the absolute values of the elements at these pointers.
- The larger squared value gets placed at the end of the result array, and the corresponding pointer (`left` or `right`) moves inward.
- Repeat this process until all elements are processed.

This ensures that the result array is filled with squares in non-decreasing order without needing to sort explicitly.



### Algorithm Steps:

1. Initialize an empty result array `res` of the same size as `nums`.
2. Set two pointers: `left = 0` and `right = len(nums) - 1`.
3. Iterate from the end of the result array (`i = len(nums) - 1`) to the start:
   - Compare `abs(nums[left])` and `abs(nums[right])`.
   - Place the square of the larger value at `res[i]`.
   - Move the corresponding pointer inward (`left++` or `right--`).
4. Return the result array `res`.



### Code Implementation 🧑‍💻

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)  # Result array initialized with zeros
        left, right = 0, len(nums) - 1  # Two pointers
        
        for i in range(len(nums) - 1, -1, -1):  # Fill result array from the end
            if abs(nums[left]) > abs(nums[right]):  # Compare absolute values
                res[i] = nums[left] ** 2  # Square the larger value
                left += 1  # Move left pointer inward
            else:
                res[i] = nums[right] ** 2  # Square the larger value
                right -= 1  # Move right pointer inward
                
        return res
```



### Complexity Analysis 📊

#### Time Complexity: ⏳
- **O(n)** where `n` is the length of the input array `nums`.  
  We only iterate through the array once, comparing and filling the result array.

#### Space Complexity: 🗄️
- **O(n)** for the result array `res`.  
  No additional space is used apart from the output array.


### Key Takeaways 🎯

- The two-pointer technique is efficient for problems involving sorted arrays with negative and positive numbers. 👌
- By leveraging the fact that the input array is sorted, we avoid the need for explicit sorting, achieving **O(n)** time complexity. 🚀
- This approach ensures optimal performance even for large input sizes (up to `10^4`). 📈

Happy coding! 🌟