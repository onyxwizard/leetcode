 # 🌟 Two Sum  
**Difficulty:** 🟢 Easy  
**Topics:** 📊 Array, 🗄️ Hash Table  
**Hint:** 💡 Think about using a data structure to improve the solution's time complexity.  



## Problem Statement 📜  
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`. ✨  

You may assume that:
- Each input would have exactly **one solution**. 🔐  
- You may **not** use the same element twice. ⚠️  

You can return the answer in any order. 🔄  



## Examples 🚀  

### Example 1  
**Input:**  
`nums = [2,7,11,15]`, `target = 9`  
**Output:**  
`[0,1]`  
**Explanation:**  
`nums[0] + nums[1] == 9`, so we return `[0, 1]`. 🧮 ✅  

### Example 2  
**Input:**  
`nums = [3,2,4]`, `target = 6`  
**Output:**  
`[1,2]` ✔️  

### Example 3  
**Input:**  
`nums = [3,3]`, `target = 6`  
**Output:**  
`[0,1]` 💯  


## Constraints ⛓️  
- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i] <= 10^9`  
- `-10^9 <= target <= 10^9`  
- **Only one valid answer exists.** 🛡️  



## Follow-up 💭  
Can you come up with an algorithm that is **less than O(n²)** time complexity? 🚀💡  


## Optimization Hint 🌈  
🧠 Consider using a **hash table** (dictionary) to store numbers you've seen along with their indices. You can then check if the complement of the current number exists in the table during a single traversal. ⚡  



## Step-by-Step Explanation 🤔  

### **Logic Behind the Solution**  
The problem requires finding two numbers in the array that sum up to the given `target`. Here’s how we solve it step by step:  

1. **Brute Force Approach (Suboptimal):**  
   - Use two nested loops to check all pairs of numbers in the array.  
   - For each pair `(i, j)`, check if `nums[i] + nums[j] == target`.  
   - **Time Complexity:** O(n^2), as we compare every possible pair.  
   - **Space Complexity:** O(1), since no extra space is used.  

2. **Optimized Approach Using a Hash Table:**  
   - Traverse the array once while maintaining a hash table (`seen`) to store previously encountered numbers and their indices.  
   - For each number `nums[i]`:  
     - Calculate its **complement**: `complement = target - nums[i]`.  
     - Check if the complement exists in the hash table:  
       - If yes, return the indices of the complement and the current number.  
       - If not, add the current number and its index to the hash table for future reference.  
   - **Time Complexity:** O(n), as we traverse the array only once.  
   - **Space Complexity:** O(n), due to the hash table storing up to `n` elements.  



## Code Implementation 🖥️  

```python
from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store seen numbers and their indices
        seen = defaultdict(int)
        
        # Iterate through the array
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in seen:
                return [seen[complement], index]
            
            # Add the current number and its index to the dictionary
            seen[num] = index
```

# Code Explanation 🧩  

### **How It Works** 🤔  

1. **Initialization:** 🔧  
   - A `defaultdict` named `seen` is used to store numbers as keys and their indices as values.  
   - This dictionary will help us quickly look up whether the complement of the current number has already been encountered. 📊  

2. **Single Pass Through the Array:** 🚀  
   - For each number `num` at index `index`:  
     - Calculate the **complement**: `complement = target - num`. 🔢  
       - The complement is the number that, when added to `num`, equals the `target`.  
     - Check if the complement exists in the `seen` dictionary: 🗄️  
       - If yes, we’ve found the two numbers that add up to the target! Return the indices of the complement and the current number immediately. ✨  
       - If not, add the current number and its index to the `seen` dictionary for future reference. 📥  

3. **Return the Result:** 🎯  
   - Once a valid pair is found, return their indices immediately.  
   - Since the problem guarantees exactly one solution, we don’t need to handle cases where no solution exists. 💯  



## Time and Space Complexity Analysis ⏳  

### **Time Complexity** ⏱️  
- **Best Case:** O(1) — The complement is found during the very first iteration. 🌟  
- **Average and Worst Case:** O(n) — We iterate through the array once, performing constant-time operations (like dictionary lookups) for each element. 🔄  

### **Space Complexity** 💾  
- O(n) — In the worst case, the hash table (`seen`) stores all `n` elements of the array. 📊  



## Comparison of Solutions 📊  

| **Approach**          | **Time Complexity** | **Space Complexity** | **Pros**                                      | **Cons**                                   |
|------------------------|---------------------|-----------------------|-----------------------------------------------|--------------------------------------------|
| **Brute Force**       | O(n²)             | O(1)                | Simple to implement                          | Inefficient for large inputs               |
| **Hash Table**        | O(n)              | O(n)                | Efficient, works well for large inputs       | Requires additional space                  |



## Detailed Explanation 💪  

### **Why the Hash Table Approach is Better?** 🤔  
The brute-force approach involves checking every possible pair of numbers using two nested loops. While it’s simple, it becomes inefficient for large arrays because its time complexity is $O(n²)$. 😅  

The hash table approach improves this by reducing the time complexity to O(n). Here’s how:  
1. **Constant-Time Lookups:** 🕒  
   - Dictionaries (hash tables) allow us to check if a number exists in O(1) time. This eliminates the need for a second loop.  
2. **Single Pass:** 🚀  
   - By storing previously seen numbers and their indices, we can find the complement in just one traversal of the array.  

### **Trade-Offs:** ⚖️  
- The hash table approach uses extra space (O(n)), but this trade-off is worth it for larger datasets where performance matters. 💪  


## Final Thoughts 🎯  

The **hash table approach** is the best solution for this problem due to its optimal time complexity of O(n) and simplicity. While it uses extra space, the trade-off is worth it for larger datasets where performance matters. 🌟  

Let me know if you'd like further clarification or additional enhancements! 🚀✨