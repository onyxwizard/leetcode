# LeetCode 75: Sort Colors

## 📌 Problem Description

Given an array `nums` containing `n` integers where the values are either `0`, `1`, or `2` (representing red, white, and blue colors respectively), **sort the array in-place** so that all `0`s come first, followed by all `1`s, and then all `2`s. You must do this **without using built-in sorting functions**.


## 🧠 Problem Analysis

### Key Observations:
- The array contains only **three distinct values**: `0`, `1`, and `2`.
- A **two-pass** solution can count and then reconstruct the array.
- The **follow-up challenge** asks for a **one-pass** solution using **constant extra space**.

### Constraints:
- `1 ≤ n ≤ 300`
- `nums[i] ∈ {0, 1, 2}`



## 🛠️ Solution Approaches

### 1️⃣ Counting and Rebuilding (Two-Pass Approach)

#### Idea:
- Count the frequency of `0`, `1`, and `2`.
- Reconstruct the array by placing all `0`s first, followed by all `1`s, then all `2`s.

#### Why It Works:
- Since there are only three possible values, we can count them in one pass and then fill the array accordingly in a second pass.
- This is **simple** and efficient for small input sizes.

#### Code:
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {0: 0, 1: 0, 2: 0}
        for num in nums:
            freq[num] += 1
        
        idx = 0
        for key in [0, 1, 2]:
            for _ in range(freq[key]):
                nums[idx] = key
                idx += 1
```



### 2️⃣ Dutch National Flag Algorithm (One-Pass, Constant Space)

#### Idea:
- Use **three pointers**:
  - `low`: Everything before `low` is `0`.
  - `mid`: Everything between `low` and `mid` is `1`.
  - `high`: Everything after `high` is `2`.
- Traverse the list with `mid` and swap elements accordingly to move `0`s to the front and `2`s to the end.

#### Why It Works:
- This is a **greedy, one-pass** algorithm.
- It maintains **invariants** to ensure the array is partitioned into three regions: `0`s, `1`s, and `2`s.

#### Code:
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```



## ⏱️ Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|---------|------------------|------------------|
| Counting and Rebuilding | O(n) | O(1) |
| Dutch National Flag | O(n) | O(1) |

- Both algorithms run in **linear time**.
- The Dutch Flag algorithm is **one-pass**, making it more optimal for the follow-up requirement.


## 🔍 Step-by-Step Execution (Dutch Flag)

### Example Input:
```python
nums = [2, 0, 2, 1, 1, 0]
```

### Execution Steps:
1. `low = 0`, `mid = 0`, `high = 5`
   - `nums[mid] = 2` → swap with `high`, `high = 4`
2. `mid = 0`, `nums[mid] = 2` → swap with `high`, `high = 3`
3. `mid = 0`, `nums[mid] = 1` → move `mid` to `1`
4. `mid = 1`, `nums[mid] = 0` → swap with `low`, now `low = 1`, `mid = 2`
5. `mid = 2`, `nums[mid] = 2` → swap with `high`, `high = 2`
6. Loop ends (`mid > high`)

### Final Output:
```python
[0, 0, 1, 1, 2, 2]
```



## 🧪 Test Cases

### ✅ Basic Examples:
- **Input:** `[2,0,2,1,1,0]`  
  **Output:** `[0,0,1,1,2,2]`

- **Input:** `[2,0,1]`  
  **Output:** `[0,1,2]`

### 🧪 Edge Cases:
- **Input:** `[0]`  
  **Output:** `[0]` (no change)

- **Input:** `[2,2,2]`  
  **Output:** `[2,2,2]`

- **Input:** `[1,0,1,0,1,0]`  
  **Output:** `[0,0,0,1,1,1]`


## ⚠️ Common Mistakes to Avoid

- ❌ Using built-in sort functions (`O(n log n)` and not allowed).
- ❌ Incorrect pointer manipulation in the Dutch Flag algorithm (e.g., forgetting to update `low` or `mid`).
- ❌ Off-by-one errors in the loop condition (`mid <= high` is essential).
- ❌ Swapping incorrectly and losing track of unprocessed elements.


## 🧩 Additional Notes

- The Dutch National Flag algorithm is **optimal** for this problem, especially for the follow-up.
- The counting approach is easier to understand but requires two passes.
- Both approaches are **in-place**, satisfying the problem's constraints.



## 📚 Summary

This problem asks you to sort an array of `0`s, `1`s, and `2`s in-place. Two efficient approaches exist:

1. **Counting and Rebuilding** — simple and easy to implement, but a **two-pass** solution.
2. **Dutch National Flag Algorithm** — a **one-pass** solution using **three pointers**, ideal for the follow-up.

Both approaches have **linear time** and **constant space** complexity, making them suitable for large input sizes. The Dutch Flag algorithm is the most elegant and efficient solution for this classic problem.