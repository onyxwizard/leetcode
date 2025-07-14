# LeetCode 11: Container With Most Water

## 📌 Problem Description

You are given an array `height` of integers, where each element represents a vertical line of height `height[i]` at coordinate `(i, height[i])`. Your task is to find **two lines** that together with the x-axis form a **container** that can hold the **maximum amount of water**.

The **area** of the container is calculated as:
```
Area = (right - left) * min(height[left], height[right])
```


## 🧠 Problem Analysis

### Key Observations:
- The **width** of the container is determined by the distance between the two lines (`right - left`).
- The **height** of the container is determined by the **shorter** of the two lines (`min(height[left], height[right])`).
- To maximize the area, you must balance **width** and **height**.
- A **brute-force** solution would check all possible pairs of lines in `O(n^2)` time — too slow for large inputs.

### Constraints:
- `2 ≤ n ≤ 10^5`
- `0 ≤ height[i] ≤ 10^4`



## 🛠️ Solution Approach

### Optimal Strategy: **Two-Pointer Technique**

#### Idea:
- Start with the **widest possible container** (`left = 0`, `right = len(height) - 1`).
- At each step:
  - Calculate the area.
  - Move the pointer pointing to the **shorter** line inward, hoping to find a **taller** line.
- This greedy strategy ensures that we explore potential candidates that may yield a larger area.

#### Why It Works:
- Moving the **taller** line inward will **not** increase the height (since the area is limited by the shorter line).
- Therefore, it makes sense to try to **improve the shorter line** to possibly increase the area.


## 💻 Code Implementation

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```



## ⏱️ Time & Space Complexity

- **Time Complexity**: `O(n)`  
  Each pointer moves from one end to the other at most once.
  
- **Space Complexity**: `O(1)`  
  Only a few variables are used (pointers and area tracker).


## 🔍 Step-by-Step Execution

### Example Input:
```python
height = [1,8,6,2,5,4,8,3,7]
```

### Execution Steps:
1. `left = 0`, `right = 8` → area = `8 * 1 = 8` → move `left` to `1`
2. `left = 1`, `right = 8` → area = `7 * 7 = 49` → move `right` to `7`
3. `left = 1`, `right = 7` → area = `6 * 3 = 18` → move `right` to `6`
4. `left = 1`, `right = 6` → area = `5 * 8 = 40` → move `right` to `5`
5. `left = 1`, `right = 5` → area = `4 * 4 = 16` → move `right` to `4`
6. `left = 1`, `right = 4` → area = `3 * 5 = 15` → move `right` to `3`
7. ... continue until `left == right`

### Final Output:
```python
49
```



## 🧪 Test Cases

### ✅ Basic Examples:
- **Input:** `[1,8,6,2,5,4,8,3,7]`  
  **Output:** `49`

- **Input:** `[1,1]`  
  **Output:** `1`

### 🧪 Edge Cases:
- **Input:** `[1,2,1]`  
  **Output:** `2`

- **Input:** `[1,2,3,4,5]`  
  **Output:** `9`

- **Input:** `[1,1,1,1]`  
  **Output:** `3`

- **Input:** `[2,3,4,5,18,17,6]`  
  **Output:** `16`


## ⚠️ Common Mistakes to Avoid

- ❌ Using a brute-force approach with nested loops (`O(n²)` time).
- ❌ Forgetting that the **area is limited by the shorter line**.
- ❌ Moving both pointers at once — only one should move per iteration.
- ❌ Not handling the case when both lines are equal in height.


## 🧩 Additional Notes

- This problem is a **classic greedy algorithm**.
- It demonstrates how **two pointers** can be used effectively to reduce time complexity.
- The solution is **in-place** and uses **constant space**.


## 📚 Summary

This problem requires finding the **maximum area** formed between any two lines in a list. The optimal solution uses the **two-pointer technique**, starting from the **widest container** and greedily moving the pointer pointing to the **shorter line** inward. This ensures that we explore promising candidates for maximizing area while maintaining **linear time complexity**.