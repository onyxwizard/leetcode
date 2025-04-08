# 128. Longest Consecutive Sequence 🚀

**Solved** ✅  **Medium** 🌟  **Topics** 📚   :  **`Hash set`**

# Problem Statement:

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time. 🧮



## Examples:

### Example 1:
**Input:** `nums = [100, 4, 200, 1, 3, 2]`  
**Output:** `4`  
**Explanation:**  
The longest consecutive elements sequence is `[1, 2, 3, 4]`.  
Therefore, its length is `4`. 📏

### Example 2:
**Input:** `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`  
**Output:** `9`  
**Explanation:**  
The longest consecutive elements sequence is `[0, 1, 2, 3, 4, 5, 6, 7, 8]`.  
Its length is `9`. 🎯

### Example 3:
**Input:** `nums = [1, 0, 1, 2]`  
**Output:** `3`  
**Explanation:**  
The longest consecutive elements sequence is `[0, 1, 2]`.  
Its length is `3`. 🔗



## Constraints:

- `0 <= nums.length <= 10^5` 🧮  
- `-10^9 <= nums[i] <= 10^9` 🗺️




## Problem Understanding 🧠

The goal is to determine the **length** of the longest sequence of consecutive integers that can be formed using the elements of an unsorted array. Consecutive integers follow each other without any gaps (e.g., `[1, 2, 3, 4]` is valid, while `[1, 3, 4]` is not).


## Logical Approach 🔍

To solve the problem efficiently in **O(n)** time complexity, we can utilize a **hash set** for quick lookups. Here's the logical breakdown:

1. **Hash Set for Presence Check**:  
   Store all the elements of the array in a hash set. This enables fast checks to determine whether a number is present in the array.  

2. **Sequence Starting Points**:  
   Only consider elements that are the **start of a sequence**. A number is a starting point if `num - 1` does not exist in the set.  

3. **Build Consecutive Sequences**:  
   From each starting point, extend the sequence by checking for consecutive elements (`num + 1`, `num + 2`, etc.). Track the length of each sequence.  

4. **Track the Longest Sequence**:  
   Keep track of the longest sequence length during the iteration.


## Code:
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
```

## Code Breakdown with Line-by-Line Explanation 📊

| **Line of Code**                                          | **Explanation**                                                                                     |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `class Solution:`                                          | 🏗️ Defines a class named `Solution`. This encapsulates the method `longestConsecutive`.             |
| `def longestConsecutive(self, nums: List[int]) -> int:`    | ✍️ Defines a method named `longestConsecutive` that takes a list of integers (`nums`) as input and returns an integer (`int`). |
| `if not nums:`                                             | ❓ Checks for an edge case: if the input list is empty, returns `0` immediately since no sequence exists. |
| `num_set = set(nums)`                                      | 🔄 Converts the input list `nums` into a hash set `num_set` for quick lookups of elements. This ensures **O(1)** lookup time. |
| `max_length = 0`                                           | 🧮 Initializes `max_length` to `0`, which will store the length of the longest consecutive sequence found so far. |
| `for num in num_set:`                                      | 🔍 Iterates through each number in the hash set `num_set`. This avoids duplicate processing.          |
| `if num - 1 not in num_set:`                               | 🔑 Checks if the current number is the **start of a sequence**. A number is the start if `num - 1` is not in the set. |
| `current_num = num`                                        | 🔢 Initializes `current_num` to the current number. This variable will be used to explore the sequence. |
| `current_length = 1`                                       | 📏 Initializes `current_length` to `1`, as the sequence containing just the current number is at least 1 long. |
| `while current_num + 1 in num_set:`                        | 🔁 Checks for the next consecutive number (`current_num + 1`). If it exists in the set, the sequence is extended. |
| `current_num += 1`                                         | ➕ Moves to the next number in the sequence (`current_num` is incremented by `1`).                   |
| `current_length += 1`                                      | 📏 Increases the `current_length` by `1` as the sequence is extended.                                |
| `max_length = max(max_length, current_length)`             | 🔝 Updates the `max_length` with the longer value between `max_length` and `current_length`.         |
| `return max_length`                                        | ✅ Returns the length of the longest consecutive sequence found (`max_length`).                      |



## Key Insights 🔑

1. **Logic**:  
   - The algorithm converts the list to a hash set for **O(1)** lookups.  
   - It identifies starting points of sequences (numbers that don't have a predecessor in the set).  
   - Using these starting points, it builds and measures the length of sequences.

2. **Efficiency**:  
   - **Time Complexity**:  
     - The loop iterates through the hash set, which has at most `n` elements (length of input list).  
     - Each element is processed only once, resulting in an overall time complexity of **O(n)**.  
   - **Space Complexity**:  
     - The hash set requires **O(n)** space, where `n` is the number of unique elements in the input list.



## Example Walkthrough 📚

**Input:** `nums = [100, 4, 200, 1, 3, 2]`

1. **Step 1: Edge Case Check**  
   - `nums` is not empty, so the algorithm proceeds.  

2. **Step 2: Convert to Hash Set**  
   - `num_set = {1, 2, 3, 4, 100, 200}`  

3. **Step 3: Iterate Through `num_set`**  
   - For `100`:  
     - `99` is not in `num_set` → Start of a sequence.  
     - Sequence: `[100]`, `current_length = 1`.  
   - For `4`:  
     - `3` is in `num_set` → Not a starting point. Skip.  
   - For `200`:  
     - `199` is not in `num_set` → Start of a sequence.  
     - Sequence: `[200]`, `current_length = 1`.  
   - For `1`:  
     - `0` is not in `num_set` → Start of a sequence.  
     - Sequence: `[1, 2, 3, 4]`, `current_length = 4`.  

4. **Step 4: Track Longest Sequence**  
   - `max_length = 4`.

**Output:** `4`



Let me know if you'd like further clarifications or refinements! 😊✨


## Time Complexity ⏱️

1. **Building the Hash Set:**  
   Adding all elements to the hash set takes **O(n)** time.  

2. **Iteration and Sequence Building:**  
   Each element is processed at most twice—once as a potential starting point and once during sequence building. This takes **O(n)** time.  

**Overall Time Complexity:** **O(n)**  



## Space Complexity 📏

1. **Hash Set Storage:**  
   The hash set stores up to `n` elements in the worst case, requiring **O(n)** space.  

**Overall Space Complexity:** **O(n)**  



Let me know if you'd like further clarifications or refinements! 😊✨

---