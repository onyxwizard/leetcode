# 217. [Contains Duplicate 🚀 ](https://leetcode.com/problems/contains-duplicate/)

**Solved** ✅   **Easy** 🌟   **Topics** 📚   


## Problem Statement:

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct. 🔍


## Examples:

### Example 1:
**Input:** `nums = [1,2,3,1]`  
**Output:** `true` ✅  
**Explanation:**   The element `1` occurs at the indices `0` and `3`. 📊

### Example 2:
**Input:** `nums = [1,2,3,4]`  
**Output:** `false` ❌  
**Explanation:** All elements are distinct. 🌈

### Example 3:
**Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
**Output:** `true` ✅


## Constraints:

- `1 <= nums.length <= 10^5` 🧮  
- `-10^9 <= nums[i] <= 10^9` 🗺️


## Approach 1: Sorting the Array and Using Two Pointers 🧮

### Concept:  
This approach sorts the array first, ensuring that any duplicate elements will appear next to each other. Then, use two pointers to check adjacent elements for duplicates. 🧹  

### Example:  
**Input:** `nums = [1, 2, 3, 1]`  
**Steps:**  
1. Sort the array:  
   - **Before Sorting:** `nums = [1, 2, 3, 1]`  
   - **After Sorting:** `nums = [1, 1, 2, 3]` 📜  
2. Use two pointers to compare adjacent elements:  
   - **Left = 0, Right = 1:**  
     - Compare `nums[left]` and `nums[right]` (1 == 1).  
     - Found duplicate, return `True`. ✅  

**Output:** `True`  

### Code
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    # Sort the array
    nums.sort()
    
    # Initialize two pointers
    left = 0
    right = 1
    
    # Iterate through the sorted array
    while right < len(nums):
        # If two adjacent elements are equal, return True
        if nums[left] == nums[right]:
            return True
        # Otherwise, move both pointers forward
        left += 1
        right += 1
    
    # If no duplicates are found, return False
    return False

```

### Efficiency:  
- **Time Complexity:** Sorting the array takes **O(n log n)**, and traversing it with two pointers is **O(n)**. Overall complexity: **O(n log n)**. 🔍  
- **Space Complexity:** **O(1)** if sorting is done in-place. ⚖️  


## Approach 2: Using a `Set` to Track Duplicate Elements 💡

### Concept:  
The idea is to use a `set` to keep track of elements we've seen so far in the array. A `set` allows fast lookups, making it ideal for detecting duplicates efficiently. 🌟  

### Example:  
**Input:** `nums = [1, 2, 3, 1]`  
**Steps:**  
1. Start with an empty `set`: `seen = {}` 🧺  
2. Iterate through the array:  
   - **Element = 1:**  
     - Not in `seen`, so add it.  
     - `seen = {1}` ➕  
   - **Element = 2:**  
     - Not in `seen`, so add it.  
     - `seen = {1, 2}` ➕  
   - **Element = 3:**  
     - Not in `seen`, so add it.  
     - `seen = {1, 2, 3}` ➕  
   - **Element = 1:**  
     - Already in `seen`, so return `True`. ✅  

**Output:** `True`  

### Code
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    # Initialize an empty set to track elements seen so far
    seen = set()
    
    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is already in the set, return True
        if nums[i] in seen:
            return True
        # Add the current element to the set
        seen.add(nums[i])
    
    # If no duplicates are found, return False
    return False
```

### Efficiency:  
- **Time Complexity:** **O(n)** because we only traverse the array once, and set operations (lookup and insertion) are **O(1)**. 🚀  
- **Space Complexity:** **O(n)** for the set. 📏  


## Comparison of Approaches 🤔

| **Approach**             | **Pros**                             | **Cons**                              |
|--------------------------|---------------------------------------|---------------------------------------|
| **Using Set** 💡          | Fast and simple implementation. 🚀   | Extra space for the set. 📏           |
| **Sorting + Two Pointers** 🧮 | Space-efficient when sorting in-place. 🧹 | Slower due to sorting overhead. 🕐     |

### Conclusion:
Both approaches are effective and have different trade-offs. If you prioritize speed, use the set-based approach. If you aim to reduce space usage, go for the sorting approach! 🌟

---
