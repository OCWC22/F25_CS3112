# Chapter 2.3 Exercises: Complete Solutions with Frameworks

**Section:** 2.3 - Designing Algorithms (Merge Sort)  
**Focus:** Divide-and-conquer, merge sort, and recurrence analysis

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Trace Execution** | "illustrate operation" | Show divide and merge steps | Draw tree, show merges |
| **Prove Correctness** | "argue", "prove correct" | Show algorithm works | Loop invariant with 3 properties |
| **Loop Invariant** | "state loop invariant" | Identify what's preserved | Analyze loop structure |
| **Solve Recurrence** | "show that", "solution is" | Prove running time | Induction or recursion tree |
| **Design Algorithm** | "write pseudocode" | Create new algorithm | Apply D&C paradigm |
| **Hybrid Algorithm** | "modify", "combine" | Mix two approaches | Analyze trade-offs |

---

## Exercise 2.3-1: Trace Merge Sort

### Problem Statement
Using Figure 2.4 as a model, illustrate the operation of merge sort on an array initially containing the sequence 〈3, 41, 52, 26, 38, 57, 9, 49〉.

---

### What This Problem Is Asking

**Task:** Show complete divide-and-conquer process
**Format:** Tree showing splits and merges
**Goal:** Demonstrate understanding of algorithm

### Framework
1. Show divide phase (top-down)
2. Show base cases (1-element arrays)
3. Show merge phase (bottom-up)
4. Verify final result

---

### Solution

**Initial array:** [3, 41, 52, 26, 38, 57, 9, 49]

---

**DIVIDE PHASE (Top-Down):**

```
Level 0: [3, 41, 52, 26, 38, 57, 9, 49]
                    ↓ split at q=4
         ┌──────────┴──────────┐
Level 1: [3, 41, 52, 26]    [38, 57, 9, 49]
              ↓ split              ↓ split
         ┌────┴────┐          ┌────┴────┐
Level 2: [3, 41]  [52, 26]  [38, 57]  [9, 49]
          ↓ split   ↓ split   ↓ split   ↓ split
         ┌┴┐       ┌┴┐       ┌┴┐       ┌┴┐
Level 3: [3][41]  [52][26]  [38][57]  [9][49]
```

**Base case reached: 8 subarrays of size 1**

---

**MERGE PHASE (Bottom-Up):**

```
Level 3: [3] [41]  [52] [26]  [38] [57]  [9] [49]
          ↓ merge    ↓ merge    ↓ merge    ↓ merge
Level 2: [3, 41]   [26, 52]   [38, 57]   [9, 49]
              ↓ merge              ↓ merge
         ┌────┴────┐          ┌────┴────┐
Level 1: [3, 26, 41, 52]    [9, 38, 49, 57]
                    ↓ merge
         ┌──────────┴──────────┐
Level 0: [3, 9, 26, 38, 41, 49, 52, 57]
```

---

**Detailed Merge Steps:**

**Merge [3] and [41]:**
```
L=[3], R=[41]
Compare: 3 < 41
Result: [3, 41]
```

**Merge [52] and [26]:**
```
L=[52], R=[26]
Compare: 26 < 52
Result: [26, 52]
```

**Merge [38] and [57]:**
```
L=[38], R=[57]
Compare: 38 < 57
Result: [38, 57]
```

**Merge [9] and [49]:**
```
L=[9], R=[49]
Compare: 9 < 49
Result: [9, 49]
```

**Merge [3, 41] and [26, 52]:**
```
L=[3, 41], R=[26, 52]
Compare 3 vs 26: 3 < 26 → copy 3
Compare 41 vs 26: 26 < 41 → copy 26
Compare 41 vs 52: 41 < 52 → copy 41
Copy remaining: 52
Result: [3, 26, 41, 52]
```

**Merge [38, 57] and [9, 49]:**
```
L=[38, 57], R=[9, 49]
Compare 38 vs 9: 9 < 38 → copy 9
Compare 38 vs 49: 38 < 49 → copy 38
Compare 57 vs 49: 49 < 57 → copy 49
Copy remaining: 57
Result: [9, 38, 49, 57]
```

**Merge [3, 26, 41, 52] and [9, 38, 49, 57]:**
```
L=[3, 26, 41, 52], R=[9, 38, 49, 57]
Compare 3 vs 9: 3 < 9 → copy 3
Compare 26 vs 9: 9 < 26 → copy 9
Compare 26 vs 38: 26 < 38 → copy 26
Compare 41 vs 38: 38 < 41 → copy 38
Compare 41 vs 49: 41 < 49 → copy 41
Compare 52 vs 49: 49 < 52 → copy 49
Compare 52 vs 57: 52 < 57 → copy 52
Copy remaining: 57
Result: [3, 9, 26, 38, 41, 49, 52, 57]
```

---

**Final sorted array:** [3, 9, 26, 38, 41, 49, 52, 57] ✓

---

## Exercise 2.3-2: Base Case Condition

### Problem Statement
The test in line 1 of MERGE-SORT reads "if p ≥ r" rather than "if p ≠ r". If MERGE-SORT is called with p > r, then the subarray A[p : r] is empty. Argue that as long as the initial call MERGE-SORT(A, 1, n) has n ≥ 1, the test "if p ≠ r" suffices to ensure that no recursive call has p > r.

---

### What This Problem Is Asking

**Task:** Prove "if p ≠ r" is sufficient (p > r never happens)
**Context:** Understanding base case and recursion
**Goal:** Show p > r is impossible with correct initial call

### Framework
1. Analyze initial call
2. Analyze recursive calls
3. Show p > r never occurs
4. Conclude p ≠ r sufficient

---

### Solution

**Step 1: Initial Call**

**Given:** MERGE-SORT(A, 1, n) with n ≥ 1

**This means:** p = 1, r = n ≥ 1

**So:** p ≤ r initially ✓

---

**Step 2: Recursive Calls**

**In MERGE-SORT, recursive calls are:**
```
Line 4: MERGE-SORT(A, p, q)
Line 5: MERGE-SORT(A, q+1, r)
```

**Where:** q = ⌊(p + r)/2⌋

---

**Step 3: Analyze First Recursive Call**

**Call:** MERGE-SORT(A, p, q)

**New parameters:** p' = p, r' = q

**Need to show:** p' ≤ r' (i.e., p ≤ q)

**Since q = ⌊(p + r)/2⌋:**
```
q ≥ (p + r)/2 - 1
q ≥ p + (r - p)/2 - 1
```

**If p < r (recursive case):**
```
q = ⌊(p + r)/2⌋ ≥ p

Example: p=1, r=2
q = ⌊3/2⌋ = 1 ≥ p ✓
```

**So:** p ≤ q ✓

---

**Step 4: Analyze Second Recursive Call**

**Call:** MERGE-SORT(A, q+1, r)

**New parameters:** p' = q+1, r' = r

**Need to show:** p' ≤ r' (i.e., q+1 ≤ r)

**Since q = ⌊(p + r)/2⌋:**
```
q < (p + r)/2 + 1
q + 1 < (p + r)/2 + 2
```

**If p < r:**
```
q = ⌊(p + r)/2⌋ < r

Example: p=1, r=2
q = ⌊3/2⌋ = 1 < 2 = r
So q+1 = 2 ≤ r ✓
```

**So:** q+1 ≤ r ✓

---

**Step 5: Conclusion**

**We've shown:**
1. Initial call has p ≤ r ✓
2. First recursive call has p ≤ q ✓
3. Second recursive call has q+1 ≤ r ✓

**By induction:** All recursive calls have p ≤ r

**Therefore:** p > r never occurs!

**So:** Test "if p ≠ r" is sufficient (p = r is only base case needed) ✓

**Note:** Using "if p ≥ r" is defensive programming - handles edge cases even if called incorrectly.

---

## Exercise 2.3-3: MERGE Loop Invariant

### Problem Statement
State a loop invariant for the while loop of lines 12-18 of the MERGE procedure. Show how to use it, along with the while loops of lines 20-23 and 24-27, to prove that the MERGE procedure is correct.

---

### What This Problem Is Asking

**Task:** Prove MERGE correctly merges two sorted subarrays
**Focus:** Main while loop invariant
**Goal:** Complete correctness proof

### Framework
1. State invariant for main loop
2. Prove three properties
3. Show cleanup loops handle remainder
4. Conclude correctness

---

### Solution

**Step 1: State Loop Invariant**

**Loop Invariant (for lines 12-18):**
> At the start of each iteration of the while loop, the subarray A[p : k-1] contains the k-p smallest elements of L[0 : nL-1] and R[0 : nR-1] in sorted order. Moreover, L[i] and R[j] are the smallest elements of their respective arrays that have not been copied back into A.

**Breaking it down:**
1. **A[p : k-1]:** Elements already merged
2. **k-p smallest:** Correct elements in correct order
3. **L[i] and R[j]:** Next candidates to merge

---

**Step 2: Prove Initialization**

**Before first iteration:**
- i = 0, j = 0, k = p (lines 8-10)
- A[p : k-1] = A[p : p-1] = empty subarray
- Empty subarray trivially contains 0 smallest elements in sorted order ✓
- L[0] and R[0] are first (smallest) elements of L and R ✓

**Initialization holds!**

---

**Step 3: Prove Maintenance**

**Assume:** Invariant true at start of iteration

**During iteration:**
- Compare L[i] with R[j]
- Copy smaller element to A[k]
- Increment appropriate index (i or j)
- Increment k

**Case 1: L[i] ≤ R[j]**
- L[i] is smallest remaining element overall
- Copy L[i] to A[k]
- Now A[p : k] contains k-p+1 smallest elements, sorted
- L[i+1] and R[j] are next candidates
- Invariant maintained ✓

**Case 2: L[i] > R[j]**
- R[j] is smallest remaining element overall
- Copy R[j] to A[k]
- Now A[p : k] contains k-p+1 smallest elements, sorted
- L[i] and R[j+1] are next candidates
- Invariant maintained ✓

**Maintenance holds!**

---

**Step 4: Prove Termination**

**Loop terminates when:** i = nL OR j = nR

**Case 1: i = nL (L exhausted)**
- All of L copied to A
- A[p : k-1] contains all of L plus some of R, sorted
- Remaining elements in R are all ≥ elements in A[p : k-1]
- Lines 24-27 copy remaining R to A[k : r]
- Result: A[p : r] contains all elements, sorted ✓

**Case 2: j = nR (R exhausted)**
- All of R copied to A
- A[p : k-1] contains all of R plus some of L, sorted
- Remaining elements in L are all ≥ elements in A[p : k-1]
- Lines 20-23 copy remaining L to A[k : r]
- Result: A[p : r] contains all elements, sorted ✓

**Termination holds!**

---

**Step 5: Conclusion**

**We've proven:**
1. Main loop maintains sorted order ✓
2. Cleanup loops handle remaining elements ✓
3. Final result is sorted ✓

**Therefore:** MERGE correctly merges two sorted subarrays! ✓

---

## Exercise 2.3-4: Solve Recurrence by Induction

### Problem Statement
Use mathematical induction to show that when n ≥ 2 is an exact power of 2, the solution of the recurrence T(n) = 2T(n/2) + n, with T(1) = 1, is T(n) = n lg n.

---

### What This Problem Is Asking

**Task:** Prove T(n) = n lg n using induction
**Given:** T(n) = 2T(n/2) + n, T(1) = 1
**Assumption:** n is power of 2

### Framework
1. State claim precisely
2. Prove base case
3. State inductive hypothesis
4. Prove inductive step
5. Conclude

---

### Solution

**Claim:** T(n) = n lg n for all n ≥ 1 where n is a power of 2

---

**Step 1: Base Case**

**n = 1:**
```
T(1) = 1 (given)
n lg n = 1 × lg 1 = 1 × 0 = 0 ✗
```

**Problem:** Doesn't match!

**Modified claim:** T(n) = n lg n for n ≥ 2, with T(1) = 1 as special case

**n = 2:**
```
T(2) = 2T(1) + 2 = 2(1) + 2 = 4
n lg n = 2 lg 2 = 2 × 1 = 2 ✗
```

**Still doesn't match! Let's reconsider...**

**Actually, the recurrence should be:**
```
T(n) = 2T(n/2) + n for n > 1
T(1) = 1
```

**Let's verify n=2:**
```
T(2) = 2T(1) + 2 = 2(1) + 2 = 4
But 2 lg 2 = 2
```

**The formula T(n) = n lg n doesn't include the base case constant. Let's prove it for n ≥ 2.**

**Better approach: Prove T(n) = n lg n + n**

**n = 2:**
```
T(2) = 2T(1) + 2 = 2(1) + 2 = 4
n lg n + n = 2(1) + 2 = 4 ✓
```

**Base case holds!**

---

**Step 2: Inductive Hypothesis**

**Assume:** T(k) = k lg k + k for all powers of 2 with 1 ≤ k < n

**Specifically:** T(n/2) = (n/2) lg(n/2) + (n/2)

---

**Step 3: Inductive Step**

**Prove:** T(n) = n lg n + n

**Start with recurrence:**
```
T(n) = 2T(n/2) + n
```

**Apply inductive hypothesis:**
```
T(n) = 2[(n/2) lg(n/2) + (n/2)] + n
     = n lg(n/2) + n + n
     = n(lg n - lg 2) + 2n
     = n(lg n - 1) + 2n
     = n lg n - n + 2n
     = n lg n + n ✓
```

**Inductive step holds!**

---

**Step 4: Conclusion**

**We've shown:**
- Base case: T(2) = 2 lg 2 + 2 = 4 ✓
- Inductive step: T(n) = n lg n + n ✓

**Therefore:** T(n) = n lg n + n for all n ≥ 2 (powers of 2)

**In Θ-notation:** T(n) = Θ(n lg n) ✓

**Note:** The "+n" is a lower-order term that doesn't affect asymptotic growth.

---

## Exercise 2.3-5: Recursive Insertion Sort

### Problem Statement
You can also think of insertion sort as a recursive algorithm. In order to sort A[1 : n], recursively sort the subarray A[1 : n-1] and then insert A[n] into the sorted subarray A[1 : n-1]. Write pseudocode for this recursive version of insertion sort. Give a recurrence for its worst-case running time.

---

### What This Problem Is Asking

**Task:** Rewrite insertion sort recursively
**Goal:** Show insertion sort can use recursion
**Analysis:** Derive recurrence relation

### Framework
1. Design recursive structure
2. Identify base case
3. Write pseudocode
4. Derive recurrence
5. Solve recurrence

---

### Solution

**Step 1: Recursive Design**

**Idea:**
- To sort A[1 : n], first sort A[1 : n-1]
- Then insert A[n] into correct position

**Base case:** n = 1 (single element already sorted)

**Recursive case:** Sort A[1 : n-1], then insert A[n]

---

**Step 2: Pseudocode**

```
RECURSIVE-INSERTION-SORT(A, n)
1  if n ≤ 1
2      return
3  RECURSIVE-INSERTION-SORT(A, n-1)
4  // Insert A[n] into sorted A[1 : n-1]
5  key = A[n]
6  j = n - 1
7  while j > 0 and A[j] > key
8      A[j+1] = A[j]
9      j = j - 1
10 A[j+1] = key
```

**Lines 1-2:** Base case (0 or 1 element)

**Line 3:** Recursively sort first n-1 elements

**Lines 5-10:** Insert A[n] (same as iterative version)

---

**Step 3: Derive Recurrence**

**Worst case:** A[n] must go to position 1

**Time for sorting A[1 : n]:**
- Sort A[1 : n-1]: T(n-1)
- Insert A[n]: Θ(n) in worst case (n-1 comparisons + shifts)

**Recurrence:**
```
T(n) = T(n-1) + Θ(n)
T(1) = Θ(1)
```

---

**Step 4: Solve Recurrence**

**Expand:**
```
T(n) = T(n-1) + cn
     = [T(n-2) + c(n-1)] + cn
     = T(n-2) + c(n-1) + cn
     = [T(n-3) + c(n-2)] + c(n-1) + cn
     = ...
     = T(1) + c(2 + 3 + ... + n)
     = c₁ + c(2 + 3 + ... + n)
     = c₁ + c[n(n+1)/2 - 1]
     = c₁ + cn(n+1)/2 - c
     = Θ(n²)
```

**Worst-case running time: T(n) = Θ(n²)**

---

**Step 5: Comparison**

**Recursive vs Iterative:**
- Same worst-case time: Θ(n²)
- Same algorithm, different implementation
- Recursive has function call overhead
- Iterative generally preferred

---

## Exercise 2.3-6: Binary Search

### Problem Statement
Observe that if the subarray being searched is already sorted, the searching algorithm can check the midpoint of the subarray against v and eliminate half of the subarray from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is Θ(lg n).

---

### What This Problem Is Asking

**Task:** Design binary search algorithm
**Approach:** Divide-and-conquer for searching
**Goal:** Achieve Θ(lg n) search time

### Framework
1. Design algorithm (iterative or recursive)
2. Write pseudocode
3. Analyze worst case
4. Prove Θ(lg n)

---

### Solution

**Step 1: Algorithm Design**

**Idea:**
1. Check middle element
2. If match, return index
3. If target < middle, search left half
4. If target > middle, search right half
5. Repeat until found or exhausted

---

**Step 2: Recursive Pseudocode**

```
BINARY-SEARCH(A, p, r, x)
1  if p > r
2      return NIL
3  q = ⌊(p + r)/2⌋
4  if A[q] == x
5      return q
6  else if x < A[q]
7      return BINARY-SEARCH(A, p, q-1, x)
8  else
9      return BINARY-SEARCH(A, q+1, r, x)
```

**Initial call:** BINARY-SEARCH(A, 1, n, x)

---

**Step 3: Iterative Pseudocode**

```
ITERATIVE-BINARY-SEARCH(A, n, x)
1  p = 1
2  r = n
3  while p ≤ r
4      q = ⌊(p + r)/2⌋
5      if A[q] == x
6          return q
7      else if x < A[q]
8          r = q - 1
9      else
10         p = q + 1
11 return NIL
```

---

**Step 4: Worst-Case Analysis**

**Worst case:** Element not in array

**What happens:**
- Each iteration eliminates half the search space
- Start with n elements
- After 1 comparison: n/2 elements
- After 2 comparisons: n/4 elements
- After k comparisons: n/2^k elements
- Stop when n/2^k = 1, i.e., k = lg n

**Worst-case comparisons:** lg n + 1

**Recurrence (recursive version):**
```
T(n) = T(n/2) + Θ(1)
T(1) = Θ(1)
```

**Solution (by Master Theorem):**
```
a = 1, b = 2, f(n) = Θ(1)
n^(log_b a) = n^0 = 1
Case 2: f(n) = Θ(1) = Θ(1 × (lg n)^0)
Solution: T(n) = Θ(lg n) ✓
```

---

**Step 5: Argument for Θ(lg n)**

**Upper bound:**
- Each comparison eliminates half
- At most lg n + 1 comparisons
- T(n) = O(lg n)

**Lower bound:**
- Must eliminate all but one element
- Each comparison eliminates at most half
- Need at least lg n comparisons
- T(n) = Ω(lg n)

**Therefore:** T(n) = Θ(lg n) ✓

---

## Exercise 2.3-7: Binary Search in Insertion Sort

### Problem Statement
The while loop of lines 5-7 of INSERTION-SORT uses linear search to scan backward through the sorted subarray A[1 : j-1]. What if insertion sort used binary search instead? Would that improve the overall worst-case running time to Θ(n lg n)?

---

### What This Problem Is Asking

**Task:** Analyze hybrid algorithm
**Question:** Does binary search improve insertion sort?
**Goal:** Understand why or why not

### Framework
1. Identify what binary search improves
2. Identify what it doesn't improve
3. Analyze total running time
4. Conclude

---

### Solution

**Step 1: What Binary Search Improves**

**Finding insertion position:**
- Linear search: Θ(i) comparisons
- Binary search: Θ(lg i) comparisons

**For all iterations:**
- Linear: Σᵢ₌₂ⁿ i = Θ(n²) comparisons
- Binary: Σᵢ₌₂ⁿ lg i = Θ(n lg n) comparisons

**Comparisons improved!** ✓

---

**Step 2: What Binary Search Doesn't Improve**

**Shifting elements:**
- Must still shift elements to make room
- Shifting is Θ(i) in worst case (can't avoid)
- Binary search doesn't help with shifting!

**For all iterations:**
- Shifts: Σᵢ₌₂ⁿ i = Θ(n²) shifts

**Shifts unchanged!** ✗

---

**Step 3: Total Running Time**

**With binary search:**
```
Comparisons: Θ(n lg n)
Shifts: Θ(n²)
Total: Θ(n lg n) + Θ(n²) = Θ(n²)
```

**Without binary search:**
```
Comparisons: Θ(n²)
Shifts: Θ(n²)
Total: Θ(n²)
```

**Same asymptotic time!**

---

**Step 4: Conclusion**

**Answer:** NO, binary search does NOT improve worst-case to Θ(n lg n)

**Why not:**
- Comparisons reduced to Θ(n lg n) ✓
- But shifts still Θ(n²) ✗
- Shifts dominate the running time
- Total remains Θ(n²)

**Key insight:** Bottleneck is shifting, not finding position!

**Practical note:** Binary search might improve constant factors (fewer comparisons), but doesn't change asymptotic complexity.

---

## Exercise 2.3-8: Two-Sum Problem

### Problem Statement
Describe an algorithm that, given a set S of n integers and another integer x, determines whether S contains two elements that sum to exactly x. Your algorithm should take Θ(n lg n) time in the worst case.

---

### What This Problem Is Asking

**Task:** Design algorithm for two-sum problem
**Constraint:** Must be Θ(n lg n)
**Hint:** Use sorting + searching

### Framework
1. Design approach
2. Write pseudocode
3. Analyze running time
4. Verify Θ(n lg n)

---

### Solution

**Step 1: Algorithm Design**

**Approach:**
1. Sort array S (Θ(n lg n))
2. For each element S[i], search for x - S[i] using binary search
3. If found, return TRUE
4. If none found, return FALSE

**Alternative (more efficient):**
1. Sort array S (Θ(n lg n))
2. Use two pointers (left and right)
3. If sum < x, move left pointer right
4. If sum > x, move right pointer left
5. If sum = x, return TRUE

---

**Step 2: Pseudocode (Two-Pointer Approach)**

```
TWO-SUM(S, n, x)
1  MERGE-SORT(S, 1, n)           // sort array
2  left = 1
3  right = n
4  while left < right
5      sum = S[left] + S[right]
6      if sum == x
7          return TRUE
8      else if sum < x
9          left = left + 1
10     else
11         right = right - 1
12 return FALSE
```

---

**Step 3: Alternative (Binary Search Approach)**

```
TWO-SUM-BINARY(S, n, x)
1  MERGE-SORT(S, 1, n)           // sort array
2  for i = 1 to n
3      target = x - S[i]
4      j = BINARY-SEARCH(S, 1, n, target)
5      if j ≠ NIL and j ≠ i
6          return TRUE
7  return FALSE
```

---

**Step 4: Running Time Analysis**

**Two-pointer approach:**
```
Sorting: Θ(n lg n)
Two-pointer scan: Θ(n) (each pointer moves at most n times)
Total: Θ(n lg n) + Θ(n) = Θ(n lg n) ✓
```

**Binary search approach:**
```
Sorting: Θ(n lg n)
Loop: n iterations
Binary search per iteration: Θ(lg n)
Total: Θ(n lg n) + n × Θ(lg n) = Θ(n lg n) + Θ(n lg n) = Θ(n lg n) ✓
```

**Both achieve Θ(n lg n)!**

---

**Step 5: Example**

**Input:** S = [3, 5, 2, 8, 1], x = 10

**After sorting:** S = [1, 2, 3, 5, 8]

**Two-pointer approach:**
```
left=1, right=5: 1+8=9 < 10 → left++
left=2, right=5: 2+8=10 = 10 → return TRUE ✓
```

**Found: S[2]=2 and S[5]=8 sum to 10!**

---

### Answer

**Algorithm:** Sort array, then use two-pointer technique

**Pseudocode:** (See above)

**Running time:**
- Sorting: Θ(n lg n)
- Two-pointer scan: Θ(n)
- Total: Θ(n lg n) ✓

**Correctness:**
- Sorting preserves all elements
- Two-pointer checks all pairs efficiently
- Returns TRUE if pair exists, FALSE otherwise

---

## 📋 Quick Reference: All Exercises

### 2.3-1: Trace Merge Sort
```
Input: [3, 41, 52, 26, 38, 57, 9, 49]
Divide: Split recursively to 1-element arrays
Merge: Combine bottom-up
Output: [3, 9, 26, 38, 41, 49, 52, 57]
```

### 2.3-2: Base Case Sufficiency
```
Initial: p ≤ r (given n ≥ 1)
Recursive calls: Always maintain p ≤ r
Conclusion: p > r never occurs
Therefore: "if p ≠ r" sufficient
```

### 2.3-3: MERGE Loop Invariant
```
Invariant: A[p:k-1] has k-p smallest, sorted
Init: Empty subarray
Maint: Copy smaller element
Term: All elements merged, sorted
```

### 2.3-4: Solve T(n) = 2T(n/2) + n
```
Claim: T(n) = n lg n + n
Base: T(2) = 4 = 2 lg 2 + 2 ✓
Inductive: T(n) = n lg n + n ✓
Result: Θ(n lg n)
```

### 2.3-5: Recursive Insertion Sort
```
Pseudocode: Sort A[1:n-1], insert A[n]
Recurrence: T(n) = T(n-1) + Θ(n)
Solution: T(n) = Θ(n²)
Same as iterative version
```

### 2.3-6: Binary Search
```
Algorithm: Check middle, eliminate half
Recurrence: T(n) = T(n/2) + Θ(1)
Solution: T(n) = Θ(lg n)
Much faster than linear search!
```

### 2.3-7: Binary Search in Insertion Sort
```
Comparisons: Θ(n lg n) (improved!)
Shifts: Θ(n²) (unchanged!)
Total: Θ(n²) (no improvement)
Bottleneck is shifting, not finding
```

### 2.3-8: Two-Sum Problem
```
Algorithm: Sort + two-pointer
Sort: Θ(n lg n)
Scan: Θ(n)
Total: Θ(n lg n) ✓
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Merge Bounds
```
✗ MERGE(A, p, q, r) with q = r
✓ Require p ≤ q < r
```

### Mistake 2: Forgetting Cleanup Loops
```
✗ Only main merge loop
✓ Three loops (main + two cleanup)
```

### Mistake 3: Wrong Recurrence
```
✗ T(n) = T(n/2) + n (only one call)
✓ T(n) = 2T(n/2) + n (two calls)
```

### Mistake 4: Binary Search Improvement
```
✗ "Binary search makes insertion sort Θ(n lg n)"
✓ Still Θ(n²) due to shifting
```

### Mistake 5: Two-Sum Brute Force
```
✗ Check all pairs: Θ(n²)
✓ Sort + two-pointer: Θ(n lg n)
```

---

## 🚀 Exam Strategy

### For Tracing (2.3-1)
- [ ] Draw complete tree
- [ ] Show all splits
- [ ] Show all merges
- [ ] Verify result

### For Proofs (2.3-2, 2.3-3)
- [ ] State claim clearly
- [ ] Prove systematically
- [ ] Handle all cases
- [ ] Conclude explicitly

### For Recurrences (2.3-4, 2.3-5)
- [ ] Write recurrence correctly
- [ ] Solve using appropriate method
- [ ] Express in Θ-notation
- [ ] Verify solution

### For Design (2.3-6, 2.3-8)
- [ ] Choose right approach
- [ ] Write clear pseudocode
- [ ] Analyze running time
- [ ] Verify correctness

### Time Management
- Trace: 10-15 min
- Proofs: 15-20 min
- Recurrence: 10-15 min
- Design: 15-25 min

---

**You're ready to master merge sort! 🎉**

---

**End of Guide**
