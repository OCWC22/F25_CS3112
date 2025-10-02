# Chapter 4.1 Exercises: Complete Solutions with Frameworks

**Section:** 4.1 - Multiplying Square Matrices  
**Focus:** Divide-and-conquer matrix multiplication, recurrence analysis

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Generalize Algorithm** | "generalize", "not power of 2" | Handle edge cases, unequal splits | Use ceiling/floor, adjust recurrence |
| **Non-Square Matrices** | "kn × n", "rectangular" | Multiply different dimensions | Determine partitioning strategy, count calls |
| **Implementation Analysis** | "copying", "index calculation" | Compare implementation approaches | Calculate costs, compare recurrences |
| **Design Variant** | "write pseudocode", "matrix addition" | Apply technique to related problem | Follow divide-and-conquer template |

---

## Exercise 4.1-1: Generalize for Non-Powers of 2

### Problem Statement
Generalize MATRIX-MULTIPLY-RECURSIVE to multiply n×n matrices for which n is not necessarily an exact power of 2. Give a recurrence describing its running time. Argue that it runs in Θ(n³) time in the worst case.

---

### What This Problem Is Asking

**The issue:**
- Original algorithm assumes n is a power of 2 (n = 2^k)
- When dividing by 2, we get integer sizes: n/2, n/4, n/8, ...
- What if n = 5, 7, 10, 100, etc.?

**What breaks:**
- n/2 might not be an integer (e.g., 5/2 = 2.5)
- Submatrices might have different sizes
- Need to handle odd dimensions

**What we need to show:**
1. How to modify the algorithm
2. New recurrence relation
3. Proof that it's still Θ(n³)

---

### Framework to Solve

1. **Identify the fix:** Use ceiling ⌈n/2⌉ and floor ⌊n/2⌋
2. **Handle unequal submatrices:** Some size ⌈n/2⌉, some size ⌊n/2⌋
3. **Write new recurrence:** Account for unequal splits
4. **Prove Θ(n³):** Show asymptotic behavior unchanged

---

### Solution

**Step 1: Modified Algorithm**

```
MATRIX-MULTIPLY-RECURSIVE-GENERAL(A, B, C, n)
1  if n == 1
2    c₁₁ = c₁₁ + a₁₁ · b₁₁
3    return
4  // Divide (handle odd n)
5  n1 = ⌈n/2⌉    // size of top/left submatrices
6  n2 = ⌊n/2⌋    // size of bottom/right submatrices
7  partition A, B, C into submatrices of appropriate sizes
8  // Conquer (8 recursive calls with possibly different sizes)
9  MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₁₁, B₁₁, C₁₁, n1)
10 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₁₁, B₁₂, C₁₂, n1)
11 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₂₁, B₁₁, C₂₁, n2)
12 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₂₁, B₁₂, C₂₂, n2)
13 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₁₂, B₂₁, C₁₁, n2)
14 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₁₂, B₂₂, C₁₂, n2)
15 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₂₂, B₂₁, C₂₁, n2)
16 MATRIX-MULTIPLY-RECURSIVE-GENERAL(A₂₂, B₂₂, C₂₂, n2)
```

**Key changes:**
- Lines 5-6: Calculate submatrix sizes using ceiling and floor
- Lines 9-16: Pass appropriate sizes to recursive calls

**Example with n = 5:**
```
n = 5
n1 = ⌈5/2⌉ = ⌈2.5⌉ = 3
n2 = ⌊5/2⌋ = ⌊2.5⌋ = 2

Matrix partitioning:
[x x x | x x]
[x x x | x x]
[x x x | x x]
[-----+----]
[x x x | x x]
[x x x | x x]

Top-left: 3×3
Top-right: 3×2
Bottom-left: 2×3
Bottom-right: 2×2
```

---

**Step 2: Recurrence Analysis**

**Worst case:** n is odd, so submatrices have different sizes

**Sizes of recursive calls:**
- 4 calls on ⌈n/2⌉ × ⌈n/2⌉ matrices
- 4 calls on ⌊n/2⌋ × ⌊n/2⌋ matrices (or mixed sizes)

**Most general recurrence:**
```
T(n) = T(⌈n/2⌉) + T(⌊n/2⌋) + ... (8 terms total) + Θ(n²)
```

**Simplified worst-case recurrence:**
```
T(n) ≤ 8T(⌈n/2⌉) + Θ(n²)
```

**Why?**
- All recursive calls are on matrices of size at most ⌈n/2⌉
- This gives an upper bound

**For lower bound:**
```
T(n) ≥ 8T(⌊n/2⌋) + Θ(n²)
```

---

**Step 3: Prove T(n) = Θ(n³)**

**Upper bound (T(n) = O(n³)):**

Use recurrence: T(n) ≤ 8T(⌈n/2⌉) + cn² for some constant c

**Guess:** T(n) ≤ dn³ for some constant d

**Proof by induction:**

**Base case:** T(1) = Θ(1) ≤ d·1³ = d (for large enough d) ✓

**Inductive step:**
Assume T(k) ≤ dk³ for all k < n.

```
T(n) ≤ 8T(⌈n/2⌉) + cn²
     ≤ 8d(⌈n/2⌉)³ + cn²
     ≤ 8d(n/2 + 1)³ + cn²        [since ⌈n/2⌉ ≤ n/2 + 1]
     ≤ 8d(n/2)³(1 + 2/n)³ + cn²
     ≤ 8d(n³/8)(1 + 2/n)³ + cn²
     = dn³(1 + 2/n)³ + cn²
```

For large n, (1 + 2/n)³ ≈ 1, so:
```
T(n) ≤ dn³ + cn²
```

For n ≥ some n₀, the cn² term is negligible compared to dn³, so:
```
T(n) ≤ dn³  for n ≥ n₀
```

Therefore T(n) = O(n³) ✓

---

**Lower bound (T(n) = Ω(n³)):**

Use recurrence: T(n) ≥ 8T(⌊n/2⌋) + cn²

**Guess:** T(n) ≥ dn³ for some constant d

**Proof by induction:**

**Base case:** T(1) = Θ(1) ≥ d·1³ = d (for small enough d) ✓

**Inductive step:**
```
T(n) ≥ 8T(⌊n/2⌋) + cn²
     ≥ 8d(⌊n/2⌋)³ + cn²
     ≥ 8d(n/2 - 1)³ + cn²
     ≥ 8d(n/2)³(1 - 2/n)³ + cn²
     = dn³(1 - 2/n)³ + cn²
```

For large n, (1 - 2/n)³ ≈ 1, so:
```
T(n) ≥ dn³ + cn²
     ≥ dn³  for appropriate d
```

Therefore T(n) = Ω(n³) ✓

---

**Combining:**
Since T(n) = O(n³) and T(n) = Ω(n³), we have:
```
T(n) = Θ(n³) ✓
```

---

### Summary

**Modified algorithm:**
- Use ⌈n/2⌉ and ⌊n/2⌋ for submatrix sizes
- Handle unequal partitions
- Still makes 8 recursive calls

**Recurrence:**
```
T(n) = 8T(⌈n/2⌉) + Θ(n²)  [worst case]
```

**Solution:**
```
T(n) = Θ(n³)
```

**Key insight:** Ceiling/floor functions add at most constant overhead, don't change asymptotic complexity.

---

## Exercise 4.1-2: Non-Square Matrix Multiplication

### Problem Statement
How quickly can you multiply a kn × n matrix (kn rows and n columns) by an n × kn matrix, where k ≥ 1, using MATRIX-MULTIPLY-RECURSIVE as a subroutine? Answer the same question for multiplying an n × kn matrix by a kn × n matrix. Which is asymptotically faster, and by how much?

---

### What This Problem Is Asking

**Part 1:** Multiply (kn × n) by (n × kn)
```
[kn rows]   [n rows]     [kn rows]
[n cols ] × [kn cols] =  [kn cols]

Result: kn × kn matrix
```

**Part 2:** Multiply (n × kn) by (kn × n)
```
[n rows]    [kn rows]    [n rows]
[kn cols] × [n cols ] =  [n cols]

Result: n × n matrix
```

**What we need to find:**
1. How to partition non-square matrices
2. Number of recursive calls needed
3. Recurrence relation
4. Asymptotic running time
5. Which is faster and why

---

### Framework to Solve

1. **Understand dimensions:** Result size determines complexity
2. **Partition strategy:** Divide into square submatrices when possible
3. **Count subproblems:** How many recursive calls?
4. **Write recurrence:** Based on subproblem count and sizes
5. **Solve recurrence:** Find asymptotic time
6. **Compare:** Which grows faster?

---

### Solution Part 1: (kn × n) × (n × kn)

**Step 1: Understand the multiplication**

```
A: kn × n matrix
B: n × kn matrix
C = A × B: kn × kn matrix
```

**Step 2: Partition strategy**

Divide result C into k² blocks of size n × n:

```
C = [C₁₁  C₁₂  ...  C₁ₖ]
    [C₂₁  C₂₂  ...  C₂ₖ]
    [ ⋮    ⋮    ⋱    ⋮ ]
    [Cₖ₁  Cₖ₂  ...  Cₖₖ]
```

Each Cᵢⱼ is n × n.

**Step 3: Partition A and B**

```
A = [A₁]    (k blocks of size n × n)
    [A₂]
    [ ⋮]
    [Aₖ]

B = [B₁  B₂  ...  Bₖ]    (k blocks of size n × n)
```

**Step 4: Compute each block**

```
Cᵢⱼ = Aᵢ × Bⱼ
```

Each multiplication is n × n by n × n, giving n × n result.

**Step 5: Count operations**

- Number of blocks in C: k²
- Each block requires one n × n multiplication
- Total: k² multiplications of n × n matrices

**Step 6: Running time**

Using MATRIX-MULTIPLY-RECURSIVE for each n × n multiplication:
- Each call: T(n) = Θ(n³)
- Total calls: k²
- **Total time: k² × Θ(n³) = Θ(k²n³)**

---

### Solution Part 2: (n × kn) × (kn × n)

**Step 1: Understand the multiplication**

```
A: n × kn matrix
B: kn × n matrix
C = A × B: n × n matrix
```

**Step 2: Partition strategy**

Result C is just n × n (single block!).

**Step 3: Partition A and B**

```
A = [A₁  A₂  ...  Aₖ]    (k blocks of size n × n)

B = [B₁]    (k blocks of size n × n)
    [B₂]
    [ ⋮]
    [Bₖ]
```

**Step 4: Compute result**

```
C = A₁B₁ + A₂B₂ + ... + AₖBₖ
```

This is a sum of k products, each n × n.

**Step 5: Count operations**

- Number of multiplications: k (of n × n matrices)
- Number of additions: k-1 (of n × n matrices)

**Step 6: Running time**

- Multiplications: k × Θ(n³) = Θ(kn³)
- Additions: (k-1) × Θ(n²) = Θ(kn²)
- **Total time: Θ(kn³) + Θ(kn²) = Θ(kn³)**

---

### Comparison

| Operation | Result Size | Time Complexity |
|-----------|-------------|-----------------|
| (kn × n) × (n × kn) | kn × kn | Θ(k²n³) |
| (n × kn) × (kn × n) | n × n | Θ(kn³) |

**Which is faster?**

Compare Θ(k²n³) vs Θ(kn³):
```
Θ(k²n³) / Θ(kn³) = k
```

**Answer:** (n × kn) × (kn × n) is **k times faster** asymptotically!

**Why?**
- First case: Result is kn × kn, requires k² multiplications
- Second case: Result is n × n, requires only k multiplications
- Smaller result → less work

**Intuition:**
- Matrix multiplication cost depends on result size
- Larger result matrix → more elements to compute → more time

---

### Verification with Example

**Let k = 2, n = 4:**

**Case 1:** (8 × 4) × (4 × 8) = (8 × 8)
- Result has 64 elements
- Each element: 4 multiplications
- Total: 64 × 4 = 256 operations
- Time: Θ(4 × 4³) = Θ(256)

**Case 2:** (4 × 8) × (8 × 4) = (4 × 4)
- Result has 16 elements
- Each element: 8 multiplications
- Total: 16 × 8 = 128 operations
- Time: Θ(2 × 4³) = Θ(128)

Ratio: 256/128 = 2 = k ✓

---

### Summary

**Part 1: (kn × n) × (n × kn)**
- Result: kn × kn
- Time: Θ(k²n³)

**Part 2: (n × kn) × (kn × n)**
- Result: n × n
- Time: Θ(kn³)

**Comparison:**
- Part 2 is k times faster
- Reason: Smaller result matrix

**Key insight:** Matrix multiplication time depends on output size, not just input sizes!

---

## Exercise 4.1-3: Matrix Multiplication with Copying

**Note:** This problem is already solved in detail in HW_ANSWERS_4.1.md. Here's a concise summary.

### Problem Statement
Suppose that instead of partitioning matrices by index calculation in MATRIX-MULTIPLY-RECURSIVE, you copy the appropriate elements of A, B, and C into separate n/2 × n/2 submatrices. After the recursive calls, you copy the results back into C. How does recurrence (4.9) change, and what is its solution?

---

### What This Problem Is Asking

**Original (index calculation):**
- No copying, just track indices
- Partition cost: Θ(1)

**Modified (copying):**
- Copy elements to new arrays
- Copy results back
- Partition cost: Θ(n²)

**Questions:**
1. How does recurrence change?
2. What's the solution?
3. Does it affect asymptotic complexity?

---

### Solution Summary

**Step 1: Calculate copying costs**

**Copy IN:**
- Copy A and B into submatrices
- 2 matrices × 4 submatrices × (n/2)² elements = 2n²
- Cost: Θ(n²)

**Copy OUT:**
- Copy C submatrices back
- 4 submatrices × (n/2)² elements = n²
- Cost: Θ(n²)

**Total copying:** Θ(n²) + Θ(n²) = Θ(n²)

---

**Step 2: New recurrence**

```
T(n) = 8T(n/2) + Θ(n²)
```

**Same as original!** The copying adds Θ(n²) work, but original also had Θ(n²) for combining.

---

**Step 3: Solve recurrence**

Using Master Theorem:
- a = 8, b = 2, f(n) = Θ(n²)
- n^(log₂ 8) = n³
- f(n) = n² is polynomially smaller than n³
- **Case 1:** T(n) = Θ(n³)

---

**Step 4: Comparison**

| Aspect | Index Calculation | Copying |
|--------|-------------------|---------|
| Time | Θ(n³) | Θ(n³) |
| Space | O(1) extra | O(n²) extra |
| Practical speed | Faster | Slower |
| Implementation | Complex | Simple |

**Key insight:** Copying doesn't change asymptotic time but uses more space and has larger constants.

---

## Exercise 4.1-4: Matrix Addition with Divide-and-Conquer

### Problem Statement
Write pseudocode for a divide-and-conquer algorithm MATRIX-ADD-RECURSIVE that sums two n×n matrices A and B by partitioning each of them into four n/2 × n/2 submatrices and then recursively summing corresponding pairs of submatrices. Assume that matrix partitioning uses Θ(1)-time index calculations. Write a recurrence for the worst-case running time of MATRIX-ADD-RECURSIVE, and solve your recurrence. What happens if you use Θ(n²)-time copying to implement the partitioning instead of index calculations?

---

### What This Problem Is Asking

**Task 1:** Design recursive matrix addition algorithm
**Task 2:** Analyze with index calculation (Θ(1) partition)
**Task 3:** Analyze with copying (Θ(n²) partition)
**Task 4:** Compare with iterative approach

**Key question:** Is recursion helpful for addition?

---

### Framework to Solve

1. **Write pseudocode:** Follow divide-and-conquer template
2. **Identify costs:** Base case, partition, recursive calls, combine
3. **Write recurrence:** T(n) = aT(n/b) + f(n)
4. **Solve recurrence:** Use Master Theorem or expansion
5. **Compare approaches:** Recursive vs iterative, index vs copying

---

### Solution

**Step 1: Pseudocode**

```
MATRIX-ADD-RECURSIVE(A, B, C, n)
1  if n == 1
2    c₁₁ = a₁₁ + b₁₁
3    return
4  // Divide
5  partition A, B, C into n/2 × n/2 submatrices
     A₁₁, A₁₂, A₂₁, A₂₂; B₁₁, B₁₂, B₂₁, B₂₂; C₁₁, C₁₂, C₂₁, C₂₂
6  // Conquer
7  MATRIX-ADD-RECURSIVE(A₁₁, B₁₁, C₁₁, n/2)
8  MATRIX-ADD-RECURSIVE(A₁₂, B₁₂, C₁₂, n/2)
9  MATRIX-ADD-RECURSIVE(A₂₁, B₂₁, C₂₁, n/2)
10 MATRIX-ADD-RECURSIVE(A₂₂, B₂₂, C₂₂, n/2)
```

**Key observations:**
- Base case: Single element addition
- 4 recursive calls (one per submatrix pair)
- No combine step (addition done in place)

---

**Step 2: Analysis with Index Calculation**

**Costs:**
- Base case: Θ(1)
- Partition (line 5): Θ(1) with index calculation
- Recursive calls (lines 7-10): 4T(n/2)
- Combine: None (Θ(1))

**Recurrence:**
```
T(n) = 4T(n/2) + Θ(1)
```

---

**Step 3: Solve Recurrence (Index Calculation)**

**Using Master Theorem:**
- a = 4, b = 2, f(n) = Θ(1)
- n^(log_b a) = n^(log₂ 4) = n²

**Compare f(n) with n²:**
- f(n) = Θ(1) = O(n^(2-ε)) for any ε ≤ 2
- f(n) is polynomially smaller than n²

**Case 1 applies:**
```
T(n) = Θ(n^(log₂ 4)) = Θ(n²)
```

---

**Step 4: Analysis with Copying**

**Costs:**
- Partition: Θ(n²) - copy A, B, C into submatrices
- Recursive calls: 4T(n/2)
- Copy back: Θ(n²) - copy results to C

**Recurrence:**
```
T(n) = 4T(n/2) + Θ(n²)
```

---

**Step 5: Solve Recurrence (Copying)**

**Using Master Theorem:**
- a = 4, b = 2, f(n) = Θ(n²)
- n^(log_b a) = n²

**Compare f(n) with n²:**
- f(n) = Θ(n²) = Θ(n^(log_b a))

**Case 2 applies:**
```
T(n) = Θ(n² lg n)
```

**Why Case 2?**
When f(n) = Θ(n^(log_b a)), the solution is Θ(n^(log_b a) lg n).

---

**Step 6: Comparison**

| Approach | Recurrence | Solution | Notes |
|----------|------------|----------|-------|
| Iterative | - | Θ(n²) | Simple double loop |
| Recursive + Index | 4T(n/2) + Θ(1) | Θ(n²) | Same as iterative! |
| Recursive + Copying | 4T(n/2) + Θ(n²) | Θ(n² lg n) | Slower! |

**Key insights:**

1. **Index calculation:** Θ(n²) - same as iterative
   - Recursion adds no overhead asymptotically
   - But adds function call overhead in practice

2. **Copying:** Θ(n² lg n) - slower than iterative!
   - Extra lg n factor from recursion depth
   - Copying at each level adds up

3. **Iterative is best:**
   - Simplest implementation
   - No recursion overhead
   - Best practical performance

---

**Step 7: Why the Difference?**

**Matrix multiplication:**
```
T(n) = 8T(n/2) + Θ(n²)
Result: Θ(n³)
```
- 8 subproblems dominate
- Copying doesn't change asymptotic time

**Matrix addition:**
```
T(n) = 4T(n/2) + Θ(n²)
Result: Θ(n² lg n) with copying
```
- Only 4 subproblems
- Copying cost accumulates across lg n levels
- Total copying: n² × lg n = Θ(n² lg n)

**The difference:**
- Multiplication: Recursive calls dominate (n³ >> n² lg n)
- Addition: Copying cost significant (n² lg n vs n²)

---

### Summary

**Algorithm:** MATRIX-ADD-RECURSIVE
- 4 recursive calls
- No combine step

**With index calculation:**
- Recurrence: T(n) = 4T(n/2) + Θ(1)
- Solution: T(n) = Θ(n²)
- Same as iterative!

**With copying:**
- Recurrence: T(n) = 4T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n² lg n)
- Slower than iterative!

**Lesson:** Recursion not always helpful. For simple operations like addition, iterative is better.

---

## 📋 Quick Reference: All Exercises

### Exercise 4.1-1: Non-Powers of 2
- **Fix:** Use ⌈n/2⌉ and ⌊n/2⌋
- **Recurrence:** T(n) = 8T(⌈n/2⌉) + Θ(n²)
- **Solution:** T(n) = Θ(n³)

### Exercise 4.1-2: Non-Square Matrices
- **(kn×n) × (n×kn):** Θ(k²n³)
- **(n×kn) × (kn×n):** Θ(kn³)
- **Faster:** Second is k times faster

### Exercise 4.1-3: Copying
- **Recurrence:** T(n) = 8T(n/2) + Θ(n²)
- **Solution:** T(n) = Θ(n³)
- **Effect:** Same asymptotic time, more space

### Exercise 4.1-4: Matrix Addition
- **Index:** T(n) = 4T(n/2) + Θ(1) → Θ(n²)
- **Copying:** T(n) = 4T(n/2) + Θ(n²) → Θ(n² lg n)
- **Best:** Iterative Θ(n²)

---

**You've mastered Chapter 4.1 exercises! 🎉**

---

**End of Solutions**
