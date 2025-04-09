# 73. Set Matrix Zeroes 🧮
**Medium ⚡**

## Topics 📚
- Arrays 📊
- Matrices 🧩
- In-place Algorithms 🔀

## Problem Statement 📝
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`s ❌.

You must do it **in place** 💾.



### Example 1: 🖥️

![Example1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

**Input**:  
```plaintext
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

**Output**:  
```plaintext
matrix =   [[1,0,1],
            [0,0,0],
            [1,0,1]]
```
### Example 2: 🖥️

![Example2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

**Input**:  
```plaintext
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
```

**Output**:  
```plaintext
matrix =   [[0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]]
```
**Constraints:** ⛓️

- `m == matrix.length` 📏  
- `n == matrix[0].length` 📏  
- `1 <= m, n <= 200` 🔢  
- `-2^31 <= matrix[i][j] <= 2^31 - 1` 📉  

<br>

**Follow Up:** 🤔  

- A straightforward solution using **O(mn)** space is probably a bad idea 🙅‍♂️.  
- A simple improvement uses **O(m + n)** space, but still not the best solution 🤷‍♀️.  
- Could you devise a **constant space** solution? 🎯  



### Step-by-Step Explanation 🔍

#### **Step 1: Check if the First Row and First Column Contain Zeros** 🔎
```python
first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))  
first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
```

- **What’s Happening?** 🤷‍♂️  
  - We check if the **first row** (`matrix[0][...]`) contains any zeros. ❌  
  - We also check if the **first column** (`matrix[...][0]`) contains any zeros. ❌  
  - These checks are stored in two boolean variables:  
    - `first_row_has_zero`: `True` if the first row has a zero, `False` otherwise.  
    - `first_col_has_zero`: `True` if the first column has a zero, `False` otherwise.  

- **Why Do This?** 🤔  
  - The first row and first column will later be used as markers to indicate which rows and columns need to be zeroed out. 📌  
  - However, if the first row or column itself contains zeros, we need to handle them separately at the end. Otherwise, they might interfere with the marking process. ⚠️  



#### **Step 2: Mark Rows and Columns That Need to Be Zeroed** 📍
```python
for i in range(1, m):  
    for j in range(1, n):  
        if matrix[i][j] == 0:|  
            matrix[i][0] = 0  # Mark the row 
            matrix[0][j] = 0  # Mark the column
```

- **What’s Happening?** 🤷‍♀️  
  - We iterate through the matrix starting from the second row and second column (`i = 1`, `j = 1`), skipping the first row and first column.  
  - If we find a zero at position `(i, j)`, we mark:  
    - The **first cell of the row** (`matrix[i][0]`) as `0`. 🟩  
    - The **first cell of the column** (`matrix[0][j]`) as `0`. 🟥  

- **Why Do This?** 🤔  
  - This step uses the first row and first column as markers to remember which rows and columns need to be zeroed out later. 📌  
  - For example, if `matrix[1][2] == 0`, we mark:  
    - `matrix[1][0] = 0` (indicating row 1 needs to be zeroed).  
    - `matrix[0][2] = 0` (indicating column 2 needs to be zeroed).  


- **Example Walkthrough** 🧩  
    Input:  
     ```plaintext
      [[1, 1, 1],  
       [1, 0, 1],  
       [1, 1, 1]]
    ```
    After this step:
    ```bash
    [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
    ```
    
    - **`matrix[1][1] == 0`**, so we mark:
      - **`matrix[1][0] = 0`** (row 1 needs to be zeroed).
      - **`matrix[0][1] = 0`** (column 1 needs to be zeroed).



#### **Step 3: Zero Out Cells Based on Markers** ✨

```plaintext
for i in range(1, m):  
    for j in range(1, n): 
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0
```

- **What’s Happening?** 🤷‍♂️  
  - We iterate through the matrix again, starting from the second row and second column (`i = 1`, `j = 1`).  
  - For each cell `(i, j)`, we check:  
    - If the corresponding row marker (`matrix[i][0]`) is `0`, set `matrix[i][j] = 0`. 🟩  
    - If the corresponding column marker (`matrix[0][j]`) is `0`, set `matrix[i][j] = 0`. 🟥  

- **Why Do This?** 🤔  
  - This step applies the zeroing based on the markers we set in Step 2.  
  - It ensures that all cells in rows and columns marked for zeroing are set to `0`. ❌  

- **Example Walkthrough** 🧩  
  From the previous step: 
  ```plaintext
  [[1, 0, 1],  
   [1, 0, 1],  
   [1, 1, 1]]  
  ```
     After this step:
     ```plaintext
      [[1, 0, 1],  
       [0, 0, 0],  
       [1, 0, 1]]  
     ```



#### **Step 4: Zero Out the First Row (if Needed)** 🟩

```plaintext
if first_row_has_zero: 
   for j in range(n): 
        matrix[0][j] = 0
```

- **What’s Happening?** 🤷‍♀️  
  - If `first_row_has_zero` is `True` (from Step 1), we set all elements in the first row to `0`.  

- **Why Do This?** 🤔  
  - Since the first row was used as a marker in Step 2, it wasn’t modified earlier. Now we handle it separately based on the initial check.  

- **Example Walkthrough** 🧩  
  If `first_row_has_zero = True`:
  ```plaintext
   [[1, 0, 1],  
    [0, 0, 0],  
    [1, 0, 1]]
  ```
  

  After this step: 
  ```plaintext
  [[0, 0, 0],  
   [0, 0, 0],  
   [1, 0, 1]]
  ```
  


#### **Step 5: Zero Out the First Column (if Needed)** 🟥

```plaintext
if first_col_has_zero:  
    for i in range(m):  
        matrix[i][0] = 0
```

- **What’s Happening?** 🤷‍♂️  
  - If `first_col_has_zero` is `True` (from Step 1), we set all elements in the first column to `0`.  

- **Why Do This?** 🤔  
  - Similar to the first row, the first column was used as a marker in Step 2, so it wasn’t modified earlier. Now we handle it separately based on the initial check.  

- **Example Walkthrough** 🧩  
  If `first_col_has_zero = True`: 
    ```plaintext
  [[0, 0, 0],  
   [0, 0, 0],  
   [1, 0, 1]] 
  ```
    After this step:
    ```plaintext
  [[0, 0, 0],  
   [0, 0, 0],  
   [0, 0, 1]]
  ``` 
      



### Final Output 🎯
After completing all five steps, the matrix will have been modified in place to reflect the desired result.  

### Code :
```python
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Use the first row and first column as markers
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 2: Mark rows and columns that need to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Step 3: Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 5: Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        return matrix
if __name__ == "__main__":
    zero = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(zero.setZeroes(matrix))
```

### Summary of Steps 📋
1. **Check if the first row and first column contain zeros** (store results in `first_row_has_zero` and `first_col_has_zero`). 🔎  
2. **Mark rows and columns that need to be zeroed** using the first row and first column as markers. 📍  
3. **Zero out cells based on the markers** (apply changes to the matrix). ✨  
4. **Zero out the first row** (if needed, based on `first_row_has_zero`). 🟩  
5. **Zero out the first column** (if needed, based on `first_col_has_zero`). 🟥  



### Complexity Analysis 📊
- **Time Complexity**: O(m x n) 
  - We traverse the matrix twice: once to mark rows/columns and once to apply the changes.  
- **Space Complexity**: O(1)
  - We use the first row and column of the matrix to store markers, so no additional space is required.  

This approach ensures **constant space complexity** (O(1)) and **optimal time complexity** (O(m x n). 🎉

     
