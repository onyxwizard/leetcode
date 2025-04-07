# 🚀 268. Missing Number

## 📚 Topics

- Array 🧮  
- Math ➕  
- Bit Manipulation 🔢  


## 💡 Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### ⚡ Requirements:
- Implement a solution with **linear runtime complexity** (O(n)).
- Use only **constant extra space** (O(1)).

## 🌟 Examples

### Testcase 1:


```plaintext
Input: nums = [3, 0, 1]

Output:  2
```
#### Explanation:  

* `n = 3` since there are 3 numbers, so all numbers are in the range [0, 3].
* `2` is the missing number in the range since it does not appear in nums.
 
### Testcase 2:


```plaintext
Input: nums = [ 0, 1]

Output:  2
```
#### Explanation:  
* `n = 2` since there are 2 numbers, so all numbers are in the range [0, 2].
* `2` is the missing number in the range since it does not appear in nums.
     
### Testcase 3:


```plaintext
Input: nums =nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

Output:  8
```
#### Explanation:  
* `n = 9` since there are 9 numbers, so all numbers are in the range [0, 9].
* `8` is the missing number in the range since it does not appear in nums.

### ⚖️ Constraints
```
1. n == nums.length
2. 1 <= n <= 10^4
3. 0 <= nums[i] <= n
4. All the numbers of nums are unique.
```
### 🤔 Follow-up 
Could you implement a solution using only O(1) extra space complexity  and O(n) runtime complexity ? 

---
# 🛠️ Approaches in Detail

## 1️⃣ XOR Bit Manipulation Approach: O(n) Time, O(1) Space ⚡

### Logic Explanation:

#### Step 1: Initialize `xor_result`
- Start with `xor_result = 0`. This variable will hold the cumulative XOR result of all numbers in the array and the range `[0, n]`.

#### Step 2: XOR All Numbers in the Array
- Traverse the array and XOR each number with `xor_result`.
- This ensures that all numbers present in the array are included in the XOR operation.

#### Step 3: XOR All Numbers in the Range `[0, n]`
- Traverse the range `[0, n]` (inclusive) and XOR each number with `xor_result`.
- This includes all numbers that should be present in the range.

#### Step 4: Return the Result
- After both loops, `xor_result` will contain the missing number because:
  - Numbers appearing twice (once in the array and once in the range) cancel out (`a ^ a = 0`).
  - The missing number appears only once, leaving it as the final result.

### Why Does This Work?

- **Properties of XOR:**
  - `a ^ a = 0`: Any number XORed with itself cancels out.
  - `a ^ 0 = a`: Any number XORed with `0` remains unchanged.
  - XOR is commutative and associative, meaning the order of operations does not matter.

- By XORing all numbers in the array and the range `[0, n]`, duplicates cancel out, leaving only the missing number.


### Example Walkthrough:

#### Input:
```plaintext
nums = [3, 0, 1]
```
### Execution Steps:

- Initialize `xor_result = 0`.
- XOR all numbers in the array:
  - `xor_result = 0 ^ 3 = 3`
  - `xor_result = 3 ^ 0 = 3`
  - `xor_result = 3 ^ 1 = 2`
- XOR all numbers in the range `[0, 3]`:
  - `xor_result = 2 ^ 0 = 2`
  - `xor_result = 2 ^ 1 = 3`
  - `xor_result = 3 ^ 2 = 1`
  - `xor_result = 1 ^ 3 = 2`
- Final `xor_result = 2`, which is the missing number.


### Detailed Logic:

- **Time Complexity:** O(n)  
  We traverse the array once (O(n)) and the range `[0, n]` once (O(n)), resulting in linear time complexity.
  
- **Space Complexity:** O(1)  
  No additional data structures are used, so the space complexity is constant.

---

## 2️⃣ Sum Formula Approach: O(n) Time, O(1) Space

### Logic Explanation:

#### Step 1: Calculate the Expected Sum
- Use the formula for the sum of the first `n` natural numbers:
```
expected_sum = n * (n + 1) / 2
```
This gives the total sum of all numbers in the range `[0, n]`.

#### Step 2: Calculate the Actual Sum
- Traverse the array and calculate the sum of all numbers present in the array.

#### Step 3: Find the Missing Number
- Subtract the actual sum from the expected sum:
```
missing_number = expected_sum - actual_sum
```

### Why Does This Work?

- The sum formula guarantees the total of all numbers in the range `[0, n]`.
- By subtracting the sum of the array from this total, we isolate the missing number.


### Example Walkthrough:

**Input:** nums = [3, 0, 1]

### Execution Steps:
- Calculate the expected sum:
  - `expected_sum = 3 * (3 + 1) / 2 = 6`
- Calculate the actual sum:
  - `actual_sum = 3 + 0 + 1 = 4`
- Find the missing number:
  - `missing_number = 6 - 4 = 2`


### Detailed Logic:

- **Time Complexity:** O(n), as we traverse the array once to calculate the sum.
- **Space Complexity:** O(1), as no additional data structures are used.

---
## 3️⃣ Sorting Approach: O(n log n) Time, O(1) Space

### Logic Explanation:

#### Step 1: Sort the Array
- Sort the array in ascending order.

#### Step 2: Compare Indices with Values
- Iterate through the sorted array and compare each index with its corresponding value:
  - If the index does not match the value, the index is the missing number.

#### Step 3: Handle Edge Case
- If no mismatch is found during the iteration, the missing number is `n`.



### Why Does This Work?

- Sorting ensures that numbers are in their correct positions, except for the missing number.
- By comparing indices with values, we can detect the missing number.


### Example Walkthrough:

**Input:** nums = [3, 0, 1]

### Execution Steps:

- Sort the array:
  - Sorted array: `[0, 1, 3]`
- Compare indices with values:
  - Index `0` matches value `0`.
  - Index `1` matches value `1`.
  - Index `2` does not match value `3`.
- The missing number is `2`.



### Detailed Logic:

- **Time Complexity:** O(n log n), due to sorting.
- **Space Complexity:** O(1), if sorting is done in-place.



# 🎯 Key Takeaways

| Approach              | Time Complexity | Space Complexity | Pros                          | Cons                          |
|-----------------------|-----------------|------------------|-------------------------------|-------------------------------|
| **XOR Bit Manipulation** | O(n)          | O(1)             | Optimal time and space        | Requires understanding of XOR |
| **Sum Formula**       | O(n)            | O(1)             | Simple and efficient          | Prone to integer overflow     |
| **Sorting**           | O(n log n)      | O(1)             | Easy to understand            | Slower due to sorting         |

# 🙌 Conclusion

The **XOR Bit Manipulation Approach** and **Sum Formula Approach** are the most efficient solutions for this problem, satisfying the constraints of linear runtime complexity and constant extra space. While the **Sorting Approach** is straightforward, it is less efficient due to its reliance on sorting. Understanding bitwise operations like XOR is crucial for solving similar problems optimally. Practice more bit manipulation techniques to strengthen your problem-solving skills! 🚀

---