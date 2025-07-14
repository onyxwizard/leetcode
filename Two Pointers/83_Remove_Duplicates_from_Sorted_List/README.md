# LeetCode 83: Remove Duplicates from Sorted List

## 📌 Problem Description

Given the head of a **sorted** singly linked list, delete all duplicates such that each element appears **only once**. The resulting linked list should remain sorted.



## 🧠 Problem Analysis

### Key Observations:
- The list is **sorted in ascending order**, so **duplicates are consecutive**.
- We can leverage this property to remove duplicates in a **single traversal**.
- We only need to compare each node with its next node to detect duplicates.

### Constraints:
- Number of nodes: `0 ≤ n ≤ 300`
- Node values: `-100 ≤ val ≤ 100`
- The list is **guaranteed to be sorted**.



## 🛠️ Solution Approach

### Strategy:
- Use a **single pointer** (`current`) to traverse the list.
- For each node, compare it with the next node:
  - If they are equal, **bypass** the next node.
  - If not, move the pointer forward.
- This ensures all duplicates are removed **in-place**.

### Why This Works:
- Since the list is sorted, any duplicates are adjacent.
- By comparing `current` and `current.next`, we can **remove duplicates in a single pass**.
- No extra data structures are needed, and the solution uses **constant space**.



## 💻 Code Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate
            else:
                current = current.next  # Move to next unique node
        return head
```



## ⏱️ Time & Space Complexity

- **Time Complexity**: `O(n)`  
  We traverse the list exactly once.
  
- **Space Complexity**: `O(1)`  
  We use only a constant amount of extra space (the `current` pointer).



## 🔍 Step-by-Step Execution

### Example Input:
```python
head = 1 -> 1 -> 2 -> 3 -> 3
```

### Execution Steps:
1. Start at `current = 1`
   - `current.next = 1` → duplicate → set `current.next = 2`
2. `current` still at `1`, `current.next = 2` → not duplicate → move `current = 2`
3. `current = 2`, `current.next = 3` → not duplicate → move `current = 3`
4. `current = 3`, `current.next = 3` → duplicate → set `current.next = None`
5. Loop ends → return `head`

### Final Output:
```python
1 -> 2 -> 3
```


## 🧪 Test Cases

### ✅ Basic Examples:
- **Input:** `1 -> 1 -> 2`  
  **Output:** `1 -> 2`

- **Input:** `1 -> 1 -> 2 -> 3 -> 3`  
  **Output:** `1 -> 2 -> 3`

### 🧪 Edge Cases:
- **Input:** `None` (empty list)  
  **Output:** `None`

- **Input:** `5` (single node)  
  **Output:** `5`

- **Input:** `2 -> 2 -> 2 -> 2`  
  **Output:** `2`

- **Input:** `1 -> 2 -> 3 -> 4`  
  **Output:** `1 -> 2 -> 3 -> 4` (no duplicates)



## ⚠️ Common Mistakes to Avoid

- ❌ **Not updating node pointers** (e.g., only moving the `head` pointer without modifying links)
- ❌ **Not handling multiple duplicates in a row**
- ❌ **Assuming the list is unsorted** (unnecessary use of hash sets or sorting)



## 🧩 Additional Notes

- This approach is **in-place** and does not require extra memory.
- If the list were **not sorted**, we would need to use a **hash set** to track seen values, increasing space complexity to `O(n)`.



## 📚 Summary

This solution efficiently removes duplicates from a **sorted linked list** using a single pointer. It leverages the sorted nature of the list to compare adjacent nodes and remove duplicates in a single pass. The algorithm runs in **linear time** and uses **constant space**, making it optimal for the problem constraints.