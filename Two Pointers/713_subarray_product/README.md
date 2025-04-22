# 📚 Problem Statement: Subarray Product Less Than K (LeetCode 713) 🧮


## 🌟 Problem Overview:
Given an array of integers `nums` and an integer `k`, the task is to find the **number of contiguous subarrays** where the product of all elements in the subarray is **strictly less than** `k`.

### 🔑 Key Points:
- A subarray is a contiguous portion of the array.
- The product must be strictly less than `k`.
- If no such subarrays exist, return `0`.



## 📝 Example Walkthrough:

### Example 1:
#### Input:
```plaintext
nums = [10, 5, 2, 6], k = 100
```

#### Explanation:
The valid subarrays with product < 100 are:
- `[10]` → Product = 10
- `[5]` → Product = 5
- `[2]` → Product = 2
- `[6]` → Product = 6
- `[10, 5]` → Product = 50
- `[5, 2]` → Product = 10
- `[2, 6]` → Product = 12
- `[5, 2, 6]` → Product = 60

Thus, there are **8 valid subarrays**.

#### Output:
```plaintext
8
```


### Example 2:
#### Input:
```plaintext
nums = [1, 2, 3], k = 0
```

#### Explanation:
Since `k = 0`, and all products are positive integers, no subarray will have a product less than `0`. Hence, the result is `0`.

#### Output:
```plaintext
0
```

## 💡 Core Logic: Sliding Window Approach

To solve this problem efficiently, we use the **sliding window technique**. This approach ensures that we maintain a "window" of subarrays whose product is less than `k`. Here's how it works:

1. **Initialize Variables**:
   - `product`: Tracks the product of the current window.
   - `left`: Pointer for the start of the window.
   - `count`: Tracks the total number of valid subarrays.

2. **Iterate Through the Array**:
   - For each element at index `right`, multiply it into the `product`.
   - If the `product` becomes greater than or equal to `k`, shrink the window from the left by dividing the `product` by `nums[left]` and incrementing `left`.
   - Once the `product` is valid again (< `k`), calculate the number of valid subarrays ending at `right`. This is given by `(right - left + 1)`.

3. **Why `(right - left + 1)`?**
   - Every new element at `right` can form valid subarrays with all elements from `left` to `right`.

4. **Edge Case**:
   - If `k <= 1`, return `0` immediately since no product can be less than `1` (all numbers are positive).

## 🧪 Test Cases:

### Test Case 1:
```plaintext
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
```

### Test Case 2:
```plaintext
Input: nums = [1, 2, 3], k = 0
Output: 0
```

### Test Case 3:
```plaintext
Input: nums = [1, 1, 1], k = 2
Output: 6
```

## 🎉 Final Answer:
```plaintext
For nums = [10, 5, 2, 6] and k = 100, the output is 8.
```
## ⏱️ Time Complexity:
- **O(n)**: We traverse the array once using the sliding window. Each element is added and removed from the window at most once.

## 📦 Space Complexity:
- **O(1)**: We only use a few variables (`product`, `left`, `count`), so the space usage is constant.

## 🛠️ Code Implementation:

```python
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:  # Edge case: No product can be less than 1
        return 0
    
    product = 1
    left = 0
    count = 0
    
    for right in range(len(nums)):
        product *= nums[right]  # Expand the window
        
        # Shrink the window if the product is invalid
        while product >= k and left <= right:
            product //= nums[left]
            left += 1
        
        # Count valid subarrays ending at `right`
        count += (right - left + 1)
    
    return count
```



## 🎯 Summary:

This problem elegantly demonstrates the power of the **sliding window technique**. By maintaining a dynamic window and adjusting it based on the product constraint, we achieve an efficient solution with linear time complexity. The key insight is recognizing how to count subarrays dynamically as the window expands and shrinks.
