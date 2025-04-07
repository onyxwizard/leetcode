# 🚀 LeetCode DSA Solutions Repository 🚀

Welcome to my **LeetCode DSA Solutions** repository! This space is dedicated to solving and documenting solutions to LeetCode problems focused on **Data Structures and Algorithms (DSA)**. Whether you're preparing for technical interviews 💼, improving your problem-solving skills 🧠, or just exploring the beauty of algorithms, this repo is here to help.

---

## 📚 About This Repository

This repository contains Python 🐍 solutions to various LeetCode problems categorized by **data structures** and **algorithms**. Each solution is carefully written to be clean, efficient, and well-documented, making it easy for learners to understand and adapt.

### 🎯 Goals:
- Solve a wide range of DSA problems to strengthen algorithmic thinking.
- Provide clear explanations and optimized code for each problem.
- Create a structured resource for interview preparation and learning.

---
## 🏷️ Categories
| Order               | Description                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------|
| 🧱 **Arrays**          | The most fundamental data structure. Solving array problems helps build a strong foundation in algorithms. |
| ↔️ **Two Pointers**     | Builds on arrays and introduces efficient traversal techniques for solving problems like two-sum and subarray manipulation. |
| 🖇️ **Sliding Window**   | Extends two pointers to solve subarray/substring problems, often used in problems involving contiguous sequences. |
| 🐢🐇 **Fast & Slow Pointers** | Focuses on linked lists and cycle detection, building on pointer manipulation techniques.              |
| 🔍 **Modified Binary Search** | A foundational algorithm for searching in sorted data, often extended to solve more complex variations. |
| 📅 **Merge Intervals**  | Introduces interval-based problems, which are common in real-world applications like scheduling and resource allocation. |
| 🔄 **K-way Merge**      | Extends merging concepts to handle multiple sorted inputs, such as merging k sorted lists or finding the smallest range. |
| ⚖️ **2 Heaps**          | Useful for solving problems involving medians or dynamic sets, leveraging min-heaps and max-heaps.    |
| 🔝 **Top K Elements**   | Builds on heaps and sorting for finding top elements, such as the kth largest element or k closest points. |
| ↪️🔄 **Backtracking**    | Introduces recursion and combinatorial problem-solving, commonly used in problems involving subsets, permutations, and combinations. |
| 💡 **Dynamic Programming (DP)** | A powerful technique for optimization and counting problems, using memoization or tabulation to solve subproblems efficiently. |
| 🌳🌍 **Graph Traversal** | Essential for solving problems involving networks, paths, or connectivity, using algorithms like DFS and BFS. |
| 🔀 **Topological Sorting** | Builds on graph traversal for dependency resolution, commonly used in scheduling and ordering problems. |
| 🌲 **Tree BFS/DFS**     | Fundamental for solving tree-based problems, including level-order traversal, path sums, and tree serialization. |
| 🔗 **In-place Traversal of Linked List** | Advanced linked list manipulation without extra space, focusing on efficient pointer reassignment. |

---

## 📂 Repository Structure

Each problem will have its own folder with the following structure:
```
/problems
  ├── {Problem_Name}/
  │     ├── solution.py       # Python solution file
  │     ├── README.md         # Problem description, approach, and complexity analysis
  │     └── test_cases.py     # Sample test cases (optional)
```

---

## 🛠️ How to Use This Repository

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/onyxwizard/leetcode.git
   cd leetcode
   ```
2. **Explore Solutions:**
    ```
    Navigate through the /problems directory to find solutions by category or difficulty.
    ```
3. **Run the Code:**
    ```
    Open the solution.py file in your favorite Python IDE or run it directly:
    ```
4. **Contribute:** 
      
    Contributions are welcome! If you'd like to add a new solution or improve an existing one, feel free to open a     pull request.

---
# 🌟 Arrays Problems

Below is the list of problems under the **Arrays** pattern:

| Problem | Difficulty | Acceptance Rate | Progress | Link | Solution |
|---------|------------|-----------------|----------|------|----------|
| 448. Find All Numbers Disappeared in an Array | Easy | 62.1% | 🟩 | [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [📝](https://github.com/onyxwizard/leetcode/blob/main/Arrays/448_find-all-numbers-disappeared-in-an-array/README.md) |
| 136. Single Number | Easy | 75.5% | 🟩 | [LeetCode](https://leetcode.com/problems/single-number/) | [📝](https://github.com/onyxwizard/leetcode/blob/main/Arrays/136_singlenumber/README.md)|
| 268. Missing Number | Easy | 69.6% | 🟩 | [LeetCode](https://leetcode.com/problems/missing-number/) | [📝](https://github.com/onyxwizard/leetcode/blob/main/Arrays/268_missing-number/README.md)|
| 217. Contains Duplicate | Easy | 62.9% | ⬜ | [LeetCode](https://leetcode.com/problems/contains-duplicate/) | |
| 128. Longest Consecutive Sequence | Medium | 47.1% | ⬜ | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) | |
| 581. Shortest Unsorted Continuous Subarray | Medium | 37.3% | ⬜ | [LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | |
| 73. Set Matrix Zeroes | Medium | 59.2% | ⬜ | [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) | |
| 457. Circular Array Loop | Medium | 35.3% | ⬜ | [LeetCode](https://leetcode.com/problems/circular-array-loop/) | |
| 792. Number of Matching Subsequences | Medium | 50.7% | ⬜ | [LeetCode](https://leetcode.com/problems/number-of-matching-subsequences/) | |
| 238. Product of Array Except Self | Medium | 67.5% | ⬜ | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | |
| 79. Word Search | Medium | 44.8% | ⬜ | [LeetCode](https://leetcode.com/problems/word-search/) | |
| 48. Rotate Image | Medium | 77.4% | ⬜ | [LeetCode](https://leetcode.com/problems/rotate-image/) | |
| 54. Spiral Matrix | Medium | 53.2% | ⬜ | [LeetCode](https://leetcode.com/problems/spiral-matrix/) | |
| 442. Find All Duplicates in an Array | Medium | 76.3% | ⬜ | [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | |
| 287. Find the Duplicate Number | Medium | 62.5% | ⬜ | [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) | |
| 41. First Missing Positive | Hard | 40.8% | ⬜ | [LeetCode](https://leetcode.com/problems/first-missing-positive/) | |

---

# 🌟 Two Pointers Problems

Below is the list of problems under the **Two Pointers** pattern:

| Problem | Difficulty | Acceptance Rate | Progress | Link | Solution |
|---------|------------|-----------------|----------|------|----------|
| 1. Two Sum | Easy | 55.3% | ⬜ | [LeetCode](https://leetcode.com/problems/two-sum/) | |
| 844. Backspace String Compare | Easy | 49.4% | ⬜ | [LeetCode](https://leetcode.com/problems/backspace-string-compare/) | |
| 83. Remove Duplicates from Sorted List | Easy | 54.5% | ⬜ | [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | |
| 977. Squares of a Sorted Array | Easy | 73.1% | ⬜ | [LeetCode](https://leetcode.com/problems/squares-of-a_sorted_array/) | |
| 259. 3Sum Smaller | Medium | 50.9% | ⬜ | [LeetCode](https://leetcode.com/problems/3sum-smaller/) | |
| 713. Subarray Product Less Than K | Medium | 52.5% | ⬜ | [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/) | |
| 11. Container With Most Water | Medium | 57.4% | ⬜ | [LeetCode](https://leetcode.com/problems/container-with-most-water/) | |
| 75. Sort Colors | Medium | 66.6% | ⬜ | [LeetCode](https://leetcode.com/problems/sort-colors/) | |
| 15. 3Sum | Medium | 36.6% | ⬜ | [LeetCode](https://leetcode.com/problems/3sum/) | |
| 16. 3Sum Closest | Medium | 46.7% | ⬜ | [LeetCode](https://leetcode.com/problems/3sum-closest/) | |
| 42. Trapping Rain Water | Hard | 64.5% | ⬜ | [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | |
| 76. Minimum Window Substring | Hard | 44.9% | ⬜ | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | |

---

# 🌟 Sliding Window Problems

Below is the list of problems under the **Sliding Window** pattern:

| Problem | Difficulty | Acceptance Rate | Progress | Link | Solution |
|---------|------------|-----------------|----------|------|----------|
| 3. Longest Substring Without Repeating Characters | Medium | 36.5% | ⬜ | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | |
| 424. Longest Repeating Character Replacement | Medium | 56.6% | ⬜ | [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) | |
| 904. Fruit Into Baskets | Medium | 45.8% | ⬜ | [LeetCode](https://leetcode.com/problems/fruit-into-baskets/) | |
| 209. Minimum Size Subarray Sum | Medium | 48.9% | ⬜ | [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) | |
| 340. Longest Substring with At Most K Distinct Characters | Medium | 49.4% | ⬜ | [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) | |
| 567. Permutation in String | Medium | 46.9% | ⬜ | [LeetCode](https://leetcode.com/problems/permutation-in-string/) | |
| 76. Minimum Window Substring | Hard | 44.9% | ⬜ | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | |
| 828. Count Unique Characters of All Substrings of a Given String | Hard | 52.7% | ⬜ | [LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/) | |
| 239. Sliding Window Maximum | Hard | 47.3% | ⬜ | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | |
| 995. Minimum Number of K Consecutive Bit Flips | Hard | 62.1% | ⬜ | [LeetCode](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | |
| 30. Substring with Concatenation of All Words | Hard | 32.8% | ⬜ | [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | |

---

# 🌟 Fast & Slow Pointers Problems

Below is the list of problems under the **Fast & Slow Pointers** pattern:

| Problem Number | Title                          | Difficulty | Acceptance Rate | Status | Platform | Solution |
|----------------|--------------------------------|------------|-----------------|--------|----------|----------|
| 234            | Palindrome Linked List         | Easy       | 55.4%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 203            | Remove Linked List Elements    | Easy       | 51.4%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 876           | Middle of the Linked List      | Easy       | 80.3%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 141           | Linked List Cycle              | Easy       | 52.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 83            | Remove Duplicates from Sorted List | Easy    | 54.5%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 2             | Add Two Numbers                | Medium     | 45.7%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 142           | Linked List Cycle II           | Medium     | 54.3%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 143           | Reorder List                   | Medium     | 61.9%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 19            | Remove Nth Node From End of List | Medium   | 48.4%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 148           | Sort List                      | Medium     | 61.1%           | ⬜      | [LeetCode](https://leetcode.com) | |

---

# 🌟 Modified Binary Search Problems

Below is the list of problems under the **Modified Binary Search** pattern:

| Problem Number | Title                                | Difficulty | Acceptance Rate | Status | Platform | Solution |
|----------------|--------------------------------------|------------|-----------------|--------|----------|----------|
| 704            | Binary Search                        | Easy       | 59.3%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 744            | Find Smallest Letter Greater Than Target | Easy    | 53.7%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 33             | Search in Rotated Sorted Array       | Medium     | 42.5%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 162            | Find Peak Element                    | Medium     | 46.4%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 74             | Search a 2D Matrix                   | Medium     | 51.9%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 81             | Search in Rotated Sorted Array II    | Medium     | 38.7%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 852            | Peak Index in a Mountain Array       | Medium     | 67.7%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 153            | Find Minimum in Rotated Sorted Array | Medium     | 52.3%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 327            | Count of Range Sum                  | Hard       | 36.7%           | ⬜      | [LeetCode](https://leetcode.com) | |

---

# 🌟 Merge Intervals Problems

Below is the list of problems under the **Merge Intervals** pattern:

| Problem Number | Title                                   | Difficulty | Acceptance Rate | Status | Platform | Solution |
|----------------|-----------------------------------------|------------|-----------------|--------|----------|----------|
| 252            | Meeting Rooms                           | Easy       | 58.8%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 435            | Non-overlapping Intervals               | Medium     | 55.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 452            | Minimum Number of Arrows to Burst Balloons | Medium  | 60.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 56             | Merge Intervals                         | Medium     | 49.0%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 57             | Insert Interval                         | Medium     | 43.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 621            | Task Scheduler                          | Medium     | 61.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 986            | Interval List Intersections             | Medium     | 72.5%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 253            | Meeting Rooms II                        | Medium     | 52.0%           | ⬜      | [LeetCode](https://leetcode.com) | |

---

# 🌟 K-Way Merge Problems

Below is the list of problems under the **K-Way Merge** pattern:

| Problem Number | Title                                | Difficulty | Acceptance Rate | Status | Platform | Solution |
|----------------|--------------------------------------|------------|-----------------|--------|----------|----------|
| 21             | Merge Two Sorted Lists               | Easy       | 66.5%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 373            | Find K Pairs with Smallest Sums      | Medium     | 40.5%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 378            | Kth Smallest Element in a Sorted Matrix | Medium | 63.3%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 23             | Merge k Sorted Lists                 | Hard       | 56.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 632            | Smallest Range Covering Elements from K Lists | Hard | 69.7% | ⬜ | [LeetCode](https://leetcode.com) | |

---

# 🌟 2 Heaps Problems

Below is the list of problems under the **2 Heaps** pattern:

| Problem Number | Title                                | Difficulty | Acceptance Rate | Status | Platform | Solution |
|----------------|--------------------------------------|------------|-----------------|--------|----------|----------|
| 295            | Find Median from Data Stream         | Hard       | 53.1%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 480            | Sliding Window Median                | Hard       | 38.6%           | ⬜      | [LeetCode](https://leetcode.com) | |
| 502            | IPO                                  | Hard       | 53.0%           | ⬜      | [LeetCode](https://leetcode.com) | |

---


# 📈 Progress Tracker

| Pattern                  | Progress          |
|--------------------------|-------------------|
| Arrays                   | 🟩⬜⬜⬜⬜       |
| Two Pointers             | ⬜⬜⬜⬜⬜       |
| Sliding Window           | ⬜⬜⬜⬜⬜       |
| Fast & Slow Pointers     | ⬜⬜⬜⬜⬜       |
| Modified Binary Search   | ⬜⬜⬜⬜⬜       |
| Merge Intervals          | ⬜⬜⬜⬜⬜       |
| K-way Merge              | ⬜⬜⬜⬜⬜       |
| 2 Heaps                  | ⬜⬜⬜⬜⬜       |
| Top K Elements           | ⬜⬜⬜⬜⬜       |
| Backtracking             | ⬜⬜⬜⬜⬜       |
| Dynamic Programming      | ⬜⬜⬜⬜⬜       |
| Graph Traversal          | ⬜⬜⬜⬜⬜       |
| Topological Sorting      | ⬜⬜⬜⬜⬜       |
| Tree BFS                 | ⬜⬜⬜⬜⬜       |
| Tree DFS                 | ⬜⬜⬜⬜⬜       |
| In-place Traversal of LL | ⬜⬜⬜⬜⬜       |
---

# 📜 License

This repository is licensed under the **MIT License**. Feel free to use, modify, and distribute the code as per the license terms. Attribution is appreciated but not mandatory.

For more details, see the [LICENSE](LICENSE) file.

---

# 🌟 Acknowledgments

- Special thanks to [LeetCode](https://leetcode.com/) for providing an incredible platform to practice DSA problems.
- Some solutions may have been inspired or refined with the help of AI tools like ChatGPT or GitHub Copilot.
