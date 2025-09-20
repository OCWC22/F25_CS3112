# Chapter 4: Divide-and-Conquer

## Overview

This chapter covers the divide-and-conquer paradigm and its applications in algorithm design, including matrix multiplication algorithms and recurrence analysis techniques.

## Content

### Divide-and-Conquer Paradigm

Recall the divide-and-conquer paradigm, which we used for merge sort:

1. **Divide** the problem into one or more subproblems that are smaller instances of the same problem.
2. **Conquer** the subproblems by solving them recursively.
3. **Base case**: If the subproblems are small enough, just solve them by brute force.
4. **Combine** the subproblem solutions to form a solution to the original problem.

### Recurrence Analysis

Use a recurrence to characterize the running time of a divide-and-conquer algorithm. Solving the recurrence gives us the asymptotic running time.

A recurrence is a function defined in terms of:
- One or more base cases, and
- Itself, with smaller arguments.

#### Algorithmic Recurrences

A recurrence T(n) is algorithmic if for every sufficiently large threshold constant n₀ > 0:
- For all n < n₀, T(n) = Θ(1) [Constant time for small problems]
- For all n ≥ n₀, every path of recursion terminates in a defined base case within a finite number of recursive invocations [The algorithm terminates]

#### Conventions

- Recurrences are often stated without base cases (assumed algorithmic)
- Ceilings and floors don't change asymptotic behavior
- Some recurrences use inequalities rather than equations

#### Examples of Recurrences

1. **Simple matrix multiplication**: T(n) = 8T(n/2) + Θ(1) → T(n) = Θ(n³)
2. **Strassen's algorithm**: T(n) = 7T(n/2) + Θ(1) → T(n) = Θ(n^lg7) = O(n^2.81)
3. **Split into n/3 and 2n/3**: T(n) = T(n/3) + T(2n/3) + Θ(n) → T(n) = Θ(n log n)
4. **Linear search**: T(n) = T(n-1) + Θ(1) → T(n) = Θ(n)

### Methods for Solving Recurrences

1. **Substitution method**: Guess the solution, then use induction to prove it's correct
2. **Recursion-tree method**: Draw recursion tree, sum costs at each level (good for guessing)
3. **Master method**: Cookbook method for T(n) = aT(n/b) + f(n)
4. **Akra-Bazzi method**: General method requiring calculus (not covered)

### Matrix Multiplication Algorithms

#### Standard Matrix Multiplication

Input: Three n×n matrices A, B, and C
Result: C += A×B

```python
Matrix-Multiply(A, B, C, n):
    for i = 1 to n:
        for j = 1 to n:
            for k = 1 to n:
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
```

Time: Θ(n³)

#### Simple Divide-and-Conquer Algorithm

Partition matrices into four n/2 × n/2 submatrices:
- A = [A₁₁ A₁₂; A₂₁ A₂₂]
- B = [B₁₁ B₁₂; B₂₁ B₂₂]  
- C = [C₁₁ C₁₂; C₂₁ C₂₂]

Then:
- C₁₁ = A₁₁B₁₁ + A₁₂B₂₁
- C₁₂ = A₁₁B₁₂ + A₁₂B₂₂
- C₂₁ = A₂₁B₁₁ + A₂₂B₂₁
- C₂₂ = A₂₁B₁₂ + A₂₂B₂₂

Recurrence: T(n) = 8T(n/2) + Θ(1) = Θ(n³)

#### Strassen's Algorithm

Key insight: Use only 7 recursive multiplications instead of 8

**Steps:**
1. Create 10 matrices S₁...S₁₀ (sums/differences of submatrices)
2. Create 7 matrices P₁...P₇ using recursive multiplication
3. Combine results to get C

**The 10 S matrices:**
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

**The 7 P matrices:**
- P₁ = A₁₁S₁ = A₁₁(B₁₂ - B₂₂)
- P₂ = S₂B₂₂ = (A₁₁ + A₁₂)B₂₂
- P₃ = S₃B₁₁ = (A₂₁ + A₂₂)B₁₁
- P₄ = A₂₂S₄ = A₂₂(B₂₁ - B₁₁)
- P₅ = S₅S₆ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
- P₆ = S₇S₈ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
- P₇ = S₉S₁₀ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)

**Final combinations:**
- C₁₁ = P₅ + P₄ - P₂ + P₆
- C₁₂ = P₁ + P₂
- C₂₁ = P₃ + P₄
- C₂₂ = P₅ + P₁ - P₃ - P₇

Recurrence: T(n) = 7T(n/2) + Θ(n²) = Θ(n^lg7) = O(n^2.81)

### Substitution Method

1. Guess the solution
2. Use induction to find constants and prove correctness
3. Usually establishes upper (O) or lower (Ω) bounds

#### Example: T(n) = 2T(⌊n/2⌋) + Θ(n)

**Guess:** T(n) = O(n log n)

**Inductive hypothesis:** T(n) ≤ cn log n for all n ≥ n₀

**Substitution:**
```
T(n) ≤ 2T(⌊n/2⌋) + Θ(n)
    ≤ 2c⌊n/2⌋log⌊n/2⌋ + Θ(n)
    ≤ 2c(n/2)log(n/2) + Θ(n)
    = cn log(n/2) + Θ(n)
    = cn log n - cn + Θ(n)
    ≤ cn log n
```

#### Making Good Guesses

- Experience helps
- Draw recursion trees
- Use similar recurrences as guidance
- When stuck, subtract lower-order terms

### Recursion Tree Method

Use to generate guesses, then verify with substitution.

#### Example: T(n) = 3T(n/4) + cn²

Draw tree:
- Level 0: cn²
- Level 1: 3 × c(n/4)² = 3cn²/16
- Level 2: 9 × c(n/16)² = 9cn²/256
- ...
- Height: log₄n
- Leaves: 3^log₄n = n^log₄3

Sum geometric series: T(n) = O(n²)

### Master Method

For recurrences of form T(n) = aT(n/b) + f(n) where a ≥ 1, b > 1

Compare f(n) with n^log_b a:

**Case 1:** f(n) = O(n^log_b a-ε) for some ε > 0
- Solution: T(n) = Θ(n^log_b a)
- Cost dominated by leaves

**Case 2:** f(n) = Θ(n^log_b a log^k n) for some k ≥ 0
- Solution: T(n) = Θ(n^log_b a log^{k+1} n)
- Cost distributed across levels

**Case 3:** f(n) = Ω(n^log_b a+ε) for some ε > 0 and regularity condition
- Solution: T(n) = Θ(f(n))
- Cost dominated by root

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1 and sufficiently large n

#### Master Method Examples

1. T(n) = 5T(n/2) + Θ(n²)
   - n^log₂5 vs n² → Case 1 → T(n) = Θ(n^lg5)

2. T(n) = 27T(n/3) + Θ(n³ log n)
   - n³ vs n³ log n → Case 2 (k=1) → T(n) = Θ(n³ log²n)

3. T(n) = 5T(n/2) + Θ(n³)
   - n^log₂5 vs n³ → Case 3 → T(n) = Θ(n³)

4. T(n) = 27T(n/3) + Θ(n³/log n)
   - Cannot use master method (gap between cases)

## Key Topics Covered

- Divide-and-conquer paradigm
- Matrix multiplication algorithms (Strassen's algorithm)
- Recurrence analysis techniques
- Master theorem for solving recurrences
- Applications of divide-and-conquer

## Summary

This chapter provides a comprehensive introduction to divide-and-conquer algorithms, covering both the theoretical foundations and practical applications of this important algorithmic paradigm in computer science.

---
*Extracted from: Chapter 4_pdf.pdf*
*Processing completed successfully*