# Homework Solutions: Section 4.5 - The Master Method

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 4.5 (Solving Recurrences - Master Method)  
**Date:** 2025-09-29

---

## Background: What is the Master Method?

### The Problem

**We have recurrences of the form:**
```
T(n) = aT(n/b) + f(n)
```

**Where:**
- **a ≥ 1:** Number of subproblems
- **b > 1:** Factor by which problem size decreases
- **f(n):** Cost of dividing and combining

**Examples:**
- Merge sort: T(n) = 2T(n/2) + n → a=2, b=2, f(n)=n
- Binary search: T(n) = T(n/2) + 1 → a=1, b=2, f(n)=1
- Strassen: T(n) = 7T(n/2) + n² → a=7, b=2, f(n)=n²

---

### What is the Master Method?

**The Master Method is a formula that directly gives the solution!**

**No need for:**
- Drawing recursion trees
- Doing substitution proofs
- Summing geometric series

**Just:**
1. Identify a, b, and f(n)
2. Compare f(n) with n^(log_b a)
3. Apply the appropriate case
4. Read off the answer!

---

### The Master Theorem (Three Cases)

**Given:** T(n) = aT(n/b) + f(n)

**Calculate:** n^(log_b a) (this is the "critical exponent")

**Compare f(n) with n^(log_b a):**

---

#### Case 1: f(n) is polynomially smaller than n^(log_b a)

**Condition:** f(n) = O(n^(log_b a - ε)) for some ε > 0

**Translation:** f(n) grows slower than n^(log_b a)

**Solution:** T(n) = Θ(n^(log_b a))

**Intuition:** The leaves dominate (recursive calls do most of the work)

**Example:** T(n) = 8T(n/2) + n²
- n^(log_b a) = n^(log₂ 8) = n³
- f(n) = n² is smaller than n³
- Solution: T(n) = Θ(n³)

---

#### Case 2: f(n) is equal to n^(log_b a) (times a logarithmic factor)

**Condition:** f(n) = Θ(n^(log_b a) × log^k n) for some k ≥ 0

**Translation:** f(n) grows at the same rate as n^(log_b a)

**Solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**Intuition:** All levels contribute equally (balanced work)

**Example:** T(n) = 2T(n/2) + n
- n^(log_b a) = n^(log₂ 2) = n¹ = n
- f(n) = n = Θ(n × log⁰ n) (k=0)
- Solution: T(n) = Θ(n log n)

---

#### Case 3: f(n) is polynomially larger than n^(log_b a)

**Condition:** 
1. f(n) = Ω(n^(log_b a + ε)) for some ε > 0
2. **Regularity condition:** af(n/b) ≤ cf(n) for some c < 1 and large n

**Translation:** f(n) grows faster than n^(log_b a), and is "regular"

**Solution:** T(n) = Θ(f(n))

**Intuition:** The root dominates (divide/combine does most of the work)

**Example:** T(n) = 2T(n/2) + n²
- n^(log_b a) = n^(log₂ 2) = n
- f(n) = n² is larger than n
- Regularity: 2(n/2)² = n²/2 ≤ (1/2)n² ✓
- Solution: T(n) = Θ(n²)

---

### Key Concepts Explained

#### What is log_b a?

**Definition:** log_b a is the logarithm of a with base b

**What it means:** "How many times do I multiply b to get a?"

**Examples:**
- log₂ 8 = 3 (because 2³ = 8)
- log₂ 4 = 2 (because 2² = 4)
- log₃ 9 = 2 (because 3² = 9)
- log₂ 7 ≈ 2.807 (because 2^2.807 ≈ 7)

**Why it matters:**
- n^(log_b a) represents the cost of all the leaves in the recursion tree
- It's the "natural" growth rate for this recurrence

---

#### What is "polynomially smaller/larger"?

**Polynomially smaller:** f(n) = O(n^(log_b a - ε)) for some ε > 0
- Not just smaller, but smaller by a polynomial factor
- Example: n² is polynomially smaller than n³ (ε = 1)
- Example: n is polynomially smaller than n² (ε = 1)

**Polynomially larger:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0
- Not just larger, but larger by a polynomial factor
- Example: n² is polynomially larger than n (ε = 1)
- Example: n³ is polynomially larger than n² (ε = 1)

**Not polynomial difference:**
- n vs n log n (only logarithmic difference)
- n² vs n² log n (only logarithmic difference)
- These fall into Case 2!

---

#### What is the regularity condition?

**Condition:** af(n/b) ≤ cf(n) for some c < 1

**What it means:** The cost at the root is at least a constant fraction larger than the total cost of the children

**Why it's needed:** Ensures that the root level dominates, not just that f(n) is large

**How to check:**
```
af(n/b) ≤ cf(n)
```

**Example:** f(n) = n²
```
af(n/b) = 2(n/2)² = 2 × n²/4 = n²/2
cf(n) = c × n²

Need: n²/2 ≤ c × n²
So: 1/2 ≤ c

Choose c = 1/2 (or any c with 1/2 ≤ c < 1)
```

This works! ✓

---

## Problem 4.5-1: Master Method Applications

### Problem Statement
Use the master method to give tight asymptotic bounds for the following recurrences.

a. T(n) = 2T(n/4) + 1
b. T(n) = 2T(n/4) + √n
c. T(n) = 2T(n/4) + n
d. T(n) = 2T(n/4) + n²

---

## Problem 4.5-1(a): T(n) = 2T(n/4) + 1

### Step 1: Identify Parameters

**Recurrence:** T(n) = 2T(n/4) + 1

**Parameters:**
- a = 2 (number of subproblems)
- b = 4 (size reduction factor)
- f(n) = 1 (constant work)

---

### Step 2: Calculate n^(log_b a)

**Formula:** n^(log_b a) = n^(log₄ 2)

**Calculate log₄ 2:**
```
log₄ 2 = log₂ 2 / log₂ 4
       = 1 / 2
       = 0.5
```

**So:** n^(log₄ 2) = n^0.5 = √n

---

### Step 3: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = 1
- n^(log_b a) = √n

**Compare:**
- f(n) = 1 is constant
- √n grows with n

**Clearly:** 1 < √n for all n > 1

**Is f(n) polynomially smaller?**

**We need:** f(n) = O(n^(log_b a - ε)) for some ε > 0

**That is:** 1 = O(√n - ε) = O(n^(0.5 - ε))

**This is true for any ε < 0.5!**

**Choose ε = 0.25:**
```
1 = O(n^(0.5 - 0.25)) = O(n^0.25) = O(n^(1/4))
```

This is true because 1 is constant and n^(1/4) grows.

---

### Step 4: Apply Master Theorem

**Since f(n) = O(n^(log_b a - ε)) with ε = 0.25:**

**Case 1 applies!**

**Solution:** T(n) = Θ(n^(log_b a)) = Θ(n^(log₄ 2)) = Θ(√n)

---

### Final Answer for 4.5-1(a)

**Recurrence:** T(n) = 2T(n/4) + 1

**Parameters:** a = 2, b = 4, f(n) = 1

**Critical exponent:** n^(log₄ 2) = √n

**Comparison:** f(n) = 1 = O(n^(0.5-ε)) for ε = 0.25

**Case:** Case 1 (f(n) is polynomially smaller)

**Solution:** T(n) = Θ(√n)

---

## Problem 4.5-1(b): T(n) = 2T(n/4) + √n

### Step 1: Identify Parameters

**Recurrence:** T(n) = 2T(n/4) + √n

**Parameters:**
- a = 2
- b = 4
- f(n) = √n = n^0.5

---

### Step 2: Calculate n^(log_b a)

**From previous problem:** n^(log₄ 2) = √n = n^0.5

---

### Step 3: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = √n
- n^(log_b a) = √n

**They're equal!**

---

### Step 4: Check if Case 2 Applies

**Case 2 condition:** f(n) = Θ(n^(log_b a) × log^k n) for some k ≥ 0

**We have:** f(n) = √n = √n × log⁰ n

**So k = 0!**

**Case 2 applies!**

---

### Step 5: Apply Master Theorem

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With k = 0:**
```
T(n) = Θ(√n × log^(0+1) n)
     = Θ(√n × log n)
     = Θ(√n lg n)
```

---

### Final Answer for 4.5-1(b)

**Recurrence:** T(n) = 2T(n/4) + √n

**Parameters:** a = 2, b = 4, f(n) = √n

**Critical exponent:** n^(log₄ 2) = √n

**Comparison:** f(n) = √n = Θ(√n × log⁰ n)

**Case:** Case 2 with k = 0

**Solution:** T(n) = Θ(√n lg n)

---

## Problem 4.5-1(c): T(n) = 2T(n/4) + n

### Step 1: Identify Parameters

**Recurrence:** T(n) = 2T(n/4) + n

**Parameters:**
- a = 2
- b = 4
- f(n) = n

---

### Step 2: Calculate n^(log_b a)

**From before:** n^(log₄ 2) = √n

---

### Step 3: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = n
- n^(log_b a) = √n = n^0.5

**Compare:**
- n = n^1.0
- √n = n^0.5

**Clearly:** n > √n for all n > 1

**Is f(n) polynomially larger?**

**We need:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0

**That is:** n = Ω(√n + ε) = Ω(n^(0.5 + ε))

**We have:** n = n^1.0 and need n^(0.5 + ε)

**So:** 1.0 ≥ 0.5 + ε
**Thus:** ε ≤ 0.5

**Choose ε = 0.25:**
```
n = Ω(n^(0.5 + 0.25)) = Ω(n^0.75)
```

This is true! ✓

---

### Step 4: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**Calculate:**
```
af(n/b) = 2 × f(n/4)
        = 2 × (n/4)
        = n/2
```

**We need:** n/2 ≤ c × n

**Simplify:** 1/2 ≤ c

**Choose:** c = 1/2 (or any c with 1/2 ≤ c < 1, like c = 0.6)

**Wait!** We need c < 1, and we need 1/2 ≤ c.

**So:** 1/2 ≤ c < 1

**Choose c = 3/4:** 
```
n/2 ≤ (3/4)n
1/2 ≤ 3/4 ✓
```

**Regularity condition holds!** ✓

---

### Step 5: Apply Master Theorem

**Since:**
1. f(n) = Ω(n^(log_b a + ε)) with ε = 0.25 ✓
2. Regularity condition holds ✓

**Case 3 applies!**

**Solution:** T(n) = Θ(f(n)) = Θ(n)

---

### Final Answer for 4.5-1(c)

**Recurrence:** T(n) = 2T(n/4) + n

**Parameters:** a = 2, b = 4, f(n) = n

**Critical exponent:** n^(log₄ 2) = √n

**Comparison:** f(n) = n = Ω(n^(0.5+ε)) for ε = 0.25

**Regularity:** 2(n/4) = n/2 ≤ (3/4)n ✓

**Case:** Case 3 (f(n) is polynomially larger and regular)

**Solution:** T(n) = Θ(n)

---

## Problem 4.5-1(d): T(n) = 2T(n/4) + n²

### Step 1: Identify Parameters

**Recurrence:** T(n) = 2T(n/4) + n²

**Parameters:**
- a = 2
- b = 4
- f(n) = n²

---

### Step 2: Calculate n^(log_b a)

**From before:** n^(log₄ 2) = √n

---

### Step 3: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = n²
- n^(log_b a) = √n = n^0.5

**Compare:**
- n² = n^2.0
- √n = n^0.5

**Clearly:** n² >> √n (much larger!)

**Is f(n) polynomially larger?**

**We need:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0

**That is:** n² = Ω(n^(0.5 + ε))

**We have:** n² = n^2.0 and need n^(0.5 + ε)

**So:** 2.0 ≥ 0.5 + ε
**Thus:** ε ≤ 1.5

**Choose ε = 1:**
```
n² = Ω(n^(0.5 + 1)) = Ω(n^1.5)
```

This is true! ✓

---

### Step 4: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**Calculate:**
```
af(n/b) = 2 × f(n/4)
        = 2 × (n/4)²
        = 2 × n²/16
        = n²/8
```

**We need:** n²/8 ≤ c × n²

**Simplify:** 1/8 ≤ c

**Choose:** c = 1/4 (or any c with 1/8 ≤ c < 1)

**Verify:**
```
n²/8 ≤ (1/4)n²
1/8 ≤ 1/4 ✓
```

**Regularity condition holds!** ✓

---

### Step 5: Apply Master Theorem

**Since:**
1. f(n) = Ω(n^(log_b a + ε)) with ε = 1 ✓
2. Regularity condition holds ✓

**Case 3 applies!**

**Solution:** T(n) = Θ(f(n)) = Θ(n²)

---

### Final Answer for 4.5-1(d)

**Recurrence:** T(n) = 2T(n/4) + n²

**Parameters:** a = 2, b = 4, f(n) = n²

**Critical exponent:** n^(log₄ 2) = √n

**Comparison:** f(n) = n² = Ω(n^(0.5+ε)) for ε = 1

**Regularity:** 2(n/4)² = n²/8 ≤ (1/4)n² ✓

**Case:** Case 3 (f(n) is polynomially larger and regular)

**Solution:** T(n) = Θ(n²)

---

## Problem 4.5-1(e): T(n) = 2T(n/4) + n²

**Note:** This is the same as part (d)! There might be a typo in the problem statement.

**If the problem meant:** T(n) = 2T(n/4) + √n lg² n

Let me solve that version:

---

## Problem 4.5-1(e-corrected): T(n) = 2T(n/4) + √n lg² n

### Step 1: Identify Parameters

**Recurrence:** T(n) = 2T(n/4) + √n lg² n

**Parameters:**
- a = 2
- b = 4
- f(n) = √n lg² n = n^0.5 × (lg n)²

---

### Step 2: Calculate n^(log_b a)

**From before:** n^(log₄ 2) = √n = n^0.5

---

### Step 3: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = √n lg² n
- n^(log_b a) = √n

**Compare:**
- f(n) = √n × (lg n)²
- n^(log_b a) = √n × 1

**The difference is only the logarithmic factor (lg n)²!**

**This is NOT a polynomial difference, so neither Case 1 nor Case 3 applies.**

---

### Step 4: Check if Case 2 Applies

**Case 2 condition:** f(n) = Θ(n^(log_b a) × log^k n) for some k ≥ 0

**We have:** f(n) = √n × (lg n)² = √n × log² n

**So k = 2!**

**Case 2 applies!**

---

### Step 5: Apply Master Theorem

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With k = 2:**
```
T(n) = Θ(√n × log^(2+1) n)
     = Θ(√n × log³ n)
     = Θ(√n lg³ n)
```

---

### Final Answer for 4.5-1(e)

**Recurrence:** T(n) = 2T(n/4) + √n lg² n

**Parameters:** a = 2, b = 4, f(n) = √n lg² n

**Critical exponent:** n^(log₄ 2) = √n

**Comparison:** f(n) = √n lg² n = Θ(√n × log² n)

**Case:** Case 2 with k = 2

**Solution:** T(n) = Θ(√n lg³ n)

---

## Problem 4.5-2: Professor Caesar's Matrix Multiplication

### Problem Statement
Professor Caesar wants to develop a matrix-multiplication algorithm that is asymptotically faster than Strassen's algorithm. His algorithm will use the divide-and-conquer method, dividing each matrix into n/4 × n/4 submatrices, and the divide and combine steps together will take Θ(n²) time. Suppose that the professor's algorithm creates a recursive subproblems of size n/4. What is the largest integer value of a for which his algorithm could possibly run asymptotically faster than Strassen's?

---

### Step 1: Understand Strassen's Algorithm

**Strassen's recurrence:**
```
T_Strassen(n) = 7T(n/2) + Θ(n²)
```

**Solution:**
```
T_Strassen(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
```

**Goal:** Beat this! We need T(n) = o(n^2.807)

---

### Step 2: Set Up Caesar's Recurrence

**Caesar's algorithm:**
- Divides into n/4 × n/4 submatrices
- Creates a recursive subproblems of size n/4
- Divide and combine take Θ(n²)

**Recurrence:**
```
T_Caesar(n) = aT(n/4) + Θ(n²)
```

**Parameters:**
- a = ? (what we're solving for)
- b = 4
- f(n) = Θ(n²)

---

### Step 3: Apply Master Theorem

**Calculate critical exponent:**
```
n^(log_b a) = n^(log₄ a)
```

**We need to determine which case applies based on a.**

---

### Step 4: Determine the Solution Based on a

**Compare f(n) = n² with n^(log₄ a):**

**Case 1:** If n² < n^(log₄ a) (polynomially)
- Then T(n) = Θ(n^(log₄ a))

**Case 2:** If n² = Θ(n^(log₄ a))
- Then T(n) = Θ(n² lg n)

**Case 3:** If n² > n^(log₄ a) (polynomially)
- Then T(n) = Θ(n²)

---

### Step 5: Find When Each Case Applies

**For Case 1:** n² < n^(log₄ a)
```
2 < log₄ a
4² < a
16 < a
a > 16
```

**For Case 2:** n² = n^(log₄ a)
```
2 = log₄ a
a = 4² = 16
```

**For Case 3:** n² > n^(log₄ a)
```
2 > log₄ a
a < 16
```

---

### Step 6: Determine Solutions for Each Case

**If a > 16 (Case 1):**
```
T(n) = Θ(n^(log₄ a))
```

**If a = 16 (Case 2):**
```
T(n) = Θ(n² lg n)
```

**If a < 16 (Case 3):**
```
T(n) = Θ(n²)
```

---

### Step 7: Compare with Strassen

**Strassen:** T(n) = Θ(n^2.807)

**We need:** T_Caesar(n) < n^2.807 asymptotically

**Check each case:**

**Case 3 (a < 16):** T(n) = Θ(n²)
- n² < n^2.807 ✓
- This beats Strassen!

**Case 2 (a = 16):** T(n) = Θ(n² lg n)
- n² lg n < n^2.807 for large n? 
- lg n grows slower than n^0.807
- So n² lg n < n^2.807 ✓
- This beats Strassen!

**Case 1 (a > 16):** T(n) = Θ(n^(log₄ a))
- We need: log₄ a < 2.807
- log₄ a < 2.807
- a < 4^2.807

**Calculate 4^2.807:**
```
4^2.807 = (2²)^2.807 = 2^(2 × 2.807) = 2^5.614
```

**We know:** 2^5 = 32 and 2^6 = 64

**So:** 2^5.614 is between 32 and 64

**More precisely:**
```
2^5.614 ≈ 48.85
```

**So:** a < 48.85

**Since a must be an integer:** a ≤ 48

---

### Step 8: Find the Largest Integer a

**From our analysis:**
- If a ≤ 48, then T(n) < n^2.807 (beats Strassen)
- If a ≥ 49, then T(n) ≥ n^2.807 (doesn't beat Strassen)

**But wait!** Let's verify a = 49:

**With a = 49:**
```
log₄ 49 = lg 49 / lg 4 = lg 49 / 2
```

**Calculate lg 49:**
```
lg 49 = lg(7²) = 2 lg 7 ≈ 2 × 2.807 = 5.614
```

**So:**
```
log₄ 49 = 5.614 / 2 = 2.807
```

**This gives:** T(n) = Θ(n^2.807) - exactly the same as Strassen!

**Not faster!**

**Therefore, the largest a is 48.**

---

### Final Answer for Problem 4.5-2

**Caesar's recurrence:** T(n) = aT(n/4) + Θ(n²)

**Strassen's complexity:** Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

**To beat Strassen, we need:**
```
n^(log₄ a) < n^2.807
log₄ a < 2.807
a < 4^2.807
a < 2^5.614
a < 48.85
```

**Largest integer value:** a = 48

**Verification:**
- With a = 48: T(n) = Θ(n^(log₄ 48)) ≈ Θ(n^2.795) < Θ(n^2.807) ✓
- With a = 49: T(n) = Θ(n^(log₄ 49)) = Θ(n^2.807) (not faster) ✗

**Answer:** The largest integer value of a is **48**.

---

## Problem 4.5-3: Binary Search with Master Method

### Problem Statement
Use the master method to show that the solution to the binary-search recurrence T(n) = T(n/2) + Θ(1) is T(n) = Θ(lg n).

---

### Step 1: Understand Binary Search

**What is binary search?**
- Search for an element in a sorted array
- Compare with middle element
- Recurse on left or right half
- Constant work per step

**Recurrence:** T(n) = T(n/2) + Θ(1)

---

### Step 2: Identify Parameters

**Recurrence:** T(n) = T(n/2) + Θ(1)

**Parameters:**
- a = 1 (one subproblem)
- b = 2 (size halves)
- f(n) = Θ(1) (constant work)

---

### Step 3: Calculate n^(log_b a)

**Formula:** n^(log_b a) = n^(log₂ 1)

**Calculate log₂ 1:**
```
log₂ 1 = 0  (because 2⁰ = 1)
```

**So:** n^(log₂ 1) = n⁰ = 1

---

### Step 4: Compare f(n) with n^(log_b a)

**We have:**
- f(n) = Θ(1)
- n^(log_b a) = 1

**They're both constant!**

**So:** f(n) = Θ(n^(log_b a) × log⁰ n)

**This is Case 2 with k = 0!**

---

### Step 5: Apply Master Theorem

**Case 2 solution:** T(n) = Θ(n^(log_b a) × log^(k+1) n)

**With log_b a = 0 and k = 0:**
```
T(n) = Θ(n⁰ × log^(0+1) n)
     = Θ(1 × log n)
     = Θ(log n)
     = Θ(lg n)
```

---

### Final Answer for Problem 4.5-3

**Recurrence:** T(n) = T(n/2) + Θ(1)

**Parameters:** a = 1, b = 2, f(n) = Θ(1)

**Critical exponent:** n^(log₂ 1) = n⁰ = 1

**Comparison:** f(n) = Θ(1) = Θ(n⁰ × log⁰ n)

**Case:** Case 2 with k = 0

**Solution:** T(n) = Θ(lg n) ✓

**Interpretation:** Binary search takes logarithmic time, which makes sense - we halve the search space each time!

---

## Problem 4.5-4: Logarithmic Function and Master Theorem

### Problem Statement
Consider the function f(n) = lg n. Argue that although f(n/2) < f(n), the regularity condition af(n/b) ≤ cf(n) with a = 1 and b = 2 does not hold for any constant c < 1. Argue further that for any ε > 0, the condition in case 3 that f(n) = Ω(n^(log_b a + ε)) does not hold.

---

### Step 1: Understand the Setup

**Function:** f(n) = lg n

**Recurrence context:** T(n) = T(n/2) + lg n

**Parameters:**
- a = 1
- b = 2
- f(n) = lg n

**Critical exponent:** n^(log₂ 1) = n⁰ = 1

---

### Step 2: Show f(n/2) < f(n)

**Calculate:**
```
f(n) = lg n
f(n/2) = lg(n/2) = lg n - lg 2 = lg n - 1
```

**Compare:**
```
f(n/2) = lg n - 1 < lg n = f(n) ✓
```

**So yes, f(n/2) < f(n).**

---

### Step 3: Check Regularity Condition

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**With a = 1, b = 2:**
```
1 × f(n/2) ≤ c × f(n)
f(n/2) ≤ c × f(n)
lg(n/2) ≤ c × lg n
lg n - 1 ≤ c × lg n
```

**Rearrange:**
```
lg n - 1 ≤ c × lg n
lg n - c × lg n ≤ 1
lg n(1 - c) ≤ 1
lg n ≤ 1/(1 - c)
```

**Problem:** lg n grows without bound as n → ∞

**But:** 1/(1-c) is a constant (for fixed c)

**So:** For large enough n, lg n > 1/(1-c)

**This means the inequality fails for large n!**

**Conclusion:** The regularity condition does NOT hold for any constant c < 1. ✗

---

### Step 4: Why Regularity Fails

**Intuition:**
- The regularity condition requires the cost to decrease by a constant factor
- But lg(n/2) = lg n - 1 (only decreases by a constant, not a constant factor)
- The ratio f(n/2)/f(n) = (lg n - 1)/(lg n) → 1 as n → ∞
- This ratio never stays below a constant c < 1

**Mathematical proof:**
```
f(n/2)/f(n) = (lg n - 1)/(lg n) = 1 - 1/(lg n)
```

**As n → ∞:** 1/(lg n) → 0, so the ratio → 1

**For any c < 1:** Eventually 1 - 1/(lg n) > c

**So the regularity condition fails!**

---

### Step 5: Check Case 3 Condition

**Case 3 requires:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0

**With log_b a = 0:**
```
f(n) = Ω(n^(0 + ε)) = Ω(n^ε)
```

**We have:** f(n) = lg n

**Question:** Is lg n = Ω(n^ε) for any ε > 0?

**Answer:** NO!

---

### Step 6: Prove lg n ≠ Ω(n^ε)

**To show:** lg n is NOT Ω(n^ε) for any ε > 0

**Proof by contradiction:**

**Assume:** lg n = Ω(n^ε) for some ε > 0

**This means:** There exist constants c, n₀ such that lg n ≥ c × n^ε for all n ≥ n₀

**But:** We know that logarithms grow slower than any polynomial

**Specifically:** lim(n→∞) (lg n)/(n^ε) = 0 for any ε > 0

**This means:** For any c > 0, there exists N such that lg n < c × n^ε for all n > N

**This contradicts our assumption!**

**Conclusion:** lg n ≠ Ω(n^ε) for any ε > 0. ✗

---

### Step 7: Why This Matters

**The Master Theorem doesn't apply to T(n) = T(n/2) + lg n!**

**Why not?**
- Case 1: f(n) = lg n is not polynomially smaller than n⁰ = 1
- Case 2: f(n) = lg n is not Θ(1 × log^k n) for any k
- Case 3: Regularity condition fails, and f(n) is not Ω(n^ε)

**This recurrence falls in a "gap" between the cases!**

**Actual solution (by other methods):**
```
T(n) = Θ(lg² n)
```

---

### Final Answer for Problem 4.5-4

**Part 1: Regularity condition fails**

**Given:** f(n) = lg n, a = 1, b = 2

**Regularity requires:** f(n/2) ≤ c × f(n) for some c < 1

**We have:**
```
f(n/2) = lg n - 1
f(n) = lg n

Ratio: (lg n - 1)/(lg n) = 1 - 1/(lg n) → 1 as n → ∞
```

**Since the ratio approaches 1, it cannot stay below any c < 1 for all large n.**

**Conclusion:** Regularity condition fails. ✗

---

**Part 2: Case 3 polynomial condition fails**

**Case 3 requires:** f(n) = Ω(n^ε) for some ε > 0

**We have:** f(n) = lg n

**But:** lim(n→∞) (lg n)/(n^ε) = 0 for any ε > 0

**This means:** lg n grows slower than any polynomial n^ε

**Conclusion:** f(n) = lg n is NOT Ω(n^ε) for any ε > 0. ✗

---

**Key insight:** Logarithmic functions grow slower than any polynomial (even n^0.0001), but faster than constants. They fall in a gap where the Master Theorem doesn't apply!

---

## Summary: Master Method

### Quick Reference

**Given:** T(n) = aT(n/b) + f(n)

**Step 1:** Calculate n^(log_b a)

**Step 2:** Compare f(n) with n^(log_b a)

**Step 3:** Apply the appropriate case:

| Case | Condition | Solution |
|------|-----------|----------|
| 1 | f(n) = O(n^(log_b a - ε)) | T(n) = Θ(n^(log_b a)) |
| 2 | f(n) = Θ(n^(log_b a) log^k n) | T(n) = Θ(n^(log_b a) log^(k+1) n) |
| 3 | f(n) = Ω(n^(log_b a + ε)) AND regularity | T(n) = Θ(f(n)) |

---

### Common Pitfalls

**1. Forgetting to check regularity in Case 3**
- Not enough to just have f(n) large
- Must also verify af(n/b) ≤ cf(n)

**2. Confusing logarithmic and polynomial differences**
- n vs n lg n: logarithmic difference (Case 2)
- n vs n²: polynomial difference (Case 1 or 3)

**3. Using wrong logarithm base**
- Always use log_b a (not log₂ a)
- Convert if needed: log_b a = (lg a)/(lg b)

**4. Gaps in the Master Theorem**
- Some recurrences don't fit any case
- Example: T(n) = T(n/2) + lg n
- Need other methods for these

---

**End of Section 4.5 Solutions**
