# Chapter 4.3 Complete Guide: The Substitution Method

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 4.3 - The Substitution Method for Solving Recurrences  
**Purpose:** Master the most general method for solving recurrences

---

## 🎯 What Chapter 4.3 Is Really About

### The Big Picture

Chapter 4.3 teaches you **the substitution method** - the most powerful and general technique for solving recurrences.

**Mental model:** The substitution method is like solving a puzzle:
1. **Guess** what the answer looks like (the hard part)
2. **Prove** your guess is correct using induction (mechanical)

**Why it's important:**
- Works for ANY recurrence (most general method)
- Teaches you to think about growth rates
- Foundation for understanding other methods
- Essential for proving tight bounds

**Key insight:** You don't need to know the exact answer - just the asymptotic form (O, Ω, or Θ)

---

## 📚 The Two-Step Process

### Step 1: Guess the Form

**What to guess:**
- The asymptotic form with symbolic constants
- Example: "I think T(n) = O(n²)" becomes "T(n) ≤ cn²"

**How to make good guesses:**
1. **Use recursion trees** (Section 4.4)
2. **Look at similar recurrences** you've seen before
3. **Start with loose bounds** and narrow down
4. **Use intuition** about the problem

**Common forms to try:**
```
O(1)         - constant
O(lg n)      - logarithmic
O(n)         - linear
O(n lg n)    - linearithmic
O(n²)        - quadratic
O(n³)        - cubic
O(2ⁿ)        - exponential
```

---

### Step 2: Prove by Induction

**Mathematical induction structure:**

**1. Base case:**
- Verify the guess holds for small values (usually n = 1 or n = 2)
- Choose constants to make it work

**2. Inductive hypothesis:**
- **Assume** the guess holds for all values smaller than n
- This is your "given" for the proof

**3. Inductive step:**
- **Prove** the guess holds for n using the hypothesis
- Substitute the hypothesis into the recurrence
- Use algebra to verify

**If all three work:** Your guess is correct! ✓

---

## 🎓 Detailed Example: T(n) = 2T(⌊n/2⌋) + Θ(n)

### The Problem

**Recurrence:**
```
T(n) = 2T(⌊n/2⌋) + Θ(n)
```

**Goal:** Prove T(n) = O(n lg n)

---

### Step 1: Make Precise Guess

**Claim:** T(n) ≤ cn lg n for some constant c > 0 and all n ≥ n₀

**Why this form?**
- We're proving O(n lg n), which means T(n) ≤ c·(n lg n)
- Must use explicit constant c (not asymptotic notation in hypothesis!)

**Important:** Don't write "T(n) ≤ O(n lg n)" - this is wrong!

---

### Step 2: Inductive Hypothesis

**Assume:** T(k) ≤ ck lg k for all k < n (specifically for ⌊n/2⌋)

**Why we can assume this:**
- We're doing induction
- We get to assume it's true for smaller values
- Then we prove it for n

---

### Step 3: Inductive Step

**Start with recurrence:**
```
T(n) = 2T(⌊n/2⌋) + Θ(n)
```

**Simplify Θ(n):**
Since Θ(n) ≤ dn for some constant d:
```
T(n) ≤ 2T(⌊n/2⌋) + dn
```

**Apply inductive hypothesis:**
Since ⌊n/2⌋ < n, we have T(⌊n/2⌋) ≤ c⌊n/2⌋ lg(⌊n/2⌋)

**Substitute:**
```
T(n) ≤ 2·c⌊n/2⌋ lg(⌊n/2⌋) + dn
```

**Simplify floor function:**
Since ⌊n/2⌋ ≤ n/2:
```
T(n) ≤ 2·c(n/2) lg(n/2) + dn
     = cn lg(n/2) + dn
```

**Simplify logarithm:**
```
lg(n/2) = lg n - lg 2 = lg n - 1
```

**Continue:**
```
T(n) ≤ cn(lg n - 1) + dn
     = cn lg n - cn + dn
     = cn lg n + n(d - c)
```

**Goal:** We want T(n) ≤ cn lg n

**For this to work:**
```
cn lg n + n(d - c) ≤ cn lg n
n(d - c) ≤ 0
d - c ≤ 0
c ≥ d
```

**Choose:** c = d (or any c ≥ d)

**Result:**
```
T(n) ≤ cn lg n + n(d - d) = cn lg n ✓
```

**The induction works!**

---

### Step 4: Base Case

**Problem:** lg 1 = 0, so T(1) ≤ c·1·0 = 0 might not work

**Solutions:**

**Option 1:** Start at n = 2
```
T(2) ≤ c·2·lg 2 = 2c
```
Choose c large enough so T(2) ≤ 2c

**Option 2:** Modify guess to T(n) ≤ cn lg n + b
- The constant b handles base case
- Doesn't affect asymptotic behavior

**For this example:** Use n₀ = 2 and choose c ≥ max{T(2)/2, T(3)/(3 lg 3)}

---

### Step 5: Conclusion

**We've shown:**
- T(n) ≤ cn lg n for all n ≥ 2 (for appropriate c)
- Therefore: T(n) = O(n lg n) ✓

---

## 💡 The Trick: Subtracting Lower-Order Terms

### When Simple Guesses Fail

**Common problem:** You guess correctly, but the math doesn't work out

**Example:** T(n) = 4T(n/2) + n, guess T(n) ≤ cn²

**What happens:**
```
T(n) = 4T(n/2) + n
     ≤ 4c(n/2)² + n
     = cn² + n
```

**Problem:** We get cn² + n, not cn²! The extra +n breaks the proof.

---

### The Solution: Subtract a Lower-Order Term

**Modified guess:** T(n) ≤ cn² - dn

**Why this works:**
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n
     = cn² - 2dn + n
     = cn² - dn - (d-1)n
     ≤ cn² - dn  [if d ≥ 1]
```

**The magic:** Subtracting dn from each subproblem gives us -2dn total, which absorbs the +n!

---

### When to Subtract vs Add

**Subtract lower-order term when:**
- Recurrence adds extra terms: T(n) = aT(n/b) + f(n) + extra
- Simple guess gives: T(n) ≤ f(n) + extra
- Need to absorb the extra term
- **Example:** T(n) = 4T(n/2) + n → guess cn² - dn

**Add lower-order term when:**
- Base case doesn't work (e.g., lg 1 = 0)
- Need more flexibility
- **Example:** T(n) ≤ cn lg n + b handles base case

---

## 🎯 Problem-Solving Framework

### Framework for Any Substitution Proof

**Step 1: Understand the recurrence**
- What does it represent?
- What's the intuition?
- What do you expect the answer to be?

**Step 2: Make a precise guess**
- Convert O(f(n)) to T(n) ≤ cf(n)
- Convert Ω(f(n)) to T(n) ≥ cf(n)
- Use explicit constants (c, d, etc.)

**Step 3: Set up induction**
- State base case
- State inductive hypothesis
- State what you'll prove

**Step 4: Prove inductive step**
- Start with recurrence
- Apply inductive hypothesis
- Substitute and simplify
- Verify inequality holds

**Step 5: Handle base case**
- Check if base case works
- If not, modify guess or change n₀

**Step 6: Conclude**
- State the result clearly
- Box or mark the final answer

---

## 📋 Common Recurrence Patterns

### Pattern 1: Linear Decrease

**Form:** T(n) = T(n-1) + f(n)

**Examples:**
```
T(n) = T(n-1) + 1       → T(n) = Θ(n)
T(n) = T(n-1) + n       → T(n) = Θ(n²)
T(n) = T(n-1) + n²      → T(n) = Θ(n³)
```

**Pattern:** T(n) = Θ(Σf(i)) = Θ(sum of f from 1 to n)

---

### Pattern 2: Logarithmic Decrease

**Form:** T(n) = T(n/2) + f(n)

**Examples:**
```
T(n) = T(n/2) + 1       → T(n) = Θ(lg n)
T(n) = T(n/2) + n       → T(n) = Θ(n)
T(n) = T(n/2) + n²      → T(n) = Θ(n²)
```

**Pattern:** Dominated by f(n) at root (top level)

---

### Pattern 3: Binary Split

**Form:** T(n) = 2T(n/2) + f(n)

**Examples:**
```
T(n) = 2T(n/2) + 1      → T(n) = Θ(n)
T(n) = 2T(n/2) + n      → T(n) = Θ(n lg n)
T(n) = 2T(n/2) + n²     → T(n) = Θ(n²)
```

**Pattern:** Depends on f(n) vs n (see Master Theorem)

---

### Pattern 4: Exponential Growth

**Form:** T(n) = 2T(n-1) + f(n)

**Examples:**
```
T(n) = 2T(n-1) + 1      → T(n) = Θ(2ⁿ)
T(n) = 2T(n-1) + n      → T(n) = Θ(2ⁿ)
```

**Pattern:** Exponential dominates everything

---

## ⚠️ Common Mistakes and Pitfalls

### Mistake 1: Using Asymptotic Notation in Hypothesis

**Wrong:**
```
Inductive hypothesis: T(n) = O(n lg n)
T(n) ≤ 2·O(n/2 lg(n/2)) + n
     = O(n lg n)  ✗
```

**Why it's wrong:**
- Constants hidden by O can change
- Not a valid mathematical proof

**Right:**
```
Inductive hypothesis: T(n) ≤ cn lg n
T(n) ≤ 2·c(n/2)lg(n/2) + n
     = cn lg n - cn + n
     ≤ cn lg n  [if c ≥ 1]  ✓
```

---

### Mistake 2: Proving Wrong Statement

**Wrong:**
```
Goal: Prove T(n) = O(n)
Hypothesis: T(n) ≤ cn
Result: T(n) ≤ cn + Θ(n) = O(n)  ✗
```

**Why it's wrong:**
- Must prove EXACT form of hypothesis
- Can't conclude T(n) ≤ cn from T(n) ≤ cn + Θ(n)

**Right:**
- Prove exactly what you claimed: T(n) ≤ cn
- If you get extra terms, modify your guess

---

### Mistake 3: Ignoring Base Case

**Wrong:**
```
Prove inductive step only, ignore base case  ✗
```

**Why it's wrong:**
- Induction needs both base case and inductive step
- Base case grounds the proof

**Right:**
- Always verify base case
- Choose constants to make it work
- Or modify guess if needed

---

### Mistake 4: Wrong Inequality Direction

**For O (upper bound):**
```
✓ Use ≤
✗ Don't use ≥
```

**For Ω (lower bound):**
```
✓ Use ≥
✗ Don't use ≤
```

---

## 🔧 Advanced Techniques

### Technique 1: Changing Variables

**Sometimes useful to substitute:**
- Let m = lg n, then n = 2^m
- Recurrence in n becomes recurrence in m
- Solve for m, then convert back

**Example:**
```
T(n) = 2T(√n) + lg n

Let m = lg n, so n = 2^m and √n = 2^(m/2)
S(m) = T(2^m)
S(m) = 2S(m/2) + m
Solution: S(m) = Θ(m lg m)
Therefore: T(n) = Θ(lg n · lg lg n)
```

---

### Technique 2: Strengthening Hypothesis

**If simple guess fails, try:**
- Subtracting lower-order terms: cn² - dn
- Adding lower-order terms: cn lg n + b
- Using different constants for different terms

**Example:**
```
T(n) = T(n/2) + T(n/4) + n

Simple guess T(n) ≤ cn fails
Modified guess T(n) ≤ cn - d works
```

---

### Technique 3: Handling Floor/Ceiling

**For ⌊n/2⌋ or ⌈n/2⌉:**
- Usually safe to replace with n/2 in the proof
- Rigorous approach: show ⌊n/2⌋ ≤ n/2 and proceed

**Example:**
```
T(⌊n/2⌋) ≤ c⌊n/2⌋ lg(⌊n/2⌋)
         ≤ c(n/2) lg(n/2)
```

---

## 📊 Complete Examples

### Example 1: T(n) = T(n-1) + n

**Guess:** T(n) = O(n²), so T(n) ≤ cn²

**Inductive step:**
```
T(n) = T(n-1) + n
     ≤ c(n-1)² + n
     = c(n² - 2n + 1) + n
     = cn² - 2cn + c + n
     = cn² + n(1 - 2c) + c
     ≤ cn²  [if c ≥ 1]
```

**Base case:** T(1) ≤ c works for c ≥ T(1)

**Conclusion:** T(n) = O(n²) ✓

---

### Example 2: T(n) = T(n/2) + Θ(1)

**Guess:** T(n) = O(lg n), so T(n) ≤ c lg n

**Problem:** lg 1 = 0 makes base case fail

**Modified guess:** T(n) ≤ c lg n + b

**Inductive step:**
```
T(n) = T(n/2) + d
     ≤ [c lg(n/2) + b] + d
     = c(lg n - 1) + b + d
     = c lg n + (b + d - c)
     ≤ c lg n + b  [if c ≥ d]
```

**Base case:** T(1) ≤ b works for b ≥ T(1)

**Conclusion:** T(n) = O(lg n) ✓

---

### Example 3: T(n) = 2T(n/2) + n

**Guess:** T(n) = Θ(n lg n)

**Upper bound:** T(n) ≤ cn lg n
```
T(n) = 2T(n/2) + n
     ≤ 2·c(n/2)lg(n/2) + n
     = cn lg(n/2) + n
     = cn(lg n - 1) + n
     = cn lg n - cn + n
     = cn lg n + n(1 - c)
     ≤ cn lg n  [if c ≥ 1]
```

**Lower bound:** T(n) ≥ cn lg n
```
T(n) = 2T(n/2) + n
     ≥ 2·c(n/2)lg(n/2) + n
     = cn lg n + n(1 - c)
     ≥ cn lg n  [if c ≤ 1]
```

**Choose c = 1:** Both bounds work!

**Conclusion:** T(n) = Θ(n lg n) ✓

---

### Example 4: T(n) = 2T(n/3) + Θ(n)

**Guess:** T(n) = Θ(n)

**Upper bound:** T(n) ≤ cn
```
T(n) ≤ 2T(n/3) + dn
     ≤ 2·c(n/3) + dn
     = (2c/3)n + dn
     = n(2c/3 + d)
     ≤ cn  [if 2c/3 + d ≤ c, i.e., c ≥ 3d]
```

**Choose c = 3d:** Works! ✓

**Lower bound:** Similar, choose c ≤ 3d

**Conclusion:** T(n) = Θ(n) ✓

---

### Example 5: T(n) = 4T(n/2) + Θ(n)

**Guess:** T(n) = Θ(n²)

**Simple guess T(n) ≤ cn² fails:**
```
T(n) ≤ 4c(n/2)² + dn
     = cn² + dn
     ≰ cn²  [extra dn term!]
```

**Modified guess T(n) ≤ cn² - en works:**
```
T(n) ≤ 4[c(n/2)² - e(n/2)] + dn
     = cn² - 2en + dn
     = cn² - en - (e - d)n
     ≤ cn² - en  [if e ≥ d]
```

**Choose e = d:** Works! ✓

**Conclusion:** T(n) = Θ(n²) ✓

---

### Example 6: T(n) = 2T(n-1) + 1

**Guess:** T(n) = O(2ⁿ)

**Simple guess T(n) ≤ c·2ⁿ fails:**
```
T(n) = 2T(n-1) + 1
     ≤ 2·c·2^(n-1) + 1
     = c·2^n + 1
     ≰ c·2^n  [extra +1!]
```

**Modified guess T(n) ≤ c·2ⁿ - d works:**
```
T(n) = 2T(n-1) + 1
     ≤ 2[c·2^(n-1) - d] + 1
     = c·2^n - 2d + 1
     ≤ c·2^n - d  [if d ≥ 1]
```

**Choose d = 1:** Works! ✓

**Conclusion:** T(n) = O(2ⁿ) ✓

---

## 🎯 Decision Tree: What to Guess

### Based on Recurrence Form

```
T(n) = T(n-1) + f(n)
├─ f(n) = Θ(1)     → Guess Θ(n)
├─ f(n) = Θ(n)     → Guess Θ(n²)
└─ f(n) = Θ(n^k)   → Guess Θ(n^(k+1))

T(n) = T(n/2) + f(n)
├─ f(n) = Θ(1)     → Guess Θ(lg n)
├─ f(n) = Θ(n)     → Guess Θ(n)
└─ f(n) = Θ(n^k)   → Guess Θ(n^k)

T(n) = 2T(n/2) + f(n)
├─ f(n) = Θ(1)     → Guess Θ(n)
├─ f(n) = Θ(n)     → Guess Θ(n lg n)
└─ f(n) = Θ(n²)    → Guess Θ(n²)

T(n) = aT(n/b) + f(n)
├─ a < b           → Guess Θ(f(n))
├─ a = b           → Guess Θ(f(n) lg n)
└─ a > b           → Guess Θ(n^(log_b a))

T(n) = 2T(n-1) + f(n)
└─ Any f(n)        → Guess Θ(2ⁿ)
```

---

## ⚠️ Common Mistakes Summary

### Mistake 1: Asymptotic Notation in Hypothesis
```
✗ T(n) = O(n lg n)
✓ T(n) ≤ cn lg n
```

### Mistake 2: Not Proving Exact Form
```
✗ T(n) ≤ cn + Θ(1) = O(n)
✓ T(n) ≤ cn (prove exactly this)
```

### Mistake 3: Ignoring Base Case
```
✗ Only prove inductive step
✓ Prove both base case and inductive step
```

### Mistake 4: Wrong Constants
```
✗ Choosing c that doesn't satisfy constraints
✓ Verify c satisfies all inequalities
```

### Mistake 5: Not Modifying Failed Guess
```
✗ Give up when simple guess fails
✓ Try subtracting/adding lower-order terms
```

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Identify recurrence pattern
- [ ] Make educated guess based on pattern
- [ ] Decide if proving O, Ω, or Θ

### While Solving
- [ ] Write precise hypothesis with constants
- [ ] Show all algebraic steps
- [ ] Verify inequality direction (≤ for O, ≥ for Ω)
- [ ] Check base case
- [ ] State conclusion clearly

### If Stuck
- [ ] Try subtracting lower-order term
- [ ] Try adding constant term
- [ ] Check if you're proving exact form
- [ ] Verify constant constraints

### Time Management
- Simple proof: 10-15 min
- With modifications: 15-20 min
- Θ proof (both bounds): 20-30 min

---

**You're ready to master the substitution method! 🎉**

---

**End of Guide**
