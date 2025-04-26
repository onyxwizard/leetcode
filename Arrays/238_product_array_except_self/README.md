# 🚀 **238. Product of Array Except Self** 🚀

## **Problem Statement** 🧮

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` **except** `nums[i]`.

### **Constraints**:
- You cannot use the division operation.
- The algorithm must run in **O(n)** time.
- Solve the problem using **O(1)** extra space complexity (the output array does not count as extra space).



## **Approach** 💡

To solve this problem, we can leverage the concept of **prefix and suffix products** without explicitly creating separate arrays for them. Instead, we compute the prefix and suffix products on the fly and store the results directly in the output array.

### **Detailed Logic** 🤔

1. **Prefix Product**:
   - The prefix product for an element at index `i` is the product of all elements to the left of `i`.
   - We calculate this by iterating from left to right and maintaining a running product.

2. **Suffix Product**:
   - The suffix product for an element at index `i` is the product of all elements to the right of `i`.
   - We calculate this by iterating from right to left and maintaining a running product.

3. **Combining Prefix and Suffix**:
   - For each index `i`, the result is the product of the prefix product (left side) and the suffix product (right side).
   - By calculating the prefix and suffix products in two passes, we avoid using division and achieve **O(n)** time complexity.

4. **Space Optimization**:
   - Instead of using additional arrays for prefix and suffix products, we compute them directly in the output array (`answer`) and reuse it during the second pass.


## **Step-by-Step Iteration** 🔍

### Example Input:
```python
nums = [1, 2, 3, 4]
```

#### **Pass 1: Compute Prefix Products**
- Initialize `answer = [1, 1, 1, 1]` (output array).
- Use a variable `prefix = 1` to track the running product.
- Iterate from left to right:
  - `answer[0] = 1` (no elements to the left of index 0).
  - `prefix = prefix * nums[0] = 1 * 1 = 1`.
  - `answer[1] = prefix = 1`.
  - `prefix = prefix * nums[1] = 1 * 2 = 2`.
  - `answer[2] = prefix = 2`.
  - `prefix = prefix * nums[2] = 2 * 3 = 6`.
  - `answer[3] = prefix = 6`.
- After Pass 1: `answer = [1, 1, 2, 6]`.

#### **Pass 2: Compute Suffix Products**
- Use a variable `suffix = 1` to track the running product.
- Iterate from right to left:
  - `suffix = suffix * nums[3] = 1 * 4 = 4`.
  - `answer[3] = answer[3] * suffix = 6 * 1 = 6`.
  - `suffix = suffix * nums[2] = 4 * 3 = 12`.
  - `answer[2] = answer[2] * suffix = 2 * 4 = 8`.
  - `suffix = suffix * nums[1] = 12 * 2 = 24`.
  - `answer[1] = answer[1] * suffix = 1 * 12 = 12`.
  - `suffix = suffix * nums[0] = 24 * 1 = 24`.
  - `answer[0] = answer[0] * suffix = 1 * 24 = 24`.
- Final Output: `answer = [24, 12, 8, 6]`.



## **Core Logic Code Explanation** 🛠️

Here’s the Python implementation:

```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Initialize output array with 1s
    
    # Pass 1: Compute prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix  # Store prefix product in answer
        prefix *= nums[i]   # Update prefix product
    
    # Pass 2: Compute suffix products and combine with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix  # Multiply suffix product into answer
        suffix *= nums[i]    # Update suffix product
    
    return answer
```

### **Explanation of Key Steps**:
1. **Initialization**:
   - Start with `answer = [1, 1, ..., 1]` (size `n`).
   - Use `prefix` and `suffix` variables to track cumulative products.

2. **First Pass (Left to Right)**:
   - Populate `answer` with prefix products.
   - Update `prefix` after each iteration.

3. **Second Pass (Right to Left)**:
   - Multiply `answer[i]` with the suffix product.
   - Update `suffix` after each iteration.

4. **Result**:
   - The final `answer` array contains the desired product of all elements except `nums[i]`.



## **Time and Space Complexity** ⏱️

### **Time Complexity**:
- **O(n)**: Two linear passes through the array (one for prefix, one for suffix).

### **Space Complexity**:
- **O(1)**: No additional space is used apart from the output array (`answer`), which does not count towards extra space.



## **Examples** 📚

### Example 1:
```python
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
```

### Example 2:
```python
nums = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums))  # Output: [0, 0, 9, 0, 0]
```

## **Key Takeaways** 🌟

1. **Prefix and Suffix Concept**: Understand how to compute cumulative products efficiently.
2. **Space Optimization**: Learn how to reuse the output array to achieve O(1) extra space complexity.
3. **Avoid Division**: Solve the problem without using division, adhering to constraints.

This approach ensures an efficient, clean, and elegant solution to the problem. Happy coding! ✨
```