# Homework Solutions: Section 4.3 - The Substitution Method

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 4.3 (Solving Recurrences - Substitution Method)  
**Date:** 2025-09-29

---

## Background: What is the Substitution Method?

### The Problem We're Solving

**What is a recurrence?**
A recurrence is an equation that defines a function in terms of itself on smaller inputs.

**Example:**
```
T(n) = 2T(n/2) + n
```
This says: "The time for problem size n equals the time for two problems of size n/2, plus n extra work."

**The question:** What is T(n) in closed form (without recursion)?

---

### What is the Substitution Method?

**The Substitution Method is a two-step process:**

**Step 1: GUESS** the form of the solution
- Use intuition, recursion trees, or experience
- Example guess: "I think T(n) = O(n²)"

**Step 2: PROVE** your guess using mathematical induction
- Show it works for base case
- Show if it works for smaller n, it works for n
- Use algebra to verify

**Why "substitution"?**
- We substitute our guessed solution into the recurrence
- Then verify it satisfies the recurrence

---

### Mathematical Induction Refresher

**What is induction?**
A proof technique with three parts:

**1. Base Case:**
- Show the statement is true for the smallest value (usually n=1 or n=0)

**2. Inductive Hypothesis:**
- ASSUME the statement is true for some value k (or for all values up to k)

**3. Inductive Step:**
- PROVE the statement is true for k+1 (or n) using the hypothesis

**Analogy:**
- Like dominoes: if the first falls (base case), and each falling domino knocks down the next (inductive step), then all dominoes fall

---

### Asymptotic Notation Review

**O-notation (Big-O):**
- T(n) = O(f(n)) means T(n) grows no faster than f(n)
- Formally: ∃ c, n₀ such that T(n) ≤ c·f(n) for all n ≥ n₀
- Example: T(n) = 3n² + 5n = O(n²)

**Ω-notation (Big-Omega):**
- T(n) = Ω(f(n)) means T(n) grows at least as fast as f(n)
- Formally: ∃ c, n₀ such that T(n) ≥ c·f(n) for all n ≥ n₀
- Example: T(n) = 3n² + 5n = Ω(n²)

**Θ-notation (Big-Theta):**
- T(n) = Θ(f(n)) means T(n) grows exactly like f(n)
- Formally: T(n) = O(f(n)) AND T(n) = Ω(f(n))
- Example: T(n) = 3n² + 5n = Θ(n²)

**Key insight:**
- O is an upper bound (≤)
- Ω is a lower bound (≥)
- Θ is a tight bound (=)

---

## Problem 4.3-1: Substitution Method Proofs

### Problem Statement
Use the substitution method to show that each of the following recurrences defined on the reals has the asymptotic solution specified:

a. T(n) = T(n-1) + n has solution T(n) = O(n²)
b. T(n) = T(n/2) + Θ(1) has solution T(n) = O(lg n)
c. T(n) = 2T(n/2) + n has solution T(n) = Θ(n lg n)
e. T(n) = 2T(n/3) + Θ(n) has solution T(n) = Θ(n)
f. T(n) = 4T(n/2) + Θ(n) has solution T(n) = Θ(n²)

---

## Problem 4.3-1(a): T(n) = T(n-1) + n, prove T(n) = O(n²)

### Step 1: Understand the Recurrence

**What does T(n) = T(n-1) + n mean?**
- To solve a problem of size n, we:
  - Solve a problem of size n-1
  - Do n additional work
- This is a linear recurrence (decreases by 1 each time)

**Intuition:**
```
T(n) = T(n-1) + n
     = [T(n-2) + (n-1)] + n
     = T(n-2) + (n-1) + n
     = [T(n-3) + (n-2)] + (n-1) + n
     = ...
     = T(1) + 2 + 3 + ... + (n-1) + n
     = T(1) + (sum of 1 to n)
     = T(1) + n(n+1)/2
     = Θ(n²)
```

So we expect T(n) = O(n²).

---

### Step 2: Make the Guess Precise

**Claim:** T(n) ≤ cn² for some constant c > 0 and all n ≥ n₀

**What we need to prove:**
- Find constants c and n₀
- Show T(n) ≤ cn² for all n ≥ n₀

---

### Step 3: Set Up the Induction

**Base Case:** We need to verify for some small value(s)

**Inductive Hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive Step:** Prove T(n) ≤ cn²

---

### Step 4: The Inductive Step

**Start with the recurrence:**
```
T(n) = T(n-1) + n
```

**Apply the inductive hypothesis to T(n-1):**
Since n-1 < n, we can assume T(n-1) ≤ c(n-1)²

**Substitute:**
```
T(n) = T(n-1) + n
     ≤ c(n-1)² + n          [by inductive hypothesis]
```

**Expand (n-1)²:**
```
(n-1)² = n² - 2n + 1
```

**Continue:**
```
T(n) ≤ c(n² - 2n + 1) + n
     = cn² - 2cn + c + n
     = cn² + n(1 - 2c) + c
```

**Goal:** We want T(n) ≤ cn²

**For this to work, we need:**
```
cn² + n(1 - 2c) + c ≤ cn²
```

**Simplify:**
```
n(1 - 2c) + c ≤ 0
```

**This is true if:**
- 1 - 2c < 0 (so the n term is negative)
- Which means c > 1/2

**Choose c = 1:**
```
n(1 - 2) + 1 = -n + 1 ≤ 0  for n ≥ 1
```

Perfect! So c = 1 works for n ≥ 1.

---

### Step 5: Verify the Base Case

**Base case: n = 1**

**Assume:** T(1) = some constant (given by the problem)

**We need:** T(1) ≤ c·1² = c

**Since c = 1, we need:** T(1) ≤ 1

**If T(1) > 1:** We can choose a larger c, say c = T(1)

**Conclusion:** The base case holds for appropriate choice of c.

---

### Step 6: Complete the Proof

**Summary:**

**Claim:** T(n) = O(n²)

**Proof by induction:**

**Base case:** T(1) ≤ c·1² for c ≥ T(1)

**Inductive hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive step:**
```
T(n) = T(n-1) + n
     ≤ c(n-1)² + n
     = cn² - 2cn + c + n
     = cn² + n(1-2c) + c
     ≤ cn²  [for c ≥ 1 and n ≥ 1]
```

**Therefore:** T(n) ≤ cn² for all n ≥ 1, which means T(n) = O(n²). ∎

---

## Problem 4.3-1(b): T(n) = T(n/2) + Θ(1), prove T(n) = O(lg n)

### Step 1: Understand the Recurrence

**What does T(n) = T(n/2) + Θ(1) mean?**
- To solve a problem of size n, we:
  - Solve a problem of size n/2
  - Do constant additional work
- This is a logarithmic recurrence (halves each time)

**What is Θ(1)?**
- Θ(1) means "constant time"
- There exist constants c₁, c₂ such that c₁ ≤ Θ(1) ≤ c₂
- For our proof, we'll use: Θ(1) ≤ d for some constant d

**Intuition:**
```
T(n) = T(n/2) + d
     = [T(n/4) + d] + d
     = T(n/4) + 2d
     = [T(n/8) + d] + 2d
     = T(n/8) + 3d
     = ...
```

**How many times can we halve n?**
- n → n/2 → n/4 → ... → 1
- This takes log₂ n steps
- So T(n) ≈ d·log₂ n = Θ(lg n)

**Note:** "lg n" means log₂ n (logarithm base 2)

---

### Step 2: Make the Guess Precise

**Claim:** T(n) ≤ c lg n for some constants c > 0 and all n ≥ n₀

**What is lg n?**
- lg n = log₂ n (logarithm base 2)
- lg 1 = 0, lg 2 = 1, lg 4 = 2, lg 8 = 3, etc.
- lg n is the number of times you can divide n by 2 until you reach 1

---

### Step 3: Set Up the Induction

**Base Case:** n = 1 (or n = 2)

**Inductive Hypothesis:** Assume T(k) ≤ c lg k for all k < n

**Inductive Step:** Prove T(n) ≤ c lg n

---

### Step 4: The Inductive Step

**Start with the recurrence:**
```
T(n) = T(n/2) + Θ(1)
```

**Since Θ(1) ≤ d for some constant d:**
```
T(n) ≤ T(n/2) + d
```

**Apply the inductive hypothesis to T(n/2):**
Since n/2 < n, we can assume T(n/2) ≤ c lg(n/2)

**Substitute:**
```
T(n) ≤ c lg(n/2) + d
```

**Simplify lg(n/2):**
```
lg(n/2) = lg n - lg 2 = lg n - 1
```

**Why?** Because log(a/b) = log a - log b, and lg 2 = 1

**Continue:**
```
T(n) ≤ c(lg n - 1) + d
     = c lg n - c + d
```

**Goal:** We want T(n) ≤ c lg n

**For this to work, we need:**
```
c lg n - c + d ≤ c lg n
```

**Simplify:**
```
-c + d ≤ 0
d ≤ c
```

**So we need:** c ≥ d

**Choose:** c = d (or any c ≥ d)

---

### Step 5: Verify the Base Case

**Problem:** lg 1 = 0, so T(1) ≤ c·0 = 0 doesn't work!

**Solution:** Start induction at a larger base case

**Try n = 2:**
```
T(2) ≤ c lg 2 = c·1 = c
```

This works if T(2) ≤ c, which we can ensure by choosing c large enough.

**Alternative:** Modify the guess to T(n) ≤ c lg n + b for some constant b

---

### Step 6: Complete the Proof (with modified guess)

**Better claim:** T(n) ≤ c lg n + b for constants c, b > 0

**Inductive step:**
```
T(n) = T(n/2) + d
     ≤ [c lg(n/2) + b] + d
     = c(lg n - 1) + b + d
     = c lg n - c + b + d
     = c lg n + b + (d - c)
     ≤ c lg n + b  [if c ≥ d]
```

**Base case:** n = 1
```
T(1) ≤ c lg 1 + b = 0 + b = b
```
This works if T(1) ≤ b, which we can ensure by choosing b ≥ T(1).

**Conclusion:** T(n) ≤ c lg n + b = O(lg n) ∎

**Note:** The constant b doesn't affect the asymptotic notation, so T(n) = O(lg n).

---

## Problem 4.3-1(c): T(n) = 2T(n/2) + n, prove T(n) = Θ(n lg n)

### Step 1: Understand the Recurrence

**What does T(n) = 2T(n/2) + n mean?**
- Solve TWO subproblems of size n/2
- Do n additional work to combine
- This is the recurrence for merge sort!

**Intuition (recursion tree):**
```
Level 0: 1 problem of size n, cost n
Level 1: 2 problems of size n/2, total cost 2·(n/2) = n
Level 2: 4 problems of size n/4, total cost 4·(n/4) = n
...
Level lg n: n problems of size 1, total cost n·1 = n

Total: n + n + n + ... + n (lg n times) = n lg n
```

So we expect T(n) = Θ(n lg n).

---

### Step 2: Prove Upper Bound T(n) = O(n lg n)

**Claim:** T(n) ≤ cn lg n for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≤ ck lg k for all k < n

**Inductive Step:**
```
T(n) = 2T(n/2) + n
     ≤ 2·c(n/2)lg(n/2) + n     [by hypothesis]
     = cn lg(n/2) + n
     = cn(lg n - lg 2) + n
     = cn(lg n - 1) + n
     = cn lg n - cn + n
     = cn lg n + n(1 - c)
```

**Goal:** We want T(n) ≤ cn lg n

**For this to work:**
```
cn lg n + n(1 - c) ≤ cn lg n
n(1 - c) ≤ 0
1 - c ≤ 0
c ≥ 1
```

**Choose:** c = 1 (or any c ≥ 1)

**With c = 1:**
```
T(n) ≤ n lg n + n(1-1) = n lg n ✓
```

---

### Step 3: Handle Base Case for Upper Bound

**Problem:** lg 1 = 0, so T(1) ≤ c·1·0 = 0 doesn't work

**Solution:** Use modified guess T(n) ≤ cn lg n + bn

**Inductive step with modified guess:**
```
T(n) = 2T(n/2) + n
     ≤ 2[c(n/2)lg(n/2) + b(n/2)] + n
     = cn lg(n/2) + bn + n
     = cn(lg n - 1) + bn + n
     = cn lg n - cn + bn + n
     = cn lg n + n(b + 1 - c)
     ≤ cn lg n + bn  [if c ≥ b + 1]
```

**Base case:** n = 1
```
T(1) ≤ c·1·lg 1 + b·1 = 0 + b = b
```
Works if T(1) ≤ b.

**Conclusion:** T(n) = O(n lg n) ✓

---

### Step 4: Prove Lower Bound T(n) = Ω(n lg n)

**To prove Θ, we need both O and Ω!**

**Claim:** T(n) ≥ cn lg n for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≥ ck lg k for all k < n

**Inductive Step:**
```
T(n) = 2T(n/2) + n
     ≥ 2·c(n/2)lg(n/2) + n     [by hypothesis]
     = cn lg(n/2) + n
     = cn(lg n - 1) + n
     = cn lg n - cn + n
     = cn lg n + n(1 - c)
```

**Goal:** We want T(n) ≥ cn lg n

**For this to work:**
```
cn lg n + n(1 - c) ≥ cn lg n
n(1 - c) ≥ 0
1 - c ≥ 0
c ≤ 1
```

**Choose:** c = 1 (or any 0 < c ≤ 1)

**With c = 1:**
```
T(n) ≥ n lg n + n(1-1) = n lg n ✓
```

---

### Step 5: Handle Base Case for Lower Bound

**Use modified guess:** T(n) ≥ cn lg n - bn

**Inductive step:**
```
T(n) = 2T(n/2) + n
     ≥ 2[c(n/2)lg(n/2) - b(n/2)] + n
     = cn lg(n/2) - bn + n
     = cn(lg n - 1) - bn + n
     = cn lg n - cn - bn + n
     = cn lg n - n(c + b - 1)
     ≥ cn lg n - bn  [if c ≤ 1 - b, or b ≤ 1 - c]
```

**Base case:** Choose appropriate constants to make it work.

**Conclusion:** T(n) = Ω(n lg n) ✓

---

### Step 6: Combine for Θ

**Since:**
- T(n) = O(n lg n) (upper bound)
- T(n) = Ω(n lg n) (lower bound)

**Therefore:**
- T(n) = Θ(n lg n) ∎

---

## Problem 4.3-1(e): T(n) = 2T(n/3) + Θ(n), prove T(n) = Θ(n)

### Step 1: Understand the Recurrence

**What does T(n) = 2T(n/3) + Θ(n) mean?**
- Solve TWO subproblems of size n/3
- Do Θ(n) work (linear work)

**Intuition (recursion tree):**
```
Level 0: 1 problem, cost cn
Level 1: 2 problems of size n/3, cost 2·c(n/3) = (2/3)cn
Level 2: 4 problems of size n/9, cost 4·c(n/9) = (4/9)cn
Level 3: 8 problems of size n/27, cost 8·c(n/27) = (8/27)cn
...
```

**Pattern:** Cost at level i = (2/3)^i · cn

**This is a decreasing geometric series!**
```
Total = cn[1 + 2/3 + (2/3)² + (2/3)³ + ...]
      = cn · 1/(1 - 2/3)    [geometric series formula]
      = cn · 3
      = 3cn
      = Θ(n)
```

So we expect T(n) = Θ(n).

---

### Step 2: Prove Upper Bound T(n) = O(n)

**Claim:** T(n) ≤ cn for some constant c > 0

**Simplify Θ(n) to dn:**
Since T(n) = 2T(n/3) + Θ(n), there exists d such that:
```
T(n) ≤ 2T(n/3) + dn
```

**Inductive Hypothesis:** Assume T(k) ≤ ck for all k < n

**Inductive Step:**
```
T(n) ≤ 2T(n/3) + dn
     ≤ 2·c(n/3) + dn
     = (2c/3)n + dn
     = n(2c/3 + d)
```

**Goal:** We want T(n) ≤ cn

**For this to work:**
```
n(2c/3 + d) ≤ cn
2c/3 + d ≤ c
d ≤ c - 2c/3
d ≤ c/3
c ≥ 3d
```

**Choose:** c = 3d

**Verification:**
```
T(n) ≤ n(2·3d/3 + d) = n(2d + d) = 3dn = cn ✓
```

**Base case:** Choose c large enough so T(1) ≤ c.

**Conclusion:** T(n) = O(n) ✓

---

### Step 3: Prove Lower Bound T(n) = Ω(n)

**Claim:** T(n) ≥ cn for some constant c > 0

**Since T(n) = 2T(n/3) + Θ(n), there exists d such that:**
```
T(n) ≥ 2T(n/3) + dn
```

**Inductive Hypothesis:** Assume T(k) ≥ ck for all k < n

**Inductive Step:**
```
T(n) ≥ 2T(n/3) + dn
     ≥ 2·c(n/3) + dn
     = (2c/3)n + dn
     = n(2c/3 + d)
```

**Goal:** We want T(n) ≥ cn

**For this to work:**
```
n(2c/3 + d) ≥ cn
2c/3 + d ≥ c
d ≥ c - 2c/3
d ≥ c/3
c ≤ 3d
```

**Choose:** c = d (or any c ≤ 3d)

**Verification:**
```
T(n) ≥ n(2d/3 + d) = n(2d/3 + 3d/3) = n(5d/3) ≥ dn = cn ✓
```

**Conclusion:** T(n) = Ω(n) ✓

---

### Step 4: Combine for Θ

**Since:**
- T(n) = O(n)
- T(n) = Ω(n)

**Therefore:**
- T(n) = Θ(n) ∎

---

## Problem 4.3-1(f): T(n) = 4T(n/2) + Θ(n), prove T(n) = Θ(n²)

### Step 1: Understand the Recurrence

**What does T(n) = 4T(n/2) + Θ(n) mean?**
- Solve FOUR subproblems of size n/2
- Do Θ(n) work

**Intuition (recursion tree):**
```
Level 0: 1 problem, cost cn
Level 1: 4 problems of size n/2, cost 4·c(n/2) = 2cn
Level 2: 16 problems of size n/4, cost 16·c(n/4) = 4cn
Level 3: 64 problems of size n/8, cost 64·c(n/8) = 8cn
...
Level i: 4^i problems of size n/2^i, cost 4^i·c(n/2^i) = 2^i·cn
```

**Pattern:** Cost at level i = 2^i · cn (growing!)

**Total levels:** lg n

**Total cost:**
```
cn[1 + 2 + 4 + 8 + ... + 2^(lg n)]
= cn[2^(lg n + 1) - 1]
= cn[2n - 1]
≈ 2cn²
= Θ(n²)
```

So we expect T(n) = Θ(n²).

---

### Step 2: Prove Upper Bound T(n) = O(n²)

**Claim:** T(n) ≤ cn² for some constant c > 0

**Simplify:** T(n) ≤ 4T(n/2) + dn for some constant d

**Inductive Hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive Step:**
```
T(n) ≤ 4T(n/2) + dn
     ≤ 4·c(n/2)² + dn
     = 4·c(n²/4) + dn
     = cn² + dn
```

**Goal:** We want T(n) ≤ cn²

**We have:**
```
T(n) ≤ cn² + dn
```

**Problem:** The extra dn term prevents T(n) ≤ cn²!

**Solution:** Use a modified guess (see Problem 4.3-2 for details)

**Modified guess:** T(n) ≤ cn² - bn

**Inductive step with modified guess:**
```
T(n) ≤ 4T(n/2) + dn
     ≤ 4[c(n/2)² - b(n/2)] + dn
     = 4[cn²/4 - bn/2] + dn
     = cn² - 2bn + dn
     = cn² - n(2b - d)
     ≤ cn² - bn  [if 2b - d ≥ b, i.e., b ≥ d]
```

**Choose:** b = d

**Conclusion:** T(n) = O(n²) ✓

---

### Step 3: Prove Lower Bound T(n) = Ω(n²)

**Claim:** T(n) ≥ cn² for some constant c > 0

**Simplify:** T(n) ≥ 4T(n/2) + dn

**Inductive Hypothesis:** Assume T(k) ≥ ck² for all k < n

**Inductive Step:**
```
T(n) ≥ 4T(n/2) + dn
     ≥ 4·c(n/2)² + dn
     = cn² + dn
     ≥ cn²  [since dn ≥ 0]
```

**This works immediately!**

**Conclusion:** T(n) = Ω(n²) ✓

---

### Step 4: Combine for Θ

**Since:**
- T(n) = O(n²)
- T(n) = Ω(n²)

**Therefore:**
- T(n) = Θ(n²) ∎

---

## Problem 4.3-2: Subtraction of Lower-Order Terms

### Problem Statement
The solution to the recurrence T(n) = 4T(n/2) + n turns out to be T(n) = Θ(n²). Show that a substitution proof with the assumption T(n) ≤ cn² fails. Then show how to subtract a lower-order term to make a substitution proof work.

---

### Part 1: Show That T(n) ≤ cn² Fails

**Recurrence:** T(n) = 4T(n/2) + n

**Guess:** T(n) ≤ cn²

**Inductive Hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive Step:**
```
T(n) = 4T(n/2) + n
     ≤ 4·c(n/2)² + n     [by hypothesis]
     = 4·c·n²/4 + n
     = cn² + n
```

**Goal:** We want to show T(n) ≤ cn²

**But we have:** T(n) ≤ cn² + n

**Problem:** The extra "+n" term means we CANNOT conclude T(n) ≤ cn²!

**Why this fails:**
- We need T(n) ≤ cn² exactly
- But we get T(n) ≤ cn² + n
- The extra n term breaks the proof
- No choice of c can make "cn² + n ≤ cn²" true for all n

**Conclusion:** The simple guess T(n) ≤ cn² FAILS. ✗

---

### Part 2: Subtract a Lower-Order Term

**Key insight:** The problem is the extra linear term (+n)

**Solution:** Modify the guess to "absorb" this term

**New guess:** T(n) ≤ cn² - dn for some constants c, d > 0

**Why this might work:**
- The -dn term is "lower-order" (smaller than n²)
- It can potentially cancel out the +n we get from the recurrence
- Asymptotically, cn² - dn is still Θ(n²)

---

### Part 3: Prove the Modified Guess

**Claim:** T(n) ≤ cn² - dn for appropriate constants c, d > 0

**Inductive Hypothesis:** Assume T(k) ≤ ck² - dk for all k < n

**Inductive Step:**
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n     [by hypothesis]
     = 4[c·n²/4 - d·n/2] + n
     = cn² - 2dn + n
     = cn² - dn - dn + n
     = cn² - dn - n(d - 1)
```

**Goal:** We want T(n) ≤ cn² - dn

**For this to work:**
```
cn² - dn - n(d - 1) ≤ cn² - dn
-n(d - 1) ≤ 0
d - 1 ≥ 0
d ≥ 1
```

**Choose:** d = 1 (or any d ≥ 1)

**With d = 1:**
```
T(n) ≤ cn² - n - n(1-1) = cn² - n ✓
```

**This works!**

---

### Part 4: Verify Base Case

**Base case:** n = 1

**We need:** T(1) ≤ c·1² - d·1 = c - d

**If T(1) is given:** Choose c large enough so that c - d ≥ T(1)

**For example:** If T(1) = 1 and d = 1, choose c = 2:
```
T(1) = 1 ≤ 2 - 1 = 1 ✓
```

---

### Part 5: Why This Works

**The modified guess cn² - dn:**
- Still represents O(n²) (the -dn doesn't change asymptotic behavior)
- The -dn term provides "room" to absorb the +n from the recurrence
- Mathematically: -2dn + n = -dn - (d-1)n ≤ -dn when d ≥ 1

**General principle:**
- When a simple guess fails due to lower-order terms
- Subtract a lower-order term from your guess
- This gives you "slack" to absorb extra terms in the induction

---

### Final Answer for Problem 4.3-2

**Part 1: Simple guess fails**
```
Guess: T(n) ≤ cn²
Result: T(n) ≤ cn² + n
Conclusion: Cannot prove T(n) ≤ cn² (extra +n term)
```

**Part 2: Modified guess succeeds**
```
Guess: T(n) ≤ cn² - dn (with d ≥ 1)
Proof:
  T(n) = 4T(n/2) + n
       ≤ 4[c(n/2)² - d(n/2)] + n
       = cn² - 2dn + n
       = cn² - dn - (d-1)n
       ≤ cn² - dn  [for d ≥ 1]
Conclusion: T(n) = O(n²) ✓
```

---

## Problem 4.3-3: Exponential Recurrence with Lower-Order Term

### Problem Statement
The recurrence T(n) = 2T(n-1) + 1 has the solution T(n) = O(2ⁿ). Show that a substitution proof fails with the assumption T(n) ≤ c·2ⁿ, where c > 0 is constant. Then show how to subtract a lower-order term to make a substitution proof work.

---

### Part 1: Understand the Recurrence

**What does T(n) = 2T(n-1) + 1 mean?**
- To solve size n, solve TWO problems of size n-1
- Plus constant work (+1)
- This grows exponentially!

**Intuition:**
```
T(n) = 2T(n-1) + 1
     = 2[2T(n-2) + 1] + 1
     = 4T(n-2) + 2 + 1
     = 4[2T(n-3) + 1] + 2 + 1
     = 8T(n-3) + 4 + 2 + 1
     = ...
     = 2^k T(n-k) + (2^(k-1) + ... + 2 + 1)
     = 2^k T(n-k) + (2^k - 1)
```

**When k = n-1:**
```
T(n) = 2^(n-1) T(1) + (2^(n-1) - 1)
     = 2^(n-1) T(1) + 2^(n-1) - 1
     = 2^(n-1)(T(1) + 1) - 1
     = Θ(2^n)
```

---

### Part 2: Show That T(n) ≤ c·2ⁿ Fails

**Guess:** T(n) ≤ c·2ⁿ

**Inductive Hypothesis:** Assume T(k) ≤ c·2^k for all k < n

**Inductive Step:**
```
T(n) = 2T(n-1) + 1
     ≤ 2·c·2^(n-1) + 1     [by hypothesis]
     = c·2^n + 1
```

**Goal:** We want T(n) ≤ c·2ⁿ

**But we have:** T(n) ≤ c·2ⁿ + 1

**Problem:** The extra "+1" prevents us from concluding T(n) ≤ c·2ⁿ

**Why no choice of c works:**
- We need: c·2ⁿ + 1 ≤ c·2ⁿ
- This requires: 1 ≤ 0
- Impossible!

**Conclusion:** The simple guess T(n) ≤ c·2ⁿ FAILS. ✗

---

### Part 3: Subtract a Lower-Order Term

**Key insight:** 2ⁿ grows much faster than any constant

**Lower-order terms compared to 2ⁿ:**
- Constants: 1, 2, 100, ... (much smaller)
- Linear: n, 2n, ... (much smaller)
- Polynomial: n², n³, ... (much smaller)
- All are "lower-order" compared to 2ⁿ

**New guess:** T(n) ≤ c·2ⁿ - d for some constants c, d > 0

**Why subtract a constant?**
- The recurrence adds a constant (+1)
- Subtracting a constant from our guess can absorb this

---

### Part 4: Prove the Modified Guess

**Claim:** T(n) ≤ c·2ⁿ - d for appropriate constants c, d > 0

**Inductive Hypothesis:** Assume T(k) ≤ c·2^k - d for all k < n

**Inductive Step:**
```
T(n) = 2T(n-1) + 1
     ≤ 2[c·2^(n-1) - d] + 1     [by hypothesis]
     = 2c·2^(n-1) - 2d + 1
     = c·2^n - 2d + 1
```

**Goal:** We want T(n) ≤ c·2ⁿ - d

**For this to work:**
```
c·2^n - 2d + 1 ≤ c·2^n - d
-2d + 1 ≤ -d
1 ≤ 2d - d
1 ≤ d
d ≥ 1
```

**Choose:** d = 1 (or any d ≥ 1)

**With d = 1:**
```
T(n) ≤ c·2^n - 2 + 1 = c·2^n - 1 ✓
```

**This works!**

---

### Part 5: Verify Base Case

**Base case:** n = 1

**We need:** T(1) ≤ c·2¹ - d = 2c - d

**If T(1) is given:** Choose c large enough so that 2c - d ≥ T(1)

**For example:** If T(1) = 1 and d = 1:
```
Need: 2c - 1 ≥ 1
      2c ≥ 2
      c ≥ 1
```

Choose c = 1:
```
T(1) = 1 ≤ 2·1 - 1 = 1 ✓
```

---

### Part 6: Why This Works

**The modified guess c·2ⁿ - d:**
- Still represents O(2ⁿ) (the -d doesn't change asymptotic behavior)
- The constant -d provides room to absorb the +1 from the recurrence
- Mathematically: -2d + 1 ≤ -d when d ≥ 1

**Key principle:**
- Exponential terms dominate everything else
- Subtracting a lower-order term (even a constant) gives enough slack
- The proof works because 2d - d = d ≥ 1

---

### Final Answer for Problem 4.3-3

**Part 1: Simple guess fails**
```
Guess: T(n) ≤ c·2ⁿ
Result: T(n) ≤ c·2ⁿ + 1
Conclusion: Cannot prove T(n) ≤ c·2ⁿ (extra +1 term)
```

**Part 2: Modified guess succeeds**
```
Guess: T(n) ≤ c·2ⁿ - d (with d ≥ 1)
Proof:
  T(n) = 2T(n-1) + 1
       ≤ 2[c·2^(n-1) - d] + 1
       = c·2^n - 2d + 1
       ≤ c·2^n - d  [for d ≥ 1]
Conclusion: T(n) = O(2ⁿ) ✓
```

---

## Summary: Key Techniques for Substitution Method

### General Strategy

**1. Guess the solution form**
- Use intuition, recursion trees, or experience
- Common forms: O(n), O(n lg n), O(n²), O(2ⁿ)

**2. Prove by induction**
- Base case: Verify for small n
- Inductive hypothesis: Assume for k < n
- Inductive step: Prove for n using hypothesis

**3. If simple guess fails**
- Add or subtract lower-order terms
- Common modifications:
  - cn² → cn² - dn (subtract linear)
  - cn → cn + b (add constant)
  - c·2ⁿ → c·2ⁿ - d (subtract constant)

### Common Pitfalls

**1. Base case issues**
- lg 1 = 0 can cause problems
- Solution: Start at n = 2, or add constant term

**2. Extra terms in induction**
- Getting cn² + n instead of cn²
- Solution: Modify guess to cn² - dn

**3. Wrong direction for inequality**
- For O: need ≤
- For Ω: need ≥
- For Θ: need both

### When to Use Lower-Order Terms

**Subtract lower-order term when:**
- Recurrence adds a term (e.g., +n, +1)
- Simple guess gives T(n) ≤ f(n) + extra
- Need to absorb the extra term

**Add lower-order term when:**
- Base case doesn't work (e.g., lg 1 = 0)
- Need more flexibility in the proof

---

**End of Section 4.3 Solutions**
