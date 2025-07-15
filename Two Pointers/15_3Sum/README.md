# LeetCode 15: 3Sum

## 📌 Problem Description

Given an array `nums` of `n` integers, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- The solution set must **not contain duplicate triplets**


## 🧠 Problem Analysis

### Key Observations:
- We need to find **three distinct elements** whose **sum is zero**.
- The result must contain **no duplicate triplets**, even if the same values appear in different positions.
- A brute-force solution would check all combinations in `O(n³)` time — too slow for large inputs (`n ≤ 3000`).
- A more efficient solution uses **sorting** and the **two-pointer technique**.

### Constraints:
- `3 ≤ n ≤ 3000`
- `-10⁵ ≤ nums[i] ≤ 10⁵`


## 🛠️ Solution Approaches

### 1️⃣ Brute Force (Not Recommended)

#### Idea:
- Check all possible triplets using three nested loops.
- Store sorted triplets in a list to avoid duplicates.

#### Code:
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in res:
                            res.append(triplet)
        return res
```

#### Why It Fails:
- **Time Complexity**: `O(n³)` → **Too slow** for `n = 3000`
- **Space Complexity**: `O(n)` for storing results



### 2️⃣ Optimized Approach (Two-Pointer + Sorting)

#### Idea:
- **Sort** the array first.
- Iterate through each element `nums[i]` as the **first number** of the triplet.
- Use **two pointers**:
  - `left = i + 1`
  - `right = len(nums) - 1`
- For each `nums[i]`, find pairs such that `nums[left] + nums[right] == -nums[i]`
- **Skip duplicates** for `i`, `left`, and `right` to avoid duplicate triplets.

#### Code:
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for i
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
```

#### Why It Works:
- Sorting allows us to **avoid duplicates** and use two pointers efficiently.
- Time complexity is reduced to `O(n²)` — acceptable for `n = 3000`.


## ⏱️ Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|---------|------------------|------------------|
| Brute Force | `O(n³)` | `O(n)` |
| Two-Pointer | `O(n²)` | `O(1)` (excluding output) |



## 🔍 Step-by-Step Execution (Optimized)

### Example Input:
```python
nums = [-1, 0, 1, 2, -1, -4]
```

### Sorted Input:
```python
[-4, -1, -1, 0, 1, 2]
```

### Execution Steps:
1. Fix `i = 0` (`-4`) → skip (no pair found)
2. Fix `i = 1` (`-1`) → search for `target = 1`
   - `left = 2`, `right = 5` → `nums[left] = -1`, `nums[right] = 2` → total = `0` → add `[-1, -1, 2]`
   - Skip duplicates for `left` → move to index 3
3. Fix `i = 2` (`-1`) → skip (duplicate)
4. Fix `i = 3` (`0`) → target = `0`
   - `left = 4`, `right = 5` → total = `0 + 1 + 2 = 3` → too big → move `right`
   - `left = 4`, `right = 4` → stop
5. Continue until all valid triplets are found

### Final Output:
```python
[[-1, -1, 2], [-1, 0, 1]]
```



## 🧪 Test Cases

### ✅ Basic Examples:
- **Input:** `[-1,0,1,2,-1,-4]`  
  **Output:** `[[-1,-1,2], [-1,0,1]]`

- **Input:** `[0,1,1]`  
  **Output:** `[]`

- **Input:** `[0,0,0]`  
  **Output:** `[[0,0,0]]`

### 🧪 Edge Cases:
- **Input:** `[0,0,0,0]`  
  **Output:** `[[0,0,0]]`

- **Input:** `[1,2,3,4,5]`  
  **Output:** `[]`

- **Input:** `[0,0,0,0]`  
  **Output:** `[[0,0,0]]`

## ⚠️ Common Mistakes to Avoid

- ❌ Not skipping duplicates for `i`, `left`, or `right`
- ❌ Incorrect pointer movement (e.g., moving both `left` and `right` after a match)
- ❌ Using `set()` or `in` to check for duplicates — too slow for large inputs
- ❌ Forgetting to sort the array before applying the two-pointer approach

## 🧩 Additional Notes

- This problem is a **classic two-pointer** problem.
- The two-pointer approach is also used in similar problems like `4Sum`, `Two Sum II`, and `3Sum Closest`.
- Sorting helps **avoid duplicates** and **optimize the search**.

## 📚 Summary

This problem asks you to find **all unique triplets** in an array that sum to zero. The brute-force solution is too slow for large inputs, so we use a **two-pointer approach** with sorting to reduce time complexity to `O(n²)`.

Key steps:
1. **Sort** the array.
2. Iterate through each element as the **first number** of the triplet.
3. Use **two pointers** to find the other two numbers.
4. **Skip duplicates** to ensure only unique triplets are added.

This approach is both **efficient** and **correct**, making it ideal for solving the 3Sum problem.