# 287. Find the Duplicate Number 🔍



## Problem Statement 📝

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is **only one repeated number** in `nums`. Return this repeated number.

### Constraints:
- You must solve the problem **without modifying the array `nums`**.
- You must use only **constant extra space** (O(1)).



### Example 1: 🌟

**Input:**  
`nums = [1, 3, 4, 2, 2]`

**Output:**  
`2`

**Explanation:**  
The number `2` appears twice in the array.



### Example 2: 🌟

**Input:**  
`nums = [3, 1, 3, 4, 2]`

**Output:**  
`3`

**Explanation:**  
The number `3` appears twice in the array.


### Example 3: 🌟

**Input:**  
`nums = [3, 3, 3, 3, 3]`

**Output:**  
`3`

**Explanation:**  
All elements are the same, so the duplicate is `3`.



### Constraints ⚖️

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.


### Follow Up 💡

1. **How can we prove that at least one duplicate number must exist in `nums`?**
   - By the **Pigeonhole Principle**, since there are `n + 1` numbers but only `n` unique values (`1` to `n`), at least one number must be repeated.

2. **Can you solve the problem in linear runtime complexity?**
   - Yes! Using techniques like **Floyd's Tortoise and Hare (Cycle Detection)**, we can solve the problem in **O(n)** time with **O(1)** space.



## Approaches to Solve the Problem 🛠️

Here are all possible approaches to solve the problem, along with their explanations:



### Approach 1: Brute Force (Nested Loops) ❌

#### Explanation:
- Compare every pair of elements in the array to find the duplicate.
- If `nums[i] == nums[j]` for any `i != j`, return `nums[i]`.

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
```

#### Time Complexity: ⏳
- **O(n²)**: Two nested loops iterate over all pairs of elements.

#### Space Complexity: 🗄️
- **O(1)**: No additional space is used.

#### Drawbacks:
- This approach is inefficient for large arrays (`n > 10^4`) and will exceed time limits for large inputs.



### Approach 2: Sorting ✨

#### Explanation:
- Sort the array first. After sorting, the duplicate number will appear next to itself.
- Iterate through the sorted array and check if `nums[i] == nums[i+1]`.

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
```

#### Time Complexity: ⏳
- **O(n log n)**: Sorting takes **O(n log n)**, and iterating through the array takes **O(n)**.

#### Space Complexity: 🗄️
- **O(1)**: Sorting is done in-place, so no additional space is used.

#### Drawbacks:
- Modifies the input array by sorting it, violating the constraint of not modifying the array.



### Approach 3: Hash Set (Extra Space) ✨

#### Explanation:
- Use a hash set to track visited numbers.
- For each number in the array, check if it already exists in the set. If yes, return it as the duplicate.

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```

#### Time Complexity: ⏳
- **O(n)**: Each element is processed once.

#### Space Complexity: 🗄️
- **O(n)**: The hash set stores up to `n` elements.

#### Drawbacks:
- Uses **O(n)** extra space, violating the constant space constraint.



### Approach 4: Negative Marking (Array Modification) ✨

#### Explanation:
- Use the indices of the array as markers.
- For each number `num`, negate the value at index `abs(num)`. If the value at that index is already negative, it means `num` is a duplicate.

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                return index
            nums[index] = -nums[index]
```

#### Time Complexity: ⏳
- **O(n)**: Each element is processed once.

#### Space Complexity: 🗄️
- **O(1)**: No additional space is used.

#### Drawbacks:
- Modifies the input array by negating values, violating the constraint of not modifying the array.



### Approach 5: Binary Search (No Modifications) ✨

#### Explanation:
- Perform binary search on the range `[1, n]`:
  - Count how many numbers in `nums` are less than or equal to the midpoint.
  - If the count exceeds the midpoint, the duplicate lies in the left half; otherwise, it lies in the right half.
- Repeat until the duplicate is found.

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low
```

#### Time Complexity: ⏳
- **O(n log n)**: Binary search runs in **O(log n)**, and counting elements takes **O(n)** per iteration.

#### Space Complexity: 🗄️
- **O(1)**: No additional space is used.

#### Advantages:
- Does not modify the array and uses constant space.



### Approach 6: Floyd's Tortoise and Hare (Cycle Detection) ✨

#### Explanation:
- Treat the array as a linked list where each value points to an index.
- Use Floyd's Tortoise and Hare algorithm to detect the cycle caused by the duplicate number.
- Once the cycle is detected, find the entry point of the cycle (the duplicate).

#### Code Implementation:
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect the cycle using Floyd's Tortoise and Hare
        tortoise = hare = nums[0]
        
        # Move tortoise one step and hare two steps
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Step 2: Find the entry point of the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
```

#### Time Complexity: ⏳
- **O(n)**: Cycle detection and finding the entry point both take linear time.

#### Space Complexity: 🗄️
- **O(1)**: No additional space is used.

#### Advantages:
- Efficient (**O(n)** time) and adheres to constraints (no modifications, constant space).



## Comparison of Approaches 📊

| Approach                  | Time Complexity | Space Complexity | Modifies Array? | Meets Constraints? |
|---------------------------|-----------------|-------------------|------------------|--------------------|
| Brute Force               | O(n²)           | O(1)              | No               | ❌                 |
| Sorting                   | O(n log n)      | O(1)              | Yes              | ❌                 |
| Hash Set                  | O(n)            | O(n)              | No               | ❌                 |
| Negative Marking          | O(n)            | O(1)              | Yes              | ❌                 |
| Binary Search             | O(n log n)      | O(1)              | No               | ✅                 |
| Floyd's Tortoise and Hare | O(n)            | O(1)              | No               | ✅                 |



## Key Takeaways 🎯

1. **Floyd's Tortoise and Hare** is the most efficient solution:
   - It runs in **O(n)** time and uses **O(1)** space.
   - It does not modify the input array.

2. **Binary Search** is a good alternative:
   - It runs in **O(n log n)** time and uses **O(1)** space.
   - It also adheres to the constraints.

3. **Other approaches** like brute force, sorting, and hash sets are either too slow or violate constraints.


Happy coding! 🌟