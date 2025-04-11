# 844. Backspace String Compare 🧮  
**Difficulty:** 🟢 Easy  
**Topics:** 🔡 String, 💻 Two Pointers, ⬅️ Stack  
**Companies:** 🏢 Google, 🏢 Facebook  



## Problem Statement 📜  
Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. The character `'#'` represents a **backspace** operation.  

- If a backspace is applied to an empty text, the text remains empty.  



## Examples 🚀  

### Example 1  
**Input:**  
`s = "ab#c"`, `t = "ad#c"`  
**Output:**  
`true`  
**Explanation:**  
Both `s` and `t` become `"ac"` after processing backspaces. ✨  

### Example 2  
**Input:**  
`s = "ab##"`, `t = "c#d#"`  
**Output:**  
`true`  
**Explanation:**  
Both `s` and `t` become `""` (empty strings) after processing backspaces. ✨  

### Example 3  
**Input:**  
`s = "a#c"`, `t = "b"`  
**Output:**  
`false`  
**Explanation:**  
`s` becomes `"c"`, while `t` becomes `"b"`. These are not equal. ❌  



## Constraints ⛓️  
- `1 <= s.length, t.length <= 200`  
- `s` and `t` only contain lowercase letters and `'#'` characters.  



## Follow-Up 💭  
Can you solve it in **O(n)** time and **O(1)** space? 🚀💡  

