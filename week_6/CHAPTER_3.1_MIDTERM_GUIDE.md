# Chapter 3.1 Midterm Guide: Characterizing Running Times

**Course:** CS3112 - Introduction to Algorithms  
**Topic:** O, Ω, Θ Notation - Intuitive Understanding  
**Purpose:** Master informal asymptotic analysis for midterm

---

## 🎯 Core Mental Model: What Chapter 3.1 Is Really About

### The Big Picture
Chapter 3.1 introduces **informal, intuitive understanding** of asymptotic notation BEFORE the formal definitions in 3.2.

**Key difference from 3.2:**
- **3.1:** Intuitive, practical understanding ("grows no faster than", "grows at least as fast")
- **3.2:** Formal mathematical definitions (∃c, n₀, inequalities)

**Think of it as:**
- 3.1 = Learning to drive (intuition, feel)
- 3.2 = Driver's manual (formal rules, laws)

---

## 📊 The Three Notations: Intuitive Understanding

### O-notation: Upper Bound

**Intuition:** "Grows **no faster than**"

**What it means:**
- O(n³) means the function grows no faster than n³
- It's an **upper bound** on growth rate
- Like saying "the speed limit is 65 mph" (could be slower, but not faster)

**Example: 7n³ + 100n² - 20n + 6**

**Highest-order term:** 7n³

**What we can say:**
```
✓ This function is O(n³)   [grows no faster than n³]
✓ This function is O(n⁴)   [also grows no faster than n⁴]
✓ This function is O(n⁵)   [also grows no faster than n⁵]
✓ Generally: O(nᶜ) for any c ≥ 3
```

**Why O(n⁴) is also correct:**
- If something grows no faster than n³, it also grows no faster than n⁴
- Like saying "I'm under 30 years old" when you're 25 (true, but not tight)

**Key insight:** O gives an upper bound, but not necessarily the tightest one.

---

### Ω-notation: Lower Bound

**Intuition:** "Grows **at least as fast as**"

**What it means:**
- Ω(n³) means the function grows at least as fast as n³
- It's a **lower bound** on growth rate
- Like saying "minimum wage is $15/hour" (could be more, but not less)

**Example: 7n³ + 100n² - 20n + 6**

**Highest-order term:** 7n³

**What we can say:**
```
✓ This function is Ω(n³)   [grows at least as fast as n³]
✓ This function is Ω(n²)   [also grows at least as fast as n²]
✓ This function is Ω(n)    [also grows at least as fast as n]
✓ Generally: Ω(nᶜ) for any c ≤ 3
```

**Why Ω(n²) is also correct:**
- If something grows at least as fast as n³, it also grows at least as fast as n²
- Like saying "I'm over 20 years old" when you're 25 (true, but not tight)

**Key insight:** Ω gives a lower bound, but not necessarily the tightest one.

---

### Θ-notation: Tight Bound

**Intuition:** "Grows **precisely at** this rate"

**What it means:**
- Θ(n³) means the function grows precisely at rate n³
- It's a **tight bound** on growth rate
- Bounded from above AND below by constant multiples of n³
- Like saying "I'm exactly 25 years old" (precise)

**Example: 7n³ + 100n² - 20n + 6**

**Highest-order term:** 7n³

**What we can say:**
```
✓ This function is Θ(n³)   [grows precisely at rate n³]
✗ This function is NOT Θ(n²)  [grows faster than n²]
✗ This function is NOT Θ(n⁴)  [grows slower than n⁴]
```

**Key relationship:**
```
If f(n) is both O(n³) AND Ω(n³), then f(n) is Θ(n³)
```

**Key insight:** Θ is the most precise characterization - it pins down the exact growth rate.

---

## 🔍 Visual Understanding

### Growth Rate Comparison

```
Function: 7n³ + 100n² - 20n + 6

Upper bounds (O):
    n⁵  ←  grows no faster than this
    n⁴  ←  grows no faster than this
    n³  ←  grows no faster than this (tightest)
    ↑
  [function]
    
Lower bounds (Ω):
    n³  ←  grows at least as fast as this (tightest)
    n²  ←  grows at least as fast as this
    n   ←  grows at least as fast as this
    ↓

Tight bound (Θ):
    n³  ←  grows precisely at this rate
```

---

## 📚 Insertion Sort Analysis: Step-by-Step

### The Algorithm (Recap)

```
INSERTION-SORT(A, n)
1  for i = 2 to n                    [outer loop: n-1 iterations]
2    key = A[i]
3    // Insert A[i] into sorted subarray A[1:i-1]
4    j = i - 1
5    while j > 0 and A[j] > key     [inner loop: variable iterations]
6      A[j+1] = A[j]
7      j = j - 1
8    A[j+1] = key
```

---

### Upper Bound Analysis: O(n²)

**Goal:** Show insertion sort runs in O(n²) time for **all inputs**

**Observations:**
1. Outer loop (line 1): runs exactly n-1 times
2. Inner loop (line 5): runs **at most** i-1 times for iteration i
3. Body of inner loop (lines 6-7): constant time per iteration

**Reasoning:**

**Step 1: Count inner loop iterations**
```
For i = 2: at most 1 iteration
For i = 3: at most 2 iterations
...
For i = n: at most n-1 iterations

Total: at most 1 + 2 + ... + (n-1) = (n-1)n/2 < n²
```

**Step 2: Calculate total time**
```
Each inner loop iteration: constant time c
Total inner loop time: at most c·n²
```

**Step 3: Conclude**
```
Total time ≤ c·n² for some constant c
Therefore: T(n) = O(n²) ✓
```

**Key insight:** We used the **worst case** for the inner loop (i-1 iterations) to establish an upper bound that holds for **all inputs**.

---

### Lower Bound Analysis: Ω(n²)

**Goal:** Show there exists an input where insertion sort takes Ω(n²) time

**Strategy:** Find a "bad" input that forces many operations

**The Bad Input:**

Assume n is a multiple of 3 (for simplicity). Divide array into three parts:
```
[First n/3] [Middle n/3] [Last n/3]
```

**Bad input:** Put the n/3 **largest** values in the **first** n/3 positions.

**What happens:**
1. Each of these n/3 large values must end up in the last n/3 positions
2. To get there, each must pass through the middle n/3 positions
3. Each value moves one position at a time (line 6)

**Counting operations:**

```
Number of large values: n/3
Positions each must pass through: n/3
Operations per value: at least n/3

Total operations: (n/3) × (n/3) = n²/9
```

**Conclusion:**
```
T(n) ≥ c·n² for some constant c = 1/9
Therefore: T(n) = Ω(n²) ✓
```

**Key insight:** We found a **specific input** that forces Ω(n²) operations, proving the lower bound.

---

### Tight Bound: Θ(n²)

**Combining results:**
```
Insertion sort is O(n²)  [upper bound for all inputs]
Insertion sort is Ω(n²)  [lower bound for worst-case input]

Therefore: Insertion sort worst-case is Θ(n²) ✓
```

**Important distinction:**
- **Worst-case** is Θ(n²)
- **Best-case** is Θ(n) (when array already sorted)
- **Average-case** is Θ(n²)

---

## 🎓 Problem-Solving Framework

### Problem Type 1: Modify Lower Bound Argument (3.1-1)

**Pattern:** "Modify the lower-bound argument for..."

**Approach:**
1. Understand the original argument
2. Identify what changes with new constraint
3. Adjust the counting to handle the change
4. Verify the bound still holds

**Key skill:** Adapting proof techniques to new situations

---

### Problem Type 2: Analyze New Algorithm (3.1-2)

**Pattern:** "Analyze the running time of..."

**Approach:**
1. Identify nested loops and their iteration counts
2. Determine what dominates the running time
3. Establish upper bound (O) using worst-case loop iterations
4. Establish lower bound (Ω) by finding a bad input
5. Combine for tight bound (Θ) if possible

**Key skill:** Systematic loop analysis

---

### Problem Type 3: Generalize Argument (3.1-3)

**Pattern:** "Generalize the argument to consider..."

**Approach:**
1. Replace specific values (like n/3) with parameters (like αn)
2. Redo the counting with parameters
3. Determine constraints on parameters
4. Optimize (find maximum/minimum)

**Key skill:** Parameterization and optimization

---

## 💡 How to Approach Each Problem

### Problem 3.1-1: Non-multiple of 3

**What the problem asks:**
Modify the Ω(n²) lower bound argument to work when n is not necessarily a multiple of 3.

**Why this matters:**
- Original argument assumed n divisible by 3 for clean n/3 groups
- Need to handle general n (like n = 10, 11, 100, etc.)
- Shows how to make proofs more general

**Step-by-step approach:**

**Step 1: Understand the original argument**
```
Original: Divide into three groups of size n/3
- First n/3: large values
- Middle n/3: positions to pass through
- Last n/3: final positions

Operations: (n/3) × (n/3) = n²/9
```

**Step 2: Handle general n**

Use **floor function** ⌊n/3⌋ instead of n/3:
```
First ⌊n/3⌋ positions: large values
Middle ⌊n/3⌋ positions: pass through
Last ⌊n/3⌋ positions: final positions
```

**Step 3: Count operations**
```
Number of large values: ⌊n/3⌋
Positions to pass through: ⌊n/3⌋

Operations: ⌊n/3⌋ × ⌊n/3⌋ = ⌊n/3⌋²
```

**Step 4: Show this is still Ω(n²)**

For n ≥ 3:
```
⌊n/3⌋ ≥ n/3 - 1 ≥ n/4  (for large n)

So: ⌊n/3⌋² ≥ (n/4)² = n²/16

Therefore: T(n) ≥ (1/16)n² = Ω(n²) ✓
```

**Key insight:** Floor function reduces size slightly, but still gives Ω(n²) bound.

---

### Problem 3.1-2: Selection Sort Analysis

**What the problem asks:**
Analyze the running time of selection sort using similar reasoning to insertion sort.

**Selection Sort Algorithm (from Exercise 2.2-2):**
```
SELECTION-SORT(A, n)
1  for i = 1 to n-1
2    min_index = i
3    for j = i+1 to n
4      if A[j] < A[min_index]
5        min_index = j
6    swap A[i] with A[min_index]
```

**Step-by-step analysis:**

**Step 1: Identify loop structure**
```
Outer loop (line 1): runs n-1 times
Inner loop (line 3): runs (n-i) times for iteration i
Body (lines 4-5): constant time
Swap (line 6): constant time
```

**Step 2: Upper bound (O)**

Count inner loop iterations:
```
For i = 1: (n-1) iterations
For i = 2: (n-2) iterations
...
For i = n-1: 1 iteration

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)
```

Each iteration takes constant time, so:
```
T(n) = O(n²) ✓
```

**Step 3: Lower bound (Ω)**

**Key observation:** Unlike insertion sort, selection sort **always** runs the inner loop fully!

For **any input**:
```
Inner loop iterations: n(n-1)/2
Each iteration: constant time c

Total time: c·n(n-1)/2 ≥ c·n²/4 for n ≥ 2

Therefore: T(n) = Ω(n²) ✓
```

**Step 4: Tight bound (Θ)**

Since T(n) = O(n²) and T(n) = Ω(n²):
```
T(n) = Θ(n²) ✓
```

**Key insight:** Selection sort is Θ(n²) in **all cases** (best, worst, average) because the inner loop always runs fully!

**Comparison with insertion sort:**
```
Selection sort: Θ(n²) in all cases
Insertion sort: Θ(n) best case, Θ(n²) worst case
```

---

### Problem 3.1-3: Generalized Lower Bound

**What the problem asks:**
Generalize the insertion sort lower bound to use parameter α instead of 1/3, find restrictions on α, and find the α that maximizes operations.

**Step-by-step solution:**

**Step 1: Generalize the argument**

Instead of dividing into thirds (n/3 each), divide using parameter α:
```
First αn positions: large values
Middle (1-2α)n positions: pass through
Last αn positions: final positions
```

**Visual:**
```
[αn large values] [middle (1-2α)n] [αn final positions]
```

**Step 2: Count operations**
```
Number of large values: αn
Positions to pass through: (1-2α)n

Operations: (αn) × (1-2α)n = α(1-2α)n²
```

**Step 3: Find restrictions on α**

For this to make sense, we need:
```
1. α > 0           [need some large values]
2. 1-2α > 0        [need middle section to exist]
   → 2α < 1
   → α < 1/2
3. α < 1           [can't use more than all positions]
```

**Combining:** 0 < α < 1/2

**Step 4: Maximize α(1-2α)n²**

Since n² is constant, maximize f(α) = α(1-2α):
```
f(α) = α - 2α²
f'(α) = 1 - 4α

Set f'(α) = 0:
1 - 4α = 0
α = 1/4
```

**Verify it's a maximum:**
```
f''(α) = -4 < 0  [concave down, so maximum] ✓
```

**Check constraint:** 1/4 < 1/2 ✓

**Step 5: Calculate maximum operations**
```
f(1/4) = (1/4)(1 - 2·1/4) = (1/4)(1/2) = 1/8

Maximum operations: (1/8)n²
```

**Summary:**
- **Restriction:** 0 < α < 1/2
- **Optimal α:** 1/4
- **Maximum operations:** n²/8

**Key insight:** The optimal split is 1/4, 1/2, 1/4 (not 1/3, 1/3, 1/3), giving n²/8 operations instead of n²/9.

---

## 🧮 Key Concepts Summary

### Three Notations at a Glance

| Notation | Meaning | Example | Analogy |
|----------|---------|---------|---------|
| O(n³) | No faster than n³ | 7n³+100n² is O(n³), O(n⁴), O(n⁵) | Speed limit |
| Ω(n³) | At least as fast as n³ | 7n³+100n² is Ω(n³), Ω(n²), Ω(n) | Minimum wage |
| Θ(n³) | Precisely at rate n³ | 7n³+100n² is Θ(n³) only | Exact age |

### Proving Bounds

**Upper bound (O):**
- Analyze worst-case behavior
- Count maximum operations
- Show T(n) ≤ c·f(n)

**Lower bound (Ω):**
- Find a bad input
- Count operations for that input
- Show T(n) ≥ c·f(n)

**Tight bound (Θ):**
- Prove both O and Ω
- Conclude Θ

---

## 🎯 Problem Recognition Guide

### Type 1: Modify Proof
**Keywords:** "modify", "handle", "generalize"  
**Approach:** Adapt original argument, use floor/ceiling if needed

### Type 2: Analyze Algorithm
**Keywords:** "analyze running time", "similar reasoning"  
**Approach:** Count loop iterations, establish O and Ω bounds

### Type 3: Parameterize and Optimize
**Keywords:** "generalize", "what value maximizes"  
**Approach:** Replace constants with parameters, take derivatives

---

## 💪 Quick Self-Test

### Can you answer these?

1. **Is 5n² + 3n = O(n³)?**
   - Yes! Grows no faster than n³

2. **Is 5n² + 3n = Ω(n)?**
   - Yes! Grows at least as fast as n

3. **Is 5n² + 3n = Θ(n²)?**
   - Yes! Grows precisely at rate n²

4. **Why is insertion sort Ω(n²) in worst case?**
   - Bad input forces n²/9 operations

5. **Why is selection sort Θ(n²) in all cases?**
   - Inner loop always runs fully

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Identify if it's O, Ω, or Θ question
- [ ] Determine if it's upper bound, lower bound, or tight bound
- [ ] Recall relevant algorithm or proof technique

### While Solving
- [ ] For O: count worst-case operations
- [ ] For Ω: find bad input
- [ ] For Θ: prove both O and Ω
- [ ] Show your counting clearly

### Common Mistakes
- ❌ Confusing O with Θ (O is upper, Θ is tight)
- ❌ Forgetting to find bad input for Ω
- ❌ Using specific n values instead of general argument
- ❌ Not verifying constraints (like 0 < α < 1/2)

---

## 📋 Essential Facts

### Insertion Sort
```
Best case: Θ(n)    [already sorted]
Worst case: Θ(n²) [reverse sorted]
Average case: Θ(n²)
```

### Selection Sort
```
All cases: Θ(n²)  [always runs inner loop fully]
```

### Relationship
```
f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))
```

---

**You're ready to tackle Chapter 3.1 problems! 🎉**

---

**End of Guide**
