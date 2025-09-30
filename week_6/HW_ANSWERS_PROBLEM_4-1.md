# Homework Solutions: Problem 4-1 - Recurrence Examples

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Problem:** 4-1 (Recurrence Examples - Parts a through g)  
**Date:** 2025-09-29

---

## Problem Statement

**Problem 4-1: Recurrence examples**

Give asymptotically tight upper and lower bounds for T(n) in each of the following algorithmic recurrences. Justify your answers.

a. T(n) = 2T(n/2) + n³
b. T(n) = T(8n/11) + n
c. T(n) = 16T(n/4) + n²
d. T(n) = 4T(n/2) + n² lg n
e. T(n) = 8T(n/3) + n²
f. T(n) = 7T(n/2) + n² lg n
g. T(n) = 2T(n/4) + √n

---

## Background: What Does "Tight Bounds" Mean?

### Asymptotic Notation Review

**Big-O (O):** Upper bound
- T(n) = O(f(n)) means T(n) grows no faster than f(n)
- Example: T(n) = 3n² + 5n = O(n²)

**Big-Omega (Ω):** Lower bound
- T(n) = Ω(f(n)) means T(n) grows at least as fast as f(n)
- Example: T(n) = 3n² + 5n = Ω(n²)

**Big-Theta (Θ):** Tight bound
- T(n) = Θ(f(n)) means T(n) grows exactly like f(n)
- T(n) = Θ(f(n)) if and only if T(n) = O(f(n)) AND T(n) = Ω(f(n))
- Example: T(n) = 3n² + 5n = Θ(n²)

**What the problem asks:**
- Find Θ(f(n)) - a function that gives both upper and lower bounds
- This is the "tight" bound - not too loose, not too tight
- We need to justify our answer (show our work!)

---

### Methods We'll Use

**For each recurrence, we'll use:**
1. **Master Theorem** (when applicable)
2. **Recursion Tree** (for intuition)
3. **Substitution Method** (for verification)

---

## Problem 4-1(a): T(n) = 2T(n/2) + n³

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 2T(n/2) + n³

**What this means:**
- Divide problem into 2 subproblems of size n/2
- Do n³ work to divide and combine
- This is a divide-and-conquer recurrence

---

### Step 2: Apply Master Theorem

**Master Theorem form:** T(n) = aT(n/b) + f(n)

**Identify parameters:**
- a = 2 (number of subproblems)
- b = 2 (size reduction factor)
- f(n) = n³ (divide/combine cost)

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₂ 2) = n^1 = n
```

**Compare f(n) with n^(log_b a):**
- f(n) = n³
- n^(log_b a) = n

**Clearly:** n³ >> n (much larger!)

**Is this polynomially larger?**

**Check:** Is n³ = Ω(n^(1+ε)) for some ε > 0?
- n³ = n^3
- n^(1+ε) requires 1 + ε ≤ 3
- So ε ≤ 2

**Choose ε = 1:**
```
n³ = Ω(n^(1+1)) = Ω(n²) ✓
```

**This is Case 3!**

---

### Step 3: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**Calculate:**
```
af(n/b) = 2 × (n/2)³
        = 2 × n³/8
        = n³/4
```

**We need:** n³/4 ≤ c × n³

**Simplify:** 1/4 ≤ c

**Choose c = 1/2:**
```
n³/4 ≤ (1/2)n³
1/4 ≤ 1/2 ✓
```

**Regularity holds!**

---

### Step 4: Apply Master Theorem Case 3

**Since:**
1. f(n) = Ω(n^(log_b a + ε)) with ε = 1 ✓
2. Regularity condition holds ✓

**Case 3 applies:**
```
T(n) = Θ(f(n)) = Θ(n³)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n³                              Cost: n³
                     /  \
Level 1:         (n/2)³  (n/2)³                       Cost: 2(n/2)³ = n³/4
                 /  \    /  \
Level 2:      (n/4)³ ... (4 nodes)                    Cost: 4(n/4)³ = n³/16
              ...
Level lg n:   1³ ... (n nodes)                        Cost: n × 1 = n
```

**Cost per level:**
- Level 0: n³
- Level 1: n³/4
- Level 2: n³/16
- Level i: n³/4^i

**This is a decreasing geometric series with r = 1/4 < 1**

**Total cost:**
```
T(n) = n³(1 + 1/4 + 1/16 + ...)
     = n³ × 1/(1 - 1/4)
     = n³ × 4/3
     = (4/3)n³
     = Θ(n³)
```

**The root dominates!**

---

### Step 6: Justify the Answer

**Why T(n) = Θ(n³)?**

**Upper bound (O):**
- By Master Theorem Case 3: T(n) = O(n³)
- The root level does n³ work
- All other levels sum to less than n³/3
- Total: at most (4/3)n³ = O(n³)

**Lower bound (Ω):**
- The root alone does n³ work
- So T(n) ≥ n³ = Ω(n³)

**Tight bound:**
- T(n) = O(n³) AND T(n) = Ω(n³)
- Therefore: T(n) = Θ(n³)

---

### Final Answer for 4-1(a)

**Recurrence:** T(n) = 2T(n/2) + n³

**Tight bound:** T(n) = Θ(n³)

**Justification:**
- Master Theorem Case 3 applies (f(n) polynomially larger than n^(log₂ 2) = n)
- Regularity condition holds: 2(n/2)³ = n³/4 ≤ (1/2)n³
- Recursion tree shows root dominates (geometric series with r = 1/4)
- Therefore: T(n) = Θ(n³)

---

---

## Problem 4-1(b): T(n) = T(8n/11) + n

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = T(8n/11) + n

**What this means:**
- ONE subproblem of size 8n/11 (shrinks by factor 11/8)
- Linear work (n) per level
- Unusual shrinking factor!

---

### Step 2: Try Master Theorem

**Master Theorem form:** T(n) = aT(n/b) + f(n)

**Identify parameters:**
- a = 1 (one subproblem)
- b = 11/8 (size reduction factor - unusual!)
- f(n) = n

**Calculate critical exponent:**
```
n^(log_b a) = n^(log_(11/8) 1) = n^0 = 1
```

**Why?** Because log of 1 in any base is 0.

**Compare f(n) with n^(log_b a):**
- f(n) = n
- n^(log_b a) = 1

**Clearly:** n >> 1

**Is this polynomially larger?**
```
n = Ω(1^(1+ε)) = Ω(1) ✓ for any ε > 0
```

**This is Case 3!**

---

### Step 3: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**Calculate:**
```
af(n/b) = 1 × f(8n/11)
        = 8n/11
```

**We need:** 8n/11 ≤ c × n

**Simplify:** 8/11 ≤ c

**Since 8/11 ≈ 0.727 < 1:**

**Choose c = 0.8:**
```
8n/11 ≤ 0.8n
8/11 ≤ 0.8
0.727 ≤ 0.8 ✓
```

**Regularity holds!**

---

### Step 4: Apply Master Theorem Case 3

**Since:**
1. f(n) = n = Ω(n^(0+ε)) for any ε > 0 ✓
2. Regularity condition holds ✓

**Case 3 applies:**
```
T(n) = Θ(f(n)) = Θ(n)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n                               Cost: n
                      |
Level 1:            8n/11                             Cost: 8n/11
                      |
Level 2:          (8/11)²n                            Cost: (8/11)²n
                      |
Level 3:          (8/11)³n                            Cost: (8/11)³n
                      ...
```

**Cost per level:**
- Level i: (8/11)^i × n

**This is a decreasing geometric series with r = 8/11 < 1**

**Total cost:**
```
T(n) = n(1 + 8/11 + (8/11)² + ...)
     = n × 1/(1 - 8/11)
     = n × 11/3
     = (11/3)n
     = Θ(n)
```

**The root dominates!**

---

### Step 6: Justify the Answer

**Why T(n) = Θ(n)?**

**Upper bound:**
- Each level does at most n work
- Costs decrease geometrically
- Total: n × (geometric series) = O(n)

**Lower bound:**
- Root alone does n work
- So T(n) ≥ n = Ω(n)

**Tight bound:**
- T(n) = Θ(n)

---

### Final Answer for 4-1(b)

**Recurrence:** T(n) = T(8n/11) + n

**Tight bound:** T(n) = Θ(n)

**Justification:**
- Master Theorem Case 3 applies (f(n) = n polynomially larger than n^0 = 1)
- Regularity condition holds: 8n/11 ≤ 0.8n
- Recursion tree shows decreasing geometric series (r = 8/11)
- Root dominates: total = n × 11/3 = Θ(n)

---

---

## Problem 4-1(c): T(n) = 16T(n/4) + n²

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 16T(n/4) + n²

**What this means:**
- 16 subproblems of size n/4
- Quadratic work (n²) per level
- Very wide branching!

---

### Step 2: Apply Master Theorem

**Identify parameters:**
- a = 16
- b = 4
- f(n) = n²

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₄ 16)
```

**Calculate log₄ 16:**
```
log₄ 16 = log₄ 4² = 2
```

**So:** n^(log₄ 16) = n²

**Compare f(n) with n^(log_b a):**
- f(n) = n²
- n^(log_b a) = n²

**They're equal!**

---

### Step 3: Determine Which Case

**Since f(n) = Θ(n^(log_b a)):**

**Check if f(n) = Θ(n² × log^k n) for some k:**
- f(n) = n² = n² × log⁰ n
- So k = 0

**This is Case 2 with k = 0!**

---

### Step 4: Apply Master Theorem Case 2

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With k = 0:**
```
T(n) = Θ(n² × log^(0+1) n)
     = Θ(n² × log n)
     = Θ(n² lg n)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n²                              Cost: n²
                   /  |  \  \
Level 1:      (n/4)² ... (16 nodes)                   Cost: 16(n/4)² = n²
              /  |  \  \
Level 2:    (n/16)² ... (256 nodes)                   Cost: 256(n/16)² = n²
            ...
Level log₄ n: 1² ... (16^(log₄ n) = n² nodes)        Cost: n² × 1 = n²
```

**Cost per level:**
- Every level costs exactly n²!
- Number of levels: log₄ n = (lg n)/(lg 4) = (lg n)/2

**Total cost:**
```
T(n) = n² × (number of levels)
     = n² × log₄ n
     = n² × (lg n)/2
     = Θ(n² lg n)
```

**All levels contribute equally!**

---

### Step 6: Justify the Answer

**Why T(n) = Θ(n² lg n)?**

**Key insight:**
- Each level does exactly n² work
- There are log₄ n = Θ(lg n) levels
- Total: n² × lg n

**This is the classic "balanced" case where:**
- Work per level is constant (n²)
- Number of levels is logarithmic
- Result: Θ(n² lg n)

---

### Final Answer for 4-1(c)

**Recurrence:** T(n) = 16T(n/4) + n²

**Tight bound:** T(n) = Θ(n² lg n)

**Justification:**
- Master Theorem Case 2 applies (f(n) = n² = Θ(n^(log₄ 16)) with k = 0)
- Critical exponent: n^(log₄ 16) = n²
- All levels contribute equally (each costs n²)
- Number of levels: log₄ n = Θ(lg n)
- Therefore: T(n) = Θ(n² lg n)

---

---

## Problem 4-1(d): T(n) = 4T(n/2) + n² lg n

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 4T(n/2) + n² lg n

**What this means:**
- 4 subproblems of size n/2
- n² lg n work per level (quadratic with log factor)

---

### Step 2: Apply Master Theorem

**Identify parameters:**
- a = 4
- b = 2
- f(n) = n² lg n

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₂ 4) = n² 
```

**Compare f(n) with n^(log_b a):**
- f(n) = n² lg n
- n^(log_b a) = n²

**Compare:**
- f(n) = n² lg n
- n^(log_b a) = n²

**The difference is only the logarithmic factor lg n!**

---

### Step 3: Determine Which Case

**Check if this is Case 2:**

**Case 2 requires:** f(n) = Θ(n^(log_b a) × log^k n)

**We have:**
```
f(n) = n² lg n = n² × log¹ n
```

**So k = 1!**

**This is Case 2 with k = 1!**

---

### Step 4: Apply Master Theorem Case 2

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With k = 1:**
```
T(n) = Θ(n² × log^(1+1) n)
     = Θ(n² × log² n)
     = Θ(n² lg² n)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n² lg n                         Cost: n² lg n
                   /  |  \  \
Level 1:      (n/2)² lg(n/2) ... (4 nodes)            Cost: 4(n/2)² lg(n/2) = n²(lg n - 1)
              /  |  \  \
Level 2:    (n/4)² lg(n/4) ... (16 nodes)             Cost: 16(n/4)² lg(n/4) = n²(lg n - 2)
            ...
```

**Cost per level:**
- Level 0: n² lg n
- Level 1: n²(lg n - 1)
- Level 2: n²(lg n - 2)
- Level i: n²(lg n - i)

**Total cost:**
```
T(n) = n²[lg n + (lg n - 1) + (lg n - 2) + ... + 1]
     = n²[(lg n) + (lg n - 1) + ... + 1]
     = n² × Σ(i=1 to lg n) i
     = n² × (lg n)(lg n + 1)/2
     = Θ(n² lg² n)
```

---

### Step 6: Justify the Answer

**Why T(n) = Θ(n² lg² n)?**

**Key insight:**
- Each level i costs n²(lg n - i)
- Sum over lg n levels
- This is an arithmetic series that sums to Θ(lg² n)
- Multiply by n²: Θ(n² lg² n)

---

### Final Answer for 4-1(d)

**Recurrence:** T(n) = 4T(n/2) + n² lg n

**Tight bound:** T(n) = Θ(n² lg² n)

**Justification:**
- Master Theorem Case 2 applies (f(n) = n² lg n = Θ(n² × log¹ n) with k = 1)
- Critical exponent: n^(log₂ 4) = n²
- Costs per level form arithmetic series: n² lg n, n²(lg n-1), ..., n²
- Sum: n² × [lg n + (lg n-1) + ... + 1] = n² × Θ(lg² n)
- Therefore: T(n) = Θ(n² lg² n)

---

---

## Problem 4-1(e): T(n) = 8T(n/3) + n²

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 8T(n/3) + n²

**What this means:**
- 8 subproblems of size n/3
- Quadratic work (n²) per level

---

### Step 2: Apply Master Theorem

**Identify parameters:**
- a = 8
- b = 3
- f(n) = n²

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₃ 8)
```

**Calculate log₃ 8:**
```
log₃ 8 = lg 8 / lg 3
       = 3 / 1.585
       ≈ 1.893
```

**So:** n^(log₃ 8) ≈ n^1.893

**Compare f(n) with n^(log_b a):**
- f(n) = n² = n^2.0
- n^(log_b a) = n^1.893

**Clearly:** n² > n^1.893

---

### Step 3: Determine Which Case

**Is f(n) polynomially larger?**

**Check:** Is n² = Ω(n^(1.893 + ε)) for some ε > 0?

**We have:** n² = n^2.0

**Need:** 2.0 ≥ 1.893 + ε

**So:** ε ≤ 2.0 - 1.893 = 0.107

**Choose ε = 0.05:**
```
n² = Ω(n^(1.893 + 0.05)) = Ω(n^1.943) ✓
```

**This is Case 3!**

---

### Step 4: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**Calculate:**
```
af(n/b) = 8 × (n/3)²
        = 8 × n²/9
        = 8n²/9
```

**We need:** 8n²/9 ≤ c × n²

**Simplify:** 8/9 ≤ c

**Since 8/9 ≈ 0.889 < 1:**

**Choose c = 0.9:**
```
8n²/9 ≤ 0.9n²
8/9 ≤ 0.9
0.889 ≤ 0.9 ✓
```

**Regularity holds!**

---

### Step 5: Apply Master Theorem Case 3

**Since:**
1. f(n) = Ω(n^(log_b a + ε)) with ε = 0.05 ✓
2. Regularity condition holds ✓

**Case 3 applies:**
```
T(n) = Θ(f(n)) = Θ(n²)
```

---

### Step 6: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n²                              Cost: n²
                   /  |  \  \
Level 1:      (n/3)² ... (8 nodes)                    Cost: 8(n/3)² = 8n²/9
              /  |  \  \
Level 2:    (n/9)² ... (64 nodes)                     Cost: 64(n/9)² = 64n²/81
            ...
```

**Cost per level:**
- Level 0: n²
- Level 1: 8n²/9 ≈ 0.889n²
- Level 2: (8/9)²n² ≈ 0.790n²
- Level i: (8/9)^i × n²

**This is a decreasing geometric series with r = 8/9 < 1**

**Total cost:**
```
T(n) = n²(1 + 8/9 + (8/9)² + ...)
     = n² × 1/(1 - 8/9)
     = n² × 9
     = 9n²
     = Θ(n²)
```

**The root dominates!**

---

### Step 7: Justify the Answer

**Why T(n) = Θ(n²)?**

**Key insight:**
- Root does n² work
- Each subsequent level does (8/9) of previous level
- Geometric series sums to constant × n²
- Root dominates

---

### Final Answer for 4-1(e)

**Recurrence:** T(n) = 8T(n/3) + n²

**Tight bound:** T(n) = Θ(n²)

**Justification:**
- Master Theorem Case 3 applies (f(n) = n² polynomially larger than n^(log₃ 8) ≈ n^1.893)
- Regularity condition holds: 8(n/3)² = 8n²/9 ≤ 0.9n²
- Recursion tree shows decreasing geometric series (r = 8/9)
- Root dominates: total = n² × 9 = Θ(n²)

---

---

## Problem 4-1(f): T(n) = 7T(n/2) + n² lg n

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 7T(n/2) + n² lg n

**What this means:**
- 7 subproblems of size n/2
- n² lg n work per level
- This is similar to Strassen's algorithm!

---

### Step 2: Apply Master Theorem

**Identify parameters:**
- a = 7
- b = 2
- f(n) = n² lg n

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₂ 7) ≈ n^2.807
```

**Compare f(n) with n^(log_b a):**
- f(n) = n² lg n
- n^(log_b a) ≈ n^2.807

**Compare growth rates:**
- n² lg n grows slower than n^2.807
- Why? Because lg n grows slower than any polynomial n^ε

**Specifically:**
- n² lg n = o(n^(2.807))
- The logarithmic factor doesn't make up for the polynomial difference

---

### Step 3: Determine Which Case

**Is f(n) polynomially smaller?**

**Check:** Is n² lg n = O(n^(2.807 - ε)) for some ε > 0?

**Key fact:** n² lg n = O(n^(2+δ)) for any δ > 0

**So:** n² lg n = O(n^2.1) = O(n^(2.807 - 0.707))

**Choose ε = 0.5:**
```
n² lg n = O(n^(2.807 - 0.5)) = O(n^2.307) ✓
```

**This is Case 1!**

---

### Step 4: Apply Master Theorem Case 1

**Case 1 solution:** T(n) = Θ(n^(log_b a))

**Therefore:**
```
T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              n² lg n                         Cost: n² lg n
                   /  |  \  \ ...
Level 1:      (n/2)² lg(n/2) ... (7 nodes)            Cost: 7(n/2)² lg(n/2) ≈ 1.75n² lg n
              /  |  \  \ ...
Level 2:    (n/4)² lg(n/4) ... (49 nodes)             Cost: 49(n/4)² lg(n/4) ≈ 3.06n² lg n
            ...
```

**Cost per level (approximately):**
- Level 0: n² lg n
- Level 1: 1.75n² lg n (growing!)
- Level 2: 3.06n² lg n (growing!)
- Level i: (7/4)^i × n² lg n

**This is an increasing geometric series with r = 7/4 > 1**

**The leaves dominate!**

**Number of leaves:** 7^(lg n) = n^(log₂ 7) ≈ n^2.807

**Total cost dominated by leaves:**
```
T(n) = Θ(n^(log₂ 7))
```

---

### Step 6: Justify the Answer

**Why T(n) = Θ(n^2.807)?**

**Key insight:**
- Costs grow geometrically (r = 7/4 > 1)
- Last level dominates
- Number of leaves: n^(log₂ 7)
- Each leaf does constant work
- Total: Θ(n^(log₂ 7))

**Connection to Strassen:**
- Strassen's algorithm has recurrence T(n) = 7T(n/2) + Θ(n²)
- This is the same structure!
- Both have complexity Θ(n^2.807)

---

### Final Answer for 4-1(f)

**Recurrence:** T(n) = 7T(n/2) + n² lg n

**Tight bound:** T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

**Justification:**
- Master Theorem Case 1 applies (f(n) = n² lg n polynomially smaller than n^2.807)
- Critical exponent: n^(log₂ 7) ≈ n^2.807
- Recursion tree shows increasing costs (r = 7/4 > 1)
- Leaves dominate: 7^(lg n) = n^(log₂ 7) leaves
- Therefore: T(n) = Θ(n^2.807)

---

---

## Problem 4-1(g): T(n) = 2T(n/4) + √n

### Step 1: Identify the Recurrence Type

**Recurrence:** T(n) = 2T(n/4) + √n

**What this means:**
- 2 subproblems of size n/4
- √n work per level

---

### Step 2: Apply Master Theorem

**Identify parameters:**
- a = 2
- b = 4
- f(n) = √n = n^0.5

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₄ 2)
```

**Calculate log₄ 2:**
```
log₄ 2 = lg 2 / lg 4 = 1 / 2 = 0.5
```

**So:** n^(log₄ 2) = n^0.5 = √n

**Compare f(n) with n^(log_b a):**
- f(n) = √n
- n^(log_b a) = √n

**They're equal!**

---

### Step 3: Determine Which Case

**Since f(n) = Θ(n^(log_b a)):**

**Check if f(n) = Θ(n^0.5 × log^k n) for some k:**
- f(n) = √n = √n × log⁰ n
- So k = 0

**This is Case 2 with k = 0!**

---

### Step 4: Apply Master Theorem Case 2

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With k = 0:**
```
T(n) = Θ(√n × log^(0+1) n)
     = Θ(√n × log n)
     = Θ(√n lg n)
```

---

### Step 5: Verify with Recursion Tree

**Recursion tree visualization:**

```
Level 0:              √n                              Cost: √n
                     /  \
Level 1:         √(n/4)  √(n/4)                       Cost: 2√(n/4) = √n
                 /  \    /  \
Level 2:      √(n/16) ... (4 nodes)                   Cost: 4√(n/16) = √n
              ...
Level log₄ n: √1 ... (2^(log₄ n) nodes)              Cost: 2^(log₄ n) × 1
```

**Cost per level:**
- Every level costs exactly √n!

**Number of levels:**
```
log₄ n = (lg n)/(lg 4) = (lg n)/2
```

**Total cost:**
```
T(n) = √n × (number of levels)
     = √n × log₄ n
     = √n × (lg n)/2
     = Θ(√n lg n)
```

**All levels contribute equally!**

---

### Step 6: Justify the Answer

**Why T(n) = Θ(√n lg n)?**

**Key insight:**
- Each level does exactly √n work
- There are log₄ n = Θ(lg n) levels
- Total: √n × lg n

**This is the balanced case:**
- Work per level is constant (√n)
- Number of levels is logarithmic
- Result: Θ(√n lg n)

---

### Final Answer for 4-1(g)

**Recurrence:** T(n) = 2T(n/4) + √n

**Tight bound:** T(n) = Θ(√n lg n)

**Justification:**
- Master Theorem Case 2 applies (f(n) = √n = Θ(n^(log₄ 2)) with k = 0)
- Critical exponent: n^(log₄ 2) = √n
- All levels contribute equally (each costs √n)
- Number of levels: log₄ n = Θ(lg n)
- Therefore: T(n) = Θ(√n lg n)

---

---

## Summary Table: All Answers

| Part | Recurrence | Tight Bound | Method | Key Insight |
|------|------------|-------------|--------|-------------|
| (a) | T(n) = 2T(n/2) + n³ | Θ(n³) | Case 3 | Root dominates (r = 1/4) |
| (b) | T(n) = T(8n/11) + n | Θ(n) | Case 3 | Root dominates (r = 8/11) |
| (c) | T(n) = 16T(n/4) + n² | Θ(n² lg n) | Case 2 | All levels equal |
| (d) | T(n) = 4T(n/2) + n² lg n | Θ(n² lg² n) | Case 2 | All levels equal (k=1) |
| (e) | T(n) = 8T(n/3) + n² | Θ(n²) | Case 3 | Root dominates (r = 8/9) |
| (f) | T(n) = 7T(n/2) + n² lg n | Θ(n^2.807) | Case 1 | Leaves dominate (Strassen) |
| (g) | T(n) = 2T(n/4) + √n | Θ(√n lg n) | Case 2 | All levels equal |

---

## Key Patterns and Insights

### Pattern 1: Root Dominates (Case 3)
**When:** f(n) >> n^(log_b a)
**Examples:** (a), (b), (e)
**Result:** T(n) = Θ(f(n))
**Intuition:** Non-recursive work dominates

### Pattern 2: All Levels Equal (Case 2)
**When:** f(n) ≈ n^(log_b a) × log^k n
**Examples:** (c), (d), (g)
**Result:** T(n) = Θ(n^(log_b a) × log^(k+1) n)
**Intuition:** Balanced - all levels contribute

### Pattern 3: Leaves Dominate (Case 1)
**When:** f(n) << n^(log_b a)
**Examples:** (f)
**Result:** T(n) = Θ(n^(log_b a))
**Intuition:** Recursive calls dominate

---

## Master Theorem Quick Reference

**Given:** T(n) = aT(n/b) + f(n)

**Step 1:** Calculate n^(log_b a)

**Step 2:** Compare f(n) with n^(log_b a)

**Step 3:** Apply appropriate case:

| Case | Condition | Solution |
|------|-----------|----------|
| 1 | f(n) = O(n^(log_b a - ε)) | T(n) = Θ(n^(log_b a)) |
| 2 | f(n) = Θ(n^(log_b a) log^k n) | T(n) = Θ(n^(log_b a) log^(k+1) n) |
| 3 | f(n) = Ω(n^(log_b a + ε)) + regularity | T(n) = Θ(f(n)) |

---

## Common Mistakes to Avoid

### Mistake 1: Forgetting Regularity in Case 3
- Case 3 requires BOTH polynomial difference AND regularity
- Always check: af(n/b) ≤ cf(n) for some c < 1

### Mistake 2: Confusing Logarithmic and Polynomial Differences
- n vs n lg n: logarithmic (Case 2)
- n vs n²: polynomial (Case 1 or 3)

### Mistake 3: Wrong Logarithm Base
- Always use log_b a (not log₂ a)
- Convert: log_b a = (lg a)/(lg b)

### Mistake 4: Ignoring the k in Case 2
- If f(n) = n^(log_b a) × log^k n
- Then T(n) = Θ(n^(log_b a) × log^(k+1) n)
- The exponent on log increases by 1!

---

## Verification Checklist

For each problem, verify:
- ✅ Identified a, b, f(n) correctly
- ✅ Calculated n^(log_b a) correctly
- ✅ Compared f(n) with n^(log_b a) properly
- ✅ Checked regularity for Case 3
- ✅ Applied correct case formula
- ✅ Verified with recursion tree (optional but recommended)
- ✅ Stated tight bound Θ(...)
- ✅ Provided justification

---

**End of Problem 4-1 Solutions**
