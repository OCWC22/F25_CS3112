# Chapter 2.2 Exercises: Complete Solutions with Frameworks

**Section:** 2.2 - Analyzing Algorithms  
**Focus:** Running time analysis and algorithm design

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Simplify to Θ** | "express in Θ-notation" | Find dominant term | Identify highest degree, drop constants |
| **Design Algorithm** | "write pseudocode" | Create new algorithm | Design, code, prove, analyze |
| **Analyze Cases** | "best-case", "worst-case", "average-case" | Determine running time | Count operations for each case |
| **Compare Algorithms** | "is best-case better" | Compare different scenarios | Analyze all cases, compare |

---

## Exercise 2.2-1: Express in Θ-Notation

### Problem Statement
Express the function n³/1000 + 100n² - 100n + 3 in terms of Θ-notation.

---

### What This Problem Is Asking

**Task:** Simplify polynomial to asymptotic form
**Goal:** Identify dominant term, drop everything else

### Framework
1. List all terms
2. Identify highest-degree term
3. Drop constant coefficient
4. Express as Θ(term)

---

### Solution

**Step 1: Identify all terms**
```
n³/1000   - cubic term (degree 3)
100n²     - quadratic term (degree 2)
-100n     - linear term (degree 1)
3         - constant term (degree 0)
```

**Step 2: Find highest-degree term**
```
Highest degree: 3
Dominant term: n³/1000
```

**Step 3: Compare growth rates**
```
For large n:
n³/1000 >> 100n²
n³/1000 >> 100n
n³/1000 >> 3

Example (n=1000):
n³/1000 = 1,000,000,000
100n² = 100,000,000
100n = 100,000
3 = 3
```

**Step 4: Drop constant coefficient**
```
n³/1000 → n³
```

**Step 5: Express in Θ-notation**
```
n³/1000 + 100n² - 100n + 3 = Θ(n³)
```

---

### Answer

**Θ(n³)**

**Explanation:** For large n, the n³ term dominates all other terms, and the constant coefficient 1/1000 doesn't affect asymptotic growth.

---

## Exercise 2.2-2: Selection Sort

### Problem Statement
Consider sorting n numbers stored in array A[1 : n] by first finding the smallest element of A[1 : n] and exchanging it with the element in A[1]. Then find the smallest element of A[2 : n], and exchange it with A[2]. Continue in this manner for the first n-1 elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n-1 elements, rather than for all n elements? Give the worst-case running time of selection sort in Θ-notation. Is the best-case running time any better?

---

### What This Problem Is Asking

**Task:** Design, prove, and analyze selection sort
**Components:** Pseudocode + invariant + analysis
**Goal:** Complete algorithm specification

### Framework
1. Write pseudocode
2. State loop invariant
3. Explain why n-1 iterations
4. Analyze worst case
5. Compare with best case

---

### Solution Part 1: Pseudocode

```
SELECTION-SORT(A, n)
1  for i = 1 to n - 1
2      min_index = i
3      for j = i + 1 to n
4          if A[j] < A[min_index]
5              min_index = j
6      swap A[i] with A[min_index]
```

**Line-by-line explanation:**

**Line 1:** Loop through first n-1 positions

**Line 2:** Assume current position has minimum

**Lines 3-5:** Find actual minimum in unsorted portion
- Check all elements from i+1 to n
- Update min_index if find smaller element

**Line 6:** Swap minimum to position i

---

### Solution Part 2: Loop Invariant

**Loop Invariant:**
> At the start of each iteration of the for loop (line 1), the subarray A[1 : i-1] contains the i-1 smallest elements of the original array in sorted order.

**Key properties:**
1. **Smallest elements:** Not original positions, but smallest values
2. **Sorted order:** Arranged in increasing order
3. **From original array:** Permutation of original elements

**Proof:**

**Initialization (i=1):**
- A[1 : 0] is empty
- Trivially contains 0 smallest elements in sorted order ✓

**Maintenance:**
- **Before iteration i:** A[1 : i-1] has i-1 smallest elements, sorted
- **During iteration:** Find minimum of A[i : n], swap to position i
- **After iteration:** A[1 : i] has i smallest elements, sorted
- Invariant maintained ✓

**Termination (i=n):**
- A[1 : n-1] contains n-1 smallest elements
- A[n] must be the largest element (only one left)
- Entire array sorted ✓

---

### Solution Part 3: Why Only n-1 Iterations?

**Reason 1: Last element automatically correct**
- After n-1 iterations, n-1 smallest elements in positions 1 to n-1
- Only one element left: must be the largest
- No need to "select" it

**Reason 2: Nothing to swap with**
- If we ran iteration n, we'd find min of A[n : n]
- That's just A[n] itself
- Swapping A[n] with A[n] does nothing

**Reason 3: Loop invariant**
- At i = n: A[1 : n-1] has n-1 smallest elements
- Only one element remains: must be largest
- Array is sorted

---

### Solution Part 4: Worst-Case Running Time

**Count operations:**

**Outer loop:** n-1 iterations

**Inner loop (for each i):**
```
i=1: n-1 comparisons
i=2: n-2 comparisons
i=3: n-3 comparisons
...
i=n-1: 1 comparison

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2
```

**Swaps:** n-1 swaps (one per outer loop iteration)

**Total operations:**
```
Comparisons: n(n-1)/2 = Θ(n²)
Swaps: n-1 = Θ(n)
Total: Θ(n²) + Θ(n) = Θ(n²)
```

**Worst-case running time: Θ(n²)**

---

### Solution Part 5: Best-Case Running Time

**Question:** Is best case better?

**Answer:** NO!

**Why?**
- Selection sort ALWAYS scans entire unsorted portion
- Even if array is sorted, still makes n(n-1)/2 comparisons
- Cannot exit early

**Best-case running time: Θ(n²)**

**Key difference from insertion sort:**
- Insertion sort: Best case Θ(n) (can exit early)
- Selection sort: Best case Θ(n²) (must scan all)

---

### Complete Answer for 2.2-2

**Pseudocode:** (See above)

**Loop invariant:** A[1 : i-1] contains the i-1 smallest elements in sorted order

**Why n-1 iterations:** Last element automatically in correct position

**Worst-case time:** Θ(n²)

**Best-case time:** Θ(n²) (no better!)

**Comparison with insertion sort:**
- Insertion sort: Best Θ(n), Worst Θ(n²)
- Selection sort: Best Θ(n²), Worst Θ(n²)
- Insertion sort better for nearly-sorted data

---

## Exercise 2.2-3: Linear Search Analysis

### Problem Statement
Consider linear search again (see Exercise 2.1-4). How many elements of the input array need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? Using Θ-notation, give the average-case and worst-case running times of linear search. Justify your answers.

---

### What This Problem Is Asking

**Task:** Analyze average and worst case for linear search
**Assumption:** x equally likely to be any element
**Goal:** Count comparisons, express in Θ-notation

### Framework
1. Identify best/worst/average scenarios
2. Count operations for each
3. Express in Θ-notation
4. Justify reasoning

---

### Solution

**Algorithm (from 2.1-4):**
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

---

**Part 1: Average Case**

**Assumption:** x is equally likely to be at any position

**Analysis:**
- If x at position 1: 1 comparison
- If x at position 2: 2 comparisons
- If x at position 3: 3 comparisons
- ...
- If x at position n: n comparisons

**Probability:** Each position has probability 1/n

**Expected number of comparisons:**
```
E[comparisons] = (1/n) × 1 + (1/n) × 2 + ... + (1/n) × n
                = (1/n)(1 + 2 + 3 + ... + n)
                = (1/n) × n(n+1)/2
                = (n+1)/2
                ≈ n/2
```

**Average case: Check (n+1)/2 elements**

**In Θ-notation: Θ(n)**

---

**Part 2: Worst Case**

**Scenario:** x is not in array OR x is last element

**Analysis:**
- Must check all n elements
- Loop runs n times

**Worst case: Check n elements**

**In Θ-notation: Θ(n)**

---

**Part 3: Justification**

**Why average is Θ(n):**
- Average checks n/2 elements
- n/2 = Θ(n) (constant factor doesn't matter)
- Linear growth in input size

**Why worst is Θ(n):**
- Worst checks n elements
- n = Θ(n) (obviously)
- Linear growth in input size

**Key insight:** Average and worst case have same asymptotic growth!
- Average is about half of worst
- But both are Θ(n)
- Constants don't affect Θ-notation

---

### Answer

**Average case:**
- Elements checked: (n+1)/2 ≈ n/2
- Running time: Θ(n)

**Worst case:**
- Elements checked: n
- Running time: Θ(n)

**Justification:**
- Average checks half the array on average
- Worst checks entire array
- Both are linear in n
- Same asymptotic growth: Θ(n)

---

## Exercise 2.2-4: Modify for Good Best Case

### Problem Statement
How can you modify any sorting algorithm to have a good best-case running time?

---

### What This Problem Is Asking

**Task:** General technique for improving best case
**Context:** Works for ANY sorting algorithm
**Goal:** Achieve Θ(n) best case

### Framework
1. Identify what makes best case good
2. Design check for best case
3. Apply to any algorithm
4. Analyze impact

---

### Solution

**The Trick: Check if Already Sorted First!**

**Modified algorithm structure:**
```
MODIFIED-SORT(A, n)
1  // Check if already sorted
2  for i = 1 to n - 1
3      if A[i] > A[i+1]
4          goto line 6
5  return A  // Already sorted!
6  // Run original sorting algorithm
7  ORIGINAL-SORT(A, n)
8  return A
```

**Alternative (cleaner):**
```
MODIFIED-SORT(A, n)
1  if IS-SORTED(A, n)
2      return A
3  ORIGINAL-SORT(A, n)
4  return A

IS-SORTED(A, n)
1  for i = 1 to n - 1
2      if A[i] > A[i+1]
3          return FALSE
4  return TRUE
```

---

**Analysis:**

**Best case (already sorted):**
- IS-SORTED runs in Θ(n) time
- Original algorithm never runs
- **Total: Θ(n)** ✓

**Worst case (not sorted):**
- IS-SORTED runs in Θ(n) time
- Original algorithm runs in its worst case (e.g., Θ(n²))
- **Total: Θ(n) + Θ(n²) = Θ(n²)**
- No worse than original!

---

**Impact:**

**For insertion sort:**
- Already has Θ(n) best case
- No improvement needed

**For selection sort:**
- Original best case: Θ(n²)
- Modified best case: Θ(n)
- Significant improvement!

**For any algorithm:**
- Best case becomes Θ(n)
- Worst case unchanged
- Small overhead (one extra pass)

---

### Answer

**Technique:** Add a preprocessing check to test if array is already sorted.

**Implementation:**
```
1. Check if A[i] ≤ A[i+1] for all i
2. If yes, return immediately (Θ(n) time)
3. If no, run original algorithm
```

**Result:**
- Best case: Θ(n) (just the check)
- Worst case: Θ(original worst case)
- Overhead: Θ(n) (negligible for Θ(n²) algorithms)

**Justification:**
- Checking takes linear time
- If sorted, save all sorting work
- If not sorted, overhead is small compared to sorting cost

---

## 📋 Quick Reference: All Exercises

### 2.2-1: Simplify to Θ-Notation
```
Function: n³/1000 + 100n² - 100n + 3
Dominant term: n³/1000
Drop constants: n³
Answer: Θ(n³)
```

### 2.2-2: Selection Sort
```
Pseudocode: Find min, swap, repeat
Loop invariant: A[1:i-1] has i-1 smallest elements, sorted
Why n-1: Last element automatically correct
Worst case: Θ(n²)
Best case: Θ(n²) (no better!)
```

### 2.2-3: Linear Search Cases
```
Average: (n+1)/2 checks → Θ(n)
Worst: n checks → Θ(n)
Both linear, same asymptotic growth
```

### 2.2-4: Improve Best Case
```
Technique: Check if sorted first
Best case: Θ(n) (just check)
Worst case: Unchanged
Works for any sorting algorithm
```

---

## 🔑 Key Concepts Summary

### RAM Model
```
✓ Sequential execution
✓ Constant-time operations
✓ Constant-time array access
✓ Simple instructions only
```

### Analysis Process
```
1. Count operations
2. Express as function of n
3. Identify dominant term
4. Drop constants and lower-order terms
5. Express in Θ-notation
```

### Case Analysis
```
Best case: Minimum time (best input)
Worst case: Maximum time (worst input)
Average case: Expected time (random input)
```

### Selection Sort vs Insertion Sort
```
Selection Sort:
- Best: Θ(n²)
- Worst: Θ(n²)
- Always scans entire unsorted portion

Insertion Sort:
- Best: Θ(n)
- Worst: Θ(n²)
- Can exit early if nearly sorted
```

---

## ⚠️ Common Mistakes

### Mistake 1: Keeping Constants
```
✗ Θ(5n²)
✓ Θ(n²)
```

### Mistake 2: Keeping Lower-Order Terms
```
✗ Θ(n² + n)
✓ Θ(n²)
```

### Mistake 3: Wrong Summation
```
✗ Σᵢ₌₁ⁿ i = n²
✓ Σᵢ₌₁ⁿ i = n(n+1)/2 = Θ(n²)
```

### Mistake 4: Confusing Best and Worst
```
✗ "Selection sort best case is Θ(n)"
✓ Selection sort is ALWAYS Θ(n²)
```

### Mistake 5: Wrong Loop Count
```
✗ for i = 1 to n-1 → n iterations
✓ for i = 1 to n-1 → n-1 iterations
```

---

## 🚀 Exam Strategy

### For Θ-Notation (2.2-1)
- [ ] Identify all terms
- [ ] Find highest degree
- [ ] Drop constants
- [ ] State answer clearly

### For Algorithm Design (2.2-2)
- [ ] Write clear pseudocode
- [ ] State loop invariant
- [ ] Prove correctness
- [ ] Analyze running time

### For Case Analysis (2.2-3)
- [ ] Identify best/worst/average scenarios
- [ ] Count operations for each
- [ ] Express in Θ-notation
- [ ] Justify reasoning

### For Modifications (2.2-4)
- [ ] Understand original algorithm
- [ ] Design modification
- [ ] Analyze impact
- [ ] Verify improvement

### Time Management
- Θ-notation: 2-3 min
- Selection sort: 15-20 min
- Linear search: 10-15 min
- Modification: 5-10 min

---

**You're ready to master algorithm analysis! 🎉**

---

**End of Guide**
