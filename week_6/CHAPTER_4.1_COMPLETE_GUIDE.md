# Chapter 4.1 Complete Guide: Matrix Multiplication with Divide-and-Conquer

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 4.1 - Multiplying Square Matrices  
**Purpose:** Master divide-and-conquer for matrix multiplication and understand recurrence analysis

---

## 🎯 What Chapter 4.1 Is Really About

### The Big Picture

Chapter 4.1 introduces **divide-and-conquer applied to matrix multiplication**. It's your first real example of how to:
1. Take a concrete problem (multiplying matrices)
2. Apply divide-and-conquer strategy
3. Analyze the resulting algorithm with recurrences
4. Understand why some approaches work better than others

**Mental model:** This chapter is a **case study** that sets up the tools you'll learn in 4.3-4.5 (solving recurrences).

**Key question:** Can we beat the naive O(n³) algorithm for matrix multiplication?
- Spoiler: Not with the simple divide-and-conquer approach (still O(n³))
- But it sets up Strassen's algorithm (4.2) which DOES beat O(n³)!

---

## 📚 Foundation: Matrix Multiplication Basics

### What Is Matrix Multiplication?

**Definition:**
Given two n×n matrices A and B, their product C = A·B is an n×n matrix where:

```
c_ij = Σ(k=1 to n) a_ik · b_kj
```

**In plain English:**
- Element C[i,j] = (row i of A) · (column j of B)
- Multiply corresponding elements and add them up

**Example (2×2):**
```
[1  2]   [5  6]   [1·5+2·7  1·6+2·8]   [19  22]
[3  4] × [7  8] = [3·5+4·7  3·6+4·8] = [43  50]
```

**Computation:**
- C[1,1] = 1·5 + 2·7 = 5 + 14 = 19
- C[1,2] = 1·6 + 2·8 = 6 + 16 = 22
- C[2,1] = 3·5 + 4·7 = 15 + 28 = 43
- C[2,2] = 3·6 + 4·8 = 18 + 32 = 50

---

### The Naive Algorithm

**Pseudocode:**
```
MATRIX-MULTIPLY(A, B, C, n)
1  for i = 1 to n
2    for j = 1 to n
3      for k = 1 to n
4        c_ij = c_ij + a_ik · b_kj
```

**Analysis:**
- Three nested loops, each running n times
- Line 4 executes n³ times
- Each execution: constant time (one multiply, one add)
- **Total: Θ(n³) time**

**Why this matters:**
- For n = 1000: ~1 billion operations
- For n = 2000: ~8 billion operations (8× more!)
- Cubic growth is SLOW for large matrices

---

## 🔧 Divide-and-Conquer Approach

### The Strategy

**Core idea:** Break n×n matrices into four (n/2)×(n/2) submatrices

**Matrix partitioning:**
```
     [A₁₁  A₁₂]       [B₁₁  B₁₂]       [C₁₁  C₁₂]
A =  [A₂₁  A₂₂]   B = [B₂₁  B₂₂]   C = [C₂₁  C₂₂]
```

Where each submatrix is (n/2)×(n/2).

**Matrix multiplication formula:**
```
[C₁₁  C₁₂]   [A₁₁  A₁₂] [B₁₁  B₁₂]
[C₂₁  C₂₂] = [A₂₁  A₂₂] [B₂₁  B₂₂]
```

**Expanding:**
```
C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁    (equation 4.5)
C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂    (equation 4.6)
C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁    (equation 4.7)
C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂    (equation 4.8)
```

**Key observation:** Each equation requires:
- 2 matrix multiplications (of size n/2)
- 1 matrix addition (of size n/2)

**Total:** 8 multiplications, 4 additions

---

### The Algorithm

```
MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
1  if n == 1
2    c₁₁ = c₁₁ + a₁₁ · b₁₁    // base case
3    return
4  // Divide
5  partition A, B, C into n/2 × n/2 submatrices
6  // Conquer
7  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
8  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₂, C₁₂, n/2)
9  MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₁, C₂₁, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₂, C₂₂, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₁, C₁₁, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₂, C₁₂, n/2)
13 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₁, C₂₁, n/2)
14 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```

**Line-by-line:**

**Lines 1-3:** Base case
- When n = 1, matrices are just single elements
- Do one scalar multiplication and addition
- Return immediately

**Line 5:** Divide step
- Partition each matrix into 4 submatrices
- Cost depends on implementation (see below)

**Lines 7-14:** Conquer step
- 8 recursive calls, each on (n/2)×(n/2) matrices
- Lines 7-10: Compute first terms of equations 4.5-4.8
- Lines 11-14: Compute and add second terms

**Note:** No explicit combine step!
- Results are added directly to C in place
- The "+" in equations 4.5-4.8 happens automatically

---

## 🔑 Two Implementation Approaches

### Approach 1: Index Calculation (Fast)

**Idea:** Don't create new arrays, just track indices

**How it works:**
```
Original matrix A (4×4):
[a₀₀  a₀₁  a₀₂  a₀₃]
[a₁₀  a₁₁  a₁₂  a₁₃]
[a₂₀  a₂₁  a₂₂  a₂₃]
[a₃₀  a₃₁  a₃₂  a₃₃]

A₁₁ = A[0:2, 0:2]  (rows 0-1, cols 0-1)
A₁₂ = A[0:2, 2:4]  (rows 0-1, cols 2-3)
A₂₁ = A[2:4, 0:2]  (rows 2-3, cols 0-1)
A₂₂ = A[2:4, 2:4]  (rows 2-3, cols 2-3)
```

**Implementation:**
- Pass row/column offsets to recursive calls
- Access elements using: A[row_offset + i][col_offset + j]
- No copying, no extra space

**Cost:**
- Partitioning: Θ(1) - just arithmetic on indices
- Space: O(1) extra space

---

### Approach 2: Copying (Simple but Slow)

**Idea:** Create new arrays for each submatrix

**How it works:**
```
1. Create new arrays: A₁₁_copy, A₁₂_copy, etc.
2. Copy elements from A into these arrays
3. Recursively multiply the copies
4. Copy results back to C
```

**Example:**
```
// Copy A₁₁
for i = 0 to n/2-1
  for j = 0 to n/2-1
    A₁₁_copy[i][j] = A[i][j]

// Recursive call
MATRIX-MULTIPLY-RECURSIVE(A₁₁_copy, B₁₁_copy, C₁₁_copy, n/2)

// Copy back
for i = 0 to n/2-1
  for j = 0 to n/2-1
    C[i][j] = C₁₁_copy[i][j]
```

**Cost:**
- Copying IN: Θ(n²) - copy all elements of A and B
- Copying OUT: Θ(n²) - copy results back to C
- Space: O(n²) extra space per level

---

## 📊 Recurrence Analysis

### With Index Calculation

**Recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Breaking it down:**
- **8T(n/2):** 8 recursive calls on (n/2)×(n/2) matrices
- **Θ(n²):** Time for partitioning (Θ(1)) + combining (Θ(n²))
  - Partitioning: constant time with index calculation
  - Combining: adding four (n/2)×(n/2) matrices = Θ(n²)

**Note:** The book sometimes writes Θ(1) for the non-recursive work, but this is imprecise. The additions contribute Θ(n²).

---

### With Copying

**Recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Breaking it down:**
- **8T(n/2):** 8 recursive calls (same as before)
- **Θ(n²):** Copying + combining
  - Copy IN: Θ(n²) - copy elements from A, B to submatrices
  - Copy OUT: Θ(n²) - copy results back to C
  - Combine: Θ(n²) - add submatrices
  - Total: Θ(n²) + Θ(n²) + Θ(n²) = Θ(n²)

**Key insight:** Same recurrence! Copying adds overhead but doesn't change asymptotic complexity.

---

## 🧮 Solving the Recurrence

### Method 1: Recursion Tree

**Visual representation:**
```
Level 0:  1 problem of size n
          Cost: n²
          Subproblems: 8 of size n/2

Level 1:  8 problems of size n/2
          Cost per problem: (n/2)² = n²/4
          Total cost: 8 × n²/4 = 2n²
          Subproblems: 64 of size n/4

Level 2:  64 problems of size n/4
          Cost per problem: (n/4)² = n²/16
          Total cost: 64 × n²/16 = 4n²
          Subproblems: 512 of size n/8

...

Level i:  8ⁱ problems of size n/2ⁱ
          Cost per problem: (n/2ⁱ)² = n²/4ⁱ
          Total cost: 8ⁱ × n²/4ⁱ = (8/4)ⁱ × n² = 2ⁱ × n²
```

**Pattern at each level:**
```
Level i cost = 2ⁱ × n²
```

**Number of levels:**
- Keep dividing by 2 until size = 1
- n/2ⁱ = 1 ⟹ 2ⁱ = n ⟹ i = lg n
- Total levels: lg n + 1 (including level 0)

**Total cost:**
```
T(n) = Σ(i=0 to lg n) 2ⁱ × n²
     = n² × Σ(i=0 to lg n) 2ⁱ
     = n² × (2^(lg n + 1) - 1)/(2 - 1)    [geometric series]
     = n² × (2 × 2^(lg n) - 1)
     = n² × (2n - 1)                       [since 2^(lg n) = n]
     = 2n³ - n²
     = Θ(n³)
```

**Geometric series formula:**
```
Σ(i=0 to k) rⁱ = (r^(k+1) - 1)/(r - 1)
```

---

### Method 2: Master Theorem (Preview)

**Master Theorem form:**
```
T(n) = aT(n/b) + f(n)
```

**Our recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Parameters:**
- a = 8 (number of subproblems)
- b = 2 (factor by which size decreases)
- f(n) = Θ(n²) (non-recursive work)

**Calculate n^(log_b a):**
```
log_b a = log₂ 8 = log₂ 2³ = 3
n^(log_b a) = n³
```

**Compare f(n) with n^(log_b a):**
```
f(n) = n²
n^(log_b a) = n³
```

So f(n) is polynomially smaller than n³.

**Master Theorem Case 1:**
If f(n) = O(n^(log_b a - ε)) for some ε > 0, then T(n) = Θ(n^(log_b a))

Check: Is n² = O(n^(3-ε))?
- Yes! Take ε = 1: n² = O(n²) which is O(n^(3-1)) = O(n²) ✓

**Therefore:**
```
T(n) = Θ(n^(log₂ 8)) = Θ(n³)
```

---

## 💡 Why Doesn't Divide-and-Conquer Help?

### The Problem: Too Many Subproblems

**Key insight:** We make **8 recursive calls**

**Growth of work:**
```
Level 0: 1 problem,  cost n²
Level 1: 8 problems, cost 2n²
Level 2: 64 problems, cost 4n²
Level 3: 512 problems, cost 8n²
...
```

**The pattern:**
- Number of problems: 8ⁱ (exponential growth!)
- Cost per level: 2ⁱ × n² (also growing!)
- Total: Dominated by the leaves (n³ leaf nodes)

**Comparison with Merge Sort:**
```
Merge Sort: T(n) = 2T(n/2) + Θ(n)
- 2 subproblems (not 8!)
- Cost per level: constant (n)
- Total: Θ(n lg n)
```

**Why merge sort is faster:**
- Fewer subproblems (2 vs 8)
- Cost per level doesn't grow (stays n)
- Result: logarithmic depth dominates, not exponential leaves

---

### What Would Help?

**Reduce the number of recursive calls!**

This is exactly what **Strassen's algorithm** does (Section 4.2):
- Uses only **7 recursive calls** instead of 8
- Recurrence: T(n) = 7T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
- **Faster than n³!**

**The trick:** Clever algebraic manipulation to eliminate one multiplication

---

## 🎯 Problem-Solving Framework

### Problem Type 1: Modify for Non-Powers of 2 (Exercise 4.1-1)

**What it's asking:**
Handle matrices where n is not a power of 2

**Framework:**
1. Identify what breaks (submatrices not equal size)
2. Use ceiling/floor to handle odd sizes
3. Adjust recurrence for unequal subproblems
4. Show asymptotic complexity unchanged

**Key insight:** Unequal splits don't change Θ(n³) result

---

### Problem Type 2: Non-Square Matrices (Exercise 4.1-2)

**What it's asking:**
Multiply kn × n by n × kn matrices (or vice versa)

**Framework:**
1. Determine how to partition non-square matrices
2. Count recursive calls needed
3. Write recurrence
4. Solve and compare

**Key insight:** Asymmetry affects number of subproblems

---

### Problem Type 3: Analyze Implementation Changes (Exercise 4.1-3)

**What it's asking:**
How does copying affect the recurrence?

**Framework:**
1. Calculate cost of copying (Θ(n²))
2. Add to non-recursive work
3. Show recurrence unchanged asymptotically
4. Note practical differences (space, constants)

**Key insight:** Θ(n²) copying doesn't change Θ(n³) result

---

### Problem Type 4: Design Related Algorithm (Exercise 4.1-4)

**What it's asking:**
Apply divide-and-conquer to matrix addition

**Framework:**
1. Identify base case (1×1 matrices)
2. Partition into submatrices
3. Recursively add corresponding submatrices
4. Write recurrence
5. Solve recurrence
6. Compare with iterative approach

**Key insight:** Sometimes recursion adds unnecessary overhead

---

## 📋 Key Concepts Summary

### Matrix Multiplication
```
C = A × B
c_ij = Σ(k=1 to n) a_ik · b_kj
Naive: Θ(n³)
```

### Divide-and-Conquer
```
Divide: Partition into 4 submatrices
Conquer: 8 recursive multiplications
Combine: Add results (in place)
```

### Recurrence
```
T(n) = 8T(n/2) + Θ(n²)
Solution: T(n) = Θ(n³)
```

### Implementation
```
Index calculation: Θ(1) partition, O(1) space
Copying: Θ(n²) partition, O(n²) space
Both give same asymptotic time
```

### Why No Improvement?
```
8 subproblems → exponential growth
Leaves dominate → Θ(n³)
Need fewer subproblems (Strassen: 7)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Counting Subproblems Wrong
```
✗ "4 submatrices, so 4 recursive calls"
✓ Each of 4 output submatrices needs 2 multiplications
✓ Total: 4 × 2 = 8 recursive calls
```

### Mistake 2: Forgetting Addition Cost
```
✗ T(n) = 8T(n/2) + Θ(1)
✓ T(n) = 8T(n/2) + Θ(n²)
✓ Adding (n/2)×(n/2) matrices takes Θ(n²) time
```

### Mistake 3: Thinking Copying Changes Asymptotic Time
```
✗ "Copying makes it slower, so different Θ"
✓ Copying adds Θ(n²), but result still Θ(n³)
✓ Same asymptotic time, different constants
```

### Mistake 4: Confusing with Merge Sort
```
✗ "Divide-and-conquer always gives Θ(n lg n)"
✓ Depends on number of subproblems!
✓ 2 subproblems → Θ(n lg n)
✓ 8 subproblems → Θ(n³)
```

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Identify if it's about recurrence or implementation
- [ ] Recall the 8 subproblems (not 4!)
- [ ] Remember Θ(n²) for non-recursive work

### While Solving
- [ ] Draw recursion tree if helpful
- [ ] Count subproblems carefully
- [ ] Check if Master Theorem applies
- [ ] Verify with small example

### Common Question Types
1. **Modify algorithm:** Change partitioning or base case
2. **Analyze recurrence:** Solve T(n) = 8T(n/2) + f(n)
3. **Compare approaches:** Index vs copying, recursive vs iterative
4. **Design variant:** Apply to related problem (addition, etc.)

---

**You're ready to master Chapter 4.1! 🎉**

---

**End of Guide**
