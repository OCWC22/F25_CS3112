# Chapter 4.2 Exercises: Complete Solutions with Frameworks

**Section:** 4.2 - Strassen's Algorithm  
**Focus:** Computing with Strassen, generalizations, and applications

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Manual Computation** | "compute", "show your work" | Execute algorithm step-by-step | Follow 7 products, combine, verify |
| **Write Pseudocode** | "write pseudocode" | Implement algorithm clearly | Base case, partition, 7 recursions, combine |
| **Generalize Base Case** | "k×k matrices", "k multiplications" | Change base case size | New recurrence, solve, compare |
| **Compare Algorithms** | "which method", "best asymptotic" | Determine optimal approach | Calculate exponents, compare |
| **Apply Insight** | "complex numbers", "using only" | Use trade-off idea elsewhere | Find algebraic trick, reduce operations |
| **Use as Subroutine** | "given algorithm", "show how" | Reduce to known problem | Express in terms of subroutine |

---

## Exercise 4.2-1: Compute Matrix Product

### Problem Statement
Use Strassen's algorithm to compute the matrix product:
```
[1  3]   [6  8]
[7  5] × [4  2]
```
Show your work.

---

### What This Problem Is Asking

**Task:** Execute Strassen's algorithm manually on 2×2 matrices
**Goal:** Show understanding of the 7 products and combination formulas
**Verification:** Result should match standard multiplication

**Framework:**
1. Partition into 1×1 submatrices
2. Compute P₁ through P₇ using formulas
3. Compute C₁₁, C₁₂, C₂₁, C₂₂ from P values
4. Assemble result
5. Verify with standard method

---

### Solution

**Given:**
```
A = [1  3]    B = [6  8]
    [7  5]        [4  2]
```

**Step 1: Partition (n = 2, so n/2 = 1)**
```
A₁₁ = 1    A₁₂ = 3
A₂₁ = 7    A₂₂ = 5

B₁₁ = 6    B₁₂ = 8
B₂₁ = 4    B₂₂ = 2
```

---

**Step 2: Compute 7 Products**

**P₁ = A₁₁(B₁₂ - B₂₂)**
```
B₁₂ - B₂₂ = 8 - 2 = 6
P₁ = 1 × 6 = 6
```

**P₂ = (A₁₁ + A₁₂)B₂₂**
```
A₁₁ + A₁₂ = 1 + 3 = 4
P₂ = 4 × 2 = 8
```

**P₃ = (A₂₁ + A₂₂)B₁₁**
```
A₂₁ + A₂₂ = 7 + 5 = 12
P₃ = 12 × 6 = 72
```

**P₄ = A₂₂(B₂₁ - B₁₁)**
```
B₂₁ - B₁₁ = 4 - 6 = -2
P₄ = 5 × (-2) = -10
```

**P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)**
```
A₁₁ + A₂₂ = 1 + 5 = 6
B₁₁ + B₂₂ = 6 + 2 = 8
P₅ = 6 × 8 = 48
```

**P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)**
```
A₁₂ - A₂₂ = 3 - 5 = -2
B₂₁ + B₂₂ = 4 + 2 = 6
P₆ = (-2) × 6 = -12
```

**P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)**
```
A₁₁ - A₂₁ = 1 - 7 = -6
B₁₁ + B₁₂ = 6 + 8 = 14
P₇ = (-6) × 14 = -84
```

**Summary:**
```
P₁ = 6, P₂ = 8, P₃ = 72, P₄ = -10, P₅ = 48, P₆ = -12, P₇ = -84
```

---

**Step 3: Combine to Get C**

**C₁₁ = P₅ + P₄ - P₂ + P₆**
```
= 48 + (-10) - 8 + (-12)
= 48 - 10 - 8 - 12
= 18
```

**C₁₂ = P₁ + P₂**
```
= 6 + 8
= 14
```

**C₂₁ = P₃ + P₄**
```
= 72 + (-10)
= 62
```

**C₂₂ = P₅ + P₁ - P₃ - P₇**
```
= 48 + 6 - 72 - (-84)
= 48 + 6 - 72 + 84
= 66
```

---

**Step 4: Assemble Result**
```
C = [18  14]
    [62  66]
```

---

**Step 5: Verification (Standard Method)**
```
C[1,1] = 1×6 + 3×4 = 6 + 12 = 18 ✓
C[1,2] = 1×8 + 3×2 = 8 + 6 = 14 ✓
C[2,1] = 7×6 + 5×4 = 42 + 20 = 62 ✓
C[2,2] = 7×8 + 5×2 = 56 + 10 = 66 ✓
```

**Perfect match!** ✓

---

### Key Observations

1. **Only 7 scalar multiplications used** (not 8)
2. **Many additions/subtractions** (18 total)
3. **Correct result** verified by standard method
4. **For 2×2 matrices:** Not faster in practice (overhead), but demonstrates the technique

---

## Exercise 4.2-2: Write Pseudocode

**Note:** Already provided in the guide above. Here's the complete solution.

### Solution

```
STRASSEN-MULTIPLY(A, B, n)
    // Input: Two n×n matrices A and B (n is power of 2)
    // Output: Product matrix C = A × B
    
    // Base case
    if n == 1
        C[1,1] = A[1,1] × B[1,1]
        return C
    
    // Divide: partition into n/2 × n/2 submatrices
    A₁₁ = A[1:n/2, 1:n/2]
    A₁₂ = A[1:n/2, n/2+1:n]
    A₂₁ = A[n/2+1:n, 1:n/2]
    A₂₂ = A[n/2+1:n, n/2+1:n]
    
    B₁₁ = B[1:n/2, 1:n/2]
    B₁₂ = B[1:n/2, n/2+1:n]
    B₂₁ = B[n/2+1:n, 1:n/2]
    B₂₂ = B[n/2+1:n, n/2+1:n]
    
    // Conquer: compute 7 products recursively
    P₁ = STRASSEN-MULTIPLY(A₁₁, B₁₂ - B₂₂, n/2)
    P₂ = STRASSEN-MULTIPLY(A₁₁ + A₁₂, B₂₂, n/2)
    P₃ = STRASSEN-MULTIPLY(A₂₁ + A₂₂, B₁₁, n/2)
    P₄ = STRASSEN-MULTIPLY(A₂₂, B₂₁ - B₁₁, n/2)
    P₅ = STRASSEN-MULTIPLY(A₁₁ + A₂₂, B₁₁ + B₂₂, n/2)
    P₆ = STRASSEN-MULTIPLY(A₁₂ - A₂₂, B₂₁ + B₂₂, n/2)
    P₇ = STRASSEN-MULTIPLY(A₁₁ - A₂₁, B₁₁ + B₁₂, n/2)
    
    // Combine: compute result submatrices
    C₁₁ = P₅ + P₄ - P₂ + P₆
    C₁₂ = P₁ + P₂
    C₂₁ = P₃ + P₄
    C₂₂ = P₅ + P₁ - P₃ - P₇
    
    // Assemble result matrix
    C[1:n/2, 1:n/2] = C₁₁
    C[1:n/2, n/2+1:n] = C₁₂
    C[n/2+1:n, 1:n/2] = C₂₁
    C[n/2+1:n, n/2+1:n] = C₂₂
    
    return C
```

**Time complexity:** T(n) = 7T(n/2) + Θ(n²) = Θ(n^2.807)

---

## Exercise 4.2-3: Generalize to k×k Base Case

### Problem Statement
What is the largest k such that if you can multiply 3×3 matrices using k multiplications (not assuming commutativity of multiplication), then you can multiply n×n matrices in o(n^(lg 7)) time? What is the running time of this algorithm?

---

### What This Problem Is Asking

**Scenario:** Instead of recursing to 1×1 base case, recurse to 3×3 base case
- Divide n×n into nine (n/3)×(n/3) submatrices
- Use special algorithm to multiply 3×3 with only k multiplications
- Question: What's the maximum k that still beats Strassen?

**Framework:**
1. Write recurrence for k multiplications on 3×3 base
2. Solve recurrence
3. Find condition for o(n^(lg 7))
4. Determine maximum k

---

### Solution

**Step 1: Recurrence with k Multiplications**

If we can multiply 3×3 matrices with k multiplications:
```
T(n) = kT(n/3) + Θ(n²)
```

**Why?**
- Divide n×n into 9 blocks of (n/3)×(n/3)
- Need k multiplications to compute result
- Each multiplication is on (n/3)×(n/3) matrices
- Non-recursive work: Θ(n²) for additions

---

**Step 2: Solve Recurrence**

Using Master Theorem:
- a = k (subproblems)
- b = 3 (size reduction factor)
- f(n) = Θ(n²)

**Critical exponent:**
```
log_b a = log₃ k
n^(log₃ k) = n^(log k / log 3)
```

**Compare with f(n) = n²:**

**Case 1:** If n^(log₃ k) > n², then T(n) = Θ(n^(log₃ k))

For this to happen:
```
log₃ k > 2
k > 3² = 9
```

So if k > 9, then T(n) = Θ(n^(log₃ k))

---

**Step 3: Find Condition for o(n^(lg 7))**

We want:
```
T(n) = o(n^(lg 7))
```

This means:
```
n^(log₃ k) < n^(lg 7)
log₃ k < lg 7
k < 3^(lg 7)
```

**Calculate 3^(lg 7):**
```
lg 7 ≈ 2.807
3^2.807 ≈ 21.85
```

So we need k < 21.85

---

**Step 4: Determine Maximum k**

Since k must be an integer:
```
k ≤ 21
```

**Maximum k = 21**

---

**Step 5: Running Time with k = 21**

```
T(n) = 21T(n/3) + Θ(n²)

Using Master Theorem:
log₃ 21 = log 21 / log 3 ≈ 2.771

T(n) = Θ(n^2.771)
```

**Comparison:**
- Strassen: Θ(n^2.807)
- With k=21: Θ(n^2.771)
- **Faster than Strassen!** ✓

---

### Summary

**Maximum k:** 21 multiplications for 3×3 matrices

**Running time:** T(n) = Θ(n^(log₃ 21)) ≈ Θ(n^2.771)

**Why this works:**
- Dividing by 3 instead of 2 changes the base
- 21 subproblems on base 3 is better than 7 on base 2
- log₃ 21 < log₂ 7

**Key insight:** Larger base case with efficient algorithm can beat smaller base case!

---

## Exercise 4.2-4: Compare Pan's Algorithms

### Problem Statement
V. Pan discovered:
- 68×68 matrices using 132,464 multiplications
- 70×70 matrices using 143,640 multiplications
- 72×72 matrices using 155,424 multiplications

Which method yields the best asymptotic running time when used in a divide-and-conquer matrix-multiplication algorithm? How does it compare with Strassen's algorithm?

---

### What This Problem Is Asking

**Scenario:** Use each as base case in divide-and-conquer
**Task:** Determine which gives best asymptotic time
**Comparison:** How do they compare to Strassen?

**Framework:**
1. Write recurrence for each method
2. Calculate critical exponent for each
3. Compare exponents
4. Determine winner

---

### Solution

**Step 1: Recurrence for Each Method**

**Method 1 (68×68 with 132,464 multiplications):**
```
T(n) = 132,464 × T(n/68) + Θ(n²)
```

**Method 2 (70×70 with 143,640 multiplications):**
```
T(n) = 143,640 × T(n/70) + Θ(n²)
```

**Method 3 (72×72 with 155,424 multiplications):**
```
T(n) = 155,424 × T(n/72) + Θ(n²)
```

---

**Step 2: Calculate Critical Exponents**

Using Master Theorem, the solution is Θ(n^(log_b a)) where:
- a = number of multiplications
- b = base case size

**Method 1:**
```
log₆₈ 132,464 = log 132,464 / log 68 ≈ 2.7951284
```

**Method 2:**
```
log₇₀ 143,640 = log 143,640 / log 70 ≈ 2.7951284
```

**Method 3:**
```
log₇₂ 155,424 = log 155,424 / log 72 ≈ 2.7951284
```

**Surprising result:** All three give the **same exponent**! ≈ 2.795

---

**Step 3: Why Are They Equal?**

**The pattern:**
```
132,464 / 68² ≈ 28.633
143,640 / 70² ≈ 29.314
155,424 / 72² ≈ 29.993
```

These ratios are approximately equal! Pan designed them this way.

**Mathematical relationship:**
```
If a/b² ≈ constant, then log_b a ≈ 2 + log constant
```

All three have similar ratios, so similar exponents.

---

**Step 4: Compare with Strassen**

| Algorithm | Exponent | Approximate Value |
|-----------|----------|-------------------|
| Strassen | log₂ 7 | 2.807 |
| Pan (all 3) | ~2.795 | 2.795 |

**Winner:** Pan's algorithms are slightly better!

**Improvement:**
```
n^2.807 / n^2.795 = n^0.012

For n = 1000: speedup ≈ 1000^0.012 ≈ 1.03 (3% faster)
```

**Practical consideration:**
- Pan's algorithms have HUGE constants (132,464 multiplications!)
- Only faster for extremely large matrices
- Strassen is more practical

---

### Summary

**Best method:** All three Pan algorithms give same asymptotic time

**Running time:** Θ(n^2.795)

**Comparison with Strassen:**
- Pan: Θ(n^2.795)
- Strassen: Θ(n^2.807)
- Pan is slightly better asymptotically

**Practical reality:**
- Pan's huge constants make it impractical
- Strassen is better for real-world use
- Shows the gap between theory and practice

---

## Exercise 4.2-5: Complex Number Multiplication

### Problem Statement
Show how to multiply the complex numbers a + bi and c + di using only three multiplications of real numbers. The algorithm should take a, b, c, and d as input and produce the real component ac - bd and the imaginary component ad + bc separately.

---

### What This Problem Is Asking

**Standard method:**
```
(a + bi)(c + di) = ac - bd + (ad + bc)i

Real part: ac - bd       (2 multiplications: ac, bd)
Imaginary part: ad + bc  (2 multiplications: ad, bc)

Total: 4 real multiplications
```

**Challenge:** Reduce to 3 multiplications using Strassen's insight

**Framework:**
1. Identify what we need: ac, bd, ad, bc
2. Find algebraic trick to compute with fewer multiplications
3. Use additions to recover needed values
4. Verify correctness

---

### Solution

**Step 1: The Trick**

Compute these three products:
```
P₁ = a × c
P₂ = b × d
P₃ = (a + b) × (c + d)
```

**Step 2: Expand P₃**
```
P₃ = (a + b)(c + d)
   = ac + ad + bc + bd
   = P₁ + ad + bc + P₂
```

**Step 3: Solve for ad + bc**
```
P₃ = P₁ + (ad + bc) + P₂
ad + bc = P₃ - P₁ - P₂
```

**Step 4: Compute Result**

**Real part:**
```
ac - bd = P₁ - P₂
```

**Imaginary part:**
```
ad + bc = P₃ - P₁ - P₂
```

---

### Complete Algorithm

```
COMPLEX-MULTIPLY(a, b, c, d)
    // Input: Complex numbers (a+bi) and (c+di)
    // Output: Real and imaginary parts of product
    
    // Three multiplications
    P₁ = a × c
    P₂ = b × d
    P₃ = (a + b) × (c + d)
    
    // Compute result components
    real_part = P₁ - P₂
    imaginary_part = P₃ - P₁ - P₂
    
    return (real_part, imaginary_part)
```

**Operations count:**
- **3 multiplications:** P₁, P₂, P₃
- **4 additions:** (a+b), (c+d), P₃-P₁, (result)-P₂
- **Total:** 3 multiplications, 4 additions

---

### Verification

**Example:** (3 + 4i) × (2 + 5i)

**Standard method:**
```
Real: 3×2 - 4×5 = 6 - 20 = -14
Imaginary: 3×5 + 4×2 = 15 + 8 = 23
Result: -14 + 23i
```

**Our method:**
```
P₁ = 3 × 2 = 6
P₂ = 4 × 5 = 20
P₃ = (3+4) × (2+5) = 7 × 7 = 49

Real: P₁ - P₂ = 6 - 20 = -14 ✓
Imaginary: P₃ - P₁ - P₂ = 49 - 6 - 20 = 23 ✓
Result: -14 + 23i ✓
```

**Perfect match!**

---

### Key Insights

1. **Trade-off:** 3 multiplications + 4 additions vs 4 multiplications + 1 addition
2. **Savings:** 1 multiplication at cost of 3 extra additions
3. **Same principle as Strassen:** Reduce expensive operations
4. **Practical:** Actually useful for complex arithmetic in signal processing

---

## Exercise 4.2-6: Using Squaring to Multiply

### Problem Statement
Suppose that you have a Θ(n^α)-time algorithm for squaring n×n matrices, where α ≥ 2. Show how to use that algorithm to multiply two different n×n matrices in Θ(n^α) time.

---

### What This Problem Is Asking

**Given:** Fast squaring algorithm
- SQUARE(A) computes A² in Θ(n^α) time

**Task:** Design multiplication algorithm using squaring
- MULTIPLY(A, B) should compute A×B in Θ(n^α) time

**Challenge:** Express multiplication in terms of squaring

**Framework:**
1. Find algebraic identity relating multiplication to squaring
2. Write algorithm using identity
3. Count operations
4. Verify time complexity

---

### Solution

**Step 1: The Algebraic Identity**

**Key identity:**
```
(A + B)² - (A - B)² = A² + AB + BA + B² - (A² - AB - BA + B²)
                     = A² + AB + BA + B² - A² + AB + BA - B²
                     = 2AB + 2BA
```

If matrices commute (AB = BA):
```
(A + B)² - (A - B)² = 4AB
AB = [(A + B)² - (A - B)²] / 4
```

**But matrices don't commute in general!** (AB ≠ BA)

**Better identity:**
```
(A + B)² = A² + AB + BA + B²
(A - B)² = A² - AB - BA + B²

(A + B)² - (A - B)² = 2AB + 2BA
```

We need AB, not AB + BA. Let's try another approach.

---

**Step 2: Alternative Identity**

**Use this identity:**
```
(A + B)² - A² - B² = AB + BA
```

**But we need just AB, not AB + BA.**

**Better approach - use padding:**

Create augmented matrices:
```
     [A  B]²   [A²+AB    AB+B²]
M =  [0  0]  = [0        0    ]
```

Actually, this gets complicated. Let's use the standard identity:

**The solution:**
```
AB = [(A + B)² - A² - B²] / 2  (if AB = BA)
```

**For non-commuting matrices, use:**
```
     [0  A]²   [AB  0]
M =  [B  0]  = [0   BA]
```

Then AB is in the top-right block!

---

**Step 3: Complete Algorithm**

```
MULTIPLY-USING-SQUARE(A, B, n)
    // Create augmented 2n × 2n matrix
    M = [0  A]
        [B  0]
    
    // Square it
    M² = SQUARE(M, 2n)
    
    // Extract result
    // M² = [AB  0 ]
    //      [0   BA]
    
    return M²[1:n, n+1:2n]  // top-right block is AB
```

**Time complexity:**
- Create M: Θ(n²)
- Square M: Θ((2n)^α) = Θ(2^α × n^α) = Θ(n^α)
- Extract result: Θ(n²)
- **Total: Θ(n^α) + Θ(n²) = Θ(n^α)** (since α ≥ 2)

---

**Step 4: Verification**

**Why this works:**
```
[0  A]   [0  A]   [0·0+A·B  0·A+A·0]   [AB  0 ]
[B  0] × [B  0] = [B·0+0·B  B·A+0·0] = [0   BA]
```

The top-right block is exactly AB! ✓

---

### Alternative Solution (Simpler)

**If we assume AB = BA (commutative):**

```
MULTIPLY-USING-SQUARE(A, B, n)
    // Compute three squares
    S₁ = SQUARE(A + B, n)    // (A+B)²
    S₂ = SQUARE(A, n)        // A²
    S₃ = SQUARE(B, n)        // B²
    
    // Compute AB
    AB = (S₁ - S₂ - S₃) / 2
    
    return AB
```

**Time complexity:**
- Three squarings: 3 × Θ(n^α) = Θ(n^α)
- Subtractions and division: Θ(n²)
- **Total: Θ(n^α)**

**Note:** This only works if AB = BA, which isn't true for general matrices!

---

### Summary

**Using augmented matrix:**
- Create [0 A; B 0]
- Square it to get [AB 0; 0 BA]
- Extract AB
- Time: Θ(n^α)

**Key insight:** Can reduce multiplication to squaring with clever matrix construction

**Practical note:** This is mostly theoretical - squaring isn't usually faster than multiplication

---

## 📋 Quick Reference: All Exercises

### Exercise 4.2-1: Manual Computation
**Task:** Compute 2×2 product using Strassen  
**Steps:** Partition → 7 products → Combine → Verify  
**Result:** [18 14; 62 66]

### Exercise 4.2-2: Pseudocode
**Task:** Write Strassen's algorithm  
**Key:** Base case, 7 recursions, combine formulas  
**Time:** Θ(n^2.807)

### Exercise 4.2-3: k×k Base Case
**Task:** Find max k for 3×3 base  
**Answer:** k ≤ 21  
**Time:** Θ(n^2.771) with k=21

### Exercise 4.2-4: Pan's Algorithms
**Task:** Compare three methods  
**Answer:** All give Θ(n^2.795)  
**Best:** Slightly better than Strassen (2.795 vs 2.807)

### Exercise 4.2-5: Complex Numbers
**Task:** Multiply with 3 real multiplications  
**Trick:** P₃ = (a+b)(c+d), then ad+bc = P₃-ac-bd  
**Savings:** 4 → 3 multiplications

### Exercise 4.2-6: Squaring Subroutine
**Task:** Use squaring to multiply  
**Trick:** Square [0 A; B 0] to get [AB 0; 0 BA]  
**Time:** Θ(n^α)

---

## 🔑 Key Concepts Summary

### Strassen's Formulas (Memorize!)

**The 7 Products:**
```
P₁ = A₁₁(B₁₂ - B₂₂)
P₂ = (A₁₁ + A₁₂)B₂₂
P₃ = (A₂₁ + A₂₂)B₁₁
P₄ = A₂₂(B₂₁ - B₁₁)
P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)
```

**Combining:**
```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

---

### Complexity Comparison

| Algorithm | Multiplications | Recurrence | Solution |
|-----------|----------------|------------|----------|
| Naive | n³ | - | Θ(n³) |
| Standard D&C | 8 per level | 8T(n/2) + Θ(n²) | Θ(n³) |
| Strassen | 7 per level | 7T(n/2) + Θ(n²) | Θ(n^2.807) |
| Pan | varies | varies | Θ(n^2.795) |

---

### Why Strassen Works

**The trade-off:**
- 1 fewer multiplication (8 → 7)
- 14 more additions (4 → 18)
- Net win: multiplication is expensive!

**The math:**
- log₂ 8 = 3.000
- log₂ 7 = 2.807
- Small change in subproblems → big change in exponent

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Product Count
```
✗ "Strassen uses 8 products"
✓ Strassen uses exactly 7 products
```

### Mistake 2: Wrong Combination Formulas
```
✗ C₁₂ = P₁ + P₃ (wrong!)
✓ C₁₂ = P₁ + P₂ (correct)
```

### Mistake 3: Arithmetic Errors
```
✗ P₅ + P₄ - P₂ + P₆ = 48 + (-10) - 8 + (-12) = 20
✓ Careful: 48 - 10 - 8 - 12 = 18
```

### Mistake 4: Thinking It's Always Better
```
✗ "Always use Strassen"
✓ Only for large n (overhead for small n)
✓ Hybrid approach in practice
```

### Mistake 5: Assuming Commutativity
```
✗ "AB = BA for matrices"
✓ Matrix multiplication is NOT commutative!
✓ Must be careful with identities
```

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Memorize 7 product formulas
- [ ] Memorize 4 combination formulas
- [ ] Know Master Theorem
- [ ] Understand log₂ 7 ≈ 2.807

### While Solving
- [ ] For manual computation: work carefully, verify
- [ ] For pseudocode: include all 7 products
- [ ] For analysis: use Master Theorem
- [ ] For comparisons: calculate exponents

### Time Management
- Manual computation: 10-15 min
- Pseudocode: 10-15 min
- Analysis: 10-15 min
- Generalizations: 15-20 min

---

**You're ready to master Chapter 4.2! 🎉**

---

**End of Guide**
