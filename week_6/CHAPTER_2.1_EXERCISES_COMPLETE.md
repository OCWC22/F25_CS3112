# Chapter 2.1 Exercises: Complete Solutions with Frameworks

**Section:** 2.1 - Insertion Sort  
**Focus:** Algorithm tracing, loop invariants, and algorithm design

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Trace Execution** | "illustrate", "show operation" | Step-by-step execution | Draw array after each iteration |
| **Loop Invariant** | "state loop invariant", "prove" | Correctness proof | State invariant, prove 3 properties |
| **Modify Algorithm** | "rewrite", "sort into decreasing" | Change behavior | Modify comparison operators |
| **Design Algorithm** | "write pseudocode" | Create new algorithm | Design, code, prove correctness |
| **Binary Addition** | "add binary integers" | Implement addition | Handle carry, work right-to-left |

---

## Exercise 2.1-1: Trace Insertion Sort

### Problem Statement
Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on an array initially containing the sequence 〈31, 41, 59, 26, 41, 58〉.

---

### What This Problem Is Asking

**Task:** Show step-by-step execution of insertion sort
**Format:** Draw array state after each iteration
**Goal:** Demonstrate understanding of algorithm

### Framework
1. Write initial array
2. For each iteration (i = 2 to n):
   - Identify key
   - Show comparisons
   - Show shifts
   - Show final state
3. Mark sorted vs unsorted portions

---

### Solution

**Initial array:** [31, 41, 59, 26, 41, 58]

---

**Iteration 1 (i=2, key=41):**
```
Before: [31 | 41, 59, 26, 41, 58]
         sorted | unsorted

Compare 41 with 31: 31 ≤ 41, stop
No shifts needed

After:  [31, 41 | 59, 26, 41, 58]
```

---

**Iteration 2 (i=3, key=59):**
```
Before: [31, 41 | 59, 26, 41, 58]

Compare 59 with 41: 41 ≤ 59, stop
No shifts needed

After:  [31, 41, 59 | 26, 41, 58]
```

---

**Iteration 3 (i=4, key=26):**
```
Before: [31, 41, 59 | 26, 41, 58]

Compare 26 with 59: 59 > 26, shift 59 → [31, 41, _, 59, 41, 58]
Compare 26 with 41: 41 > 26, shift 41 → [31, _, 41, 59, 41, 58]
Compare 26 with 31: 31 > 26, shift 31 → [_, 31, 41, 59, 41, 58]
j = 0, stop
Insert 26 at position 1

After:  [26, 31, 41, 59 | 41, 58]
```

---

**Iteration 4 (i=5, key=41):**
```
Before: [26, 31, 41, 59 | 41, 58]

Compare 41 with 59: 59 > 41, shift 59 → [26, 31, 41, _, 59, 58]
Compare 41 with 41: 41 ≤ 41, stop
Insert 41 at position 4

After:  [26, 31, 41, 41, 59 | 58]
```

---

**Iteration 5 (i=6, key=58):**
```
Before: [26, 31, 41, 41, 59 | 58]

Compare 58 with 59: 59 > 58, shift 59 → [26, 31, 41, 41, _, 59]
Compare 58 with 41: 41 ≤ 58, stop
Insert 58 at position 5

After:  [26, 31, 41, 41, 58, 59]
```

---

**Final sorted array:** [26, 31, 41, 41, 58, 59] ✓

---

### Visual Summary

```
(a) [31 | 41, 59, 26, 41, 58]  i=2, key=41
         ↓

(b) [31, 41 | 59, 26, 41, 58]  i=3, key=59
            ↓

(c) [31, 41, 59 | 26, 41, 58]  i=4, key=26
               ↓ ← ← ←

(d) [26, 31, 41, 59 | 41, 58]  i=5, key=41
                     ↓ ←

(e) [26, 31, 41, 41, 59 | 58]  i=6, key=58
                        ↓ ←

(f) [26, 31, 41, 41, 58, 59]   DONE!
```

---

## Exercise 2.1-2: Loop Invariant for SUM-ARRAY

### Problem Statement
Consider the procedure SUM-ARRAY. It computes the sum of the n numbers in array A[1 : n]. State a loop invariant for this procedure, and use its initialization, maintenance, and termination properties to show that the SUM-ARRAY procedure returns the sum of the numbers in A[1 : n].

```
SUM-ARRAY(A, n)
1  sum = 0
2  for i = 1 to n
3      sum = sum + A[i]
4  return sum
```

---

### What This Problem Is Asking

**Task:** Prove correctness using loop invariant
**Algorithm:** Simple summation
**Goal:** Show invariant → correctness

### Framework
1. State loop invariant precisely
2. Prove initialization
3. Prove maintenance
4. Prove termination
5. Conclude correctness

---

### Solution

**Step 1: State Loop Invariant**

**Loop Invariant:**
> At the start of each iteration of the for loop (line 2), the variable `sum` contains the sum of the elements A[1 : i-1].

**In other words:**
```
sum = A[1] + A[2] + ... + A[i-1]
```

---

**Step 2: Initialization**

**Show:** Invariant is true before first iteration

**Before first iteration:**
- i = 1
- sum = 0 (from line 1)
- A[1 : i-1] = A[1 : 0] = empty subarray

**Sum of empty subarray = 0**

**Therefore:** sum = 0 = sum of A[1 : 0] ✓

**Initialization holds!**

---

**Step 3: Maintenance**

**Show:** If invariant is true before iteration, it remains true after

**Assume:** At start of iteration i, sum = A[1] + ... + A[i-1]

**During iteration i:**
- Line 3: sum = sum + A[i]
- New sum = (A[1] + ... + A[i-1]) + A[i]
- New sum = A[1] + ... + A[i]

**After iteration i:**
- i increments to i+1
- sum = A[1] + ... + A[i]
- This is the sum of A[1 : (i+1)-1] ✓

**Maintenance holds!**

---

**Step 4: Termination**

**Show:** When loop ends, invariant gives desired result

**Loop terminates when:** i = n + 1

**At termination:**
- Invariant says: sum = A[1] + ... + A[i-1]
- Substitute i = n + 1: sum = A[1] + ... + A[n]
- This is the sum of the entire array A[1 : n]!

**Line 4 returns sum, which is the sum of A[1 : n] ✓**

**Termination holds!**

---

**Step 5: Conclusion**

**We have shown:**
1. Invariant is true initially ✓
2. Invariant is maintained by each iteration ✓
3. When loop terminates, invariant gives us the desired result ✓

**Therefore:** SUM-ARRAY correctly returns the sum of A[1 : n] ✓

---

### Key Insights

1. **Empty subarray:** Sum of A[1 : 0] is 0 (initialization)
2. **Accumulation:** Each iteration adds one more element
3. **Final state:** When i exceeds n, we've summed all elements
4. **Simple but rigorous:** Even simple algorithms need proofs!

---

## Exercise 2.1-3: Decreasing Order Sort

### Problem Statement
Rewrite the INSERTION-SORT procedure to sort into monotonically decreasing instead of monotonically increasing order.

---

### What This Problem Is Asking

**Task:** Modify algorithm to reverse sort order
**Change:** Largest to smallest instead of smallest to largest
**Goal:** Minimal modification that works

### Framework
1. Identify what determines sort order
2. Change comparison operator
3. Verify with example
4. Write modified pseudocode

---

### Solution

**Step 1: Identify What to Change**

**Original (increasing order):**
```
Line 5: while j > 0 and A[j] > key
```

**This shifts elements that are GREATER than key to the right**

**For decreasing order:**
- We want larger elements first
- Shift elements that are SMALLER than key to the right
- Change `A[j] > key` to `A[j] < key`

---

**Step 2: Modified Pseudocode**

```
INSERTION-SORT-DECREASING(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i-1]
4      j = i - 1
5      while j > 0 and A[j] < key
6          A[j+1] = A[j]
7          j = j - 1
8      A[j+1] = key
```

**Only change:** Line 5, `A[j] > key` → `A[j] < key`

---

**Step 3: Verify with Example**

**Input:** [5, 2, 4, 6, 1, 3]

**i=2, key=2:**
```
Compare 2 with 5: 5 > 2, stop (don't shift)
Result: [5, 2, 4, 6, 1, 3]
```

**i=3, key=4:**
```
Compare 4 with 2: 2 < 4, shift 2
Compare 4 with 5: 5 > 4, stop
Insert 4 between 5 and 2
Result: [5, 4, 2, 6, 1, 3]
```

**i=4, key=6:**
```
Compare 6 with 2: 2 < 6, shift 2
Compare 6 with 4: 4 < 6, shift 4
Compare 6 with 5: 5 < 6, shift 5
Insert 6 at position 1
Result: [6, 5, 4, 2, 1, 3]
```

**i=5, key=1:**
```
Compare 1 with 2: 2 > 1, stop
Result: [6, 5, 4, 2, 1, 3]
```

**i=6, key=3:**
```
Compare 3 with 1: 1 < 3, shift 1
Compare 3 with 2: 2 < 3, shift 2
Compare 3 with 4: 4 > 3, stop
Insert 3 between 4 and 2
Result: [6, 5, 4, 3, 2, 1]
```

**Final:** [6, 5, 4, 3, 2, 1] ✓ (Decreasing order!)

---

### Key Insights

1. **Single change:** Only comparison operator needs modification
2. **Logic reversal:** Shift smaller elements instead of larger ones
3. **Same structure:** Algorithm structure unchanged
4. **Loop invariant:** Still maintains sorted subarray (just decreasing)

---

## Exercise 2.1-4: Linear Search

### Problem Statement
Consider the searching problem:
- **Input:** A sequence of n numbers 〈a₁, a₂, ..., aₙ〉 stored in array A[1 : n] and a value x
- **Output:** An index i such that x equals A[i] or the special value NIL if x does not appear in A

Write pseudocode for linear search, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is correct.

---

### What This Problem Is Asking

**Task:** Design search algorithm + prove correctness
**Approach:** Linear scan (check each element)
**Goal:** Find x or return NIL

### Framework
1. Design algorithm
2. Write pseudocode
3. State loop invariant
4. Prove correctness

---

### Solution

**Step 1: Algorithm Design**

**Approach:**
1. Start at first element
2. Check if current element equals x
3. If yes, return index
4. If no, move to next element
5. If reach end without finding, return NIL

---

**Step 2: Pseudocode**

```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

**Alternative with while loop:**

```
LINEAR-SEARCH(A, n, x)
1  i = 1
2  while i ≤ n and A[i] ≠ x
3      i = i + 1
4  if i ≤ n
5      return i
6  else
7      return NIL
```

---

**Step 3: Loop Invariant (for while version)**

**Loop Invariant:**
> At the start of each iteration of the while loop (line 2), the subarray A[1 : i-1] does not contain the value x.

**In other words:** We haven't found x in the elements we've checked so far.

---

**Step 4: Prove Correctness**

**Initialization:**
- Before first iteration: i = 1
- A[1 : i-1] = A[1 : 0] = empty subarray
- Empty subarray doesn't contain x ✓

**Maintenance:**
- **Assume:** A[1 : i-1] doesn't contain x
- **Loop condition:** A[i] ≠ x (otherwise loop exits)
- **During iteration:** i increments to i+1
- **After iteration:** A[1 : i-1] still doesn't contain x (we just checked A[i-1] and it wasn't x)
- Invariant maintained ✓

**Termination:**

**Case 1: Loop exits because A[i] == x**
- Found x at position i
- Return i ✓

**Case 2: Loop exits because i > n**
- Checked all elements A[1 : n]
- None equal x (by invariant)
- Return NIL ✓

**Correctness proven!** ✓

---

### Key Insights

1. **Two exit conditions:** Found x OR reached end
2. **Invariant tracks progress:** What we've checked so far
3. **Termination gives result:** Either found or not found
4. **Simple but complete:** Even basic algorithms need proofs

---

## Exercise 2.1-5: Binary Addition

### Problem Statement
Consider the problem of adding two n-bit binary integers a and b, stored in two n-element arrays A[0 : n-1] and B[0 : n-1], where each element is either 0 or 1. The sum c = a + b should be stored in binary form in an (n+1)-element array C[0 : n], where c = Σᵢ₌₀ⁿ C[i]·2ⁱ. Write a procedure ADD-BINARY-INTEGERS that takes as input arrays A and B, along with the length n, and returns array C holding the sum.

---

### What This Problem Is Asking

**Task:** Implement binary addition
**Input:** Two n-bit binary numbers
**Output:** (n+1)-bit binary sum
**Challenge:** Handle carry correctly

### Framework
1. Understand binary addition
2. Handle carry bit
3. Work right-to-left
4. Write pseudocode

---

### Solution

**Step 1: Understanding Binary Addition**

**Example:** Add 1011 (11) + 0111 (7)

```
    1 1 1   ← carries
    1 0 1 1
  + 0 1 1 1
  ---------
  1 0 0 1 0  = 18
```

**Rules:**
- 0 + 0 = 0, carry 0
- 0 + 1 = 1, carry 0
- 1 + 0 = 1, carry 0
- 1 + 1 = 0, carry 1
- 1 + 1 + carry = 1, carry 1

---

**Step 2: Algorithm Design**

**Approach:**
1. Start from rightmost bit (index 0)
2. Add corresponding bits plus carry
3. Store sum bit in result
4. Update carry for next position
5. Continue left to most significant bit
6. Store final carry

---

**Step 3: Pseudocode**

```
ADD-BINARY-INTEGERS(A, B, n)
1  // Create result array C[0 : n]
2  let C[0 : n] be a new array
3  carry = 0
4  for i = 0 to n - 1
5      sum = A[i] + B[i] + carry
6      C[i] = sum mod 2
7      carry = ⌊sum / 2⌋
8  C[n] = carry
9  return C
```

**Line-by-line explanation:**

**Line 2:** Create result array (one bit longer)

**Line 3:** Initialize carry to 0

**Line 4:** Loop through all bits (right to left in value, but indices 0 to n-1)

**Line 5:** Add two bits plus carry (sum can be 0, 1, 2, or 3)

**Line 6:** Store low bit of sum (sum mod 2)

**Line 7:** Calculate new carry (sum / 2, either 0 or 1)

**Line 8:** Store final carry in leftmost position

**Line 9:** Return result

---

**Step 4: Example Execution**

**Add:** A = [1, 1, 0, 1] (1011 = 11) + B = [1, 1, 1, 0] (0111 = 7)

**Note:** A[0] is rightmost bit!

**i=0 (rightmost):**
```
sum = A[0] + B[0] + carry = 1 + 1 + 0 = 2
C[0] = 2 mod 2 = 0
carry = ⌊2/2⌋ = 1
```

**i=1:**
```
sum = A[1] + B[1] + carry = 1 + 1 + 1 = 3
C[1] = 3 mod 2 = 1
carry = ⌊3/2⌋ = 1
```

**i=2:**
```
sum = A[2] + B[2] + carry = 0 + 1 + 1 = 2
C[2] = 2 mod 2 = 0
carry = ⌊2/2⌋ = 1
```

**i=3 (leftmost):**
```
sum = A[3] + B[3] + carry = 1 + 0 + 1 = 2
C[3] = 2 mod 2 = 0
carry = ⌊2/2⌋ = 1
```

**Final carry:**
```
C[4] = carry = 1
```

**Result:** C = [0, 1, 0, 0, 1] = 10010 = 18 ✓

**Verification:** 11 + 7 = 18 ✓

---

**Step 5: Loop Invariant (Optional)**

**Loop Invariant:**
> At the start of each iteration of the for loop, C[0 : i-1] contains the low-order i bits of the sum of A[0 : i-1] + B[0 : i-1] + (initial carry), and carry contains the carry-out from position i-1.

**This ensures correctness of the addition process.**

---

### Key Insights

1. **Carry propagation:** Key to binary addition
2. **Modulo and division:** Extract bit and carry
3. **Extra bit:** Result can be one bit longer
4. **Right-to-left:** Process least significant bit first
5. **Simple operations:** Just addition and bit manipulation

---

## 📋 Quick Reference: All Exercises

### 2.1-1: Trace Insertion Sort
```
Input: [31, 41, 59, 26, 41, 58]
Output: [26, 31, 41, 41, 58, 59]
Key iterations: i=4 (26 moves to front), i=6 (58 inserted)
```

### 2.1-2: SUM-ARRAY Loop Invariant
```
Invariant: sum = A[1] + ... + A[i-1]
Initialization: sum = 0 (empty sum)
Maintenance: Add A[i] each iteration
Termination: sum = A[1] + ... + A[n]
```

### 2.1-3: Decreasing Sort
```
Change: A[j] > key → A[j] < key
Effect: Shifts smaller elements right
Result: Largest to smallest order
```

### 2.1-4: Linear Search
```
Algorithm: Check each element sequentially
Return: Index if found, NIL if not
Invariant: A[1:i-1] doesn't contain x
```

### 2.1-5: Binary Addition
```
Algorithm: Add bits right-to-left with carry
Key: sum mod 2 (bit), ⌊sum/2⌋ (carry)
Result: (n+1)-bit array
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Loop Start
```
✗ for i = 1 to n
✓ for i = 2 to n (first element already sorted)
```

### Mistake 2: Incomplete Loop Invariant
```
✗ "A[1:i-1] is sorted"
✓ "A[1:i-1] contains original elements in sorted order"
```

### Mistake 3: Wrong Comparison for Decreasing
```
✗ A[j] ≥ key (allows equal, wrong position)
✓ A[j] < key (strict inequality)
```

### Mistake 4: Forgetting NIL Return
```
✗ // No return if not found
✓ return NIL (explicit not-found indicator)
```

### Mistake 5: Wrong Carry Calculation
```
✗ carry = sum / 2 (might be float!)
✓ carry = ⌊sum / 2⌋ (integer division)
```

---

## 🚀 Exam Strategy

### For Tracing (2.1-1)
- [ ] Show each iteration clearly
- [ ] Mark sorted vs unsorted
- [ ] Indicate key and shifts
- [ ] Verify final result

### For Loop Invariants (2.1-2, 2.1-4)
- [ ] State invariant precisely
- [ ] Prove all three properties
- [ ] Use correct terminology
- [ ] Connect to correctness

### For Modifications (2.1-3)
- [ ] Identify minimal change
- [ ] Test with example
- [ ] Verify correctness

### For Design (2.1-4, 2.1-5)
- [ ] Write clear pseudocode
- [ ] Include comments
- [ ] Handle edge cases
- [ ] Prove correctness

### Time Management
- Trace: 5-10 min
- Loop invariant: 10-15 min
- Modify: 5-10 min
- Design: 15-20 min

---

**You're ready to master Chapter 2.1! 🎉**

---

**End of Guide**
