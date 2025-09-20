# Chapter 4: Divide-and-Conquer (Introduction to Algorithms, 4th Edition)

## Overview

The divide-and-conquer method is a powerful strategy for designing asymptotically efficient algorithms. This chapter explores applications of the divide-and-conquer method and provides mathematical tools for solving the recurrences that arise when analyzing divide-and-conquer algorithms.

## Divide-and-Conquer Paradigm

Recall that for divide-and-conquer, you solve a given problem (instance) recursively. If the problem is small enough—the base case—you just solve it directly without recursing. Otherwise—the recursive case—you perform three characteristic steps:

1. **Divide** the problem into one or more subproblems that are smaller instances of the same problem.
2. **Conquer** the subproblems by solving them recursively.
3. **Combine** the subproblem solutions to form a solution to the original problem.

A divide-and-conquer algorithm breaks down a large problem into smaller subproblems, which themselves may be broken down into even smaller subproblems, and so forth. The recursion bottoms out when it reaches a base case and the subproblem is small enough to solve directly without further recursing.

## Recurrences

### What are Recurrences?

A recurrence is an equation that describes a function in terms of its value on other, typically smaller, arguments. Recurrences go hand in hand with the divide-and-conquer method because they give us a natural way to characterize the running times of recursive algorithms mathematically.

### Algorithmic Recurrences

A recurrence T(n) is **algorithmic** if, for every sufficiently large threshold constant n₀ > 0, the following two properties hold:

1. For all n < n₀, we have T(n) = Θ(1).
2. For all n ≥ n₀, every path of recursion terminates in a defined base case within a finite number of recursive invocations.

### Conventions for Recurrences

- Whenever a recurrence is stated without an explicit base case, we assume that the recurrence is algorithmic.
- Asymptotic solutions of algorithmic divide-and-conquer recurrences don't tend to change when we drop any floors or ceilings in a recurrence defined on the integers to convert it to a recurrence defined on the reals.
- You may sometimes see recurrences that are not equations, but rather inequalities, such as T(n) ≤ 2T(n/2) + Θ(n). Because such a recurrence states only an upper bound on T(n), we express its solution using O-notation rather than Θ-notation.

### Examples of Recurrences

1. **Simple divide-and-conquer matrix multiplication**: T(n) = 8T(n/2) + Θ(1) → T(n) = Θ(n³)
2. **Strassen's algorithm**: T(n) = 7T(n/2) + Θ(n²) → T(n) = Θ(n^lg 7) = O(n^2.81)
3. **Split into n/3 and 2n/3**: T(n) = T(n/3) + T(2n/3) + Θ(n) → T(n) = Θ(n log n)
4. **Order statistic algorithm**: T(n) = T(n/5) + T(7n/10) + Θ(n) → T(n) = Θ(n)
5. **Linear search**: T(n) = T(n-1) + Θ(1) → T(n) = Θ(n)

## Methods for Solving Recurrences

1. **Substitution method (Section 4.3)**: Guess the form of a bound and then use mathematical induction to prove your guess correct and solve for constants.
2. **Recursion-tree method (Section 4.4)**: Models the recurrence as a tree whose nodes represent the costs incurred at various levels of the recursion.
3. **Master method (Sections 4.5 and 4.6)**: The easiest method when it applies. It provides bounds for recurrences of the form T(n) = aT(n/b) + f(n), where a > 0 and b > 1 are constants and f(n) is a given "driving" function.
4. **Akra-Bazzi method (Section 4.7)**: A general method for solving divide-and-conquer recurrences that involves calculus and can attack more complicated recurrences than those addressed by the master method.

## 4.1 Multiplying Square Matrices

### Standard Matrix Multiplication

Let A = (a_ik) and B = (b_jk) be square n × n matrices. The matrix product C = A · B is also an n × n matrix, where for i, j = 1, 2, …, n, the (i, j) entry of C is given by:

```
c_ij = Σ_{k=1 to n} a_ik · b_kj
```

The MATRIX-MULTIPLY procedure implements this strategy:

```
MATRIX-MULTIPLY(A, B, C, n)
1  for i = 1 to n              // compute entries in each of n rows
2      for j = 1 to n          // compute n entries in row i
3          for k = 1 to n
4              c_ij = c_ij + a_ik · b_kj  // add in another term
```

**Time complexity**: Θ(n³) due to the triply nested loops.

### Simple Divide-and-Conquer Algorithm

For n > 1, partition each n × n matrix into four n/2 × n/2 submatrices:

```
A = [A₁₁ A₁₂; A₂₁ A₂₂]
B = [B₁₁ B₁₂; B₂₁ B₂₂]
C = [C₁₁ C₁₂; C₂₁ C₂₂]
```

The matrix product can be written as:

```
[C₁₁ C₁₂; C₂₁ C₂₂] = [A₁₁ A₁₂; A₂₁ A₂₂] · [B₁₁ B₁₂; B₂₁ B₂₂]
```

This gives us four equations:
- C₁₁ = A₁₁B₁₁ + A₁₂B₂₁
- C₁₂ = A₁₁B₁₂ + A₁₂B₂₂
- C₂₁ = A₂₁B₁₁ + A₂₂B₂₁
- C₂₂ = A₂₁B₁₂ + A₂₂B₂₂

The MATRIX-MULTIPLY-RECURSIVE procedure implements this strategy:

```
MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
1  if n == 1
2      c₁₁ = c₁₁ + a₁₁ · b₁₁    // Base case
3      return
4  // Divide: partition matrices using index calculations (Θ(1) time)
5  partition A, B, and C into n/2 × n/2 submatrices
6  // Conquer: 8 recursive calls
7  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
8  MATRIX-MULTIPLY-RECURSIVE(A₁₁, B₁₂, C₁₂, n/2)
9  MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₁, C₂₁, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A₂₁, B₁₂, C₂₂, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₁, C₁₁, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A₁₂, B₂₂, C₁₂, n/2)
13 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₁, C₂₁, n/2)
14 MATRIX-MULTIPLY-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```

**Analysis**:
- Base case (n = 1): Θ(1) time
- Recursive case (n > 1): Θ(1) + 8T(n/2) time
- Recurrence: T(n) = 8T(n/2) + Θ(1)
- Solution: T(n) = Θ(n³) [same asymptotic running time as the straightforward method]

### Matrix Partitioning Approaches

Two approaches for implementing matrix partitioning:

1. **Copy approach**: Allocate temporary storage and copy elements - takes Θ(n²) time
2. **Index calculation approach**: Specify submatrices by location information within the matrix - takes Θ(1) time

The index calculation approach is preferred as it's more efficient and practical.

## 4.2 Strassen's Algorithm for Matrix Multiplication

### Overview

V. Strassen published a remarkable recursive algorithm in 1969 that runs in Θ(n^lg 7) time. Since lg 7 ≈ 2.8073549, Strassen's algorithm runs in O(n^2.81) time, which is asymptotically better than the Θ(n³) time of the straightforward method.

### Key Insight

Make the recursion tree less bushy by performing only 7 recursive multiplications of n/2 × n/2 matrices instead of 8, at the cost of several additions/subtractions of n/2 × n/2 matrices.

### Algorithm Steps

1. **Base case**: When n = 1, perform scalar multiplication
2. **Divide**: Partition each matrix into four n/2 × n/2 submatrices (Θ(1) time)
3. **Create 10 matrices**: S₁, S₂, ..., S₁₀, each n/2 × n/2, as sums or differences of submatrices (Θ(n²) time)
4. **Create and zero 7 matrices**: P₁, P₂, ..., P₇, each n/2 × n/2 (Θ(n²) time)
5. **Recursive computation**: Compute P₁, P₂, ..., P₇ using the submatrices (7T(n/2) time)
6. **Combine**: Update C's submatrices by adding and subtracting combinations of P matrices (Θ(n²) time)

### The 10 S Matrices

- S₁ = B₁₂ - B₂₂
- S₂ = A₁₁ + A₁₂
- S₃ = A₂₁ + A₂₂
- S₄ = B₂₁ - B₁₁
- S₅ = A₁₁ + A₂₂
- S₆ = B₁₁ + B₂₂
- S₇ = A₁₂ - A₂₂
- S₈ = B₂₁ + B₂₂
- S₉ = A₁₁ - A₂₁
- S₁₀ = B₁₁ + B₁₂

### The 7 P Matrices

- P₁ = A₁₁S₁ = A₁₁(B₁₂ - B₂₂)
- P₂ = S₂B₂₂ = (A₁₁ + A₁₂)B₂₂
- P₃ = S₃B₁₁ = (A₂₁ + A₂₂)B₁₁
- P₄ = A₂₂S₄ = A₂₂(B₂₁ - B₁₁)
- P₅ = S₅S₆ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
- P₆ = S₇S₈ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
- P₇ = S₉S₁₀ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)

### Final Combinations

- C₁₁ = P₅ + P₄ - P₂ + P₆
- C₁₂ = P₁ + P₂
- C₂₁ = P₃ + P₄
- C₂₂ = P₅ + P₁ - P₃ - P₇

### Analysis

**Recurrence**: T(n) = 7T(n/2) + Θ(n²)

**Solution**: T(n) = Θ(n^lg 7) = O(n^2.81)

This beats the straightforward Θ(n³)-time method asymptotically.

### Historical Context

- Strassen's algorithm was the first to beat Θ(n³) time
- A method by Coppersmith and Winograd runs in O(n^2.376) time
- Current best asymptotic bound is O(n^2.37286) (not practical)

### Practical Considerations

**Issues with Strassen's algorithm:**
- Higher constant factor than the obvious Θ(n³)-time method
- Not good for sparse matrices
- Not numerically stable: larger errors accumulate
- Submatrices consume space, especially if copying

**Optimizations:**
- Numerical stability problem is not as bad as previously thought
- Index calculations can reduce space requirements

## 4.3 The Substitution Method for Solving Recurrences

### Overview

The substitution method involves two main steps:
1. **Guess** the form of the solution
2. **Use mathematical induction** to find the constants and show that the solution works

This method is powerful but requires making an initial guess, which can be challenging.

### Example 1: T(n) = 2T(⌊n/2⌋) + n

**Guess**: T(n) = O(n log n)

**Inductive hypothesis**: Assume T(k) ≤ ck log k for all k < n

**Substitution**:
```
T(n) = 2T(⌊n/2⌋) + n
     ≤ 2c⌊n/2⌋log⌊n/2⌋ + n
     ≤ 2c(n/2)log(n/2) + n
     = cn log(n/2) + n
     = cn log n - cn + n
     ≤ cn log n
```

We need -cn + n ≤ 0, which holds for c ≥ 1.

### Example 2: T(n) = T(n-1) + n

**Guess**: T(n) = O(n²)

**Inductive hypothesis**: Assume T(k) ≤ ck² for all k < n

**Substitution**:
```
T(n) = T(n-1) + n
     ≤ c(n-1)² + n
     = c(n² - 2n + 1) + n
     = cn² - 2cn + c + n
     ≤ cn²
```

We need -2cn + c + n ≤ 0, which holds for c ≥ 1.

### Example 3: T(n) = 4T(n/2) + n

**Incorrect guess**: T(n) = O(n²)

**Substitution**:
```
T(n) = 4T(n/2) + n
     ≤ 4c(n/2)² + n
     = 4c(n²/4) + n
     = cn² + n
```

But we need T(n) ≤ cn², which doesn't work because of the +n term.

**Correct guess**: T(n) = O(n²)

We can use T(n) ≤ cn² - dn:
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n
     = 4[c(n²/4) - dn/2] + n
     = cn² - 2dn + n
     = cn² - (2d - 1)n
```

For this to work, we need 2d - 1 ≥ 0, so d ≥ 1/2.

### Making Good Guesses

1. **Use recursion trees** to get intuition about the solution
2. **Look for patterns** in similar recurrences
3. **Start with loose bounds** and tighten them
4. **Subtract lower-order terms** when stuck

### Dealing with Floors and Ceilings

For recurrences with floors or ceilings, we can often ignore them in asymptotic analysis:
- The difference between n/2 and ⌊n/2⌋ is at most 1
- For asymptotic bounds, this difference becomes negligible

### Variable Substitution

Sometimes a change of variables can simplify the recurrence:
- Let m = log n to change the recurrence domain
- This can transform recurrences into more familiar forms

### Exercises

4.3-1: Show that T(n) = 2T(⌊n/2⌋) + n has solution T(n) = O(n log n)

4.3-2: The solution to the recurrence T(n) = 4T(n/2)+n turns out to be T(n) = Θ(n²). Show that a substitution proof with the assumption T(n) ≤ cn² fails. Then show how to subtract a lower-order term to make a substitution proof work.

4.3-3: The recurrence T(n) = 2T(n – 1) + 1 has the solution T(n) = O(2n). Show that a substitution proof fails with the assumption T(n) ≤ c 2n, where c > 0 is constant. Then show how to subtract a lower-order term to make a substitution proof work.

## 4.4 The Recursion-Tree Method for Solving Recurrences

### Overview

Although you can use the substitution method to prove that a solution to a recurrence is correct, you might have trouble coming up with a good guess. Drawing out a recursion tree can help. In a recursion tree, each node represents the cost of a single subproblem somewhere in the set of recursive function invocations. You typically sum the costs within each level of the tree to obtain the per-level costs, and then you sum all the per-level costs to determine the total cost of all levels of the recursion.

A recursion tree is best used to generate intuition for a good guess, which you can then verify by the substitution method. If you are meticulous when drawing out a recursion tree and summing the costs, however, you can use a recursion tree as a direct proof of a solution to a recurrence.

### Example 1: T(n) = 3T(n/4) + cn²

**Recursion tree construction:**
- Level 0 (root): cost = cn²
- Level 1: 3 nodes, each cost = c(n/4)² = cn²/16, total = 3cn²/16
- Level 2: 9 nodes, each cost = c(n/16)² = cn²/256, total = 9cn²/256
- ...
- Level i: 3i nodes, each cost = c(n/4i)², total = 3icn²/16i = (3/16)icn²

**Tree height**: log₄n (since n/4i = 1 when i = log₄n)

**Number of leaves**: 3^log₄n = n^log₄3

**Total cost**: Sum over all levels = cn²[1 + 3/16 + (3/16)² + ... + (3/16)^(log₄n - 1)] + Θ(n^log₄3)

This forms a decreasing geometric series with ratio 3/16 < 1, so the sum is bounded by cn² × 16/13 = O(n²).

**Verification with substitution method**:
Assume T(n) ≤ dn² for some constant d > 0:
```
T(n) ≤ 3T(n/4) + cn²
     ≤ 3d(n/4)² + cn²
     = 3dn²/16 + cn²
     = (3d/16 + c)n²
     ≤ dn²
```
This holds if we choose d ≥ (16/13)c.

### Example 2: T(n) = T(n/3) + T(2n/3) + cn

**Unbalanced recursion tree:**
- Going left: subproblem size n/3
- Going right: subproblem size 2n/3
- Tree height: Θ(log n) (along the rightmost path)
- Each level costs at most cn
- Total internal node cost: O(n log n)

**Leaf analysis**:
Let L(n) be the number of leaves. Then L(n) = L(n/3) + L(2n/3) with L(n) = 1 for n < n₀.
Using substitution: L(n) ≤ dn, so L(n) = O(n).
Total leaf cost: Θ(n).

**Total cost**: O(n log n) + Θ(n) = O(n log n).

### Exercises

4.4-1: For each recurrence, sketch recursion tree and guess asymptotic bound, then verify with substitution:
a. T(n) = T(n/2) + n³
b. T(n) = 4T(n/3) + n
c. T(n) = 4T(n/2) + n
d. T(n) = 3T(n – 1) + 1

4.4-2: Use substitution to prove L(n) = Ω(n) for recurrence (4.15), concluding L(n) = Θ(n).

4.4-3: Use substitution to prove T(n) = Ω(n lg n) for recurrence (4.14), concluding T(n) = Θ(n lg n).

4.4-4: Use recursion tree for T(n) = T(αn) + T((1–α)n) + Θ(n) where 0 < α < 1.

## 4.5 The Master Method for Solving Recurrences

### Overview

The master method provides a "cookbook" method for solving algorithmic recurrences of the form:
```
T(n) = aT(n/b) + f(n)
```
where a > 0 and b > 1 are constants. We call f(n) a **driving function**, and we call a recurrence of this general form a **master recurrence**.

A master recurrence describes the running time of a divide-and-conquer algorithm that divides a problem of size n into a subproblems, each of size n/b < n. The algorithm solves the a subproblems recursively, each in T(n/b) time. The driving function f(n) encompasses the cost of dividing the problem before the recursion, as well as the cost of combining the results of the recursive solutions to subproblems.

### The Master Theorem

**Theorem 4.1 (Master theorem)**
Let a > 0 and b > 1 be constants, and let f(n) be a driving function that is defined and nonnegative on all sufficiently large reals. Define the recurrence T(n) on n ∈ ℕ by:
```
T(n) = aT(n/b) + f(n)
```
where aT(n/b) actually means a′T(⌊n/b⌋) + a″T(⌈n/b⌉) for some constants a′ ≥ 0 and a″ ≥ 0 satisfying a = a′ + a″. Then the asymptotic behavior of T(n) can be characterized as follows:

#### Case 1: f(n) = O(n^(log_b a - ε)) for some ε > 0
If there exists a constant ε > 0 such that f(n) = O(n^(log_b a - ε)), then T(n) = Θ(n^(log_b a)).

**Intuition**: The watershed function n^(log_b a) grows asymptotically faster than the driving function f(n) by at least a polynomial factor. In the recursion tree, the cost per level grows geometrically from root to leaves, and the total cost of leaves dominates.

#### Case 2: f(n) = Θ(n^(log_b a) log^k n) for some k ≥ 0
If there exists a constant k ≥ 0 such that f(n) = Θ(n^(log_b a) log^k n), then T(n) = Θ(n^(log_b a) log^(k+1) n).

**Intuition**: The watershed and driving functions grow at nearly the same asymptotic rate, with the driving function growing faster by a factor of Θ(log^k n). Each level of the recursion tree costs approximately the same, and there are Θ(log n) levels.

#### Case 3: f(n) = Ω(n^(log_b a + ε)) for some ε > 0, with regularity condition
If there exists a constant ε > 0 such that f(n) = Ω(n^(log_b a + ε)), and if f(n) additionally satisfies the **regularity condition** af(n/b) ≤ cf(n) for some constant c < 1 and all sufficiently large n, then T(n) = Θ(f(n)).

**Intuition**: The driving function grows asymptotically faster than the watershed function by at least a polynomial factor. The regularity condition ensures that f(n) doesn't grow too slowly in local areas. In the recursion tree, the cost per level drops geometrically from root to leaves, and the root cost dominates.

### Using the Master Method

#### Example 1: T(n) = 9T(n/3) + n
- a = 9, b = 3 → log_b a = 2
- f(n) = n = O(n^(2-ε)) for ε = 1
- **Case 1 applies**: T(n) = Θ(n²)

#### Example 2: T(n) = T(2n/3) + 1
- a = 1, b = 3/2 → log_b a = 0
- f(n) = 1 = Θ(n⁰ log⁰ n) (k = 0)
- **Case 2 applies**: T(n) = Θ(log n)

#### Example 3: T(n) = 3T(n/4) + n lg n
- a = 3, b = 4 → log_b a ≈ 0.792
- f(n) = n lg n = Ω(n^(0.792+ε)) for ε ≈ 0.2
- Regularity: 3(n/4)lg(n/4) ≤ (3/4)n lg n for large n
- **Case 3 applies**: T(n) = Θ(n lg n)

#### Example 4: T(n) = 2T(n/2) + n lg n
- a = 2, b = 2 → log_b a = 1
- f(n) = n lg n = Θ(n¹ log¹ n) (k = 1)
- **Case 2 applies**: T(n) = Θ(n lg² n)

#### Classic Algorithm Examples:
1. **Merge sort**: T(n) = 2T(n/2) + Θ(n)
   - a = 2, b = 2 → log_b a = 1
   - f(n) = Θ(n) = Θ(n¹ log⁰ n) (k = 0)
   - **Case 2**: T(n) = Θ(n log n)

2. **Simple matrix multiplication**: T(n) = 8T(n/2) + Θ(1)
   - a = 8, b = 2 → log_b a = 3
   - f(n) = Θ(1) = O(n^(3-ε)) for ε < 3
   - **Case 1**: T(n) = Θ(n³)

3. **Strassen's algorithm**: T(n) = 7T(n/2) + Θ(n²)
   - a = 7, b = 2 → log_b a = lg 7 ≈ 2.807
   - f(n) = Θ(n²) = O(n^(lg 7-ε)) for ε ≈ 0.8
   - **Case 1**: T(n) = Θ(n^lg 7)

### When the Master Method Doesn't Apply

#### Gap Between Cases:
There are situations where the master theorem doesn't apply:

1. **Gap between Case 1 and 2**: When f(n) = O(n^(log_b a)) but not O(n^(log_b a - ε)) for any ε > 0
2. **Gap between Case 2 and 3**: When f(n) = Ω(n^(log_b a)) but not Ω(n^(log_b a + ε)) for any ε > 0, and f(n) grows more than polylogarithmically faster

#### Example: T(n) = 2T(n/2) + n/lg n
- a = 2, b = 2 → log_b a = 1
- f(n) = n/lg n = o(n) but not O(n^(1-ε)) for any ε > 0
- **Neither Case 1 nor Case 2 applies**
- Solution requires substitution or Akra-Bazzi method: T(n) = Θ(n lg lg n)

#### Regularity Condition Failure:
Some functions satisfy the growth condition but not the regularity condition in Case 3. For example, f(n) = 2^⌈lg n⌉ satisfies all Case 3 conditions except regularity.

### Exercises

4.5-1: Use master method for tight asymptotic bounds:
a. T(n) = 2T(n/4) + 1
b. T(n) = 2T(n/4) + √n
c. T(n) = 2T(n/4) + n
d. T(n) = 2T(n/4) + n²

4.5-2: Professor Caesar's matrix multiplication algorithm dividing into n/4 × n/4 submatrices with Θ(n²) divide/combine time. What's the largest a for asymptotically faster than Strassen's?

4.5-3: Use master method for binary search recurrence T(n) = T(n/2) + Θ(1).

4.5-4: Show f(n) = lg n doesn't satisfy regularity condition with a = 1, b = 2.

4.5-5: Show f(n) = 2^⌈lg n⌉ satisfies Case 3 conditions except regularity.

## Key Topics Covered

- Divide-and-conquer paradigm and its three steps
- Recurrence analysis and algorithmic recurrences
- Matrix multiplication algorithms
  - Standard multiplication: Θ(n³)
  - Simple divide-and-conquer: Θ(n³)
  - Strassen's algorithm: O(n^2.81)
- Methods for solving recurrences
  - Substitution method with induction proofs
  - Recursion-tree method with geometric series analysis
  - Master method with three cases and watershed functions
- Matrix partitioning techniques
- Practical considerations for algorithm implementation

## Summary

This chapter provides a comprehensive introduction to divide-and-conquer algorithms through the lens of matrix multiplication. It demonstrates how the divide-and-conquer strategy can lead to asymptotically faster algorithms, as shown by Strassen's breakthrough algorithm that broke the Θ(n³) barrier for matrix multiplication. The chapter also establishes the mathematical foundation for analyzing recursive algorithms through recurrences and provides multiple methods for solving them:

1. **Substitution method**: For proving bounds through mathematical induction
2. **Recursion-tree method**: For generating intuition and visualizing cost distribution
3. **Master method**: For quick solutions to recurrences of the form T(n) = aT(n/b) + f(n)

These tools are essential for analyzing and designing efficient recursive algorithms, forming the foundation for understanding algorithmic complexity and optimization strategies.

---
*Extracted from: Introduction to Algorithms, 4th Edition*
*Sections covered: 4.1 (pages 119-131), 4.2 (pages 131-138), 4.3 (pages 138-144), 4.4 (pages 144-153), 4.5 (pages 153-160)*