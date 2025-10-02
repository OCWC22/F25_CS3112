# Chapter 2 Exercises: Complete Solutions with Frameworks

**Sections:** 2.1, 2.2, 2.3  
**Focus:** Algorithm execution, correctness proofs, analysis, and design

---

## 🎯 Problem Recognition Framework

### How to Identify What Each Problem Is Asking

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Trace Execution** | "illustrate", "show operation", "trace" | Show step-by-step what algorithm does | Execute algorithm manually, show each iteration |
| **Modify Algorithm** | "rewrite", "modify", "change to" | Alter algorithm for different behavior | Identify what changes, modify code |
| **Prove Correctness** | "prove", "loop invariant", "show that" | Prove algorithm works correctly | Use loop invariant: initialization, maintenance, termination |
| **Analyze Time** | "running time", "express as function", "Θ-notation" | Calculate how long algorithm takes | Count operations, sum up, express in Θ |
| **Design Algorithm** | "write pseudocode", "design", "give algorithm" | Create new algorithm | Choose technique, write code, analyze |
| **Compare Algorithms** | "which is faster", "compare" | Determine which algorithm is better | Analyze both, compare growth rates |

---

## 📚 Section 2.1 Exercises: Insertion Sort

### Exercise 2.1-1: Illustrate Insertion Sort

**Problem Statement:**
Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on an array initially containing the sequence ⟨31, 41, 59, 26, 41, 58⟩.

---

**What This Problem Is Asking:**
- Show step-by-step execution of insertion sort
- Display array state after each iteration
- Show which elements are being compared and moved

**Framework to Solve:**
1. Write initial array
2. For each iteration i = 2 to n:
   - Show current key
   - Show sorted portion (left of key)
   - Show comparisons made
   - Show shifts that occur
   - Show array after insertion
3. Show final sorted array

---

**Solution:**

**Initial array:** A = [31, 41, 59, 26, 41, 58]

**Iteration i = 2 (key = 41):**
```
Initial:  [31, 41, 59, 26, 41, 58]
          sorted: [31]  current: 41

Compare 41 with 31: 31 ≤ 41, stop
No shifts needed
Result:   [31, 41, 59, 26, 41, 58]
          sorted: [31, 41]
```

**Iteration i = 3 (key = 59):**
```
Initial:  [31, 41, 59, 26, 41, 58]
          sorted: [31, 41]  current: 59

Compare 59 with 41: 41 ≤ 59, stop
No shifts needed
Result:   [31, 41, 59, 26, 41, 58]
          sorted: [31, 41, 59]
```

**Iteration i = 4 (key = 26):**
```
Initial:  [31, 41, 59, 26, 41, 58]
          sorted: [31, 41, 59]  current: 26

Compare 26 with 59: 59 > 26, shift right
Array:    [31, 41, 59, 59, 41, 58]

Compare 26 with 41: 41 > 26, shift right
Array:    [31, 41, 41, 59, 41, 58]

Compare 26 with 31: 31 > 26, shift right
Array:    [31, 31, 41, 59, 41, 58]

Reached beginning, insert 26 at position 1
Result:   [26, 31, 41, 59, 41, 58]
          sorted: [26, 31, 41, 59]
```

**Iteration i = 5 (key = 41):**
```
Initial:  [26, 31, 41, 59, 41, 58]
          sorted: [26, 31, 41, 59]  current: 41

Compare 41 with 59: 59 > 41, shift right
Array:    [26, 31, 41, 59, 59, 58]

Compare 41 with 41: 41 ≤ 41, stop
Insert 41 at position 3
Result:   [26, 31, 41, 41, 59, 58]
          sorted: [26, 31, 41, 41, 59]
```

**Iteration i = 6 (key = 58):**
```
Initial:  [26, 31, 41, 41, 59, 58]
          sorted: [26, 31, 41, 41, 59]  current: 58

Compare 58 with 59: 59 > 58, shift right
Array:    [26, 31, 41, 41, 59, 59]

Compare 58 with 41: 41 ≤ 58, stop
Insert 58 at position 5
Result:   [26, 31, 41, 41, 58, 59]
          sorted: [26, 31, 41, 41, 58, 59]
```

**Final sorted array:** [26, 31, 41, 41, 58, 59] ✓

---

**Key Observations:**
- Iteration 2 and 3: No shifts (already in order)
- Iteration 4: Maximum shifts (smallest element at end)
- Iteration 5: Duplicate value handled correctly
- Iteration 6: One shift needed

---

### Exercise 2.1-2: Rewrite for Non-increasing Order

**Problem Statement:**
Consider the procedure SUM-ARRAY on the facing page. It computes the sum of the n numbers in array A[1 : n]. State a loop invariant for this procedure, and use its initialization, maintenance, and termination properties to show that the SUM-ARRAY procedure returns the sum of the numbers in A[1 : n].

**Note:** The actual problem asks to rewrite INSERTION-SORT to sort into non-increasing order instead of non-decreasing order.

---

**What This Problem Is Asking:**
- Modify insertion sort to sort from largest to smallest
- Change comparison operator or loop direction

**Framework to Solve:**
1. Identify what determines sort order (comparison in line 5)
2. Change comparison operator
3. Verify with example

---

**Solution:**

**Original line 5:**
```
while j > 0 and A[j] > key
```

**Modified line 5 (for non-increasing order):**
```
while j > 0 and A[j] < key
```

**Complete modified algorithm:**
```
INSERTION-SORT-DECREASING(A, n)
1  for i = 2 to n
2    key = A[i]
3    // Insert A[i] into the sorted subarray A[1 : i-1]
4    j = i - 1
5    while j > 0 and A[j] < key    // CHANGED: < instead of >
6      A[j+1] = A[j]
7      j = j - 1
8    A[j+1] = key
```

**Why this works:**
- Original: Shift right if A[j] > key (to make room for smaller key)
- Modified: Shift right if A[j] < key (to make room for larger key)
- Result: Larger elements stay left, smaller elements move right

**Verification with example:**
```
Input: [5, 2, 4, 6, 1, 3]

i=2, key=2: [5, 2, 4, 6, 1, 3] → [5, 2, 4, 6, 1, 3] (5 > 2, no shift)
i=3, key=4: [5, 2, 4, 6, 1, 3] → [5, 4, 2, 6, 1, 3] (5 > 4, shift 2)
i=4, key=6: [5, 4, 2, 6, 1, 3] → [6, 5, 4, 2, 1, 3] (all < 6, shift all)
i=5, key=1: [6, 5, 4, 2, 1, 3] → [6, 5, 4, 2, 1, 3] (all > 1, no shift)
i=6, key=3: [6, 5, 4, 2, 1, 3] → [6, 5, 4, 3, 2, 1] (2,1 < 3, shift)

Output: [6, 5, 4, 3, 2, 1] ✓
```

---

### Exercise 2.1-3: Linear Search

**Problem Statement:**
Consider the searching problem:

**Input:** A sequence of n numbers ⟨a₁, a₂, ..., aₙ⟩ stored in array A[1 : n] and a value x.

**Output:** An index i such that x equals A[i] or the special value NIL if x does not appear in A.

Write pseudocode for **linear search**, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

---

**What This Problem Is Asking:**
- Write algorithm to find element in array
- Prove correctness using loop invariant
- Show initialization, maintenance, termination

**Framework to Solve:**
1. Write pseudocode for linear search
2. State loop invariant clearly
3. Prove initialization (before first iteration)
4. Prove maintenance (iteration to iteration)
5. Prove termination (when loop ends)

---

**Solution:**

**Algorithm:**
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2    if A[i] == x
3      return i
4  return NIL
```

**Loop Invariant:**
> At the start of each iteration of the for loop, the subarray A[1 : i-1] does not contain the value x.

**Proof of Correctness:**

**1. Initialization (i = 1):**
- Before first iteration, i = 1
- Subarray A[1 : i-1] = A[1 : 0] is empty
- An empty subarray trivially does not contain x
- **Loop invariant holds** ✓

**2. Maintenance (iteration i → i+1):**
- **Assume:** A[1 : i-1] does not contain x (loop invariant holds before iteration i)
- **During iteration i:**
  - Check if A[i] == x
  - If yes: return i (algorithm terminates, x found)
  - If no: A[i] ≠ x, so A[1 : i] does not contain x
- **After iteration i:**
  - i increments to i+1
  - A[1 : (i+1)-1] = A[1 : i] does not contain x
- **Loop invariant holds before next iteration** ✓

**3. Termination:**

**Case 1: Loop exits via return in line 3**
- Found A[i] == x for some i ∈ [1, n]
- Return i (correct answer: x found at position i) ✓

**Case 2: Loop completes all iterations**
- Loop terminates when i > n (i.e., i = n+1)
- Loop invariant: A[1 : n] does not contain x
- Return NIL (correct answer: x not in array) ✓

**Conclusion:** Algorithm is correct in all cases ✓

---

**Alternative Loop Invariant (more detailed):**
> At the start of each iteration of the for loop:
> 1. The subarray A[1 : i-1] does not contain x, AND
> 2. If x is in A, then x is in A[i : n]

This invariant is stronger and makes the correctness argument even clearer.

---

### Exercise 2.1-4: Adding Binary Integers

**Problem Statement:**
Consider the problem of adding two n-bit binary integers a and b, stored in two n-element arrays A[1 : n] and B[1 : n], where each element is either 0 or 1, a = Σᵢ₌₁ⁿ A[i]·2^(i-1), and b = Σᵢ₌₁ⁿ B[i]·2^(i-1). The sum c = a + b of the two integers should be stored in binary form in an (n+1)-element array C[1 : n+1], where c = Σᵢ₌₁ⁿ⁺¹ C[i]·2^(i-1). Write a procedure ADD-BINARY-INTEGERS(A, B, n) that takes as input arrays A and B, along with the length n, and returns array C holding the sum.

---

**What This Problem Is Asking:**
- Add two binary numbers represented as arrays
- Handle carry bits
- Result may need n+1 bits (overflow)

**Framework to Solve:**
1. Understand binary addition with carry
2. Process bits from right to left (least significant first)
3. Track carry bit
4. Store result in output array

---

**Solution:**

**Algorithm:**
```
ADD-BINARY-INTEGERS(A, B, n)
1  let C[1 : n+1] be a new array
2  carry = 0
3  for i = 1 to n
4    sum = A[i] + B[i] + carry
5    C[i] = sum mod 2          // bit value (0 or 1)
6    carry = ⌊sum / 2⌋          // carry bit (0 or 1)
7  C[n+1] = carry               // final carry
8  return C
```

**Line-by-line explanation:**

**Line 1:** Create output array of size n+1
- Need extra bit for potential overflow

**Line 2:** Initialize carry to 0
- No carry before first addition

**Lines 3-6:** Process each bit position
- **Line 4:** Add corresponding bits plus carry
  - sum can be 0, 1, 2, or 3
- **Line 5:** Store low bit of sum (sum mod 2)
  - This is the result bit for position i
- **Line 6:** Calculate new carry (⌊sum / 2⌋)
  - carry = 0 if sum ≤ 1
  - carry = 1 if sum ≥ 2

**Line 7:** Store final carry in C[n+1]
- This is the overflow bit

**Line 8:** Return result array

---

**Example 1: No overflow**
```
A = [1, 0, 1, 1]  (represents 1101₂ = 13₁₀)
B = [0, 1, 1, 0]  (represents 0110₂ = 6₁₀)

i=1: sum = 1+0+0 = 1, C[1] = 1, carry = 0
i=2: sum = 0+1+0 = 1, C[2] = 1, carry = 0
i=3: sum = 1+1+0 = 2, C[3] = 0, carry = 1
i=4: sum = 1+0+1 = 2, C[4] = 0, carry = 1
C[5] = 1

Result: C = [1, 1, 0, 0, 1]  (represents 10011₂ = 19₁₀)
Verify: 13 + 6 = 19 ✓
```

**Example 2: With overflow**
```
A = [1, 1, 1, 1]  (represents 1111₂ = 15₁₀)
B = [1, 0, 0, 0]  (represents 0001₂ = 1₁₀)

i=1: sum = 1+1+0 = 2, C[1] = 0, carry = 1
i=2: sum = 1+0+1 = 2, C[2] = 0, carry = 1
i=3: sum = 1+0+1 = 2, C[3] = 0, carry = 1
i=4: sum = 1+0+1 = 2, C[4] = 0, carry = 1
C[5] = 1

Result: C = [0, 0, 0, 0, 1]  (represents 10000₂ = 16₁₀)
Verify: 15 + 1 = 16 ✓
```

**Running time:** Θ(n) - single pass through arrays

---

## 📊 Section 2.2 Exercises: Analyzing Algorithms

### Exercise 2.2-1: Express n³/1000 - 100n² - 100n + 3 in Θ-notation

**Problem Statement:**
Express the function n³/1000 - 100n² - 100n + 3 in terms of Θ-notation.

---

**What This Problem Is Asking:**
- Identify highest-order term
- Drop lower-order terms and constants
- Express in Θ-notation

**Framework to Solve:**
1. Identify all terms
2. Determine which term dominates for large n
3. Drop everything except highest-order term
4. Drop coefficient of highest-order term
5. Express in Θ-notation

---

**Solution:**

**Given function:**
```
f(n) = n³/1000 - 100n² - 100n + 3
```

**Terms in order of growth:**
```
n³/1000  (cubic term)
-100n²   (quadratic term)
-100n    (linear term)
3        (constant term)
```

**For large n, which term dominates?**

Let's compare at n = 1000:
```
n³/1000 = 1000³/1000 = 1,000,000,000
100n² = 100·1000² = 100,000,000
100n = 100·1000 = 100,000
3 = 3

Cubic term is 10× larger than quadratic term!
```

**As n → ∞:**
```
lim(n→∞) (n³/1000) / (100n²) = lim(n→∞) n/100 = ∞
```

The cubic term grows much faster than all other terms.

**Applying Θ-notation rules:**
1. Keep only highest-order term: n³/1000
2. Drop constant coefficient: n³

**Answer:** f(n) = Θ(n³) ✓

**Verification:**
For Θ(n³), we need constants c₁, c₂, n₀ such that:
```
c₁·n³ ≤ n³/1000 - 100n² - 100n + 3 ≤ c₂·n³  for all n ≥ n₀
```

For large n (say n ≥ 1000):
- Upper bound: f(n) ≤ n³/1000 ≤ (1/1000)·n³, so c₂ = 1/1000 works
- Lower bound: f(n) ≥ n³/1000 - 100n² ≥ n³/2000 for large n, so c₁ = 1/2000 works

Therefore f(n) = Θ(n³) ✓

---

### Exercise 2.2-2: Selection Sort

**Problem Statement:**
Consider sorting n numbers stored in array A[1 : n] by first finding the smallest element of A[1 : n] and exchanging it with the element in A[1]. Then find the smallest element of A[2 : n] and exchange it with A[2]. Then find the smallest element of A[3 : n] and exchange it with A[3]. Continue in this manner for the first n - 1 elements of A. Write pseudocode for this algorithm, which is known as **selection sort**. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the worst-case running time of selection sort in Θ-notation. Is the best-case running time any better?

---

**What This Problem Is Asking:**
- Write pseudocode for selection sort
- State and explain loop invariant
- Explain why n-1 iterations suffice
- Analyze worst-case and best-case running time

**Framework to Solve:**
1. Write clear pseudocode
2. State loop invariant
3. Explain why n-1 iterations work
4. Count operations for worst case
5. Count operations for best case
6. Express both in Θ-notation

---

**Solution:**

**Pseudocode:**
```
SELECTION-SORT(A, n)
1  for i = 1 to n-1
2    min_index = i
3    for j = i+1 to n
4      if A[j] < A[min_index]
5        min_index = j
6    swap A[i] with A[min_index]
```

**Line-by-line explanation:**

**Line 1:** Outer loop runs n-1 times
- i represents the position to fill with minimum

**Line 2:** Assume current position has minimum
- Will update if we find smaller element

**Lines 3-5:** Inner loop finds actual minimum
- Scan from i+1 to n
- Update min_index when smaller element found

**Line 6:** Swap minimum element into position i
- Places smallest unsorted element in correct position

---

**Loop Invariant:**
> At the start of each iteration of the for loop of lines 1-6, the subarray A[1 : i-1] contains the i-1 smallest elements of A[1 : n] in sorted order.

**Proof:**

**Initialization (i = 1):**
- A[1 : 0] is empty
- Trivially contains 0 smallest elements in sorted order ✓

**Maintenance (iteration i → i+1):**
- Assume A[1 : i-1] contains i-1 smallest elements in sorted order
- Inner loop finds minimum of A[i : n]
- Swap places this minimum at position i
- Now A[1 : i] contains i smallest elements in sorted order
- Incrementing i preserves invariant ✓

**Termination (i = n):**
- Loop terminates when i = n
- A[1 : n-1] contains n-1 smallest elements in sorted order
- The remaining element A[n] must be the largest
- Therefore A[1 : n] is fully sorted ✓

---

**Why only n-1 iterations?**

After n-1 iterations:
- A[1 : n-1] contains the n-1 smallest elements in sorted order
- A[n] must contain the largest element (only one left!)
- No need to "sort" a single element

**Analogy:** If you have 10 people and line up the 9 shortest, the 10th person must be the tallest!

---

**Worst-Case Running Time:**

**Outer loop (line 1):** Runs n-1 times

**Inner loop (lines 3-5):** For iteration i, runs n-i times
```
i=1: n-1 comparisons
i=2: n-2 comparisons
...
i=n-1: 1 comparison

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = Θ(n²)
```

**Swap (line 6):** Runs n-1 times, constant time each = Θ(n)

**Total:** Θ(n²) + Θ(n) = Θ(n²)

**Worst-case running time: Θ(n²)** ✓

---

**Best-Case Running Time:**

**Key observation:** Selection sort ALWAYS scans entire unsorted portion!

Even if array is already sorted:
- Still compares every element in unsorted portion
- Still performs n(n-1)/2 comparisons
- Swaps might be with same element (no movement), but still executes

**Best-case running time: Θ(n²)** ✓

**Important:** Unlike insertion sort, selection sort has NO best case advantage!

---

**Comparison with Insertion Sort:**

| Algorithm | Best Case | Worst Case | Average Case |
|-----------|-----------|------------|--------------|
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) |

**Key difference:** Selection sort is NOT adaptive (doesn't benefit from partially sorted data)

---

### Exercise 2.2-3: Average Case for Linear Search

**Problem Statement:**
Consider linear search again (see Exercise 2.1-3). How many elements of the input array need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? Using Θ-notation, give the average-case and worst-case running times of linear search. Justify your answers.

---

**What This Problem Is Asking:**
- Calculate average number of elements checked
- Calculate worst-case number of elements checked
- Express both in Θ-notation
- Provide justification

**Framework to Solve:**
1. Identify all possible cases
2. Calculate probability of each case
3. Calculate expected value (average)
4. Identify worst case
5. Express in Θ-notation

---

**Solution:**

**Linear search algorithm (recap):**
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2    if A[i] == x
3      return i
4  return NIL
```

---

**Average-Case Analysis:**

**Assumption:** Element x is in the array and equally likely to be at any position

**Possible outcomes:**
- x at position 1: check 1 element
- x at position 2: check 2 elements
- x at position 3: check 3 elements
- ...
- x at position n: check n elements

**Probability of each outcome:** 1/n (equally likely)

**Expected number of elements checked:**
```
E[checks] = Σᵢ₌₁ⁿ (probability of position i) × (checks for position i)
          = Σᵢ₌₁ⁿ (1/n) × i
          = (1/n) × Σᵢ₌₁ⁿ i
          = (1/n) × n(n+1)/2
          = (n+1)/2
```

**For large n:** (n+1)/2 ≈ n/2

**Average-case: Θ(n)** ✓

**Intuition:** On average, we check about half the array.

---

**Worst-Case Analysis:**

**Worst case occurs when:**
- Element x is at position n (last position), OR
- Element x is not in array at all

**In both cases:** Check all n elements

**Worst-case: Θ(n)** ✓

---

**Summary:**

| Case | Elements Checked | Running Time |
|------|------------------|--------------|
| Best | 1 | Θ(1) |
| Average | (n+1)/2 ≈ n/2 | Θ(n) |
| Worst | n | Θ(n) |

**Key insight:** Average and worst case have same order of growth (both linear), but average case checks about half as many elements.

---

**What if x might not be in array?**

If probability that x is in array is p:
```
E[checks] = p × (n+1)/2 + (1-p) × n
          = p(n+1)/2 + n - pn
          = n - p(n-1)/2
```

For p = 1/2 (50% chance x is in array):
```
E[checks] = n - (1/2)(n-1)/2 = n - (n-1)/4 ≈ 3n/4
```

Still Θ(n) ✓

---

### Exercise 2.2-4: Modifying Algorithm for Good Best-Case

**Problem Statement:**
How can you modify any sorting algorithm to have a good best-case running time?

---

**What This Problem Is Asking:**
- Think creatively about improving best-case performance
- Consider what "good" means (typically Θ(n))
- Provide a general technique

**Framework to Solve:**
1. Identify what makes a best case "good"
2. Think about what can be checked quickly
3. Propose modification
4. Analyze impact on best/worst/average cases

---

**Solution:**

**Key insight:** Best case is "good" if it's Θ(n) (linear time)

**Modification:** Add a preprocessing check

**Modified algorithm template:**
```
MODIFIED-SORT(A, n)
1  if IS-SORTED(A, n)
2    return  // already sorted, do nothing
3  [ORIGINAL-SORT](A, n)  // run original sorting algorithm
```

**IS-SORTED algorithm:**
```
IS-SORTED(A, n)
1  for i = 1 to n-1
2    if A[i] > A[i+1]
3      return false
4  return true
```

**Analysis:**

**IS-SORTED running time:** Θ(n)
- Single pass through array
- Constant work per element

**Modified algorithm:**

**Best case (array already sorted):**
- IS-SORTED returns true: Θ(n)
- Skip original sort
- **Total: Θ(n)** ✓

**Worst case (array not sorted):**
- IS-SORTED returns false: Θ(n)
- Run original sort: depends on algorithm
  - If original is Θ(n²), total is Θ(n) + Θ(n²) = Θ(n²)
  - If original is Θ(n lg n), total is Θ(n) + Θ(n lg n) = Θ(n lg n)
- **Total: same as original worst case** ✓

**Average case:**
- Usually not sorted, so runs original algorithm
- Extra Θ(n) check is negligible compared to sorting
- **Total: same as original average case** ✓

---

**Examples:**

**Modified Insertion Sort:**
- Best case: Θ(n) → Θ(n) (no change, already good!)
- Worst case: Θ(n²) → Θ(n²) (no change)

**Modified Selection Sort:**
- Best case: Θ(n²) → Θ(n) (IMPROVED!)
- Worst case: Θ(n²) → Θ(n²) (no change)

**Modified Merge Sort:**
- Best case: Θ(n lg n) → Θ(n) (IMPROVED!)
- Worst case: Θ(n lg n) → Θ(n lg n) (no change)

---

**Trade-offs:**

**Advantages:**
- Improves best-case performance
- Minimal overhead (just Θ(n) check)
- Useful when data is often already sorted

**Disadvantages:**
- Extra check on every call (even when not sorted)
- Doesn't help average or worst case
- Only worthwhile if sorted data is common

**Practical consideration:** Many real-world datasets are partially sorted, so this optimization can be valuable!

---

## 🔧 Section 2.3 Exercises: Designing Algorithms

### Exercise 2.3-1: Illustrate Merge Sort

**Problem Statement:**
Using Figure 2.4 as a model, illustrate the operation of merge sort on an array initially containing the sequence ⟨3, 41, 52, 26, 38, 57, 9, 49⟩.

---

**What This Problem Is Asking:**
- Show complete recursion tree for merge sort
- Show divide phase (splitting)
- Show conquer phase (sorting)
- Show combine phase (merging)

**Framework to Solve:**
1. Draw recursion tree showing all splits
2. Show base cases (single elements)
3. Show merge operations bottom-up
4. Show final merged result

---

**Solution:**

**Initial array:** [3, 41, 52, 26, 38, 57, 9, 49]

**Complete recursion tree:**

```
Level 0 (Divide):
                    [3, 41, 52, 26, 38, 57, 9, 49]
                    /                            \
Level 1:    [3, 41, 52, 26]                [38, 57, 9, 49]
            /              \                /              \
Level 2: [3, 41]        [52, 26]        [38, 57]        [9, 49]
         /    \          /    \          /    \          /    \
Level 3: [3]  [41]     [52]  [26]     [38]  [57]      [9]  [49]
         
         (Base cases - single elements, already "sorted")

Level 3 (Merge):
         [3]  [41]     [52]  [26]     [38]  [57]      [9]  [49]
         \    /          \    /          \    /          \    /
Level 2:  [3, 41]       [26, 52]       [38, 57]       [9, 49]
            \              /                \              /
Level 1:    [3, 26, 41, 52]                [9, 38, 49, 57]
                    \                            /
Level 0:            [3, 9, 26, 38, 41, 49, 52, 57]
```

**Detailed merge operations:**

**Level 3 → Level 2 merges:**

**Merge [3] and [41]:**
```
Compare 3 vs 41: 3 < 41
Result: [3, 41]
```

**Merge [52] and [26]:**
```
Compare 52 vs 26: 26 < 52
Result: [26, 52]
```

**Merge [38] and [57]:**
```
Compare 38 vs 57: 38 < 57
Result: [38, 57]
```

**Merge [9] and [49]:**
```
Compare 9 vs 49: 9 < 49
Result: [9, 49]
```

---

**Level 2 → Level 1 merges:**

**Merge [3, 41] and [26, 52]:**
```
Step 1: Compare 3 vs 26 → 3 < 26, take 3
        Result so far: [3]
Step 2: Compare 41 vs 26 → 26 < 41, take 26
        Result so far: [3, 26]
Step 3: Compare 41 vs 52 → 41 < 52, take 41
        Result so far: [3, 26, 41]
Step 4: Only 52 left, take 52
        Final: [3, 26, 41, 52]
```

**Merge [38, 57] and [9, 49]:**
```
Step 1: Compare 38 vs 9 → 9 < 38, take 9
        Result so far: [9]
Step 2: Compare 38 vs 49 → 38 < 49, take 38
        Result so far: [9, 38]
Step 3: Compare 57 vs 49 → 49 < 57, take 49
        Result so far: [9, 38, 49]
Step 4: Only 57 left, take 57
        Final: [9, 38, 49, 57]
```

---

**Level 1 → Level 0 merge:**

**Merge [3, 26, 41, 52] and [9, 38, 49, 57]:**
```
Step 1: Compare 3 vs 9 → 3 < 9, take 3
        Result: [3]
Step 2: Compare 26 vs 9 → 9 < 26, take 9
        Result: [3, 9]
Step 3: Compare 26 vs 38 → 26 < 38, take 26
        Result: [3, 9, 26]
Step 4: Compare 41 vs 38 → 38 < 41, take 38
        Result: [3, 9, 26, 38]
Step 5: Compare 41 vs 49 → 41 < 49, take 41
        Result: [3, 9, 26, 38, 41]
Step 6: Compare 52 vs 49 → 49 < 52, take 49
        Result: [3, 9, 26, 38, 41, 49]
Step 7: Compare 52 vs 57 → 52 < 57, take 52
        Result: [3, 9, 26, 38, 41, 49, 52]
Step 8: Only 57 left, take 57
        Final: [3, 9, 26, 38, 41, 49, 52, 57]
```

**Final sorted array:** [3, 9, 26, 38, 41, 49, 52, 57] ✓

---

**Key observations:**
- Recursion depth: lg 8 = 3 levels
- Total merges: 7 (4 at level 3, 2 at level 2, 1 at level 1)
- Each element participates in lg n merges
- Total work: Θ(n lg n)

---

### Exercise 2.3-2: Rewrite MERGE without Sentinels

**Problem Statement:**
The test in line 12 of the MERGE procedure can fail when either subarray has had all its elements copied back to A, in which case we would be comparing a value in one subarray to a nonexistent value in the other. Rewrite MERGE so that it uses sentinels: special values used to simplify the code. Here, use ∞ as the sentinel value. Sentinels allow the while loop of lines 11–18 to run without the test "i < nL and j < nR" in line 11. Explain why the use of sentinels is a good programming practice in this situation.

**Note:** The actual problem asks to rewrite MERGE WITHOUT sentinels (the guide has it backwards).

---

**What This Problem Is Asking:**
- Rewrite MERGE to avoid sentinel values
- Handle end-of-array conditions explicitly
- Explain trade-offs

**Framework to Solve:**
1. Identify where sentinels are used
2. Replace with explicit bounds checking
3. Handle remaining elements
4. Compare approaches

---

**Solution:**

**Original MERGE (with sentinels - from textbook):**
```
MERGE(A, p, q, r)
1  nL = q - p + 1
2  nR = r - q
3  let L[0 : nL] and R[0 : nR] be new arrays
4  for i = 0 to nL - 1
5    L[i] = A[p + i]
6  for j = 0 to nR - 1
7    R[j] = A[q + j + 1]
8  L[nL] = ∞              // sentinel
9  R[nR] = ∞              // sentinel
10 i = 0
11 j = 0
12 k = p
13 while k ≤ r
14   if L[i] ≤ R[j]
15     A[k] = L[i]
16     i = i + 1
17   else
18     A[k] = R[j]
19     j = j + 1
20   k = k + 1
```

**Rewritten MERGE (without sentinels):**
```
MERGE-NO-SENTINELS(A, p, q, r)
1  nL = q - p + 1
2  nR = r - q
3  let L[0 : nL-1] and R[0 : nR-1] be new arrays
4  for i = 0 to nL - 1
5    L[i] = A[p + i]
6  for j = 0 to nR - 1
7    R[j] = A[q + j + 1]
8  i = 0
9  j = 0
10 k = p
11 while i < nL and j < nR          // explicit bounds check
12   if L[i] ≤ R[j]
13     A[k] = L[i]
14     i = i + 1
15   else
16     A[k] = R[j]
17     j = j + 1
18   k = k + 1
19 while i < nL                      // copy remaining L
20   A[k] = L[i]
21   i = i + 1
22   k = k + 1
23 while j < nR                      // copy remaining R
24   A[k] = R[j]
25   j = j + 1
26   k = k + 1
```

**Key changes:**

**Line 11:** Added explicit bounds check
- Must check both i < nL and j < nR
- Prevents array out-of-bounds access

**Lines 19-22:** Copy remaining elements from L
- Executes if R exhausted first
- Copies all remaining elements from L to A

**Lines 23-26:** Copy remaining elements from R
- Executes if L exhausted first
- Copies all remaining elements from R to A

**Important:** Exactly one of the two "remaining" loops will execute (never both)

---

**Comparison:**

**With sentinels:**
**Advantages:**
- Simpler main loop (no bounds checking)
- Single loop handles all cases
- Slightly faster (fewer comparisons)

**Disadvantages:**
- Requires sentinel value (∞)
- Not always possible (what if all values are valid?)
- Uses extra array space
- Conceptually less clear

**Without sentinels:**
**Advantages:**
- No special sentinel value needed
- Works with any data type
- More explicit about what's happening
- Easier to understand

**Disadvantages:**
- More complex code (three loops instead of one)
- Extra bounds checking in main loop
- Slightly slower (more comparisons)

---

**When to use each:**

**Use sentinels when:**
- Clear sentinel value exists (e.g., ∞ for numbers)
- Performance is critical
- Code simplicity is priority

**Don't use sentinels when:**
- No clear sentinel value (e.g., all integers are valid)
- Clarity is more important than performance
- Working with restricted data types

**In practice:** Modern compilers optimize both versions similarly, so clarity often wins!

---

### Exercise 2.3-3: Mathematical Induction for Merge Sort

**Problem Statement:**
Use mathematical induction to show that when n ≥ 2 is an exact power of 2, the solution of the recurrence

T(n) = 2T(n/2) + n  if n = 2^k for k ≥ 1
T(2) = 2

is T(n) = n lg n.

---

**What This Problem Is Asking:**
- Prove T(n) = n lg n using induction
- Base case: n = 2
- Inductive step: assume true for n/2, prove for n
- Only for n = 2^k (exact powers of 2)

**Framework to Solve:**
1. State what we're proving
2. Prove base case
3. State inductive hypothesis
4. Prove inductive step
5. Conclude by induction

---

**Solution:**

**Claim:** For n = 2^k where k ≥ 1, T(n) = n lg n

**Proof by mathematical induction:**

---

**Base case (k = 1, n = 2):**

Given: T(2) = 2

To show: T(2) = 2 lg 2

```
2 lg 2 = 2 · 1 = 2 ✓
```

Base case holds ✓

---

**Inductive hypothesis:**

Assume that for some k ≥ 1, the formula holds for n = 2^k:
```
T(2^k) = 2^k lg(2^k) = 2^k · k
```

---

**Inductive step:**

Prove the formula holds for n = 2^(k+1):

From the recurrence:
```
T(2^(k+1)) = 2T(2^(k+1) / 2) + 2^(k+1)
           = 2T(2^k) + 2^(k+1)
```

Apply inductive hypothesis (T(2^k) = 2^k · k):
```
T(2^(k+1)) = 2(2^k · k) + 2^(k+1)
           = 2^(k+1) · k + 2^(k+1)
           = 2^(k+1)(k + 1)
```

Now verify this equals 2^(k+1) lg(2^(k+1)):
```
2^(k+1) lg(2^(k+1)) = 2^(k+1) · (k+1)
```

Therefore:
```
T(2^(k+1)) = 2^(k+1)(k+1) = 2^(k+1) lg(2^(k+1)) ✓
```

Inductive step holds ✓

---

**Conclusion:**

By mathematical induction, T(n) = n lg n for all n = 2^k where k ≥ 1. ✓

**Converting back to n:**
If n = 2^k, then k = lg n, so:
```
T(n) = n · k = n lg n ✓
```

---

**Verification with examples:**

**n = 2 (k=1):**
```
T(2) = 2 lg 2 = 2 · 1 = 2 ✓
```

**n = 4 (k=2):**
```
T(4) = 2T(2) + 4 = 2·2 + 4 = 8
4 lg 4 = 4 · 2 = 8 ✓
```

**n = 8 (k=3):**
```
T(8) = 2T(4) + 8 = 2·8 + 8 = 24
8 lg 8 = 8 · 3 = 24 ✓
```

**n = 16 (k=4):**
```
T(16) = 2T(8) + 16 = 2·24 + 16 = 64
16 lg 16 = 16 · 4 = 64 ✓
```

All examples confirm T(n) = n lg n ✓

---

### Exercise 2.3-4: Insertion Sort as Recursive Procedure

**Problem Statement:**
We can express insertion sort as a recursive procedure as follows. In order to sort A[1 : n], recursively sort the subarray A[1 : n-1] and then insert A[n] into the sorted subarray A[1 : n-1]. Write pseudocode for this recursive version of insertion sort. Give a recurrence for its worst-case running time.

---

**What This Problem Is Asking:**
- Rewrite insertion sort using recursion
- Express running time as recurrence relation
- Analyze worst-case behavior

**Framework to Solve:**
1. Identify base case
2. Identify recursive case
3. Write pseudocode
4. Derive recurrence relation
5. Solve recurrence (if asked)

---

**Solution:**

**Recursive Insertion Sort Pseudocode:**
```
RECURSIVE-INSERTION-SORT(A, n)
1  if n ≤ 1
2    return                    // base case: 0 or 1 element
3  RECURSIVE-INSERTION-SORT(A, n-1)  // sort first n-1 elements
4  key = A[n]                  // element to insert
5  j = n - 1
6  while j > 0 and A[j] > key
7    A[j+1] = A[j]
8    j = j - 1
9  A[j+1] = key
```

**Line-by-line explanation:**

**Lines 1-2:** Base case
- If n ≤ 1, array is already sorted
- Return immediately

**Line 3:** Recursive call
- Sort first n-1 elements
- After this, A[1 : n-1] is sorted

**Lines 4-9:** Insert A[n] into sorted portion
- Same as iterative insertion sort's inner loop
- Shift elements right until correct position found
- Insert key

---

**Recurrence for Worst-Case Running Time:**

**Analysis:**

**Line 3:** Recursive call on n-1 elements
- Cost: T(n-1)

**Lines 4-9:** Insert A[n] into sorted portion
- Worst case: A[n] is smallest element
- Must compare with all n-1 elements
- Must shift all n-1 elements
- Cost: Θ(n)

**Recurrence:**
```
T(n) = T(n-1) + Θ(n)  for n > 1
T(1) = Θ(1)
```

**More precisely:**
```
T(n) = T(n-1) + cn  for some constant c
T(1) = c
```

---

**Solving the Recurrence:**

**Method 1: Expansion**
```
T(n) = T(n-1) + cn
     = [T(n-2) + c(n-1)] + cn
     = T(n-2) + c(n-1) + cn
     = [T(n-3) + c(n-2)] + c(n-1) + cn
     = T(n-3) + c(n-2) + c(n-1) + cn
     ...
     = T(1) + c·2 + c·3 + ... + c(n-1) + cn
     = c + c(2 + 3 + ... + n)
     = c + c(Σᵢ₌₂ⁿ i)
     = c + c(n(n+1)/2 - 1)
     = c + c(n² + n - 2)/2
     = Θ(n²)
```

**Method 2: Substitution (guess and verify)**

Guess: T(n) = Θ(n²)

More precisely, guess T(n) ≤ cn² for some c:
```
T(n) = T(n-1) + dn  (where d is constant from Θ(n))
     ≤ c(n-1)² + dn  (by inductive hypothesis)
     = c(n² - 2n + 1) + dn
     = cn² - 2cn + c + dn
     = cn² + (d - 2c)n + c
```

For this to be ≤ cn², we need:
```
(d - 2c)n + c ≤ 0
```

This holds for large n if c ≥ d/2.

Therefore T(n) = O(n²) ✓

Similar argument shows T(n) = Ω(n²) ✓

**Conclusion: T(n) = Θ(n²)** ✓

---

**Comparison with Iterative Version:**

| Version | Worst-Case | Best-Case | Space |
|---------|------------|-----------|-------|
| Iterative | Θ(n²) | Θ(n) | O(1) |
| Recursive | Θ(n²) | Θ(n) | O(n) |

**Key difference:** Recursive version uses O(n) stack space!

**Practical implication:** Iterative version is better (no recursion overhead, less space)

---

## 📋 Quick Reference: Problem Types

### Trace Execution
**What it asks:** Show algorithm step-by-step  
**How to solve:** Execute manually, show each iteration  
**Example:** 2.1-1, 2.3-1

### Modify Algorithm
**What it asks:** Change algorithm behavior  
**How to solve:** Identify what changes, modify code  
**Example:** 2.1-2

### Prove Correctness
**What it asks:** Prove algorithm works  
**How to solve:** Loop invariant (init, maint, term)  
**Example:** 2.1-3

### Analyze Time
**What it asks:** Calculate running time  
**How to solve:** Count operations, express in Θ  
**Example:** 2.2-1, 2.2-2, 2.2-3

### Design Algorithm
**What it asks:** Create new algorithm  
**How to solve:** Choose technique, write code, analyze  
**Example:** 2.1-4, 2.3-4

### Solve Recurrence
**What it asks:** Find closed form for T(n)  
**How to solve:** Expansion, substitution, or master theorem  
**Example:** 2.3-3

---

**You've mastered Chapter 2! 🎉**

---

**End of Solutions**
