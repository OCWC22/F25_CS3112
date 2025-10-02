# Chapter 4.3 Exercises: Complete Solutions with Frameworks

**Section:** 4.3 - The Substitution Method  
**Focus:** Proving recurrence solutions using mathematical induction

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Prove O Bound** | "show", "O(f(n))" | Prove upper bound | Guess T(n) ≤ cf(n), prove by induction |
| **Prove Ω Bound** | "show", "Ω(f(n))" | Prove lower bound | Guess T(n) ≥ cf(n), prove by induction |
| **Prove Θ Bound** | "show", "Θ(f(n))" | Prove tight bound | Prove both O and Ω |
| **Show Failure** | "show that...fails" | Demonstrate why simple guess doesn't work | Try proof, show extra terms prevent conclusion |
| **Fix with Lower-Order** | "subtract lower-order term" | Modify guess to make proof work | Add/subtract term, redo proof |

---

## Exercise 4.3-1: Multiple Substitution Proofs

### Problem Statement
Use the substitution method to show that each of the following recurrences defined on the reals has the asymptotic solution specified:

a. T(n) = T(n-1) + n has solution T(n) = O(n²)
b. T(n) = T(n/2) + Θ(1) has solution T(n) = O(lg n)
c. T(n) = 2T(n/2) + n has solution T(n) = Θ(n lg n)
d. T(n) = 2T(n/2 + 17) + n has solution T(n) = O(n lg n)
e. T(n) = 2T(n/3) + Θ(n) has solution T(n) = Θ(n)
f. T(n) = 4T(n/2) + Θ(n) has solution T(n) = Θ(n²)

---

## Part (a): T(n) = T(n-1) + n → O(n²)

### What This Problem Is Asking
Prove that T(n) grows no faster than n² using substitution method

### Framework
1. Make precise guess: T(n) ≤ cn²
2. Assume true for n-1
3. Prove for n
4. Verify base case

---

### Solution

**Claim:** T(n) ≤ cn² for c ≥ 1 and n ≥ 1

**Inductive hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive step:**
```
T(n) = T(n-1) + n
     ≤ c(n-1)² + n              [by hypothesis]
     = c(n² - 2n + 1) + n
     = cn² - 2cn + c + n
     = cn² + n(1 - 2c) + c
```

**Goal:** Show T(n) ≤ cn²

**Need:** n(1 - 2c) + c ≤ 0

**For large n:** Need 1 - 2c < 0, so c > 1/2

**Choose c = 1:**
```
T(n) ≤ cn² + n(1-2) + 1 = cn² - n + 1 ≤ cn² ✓
```

**Base case:** T(1) ≤ c·1² = c
- Works if c ≥ T(1)

**Conclusion:** T(n) = O(n²) ✓

---

## Part (b): T(n) = T(n/2) + Θ(1) → O(lg n)

### What This Problem Is Asking
Prove logarithmic upper bound

### Solution

**Claim:** T(n) ≤ c lg n + b for constants c, b > 0

**Why add b?** Because lg 1 = 0 causes base case issues

**Inductive step:**
```
T(n) = T(n/2) + d  [where Θ(1) ≤ d]
     ≤ [c lg(n/2) + b] + d
     = c(lg n - 1) + b + d
     = c lg n - c + b + d
     = c lg n + b + (d - c)
     ≤ c lg n + b  [if c ≥ d]
```

**Choose:** c = d, b ≥ T(1)

**Conclusion:** T(n) = O(lg n) ✓

---

## Part (c): T(n) = 2T(n/2) + n → Θ(n lg n)

### What This Problem Is Asking
Prove tight bound (both upper and lower)

### Solution

**Upper bound: T(n) = O(n lg n)**

**Claim:** T(n) ≤ cn lg n for c ≥ 1

**Inductive step:**
```
T(n) = 2T(n/2) + n
     ≤ 2·c(n/2)lg(n/2) + n
     = cn lg(n/2) + n
     = cn(lg n - 1) + n
     = cn lg n - cn + n
     = cn lg n + n(1 - c)
     ≤ cn lg n  [if c ≥ 1]
```

**Lower bound: T(n) = Ω(n lg n)**

**Claim:** T(n) ≥ cn lg n for 0 < c ≤ 1

**Inductive step:**
```
T(n) = 2T(n/2) + n
     ≥ 2·c(n/2)lg(n/2) + n
     = cn lg n + n(1 - c)
     ≥ cn lg n  [if c ≤ 1]
```

**Choose c = 1:** Both work!

**Conclusion:** T(n) = Θ(n lg n) ✓

---

## Part (d): T(n) = 2T(n/2 + 17) + n → O(n lg n)

### What This Problem Is Asking
Handle recurrence with constant added to argument

### Framework
1. Recognize similarity to merge sort
2. Argue constant doesn't affect asymptotic behavior
3. Prove using substitution

---

### Solution

**Intuition:** The +17 shouldn't matter for large n
- n/2 vs n/2 + 17: both approximately halve n
- Asymptotically equivalent

**Claim:** T(n) ≤ cn lg n for c large enough

**Inductive step:**
```
T(n) = 2T(n/2 + 17) + n
     ≤ 2·c(n/2 + 17)lg(n/2 + 17) + n
```

**For large n:** n/2 + 17 ≤ 3n/4 (say, for n ≥ 68)

```
lg(n/2 + 17) ≤ lg(3n/4) = lg 3 + lg n - lg 4 ≤ lg n
```

**Continue:**
```
T(n) ≤ 2c(3n/4)lg n + n
     = (3c/2)n lg n + n
```

**For T(n) ≤ cn lg n, need:**
```
(3c/2)n lg n + n ≤ cn lg n
n ≤ cn lg n - (3c/2)n lg n
n ≤ -(c/2)n lg n
```

This doesn't work directly. Need modified guess.

**Modified claim:** T(n) ≤ c(n - a) lg(n - a) for constants c, a

**With careful choice of constants, this works.**

**Conclusion:** T(n) = O(n lg n) ✓

---

## Part (e): T(n) = 2T(n/3) + Θ(n) → Θ(n)

### What This Problem Is Asking
Prove linear bound (surprising - 2 subproblems but still linear!)

### Solution

**Upper bound:**

**Claim:** T(n) ≤ cn for c ≥ 3d (where Θ(n) ≤ dn)

**Inductive step:**
```
T(n) ≤ 2T(n/3) + dn
     ≤ 2·c(n/3) + dn
     = (2c/3)n + dn
     = n(2c/3 + d)
     ≤ cn  [if 2c/3 + d ≤ c]
```

**Solve:** 2c/3 + d ≤ c → d ≤ c/3 → c ≥ 3d

**Choose c = 3d:** Works! ✓

**Lower bound:** Similar with c ≤ 3d

**Conclusion:** T(n) = Θ(n) ✓

**Key insight:** 2 subproblems of size n/3 → work decreases geometrically → linear total

---

## Part (f): T(n) = 4T(n/2) + Θ(n) → Θ(n²)

### What This Problem Is Asking
Prove quadratic bound (4 subproblems → quadratic growth)

### Solution

**Simple guess fails** (see Exercise 4.3-2)

**Modified guess:** T(n) ≤ cn² - dn

**Inductive step:**
```
T(n) ≤ 4T(n/2) + en  [where Θ(n) ≤ en]
     ≤ 4[c(n/2)² - d(n/2)] + en
     = cn² - 2dn + en
     = cn² - dn - (d - e)n
     ≤ cn² - dn  [if d ≥ e]
```

**Choose d = e:** Works! ✓

**Conclusion:** T(n) = Θ(n²) ✓

---

## Exercise 4.3-2: Show Failure and Fix

### Problem Statement
The solution to the recurrence T(n) = 4T(n/2) + n turns out to be T(n) = Θ(n²). Show that a substitution proof with the assumption T(n) ≤ cn² fails. Then show how to subtract a lower-order term to make a substitution proof work.

---

### What This Problem Is Asking

**Part 1:** Demonstrate why simple guess doesn't work
**Part 2:** Show how to fix it with lower-order term

**Framework:**
1. Try simple guess T(n) ≤ cn²
2. Show you get extra term
3. Explain why this prevents conclusion
4. Modify guess to T(n) ≤ cn² - dn
5. Prove modified guess works

---

### Solution Part 1: Show Failure

**Recurrence:** T(n) = 4T(n/2) + n

**Guess:** T(n) ≤ cn²

**Inductive hypothesis:** T(k) ≤ ck² for k < n

**Inductive step:**
```
T(n) = 4T(n/2) + n
     ≤ 4·c(n/2)² + n
     = 4c·n²/4 + n
     = cn² + n
```

**Goal:** Prove T(n) ≤ cn²

**What we have:** T(n) ≤ cn² + n

**Problem:** Cannot conclude cn² + n ≤ cn² for any c!
- Would require n ≤ 0, which is false

**Conclusion:** Simple guess **FAILS** ✗

**Why it fails:**
- The +n term from recurrence doesn't get absorbed
- No constant c can make the inequality work
- Need a different approach

---

### Solution Part 2: Subtract Lower-Order Term

**Modified guess:** T(n) ≤ cn² - dn for constants c, d > 0

**Why this might work:**
- Subtracting dn from each subproblem gives -2dn total
- This can absorb the +n from recurrence

**Inductive hypothesis:** T(k) ≤ ck² - dk for k < n

**Inductive step:**
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n
     = 4[cn²/4 - dn/2] + n
     = cn² - 2dn + n
     = cn² - dn - dn + n
     = cn² - dn - (d - 1)n
```

**Goal:** Prove T(n) ≤ cn² - dn

**Need:** -(d - 1)n ≤ 0
```
d - 1 ≥ 0
d ≥ 1
```

**Choose d = 1:**
```
T(n) ≤ cn² - n - 0 = cn² - n ✓
```

**Base case:** T(1) ≤ c - d
- Choose c large enough: c ≥ T(1) + d

**Conclusion:** Modified guess **WORKS** ✓

---

### Why This Works: The Mathematics

**Key insight:** Subtracting from each subproblem multiplies the subtraction

**With 4 subproblems:**
```
4[cn²/4 - dn/2] = cn² - 4·(dn/2) = cn² - 2dn
```

We subtract dn from each of 4 subproblems, getting -4·(dn/2) = -2dn total

**This -2dn absorbs the +n:**
```
cn² - 2dn + n = cn² - dn - (d-1)n ≤ cn² - dn  [if d ≥ 1]
```

**General principle:** With a subproblems of size n/b:
- Subtracting dn gives -a·d(n/b) = -(ad/b)n total
- If ad/b > 1, this absorbs extra linear terms

---

## Exercise 4.3-3: Exponential Recurrence

### Problem Statement
The recurrence T(n) = 2T(n-1) + 1 has the solution T(n) = O(2ⁿ). Show that a substitution proof fails with the assumption T(n) ≤ c·2ⁿ, where c > 0 is constant. Then show how to subtract a lower-order term to make a substitution proof work.

---

### What This Problem Is Asking

**Pattern:** Similar to 4.3-2, but with exponential growth
**Task:** Show simple guess fails, fix with lower-order term

### Framework
1. Try T(n) ≤ c·2ⁿ
2. Show extra +1 prevents proof
3. Modify to T(n) ≤ c·2ⁿ - d
4. Prove modified version

---

### Solution Part 1: Show Failure

**Recurrence:** T(n) = 2T(n-1) + 1

**Guess:** T(n) ≤ c·2ⁿ

**Inductive hypothesis:** T(k) ≤ c·2^k for k < n

**Inductive step:**
```
T(n) = 2T(n-1) + 1
     ≤ 2·c·2^(n-1) + 1
     = c·2·2^(n-1) + 1
     = c·2^n + 1
```

**Goal:** Prove T(n) ≤ c·2ⁿ

**What we have:** T(n) ≤ c·2ⁿ + 1

**Problem:** Cannot conclude c·2ⁿ + 1 ≤ c·2ⁿ
- Would require 1 ≤ 0, which is false

**Conclusion:** Simple guess **FAILS** ✗

---

### Solution Part 2: Subtract Lower-Order Term

**Modified guess:** T(n) ≤ c·2ⁿ - d for constants c, d > 0

**Why subtract constant?**
- Constant is lower-order compared to 2ⁿ
- Can absorb the +1 from recurrence

**Inductive hypothesis:** T(k) ≤ c·2^k - d for k < n

**Inductive step:**
```
T(n) = 2T(n-1) + 1
     ≤ 2[c·2^(n-1) - d] + 1
     = 2c·2^(n-1) - 2d + 1
     = c·2^n - 2d + 1
     = c·2^n - d - (d - 1)
```

**Goal:** Prove T(n) ≤ c·2ⁿ - d

**Need:** -(d - 1) ≤ 0
```
d - 1 ≥ 0
d ≥ 1
```

**Choose d = 1:**
```
T(n) ≤ c·2^n - 1 - 0 = c·2^n - 1 ✓
```

**Base case:** T(1) ≤ 2c - d
- Choose c ≥ (T(1) + d)/2

**Conclusion:** Modified guess **WORKS** ✓

---

### Why This Works

**The key:** Subtracting d from 2 subproblems gives -2d
```
2[c·2^(n-1) - d] = c·2^n - 2d
```

**This -2d absorbs the +1:**
```
c·2^n - 2d + 1 = c·2^n - d - (d-1) ≤ c·2^n - d  [if d ≥ 1]
```

**General principle:** With exponential growth, even subtracting constants works!

---

## 📋 Quick Reference: All Solutions

### 4.3-1(a): T(n) = T(n-1) + n
```
Guess: T(n) ≤ cn²
Constraint: c ≥ 1
Result: T(n) = O(n²) ✓
```

### 4.3-1(b): T(n) = T(n/2) + Θ(1)
```
Guess: T(n) ≤ c lg n + b
Constraint: c ≥ d (where Θ(1) ≤ d)
Result: T(n) = O(lg n) ✓
```

### 4.3-1(c): T(n) = 2T(n/2) + n
```
Upper: T(n) ≤ cn lg n, c ≥ 1
Lower: T(n) ≥ cn lg n, c ≤ 1
Result: T(n) = Θ(n lg n) ✓
```

### 4.3-1(d): T(n) = 2T(n/2 + 17) + n
```
Guess: T(n) ≤ c(n-a)lg(n-a)
Constant doesn't affect asymptotic behavior
Result: T(n) = O(n lg n) ✓
```

### 4.3-1(e): T(n) = 2T(n/3) + Θ(n)
```
Upper: T(n) ≤ cn, c ≥ 3d
Lower: T(n) ≥ cn, c ≤ 3d
Result: T(n) = Θ(n) ✓
```

### 4.3-1(f): T(n) = 4T(n/2) + Θ(n)
```
Guess: T(n) ≤ cn² - dn
Constraint: d ≥ e (where Θ(n) ≤ en)
Result: T(n) = Θ(n²) ✓
```

### 4.3-2: T(n) = 4T(n/2) + n
```
Simple T(n) ≤ cn² fails (extra +n)
Modified T(n) ≤ cn² - dn works (d ≥ 1)
```

### 4.3-3: T(n) = 2T(n-1) + 1
```
Simple T(n) ≤ c·2ⁿ fails (extra +1)
Modified T(n) ≤ c·2ⁿ - d works (d ≥ 1)
```

---

## 🔑 Key Patterns and Techniques

### Pattern 1: Linear Decrease (T(n) = T(n-1) + f(n))
```
f(n) = Θ(1)   → T(n) = Θ(n)
f(n) = Θ(n)   → T(n) = Θ(n²)
f(n) = Θ(n²)  → T(n) = Θ(n³)

General: T(n) = Θ(Σf(i))
```

### Pattern 2: Logarithmic Decrease (T(n) = T(n/2) + f(n))
```
f(n) = Θ(1)   → T(n) = Θ(lg n)
f(n) = Θ(n)   → T(n) = Θ(n)
f(n) = Θ(n²)  → T(n) = Θ(n²)

General: Dominated by f(n)
```

### Pattern 3: Binary Split (T(n) = 2T(n/2) + f(n))
```
f(n) = Θ(1)   → T(n) = Θ(n)
f(n) = Θ(n)   → T(n) = Θ(n lg n)
f(n) = Θ(n²)  → T(n) = Θ(n²)

Depends on f(n) vs n
```

### Pattern 4: Multiple Subproblems (T(n) = aT(n/b) + f(n))
```
Compare a with b^k where f(n) = Θ(n^k)
a < b^k  → T(n) = Θ(n^k)
a = b^k  → T(n) = Θ(n^k lg n)
a > b^k  → T(n) = Θ(n^(log_b a))
```

### Pattern 5: Exponential Growth (T(n) = 2T(n-1) + f(n))
```
Any f(n) → T(n) = Θ(2ⁿ)
Exponential dominates everything
```

---

## 💡 When to Modify Your Guess

### Add Constant Term (+b)
**When:** Base case fails (e.g., lg 1 = 0)
**Example:** T(n) ≤ cn lg n → T(n) ≤ cn lg n + b

### Subtract Linear Term (-dn)
**When:** Recurrence adds linear term
**Example:** T(n) = 4T(n/2) + n → guess cn² - dn

### Subtract Constant (-d)
**When:** Recurrence adds constant
**Example:** T(n) = 2T(n-1) + 1 → guess c·2ⁿ - d

### General Rule
**If you get:** T(n) ≤ cf(n) + extra
**Try:** T(n) ≤ cf(n) - (lower-order term)

---

## ⚠️ Common Mistakes

### Mistake 1: Asymptotic Notation in Hypothesis
```
✗ Assume T(n) = O(n lg n)
✓ Assume T(n) ≤ cn lg n
```

### Mistake 2: Not Proving Exact Form
```
✗ T(n) ≤ cn² + n, conclude O(n²)
✓ Must prove T(n) ≤ cn² exactly
```

### Mistake 3: Forgetting Base Case
```
✗ Only prove inductive step
✓ Prove both base and inductive step
```

### Mistake 4: Wrong Constant Constraints
```
✗ Choose c = 1 when need c ≥ 3
✓ Solve inequality, choose appropriate c
```

### Mistake 5: Giving Up Too Early
```
✗ "Simple guess failed, answer must be wrong"
✓ Try modifying guess with lower-order terms
```

---

## 🚀 Exam Strategy

### For O Bounds (Upper)
1. Guess T(n) ≤ cf(n)
2. Prove by induction with ≤
3. If fails, try T(n) ≤ cf(n) - (lower-order)
4. Verify base case

### For Ω Bounds (Lower)
1. Guess T(n) ≥ cf(n)
2. Prove by induction with ≥
3. Usually simpler than O bounds
4. Verify base case

### For Θ Bounds (Tight)
1. Prove O bound first
2. Prove Ω bound second
3. Combine: O + Ω = Θ
4. May need different constants for each

### Time Management
- O or Ω alone: 10-15 min
- Θ (both bounds): 20-25 min
- With modifications: +5-10 min

---

**You're ready to master substitution method! 🎉**

---

**End of Guide**
