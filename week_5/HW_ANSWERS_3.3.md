# Homework Solutions: Sections 2.3, 3.1, and 3.2

**Course:** CS3112 - Introduction to Algorithms  
**Date:** September 30, 2025

---

# Section 2.3: Designing Algorithms

## Exercise 2.3-4: Mathematical Induction Proof

**Problem:** Prove that when n = 2^k, the recurrence T(n) = 2T(n/2) + n has solution T(n) = n lg n.

### What You Need to Know

**Mathematical Induction:** A proof technique with three steps:
1. **Base case:** Prove it works for the smallest value
2. **Inductive hypothesis:** Assume it works for some value k
3. **Inductive step:** Prove it works for k+1

**Logarithm:** lg n = log₂ n means "how many times do I divide n by 2 to get 1?"
- lg 2 = 1, lg 4 = 2, lg 8 = 3, lg 16 = 4

### Solution

**Base Case (k=1, n=2):**
```
Given: T(2) = 2
Formula: T(2) = 2 lg 2 = 2·1 = 2 ✓
```

**Inductive Hypothesis:**
Assume T(2^k) = 2^k · k for some k ≥ 1.

**Inductive Step:**
Prove T(2^(k+1)) = 2^(k+1) · (k+1)

```
T(2^(k+1)) = 2T(2^(k+1)/2) + 2^(k+1)          [recurrence]
           = 2T(2^k) + 2^(k+1)                 [simplify]
           = 2(2^k · k) + 2^(k+1)              [inductive hypothesis]
           = 2^(k+1) · k + 2^(k+1)             [algebra]
           = 2^(k+1)(k + 1) ✓                  [factor]
```

**Conclusion:** By induction, T(n) = n lg n for all n = 2^k. ∎

---

## Exercise 2.3-5: Recursive Insertion Sort

**Problem:** Write recursive insertion sort pseudocode and give its worst-case recurrence.

### Understanding Recursion

**Recursion:** A function that calls itself on smaller inputs.
- **Base case:** Smallest problem you can solve directly
- **Recursive case:** Break problem into smaller pieces

### Solution: Pseudocode

```
RECURSIVE-INSERTION-SORT(A, n)
1  if n ≤ 1                              // Base: 0 or 1 element is sorted
2      return
3  RECURSIVE-INSERTION-SORT(A, n-1)      // Sort first n-1 elements
4  // Insert A[n] into sorted A[1:n-1]
5  key = A[n]
6  i = n - 1
7  while i > 0 and A[i] > key
8      A[i + 1] = A[i]                   // Shift right
9      i = i - 1
10 A[i + 1] = key                        // Insert
```

### Worst-Case Recurrence

**Worst case:** Array is reverse sorted, so each element must be compared with all previous elements.

```
T(1) = c₁                    [base case: constant]
T(n) = T(n-1) + cn          [recursive + insert]
```

**Solving:**
```
T(n) = T(n-1) + cn
     = T(n-2) + c(n-1) + cn
     = T(1) + c·2 + c·3 + ... + cn
     = c₁ + c(2 + 3 + ... + n)
     = c₁ + c·n(n+1)/2 - c
     = Θ(n²)
```

**Answer:** T(n) = Θ(n²) (same as iterative version)

---

## Exercise 2.3-6: Binary Search

**Problem:** Write binary search pseudocode and prove it's Θ(lg n).

### What is Binary Search?

**Binary search** finds a value in a sorted array by repeatedly halving the search space:
1. Check middle element
2. If target is smaller, search left half
3. If target is larger, search right half
4. Repeat until found or no elements left

### Solution: Iterative Version

```
BINARY-SEARCH-ITERATIVE(A, n, v)
1  left = 1
2  right = n
3  while left ≤ right
4      mid = ⌊(left + right) / 2⌋
5      if A[mid] == v
6          return mid
7      elseif A[mid] < v
8          left = mid + 1              // Search right half
9      else
10         right = mid - 1             // Search left half
11 return NIL                          // Not found
```

### Solution: Recursive Version

```
BINARY-SEARCH-RECURSIVE(A, left, right, v)
1  if left > right
2      return NIL
3  mid = ⌊(left + right) / 2⌋
4  if A[mid] == v
5      return mid
6  elseif A[mid] < v
7      return BINARY-SEARCH-RECURSIVE(A, mid+1, right, v)
8  else
9      return BINARY-SEARCH-RECURSIVE(A, left, mid-1, v)
```

### Proof: T(n) = Θ(lg n)

**Recurrence:**
```
T(1) = c
T(n) = T(n/2) + c
```

**Solving:**
```
T(n) = T(n/2) + c
     = T(n/4) + 2c
     = T(n/8) + 3c
     = T(1) + (lg n)·c
     = Θ(lg n)
```

**Why:** Each comparison eliminates half the elements. After k comparisons, n/2^k elements remain. When n/2^k = 1, we have k = lg n.

---

## Exercise 2.3-7: Binary Search in Insertion Sort

**Problem:** Would using binary search in insertion sort improve it to Θ(n lg n)?

### Answer: NO

The worst-case remains **Θ(n²)**.

### Why Binary Search Doesn't Help

Insertion sort does two things for each element:
1. **Find position:** Where to insert (comparisons)
2. **Shift elements:** Make room (data movement)

**With linear search:**
- Comparisons: O(n) per element → O(n²) total
- Shifts: O(n) per element → O(n²) total
- **Total: O(n²)**

**With binary search:**
- Comparisons: O(lg n) per element → O(n lg n) total ✓ Better!
- Shifts: O(n) per element → O(n²) total ✗ Still quadratic!
- **Total: O(n lg n) + O(n²) = O(n²)**

### The Bottleneck

**The problem:** Arrays store elements in contiguous memory. To insert at position j with i elements, you MUST physically move elements j through i-1 one position right.

**No clever searching can avoid this data movement!**

### Example

Insert 1 into [2, 3, 4, 5, 6, 7, 8, 9, 10]:

**Linear search:** 9 comparisons + 9 shifts = 18 operations
**Binary search:** 3 comparisons + 9 shifts = 12 operations

Better, but still O(n) per insertion → O(n²) overall.

---

# Section 3.1: Characterizing Running Times

## Exercise 3.1-2: Selection Sort Analysis

**Problem:** Analyze selection sort from Exercise 2.2-2.

### Selection Sort Algorithm

```
SELECTION-SORT(A, n)
  for i = 1 to n - 1
    min_idx = i
    for j = i + 1 to n
      if A[j] < A[min_idx]
        min_idx = j
    if min_idx ≠ i
      swap A[i] and A[min_idx]
```

### How It Works

1. Find smallest element in unsorted portion
2. Swap with first unsorted element
3. Move boundary one position right
4. Repeat

### Upper Bound: O(n²)

**Inner loop iterations:**
- When i=1: (n-1) iterations
- When i=2: (n-2) iterations
- ...
- When i=n-1: 1 iteration

**Total comparisons:**
```
(n-1) + (n-2) + ... + 1 = n(n-1)/2 = Θ(n²)
```

Therefore: T(n) = O(n²) ✓

### Lower Bound: Ω(n²)

**Key observation:** Selection sort ALWAYS makes the same number of comparisons, regardless of input!

To find the minimum of k elements, you must check all k elements. The inner loop always completes fully.

**For ANY input:**
```
Comparisons = n(n-1)/2 = Θ(n²)
```

Therefore: T(n) = Ω(n²) ✓

### Tight Bound: Θ(n²)

Since T(n) = O(n²) AND T(n) = Ω(n²):

**T(n) = Θ(n²) for ALL cases:**
- Best case: Θ(n²) (even if sorted)
- Worst case: Θ(n²)
- Average case: Θ(n²)

### Comparison with Insertion Sort

| Property | Selection Sort | Insertion Sort |
|----------|---------------|----------------|
| Best case | Θ(n²) | Θ(n) |
| Worst case | Θ(n²) | Θ(n²) |
| Adaptive? | No | Yes |

Selection sort is NOT adaptive - always does the same work!

---

# Section 3.2: Asymptotic Notation

## Background: The Five Notations

| Notation | Meaning | Analogy |
|----------|---------|---------|
| O(g(n)) | Upper bound | ≤ |
| Ω(g(n)) | Lower bound | ≥ |
| Θ(g(n)) | Tight bound | = |
| o(g(n)) | Strict upper | < |
| ω(g(n)) | Strict lower | > |

---

## Exercise 3.2-1: Prove max{f(n), g(n)} = Θ(f(n) + g(n))

**Given:** f(n) and g(n) are asymptotically nonnegative.

### Upper Bound: max{f(n), g(n)} = O(f(n) + g(n))

For any n:
```
max{f(n), g(n)} ≤ f(n) + g(n)
```

Why? The max is at most the sum (since both are non-negative).

Therefore: max{f(n), g(n)} = O(f(n) + g(n)) with c = 1 ✓

### Lower Bound: max{f(n), g(n)} = Ω(f(n) + g(n))

For any n:
```
max{f(n), g(n)} ≥ f(n)
max{f(n), g(n)} ≥ g(n)

Adding:
2·max{f(n), g(n)} ≥ f(n) + g(n)
max{f(n), g(n)} ≥ (1/2)·(f(n) + g(n))
```

Therefore: max{f(n), g(n)} = Ω(f(n) + g(n)) with c = 1/2 ✓

### Conclusion

max{f(n), g(n)} = Θ(f(n) + g(n)) ∎

---

## Exercise 3.2-2: Meaningless Statement

**Problem:** Why is "The running time is at least O(n²)" meaningless?

### Analysis

- **"At least"** = lower bound (≥)
- **O(n²)** = upper bound (≤)
- **Combined:** "minimum is at most n²"

### Why It's Meaningless

This provides NO useful information:
- O(1) algorithm satisfies it (1 ≤ n²)
- O(n) algorithm satisfies it (n ≤ n²)
- O(2^n) algorithm satisfies it (but NOT O(n²))

Almost every algorithm satisfies "at least O(n²)"!

### Correct Alternatives

**For lower bound:**
- "Running time is Ω(n²)"
- "Running time is at least Ω(n²)"

**For upper bound:**
- "Running time is O(n²)"
- "Running time is at most O(n²)"

**For tight bound:**
- "Running time is Θ(n²)"

---

## Exercise 3.2-3: Exponential Comparisons

### Part 1: Is 2^(n+1) = O(2^n)?

**YES** ✓

```
2^(n+1) = 2·2^n
```

This is just a constant factor (2×) larger than 2^n.

Big-O ignores constant factors, so they grow at the same rate.

**Proof:** With c = 2 and n₀ = 1:
```
2^(n+1) = 2·2^n ≤ 2·2^n for all n ≥ 1 ✓
```

### Part 2: Is 2^(2n) = O(2^n)?

**NO** ✗

```
2^(2n) = (2^n)² = 2^n · 2^n
```

This is NOT a constant multiple - it's the square of 2^n!

**Proof by contradiction:**
```
If 2^(2n) = O(2^n), then:
2^(2n) ≤ c·2^n
(2^n)² ≤ c·2^n
2^n ≤ c

But 2^n → ∞, so no constant c works! ✗
```

**Growth rate comparison:**
```
2^(2n) / 2^n = 2^n → ∞
```

The ratio grows without bound, proving different growth rates.

---

## Exercise 3.2-4: Prove Theorem 3.1

**Theorem:** f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))

### Proof (⇒): Θ implies O and Ω

**Given:** f(n) = Θ(g(n))

By definition:
```
∃ c₁, c₂, n₀ > 0: c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀
```

**Extract O:** f(n) ≤ c₂·g(n) → f(n) = O(g(n)) ✓

**Extract Ω:** c₁·g(n) ≤ f(n) → f(n) = Ω(g(n)) ✓

### Proof (⇐): O and Ω imply Θ

**Given:** f(n) = O(g(n)) AND f(n) = Ω(g(n))

From O: ∃ c₂, n₁: f(n) ≤ c₂·g(n) for n ≥ n₁
From Ω: ∃ c₁, n₂: c₁·g(n) ≤ f(n) for n ≥ n₂

Let n₀ = max{n₁, n₂}. For all n ≥ n₀:
```
c₁·g(n) ≤ f(n) ≤ c₂·g(n)
```

This is the definition of Θ! ✓

**Conclusion:** Theorem 3.1 proved. ∎

---

## Exercise 3.2-5: Algorithm Running Time Characterization

**Theorem:** T(n) = Θ(g(n)) ⟺ W(n) = O(g(n)) AND B(n) = Ω(g(n))

Where:
- T(n) = running time for any input
- W(n) = worst-case running time
- B(n) = best-case running time

### Proof (⇒): Θ for all inputs implies bounds on worst/best

**Given:** T(n) = Θ(g(n)) for all inputs

```
∃ c₁, c₂, n₀: c₁·g(n) ≤ T(n) ≤ c₂·g(n) for all n ≥ n₀, all inputs
```

**Worst case:** W(n) = max{T(n)} ≤ c₂·g(n) → W(n) = O(g(n)) ✓

**Best case:** c₁·g(n) ≤ min{T(n)} = B(n) → B(n) = Ω(g(n)) ✓

### Proof (⇐): Bounds on worst/best imply Θ for all inputs

**Given:** W(n) = O(g(n)) AND B(n) = Ω(g(n))

From O: W(n) ≤ c₂·g(n) for n ≥ n₁
From Ω: c₁·g(n) ≤ B(n) for n ≥ n₂

For n ≥ max{n₁, n₂} and any input:
```
c₁·g(n) ≤ B(n) ≤ T(n) ≤ W(n) ≤ c₂·g(n)
```

Therefore: T(n) = Θ(g(n)) ✓

**Conclusion:** Theorem proved. ∎

---

## Exercise 3.2-6: Prove o(g(n)) ∩ ω(g(n)) = ∅

**Definitions:**
- **o(g(n)):** f grows strictly slower than g
- **ω(g(n)):** f grows strictly faster than g

### Proof by Contradiction

**Assume:** ∃ f(n) ∈ o(g(n)) AND f(n) ∈ ω(g(n))

**From o(g(n)):** For c = 1, ∃ n₀: f(n) < g(n) for all n ≥ n₀

**From ω(g(n)):** For c = 1, ∃ n₁: g(n) < f(n) for all n ≥ n₁

**Let n₂ = max{n₀, n₁}. For all n ≥ n₂:**
```
f(n) < g(n) < f(n)
```

This implies f(n) < f(n), which is a **contradiction**! ✗

**Therefore:** o(g(n)) ∩ ω(g(n)) = ∅ ∎

---

## Summary

**Section 2.3:** Recursive algorithms, divide-and-conquer, solving recurrences
**Section 3.1:** Analyzing best/worst/average cases with asymptotic notation
**Section 3.2:** Formal definitions and proofs of O, Ω, Θ, o, ω notation

All solutions show step-by-step reasoning from first principles!
