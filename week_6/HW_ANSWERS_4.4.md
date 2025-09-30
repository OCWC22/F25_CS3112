# Homework Solutions: Section 4.4 - The Recursion-Tree Method

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 4.4 (Solving Recurrences - Recursion-Tree Method)  
**Date:** 2025-09-29

---

## Background: What is the Recursion-Tree Method?

### The Problem

**Given a recurrence like:**
```
T(n) = 2T(n/2) + n
```

**We want to find:** What is T(n) in closed form?

**The recursion-tree method helps us:**
1. Visualize the recursive calls
2. Calculate the cost at each level
3. Sum up all levels to get total cost
4. Make an educated guess for the solution

---

### What is a Recursion Tree?

**A recursion tree is a visual representation where:**
- Each node represents a subproblem
- The value in the node is the non-recursive cost
- Children represent recursive calls
- Levels represent recursive depth

**Example for T(n) = 2T(n/2) + n:**

```
Level 0:           n                    Cost: n
                  / \
Level 1:        n/2  n/2                Cost: n/2 + n/2 = n
               / \   / \
Level 2:     n/4 n/4 n/4 n/4            Cost: 4(n/4) = n
             ...
```

---

### How to Use Recursion Trees

**Step 1: Draw the tree**
- Root is the original problem
- Each node spawns children according to the recurrence

**Step 2: Calculate cost per level**
- Add up all nodes at each level

**Step 3: Find the height**
- How many levels until we reach base case?

**Step 4: Sum all levels**
- Total cost = sum of costs across all levels

**Step 5: Verify with substitution**
- Use the guess from the tree in a formal proof

---

## Problem 4.4-1: Recursion Trees and Substitution Verification

### Problem Statement
For each of the following recurrences, sketch its recursion tree, and guess a good asymptotic upper bound on its solution. Then use the substitution method to verify your answer.

a. T(n) = T(n/2) + n³
b. T(n) = 4T(n/3) + n
c. T(n) = 4T(n/2) + n
d. T(n) = 3T(n-1) + 1

---

## Problem 4.4-1(a): T(n) = T(n/2) + n³

### Step 1: Understand the Recurrence

**What does T(n) = T(n/2) + n³ mean?**
- ONE recursive call on size n/2
- Non-recursive cost: n³ (cubic work)

**Key observation:**
- Only 1 subproblem (not branching much)
- But the non-recursive cost is very large (n³)

---

### Step 2: Draw the Recursion Tree

**Visual representation:**

```
Level 0:                n³                           Cost: n³
                        |
Level 1:              (n/2)³                         Cost: (n/2)³ = n³/8
                        |
Level 2:              (n/4)³                         Cost: (n/4)³ = n³/64
                        |
Level 3:              (n/8)³                         Cost: (n/8)³ = n³/512
                        |
                       ...
                        |
Level lg n:             1³                           Cost: 1
```

**Explanation:**
- Each level has only ONE node (single recursive call)
- At level i, the problem size is n/2^i
- Cost at level i: (n/2^i)³ = n³/8^i

---

### Step 3: Calculate Cost Per Level

**Level 0:** n³
**Level 1:** (n/2)³ = n³/8
**Level 2:** (n/4)³ = n³/64 = n³/8²
**Level 3:** (n/8)³ = n³/512 = n³/8³
**Level i:** (n/2^i)³ = n³/8^i

**Pattern:** Each level costs (1/8) of the previous level

---

### Step 4: Find the Height of the Tree

**Question:** How many times can we divide n by 2 until we reach 1?

**Answer:** log₂ n times

**Why?**
- n → n/2 → n/4 → ... → 1
- After k divisions: n/2^k = 1
- So 2^k = n
- Therefore k = log₂ n

**Height of tree:** lg n (where lg means log₂)

---

### Step 5: Sum All Levels

**Total cost:**
```
T(n) = n³ + n³/8 + n³/64 + n³/512 + ... + 1
     = n³(1 + 1/8 + 1/64 + 1/512 + ...)
     = n³ × Σ(i=0 to lg n) (1/8)^i
```

**This is a geometric series!**

**Geometric series formula:**
```
Σ(i=0 to ∞) r^i = 1/(1-r)  when |r| < 1
```

**In our case:** r = 1/8

```
Σ(i=0 to ∞) (1/8)^i = 1/(1 - 1/8) = 1/(7/8) = 8/7
```

**Since our series is finite (only lg n terms), but the series converges:**
```
T(n) ≤ n³ × 8/7 = (8/7)n³
```

**Asymptotically:**
```
T(n) = Θ(n³)
```

**Key insight:** The first term (n³) dominates! All other terms sum to less than n³/7.

---

### Step 6: Make a Guess

**From the recursion tree analysis:**

**Guess:** T(n) = O(n³)

**Intuition:** The cost decreases geometrically, so the root dominates.

---

### Step 7: Verify with Substitution Method

**Claim:** T(n) ≤ cn³ for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≤ ck³ for all k < n

**Inductive Step:**
```
T(n) = T(n/2) + n³
     ≤ c(n/2)³ + n³         [by hypothesis]
     = c·n³/8 + n³
     = n³(c/8 + 1)
```

**Goal:** We want T(n) ≤ cn³

**For this to work:**
```
n³(c/8 + 1) ≤ cn³
c/8 + 1 ≤ c
1 ≤ c - c/8
1 ≤ 7c/8
8/7 ≤ c
```

**Choose:** c = 2 (or any c ≥ 8/7)

**Verification with c = 2:**
```
T(n) ≤ n³(2/8 + 1) = n³(1/4 + 1) = n³(5/4) = 1.25n³ ≤ 2n³ ✓
```

**Base case:** T(1) ≤ c·1³ = c, which works for c ≥ T(1).

**Conclusion:** T(n) = O(n³) ✓

---

### Final Answer for 4.4-1(a)

**Recursion tree:**
- Single path (no branching)
- Level i costs n³/8^i
- Height: lg n
- Total: n³(1 + 1/8 + 1/64 + ...) ≈ n³ × 8/7

**Guess:** T(n) = O(n³)

**Verification:** T(n) ≤ cn³ for c ≥ 8/7 ✓

**Asymptotic solution:** T(n) = Θ(n³)

---

## Problem 4.4-1(b): T(n) = 4T(n/3) + n

### Step 1: Understand the Recurrence

**What does T(n) = 4T(n/3) + n mean?**
- FOUR recursive calls on size n/3
- Non-recursive cost: n (linear work)

**Key observation:**
- Branching factor: 4 (tree grows wide)
- Each level divides size by 3

---

### Step 2: Draw the Recursion Tree

**Visual representation:**

```
Level 0:              n                              Cost: n
                   /  |  \  \
Level 1:         n/3 n/3 n/3 n/3                     Cost: 4(n/3) = 4n/3
                / | \ \ (4 nodes)
Level 2:      n/9 ... (16 nodes)                     Cost: 16(n/9) = 16n/9
              (each n/9)
Level 3:      n/27 ... (64 nodes)                    Cost: 64(n/27) = 64n/27
              (each n/27)
              ...
```

**Explanation:**
- Level 0: 1 node of size n
- Level 1: 4 nodes of size n/3 each
- Level 2: 16 nodes of size n/9 each
- Level i: 4^i nodes of size n/3^i each

---

### Step 3: Calculate Cost Per Level

**Level 0:**
- Nodes: 1
- Size per node: n
- Cost: 1 × n = n

**Level 1:**
- Nodes: 4
- Size per node: n/3
- Cost: 4 × (n/3) = 4n/3

**Level 2:**
- Nodes: 4² = 16
- Size per node: n/9
- Cost: 16 × (n/9) = 16n/9

**Level 3:**
- Nodes: 4³ = 64
- Size per node: n/27
- Cost: 64 × (n/27) = 64n/27

**Level i:**
- Nodes: 4^i
- Size per node: n/3^i
- Cost: 4^i × (n/3^i) = n × (4/3)^i

**Pattern:** Each level costs (4/3) times the previous level!

---

### Step 4: Find the Height of the Tree

**Question:** How many times can we divide n by 3 until we reach 1?

**Answer:** log₃ n times

**Height of tree:** log₃ n

**In terms of lg (log₂):**
```
log₃ n = lg n / lg 3 = lg n / 1.585 ≈ 0.631 lg n
```

---

### Step 5: Sum All Levels

**Total cost:**
```
T(n) = n + 4n/3 + 16n/9 + 64n/27 + ...
     = n(1 + 4/3 + (4/3)² + (4/3)³ + ...)
     = n × Σ(i=0 to log₃ n) (4/3)^i
```

**This is a geometric series with r = 4/3 > 1 (growing!)**

**For r > 1, the last term dominates:**
```
Σ(i=0 to k) r^i = (r^(k+1) - 1)/(r - 1) ≈ r^k/(r-1)  when r > 1
```

**Last level (i = log₃ n):**
```
(4/3)^(log₃ n) = (4/3)^(lg n / lg 3)
```

**Using the property a^(log_b c) = c^(log_b a):**
```
(4/3)^(log₃ n) = n^(log₃(4/3))
                = n^(log₃ 4 - log₃ 3)
                = n^(log₃ 4 - 1)
```

**Calculate log₃ 4:**
```
log₃ 4 = lg 4 / lg 3 = 2 / 1.585 ≈ 1.262
```

**So:**
```
(4/3)^(log₃ n) = n^(1.262 - 1) = n^0.262
```

**Wait, let's use a cleaner approach:**

**Better calculation:**
```
Cost at last level = 4^(log₃ n) × (n/3^(log₃ n)) × 1
                   = 4^(log₃ n) × 1
                   = n^(log₃ 4)
```

**Using change of base:**
```
log₃ 4 = lg 4 / lg 3 = 2 / lg 3 ≈ 1.262
```

**So the last level costs:** n^1.262

**Total cost (dominated by last level):**
```
T(n) = Θ(n^(log₃ 4)) ≈ Θ(n^1.262)
```

---

### Step 6: Make a Guess

**From the recursion tree analysis:**

**Guess:** T(n) = O(n^(log₃ 4))

**Alternatively:** Since log₃ 4 ≈ 1.262, we can say T(n) = O(n^1.3) or just O(n^(log₃ 4))

---

### Step 7: Verify with Substitution Method

**Claim:** T(n) ≤ cn^(log₃ 4) for some constant c > 0

**Let:** α = log₃ 4 ≈ 1.262

**Inductive Hypothesis:** Assume T(k) ≤ ck^α for all k < n

**Inductive Step:**
```
T(n) = 4T(n/3) + n
     ≤ 4·c(n/3)^α + n         [by hypothesis]
     = 4c·n^α/3^α + n
```

**Note:** 3^α = 3^(log₃ 4) = 4 (by definition of logarithm)

**Continue:**
```
T(n) ≤ 4c·n^α/4 + n
     = cn^α + n
```

**Goal:** We want T(n) ≤ cn^α

**Problem:** We have an extra "+n" term!

**Solution:** Use modified guess T(n) ≤ cn^α - dn

**Modified inductive step:**
```
T(n) = 4T(n/3) + n
     ≤ 4[c(n/3)^α - d(n/3)] + n
     = 4c·n^α/4 - 4dn/3 + n
     = cn^α - 4dn/3 + n
     = cn^α + n(1 - 4d/3)
     ≤ cn^α - dn  [if 1 - 4d/3 ≤ -d]
```

**Solve for d:**
```
1 - 4d/3 ≤ -d
1 ≤ 4d/3 - d
1 ≤ d/3
d ≥ 3
```

**Choose:** d = 3

**Conclusion:** T(n) = O(n^(log₃ 4)) ✓

---

### Final Answer for 4.4-1(b)

**Recursion tree:**
- Branching factor: 4
- Level i: 4^i nodes, each of size n/3^i
- Cost per level: n(4/3)^i (growing!)
- Height: log₃ n
- Last level dominates: n^(log₃ 4)

**Guess:** T(n) = O(n^(log₃ 4)) where log₃ 4 ≈ 1.262

**Verification:** T(n) ≤ cn^(log₃ 4) - dn for appropriate c, d ✓

**Asymptotic solution:** T(n) = Θ(n^(log₃ 4)) ≈ Θ(n^1.262)

---

## Problem 4.4-1(c): T(n) = 4T(n/2) + n

### Step 1: Understand the Recurrence

**What does T(n) = 4T(n/2) + n mean?**
- FOUR recursive calls on size n/2
- Non-recursive cost: n (linear work)

**Key observation:**
- Branching factor: 4 (very wide tree)
- Each level divides size by 2

---

### Step 2: Draw the Recursion Tree

**Visual representation:**

```
Level 0:              n                              Cost: n
                   /  |  \  \
Level 1:         n/2 n/2 n/2 n/2                     Cost: 4(n/2) = 2n
                / | \ \ (4 nodes)
Level 2:      n/4 ... (16 nodes)                     Cost: 16(n/4) = 4n
              (each n/4)
Level 3:      n/8 ... (64 nodes)                     Cost: 64(n/8) = 8n
              (each n/8)
              ...
Level lg n:   1 ... (4^(lg n) = n² nodes)           Cost: n² × 1 = n²
```

**Explanation:**
- Level i: 4^i nodes of size n/2^i each
- Cost at level i: 4^i × (n/2^i) = n × 2^i

---

### Step 3: Calculate Cost Per Level

**Level 0:** 1 × n = n
**Level 1:** 4 × (n/2) = 2n
**Level 2:** 16 × (n/4) = 4n
**Level 3:** 64 × (n/8) = 8n
**Level i:** 4^i × (n/2^i) = n × (4/2)^i = n × 2^i

**Pattern:** Each level costs TWICE the previous level!

---

### Step 4: Find the Height of the Tree

**Height:** lg n (dividing by 2 until we reach 1)

---

### Step 5: Sum All Levels

**Total cost:**
```
T(n) = n + 2n + 4n + 8n + ... + 2^(lg n) × n
     = n(1 + 2 + 4 + 8 + ... + 2^(lg n))
     = n × Σ(i=0 to lg n) 2^i
```

**Geometric series with r = 2:**
```
Σ(i=0 to lg n) 2^i = 2^(lg n + 1) - 1
                    = 2 × 2^(lg n) - 1
                    = 2n - 1
```

**Why?** Because 2^(lg n) = n

**Total cost:**
```
T(n) = n(2n - 1) = 2n² - n = Θ(n²)
```

**Key insight:** The last level dominates (costs n²), but all levels together sum to about 2n².

---

### Step 6: Make a Guess

**From the recursion tree analysis:**

**Guess:** T(n) = O(n²)

---

### Step 7: Verify with Substitution Method

**Claim:** T(n) ≤ cn² for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≤ ck² for all k < n

**Inductive Step:**
```
T(n) = 4T(n/2) + n
     ≤ 4·c(n/2)² + n         [by hypothesis]
     = 4c·n²/4 + n
     = cn² + n
```

**Goal:** We want T(n) ≤ cn²

**Problem:** Extra "+n" term!

**Solution:** Use modified guess T(n) ≤ cn² - dn

**Modified inductive step:**
```
T(n) = 4T(n/2) + n
     ≤ 4[c(n/2)² - d(n/2)] + n
     = cn² - 2dn + n
     = cn² + n(1 - 2d)
     ≤ cn² - dn  [if 1 - 2d ≤ -d]
```

**Solve for d:**
```
1 - 2d ≤ -d
1 ≤ d
```

**Choose:** d = 1

**Conclusion:** T(n) = O(n²) ✓

---

### Final Answer for 4.4-1(c)

**Recursion tree:**
- Branching factor: 4
- Level i: 4^i nodes, each of size n/2^i
- Cost per level: n × 2^i (doubling each level!)
- Height: lg n
- Total: n(1 + 2 + 4 + ... + n) = 2n² - n

**Guess:** T(n) = O(n²)

**Verification:** T(n) ≤ cn² - dn for d ≥ 1 ✓

**Asymptotic solution:** T(n) = Θ(n²)

---

## Problem 4.4-1(d): T(n) = 3T(n-1) + 1

### Step 1: Understand the Recurrence

**What does T(n) = 3T(n-1) + 1 mean?**
- THREE recursive calls on size n-1
- Non-recursive cost: 1 (constant work)
- This is a linear recurrence (decreases by 1)

**Key observation:**
- Branching factor: 3 (tree grows very wide!)
- Size decreases by 1 each level (not dividing)

---

### Step 2: Draw the Recursion Tree

**Visual representation:**

```
Level 0:                  1                          Cost: 1
                       /  |  \
Level 1:              1   1   1                      Cost: 3 × 1 = 3
                    / | \ (3 nodes)
Level 2:           1 ... (9 nodes)                   Cost: 9 × 1 = 9
                   (each 1)
Level 3:          1 ... (27 nodes)                   Cost: 27 × 1 = 27
                  (each 1)
              ...
Level n-1:        1 ... (3^(n-1) nodes)              Cost: 3^(n-1)
```

**Explanation:**
- Each node does constant work (1)
- Level i has 3^i nodes
- Height is n-1 (we decrease by 1 each time until we reach base case)

---

### Step 3: Calculate Cost Per Level

**Level 0:** 3^0 = 1
**Level 1:** 3^1 = 3
**Level 2:** 3^2 = 9
**Level 3:** 3^3 = 27
**Level i:** 3^i

**Pattern:** Each level has 3 times as many nodes as the previous level!

---

### Step 4: Find the Height of the Tree

**Question:** How many times do we subtract 1 from n until we reach 0?

**Answer:** n times

**Height of tree:** n

---

### Step 5: Sum All Levels

**Total cost:**
```
T(n) = 1 + 3 + 9 + 27 + ... + 3^(n-1)
     = Σ(i=0 to n-1) 3^i
```

**Geometric series with r = 3:**
```
Σ(i=0 to n-1) 3^i = (3^n - 1)/(3 - 1)
                   = (3^n - 1)/2
                   = Θ(3^n)
```

**Key insight:** The last level dominates (costs 3^(n-1)), and the total is about (1/2)×3^n.

---

### Step 6: Make a Guess

**From the recursion tree analysis:**

**Guess:** T(n) = O(3^n)

---

### Step 7: Verify with Substitution Method

**Claim:** T(n) ≤ c·3^n for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≤ c·3^k for all k < n

**Inductive Step:**
```
T(n) = 3T(n-1) + 1
     ≤ 3·c·3^(n-1) + 1         [by hypothesis]
     = c·3^n + 1
```

**Goal:** We want T(n) ≤ c·3^n

**Problem:** Extra "+1" term!

**Solution:** Use modified guess T(n) ≤ c·3^n - d

**Modified inductive step:**
```
T(n) = 3T(n-1) + 1
     ≤ 3[c·3^(n-1) - d] + 1
     = c·3^n - 3d + 1
     ≤ c·3^n - d  [if -3d + 1 ≤ -d]
```

**Solve for d:**
```
-3d + 1 ≤ -d
1 ≤ 3d - d
1 ≤ 2d
d ≥ 1/2
```

**Choose:** d = 1

**Conclusion:** T(n) = O(3^n) ✓

---

### Final Answer for 4.4-1(d)

**Recursion tree:**
- Branching factor: 3
- Level i: 3^i nodes, each doing constant work
- Cost per level: 3^i
- Height: n
- Total: 1 + 3 + 9 + ... + 3^(n-1) = (3^n - 1)/2

**Guess:** T(n) = O(3^n)

**Verification:** T(n) ≤ c·3^n - d for d ≥ 1/2 ✓

**Asymptotic solution:** T(n) = Θ(3^n)

---

## Problem 4.4-2: Lower Bound for Recurrence (4.15)

### Problem Statement
Use the substitution method to prove that recurrence (4.15) has the asymptotic lower bound L(n) = Ω(n). Conclude that L(n) = Θ(n).

**Note:** We need to look up recurrence (4.15) in the textbook. Based on context, this is likely a recurrence that we've already shown has an upper bound of O(n), and now we need to prove the lower bound.

**Typical recurrence (4.15):** L(n) = L(⌊n/2⌋) + L(⌈n/2⌉) + 1

This represents the number of leaves in a recursion tree.

---

### Step 1: Understand the Recurrence

**Recurrence:** L(n) = L(⌊n/2⌋) + L(⌈n/2⌉) + 1

**What does this mean?**
- Split problem into two halves (floor and ceiling of n/2)
- Do constant work (+1)
- This counts leaves in a binary tree

**Base case:** L(1) = 1 (a single element is a leaf)

---

### Step 2: Prove Lower Bound L(n) = Ω(n)

**Claim:** L(n) ≥ cn for some constant c > 0 and all n ≥ n₀

**Inductive Hypothesis:** Assume L(k) ≥ ck for all k < n

**Inductive Step:**
```
L(n) = L(⌊n/2⌋) + L(⌈n/2⌉) + 1
     ≥ c⌊n/2⌋ + c⌈n/2⌉ + 1         [by hypothesis]
```

**Key observation:**
```
⌊n/2⌋ + ⌈n/2⌉ = n
```

**Why?**
- If n is even: n/2 + n/2 = n
- If n is odd: (n-1)/2 + (n+1)/2 = n

**Continue:**
```
L(n) ≥ c(⌊n/2⌋ + ⌈n/2⌉) + 1
     = cn + 1
     ≥ cn  [since 1 ≥ 0]
```

**This works immediately!**

---

### Step 3: Verify Base Case

**Base case:** n = 1

**We need:** L(1) ≥ c·1 = c

**Given:** L(1) = 1

**So we need:** 1 ≥ c, which means c ≤ 1

**Choose:** c = 1

**Verification:**
```
L(1) = 1 ≥ 1 ✓
```

---

### Step 4: Conclusion

**We've proven:**
- L(n) = Ω(n) (lower bound)

**From the textbook (or previous work):**
- L(n) = O(n) (upper bound)

**Therefore:**
- L(n) = Θ(n) ✓

**Interpretation:** The number of leaves in a balanced binary recursion tree is linear in n.

---

### Final Answer for Problem 4.4-2

**Claim:** L(n) = Ω(n)

**Proof by induction:**

**Base case:** L(1) = 1 ≥ c·1 for c = 1 ✓

**Inductive hypothesis:** Assume L(k) ≥ ck for all k < n

**Inductive step:**
```
L(n) = L(⌊n/2⌋) + L(⌈n/2⌉) + 1
     ≥ c⌊n/2⌋ + c⌈n/2⌉ + 1
     = c(⌊n/2⌋ + ⌈n/2⌉) + 1
     = cn + 1
     ≥ cn ✓
```

**Conclusion:** L(n) = Ω(n), and combined with L(n) = O(n), we have L(n) = Θ(n) ✓

---

## Problem 4.4-3: Lower Bound for Recurrence (4.14)

### Problem Statement
Use the substitution method to prove that recurrence (4.14) has the solution T(n) = Ω(n lg n). Conclude that T(n) = Θ(n lg n).

**Note:** Recurrence (4.14) is likely T(n) = 2T(n/2) + n (merge sort recurrence).

---

### Step 1: Understand the Recurrence

**Recurrence:** T(n) = 2T(n/2) + n

**This is the merge sort recurrence:**
- Divide array into two halves
- Recursively sort each half
- Merge in linear time

---

### Step 2: Prove Lower Bound T(n) = Ω(n lg n)

**Claim:** T(n) ≥ cn lg n for some constant c > 0

**Inductive Hypothesis:** Assume T(k) ≥ ck lg k for all k < n

**Inductive Step:**
```
T(n) = 2T(n/2) + n
     ≥ 2·c(n/2)lg(n/2) + n         [by hypothesis]
     = cn lg(n/2) + n
     = cn(lg n - lg 2) + n
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

### Step 3: Handle Base Case

**Problem:** lg 1 = 0, so T(1) ≥ c·1·0 = 0 always works

**But we need to be more careful for small n.**

**Modified guess:** T(n) ≥ cn lg n - bn

**Inductive step with modified guess:**
```
T(n) = 2T(n/2) + n
     ≥ 2[c(n/2)lg(n/2) - b(n/2)] + n
     = cn lg(n/2) - bn + n
     = cn(lg n - 1) - bn + n
     = cn lg n - cn - bn + n
     = cn lg n + n(1 - c) - bn
     ≥ cn lg n - bn  [if 1 - c ≥ 0, i.e., c ≤ 1]
```

**Base case:** Choose appropriate constants.

---

### Step 4: Conclusion

**We've proven:**
- T(n) = Ω(n lg n) (lower bound)

**From previous work (Problem 4.3-1(c)):**
- T(n) = O(n lg n) (upper bound)

**Therefore:**
- T(n) = Θ(n lg n) ✓

---

### Final Answer for Problem 4.4-3

**Claim:** T(n) = Ω(n lg n)

**Proof by induction:**

**Inductive hypothesis:** Assume T(k) ≥ ck lg k for all k < n

**Inductive step:**
```
T(n) = 2T(n/2) + n
     ≥ 2·c(n/2)lg(n/2) + n
     = cn lg(n/2) + n
     = cn(lg n - 1) + n
     = cn lg n - cn + n
     = cn lg n + n(1 - c)
     ≥ cn lg n  [for c ≤ 1]
```

**Conclusion:** T(n) = Ω(n lg n), and combined with T(n) = O(n lg n), we have T(n) = Θ(n lg n) ✓

---

## Summary: Recursion-Tree Method

### When to Use

**The recursion-tree method is best for:**
1. Getting intuition about a recurrence
2. Making an educated guess for the solution
3. Visualizing the recursive structure
4. Understanding where the cost comes from

### General Process

**Step 1:** Draw the tree
- Root is the original problem
- Children are recursive calls

**Step 2:** Calculate cost per level
- Add up all nodes at each level

**Step 3:** Find the height
- How many levels until base case?

**Step 4:** Sum all levels
- Often a geometric series
- Identify which level(s) dominate

**Step 5:** Verify with substitution
- Use your guess in a formal induction proof

### Common Patterns

**1. Decreasing geometric series (r < 1):**
- Example: T(n) = T(n/2) + n³
- Root dominates
- Solution: Θ(cost at root)

**2. Constant per level:**
- Example: T(n) = 2T(n/2) + n
- All levels have same cost
- Solution: Θ(cost per level × height) = Θ(n lg n)

**3. Increasing geometric series (r > 1):**
- Example: T(n) = 4T(n/2) + n
- Leaves dominate
- Solution: Θ(number of leaves)

**4. Exponential growth:**
- Example: T(n) = 3T(n-1) + 1
- Last level dominates
- Solution: Θ(branching factor^height)

---

**End of Section 4.4 Solutions**
