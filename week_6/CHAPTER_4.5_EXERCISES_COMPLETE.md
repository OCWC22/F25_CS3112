# Chapter 4.5 Exercises: Complete Solutions with Frameworks

**Section:** 4.5 - The Master Method  
**Focus:** Applying the cookbook method to solve recurrences

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Apply Master Method** | "use master method", "tight bounds" | Identify case, apply formula | Calculate n^(log_b a), compare, apply case |
| **Design Algorithm** | "asymptotically faster", "what is largest a" | Find constraint on parameters | Set up inequality, solve for parameter |
| **Prove with Master** | "show that", "prove" | Use Master Method as justification | Apply appropriate case, state conclusion |
| **Show Failure** | "does not hold", "argue that" | Demonstrate why condition fails | Show inequality or condition violated |

---

## Exercise 4.5-1: Master Method Applications

### Problem Statement
Use the master method to give tight asymptotic bounds for the following recurrences.

a. T(n) = 2T(n/4) + 1
b. T(n) = 2T(n/4) + √n
c. T(n) = 2T(n/4) + n
d. T(n) = 2T(n/4) + n²

---

## Part (a): T(n) = 2T(n/4) + 1

### What This Problem Is Asking

**Pattern:** Two subproblems, divide by 4, constant work
**Task:** Apply Master Method to find solution

### Framework
1. Identify a, b, f(n)
2. Calculate n^(log_b a)
3. Compare f(n) with watershed
4. Apply appropriate case

---

### Solution

**Step 1: Identify parameters**
```
T(n) = 2T(n/4) + 1

a = 2
b = 4
f(n) = 1
```

**Step 2: Calculate watershed**
```
n^(log_b a) = n^(log₄ 2)

log₄ 2 = (lg 2)/(lg 4) = 1/2 = 0.5

n^(log₄ 2) = n^0.5 = √n
```

**Step 3: Compare**
```
f(n) = 1
n^(log_b a) = √n

1 << √n (polynomially smaller)
```

**Is it polynomially smaller?**
```
f(n) = 1 = O(n^(0.5-ε)) for ε = 0.25

1 = O(n^0.25) ✓ (constant is smaller than any polynomial)
```

**Step 4: Apply Case 1**
```
f(n) = O(n^(log_b a - ε)) with ε = 0.25

Solution: T(n) = Θ(n^(log_b a))
                = Θ(√n) ✓
```

---

### Answer

**T(n) = Θ(√n)**

**Explanation:** Constant work per level, but √n leaves dominate.

---

## Part (b): T(n) = 2T(n/4) + √n

### What This Problem Is Asking

**Pattern:** Same structure as (a), but f(n) = √n
**Task:** Recognize this equals watershed function

### Solution

**Step 1: Parameters**
```
a = 2, b = 4, f(n) = √n
```

**Step 2: Watershed**
```
n^(log₄ 2) = √n  (from part a)
```

**Step 3: Compare**
```
f(n) = √n
n^(log_b a) = √n

They're equal!
```

**Step 4: Check Case 2**
```
f(n) = √n = √n × (lg n)^0

So k = 0
```

**Step 5: Apply Case 2**
```
T(n) = Θ(n^(log_b a) × (lg n)^(k+1))
     = Θ(√n × lg n) ✓
```

---

### Answer

**T(n) = Θ(√n lg n)**

**Explanation:** All levels contribute equally, multiply by height.

---

## Part (c): T(n) = 2T(n/4) + n

### What This Problem Is Asking

**Pattern:** Linear work, compare with √n watershed
**Task:** Recognize f(n) is polynomially larger

### Solution

**Step 1: Parameters**
```
a = 2, b = 4, f(n) = n
```

**Step 2: Watershed**
```
n^(log₄ 2) = √n
```

**Step 3: Compare**
```
f(n) = n = n^1.0
n^(log_b a) = √n = n^0.5

n > √n (polynomially larger)
```

**Is it polynomially larger?**
```
f(n) = n = Ω(n^(0.5+ε)) for ε = 0.5

n = Ω(n^1.0) ✓
```

**Step 4: Check regularity**
```
af(n/b) = 2 × (n/4) = n/2

Need: n/2 ≤ c × n for some c < 1

Simplify: 1/2 ≤ c

Choose c = 3/4: 1/2 ≤ 3/4 < 1 ✓
```

**Step 5: Apply Case 3**
```
f(n) = Ω(n^(log_b a + ε)) with ε = 0.5 ✓
Regularity holds ✓

Solution: T(n) = Θ(f(n)) = Θ(n) ✓
```

---

### Answer

**T(n) = Θ(n)**

**Explanation:** Root dominates, linear work at top level.

---

## Part (d): T(n) = 2T(n/4) + n²

### What This Problem Is Asking

**Pattern:** Quadratic work, much larger than √n
**Task:** Apply Case 3 with regularity check

### Solution

**Step 1: Parameters**
```
a = 2, b = 4, f(n) = n²
```

**Step 2: Watershed**
```
n^(log₄ 2) = √n
```

**Step 3: Compare**
```
f(n) = n² = n^2.0
n^(log_b a) = √n = n^0.5

n² >> √n (much larger!)
```

**Is it polynomially larger?**
```
f(n) = n² = Ω(n^(0.5+ε)) for ε = 1.5

n² = Ω(n^2.0) ✓
```

**Step 4: Check regularity**
```
af(n/b) = 2 × (n/4)² = 2 × n²/16 = n²/8

Need: n²/8 ≤ c × n² for some c < 1

Simplify: 1/8 ≤ c

Choose c = 1/4: 1/8 ≤ 1/4 < 1 ✓
```

**Step 5: Apply Case 3**
```
f(n) = Ω(n^(log_b a + ε)) with ε = 1.5 ✓
Regularity holds ✓

Solution: T(n) = Θ(f(n)) = Θ(n²) ✓
```

---

### Answer

**T(n) = Θ(n²)**

**Explanation:** Root dominates heavily, quadratic work at top.

---

### Summary of 4.5-1

| Part | Recurrence | Watershed | Comparison | Case | Solution |
|------|------------|-----------|------------|------|----------|
| (a) | 2T(n/4) + 1 | √n | 1 << √n | 1 | Θ(√n) |
| (b) | 2T(n/4) + √n | √n | √n = √n | 2 | Θ(√n lg n) |
| (c) | 2T(n/4) + n | √n | n >> √n | 3 | Θ(n) |
| (d) | 2T(n/4) + n² | √n | n² >> √n | 3 | Θ(n²) |

**Pattern:** Same a and b, different f(n) → different cases!

---

## Exercise 4.5-2: Professor Caesar's Matrix Multiplication

### Problem Statement
Professor Caesar wants to develop a matrix-multiplication algorithm that is asymptotically faster than Strassen's algorithm. His algorithm will use the divide-and-conquer method, dividing each matrix into n/4 × n/4 submatrices, and the divide and combine steps together will take Θ(n²) time. Suppose that the professor's algorithm creates a recursive subproblems of size n/4. What is the largest integer value of a for which his algorithm could possibly run asymptotically faster than Strassen's?

---

### What This Problem Is Asking

**Context:** Design constraint problem
**Task:** Find maximum a such that T(n) < Strassen's Θ(n^2.807)
**Framework:** Set up inequality, solve for a

---

### Solution

**Step 1: Understand Strassen**
```
Strassen: T(n) = 7T(n/2) + Θ(n²)
Solution: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

Goal: Beat this!
```

**Step 2: Caesar's recurrence**
```
T(n) = aT(n/4) + Θ(n²)

Parameters:
a = ? (what we're solving for)
b = 4
f(n) = Θ(n²)
```

**Step 3: Calculate watershed**
```
n^(log_b a) = n^(log₄ a)
```

**Step 4: Determine solution based on a**

**Case 1 (a > 16):** n² < n^(log₄ a)
```
T(n) = Θ(n^(log₄ a))
```

**Case 2 (a = 16):** n² = n^(log₄ a)
```
log₄ a = 2
a = 16
T(n) = Θ(n² lg n)
```

**Case 3 (a < 16):** n² > n^(log₄ a)
```
T(n) = Θ(n²)
```

**Step 5: Compare with Strassen**

**For Case 3 (a < 16):**
```
T(n) = Θ(n²) < Θ(n^2.807) ✓
Beats Strassen!
```

**For Case 2 (a = 16):**
```
T(n) = Θ(n² lg n)

Is n² lg n < n^2.807?
lg n = o(n^0.807)
So n² lg n = o(n^2.807) ✓
Beats Strassen!
```

**For Case 1 (a > 16):**
```
T(n) = Θ(n^(log₄ a))

Need: log₄ a < 2.807
```

**Step 6: Solve inequality**
```
log₄ a < 2.807
a < 4^2.807
a < (2²)^2.807
a < 2^(2×2.807)
a < 2^5.614
```

**Calculate 2^5.614:**
```
2^5 = 32
2^6 = 64
2^5.614 ≈ 48.85
```

**Step 7: Find largest integer**
```
a < 48.85
Largest integer: a = 48
```

**Step 8: Verify**

**With a = 48:**
```
log₄ 48 = (lg 48)/(lg 4)
        = (lg 48)/2
        ≈ 5.585/2
        ≈ 2.793 < 2.807 ✓
```

**With a = 49:**
```
log₄ 49 = (lg 49)/(lg 4)
        = (lg 7²)/2
        = (2 lg 7)/2
        = lg 7
        ≈ 2.807 (not faster!) ✗
```

---

### Answer

**The largest integer value of a is 48.**

**Explanation:**
- With a ≤ 48: T(n) = Θ(n^(log₄ a)) where log₄ a < 2.807
- With a = 49: T(n) = Θ(n^2.807) (same as Strassen, not faster)
- With a ≥ 50: T(n) = Θ(n^(log₄ a)) where log₄ a > 2.807 (slower)

---

## Exercise 4.5-3: Binary Search

### Problem Statement
Use the master method to show that the solution to the binary-search recurrence T(n) = T(n/2) + Θ(1) is T(n) = Θ(lg n).

---

### What This Problem Is Asking

**Context:** Classic algorithm analysis
**Task:** Apply Master Method to binary search
**Framework:** Recognize Case 2 with k=0

---

### Solution

**Step 1: Identify parameters**
```
T(n) = T(n/2) + Θ(1)

a = 1 (one subproblem)
b = 2 (halve the size)
f(n) = Θ(1) (constant work)
```

**Step 2: Calculate watershed**
```
n^(log_b a) = n^(log₂ 1)

log₂ 1 = 0 (because 2^0 = 1)

n^(log₂ 1) = n^0 = 1
```

**Step 3: Compare**
```
f(n) = Θ(1)
n^(log_b a) = 1

They're both constant!
f(n) = Θ(1) = Θ(1 × (lg n)^0)

So k = 0
```

**Step 4: Apply Case 2**
```
f(n) = Θ(n^(log_b a) × (lg n)^k) with k = 0

Solution: T(n) = Θ(n^(log_b a) × (lg n)^(k+1))
                = Θ(1 × (lg n)^1)
                = Θ(lg n) ✓
```

---

### Answer

**T(n) = Θ(lg n)**

**Explanation:** Binary search halves the search space each time, taking logarithmic time. Each level does constant work, and there are lg n levels.

---

## Exercise 4.5-4: Logarithmic Function Failure

### Problem Statement
Consider the function f(n) = lg n. Argue that although f(n/2) < f(n), the regularity condition af(n/b) ≤ cf(n) with a = 1 and b = 2 does not hold for any constant c < 1. Argue further that for any ε > 0, the condition in case 3 that f(n) = Ω(n^(log_b a + ε)) does not hold.

---

### What This Problem Is Asking

**Context:** Understanding Master Method limitations
**Task:** Show why lg n doesn't satisfy Case 3 conditions
**Framework:** Prove both conditions fail

---

### Solution Part 1: Show f(n/2) < f(n)

**Calculate:**
```
f(n) = lg n
f(n/2) = lg(n/2) = lg n - lg 2 = lg n - 1

Compare: lg n - 1 < lg n ✓
```

**Yes, f(n/2) < f(n).**

---

### Solution Part 2: Show Regularity Fails

**Regularity condition:** af(n/b) ≤ cf(n) for some c < 1

**With a=1, b=2:**
```
1 × f(n/2) ≤ c × f(n)
f(n/2) ≤ c × f(n)
lg(n/2) ≤ c × lg n
lg n - 1 ≤ c × lg n
```

**Rearrange:**
```
lg n - c × lg n ≤ 1
lg n(1 - c) ≤ 1
lg n ≤ 1/(1-c)
```

**Problem:**
- lg n grows without bound as n → ∞
- 1/(1-c) is a constant (for fixed c)
- For large enough n: lg n > 1/(1-c)

**Therefore:** The inequality fails for large n!

**Alternative proof using ratio:**
```
f(n/2)/f(n) = (lg n - 1)/(lg n)
            = 1 - 1/(lg n)
            → 1 as n → ∞
```

**For any c < 1:** Eventually 1 - 1/(lg n) > c

**Conclusion:** Regularity condition does NOT hold for any c < 1. ✗

---

### Solution Part 3: Show Polynomial Condition Fails

**Case 3 requires:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0

**With log_b a = 0:**
```
f(n) = Ω(n^(0+ε)) = Ω(n^ε)
```

**We have:** f(n) = lg n

**Question:** Is lg n = Ω(n^ε) for any ε > 0?

**Answer:** NO!

**Proof:**
```
For any ε > 0:
lim(n→∞) (lg n)/(n^ε) = 0

This means lg n = o(n^ε)
Therefore lg n ≠ Ω(n^ε)
```

**Why?** Logarithms grow slower than ANY polynomial, even n^0.0001!

**Conclusion:** f(n) = lg n is NOT Ω(n^ε) for any ε > 0. ✗

---

### Answer

**Part 1:** f(n/2) < f(n) ✓ (lg n - 1 < lg n)

**Part 2:** Regularity fails ✗
- Ratio (lg n - 1)/(lg n) → 1 as n → ∞
- Cannot stay below any c < 1 for all large n

**Part 3:** Polynomial condition fails ✗
- lg n = o(n^ε) for any ε > 0
- Logarithms grow slower than any polynomial

**Implication:** T(n) = T(n/2) + lg n falls in a gap where Master Method doesn't apply!

**Actual solution (by other methods):** T(n) = Θ(lg² n)

---

## Exercise 4.5-5: Oscillating Function

### Problem Statement
Show that for suitable constants a, b, and ε, the function f(n) = 2^(⌈lg n⌉) satisfies all the conditions in case 3 of the master theorem except the regularity condition.

---

### What This Problem Is Asking

**Context:** Example of regularity failure
**Task:** Show f(n) is large but not regular
**Framework:** Verify polynomial condition, show regularity fails

---

### Solution

**Step 1: Understand f(n)**
```
f(n) = 2^(⌈lg n⌉)

This rounds lg n up to nearest integer, then exponentiates.

Examples:
n=2: f(2) = 2^⌈1⌉ = 2^1 = 2
n=3: f(3) = 2^⌈1.585⌉ = 2^2 = 4
n=4: f(4) = 2^⌈2⌉ = 2^2 = 4
n=5: f(5) = 2^⌈2.322⌉ = 2^3 = 8
```

**Key property:** f(n) jumps at powers of 2, stays constant between them.

---

**Step 2: Choose parameters**
```
Let a = 2, b = 2
Then n^(log_b a) = n^(log₂ 2) = n
```

**Step 3: Show polynomial condition holds**

**Need:** f(n) = Ω(n^(1+ε)) for some ε > 0

**Observe:**
```
For n = 2^k:
f(n) = 2^⌈k⌉ = 2^k = n

For 2^k < n < 2^(k+1):
f(n) = 2^(k+1) ≥ n
```

**So:** f(n) ≥ n for all n

**Therefore:** f(n) = Ω(n^(1+ε)) for small ε (say ε = 0.1)

**Polynomial condition holds!** ✓

---

**Step 4: Show regularity fails**

**Regularity requires:** af(n/b) ≤ cf(n) for some c < 1

**With a=2, b=2:**
```
2f(n/2) ≤ c × f(n)
```

**Test at n = 2^k + 1:**
```
f(n) = f(2^k + 1) = 2^⌈lg(2^k + 1)⌉ = 2^(k+1)

f(n/2) = f((2^k + 1)/2) ≈ f(2^(k-1))
       = 2^k

af(n/b) = 2 × 2^k = 2^(k+1)
f(n) = 2^(k+1)

Ratio: 2^(k+1) / 2^(k+1) = 1
```

**The ratio equals 1, not less than some c < 1!**

**Regularity fails!** ✗

---

### Answer

**Function:** f(n) = 2^(⌈lg n⌉)

**With a=2, b=2:**
- **Watershed:** n^(log₂ 2) = n
- **Polynomial condition:** f(n) ≥ n = Ω(n^(1+ε)) ✓
- **Regularity condition:** 2f(n/2) = f(n) at certain points (ratio = 1, not < 1) ✗

**Explanation:** The ceiling function causes f(n) to oscillate, preventing the regularity condition from holding even though f(n) is large.

**Implication:** Master Theorem Case 3 requires BOTH conditions. This example shows why regularity is necessary!

---

## 📋 Quick Reference: All Exercises

### 4.5-1: Five Recurrences with Same a, b

| Part | f(n) | vs √n | Case | Solution |
|------|------|-------|------|----------|
| (a) | 1 | << | 1 | Θ(√n) |
| (b) | √n | = | 2 | Θ(√n lg n) |
| (c) | n | >> | 3 | Θ(n) |
| (d) | n² | >> | 3 | Θ(n²) |

**Pattern:** Different f(n) → different cases → different solutions!

---

### 4.5-2: Caesar's Algorithm
```
Goal: Beat Strassen's Θ(n^2.807)
Recurrence: T(n) = aT(n/4) + Θ(n²)
Constraint: n^(log₄ a) < n^2.807
Solution: a ≤ 48
```

---

### 4.5-3: Binary Search
```
Recurrence: T(n) = T(n/2) + Θ(1)
Watershed: n^(log₂ 1) = 1
Case: 2 (k=0)
Solution: T(n) = Θ(lg n)
```

---

### 4.5-4: Logarithm Failures
```
Function: f(n) = lg n
Regularity: Fails (ratio → 1)
Polynomial: Fails (lg n = o(n^ε))
Conclusion: Falls in gap
```

---

### 4.5-5: Oscillating Function
```
Function: f(n) = 2^(⌈lg n⌉)
Polynomial: Holds (f(n) ≥ n)
Regularity: Fails (ratio = 1 at points)
Conclusion: Shows why regularity needed
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Logarithm Base
```
✗ Always using log₂
✓ Use log_b where b is from recurrence
```

### Mistake 2: Forgetting Regularity
```
✗ "f(n) > n^(log_b a), so Case 3"
✓ Must also check af(n/b) ≤ cf(n)
```

### Mistake 3: Logarithmic vs Polynomial
```
✗ "n lg n > n, so Case 3"
✓ Only logarithmically larger, Case 2!
```

### Mistake 4: Applying to Wrong Form
```
✗ Using Master Method on T(n) = T(n-1) + n
✓ Only for T(n) = aT(n/b) + f(n)
```

---

## 🚀 Exam Strategy

### For Application Problems (4.5-1)
- [ ] Calculate n^(log_b a) first
- [ ] Compare with f(n) carefully
- [ ] Check polynomial separation
- [ ] If Case 3, verify regularity
- [ ] State answer clearly

### For Design Problems (4.5-2)
- [ ] Set up inequality
- [ ] Solve for parameter
- [ ] Verify boundary cases
- [ ] State largest/smallest value

### For Proof Problems (4.5-3)
- [ ] Apply Master Method
- [ ] Show all steps
- [ ] State conclusion clearly

### For Failure Problems (4.5-4, 4.5-5)
- [ ] Show what fails
- [ ] Explain why it fails
- [ ] Give mathematical justification

### Time Management
- Simple application: 3-5 min
- With regularity: 5-7 min
- Design problem: 8-12 min
- Proof/failure: 10-15 min

---

**You're ready to master the Master Method! 🎉**

---

**End of Guide**
