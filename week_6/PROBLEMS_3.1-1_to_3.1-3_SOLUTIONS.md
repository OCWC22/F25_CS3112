# Chapter 3.1 Problems: Complete Step-by-Step Solutions

**Problems:** 3.1-1 through 3.1-3  
**Focus:** Intuitive asymptotic analysis and algorithm characterization

---

## Problem 3.1-1: Non-Multiple of 3 Lower Bound

### Problem Statement
Modify the lower-bound argument for insertion sort to handle input sizes that are not necessarily a multiple of 3.

---

### Understanding the Problem

**Original argument recap:**
- Assumed n is a multiple of 3
- Divided array into three equal parts of size n/3
- Showed n/3 large values must pass through n/3 middle positions
- Concluded (n/3) × (n/3) = n²/9 operations, so Ω(n²)

**The issue:**
- What if n = 10? Then n/3 = 3.333... (not an integer!)
- Can't have 3.333 array positions
- Need to handle arbitrary n

**Why this matters:**
- Real inputs don't always have nice sizes
- Proofs must work for all valid inputs
- Shows how to make arguments more general

---

### Solution

**Claim:** Insertion sort worst-case is Ω(n²) for **all** n ≥ 3, not just multiples of 3.

---

### Approach 1: Using Floor Function

**Step 1: Replace n/3 with ⌊n/3⌋**

Divide array into three parts:
```
First ⌊n/3⌋ positions: A[1 : ⌊n/3⌋]
Middle ⌊n/3⌋ positions: A[⌊n/3⌋+1 : 2⌊n/3⌋]
Last ⌊n/3⌋ positions: A[2⌊n/3⌋+1 : 3⌊n/3⌋]
```

**Note:** 3⌊n/3⌋ ≤ n, so we might not use all positions. That's okay!

**Step 2: Construct bad input**

Place the ⌊n/3⌋ largest values in the first ⌊n/3⌋ positions.

**Step 3: Count operations**

Each of the ⌊n/3⌋ large values must:
- Pass through at least ⌊n/3⌋ middle positions
- Move one position at a time (line 6 of insertion sort)

Total operations:
```
⌊n/3⌋ × ⌊n/3⌋ = ⌊n/3⌋²
```

**Step 4: Show ⌊n/3⌋² = Ω(n²)**

For any n ≥ 3:
```
⌊n/3⌋ ≥ n/3 - 1    [property of floor function]
```

For n ≥ 6:
```
n/3 - 1 ≥ n/6      [since n/3 - 1 ≥ n/6 when n ≥ 6]
```

Therefore:
```
⌊n/3⌋² ≥ (n/6)² = n²/36
```

**Conclusion:**
```
T(n) ≥ (1/36)n² for n ≥ 6

Therefore: T(n) = Ω(n²) ✓
```

**For small n (3 ≤ n < 6):** Can verify directly or use n₀ = 6 in the definition.

---

### Approach 2: Using Ceiling Function

**Alternative:** Use ⌈n/3⌉ for some parts to ensure coverage.

**Step 1: Divide array**
```
First ⌊n/3⌋ positions: large values
Middle ⌊n/3⌋ positions: pass through
Last positions: final destinations
```

**Step 2: Count operations**

Same as Approach 1:
```
⌊n/3⌋² operations
```

**Step 3: Bound from below**

For n ≥ 3:
```
⌊n/3⌋ ≥ (n-2)/3    [since ⌊x⌋ ≥ x-1]
```

So:
```
⌊n/3⌋² ≥ ((n-2)/3)² = (n-2)²/9
```

For large n:
```
(n-2)² = n² - 4n + 4 ≥ n²/2  (for n ≥ 8)
```

Therefore:
```
⌊n/3⌋² ≥ n²/18 for large n

T(n) = Ω(n²) ✓
```

---

### Approach 3: Simplest Argument

**Step 1: Use at least n/4 for each part**

For any n ≥ 12:
```
⌊n/3⌋ ≥ n/4    [since n/3 - 1 ≥ n/4 when n ≥ 12]
```

**Step 2: Count operations**
```
⌊n/3⌋² ≥ (n/4)² = n²/16
```

**Conclusion:**
```
T(n) ≥ (1/16)n² for n ≥ 12

Therefore: T(n) = Ω(n²) ✓
```

**Key insight:** We lose some constant factor (1/16 instead of 1/9), but Ω(n²) still holds!

---

### Verification with Examples

**Example 1: n = 10**
```
⌊10/3⌋ = 3

Operations: 3 × 3 = 9
Compare to n²/16 = 100/16 = 6.25

9 > 6.25 ✓
```

**Example 2: n = 11**
```
⌊11/3⌋ = 3

Operations: 3 × 3 = 9
Compare to n²/16 = 121/16 = 7.56

9 > 7.56 ✓
```

**Example 3: n = 100**
```
⌊100/3⌋ = 33

Operations: 33 × 33 = 1089
Compare to n²/16 = 10000/16 = 625

1089 > 625 ✓
```

---

### Summary

**Original argument:** n²/9 operations (for n divisible by 3)

**Modified argument:** At least n²/16 operations (for all n ≥ 12)

**Key changes:**
- Use ⌊n/3⌋ instead of n/3
- Accept slightly weaker constant (1/16 vs 1/9)
- Still get Ω(n²) bound ✓

**Important lesson:** Asymptotic notation absorbs constant factors, so losing some precision is okay!

---

## Problem 3.1-2: Selection Sort Analysis

### Problem Statement
Using reasoning similar to what we used for insertion sort, analyze the running time of the selection sort algorithm from Exercise 2.2-2.

---

### Understanding the Problem

**What is selection sort?**
- Find the minimum element in unsorted portion
- Swap it with the first unsorted element
- Repeat for remaining unsorted portion

**Algorithm:**
```
SELECTION-SORT(A, n)
1  for i = 1 to n-1
2    min_index = i
3    for j = i+1 to n
4      if A[j] < A[min_index]
5        min_index = j
6    swap A[i] with A[min_index]
```

**Goal:** Characterize running time using O, Ω, Θ notation

---

### Solution

---

### Part 1: Upper Bound Analysis (O)

**Goal:** Show T(n) = O(n²) for all inputs

**Step 1: Identify loop structure**

**Outer loop (line 1):**
- Runs from i = 1 to n-1
- Total iterations: n-1

**Inner loop (line 3):**
- For iteration i, runs from j = i+1 to n
- Total iterations for iteration i: n-i

**Body (lines 4-5):**
- Constant time per iteration: c₁

**Swap (line 6):**
- Constant time: c₂

**Step 2: Count total operations**

Inner loop iterations:
```
For i = 1: (n-1) iterations
For i = 2: (n-2) iterations
For i = 3: (n-3) iterations
...
For i = n-1: 1 iteration

Total: (n-1) + (n-2) + ... + 1 = Σⱼ₌₁ⁿ⁻¹ j = n(n-1)/2
```

**Step 3: Calculate total time**

```
Time for inner loops: c₁ · n(n-1)/2
Time for swaps: c₂ · (n-1)
Total time: c₁ · n(n-1)/2 + c₂ · (n-1)
          = (c₁/2)n² + (c₂ - c₁/2)n - c₂
```

**Step 4: Apply O-notation**

For large n:
```
T(n) ≤ (c₁/2)n² + (c₂ - c₁/2)n ≤ cn² for some c

Therefore: T(n) = O(n²) ✓
```

---

### Part 2: Lower Bound Analysis (Ω)

**Goal:** Show T(n) = Ω(n²)

**Key observation:** Unlike insertion sort, selection sort **always** runs the inner loop fully, regardless of input!

**Step 1: Count operations for ANY input**

For **every** input:
```
Inner loop iterations: n(n-1)/2
Each iteration: constant time c

Total time: c · n(n-1)/2 = (c/2)n² - (c/2)n
```

**Step 2: Bound from below**

For n ≥ 2:
```
T(n) = (c/2)n² - (c/2)n ≥ (c/2)n² - (c/2)n²/2 = (c/4)n²
```

**Step 3: Apply Ω-notation**

```
T(n) ≥ (c/4)n² for all n ≥ 2

Therefore: T(n) = Ω(n²) ✓
```

**Key insight:** We don't need to find a "bad input" because **all inputs** are bad for selection sort!

---

### Part 3: Tight Bound (Θ)

**Combining results:**
```
T(n) = O(n²)  [upper bound for all inputs]
T(n) = Ω(n²)  [lower bound for all inputs]

Therefore: T(n) = Θ(n²) ✓
```

**Important:** This is Θ(n²) in **all cases** (best, worst, average)!

---

### Comparison with Insertion Sort

| Algorithm | Best Case | Worst Case | Average Case |
|-----------|-----------|------------|--------------|
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) |

**Why the difference?**

**Insertion sort:**
- Best case: already sorted, inner loop runs 0 times
- Worst case: reverse sorted, inner loop runs i-1 times

**Selection sort:**
- All cases: inner loop always runs n-i times
- No early termination
- Always scans entire unsorted portion

---

### Detailed Example

**Input: [5, 2, 4, 6, 1, 3]** (n = 6)

**Iteration by iteration:**

```
i = 1: Compare 5 with 2,4,6,1,3 (5 comparisons) → swap 5 and 1
       [1, 2, 4, 6, 5, 3]

i = 2: Compare 2 with 4,6,5,3 (4 comparisons) → no swap
       [1, 2, 4, 6, 5, 3]

i = 3: Compare 4 with 6,5,3 (3 comparisons) → swap 4 and 3
       [1, 2, 3, 6, 5, 4]

i = 4: Compare 6 with 5,4 (2 comparisons) → swap 6 and 4
       [1, 2, 3, 4, 5, 6]

i = 5: Compare 5 with 6 (1 comparison) → no swap
       [1, 2, 3, 4, 5, 6]

Total comparisons: 5 + 4 + 3 + 2 + 1 = 15 = 6(5)/2
```

**Key observation:** Always 15 comparisons for n=6, regardless of input!

---

### Summary

**Selection sort running time:**
```
T(n) = Θ(n²) in all cases
```

**Why?**
- Inner loop always runs fully
- No dependence on input order
- Always n(n-1)/2 comparisons

**Practical implication:**
- Selection sort is predictable (always same time)
- But never fast (always quadratic)
- Insertion sort can be much faster on nearly-sorted data

---

## Problem 3.1-3: Generalized Lower Bound with Parameter α

### Problem Statement
Suppose that α is a fraction in the range 0 < α < 1. Show how to generalize the lower-bound argument for insertion sort to consider an input in which the αn largest values start in the first αn positions. What additional restriction do you need to put on α? What value of α maximizes the number of times that the αn largest values must pass through each of the middle (1-2α)n array positions?

---

### Understanding the Problem

**Original argument:**
- α = 1/3 (divide into thirds)
- First n/3: large values
- Middle n/3: pass through
- Last n/3: final positions
- Operations: (n/3) × (n/3) = n²/9

**Generalization:**
- Use parameter α instead of 1/3
- First αn: large values
- Middle (1-2α)n: pass through
- Last αn: final positions
- Operations: (αn) × (1-2α)n = ?

**Questions to answer:**
1. What restrictions on α?
2. What α maximizes operations?

---

### Solution

---

### Part 1: Generalize the Argument

**Step 1: Divide array using parameter α**

```
[First αn positions] [Middle (1-2α)n positions] [Last αn positions]
     ↑                        ↑                         ↑
  large values          pass through              final positions
```

**Step 2: Describe the bad input**

Place the αn **largest** values in the first αn positions.

**Step 3: Count operations**

Each of the αn large values must:
- Pass through the middle (1-2α)n positions
- Move one position at a time

Total operations:
```
(αn) × (1-2α)n = α(1-2α)n²
```

**Step 4: Express as Ω(n²)**

```
T(n) ≥ α(1-2α)n²

If α(1-2α) > 0, then T(n) = Ω(n²) ✓
```

---

### Part 2: Find Restrictions on α

**Constraint 1: α > 0**
- Need at least some large values
- Otherwise no operations to count

**Constraint 2: 1-2α > 0**
- Need middle section to exist
- Otherwise no positions to pass through

From Constraint 2:
```
1 - 2α > 0
1 > 2α
α < 1/2
```

**Constraint 3: α < 1**
- Can't use more than all positions
- (Actually implied by α < 1/2)

**Constraint 4: αn + (1-2α)n + αn ≤ n**
```
αn + n - 2αn + αn = n ✓
```
This is always satisfied!

**Final restriction:** **0 < α < 1/2**

**Intuition:** Need room for three sections, and middle section must exist.

---

### Part 3: Maximize Operations

**Goal:** Find α that maximizes f(α) = α(1-2α)n²

Since n² is constant, maximize:
```
f(α) = α(1-2α) = α - 2α²
```

**Step 1: Take derivative**
```
f'(α) = d/dα [α - 2α²]
      = 1 - 4α
```

**Step 2: Find critical points**
```
Set f'(α) = 0:
1 - 4α = 0
α = 1/4
```

**Step 3: Verify it's a maximum**

Second derivative:
```
f''(α) = -4 < 0
```

Since f''(α) < 0, the function is concave down, so α = 1/4 is a **maximum**. ✓

**Step 4: Check constraint**
```
Is 0 < 1/4 < 1/2?
Yes! ✓
```

**Step 5: Calculate maximum value**
```
f(1/4) = (1/4)(1 - 2·1/4)
       = (1/4)(1 - 1/2)
       = (1/4)(1/2)
       = 1/8
```

**Maximum operations:** **(1/8)n²**

---

### Part 4: Interpretation

**Optimal division:**
```
First 1/4 of array: large values (n/4 values)
Middle 1/2 of array: pass through (n/2 positions)
Last 1/4 of array: final positions
```

**Operations:**
```
(n/4) × (n/2) = n²/8
```

**Comparison with original:**
```
Original (α = 1/3): n²/9 ≈ 0.111n²
Optimal (α = 1/4): n²/8 = 0.125n²
```

**The optimal α = 1/4 gives MORE operations than α = 1/3!**

---

### Part 5: Graphical Understanding

**Function f(α) = α(1-2α) for 0 < α < 1/2:**

```
f(α)
 |
1/8 |     ╱╲
    |    ╱  ╲
    |   ╱    ╲
    |  ╱      ╲
    | ╱        ╲___
    |╱              ╲
    +-----|-----|-----α
    0    1/4   1/2

Maximum at α = 1/4
```

**Values at key points:**
```
f(0) = 0
f(1/6) = 1/6 · 2/3 = 1/9 ≈ 0.111
f(1/4) = 1/4 · 1/2 = 1/8 = 0.125  [MAXIMUM]
f(1/3) = 1/3 · 1/3 = 1/9 ≈ 0.111
f(1/2) = 1/2 · 0 = 0
```

---

### Part 6: Why α = 1/4 is Optimal

**Intuition:**

We want to maximize: (size of first section) × (size of middle section)

Given constraint: first + middle + last = n, and first = last = αn

So: middle = n - 2αn = (1-2α)n

We're maximizing: αn × (1-2α)n = α(1-2α)n²

**Trade-off:**
- Larger α → more values to move, but smaller middle section
- Smaller α → fewer values to move, but larger middle section
- Optimal balance at α = 1/4

**Mathematical insight:**
This is a classic optimization problem. For product xy with constraint x + y = constant, maximum occurs when x = y.

Here:
- Let x = αn (first section)
- Let y = (1-2α)n (middle section)
- Constraint: x + 2x + y = n (since last = first)

Maximum when x = y/2, giving α = 1/4.

---

### Summary

**Answers:**

1. **Restriction on α:** 0 < α < 1/2

2. **Optimal α:** α = 1/4

3. **Maximum operations:** n²/8

**Key insights:**
- The 1/3, 1/3, 1/3 split is NOT optimal
- The 1/4, 1/2, 1/4 split gives more operations
- This is the worst possible input for insertion sort!

---

## Summary: Problem-Solving Patterns

### Pattern 1: Modifying Proofs (3.1-1)
**Approach:**
1. Identify what changes (n/3 → ⌊n/3⌋)
2. Redo counting with new values
3. Show bound still holds (possibly with different constant)

**Key skill:** Adapting arguments to handle edge cases

---

### Pattern 2: Analyzing Algorithms (3.1-2)
**Approach:**
1. Count loop iterations
2. Establish upper bound (O)
3. Establish lower bound (Ω)
4. Combine for tight bound (Θ)

**Key skill:** Systematic loop analysis

---

### Pattern 3: Parameterization and Optimization (3.1-3)
**Approach:**
1. Replace constants with parameters
2. Express operations as function of parameters
3. Find constraints on parameters
4. Optimize using calculus

**Key skill:** Mathematical optimization

---

## Quick Reference

### Insertion Sort
```
Best: Θ(n)
Worst: Θ(n²)
Worst-case input: reverse sorted or large values at front
```

### Selection Sort
```
All cases: Θ(n²)
Always scans entire unsorted portion
```

### Lower Bound Techniques
```
1. Find bad input
2. Count operations for that input
3. Show count is Ω(f(n))
```

### Optimization
```
1. Express as function f(α)
2. Take derivative f'(α)
3. Set f'(α) = 0
4. Verify with f''(α) < 0
5. Check constraints
```

---

**You've mastered Chapter 3.1! 🎉**

---

**End of Solutions**
