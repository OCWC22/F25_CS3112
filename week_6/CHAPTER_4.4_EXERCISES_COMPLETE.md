# Chapter 4.4 Exercises: Complete Solutions with Frameworks

**Section:** 4.4 - The Recursion-Tree Method  
**Focus:** Visual analysis and solving recurrences

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Draw and Verify** | "sketch tree", "guess", "verify" | Visualize, guess, prove | Draw tree → calculate costs → sum → verify |
| **Prove Lower Bound** | "prove", "Ω" | Show grows at least as fast | Use induction with ≥ |
| **Prove Tight Bound** | "prove", "Θ" | Show exact growth rate | Prove both O and Ω |
| **Justify Guess** | "justify", "good guess" | Use tree to support claim | Draw tree, analyze pattern |

---

## Exercise 4.4-1: Draw Trees and Verify

### Problem Statement
For each of the following recurrences, sketch its recursion tree, and guess a good asymptotic upper bound on its solution. Then use the substitution method to verify your answer.

a. T(n) = T(n/2) + n³
b. T(n) = 4T(n/3) + n
c. T(n) = 4T(n/2) + n
d. T(n) = 3T(n-1) + 1

---

## Part (a): T(n) = T(n/2) + n³

### What This Problem Is Asking

**Task:** Analyze single recursive call with cubic cost
**Pattern:** Root-dominated (cost decreases geometrically)

### Framework
1. Draw tree (single path)
2. Calculate costs (geometric decrease)
3. Sum (converges to constant × root)
4. Verify with substitution

---

### Solution

**Step 1: Recursion Tree**

```
Level 0:        n³                      Cost: n³
                |
Level 1:        (n/2)³                  Cost: n³/8
                |
Level 2:        (n/4)³                  Cost: n³/64
                |
Level 3:        (n/8)³                  Cost: n³/512
                |
                ...
                |
Level lg n:     1                       Cost: 1

Height: lg n
```

**Pattern:**
- Level i: (n/2^i)³ = n³/8^i
- Ratio: 1/8 < 1 (decreasing!)

---

**Step 2: Sum All Levels**

```
T(n) = n³ + n³/8 + n³/64 + ...
     = n³(1 + 1/8 + 1/64 + ...)
     = n³ × Σ(i=0 to ∞) (1/8)^i
     = n³ × 1/(1 - 1/8)
     = n³ × 8/7
     = Θ(n³)
```

**Guess:** T(n) = O(n³)

---

**Step 3: Verify with Substitution**

**Claim:** T(n) ≤ cn³ for c ≥ 8/7

**Inductive step:**
```
T(n) = T(n/2) + n³
     ≤ c(n/2)³ + n³
     = cn³/8 + n³
     = n³(c/8 + 1)
     ≤ cn³  [if c ≥ 8/7]
```

**Choose c = 2:** 
```
n³(2/8 + 1) = n³(1.25) ≤ 2n³ ✓
```

**Conclusion:** T(n) = Θ(n³) ✓

---

### Key Insights

1. **Single recursive call** → no branching
2. **Cubic cost** >> cost at deeper levels
3. **Root dominates** → answer is Θ(root cost)
4. **Geometric series** with r < 1 converges

---

## Part (b): T(n) = 4T(n/3) + n

### What This Problem Is Asking

**Task:** Analyze 4 subproblems with linear cost
**Pattern:** Leaves-dominated (cost increases geometrically)

### Framework
1. Draw tree (branching factor 4)
2. Calculate costs (geometric increase)
3. Identify leaves dominate
4. Verify with substitution

---

### Solution

**Step 1: Recursion Tree**

```
Level 0:        n                       Cost: n
              / | \ \
Level 1:    n/3 ... (4 nodes)           Cost: 4(n/3) = 4n/3
           / | \ \ 
Level 2:  n/9 ... (16 nodes)            Cost: 16(n/9) = 16n/9
          
Level 3:  n/27 ... (64 nodes)           Cost: 64(n/27) = 64n/27

Level i:  n/3^i ... (4^i nodes)         Cost: 4^i(n/3^i) = n(4/3)^i

Height: log₃ n
```

**Pattern:**
- Level i: n × (4/3)^i
- Ratio: 4/3 > 1 (increasing!)

---

**Step 2: Sum All Levels**

```
T(n) = n(1 + 4/3 + (4/3)² + ... + (4/3)^(log₃ n))
```

**Last term dominates:**
```
Number of leaves: 4^(log₃ n)

Using a^(log_b c) = c^(log_b a):
4^(log₃ n) = n^(log₃ 4)

log₃ 4 = lg 4 / lg 3 = 2 / 1.585 ≈ 1.262
```

**So:**
```
T(n) = Θ(n^(log₃ 4)) ≈ Θ(n^1.262)
```

**Guess:** T(n) = O(n^(log₃ 4))

---

**Step 3: Verify with Substitution**

**Claim:** T(n) ≤ cn^α - dn where α = log₃ 4

**Note:** Need modified guess to absorb +n term

**Inductive step:**
```
T(n) = 4T(n/3) + n
     ≤ 4[c(n/3)^α - d(n/3)] + n
     = 4c·n^α/3^α - 4dn/3 + n
```

**Since 3^α = 3^(log₃ 4) = 4:**
```
T(n) ≤ 4c·n^α/4 - 4dn/3 + n
     = cn^α - 4dn/3 + n
     = cn^α + n(1 - 4d/3)
     ≤ cn^α - dn  [if 1 - 4d/3 ≤ -d]
```

**Solve:** d ≥ 3

**Conclusion:** T(n) = Θ(n^(log₃ 4)) ✓

---

### Key Insights

1. **4 subproblems, divide by 3** → leaves dominate
2. **Ratio 4/3 > 1** → increasing series
3. **Answer:** n^(log₃ 4) ≈ n^1.262
4. **Between linear and quadratic**

---

## Part (c): T(n) = 4T(n/2) + n

### What This Problem Is Asking

**Task:** Analyze 4 subproblems dividing by 2
**Pattern:** Leaves-dominated (cost doubles each level)

### Framework
1. Draw tree (branching 4, divide by 2)
2. Calculate costs (doubling pattern)
3. Sum to n²
4. Verify with modified guess

---

### Solution

**Step 1: Recursion Tree**

```
Level 0:        n                       Cost: n
              / | \ \
Level 1:    n/2 ... (4 nodes)           Cost: 4(n/2) = 2n
           / | \ \
Level 2:  n/4 ... (16 nodes)            Cost: 16(n/4) = 4n

Level 3:  n/8 ... (64 nodes)            Cost: 64(n/8) = 8n

Level i:  n/2^i ... (4^i nodes)         Cost: 4^i(n/2^i) = 2^i × n

Height: lg n
```

**Pattern:**
- Level i: 2^i × n
- Ratio: 2 > 1 (doubling!)

---

**Step 2: Sum All Levels**

```
T(n) = n + 2n + 4n + 8n + ... + 2^(lg n) × n
     = n(1 + 2 + 4 + ... + 2^(lg n))
     = n × (2^(lg n + 1) - 1)
     = n × (2n - 1)
     = 2n² - n
     = Θ(n²)
```

**Guess:** T(n) = O(n²)

---

**Step 3: Verify with Substitution**

**Simple guess T(n) ≤ cn² fails:**
```
T(n) = 4T(n/2) + n
     ≤ 4c(n/2)² + n
     = cn² + n  [extra +n!]
```

**Modified guess T(n) ≤ cn² - dn:**
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n
     = cn² - 2dn + n
     = cn² - dn - (d-1)n
     ≤ cn² - dn  [if d ≥ 1]
```

**Choose d = 1:** Works! ✓

**Conclusion:** T(n) = Θ(n²) ✓

---

### Key Insights

1. **4 subproblems, divide by 2** → 4/2 = 2 > 1
2. **Cost doubles each level**
3. **Leaves:** 4^(lg n) = n² nodes
4. **Total:** 2n² - n ≈ 2n²

---

## Part (d): T(n) = 3T(n-1) + 1

### What This Problem Is Asking

**Task:** Analyze exponential growth recurrence
**Pattern:** Linear decrease with branching → exponential

### Framework
1. Draw tree (3-way branching, height n)
2. Calculate costs (3^i at level i)
3. Sum geometric series
4. Verify exponential bound

---

### Solution

**Step 1: Recursion Tree**

```
Level 0:        1                       Cost: 1
              / | \
Level 1:      1 1 1 (3 nodes)           Cost: 3
            / | \ (each branches 3 ways)
Level 2:    1 ... (9 nodes)             Cost: 9

Level 3:    1 ... (27 nodes)            Cost: 27

Level i:    1 ... (3^i nodes)           Cost: 3^i

Height: n
```

**Pattern:**
- Level i: 3^i nodes
- Each does constant work
- Total at level i: 3^i

---

**Step 2: Sum All Levels**

```
T(n) = 1 + 3 + 9 + 27 + ... + 3^(n-1)
     = Σ(i=0 to n-1) 3^i
     = (3^n - 1)/(3 - 1)
     = (3^n - 1)/2
     = Θ(3^n)
```

**Guess:** T(n) = O(3^n)

---

**Step 3: Verify with Substitution**

**Simple guess T(n) ≤ c·3^n fails:**
```
T(n) = 3T(n-1) + 1
     ≤ 3·c·3^(n-1) + 1
     = c·3^n + 1  [extra +1!]
```

**Modified guess T(n) ≤ c·3^n - d:**
```
T(n) = 3T(n-1) + 1
     ≤ 3[c·3^(n-1) - d] + 1
     = c·3^n - 3d + 1
     ≤ c·3^n - d  [if 3d - 1 ≥ d, i.e., d ≥ 1/2]
```

**Choose d = 1:** Works! ✓

**Conclusion:** T(n) = Θ(3^n) ✓

---

### Key Insights

1. **Linear decrease + branching** → exponential
2. **3 branches, n levels** → 3^n total nodes
3. **Last level dominates:** 3^(n-1) ≈ (1/3)×3^n
4. **Extremely fast growth!**

---

## Exercise 4.4-2: Prove Lower Bound for Leaves

### Problem Statement
Use the substitution method to prove that recurrence (4.15) has the asymptotic lower bound L(n) = Ω(n). Conclude that L(n) = Θ(n).

**Recurrence (4.15):** L(n) = L(n/3) + L(2n/3) + 1 (from textbook context)

**Note:** This counts the number of leaves in an unbalanced tree.

---

### What This Problem Is Asking

**Context:** We've shown L(n) = O(n) (upper bound)
**Task:** Prove L(n) = Ω(n) (lower bound)
**Goal:** Conclude L(n) = Θ(n) (tight bound)

### Framework
1. Set up inductive hypothesis with ≥
2. Apply to both recursive calls
3. Use property: ⌊n/2⌋ + ⌈n/2⌉ = n
4. Show inequality holds

---

### Solution

**Claim:** L(n) ≥ cn for some constant c > 0

**Inductive hypothesis:** Assume L(k) ≥ ck for all k < n

**Inductive step:**
```
L(n) = L(n/3) + L(2n/3) + 1
     ≥ c(n/3) + c(2n/3) + 1
     = cn/3 + 2cn/3 + 1
     = cn + 1
     ≥ cn  [since 1 ≥ 0]
```

**This works immediately!** No need for modifications.

---

**Base case:** L(1) = 1
```
Need: L(1) ≥ c
So: 1 ≥ c
Choose: c = 1
```

**Verification:** L(1) = 1 ≥ 1 ✓

---

**Conclusion:**
- L(n) = Ω(n) (just proved)
- L(n) = O(n) (given or from textbook)
- **Therefore: L(n) = Θ(n)** ✓

---

### Key Insights

1. **Property:** n/3 + 2n/3 = n (subproblems sum to original)
2. **Extra +1** doesn't hurt lower bound (makes it stronger)
3. **Linear number of leaves** in unbalanced binary tree
4. **Simple proof** - no modifications needed

---

## Exercise 4.4-3: Prove Lower Bound for T(n)

### Problem Statement
Use the substitution method to prove that recurrence (4.14) has the solution T(n) = Ω(n lg n). Conclude that T(n) = Θ(n lg n).

**Recurrence (4.14):** T(n) = T(n/3) + T(2n/3) + cn (from textbook)

---

### What This Problem Is Asking

**Context:** Unbalanced tree with linear cost per level
**Task:** Prove lower bound Ω(n lg n)
**Goal:** Combine with upper bound for Θ

### Framework
1. Guess T(n) ≥ cn lg n
2. Apply to both recursive calls
3. Use logarithm properties
4. Show inequality holds

---

### Solution

**Claim:** T(n) ≥ dn lg n for some constant d > 0

**Inductive hypothesis:** Assume T(k) ≥ dk lg k for all k < n

**Inductive step:**
```
T(n) = T(n/3) + T(2n/3) + cn
     ≥ d(n/3)lg(n/3) + d(2n/3)lg(2n/3) + cn
```

**Simplify logarithms:**
```
lg(n/3) = lg n - lg 3
lg(2n/3) = lg 2 + lg n - lg 3 = 1 + lg n - lg 3
```

**Continue:**
```
T(n) ≥ d(n/3)(lg n - lg 3) + d(2n/3)(lg n - lg 3 + 1) + cn
     = d(n/3)lg n - d(n/3)lg 3 + d(2n/3)lg n - d(2n/3)lg 3 + d(2n/3) + cn
     = dn lg n[(1/3) + (2/3)] - dn lg 3 + d(2n/3) + cn
     = dn lg n - dn lg 3 + 2dn/3 + cn
     = dn lg n + n(c + 2d/3 - d lg 3)
```

**Goal:** Show T(n) ≥ dn lg n

**Need:** c + 2d/3 - d lg 3 ≥ 0

**Since lg 3 ≈ 1.585:**
```
c + 2d/3 - 1.585d ≥ 0
c ≥ 1.585d - 2d/3
c ≥ 0.918d
```

**Choose d small enough:** d ≤ c/0.918

**Conclusion:** T(n) = Ω(n lg n) ✓

---

**Combined with upper bound:**
- T(n) = O(n lg n) (from textbook analysis)
- T(n) = Ω(n lg n) (just proved)
- **Therefore: T(n) = Θ(n lg n)** ✓

---

### Key Insights

1. **Unbalanced tree** → different path lengths
2. **Linear cost per level** → n × height = n lg n
3. **Both subproblems contribute** to lower bound
4. **Tight bound:** Θ(n lg n)

---

## Exercise 4.4-4: General Unbalanced Tree

### Problem Statement
Use a recursion tree to justify a good guess for the solution to the recurrence T(n) = T(αn) + T((1-α)n) + Θ(n), where α is a constant in the range 0 < α < 1.

---

### What This Problem Is Asking

**Task:** Analyze general unbalanced binary tree
**Parameter:** α controls the split (α = 1/3 gives T(n/3) + T(2n/3))
**Goal:** Show result is Θ(n lg n) regardless of α

### Framework
1. Draw tree with α and (1-α) branches
2. Find height (determined by longer path)
3. Calculate cost per level (should be cn)
4. Sum to get Θ(n lg n)

---

### Solution

**Step 1: Recursion Tree**

```
Level 0:            cn                      Cost: cn
                   /  \
Level 1:        c(αn) c((1-α)n)             Cost: c(αn + (1-α)n) = cn
               /  \    /  \
Level 2:   c(α²n) ... c((1-α)²n)           Cost: cn
           ...
```

**Key observation:** Each level costs **exactly cn**!

**Why?**
- At each level, subproblems partition the original problem
- Total size at level i: n (distributed among nodes)
- Total cost: cn

---

**Step 2: Find Height**

**Shortest path (smaller α):**
- Follow α repeatedly: n → αn → α²n → ... → 1
- When α^h × n = 1: h = log₁/α n

**Longest path (larger 1-α):**
- Follow (1-α) repeatedly: n → (1-α)n → (1-α)²n → ... → 1
- When (1-α)^h × n = 1: h = log₁/(₁₋α) n

**Height is determined by longer path:**
```
If α < 1/2: (1-α) > α, so right path longer
Height = log₁/(₁₋α) n

If α > 1/2: α > (1-α), so left path longer
Height = log₁/α n

In general: Height = Θ(lg n)
```

**Why Θ(lg n)?**
- For any fixed 0 < α < 1, both log₁/α n and log₁/(₁₋α) n are Θ(lg n)
- Different constants, same asymptotic growth

---

**Step 3: Sum All Levels**

**Total cost:**
```
T(n) = cn × (number of levels)
     = cn × Θ(lg n)
     = Θ(n lg n)
```

**Plus leaves:**
- Number of leaves: O(n) (can be shown by induction)
- Cost per leaf: Θ(1)
- Total leaf cost: Θ(n)

**Total:** Θ(n lg n) + Θ(n) = Θ(n lg n)

---

**Step 4: Make Guess**

**Guess:** T(n) = Θ(n lg n)

**Key insight:** The split ratio α doesn't matter asymptotically!
- As long as 0 < α < 1 (both subproblems shrink)
- Result is always Θ(n lg n)

---

### Verification Sketch

**Upper bound:** T(n) ≤ cn lg n

**Inductive step:**
```
T(n) = T(αn) + T((1-α)n) + dn
     ≤ c(αn)lg(αn) + c((1-α)n)lg((1-α)n) + dn
     = cαn(lg α + lg n) + c(1-α)n(lg(1-α) + lg n) + dn
     = cn lg n + cn[α lg α + (1-α)lg(1-α)] + dn
```

**Since 0 < α < 1:** lg α < 0 and lg(1-α) < 0

**The term:** α lg α + (1-α)lg(1-α) < 0

**So:** cn[α lg α + (1-α)lg(1-α)] is negative

**For large enough c:** This negative term absorbs dn

**Conclusion:** T(n) = O(n lg n) ✓

**Similarly for lower bound:** T(n) = Ω(n lg n) ✓

**Therefore:** T(n) = Θ(n lg n) ✓

---

### Key Insights

1. **Any split 0 < α < 1** gives Θ(n lg n)
2. **Balanced or unbalanced** doesn't matter asymptotically
3. **Cost per level is always cn**
4. **Height is always Θ(lg n)**
5. **Result:** cn × Θ(lg n) = Θ(n lg n)

**Practical implication:** Merge sort is Θ(n lg n) even with unbalanced splits!

---

## 📋 Quick Reference: All Exercises

### 4.4-1(a): T(n) = T(n/2) + n³
```
Tree: Single path, costs n³, n³/8, n³/64, ...
Pattern: Decreasing (r = 1/8)
Sum: n³ × 8/7 = Θ(n³)
Guess: O(n³)
Verify: T(n) ≤ cn³ for c ≥ 8/7
```

### 4.4-1(b): T(n) = 4T(n/3) + n
```
Tree: 4-way branching, divide by 3
Pattern: Increasing (r = 4/3)
Sum: Dominated by leaves
Guess: O(n^(log₃ 4)) ≈ O(n^1.262)
Verify: T(n) ≤ cn^α - dn for d ≥ 3
```

### 4.4-1(c): T(n) = 4T(n/2) + n
```
Tree: 4-way branching, divide by 2
Pattern: Doubling (r = 2)
Sum: n(1 + 2 + 4 + ... + n) = 2n² - n
Guess: O(n²)
Verify: T(n) ≤ cn² - dn for d ≥ 1
```

### 4.4-1(d): T(n) = 3T(n-1) + 1
```
Tree: 3-way branching, height n
Pattern: Exponential
Sum: (3^n - 1)/2 = Θ(3^n)
Guess: O(3^n)
Verify: T(n) ≤ c·3^n - d for d ≥ 1/2
```

### 4.4-2: L(n) = L(n/3) + L(2n/3) + 1
```
Prove: L(n) ≥ cn
Key: n/3 + 2n/3 = n
Result: L(n) = Θ(n)
```

### 4.4-3: T(n) = T(n/3) + T(2n/3) + cn
```
Prove: T(n) ≥ dn lg n
Cost per level: cn
Height: Θ(lg n)
Result: T(n) = Θ(n lg n)
```

### 4.4-4: T(n) = T(αn) + T((1-α)n) + Θ(n)
```
Cost per level: cn (always!)
Height: Θ(lg n) (for any 0 < α < 1)
Result: T(n) = Θ(n lg n)
```

---

## 🔑 Master Pattern Recognition

### Quick Decision Tree

```
T(n) = aT(n/b) + f(n)

Calculate ratio: r = a/b^k where f(n) = Θ(n^k)

r < 1: Root dominates → Θ(f(n))
r = 1: All equal → Θ(f(n) × log_b n)
r > 1: Leaves dominate → Θ(n^(log_b a))
```

### Examples

```
T(n) = T(n/2) + n³:    a=1, b=2, k=3 → r=1/8 < 1 → Θ(n³)
T(n) = 2T(n/2) + n:    a=2, b=2, k=1 → r=2/2 = 1 → Θ(n lg n)
T(n) = 4T(n/2) + n:    a=4, b=2, k=1 → r=4/2 = 2 > 1 → Θ(n²)
T(n) = 4T(n/3) + n:    a=4, b=3, k=1 → r=4/3 > 1 → Θ(n^(log₃ 4))
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Level Count
```
✗ "Level i has i nodes"
✓ Level i has a^i nodes
```

### Mistake 2: Wrong Cost Formula
```
✗ "Cost at level i is f(i)"
✓ Cost at level i is a^i × f(n/b^i)
```

### Mistake 3: Forgetting Leaves
```
✗ Only sum internal nodes
✓ Include leaves (may dominate!)
```

### Mistake 4: Wrong Height
```
✗ "Height is n for T(n/2)"
✓ Height is lg n (divide by 2)
```

### Mistake 5: Not Verifying
```
✗ "Tree shows Θ(n²), done!"
✓ Verify with substitution method
```

### Mistake 6: Wrong Geometric Series
```
✗ "Sum is (r^n - 1)/(r-1) for any r"
✓ Different formulas for r<1, r=1, r>1
```

---

## 🚀 Exam Strategy

### For Drawing Trees
- [ ] Identify a (branching factor)
- [ ] Identify b (reduction factor)
- [ ] Draw first 3-4 levels
- [ ] Label costs clearly
- [ ] Find pattern

### For Analyzing
- [ ] Calculate cost per level
- [ ] Determine ratio r
- [ ] Identify which dominates
- [ ] Sum appropriately

### For Verifying
- [ ] Use guess in substitution
- [ ] May need modified guess
- [ ] Check base case
- [ ] State conclusion

### Time Management
- Draw tree: 5-10 min
- Analyze pattern: 5-10 min
- Sum levels: 5-10 min
- Verify: 10-15 min
- Total: 25-45 min

---

**You're ready to master recursion trees! 🎉**

---

**End of Guide**
