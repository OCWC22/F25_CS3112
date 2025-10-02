# Chapter 2.1 Complete Guide: Insertion Sort

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 2.1 - Insertion Sort  
**Purpose:** Master the first sorting algorithm and loop invariants

---

## 🎯 What Chapter 2.1 Is Really About

### The Big Picture

Chapter 2.1 teaches you **insertion sort** - your first complete algorithm with correctness proof.

**Mental model:** Insertion sort is like **sorting a hand of cards**:
- Pick up one card at a time from the table
- Insert it into the correct position in your sorted hand
- Repeat until all cards are sorted

**Why it's important:**
- **First complete algorithm:** Full pseudocode + correctness proof
- **Loop invariants:** Learn how to prove algorithms correct
- **Foundation:** Understanding this makes all future algorithms easier
- **Practical:** Simple, efficient for small arrays

**Key insight:** You don't just write code - you PROVE it works!

---

## 📚 The Insertion Sort Algorithm

### The Idea

**Start:** Array with n elements
**Goal:** Sort them in increasing order

**Strategy:**
1. Assume first element is "sorted"
2. Take next element (the "key")
3. Insert it into correct position in sorted portion
4. Repeat for all elements

**Visual analogy:**
```
Table (unsorted): [5, 2, 4, 6, 1, 3]
Hand (sorted):    []

Step 1: Pick 5 → Hand: [5]
Step 2: Pick 2 → Insert before 5 → Hand: [2, 5]
Step 3: Pick 4 → Insert between 2 and 5 → Hand: [2, 4, 5]
Step 4: Pick 6 → Insert at end → Hand: [2, 4, 5, 6]
Step 5: Pick 1 → Insert at start → Hand: [1, 2, 4, 5, 6]
Step 6: Pick 3 → Insert between 2 and 4 → Hand: [1, 2, 3, 4, 5, 6]
```

---

### The Pseudocode

```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i-1]
4      j = i - 1
5      while j > 0 and A[j] > key
6          A[j+1] = A[j]
7          j = j - 1
8      A[j+1] = key
```

**Line-by-line explanation:**

**Line 1:** Loop through array starting at position 2
- Why 2? Because A[1] is already "sorted" (single element)

**Line 2:** Save current element as `key`
- This is the card we're inserting

**Line 4:** Start comparing from position i-1
- j points to elements in the sorted portion

**Line 5:** While loop with two conditions:
- `j > 0`: Haven't reached start of array
- `A[j] > key`: Current element is larger than key

**Line 6:** Shift element one position right
- Make room for the key

**Line 7:** Move j left to check next element

**Line 8:** Insert key in correct position
- j+1 is where key belongs

---

### Example Execution

**Input:** A = [5, 2, 4, 6, 1, 3]

**Iteration 1 (i=2, key=2):**
```
Before: [5 | 2, 4, 6, 1, 3]
        sorted | unsorted

Compare 2 with 5: 5 > 2, shift 5 right
After:  [2, 5 | 4, 6, 1, 3]
```

**Iteration 2 (i=3, key=4):**
```
Before: [2, 5 | 4, 6, 1, 3]

Compare 4 with 5: 5 > 4, shift 5 right
Compare 4 with 2: 2 ≤ 4, stop
Insert 4 after 2

After:  [2, 4, 5 | 6, 1, 3]
```

**Iteration 3 (i=4, key=6):**
```
Before: [2, 4, 5 | 6, 1, 3]

Compare 6 with 5: 5 ≤ 6, stop
Insert 6 after 5 (no movement needed)

After:  [2, 4, 5, 6 | 1, 3]
```

**Iteration 4 (i=5, key=1):**
```
Before: [2, 4, 5, 6 | 1, 3]

Compare 1 with 6: 6 > 1, shift right
Compare 1 with 5: 5 > 1, shift right
Compare 1 with 4: 4 > 1, shift right
Compare 1 with 2: 2 > 1, shift right
j = 0, stop
Insert 1 at position 1

After:  [1, 2, 4, 5, 6 | 3]
```

**Iteration 5 (i=6, key=3):**
```
Before: [1, 2, 4, 5, 6 | 3]

Compare 3 with 6: 6 > 3, shift right
Compare 3 with 5: 5 > 3, shift right
Compare 3 with 4: 4 > 3, shift right
Compare 3 with 2: 2 ≤ 3, stop
Insert 3 after 2

After:  [1, 2, 3, 4, 5, 6]
```

**Done!**

---

## 🎓 Loop Invariants

### What Is a Loop Invariant?

**Definition:** A property that is true before and after each iteration of a loop

**Think of it as:** A promise the loop keeps

**For insertion sort:**
> At the start of each iteration of the for loop, the subarray A[1 : i-1] consists of the elements originally in A[1 : i-1], but in sorted order.

**Breaking it down:**
1. **A[1 : i-1]** - The first i-1 elements
2. **Originally in A[1 : i-1]** - Same elements (not new ones)
3. **In sorted order** - Arranged smallest to largest

---

### The Three Properties

**To prove correctness using loop invariants, show:**

#### 1. Initialization (Base Case)
**Show:** Invariant is true before first iteration

**For insertion sort:**
- Before first iteration: i = 2
- Subarray A[1 : i-1] = A[1 : 1] = just A[1]
- Single element is trivially sorted ✓
- Contains original element ✓

**Initialization holds!**

---

#### 2. Maintenance (Inductive Step)
**Show:** If invariant is true before iteration, it remains true after

**For insertion sort:**
- **Before iteration i:** A[1 : i-1] is sorted
- **During iteration:** Insert A[i] into correct position
- **After iteration:** A[1 : i] is sorted
- **Before next iteration (i+1):** A[1 : i] is sorted (which is A[1 : (i+1)-1])

**How it works:**
1. Save A[i] as key
2. Shift elements > key one position right
3. Insert key in correct position
4. Now A[1 : i] is sorted

**Maintenance holds!**

---

#### 3. Termination (Conclusion)
**Show:** When loop ends, invariant gives us what we want

**For insertion sort:**
- Loop ends when i = n + 1
- Invariant says: A[1 : i-1] is sorted
- Substitute i = n + 1: A[1 : n] is sorted
- A[1 : n] is the entire array!

**Termination holds!**

**Conclusion:** Algorithm is correct! ✓

---

### Why Loop Invariants Matter

**They're like mathematical induction:**
- **Base case** = Initialization
- **Inductive step** = Maintenance
- **Conclusion** = Termination

**They prove correctness:**
- Not just "it seems to work"
- Rigorous mathematical proof
- Works for ALL inputs

**They guide design:**
- Help you understand what loop should do
- Make bugs obvious
- Essential for complex algorithms

---

## 📊 Running Time Analysis

### Best Case

**When:** Array already sorted

**Example:** [1, 2, 3, 4, 5]

**What happens:**
- For each i, key is already in correct position
- While loop condition `A[j] > key` is always false
- No shifting needed

**Time:** Θ(n)
- Outer loop: n-1 iterations
- Inner loop: 0 iterations each time
- Total: Linear time

---

### Worst Case

**When:** Array in reverse order

**Example:** [5, 4, 3, 2, 1]

**What happens:**
- For each i, key must go all the way to position 1
- While loop runs i-1 times
- Maximum shifting

**Time:** Θ(n²)
- Outer loop: n-1 iterations
- Inner loop: 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 iterations total
- Total: Quadratic time

---

### Average Case

**When:** Random order

**What happens:**
- On average, key goes halfway through sorted portion
- While loop runs about (i-1)/2 times

**Time:** Θ(n²)
- Still quadratic, but with smaller constant
- About half as many comparisons as worst case

---

## 🔧 Pseudocode Conventions

### Important Conventions Used

**1. Array Indexing:**
```
A[1 : n] means elements A[1], A[2], ..., A[n]
Can use 0-origin or 1-origin (we use 1-origin)
```

**2. For Loops:**
```
for i = 2 to n
    // i goes from 2 to n inclusive
    // i retains value n+1 after loop exits
```

**3. While Loops:**
```
while condition
    // body executes while condition is true
```

**4. Comments:**
```
// This is a comment
```

**5. Variables:**
```
Local to procedure (not global)
```

**6. Subarrays:**
```
A[i : j] = elements from A[i] to A[j] inclusive
```

---

## 💡 Complete Example Walkthrough

### Problem: Sort [31, 41, 59, 26, 41, 58]

**Initial:** [31, 41, 59, 26, 41, 58]

**i=2, key=41:**
```
Sorted: [31]
Key: 41
Compare 41 with 31: 31 ≤ 41, stop
Result: [31, 41, 59, 26, 41, 58]
```

**i=3, key=59:**
```
Sorted: [31, 41]
Key: 59
Compare 59 with 41: 41 ≤ 59, stop
Result: [31, 41, 59, 26, 41, 58]
```

**i=4, key=26:**
```
Sorted: [31, 41, 59]
Key: 26
Compare 26 with 59: shift 59
Compare 26 with 41: shift 41
Compare 26 with 31: shift 31
Insert 26 at position 1
Result: [26, 31, 41, 59, 41, 58]
```

**i=5, key=41:**
```
Sorted: [26, 31, 41, 59]
Key: 41
Compare 41 with 59: shift 59
Compare 41 with 41: 41 ≤ 41, stop
Insert 41 after first 41
Result: [26, 31, 41, 41, 59, 58]
```

**i=6, key=58:**
```
Sorted: [26, 31, 41, 41, 59]
Key: 58
Compare 58 with 59: shift 59
Compare 58 with 41: 41 ≤ 58, stop
Insert 58 after 41
Result: [26, 31, 41, 41, 58, 59]
```

**Final:** [26, 31, 41, 41, 58, 59] ✓

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Trace Execution

**Given:** Array and algorithm
**Task:** Show step-by-step execution

**Steps:**
1. Write initial array
2. For each iteration:
   - Identify key
   - Show comparisons
   - Show shifts
   - Show final position
3. Write final array

---

### Framework 2: Write Loop Invariant

**Given:** Algorithm with loop
**Task:** State and prove loop invariant

**Steps:**
1. **State invariant:** What's true at loop start?
2. **Initialization:** Show true before first iteration
3. **Maintenance:** Show preserved by iteration
4. **Termination:** Show gives desired result

---

### Framework 3: Modify Algorithm

**Given:** Existing algorithm
**Task:** Change behavior (e.g., sort descending)

**Steps:**
1. Identify what needs to change
2. Modify comparison operators
3. Test with example
4. Verify correctness

---

### Framework 4: Design New Algorithm

**Given:** Problem description
**Task:** Write pseudocode

**Steps:**
1. Understand input/output
2. Design approach
3. Write pseudocode
4. Prove correctness with loop invariant
5. Analyze running time

---

## ⚠️ Common Mistakes

### Mistake 1: Off-by-One Errors
```
✗ for i = 1 to n  // Should start at 2!
✓ for i = 2 to n  // First element already sorted
```

### Mistake 2: Wrong Loop Condition
```
✗ while j >= 0 and A[j] > key  // Can access A[0]!
✓ while j > 0 and A[j] > key   // Stops at j=0
```

### Mistake 3: Forgetting to Save Key
```
✗ // Shifting without saving A[i] first
✓ key = A[i]  // Save before shifting!
```

### Mistake 4: Wrong Insertion Position
```
✗ A[j] = key      // Wrong position!
✓ A[j+1] = key    // Correct position
```

### Mistake 5: Incomplete Loop Invariant
```
✗ "A[1:i-1] is sorted"
✓ "A[1:i-1] contains original elements in sorted order"
```

---

## 🚀 Exam Strategy

### For Tracing Problems
- [ ] Write array state after each iteration
- [ ] Show key value clearly
- [ ] Indicate comparisons and shifts
- [ ] Verify final result

### For Loop Invariant Problems
- [ ] State invariant precisely
- [ ] Prove all three properties
- [ ] Use correct terminology
- [ ] Connect to correctness

### For Modification Problems
- [ ] Identify minimal changes needed
- [ ] Test with small example
- [ ] Verify loop invariant still holds

### For Design Problems
- [ ] Write clear pseudocode
- [ ] Include comments
- [ ] State loop invariant
- [ ] Prove correctness

### Time Management
- Trace execution: 5-10 min
- Loop invariant proof: 10-15 min
- Modify algorithm: 5-10 min
- Design algorithm: 15-20 min

---

**You're ready to master insertion sort! 🎉**

---

**End of Guide**
