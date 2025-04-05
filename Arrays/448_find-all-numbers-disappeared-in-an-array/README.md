# 🚀 448. Find All Numbers Disappeared in an Array

## 📚 Topics

- Arrays 🧮  
- Hash Table 🔑


## 💡 Hint

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

### 🌟 Example 1:

**Input:**

```plaintext
nums = [4,3,2,7,8,2,3,1]
```

**Output:**  
```plaintext
[5,6]

```

## ⚖️ Constraints:
```
    n == nums.length

    1 <= n <= 10^5

    1 <= nums[i] <= n
```
## 🤔 Follow-up:

Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

---
# 🛠️ Approaches

## 1️⃣ Brute Force Approach: O(n²) ⏳

This is the simplest approach but not efficient for large inputs. It involves checking every number in the range `[1, n]` to see if it exists in the array.

### Logic Explanation:

- **Outer Loop:** Iterate through all numbers from `1` to `n` (inclusive). These are the numbers we expect to find in the array.
  
- **Inner Check:** For each number in the range, check if it exists in the array using the `in` operator:
  - If the number is missing, add it to the result list.

- **Edge Case:** If the array has only one element, explicitly check if `1` is present or not.

### Why Does This Work?

- The range `[1, n]` represents all possible numbers that could appear in the array.
- By iterating through this range and checking for existence, we can identify which numbers are missing.

### Code:

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappear_item = []
        if len(nums) < 2:
            if nums[0] != 1:
                return [1]
        for item in range(1, len(nums) + 1):
            if item not in nums:
                disappear_item.append(item)
        return disappear_item
```
**Detailed Logic**

- **Time Complexity:** O(n²) because for each number in the range [1, n], we search through the entire array (each operation takes O(n)).

- **Space Complexity:** O(1) (excluding the output list).

- **Drawbacks:** Inefficient for large inputs due to its quadratic time complexity.

---
## 2️⃣ **Array Sort Approach: O(n log n) 🔄**

Sorting the array first allows us to efficiently identify missing numbers by comparing the sorted array with the expected sequence.


### **Logic Explanation:**

1. **Sort the Array:**
   - Sorting rearranges the elements in ascending order, making it easier to detect gaps.

2. **Pointer Initialization:**
   - Use a pointer (`expected`) to track the smallest number we expect to see next. Initially, set `expected = 1`.

3. **Iterate Through the Sorted Array:**
   - For each number in the sorted array:
     - If the current number is greater than `expected`, it means all numbers between `expected` and `current - 1` are missing. Add them to the result.
     - If the current number matches `expected`, increment `expected`.
     - If the current number is less than `expected`, it’s a duplicate, so skip it.

4. **Handle Remaining Numbers:**
   - After the loop, add any remaining numbers from `expected` to `n` (the size of the array).


### **Why Does This Work?**

- Sorting ensures that numbers are in order, allowing us to compare them with the expected sequence.
- By maintaining an `expected` pointer, we can efficiently detect gaps between the sorted numbers and the expected sequence.



### **Code:**

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Initialize variables
        result = []
        expected = 1  # Start expecting the number 1
        n = len(nums)

        # Step 3: Iterate through the sorted array
        for num in nums:
            if num > expected:
                # Add all missing numbers between expected and num - 1
                result.extend(range(expected, num))
            if num == expected:
                # Move to the next expected number
                expected += 1

        # Step 4: Handle remaining numbers after the last element
        result.extend(range(expected, n + 1))

        return result
```
**Detailed Logic:**

- **Time Complexity:** O(n log n) due to sorting.
- **Space Complexity:** O(1) (excluding the output list).
- **Advantages:** More efficient than brute force, especially for moderately sized inputs.

---

## 3️⃣ **Expected Approach: O(n) ⚡**

This is the most efficient solution, leveraging the input array itself to mark the presence of numbers.

#### **Logic Explanation:**

1. **Mark Presence of Numbers:**
   - Iterate through the array.
   - For each number `num`, calculate its corresponding index as `abs(num) - 1` (since indices are 0-based).
   - Mark the value at this index as negative to indicate that the number `num` is present.

2. **Identify Missing Numbers:**
   - After marking, traverse the array again.
   - If a value at index `i` is positive, it means the number `i + 1` is missing (since it was never marked as negative).
   - Collect all such missing numbers.

#### **Why Does This Work?**

- By marking the presence of numbers in-place, we avoid using extra space.
- Negative values act as "flags" to indicate the presence of numbers, allowing us to identify missing ones efficiently.

---

### **Code:**

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark the presence of each number
        for num in nums:
            index = abs(num) - 1  # Map number to index (1-based to 0-based)
            nums[index] = -abs(nums[index])  # Mark as negative

        # Step 2: Collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:  # If still positive, number (i+1) never appeared
                result.append(i + 1)

        return result
```