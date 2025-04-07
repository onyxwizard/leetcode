# 🚀 136. Single Number

## 📚 Topics

- Bit Manipulation  
- Hash Table 🔑  
- Array 🧮  

## 💡 Problem Statement

Given a non-empty array of integers `nums`, every element appears **twice** except for one. Find that single element.

### ⚡ Requirements:
- Implement a solution with **linear runtime complexity** (O(n)).
- Use only **constant extra space**.


### 🌟 Examples

#### Testcase 1: 
```plaintext
Input: nums = [2, 2, 1]

Output: 1
```

#### Testcase 2:
```plaintext
Input: nums = [4, 1, 2, 1, 2]

Output: 4
```
### ⚖️ Constraints
```bash
1. 1 <= nums.length <= 3 * 10^4
2. -3 * 10^4 <= nums[i] <= 3 * 10^4
3. Each element in the array appears twice except for one element which appears only once.
```

# 🛠️ Approaches


### 1️⃣ Hash Table Approach Using: O(n) Time, O(n) Space

#### What is `defaultdict`?

`defaultdict` is a subclass of Python's built-in `dict` class. It overrides one method (`__missing__`) and adds one writable instance variable (`default_factory`). When accessing a key that does not exist, it automatically initializes the key with a default value (e.g., `int` initializes to `0`).

#### Code:
```python
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_element = defaultdict(int)
        
        # Count occurrences of each number
        for num in nums:
            unique_element[num] += 1
        
        # Find the number with a count of 1
        for key, val in unique_element.items():
            if val == 1:
                return key
```
#### Logic Explanation:

- **Step 1: Initialize `defaultdict`:**  
  We use `defaultdict(int)` to create a dictionary where the default value for any key is `0`.

- **Step 2: Count Occurrences:**  
  Traverse the array and increment the count for each number in the dictionary.  
  For example, if `nums = [4, 1, 2, 1, 2]`, the dictionary will look like:
  ```plaintext
  {4: 1, 1: 2, 2: 2}
  ```
- **Step 3: Identify the Unique Element**
Iterate through the dictionary and check for the key with a value of `1`.  
Return the key corresponding to this value.


#### Why Does This Work?

The dictionary keeps track of how many times each number appears in the array.  
Since all numbers except one appear twice, the number with a count of `1` is the unique element.



#### Detailed Logic

- **Time Complexity:** O(n), as we traverse the array once to build the dictionary and once to find the unique element.  
- **Space Complexity:** O(n), due to the additional space used by the dictionary to store counts.


---
## 2️⃣Expected Approach - XOR Bit Manipulation : O(n) Time, O(1) Space ⚡

#### Code:
```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
```

### Logic Explanation

#### Step 1: Initialize `xor`
Start with `xor = 0`.

#### Step 2: XOR All Numbers
Traverse the array and XOR each number with the current value of `xor`.  
For example, if `nums = [4, 1, 2, 1, 2]`, the steps are:

```plaintext
xor = 0 ^ 4 = 4
xor = 4 ^ 1 = 5
xor = 5 ^ 2 = 7
xor = 7 ^ 1 = 6
xor = 6 ^ 2 = 4
```
At the end, `xor = 4`, which is the unique number.



#### Step 3: Return the Result:
The final value of `xor` is the unique number.



## Why Does This Work?

**Properties of XOR:**  
- `a ^ a = 0`: Any number XORed with itself cancels out.  
- `a ^ 0 = a`: Any number XORed with `0` remains unchanged.  
- XOR is commutative and associative, meaning the order of operations does not matter.

By `XOR`ing all numbers in the array, the pairs will cancel each other out, leaving only the unique number.



### Detailed Logic:

- **Time Complexity:** O(n), as we traverse the array once.  
- **Space Complexity:** O(1), as no additional data structures are used.



## 🎯 Key Takeaways

| Approach              | Time Complexity | Space Complexity | Pros                          | Cons                          |
|-----------------------|-----------------|------------------|-------------------------------|-------------------------------|
| **Hash Table**        | O(n)            | O(n)             | Simple to implement           | Uses extra space              |
| **XOR Bit Manipulation** | O(n)          | O(1)             | Optimal time and space        | Requires understanding of XOR |

---

# 🙌 Conclusion

The **XOR Bit Manipulation Approach** is the most efficient solution for this problem, satisfying the constraints of linear runtime complexity and constant extra space. While the **Hash Table Approach** is straightforward and easy to implement, it uses additional space, which violates the problem's requirements. Understanding bitwise operations like XOR is crucial for solving similar problems optimally. Practice more bit manipulation techniques to strengthen your problem-solving skills! 🚀

