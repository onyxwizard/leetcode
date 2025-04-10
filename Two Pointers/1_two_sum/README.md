# 🌟 Two Sum
**Difficulty:** 🟢 Easy  
**Topics:** 📊 Array, 🗄️ Hash Table  
**Hint:** 💡 Think about using a data structure to improve the solution's time complexity.



## Problem Statement 📜
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`. ✨

You may assume that:
- Each input would have exactly **one solution**. 🔐
- You may **not** use the same element twice. ⚠️

You can return the answer in any order. 🔄



## Examples 🚀

### Example 1
**Input:**  
`nums = [2,7,11,15]`, `target = 9`  
**Output:**  
`[0,1]`  
**Explanation:**  
`nums[0] + nums[1] == 9`, so we return `[0, 1]`. 🧮 ✅


### Example 2
**Input:**  
`nums = [3,2,4]`, `target = 6`  
**Output:**  
`[1,2]` ✔️


### Example 3
**Input:**  
`nums = [3,3]`, `target = 6`  
**Output:**  
`[0,1]` 💯



## Constraints ⛓️
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.** 🛡️


## Follow-up 💭
Can you come up with an algorithm that is **less than O(n²)** time complexity? 🚀💡



## Optimization Hint 🌈
🧠 Consider using a **hash table** (dictionary) to store numbers you've seen along with their indices. You can then check if the complement of the current number exists in the table during a single traversal. ⚡



Let me know if you'd like me to sprinkle in any more pizazz or perhaps add some colors to the markdown! 🎉
```