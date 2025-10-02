# Chapter 4.5 Complete Guide: The Master Method

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 4.5 - The Master Method for Solving Recurrences  
**Purpose:** Master the "cookbook" method for solving divide-and-conquer recurrences

---

## 🎯 What Chapter 4.5 Is Really About

### The Big Picture

Chapter 4.5 teaches you **the Master Method** - a powerful formula that solves most divide-and-conquer recurrences instantly.

**Mental model:** The Master Method is like a **calculator for recurrences**:
- Input: T(n) = aT(n/b) + f(n)
- Process: Compare f(n) with n^(log_b a)
- Output: The solution!

**Why it's important:**
- **Speed:** Solve recurrences in seconds, not minutes
- **No guessing:** Direct formula, no recursion trees needed
- **Covers most cases:** Works for 90%+ of practical recurrences
- **Foundation:** Understanding it deepens intuition about algorithms

**Key insight:** You don't need complex proofs - just memorize 3 cases and apply!

---

## 📚 The Master Theorem

### The General Form

**Given:** T(n) = aT(n/b) + f(n)

**Where:**
- **a ≥ 1:** Number of subproblems
- **b > 1:** Factor by which problem size decreases
- **f(n):** Driving function (cost of divide + combine)

**Goal:** Find T(n) = ?

---

### The Watershed Function

**Key concept:** n^(log_b a)

**This is called the "watershed function" or "critical exponent"**

**What it represents:**
- Cost of all leaves in the recursion tree
- Natural growth rate for this recurrence
- Dividing line between the three cases

**How to calculate:**
```
log_b a = (lg a) / (lg b)
n^(log_b a) = n^((lg a)/(lg b))
```

**Examples:**
```
a=2, b=2: n^(log₂ 2) = n^1 = n
a=4, b=2: n^(log₂ 4) = n^2
a=8, b=2: n^(log₂ 8) = n^3
a=7, b=2: n^(log₂ 7) ≈ n^2.807
a=2, b=4: n^(log₄ 2) = n^0.5 = √n
```

---

## 🎓 The Three Cases

### Case 1: Leaves Dominate

**Condition:** f(n) = O(n^(log_b a - ε)) for some ε > 0

**Translation:** f(n) is **polynomially smaller** than n^(log_b a)

**Solution:** T(n) = Θ(n^(log_b a))

**Intuition:**
- Recursive calls do most of the work
- Cost grows geometrically from root to leaves
- Leaves dominate the total cost

**Visual:**
```
Recursion tree costs:
Root:     f(n)
Level 1:  More than f(n)
Level 2:  Even more
...
Leaves:   DOMINATES (answer is here!)
```

**Example:**
```
T(n) = 8T(n/2) + n²

a=8, b=2, f(n)=n²
n^(log_b a) = n^(log₂ 8) = n³

Compare: n² vs n³
n² is polynomially smaller (ε=1)

Solution: T(n) = Θ(n³) ✓
```

---

### Case 2: All Levels Equal

**Condition:** f(n) = Θ(n^(log_b a) × (lg n)^k) for some k ≥ 0

**Translation:** f(n) grows at **same rate** as n^(log_b a) (up to logarithmic factors)

**Solution:** T(n) = Θ(n^(log_b a) × (lg n)^(k+1))

**Intuition:**
- All levels contribute equally
- Balanced work distribution
- Total = cost per level × number of levels

**Visual:**
```
Recursion tree costs:
Root:     f(n)
Level 1:  ≈ f(n)
Level 2:  ≈ f(n)
...
All equal! (multiply by height)
```

**Most common:** k = 0 (no logarithmic factor)
```
f(n) = Θ(n^(log_b a))
Solution: T(n) = Θ(n^(log_b a) × lg n)
```

**Example:**
```
T(n) = 2T(n/2) + n

a=2, b=2, f(n)=n
n^(log_b a) = n^(log₂ 2) = n

Compare: n vs n
Equal! (k=0)

Solution: T(n) = Θ(n lg n) ✓
```

**With logarithmic factor:**
```
T(n) = 2T(n/2) + n lg n

f(n) = n lg n = n × (lg n)^1
So k=1

Solution: T(n) = Θ(n lg² n) ✓
```

---

### Case 3: Root Dominates

**Condition:** 
1. f(n) = Ω(n^(log_b a + ε)) for some ε > 0
2. **Regularity:** af(n/b) ≤ cf(n) for some c < 1

**Translation:** f(n) is **polynomially larger** than n^(log_b a) AND satisfies regularity

**Solution:** T(n) = Θ(f(n))

**Intuition:**
- Divide/combine does most of the work
- Cost decreases geometrically from root to leaves
- Root dominates the total cost

**Visual:**
```
Recursion tree costs:
Root:     f(n) ← DOMINATES (answer is here!)
Level 1:  Less than f(n)
Level 2:  Even less
...
Leaves:   Negligible
```

**Example:**
```
T(n) = 2T(n/2) + n²

a=2, b=2, f(n)=n²
n^(log_b a) = n

Compare: n² vs n
n² is polynomially larger (ε=1)

Check regularity:
af(n/b) = 2(n/2)² = n²/2
cf(n) = c·n²
Need: n²/2 ≤ c·n²
So: c ≥ 1/2 (choose c=3/4) ✓

Solution: T(n) = Θ(n²) ✓
```

---

## 💡 Understanding "Polynomially Smaller/Larger"

### Polynomially Smaller

**Definition:** f(n) = O(n^(log_b a - ε)) for some ε > 0

**What it means:** f(n) is smaller by at least a factor of n^ε

**Examples:**
```
n² vs n³: polynomially smaller (ε=1)
n vs n²: polynomially smaller (ε=1)
1 vs √n: polynomially smaller (ε=0.5)
√n vs n: polynomially smaller (ε=0.5)
```

**NOT polynomially smaller:**
```
n vs n lg n: only logarithmically smaller
n² vs n² lg n: only logarithmically smaller
```

---

### Polynomially Larger

**Definition:** f(n) = Ω(n^(log_b a + ε)) for some ε > 0

**What it means:** f(n) is larger by at least a factor of n^ε

**Examples:**
```
n³ vs n²: polynomially larger (ε=1)
n² vs n: polynomially larger (ε=1)
n vs √n: polynomially larger (ε=0.5)
```

**NOT polynomially larger:**
```
n lg n vs n: only logarithmically larger
n² lg n vs n²: only logarithmically larger
```

---

### The Gaps

**Between Case 1 and Case 2:**
- f(n) = o(n^(log_b a)) but not polynomially smaller
- Example: f(n) = n/lg n when n^(log_b a) = n

**Between Case 2 and Case 3:**
- f(n) = ω(n^(log_b a)) but not polynomially larger
- Example: f(n) = n lg n when n^(log_b a) = n

**If your recurrence falls in a gap:** Master Method doesn't apply!

---

## 🔑 The Regularity Condition

### What It Is

**Condition:** af(n/b) ≤ cf(n) for some constant c < 1

**Required for:** Case 3 only

**What it means:** Cost at root is at least a constant fraction larger than total cost of children

---

### Why It's Needed

**Without regularity:** f(n) could be large but oscillate wildly

**Example of failure:** f(n) = 2^(⌈lg n⌉)
- This is large (exponential!)
- But it doesn't satisfy regularity
- Master Theorem Case 3 doesn't apply

---

### How to Check

**Step 1:** Calculate af(n/b)

**Step 2:** Compare with f(n)

**Step 3:** Find c such that af(n/b) ≤ cf(n)

**Step 4:** Verify c < 1

**Example:**
```
f(n) = n², a=2, b=2

af(n/b) = 2(n/2)² = 2·n²/4 = n²/2

Need: n²/2 ≤ c·n²
Simplify: 1/2 ≤ c

Choose: c = 3/4 (satisfies 1/2 ≤ 3/4 < 1) ✓
```

**Common functions that satisfy regularity:**
- Polynomials: n^k
- Polynomial × log: n^k (lg n)^j
- Most "well-behaved" functions

---

## 📊 Step-by-Step Process

### Step 1: Identify Parameters

**From T(n) = aT(n/b) + f(n), extract:**
- a = ?
- b = ?
- f(n) = ?

---

### Step 2: Calculate Watershed

**Compute:** n^(log_b a)

**Formula:** log_b a = (lg a) / (lg b)

**Common values:**
```
log₂ 2 = 1
log₂ 4 = 2
log₂ 8 = 3
log₄ 2 = 0.5
log₃ 9 = 2
```

---

### Step 3: Compare f(n) with n^(log_b a)

**Three possibilities:**

**1. f(n) < n^(log_b a) (polynomially)**
- Check if f(n) = O(n^(log_b a - ε)) for some ε > 0
- If yes → Case 1

**2. f(n) ≈ n^(log_b a) (same rate)**
- Check if f(n) = Θ(n^(log_b a) × (lg n)^k) for some k ≥ 0
- If yes → Case 2

**3. f(n) > n^(log_b a) (polynomially)**
- Check if f(n) = Ω(n^(log_b a + ε)) for some ε > 0
- If yes, check regularity
- If both yes → Case 3

---

### Step 4: Apply Formula

**Case 1:** T(n) = Θ(n^(log_b a))

**Case 2:** T(n) = Θ(n^(log_b a) × (lg n)^(k+1))

**Case 3:** T(n) = Θ(f(n))

---

## 🎯 Complete Examples

### Example 1: T(n) = 9T(n/3) + n

**Step 1: Parameters**
```
a = 9, b = 3, f(n) = n
```

**Step 2: Watershed**
```
n^(log_b a) = n^(log₃ 9) = n^2
```

**Step 3: Compare**
```
f(n) = n
n^(log_b a) = n²

n < n² (polynomially, ε=1)
```

**Step 4: Apply Case 1**
```
T(n) = Θ(n²) ✓
```

---

### Example 2: T(n) = T(2n/3) + 1

**Step 1: Parameters**
```
a = 1, b = 3/2, f(n) = 1
```

**Step 2: Watershed**
```
n^(log_b a) = n^(log₃/₂ 1) = n^0 = 1
```

**Step 3: Compare**
```
f(n) = 1
n^(log_b a) = 1

Equal! (k=0)
```

**Step 4: Apply Case 2**
```
T(n) = Θ(1 × lg n) = Θ(lg n) ✓
```

---

### Example 3: T(n) = 3T(n/4) + n lg n

**Step 1: Parameters**
```
a = 3, b = 4, f(n) = n lg n
```

**Step 2: Watershed**
```
n^(log_b a) = n^(log₄ 3)

log₄ 3 = (lg 3)/(lg 4) = 1.585/2 ≈ 0.793
```

**Step 3: Compare**
```
f(n) = n lg n
n^(log_b a) ≈ n^0.793

n lg n > n^0.793 (polynomially, ε≈0.2)
```

**Step 4: Check regularity**
```
af(n/b) = 3(n/4)lg(n/4)
        = (3n/4)(lg n - 2)
        ≤ (3/4)n lg n  [for large n]
        = cf(n) with c = 3/4 < 1 ✓
```

**Step 5: Apply Case 3**
```
T(n) = Θ(n lg n) ✓
```

---

### Example 4: T(n) = 2T(n/2) + n lg n

**Step 1: Parameters**
```
a = 2, b = 2, f(n) = n lg n
```

**Step 2: Watershed**
```
n^(log_b a) = n^(log₂ 2) = n
```

**Step 3: Compare**
```
f(n) = n lg n = n × (lg n)^1
n^(log_b a) = n

Same rate with k=1!
```

**Step 4: Apply Case 2**
```
T(n) = Θ(n × (lg n)^(1+1))
     = Θ(n lg² n) ✓
```

---

## 📋 Famous Recurrences

### Merge Sort
```
T(n) = 2T(n/2) + Θ(n)

a=2, b=2, f(n)=n
n^(log₂ 2) = n
Case 2 (k=0)

Solution: T(n) = Θ(n lg n) ✓
```

### Binary Search
```
T(n) = T(n/2) + Θ(1)

a=1, b=2, f(n)=1
n^(log₂ 1) = 1
Case 2 (k=0)

Solution: T(n) = Θ(lg n) ✓
```

### Naive Matrix Multiplication
```
T(n) = 8T(n/2) + Θ(n²)

a=8, b=2, f(n)=n²
n^(log₂ 8) = n³
Case 1 (f(n) < n³)

Solution: T(n) = Θ(n³) ✓
```

### Strassen's Algorithm
```
T(n) = 7T(n/2) + Θ(n²)

a=7, b=2, f(n)=n²
n^(log₂ 7) ≈ n^2.807
Case 1 (f(n) < n^2.807)

Solution: T(n) = Θ(n^2.807) ✓
```

---

## ⚠️ When Master Method Doesn't Apply

### Gap Cases

**Example 1:** T(n) = 2T(n/2) + n/lg n
```
a=2, b=2, f(n)=n/lg n
n^(log_b a) = n

f(n) = n/lg n = o(n) but not O(n^(1-ε))
Falls in gap between Case 1 and Case 2!

Master Method doesn't apply ✗
Actual solution: Θ(n lg lg n)
```

**Example 2:** T(n) = 2T(n/2) + n lg² n
```
a=2, b=2, f(n)=n lg² n
n^(log_b a) = n

f(n) = n lg² n = ω(n) but not Ω(n^(1+ε))
Falls in gap between Case 2 and Case 3!

Master Method doesn't apply ✗
Actual solution: Θ(n lg³ n)
```

---

### Regularity Failures

**Example:** T(n) = T(n/2) + 2^(⌈lg n⌉)
```
f(n) = 2^(⌈lg n⌉) oscillates
Doesn't satisfy regularity condition

Master Method Case 3 doesn't apply ✗
```

---

### Non-Master Recurrences

**These don't fit the form T(n) = aT(n/b) + f(n):**
```
T(n) = T(n-1) + n  [linear decrease]
T(n) = T(√n) + 1   [different reduction]
T(n) = T(n/2) + T(n/3) + n  [multiple different sizes]
```

---

## 🧮 Quick Reference Table

| a | b | n^(log_b a) | Common f(n) | Case | Solution |
|---|---|-------------|-------------|------|----------|
| 1 | 2 | 1 | 1 | 2 | Θ(lg n) |
| 2 | 2 | n | n | 2 | Θ(n lg n) |
| 4 | 2 | n² | n | 1 | Θ(n²) |
| 8 | 2 | n³ | n² | 1 | Θ(n³) |
| 7 | 2 | n^2.807 | n² | 1 | Θ(n^2.807) |
| 2 | 4 | √n | n | 3 | Θ(n) |
| 3 | 4 | n^0.793 | n | 3 | Θ(n) |

---

## 💪 Decision Tree

```
Given: T(n) = aT(n/b) + f(n)

Step 1: Calculate n^(log_b a)

Step 2: Compare f(n) with n^(log_b a)

┌─ f(n) << n^(log_b a) (polynomially)?
│  └─ YES → Case 1 → T(n) = Θ(n^(log_b a))
│
├─ f(n) ≈ n^(log_b a) × (lg n)^k?
│  └─ YES → Case 2 → T(n) = Θ(n^(log_b a) × (lg n)^(k+1))
│
└─ f(n) >> n^(log_b a) (polynomially)?
   ├─ Check regularity: af(n/b) ≤ cf(n)?
   │  ├─ YES → Case 3 → T(n) = Θ(f(n))
   │  └─ NO → Master Method doesn't apply
   │
   └─ NO polynomial separation → Gap → Master Method doesn't apply
```

---

## 🚀 Exam Strategy

### Before Applying
- [ ] Verify recurrence fits form T(n) = aT(n/b) + f(n)
- [ ] Identify a, b, f(n) clearly
- [ ] Calculate n^(log_b a) correctly

### While Solving
- [ ] Compare f(n) with n^(log_b a)
- [ ] Check for polynomial separation
- [ ] If Case 3, verify regularity
- [ ] Apply correct formula

### Common Mistakes to Avoid
- [ ] Don't forget regularity in Case 3
- [ ] Don't confuse logarithmic and polynomial differences
- [ ] Don't use wrong logarithm base
- [ ] Don't apply when recurrence doesn't fit form

### Time Management
- Identify case: 1-2 min
- Calculate: 2-3 min
- Verify: 1-2 min
- Total: 4-7 min per problem

---

**You're ready to master the Master Method! 🎉**

---

**End of Guide**
