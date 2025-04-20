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



### Constraints ⛓️  
- `1 <= s.length, t.length <= 200`  
- `s` and `t` only contain lowercase letters and `'#'` characters.  



### Follow-Up 💭  
Can you solve it in **O(n)** time and **O(1)** space? 🚀💡  



## Problem Overview 📝

Given two strings `s` and `t`, we need to determine if they are equal after processing backspace characters (`#`). A backspace deletes the previous character (if it exists). For example:

- `s = "ab#c"`, `t = "ad#c"` → Both become `"ac"`, so return `true`.
- `s = "ab##"`, `t = "c#d#"` → Both become `""`, so return `true`.
- `s = "a#c"`, `t = "b"` → `s` becomes `"c"`, `t` becomes `"b"`, so return `false`.

**Constraints**:

- `1 <= s.length, t.length <= 200`
- Strings contain only lowercase letters and `#`.

**Goal**: Solve it in **O(n) time** and **O(1) space** as per the follow-up challenge. 🏆

## Approach: Two-Pointer Magic ✨

We use a **two-pointer approach** to process both strings backward, finding and comparing valid characters (those not deleted by backspaces). Here's how it works:

### Key Idea 💡

- Traverse both strings (`s` and `t`) from the end using pointers `left` and `right`.
- For each string, skip characters deleted by backspaces using a helper function (`get_valid_char`).
- Compare the valid characters. If they differ, the strings are not equal. If both strings are exhausted simultaneously, they are equal.

### Helper Function: `get_valid_char` 🛠️

The `get_valid_char(string, index)` function finds the next valid character in a string starting from `index`, moving backward:

- **Track backspaces**: Use a `backspace` counter.
- **Process characters**:
    - If `string[index] == '#'`, increment `backspace` (indicating a character should be skipped).
    - If `string[index]` is a letter and `backspace > 0`, skip the letter and decrement `backspace`.
    - If `string[index]` is a letter and `backspace == 0`, return `index` (valid character).
- **End of string**: If `index < 0`, return `-1` (no valid characters left).



## Example Walkthrough 🌟

### Example 1: `s = "ab#c"`, `t = "ad#c"`

- **Initial**: `left = 3`, `right = 3`.
- **Step 1**:
    - `get_valid_char(s, 3)`: `s[3] = 'c'`, return `3`.
    - `get_valid_char(t, 3)`: `t[3] = 'c'`, return `3`.
    - Compare `s[3] = 'c'` vs `t[3] = 'c'`: Equal.
    - `left = 2`, `right = 2`.
- **Step 2**:
    - `get_valid_char(s, 2)`: `s[2] = '#'`, `s[1] = 'b'` (skip), `s[0] = 'a'`, return `0`.
    - `get_valid_char(t, 2)`: `t[2] = '#'`, `t[1] = 'd'` (skip), `t[0] = 'a'`, return `0`.
    - Compare `s[0] = 'a'` vs `t[0] = 'a'`: Equal.
    - `left = -1`, `right = -1`.
- **Step 3**: Both exhausted (`left < 0`, `right < 0`), return `true`.
- **Output**: `true` (both become `"ac"`).

### Example 2: `s = "ab##"`, `t = "c#d#"`

- Both strings process to `""`, return `true`.

### Example 3: `s = "a#c"`, `t = "b"`

- `s` processes to `"c"`, `t` to `"b"`, characters differ, return `false`.

## Time and Space Complexity ⏱️💾

- **Time Complexity**: **O(n)** 🕒
    - Each character in both strings is processed at most once.
    - The `get_valid_char` function moves the index backward, and each character is visited at most once across all calls.
    - For strings of length `n` and `m`, the total time is O(n + m), simplified to O(n) where `n` is the length of the longer string.
- **Space Complexity**: **O(1)** 💿
    - Only uses a constant amount of extra space: `left`, `right`, and `backspace` variables.
    - No additional data structures (e.g., stacks or arrays) are needed.
- Meets the follow-up challenge of O(n) time and O(1) space! 🎉

## Why This Approach? 🤔

- **Efficiency**: Achieves optimal time and space complexity.
- **Simplicity**: The backward traversal avoids processing the entire string upfront, making it intuitive for backspace handling.
- **Robustness**: Handles all edge cases, including empty strings, multiple backspaces, and unequal lengths.

## Alternative Approaches 🔍

- **Stack-Based (O(n) time, O(n) space)**:
    - Process each string into its final form using a stack, then compare.
    - Simpler but uses O(n) space, not meeting the follow-up.
- **String Building (O(n) time, O(n) space)**:
    - Build the final strings by processing characters and backspaces.
    - Similar to the stack approach, but less efficient in space.

## Conclusion 🌟

The two-pointer approach is a clean, efficient solution for the Backspace String Compare problem. It processes strings in-place, compares valid characters directly, and achieves the coveted O(n) time and O(1) space complexity. Try it out and see the magic of backspaces in action! 🚀

For questions or feedback, feel free to reach out! 😊