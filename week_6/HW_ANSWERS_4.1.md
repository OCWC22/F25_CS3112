# Homework Solutions: Section 4.1 - Divide-and-Conquer Matrix Multiplication

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 4.1 (Divide-and-Conquer - Matrix Multiplication)  
**Date:** 2025-09-29

---

## Problem 4.1-3: Matrix Multiplication with Copying

### Problem Statement
Suppose that instead of partitioning matrices by index calculation in MATRIX-MULTIPLY-RECURSIVE, you copy the appropriate elements of A, B, and C into separate (n/2 × n/2) submatrices A₁₁, A₁₂, A₂₁, A₂₂; B₁₁, B₁₂, B₂₁, B₂₂; and C₁₁, C₁₂, C₂₁, C₂₂, respectively. After the recursive calls, you copy the results from C₁₁, C₁₂, C₂₁, and C₂₂ back into the appropriate places in C. How does recurrence (4.9) change, and what is its solution?

---

## Background: What You Need to Know First

### What is Matrix Multiplication?

**Basic Definition:**
When you multiply two matrices A and B to get C = A × B, each element in C is computed by taking a row from A and a column from B, multiplying corresponding elements, and adding them up.

**Example (2×2 matrices):**
```
[a  b]   [e  f]   [ae+bg  af+bh]
[c  d] × [g  h] = [ce+dg  cf+dh]
```

**For n×n matrices:**
- Each element C[i,j] requires n multiplications and n-1 additions
- Total: n³ multiplications for the whole matrix
- This is O(n³) time - very slow for large matrices!

---

### What is Divide-and-Conquer?

**Core Idea:**
Break a big problem into smaller subproblems, solve them recursively, then combine the results.

**For Matrix Multiplication:**
1. **Divide:** Split each n×n matrix into four (n/2)×(n/2) submatrices
2. **Conquer:** Recursively multiply the smaller matrices
3. **Combine:** Add the results to get the final answer

**Visual representation:**
```
[A₁₁  A₁₂]   [B₁₁  B₁₂]   [C₁₁  C₁₂]
[A₂₁  A₂₂] × [B₂₁  B₂₂] = [C₂₁  C₂₂]

Where:
C₁₁ = A₁₁B₁₁ + A₁₂B₂₁
C₁₂ = A₁₁B₁₂ + A₁₂B₂₂
C₂₁ = A₂₁B₁₁ + A₂₂B₂₁
C₂₂ = A₂₁B₁₂ + A₂₂B₂₂
```

**Why this matters:**
- Each submatrix is n/2 × n/2 (one-quarter the size)
- We need 8 recursive multiplications (see the 8 products above)
- Plus additions to combine results

---

### What is "Partitioning by Index Calculation"?

**Index Calculation (Original Method):**
- Don't create new arrays
- Just keep track of which part of the original matrix you're working on
- Use index offsets to access the right elements

**Example:**
```
Original matrix A (4×4):
[a₀₀  a₀₁  a₀₂  a₀₃]
[a₁₀  a₁₁  a₁₂  a₁₃]
[a₂₀  a₂₁  a₂₂  a₂₃]
[a₃₀  a₃₁  a₃₂  a₃₃]

A₁₁ = elements [0:2, 0:2] (top-left quarter)
A₁₂ = elements [0:2, 2:4] (top-right quarter)
A₂₁ = elements [2:4, 0:2] (bottom-left quarter)
A₂₂ = elements [2:4, 2:4] (bottom-right quarter)
```

**Cost:** No extra time or space - just use different indices

---

### What is "Copying" (This Problem's Method)?

**Copying Method:**
- Create NEW arrays for each submatrix
- Copy elements from the original matrix into these new arrays
- Work with the new arrays
- Copy results back to the original matrix

**Example:**
```
Create new array A₁₁_copy (size n/2 × n/2)
Copy A[0:n/2, 0:n/2] → A₁₁_copy
Do recursive multiplication with A₁₁_copy
Copy results back to C[0:n/2, 0:n/2]
```

**Cost:** Takes time to copy elements!

---

## Step 1: Understanding Recurrence (4.9) - The Original

**What is a recurrence?**
A recurrence is an equation that describes the running time of a recursive algorithm in terms of the running time on smaller inputs.

**Original Recurrence (4.9) for MATRIX-MULTIPLY-RECURSIVE:**
```
T(n) = 8T(n/2) + Θ(1)
```

**Breaking this down:**
- **T(n):** Time to multiply two n×n matrices
- **8T(n/2):** Time for 8 recursive calls on (n/2)×(n/2) matrices
  - Why 8? Because we need to compute 8 products (see C₁₁, C₁₂, C₂₁, C₂₂ formulas above)
- **Θ(1):** Time to partition and combine (constant time with index calculation)
  - "Θ(1)" means "constant time" - doesn't depend on n
  - With index calculation, we just adjust indices - very fast!

**Why Θ(1) for partition/combine?**
- Partitioning: Just calculate new index boundaries - O(1)
- Combining: Just add corresponding submatrices - O(n²) for additions
- Wait, O(n²) is not O(1)! The book simplifies here; technically it's Θ(n²)

**More accurate original recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

---

## Step 2: How Does Copying Change the Recurrence?

**What changes with copying?**

### Copying IN (Before Recursion):
- Need to copy elements from A, B into submatrices
- For each of A and B, we copy 4 submatrices
- Each submatrix is (n/2) × (n/2) = n²/4 elements
- Total elements to copy: 2 matrices × 4 submatrices × n²/4 = 2n²

**Time to copy IN:** Θ(n²)

### Recursive Calls:
- Still need 8 recursive calls on (n/2) × (n/2) matrices
- This doesn't change!

**Time for recursion:** 8T(n/2)

### Copying OUT (After Recursion):
- Need to copy results from C₁₁, C₁₂, C₂₁, C₂₂ back to C
- 4 submatrices × n²/4 elements each = n² elements total

**Time to copy OUT:** Θ(n²)

### Combining (Addition):
- Still need to add submatrices together
- This is Θ(n²) as before

**Time to combine:** Θ(n²)

---

## Step 3: New Recurrence with Copying

**Total non-recursive work:**
```
Copy IN:    Θ(n²)
Copy OUT:   Θ(n²)
Combine:    Θ(n²)
-----------------------
Total:      Θ(n²) + Θ(n²) + Θ(n²) = Θ(n²)
```

**Why can we add them?**
- Θ(n²) + Θ(n²) = Θ(n²) (constant factors don't matter in Θ notation)
- 3 × Θ(n²) is still Θ(n²)

**New Recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Wait, this looks the same as the original!**
- Yes! The copying adds Θ(n²) work
- But the original also had Θ(n²) work for combining
- So the asymptotic behavior is the same

---

## Step 4: Solving the Recurrence

**We need to find what T(n) equals.**

### Method 1: Recursion Tree (Visual Approach)

**What is a recursion tree?**
A tree that shows all the recursive calls and their costs.

**Level 0 (root):**
```
Cost: n²
Subproblems: 8 of size n/2
```

**Level 1:**
```
Cost per subproblem: (n/2)² = n²/4
Number of subproblems: 8
Total cost: 8 × n²/4 = 2n²
```

**Level 2:**
```
Cost per subproblem: (n/4)² = n²/16
Number of subproblems: 8² = 64
Total cost: 64 × n²/16 = 4n²
```

**Pattern:**
- Level i has 8ⁱ subproblems
- Each subproblem has size n/2ⁱ
- Cost per subproblem: (n/2ⁱ)² = n²/4ⁱ
- Total cost at level i: 8ⁱ × n²/4ⁱ = (8/4)ⁱ × n² = 2ⁱ × n²

**How many levels?**
- We keep dividing by 2 until we reach size 1
- n/2ⁱ = 1 → 2ⁱ = n → i = log₂ n
- So there are log₂ n + 1 levels (including level 0)

**Total cost:**
```
T(n) = Σ(i=0 to log n) 2ⁱ × n²
     = n² × Σ(i=0 to log n) 2ⁱ
     = n² × (2^(log n + 1) - 1) / (2 - 1)    [geometric series formula]
     = n² × (2 × 2^(log n) - 1)
     = n² × (2n - 1)                          [because 2^(log n) = n]
     = 2n³ - n²
     = Θ(n³)
```

**What is a geometric series?**
A series where each term is a constant multiple of the previous term.
Formula: Σ(i=0 to k) rⁱ = (r^(k+1) - 1)/(r - 1)
In our case: r = 2, k = log n

---

### Method 2: Master Theorem (Formula Approach)

**What is the Master Theorem?**
A formula that gives the solution to recurrences of the form:
```
T(n) = aT(n/b) + f(n)
```

**Our recurrence:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Identify parameters:**
- a = 8 (number of subproblems)
- b = 2 (factor by which problem size decreases)
- f(n) = Θ(n²) (cost of divide and combine)

**Master Theorem has 3 cases:**

**Calculate n^(log_b a):**
```
log_b a = log₂ 8 = log₂ 2³ = 3
n^(log_b a) = n³
```

**What does this mean?**
- n^(log_b a) represents the cost of all the leaves in the recursion tree
- If we just did the recursive calls with no extra work, we'd get Θ(n³)

**Compare f(n) with n^(log_b a):**
```
f(n) = n²
n^(log_b a) = n³
```

So f(n) = n² is polynomially smaller than n³.

**Which case applies?**

**Case 1:** If f(n) = O(n^(log_b a - ε)) for some ε > 0, then T(n) = Θ(n^(log_b a))

Let's check: Is n² = O(n^(3-ε)) for some ε > 0?
- Yes! Take ε = 1: n² = O(n²) which is definitely O(n³⁻¹) = O(n²)
- Actually, n² is even smaller than n³⁻ᵋ for any ε < 1

**Therefore, Case 1 applies:**
```
T(n) = Θ(n^(log₂ 8)) = Θ(n³)
```

---

## Step 5: Detailed Explanation of the Solution

**What does T(n) = Θ(n³) mean?**

**Θ notation (Theta):**
- Θ(n³) means "grows exactly like n³"
- More precisely: there exist constants c₁, c₂, n₀ such that:
  - c₁n³ ≤ T(n) ≤ c₂n³ for all n ≥ n₀
- It's a tight bound - not too high, not too low

**In plain English:**
- If you double the matrix size (n → 2n), the time increases by a factor of 8
- Because (2n)³ = 8n³
- This is the same as the naive O(n³) algorithm!

**Why is this disappointing?**
- We hoped divide-and-conquer would be faster
- But we still get O(n³) - no improvement!
- The copying overhead doesn't change the asymptotic complexity
- But it does add constant factors (makes it slower in practice)

---

## Step 6: Comparing Original vs. Copying Version

### Original (Index Calculation):
```
Recurrence: T(n) = 8T(n/2) + Θ(n²)
Solution: T(n) = Θ(n³)
Space: O(1) extra space (just indices)
```

### With Copying:
```
Recurrence: T(n) = 8T(n/2) + Θ(n²)
Solution: T(n) = Θ(n³)
Space: O(n²) extra space (for copied submatrices)
```

**Key observations:**

1. **Same asymptotic time:** Both are Θ(n³)
   - The extra Θ(n²) copying cost doesn't change the overall complexity
   - The recursive calls dominate (they contribute n³)

2. **Different space complexity:**
   - Original: O(1) extra space
   - Copying: O(n²) extra space at each level
   - Total space with copying: O(n² log n) due to recursion depth

3. **Different constant factors:**
   - Copying version is slower in practice
   - More memory allocation and deallocation
   - Cache performance may be worse

---

## Step 7: Why Does Copying Not Help?

**Intuition:**

The problem is that we're making **8 recursive calls**. This is the bottleneck.

**Think about it:**
- Each level of recursion does O(n²) work (whether copying or not)
- But we have 8 subproblems at each level
- The number of subproblems grows as 8ⁱ
- This exponential growth in subproblems dominates everything else

**The math:**
```
Level 0: 1 problem,  cost n²
Level 1: 8 problems, cost 2n²
Level 2: 64 problems, cost 4n²
...
Total: n² × (1 + 2 + 4 + ... + n) = Θ(n³)
```

**What would help?**
- Reduce the number of recursive calls (this is what Strassen's algorithm does!)
- Strassen uses only 7 recursive calls instead of 8
- This changes the recurrence to T(n) = 7T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807) - faster than n³!

---

## Final Answer for Problem 4.1-3

### How the recurrence changes:

**Original recurrence (4.9):**
```
T(n) = 8T(n/2) + Θ(1)  [or more accurately: Θ(n²)]
```

**New recurrence with copying:**
```
T(n) = 8T(n/2) + Θ(n²)
```

**Explanation of the change:**
- The Θ(n²) term now explicitly includes:
  - Θ(n²) for copying elements into submatrices
  - Θ(n²) for copying results back
  - Θ(n²) for combining (adding) submatrices
- Total non-recursive work: Θ(n²)

### Solution to the new recurrence:

**Using Master Theorem (Case 1):**
```
T(n) = Θ(n^(log₂ 8)) = Θ(n³)
```

**Detailed derivation:**
- a = 8, b = 2, f(n) = Θ(n²)
- n^(log_b a) = n^(log₂ 8) = n³
- f(n) = n² = O(n^(3-ε)) for ε = 1
- Case 1 applies: T(n) = Θ(n³)

### Key insights:

1. ✓ Copying adds Θ(n²) overhead per level
2. ✓ This doesn't change the asymptotic complexity (still Θ(n³))
3. ✓ The recursive structure (8 subproblems) dominates the cost
4. ✓ Copying makes the algorithm slower in practice (larger constants)
5. ✓ Copying requires O(n²) extra space per level

### Comparison with original:

| Aspect | Original (Index) | With Copying |
|--------|------------------|--------------|
| Time Complexity | Θ(n³) | Θ(n³) |
| Space Complexity | O(1) extra | O(n² log n) extra |
| Practical Speed | Faster | Slower |
| Implementation | More complex | Simpler |

**Conclusion:** Copying makes the algorithm simpler to implement but slower in practice, with no asymptotic improvement.

---

**End of Section 4.1 Solutions**
