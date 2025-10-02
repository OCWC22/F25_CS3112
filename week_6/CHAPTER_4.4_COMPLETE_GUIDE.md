# Chapter 4.4 Complete Guide: The Recursion-Tree Method

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 4.4 - The Recursion-Tree Method for Solving Recurrences  
**Purpose:** Master visual intuition for solving recurrences

---

## 🎯 What Chapter 4.4 Is Really About

### The Big Picture

Chapter 4.4 teaches you **the recursion-tree method** - a visual technique for understanding and solving recurrences.

**Mental model:** A recursion tree is like a **family tree of subproblems**:
- Each node is a subproblem with its cost
- Children are the recursive calls
- Levels show recursion depth
- Total cost = sum of all nodes

**Why it's important:**
- **Intuition:** Helps you understand WHERE the cost comes from
- **Guessing:** Generates good guesses for substitution method
- **Verification:** Can be used as direct proof (if careful)
- **Visualization:** Makes abstract recurrences concrete

**Key insight:** You don't need to guess blindly - the tree shows you the answer!

---

## 📚 The Recursion-Tree Process

### Step 1: Draw the Tree

**Start with root:**
- Root = original problem of size n
- Cost = non-recursive work at root

**Expand recursively:**
- Each node spawns children based on recurrence
- Continue until base case

**Example: T(n) = 2T(n/2) + n**
```
         n          ← Level 0: 1 node
        / \
      n/2 n/2       ← Level 1: 2 nodes
      / \ / \
    n/4 ... n/4     ← Level 2: 4 nodes
    ...
```

---

### Step 2: Calculate Cost Per Level

**For each level i:**
1. Count number of nodes
2. Determine size of each node
3. Calculate cost per node
4. Sum across the level

**Example: T(n) = 2T(n/2) + n**
```
Level 0: 1 node × n = n
Level 1: 2 nodes × n/2 = n
Level 2: 4 nodes × n/4 = n
Level i: 2^i nodes × n/2^i = n
```

**Pattern:** Every level costs n (constant per level!)

---

### Step 3: Find the Height

**Height = number of levels until base case**

**Common patterns:**
```
Divide by 2: height = lg n
Divide by 3: height = log₃ n
Divide by b: height = log_b n
Subtract 1: height = n
```

**Example: T(n) = 2T(n/2) + n**
- Keep dividing by 2: n → n/2 → n/4 → ... → 1
- Takes lg n steps
- Height = lg n

---

### Step 4: Sum All Levels

**Total cost = Σ (cost at each level)**

**Three common scenarios:**

**1. Decreasing geometric series (r < 1):**
- Root dominates
- Total ≈ cost at root
- Example: T(n) = T(n/2) + n³ → Θ(n³)

**2. Constant per level:**
- All levels equal
- Total = cost per level × height
- Example: T(n) = 2T(n/2) + n → Θ(n lg n)

**3. Increasing geometric series (r > 1):**
- Leaves dominate
- Total ≈ cost at leaves
- Example: T(n) = 4T(n/2) + n → Θ(n²)

---

### Step 5: Verify with Substitution

**Always verify your guess!**
- Tree gives intuition, not rigorous proof
- Use substitution method to confirm
- May need to modify guess slightly

---

## 🎓 Detailed Example 1: T(n) = 3T(n/4) + Θ(n²)

### The Recurrence

```
T(n) = 3T(n/4) + cn²
```

**Parameters:**
- 3 subproblems (branching factor)
- Size n/4 each (reduction factor)
- cn² non-recursive work

---

### Draw the Tree

```
Level 0:                cn²                           Cost: cn²
                      /  |  \
Level 1:        c(n/4)² ... c(n/4)²                   Cost: 3 × c(n/4)² = (3/16)cn²
                (3 nodes)
Level 2:        c(n/16)² ... (9 nodes)                Cost: 9 × c(n/16)² = (9/256)cn²
                
Level 3:        c(n/64)² ... (27 nodes)               Cost: 27 × c(n/64)² = (27/4096)cn²
                
...

Level log₄ n:   Θ(1) ... (3^(log₄ n) nodes)          Cost: Θ(n^(log₄ 3))
```

---

### Calculate Costs

**Level i:**
- Number of nodes: 3^i
- Size per node: n/4^i
- Cost per node: c(n/4^i)²
- **Total cost at level i:** 3^i × c(n²/16^i) = (3/16)^i × cn²

**Pattern:** Each level costs (3/16) of previous level (decreasing!)

---

### Find Height

**Subproblem size at depth i:** n/4^i

**Base case when:** n/4^i = 1
```
4^i = n
i = log₄ n
```

**Height:** log₄ n

---

### Sum All Levels

**Internal nodes:**
```
Total = cn² + (3/16)cn² + (3/16)²cn² + ... + (3/16)^(log₄ n)cn²
      = cn² × Σ(i=0 to log₄ n) (3/16)^i
```

**Geometric series with r = 3/16 < 1:**
```
Σ(i=0 to ∞) (3/16)^i = 1/(1 - 3/16) = 16/13
```

**So:**
```
Total ≤ cn² × 16/13 = (16/13)cn²
```

**Leaves:**
```
Number of leaves: 3^(log₄ n) = n^(log₄ 3)
Cost per leaf: Θ(1)
Total leaf cost: Θ(n^(log₄ 3))
```

**Calculate log₄ 3:**
```
log₄ 3 = lg 3 / lg 4 = 1.585/2 ≈ 0.793 < 1
```

So n^(log₄ 3) < n < n², meaning leaves contribute less than internal nodes.

---

### Make Guess

**From analysis:**
- Internal nodes: O(n²) (geometric series converges)
- Leaves: O(n^0.793) (smaller)
- **Root dominates!**

**Guess:** T(n) = O(n²)

---

### Verify

**Claim:** T(n) ≤ dn² for d ≥ (16/13)c

**Inductive step:**
```
T(n) = 3T(n/4) + cn²
     ≤ 3d(n/4)² + cn²
     = 3d·n²/16 + cn²
     = n²(3d/16 + c)
     ≤ dn²  [if 3d/16 + c ≤ d]
```

**Solve:** c ≤ d - 3d/16 = 13d/16, so d ≥ (16/13)c

**Conclusion:** T(n) = O(n²) ✓

---

## 🎓 Detailed Example 2: T(n) = T(n/3) + T(2n/3) + cn

### The Recurrence (Irregular Tree)

```
T(n) = T(n/3) + T(2n/3) + cn
```

**Key feature:** **Unbalanced** - different subproblem sizes!

---

### Draw the Tree

```
                    cn
                   /  \
                 c(n/3) c(2n/3)
                /  \     /    \
            c(n/9) c(2n/9) c(2n/9) c(4n/9)
            ...
```

**Observation:**
- Left subtree: keeps dividing by 3
- Right subtree: keeps multiplying by 2/3
- Tree is **unbalanced**

---

### Find Height

**Shortest path (left edge):**
- n → n/3 → n/9 → ... → 1
- Height: log₃ n

**Longest path (right edge):**
- n → 2n/3 → 4n/9 → 8n/27 → ...
- Reaches 1 when (2/3)^h × n = 1
- h = log₃/₂ n (larger than log₃ n)

**Tree height:** Θ(lg n) (right edge determines height)

---

### Calculate Cost Per Level

**Key observation:** Each level costs **at most cn**

**Why?**
- At each level, all subproblems together partition the original problem
- Total work per level ≤ cn

**More precisely:**
```
Level 0: cn
Level 1: c(n/3) + c(2n/3) = cn
Level 2: c(n/9) + c(2n/9) + c(2n/9) + c(4n/9) = cn
...
```

**Pattern:** Every level costs exactly cn!

---

### Sum All Levels

**Total cost:**
```
T(n) = cn × (number of levels)
     = cn × Θ(lg n)
     = Θ(n lg n)
```

**Plus leaves:**
- Number of leaves: at most 2^h where h = Θ(lg n)
- But careful analysis shows: Θ(n) leaves
- Cost per leaf: Θ(1)
- Total leaf cost: Θ(n)

**Total:** Θ(n lg n) + Θ(n) = Θ(n lg n)

---

### Make Guess

**Guess:** T(n) = O(n lg n)

**Verification:** Use substitution method (see Exercise 4.4-3)

---

## 💡 Key Patterns in Recursion Trees

### Pattern 1: Root Dominates

**When:** Cost decreases geometrically (r < 1)

**Example:** T(n) = T(n/2) + n³
```
Level 0: n³
Level 1: (n/2)³ = n³/8
Level 2: (n/4)³ = n³/64
...
Ratio: 1/8 < 1 (decreasing!)
```

**Result:** T(n) = Θ(n³) (root cost)

**Recognition:** Single recursive call with large non-recursive cost

---

### Pattern 2: All Levels Equal

**When:** Cost constant per level

**Example:** T(n) = 2T(n/2) + n
```
Level 0: n
Level 1: 2(n/2) = n
Level 2: 4(n/4) = n
...
All levels: n
```

**Result:** T(n) = Θ(n × height) = Θ(n lg n)

**Recognition:** Branching factor = reduction factor

---

### Pattern 3: Leaves Dominate

**When:** Cost increases geometrically (r > 1)

**Example:** T(n) = 4T(n/2) + n
```
Level 0: n
Level 1: 4(n/2) = 2n
Level 2: 16(n/4) = 4n
...
Level lg n: n² (leaves)
Ratio: 2 > 1 (increasing!)
```

**Result:** T(n) = Θ(n²) (leaf cost)

**Recognition:** Branching factor > reduction factor

---

### Pattern 4: Exponential Growth

**When:** Linear decrease with branching

**Example:** T(n) = 3T(n-1) + 1
```
Level 0: 1
Level 1: 3
Level 2: 9
Level 3: 27
...
Level n: 3^n
```

**Result:** T(n) = Θ(3^n)

**Recognition:** T(n-1) with branching factor > 1

---

## 🧮 Essential Formulas

### Geometric Series

**Finite sum:**
```
Σ(i=0 to k) r^i = (r^(k+1) - 1)/(r - 1)
```

**Infinite sum (r < 1):**
```
Σ(i=0 to ∞) r^i = 1/(1 - r)
```

**Key cases:**
```
r < 1: First term dominates, sum ≈ first term / (1-r)
r = 1: All terms equal, sum = k+1
r > 1: Last term dominates, sum ≈ r^k / (r-1)
```

---

### Logarithm Properties

```
log_b n = lg n / lg b
log_b(n^k) = k log_b n
b^(log_b n) = n
n^(log_b a) = a^(log_b n)
```

**Common values:**
```
lg 2 = 1
lg 4 = 2
lg 8 = 3
log₃ 9 = 2
log₄ 16 = 2
```

---

### Tree Height Formulas

```
Divide by b: height = log_b n
Subtract 1: height = n
Subtract k: height = n/k
```

---

## 🎯 Problem-Solving Framework

### Framework for Drawing Trees

**Step 1: Identify parameters**
- Branching factor (a): number of recursive calls
- Reduction factor (b): how much size decreases
- Non-recursive cost: f(n)

**Step 2: Draw first few levels**
- Level 0: 1 node, size n, cost f(n)
- Level 1: a nodes, size n/b each, cost a×f(n/b)
- Level 2: a² nodes, size n/b² each, cost a²×f(n/b²)

**Step 3: Find pattern**
- Level i: a^i nodes, size n/b^i, cost a^i × f(n/b^i)

**Step 4: Determine height**
- When does n/b^i = 1?
- i = log_b n

**Step 5: Sum levels**
- Add up all levels
- Identify which dominates
- Make guess

---

### Framework for Analyzing Costs

**Calculate ratio r:**
```
r = (cost at level i+1) / (cost at level i)
```

**Three cases:**

**Case 1: r < 1 (decreasing)**
- Root dominates
- Guess: Θ(f(n))

**Case 2: r = 1 (constant)**
- All levels equal
- Guess: Θ(f(n) × height)

**Case 3: r > 1 (increasing)**
- Leaves dominate
- Guess: Θ(# of leaves × cost per leaf)

---

## 📊 Complete Examples

### Example 1: T(n) = T(n/2) + n³

**Tree:**
```
Level 0:    n³              Cost: n³
Level 1:    (n/2)³          Cost: n³/8
Level 2:    (n/4)³          Cost: n³/64
...
Height: lg n
```

**Cost pattern:**
```
Ratio: (n³/8) / n³ = 1/8 < 1
Decreasing geometric series!
```

**Sum:**
```
T(n) = n³(1 + 1/8 + 1/64 + ...)
     = n³ × 1/(1 - 1/8)
     = n³ × 8/7
     = Θ(n³)
```

**Guess:** T(n) = O(n³)

**Verification:**
```
T(n) ≤ cn³
T(n) = T(n/2) + n³
     ≤ c(n/2)³ + n³
     = cn³/8 + n³
     = n³(c/8 + 1)
     ≤ cn³  [if c ≥ 8/7]
```

**Result:** T(n) = Θ(n³) ✓

---

### Example 2: T(n) = 4T(n/3) + n

**Tree:**
```
Level 0:    n               Cost: n
Level 1:    4×(n/3)         Cost: 4n/3
Level 2:    16×(n/9)        Cost: 16n/9
Level i:    4^i×(n/3^i)     Cost: n(4/3)^i
Height: log₃ n
```

**Cost pattern:**
```
Ratio: (4n/3) / n = 4/3 > 1
Increasing geometric series!
```

**Sum:**
```
T(n) = n(1 + 4/3 + (4/3)² + ... + (4/3)^(log₃ n))
```

**Last term dominates:**
```
(4/3)^(log₃ n) = n^(log₃(4/3)) = n^(log₃ 4 - 1)

log₃ 4 = lg 4 / lg 3 ≈ 1.262

So: n^(log₃ 4 - 1) = n^0.262
```

**Wait, this doesn't look right. Let's recalculate:**

**Number of leaves:**
```
3^(log₃ n) = n leaves? No!

Actually: 4^(log₃ n) nodes at last level
```

**Better approach - use Master Theorem intuition:**
```
a = 4, b = 3, f(n) = n
n^(log_b a) = n^(log₃ 4) ≈ n^1.262

Since n < n^1.262, leaves dominate
```

**Guess:** T(n) = O(n^(log₃ 4))

**Result:** T(n) = Θ(n^(log₃ 4)) ≈ Θ(n^1.262) ✓

---

### Example 3: T(n) = 4T(n/2) + n

**Tree:**
```
Level 0:    n               Cost: n
Level 1:    4×(n/2)         Cost: 2n
Level 2:    16×(n/4)        Cost: 4n
Level 3:    64×(n/8)        Cost: 8n
Level i:    4^i×(n/2^i)     Cost: 2^i × n
Height: lg n
```

**Cost pattern:**
```
Ratio: 2n / n = 2 > 1
Increasing geometric series!
```

**Sum:**
```
T(n) = n(1 + 2 + 4 + 8 + ... + 2^(lg n))
     = n × (2^(lg n + 1) - 1)
     = n × (2n - 1)
     = 2n² - n
     = Θ(n²)
```

**Guess:** T(n) = O(n²)

**Result:** T(n) = Θ(n²) ✓

---

### Example 4: T(n) = 3T(n-1) + 1

**Tree:**
```
Level 0:    1               Cost: 1
Level 1:    3×1             Cost: 3
Level 2:    9×1             Cost: 9
Level 3:    27×1            Cost: 27
Level i:    3^i             Cost: 3^i
Height: n
```

**Sum:**
```
T(n) = 1 + 3 + 9 + ... + 3^(n-1)
     = (3^n - 1)/2
     = Θ(3^n)
```

**Guess:** T(n) = O(3^n)

**Result:** T(n) = Θ(3^n) ✓

---

## 🔑 How to Determine Which Level Dominates

### Quick Test: Calculate Ratio

**Ratio r = (cost at level i+1) / (cost at level i)**

**For T(n) = aT(n/b) + f(n):**
```
Cost at level i: a^i × f(n/b^i)
Cost at level i+1: a^(i+1) × f(n/b^(i+1))

Ratio = a × f(n/b^(i+1)) / f(n/b^i)
```

**If f(n) = n^k:**
```
Ratio = a × (n/b^(i+1))^k / (n/b^i)^k
      = a × (1/b)^k
      = a/b^k
```

**Three cases:**
```
a/b^k < 1: Root dominates → Θ(f(n))
a/b^k = 1: All equal → Θ(f(n) × height)
a/b^k > 1: Leaves dominate → Θ(n^(log_b a))
```

**This is the intuition behind Master Theorem!**

---

## 📋 Common Recurrence Types

### Type 1: Single Recursive Call

**Form:** T(n) = T(n/b) + f(n)

**Tree:** Single path (no branching)

**Height:** log_b n

**Cost:** Dominated by f(n) at root

**Examples:**
```
T(n) = T(n/2) + n³  → Θ(n³)
T(n) = T(n/2) + n   → Θ(n)
T(n) = T(n/2) + 1   → Θ(lg n)
```

---

### Type 2: Binary Split (2 subproblems)

**Form:** T(n) = 2T(n/2) + f(n)

**Tree:** Binary tree

**Height:** lg n

**Cost:** Depends on f(n)

**Examples:**
```
T(n) = 2T(n/2) + 1    → Θ(n)
T(n) = 2T(n/2) + n    → Θ(n lg n)
T(n) = 2T(n/2) + n²   → Θ(n²)
```

---

### Type 3: Multiple Subproblems

**Form:** T(n) = aT(n/b) + f(n)

**Tree:** a-ary tree

**Height:** log_b n

**Cost:** Compare a with b^k (where f(n) = Θ(n^k))

**Examples:**
```
T(n) = 3T(n/4) + n²   → Θ(n²)  [3 < 4²]
T(n) = 4T(n/3) + n    → Θ(n^1.262)  [4 > 3¹]
T(n) = 4T(n/2) + n    → Θ(n²)  [4 > 2¹]
```

---

### Type 4: Unbalanced Trees

**Form:** T(n) = T(αn) + T((1-α)n) + f(n)

**Tree:** Unbalanced binary tree

**Height:** Determined by longer path

**Cost:** Usually Θ(f(n) × height)

**Example:**
```
T(n) = T(n/3) + T(2n/3) + n  → Θ(n lg n)
```

---

### Type 5: Linear Decrease with Branching

**Form:** T(n) = aT(n-1) + f(n)

**Tree:** Very wide, height n

**Cost:** Exponential in n

**Examples:**
```
T(n) = 2T(n-1) + 1   → Θ(2^n)
T(n) = 3T(n-1) + 1   → Θ(3^n)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Number of Nodes

```
✗ "Level i has i nodes"
✓ Level i has a^i nodes (a = branching factor)
```

### Mistake 2: Wrong Cost Calculation

```
✗ "Cost at level i is f(i)"
✓ Cost at level i is a^i × f(n/b^i)
```

### Mistake 3: Forgetting Leaves

```
✗ Only sum internal nodes
✓ Include leaf costs (can dominate!)
```

### Mistake 4: Wrong Height

```
✗ "Height is n for T(n) = 2T(n/2)"
✓ Height is lg n (divide by 2)
```

### Mistake 5: Not Verifying

```
✗ "Tree gives answer, done!"
✓ Always verify with substitution method
```

---

## 🚀 Exam Strategy

### For Drawing Trees
- [ ] Identify a (branching) and b (reduction)
- [ ] Draw first 3-4 levels
- [ ] Calculate cost per level
- [ ] Find pattern

### For Analyzing
- [ ] Calculate ratio between levels
- [ ] Determine which dominates
- [ ] Sum appropriately
- [ ] Make guess

### For Verifying
- [ ] Use substitution method
- [ ] May need modified guess
- [ ] Check base case

### Time Management
- Draw tree: 5-10 min
- Analyze: 5-10 min
- Verify: 10-15 min
- Total: 20-35 min per problem

---

**You're ready to master recursion trees! 🎉**

---

**End of Guide**
