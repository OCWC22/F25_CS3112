# Chapter 2 Complete Guide: Getting Started with Algorithm Analysis

**Course:** CS3112 - Introduction to Algorithms  
**Sections:** 2.1 (Insertion Sort), 2.2 (Analyzing Algorithms), 2.3 (Designing Algorithms)  
**Purpose:** Master algorithm design, analysis, and correctness proofs

---

## 🎯 What Chapter 2 Is Really About

### The Big Picture

Chapter 2 teaches you **three fundamental skills** for working with algorithms:

1. **Understanding algorithms** (2.1) - How to read, understand, and prove correctness
2. **Analyzing algorithms** (2.2) - How to calculate running time mathematically
3. **Designing algorithms** (2.3) - How to create better algorithms using divide-and-conquer

**Mental model:** This chapter is your "algorithm toolkit" - it gives you the basic tools you'll use throughout the entire course.

---

## 📚 Section 2.1: Insertion Sort

### What This Section Teaches

**Core concepts:**
1. How to read and understand pseudocode
2. Loop invariants (proving correctness)
3. The insertion sort algorithm
4. Pseudocode conventions

**Why it matters:** Before you can analyze or design algorithms, you need to understand how they work and prove they're correct.

---

### The Sorting Problem

**Input:** A sequence of n numbers ⟨a₁, a₂, ..., aₙ⟩

**Output:** A permutation (reordering) ⟨a'₁, a'₂, ..., a'ₙ⟩ such that a'₁ ≤ a'₂ ≤ ... ≤ a'ₙ

**Key terminology:**
- **Keys:** The values being sorted
- **Satellite data:** Additional data associated with keys
- **Record:** Key + satellite data together

**Example:**
```
Input:  [5, 2, 4, 6, 1, 3]
Output: [1, 2, 3, 4, 5, 6]
```

---

### Insertion Sort: The Card-Sorting Analogy

**Real-world analogy:**
Imagine sorting a hand of playing cards:
1. Start with empty left hand
2. Cards in pile on table (right side)
3. Pick up one card at a time from pile
4. Insert it into correct position in left hand
5. Compare with cards already in left hand (right to left)
6. Insert when you find correct spot

**Key insight:** Left hand is always sorted!

---

### The Algorithm (Pseudocode)

```
INSERTION-SORT(A, n)
1  for i = 2 to n
2    key = A[i]
3    // Insert A[i] into the sorted subarray A[1 : i-1]
4    j = i - 1
5    while j > 0 and A[j] > key
6      A[j+1] = A[j]
7      j = j - 1
8    A[j+1] = key
```

**Line-by-line explanation:**

**Line 1:** Loop through array starting at position 2 (assume first element already "sorted")
- `i` is the "current card" being inserted
- Runs n-1 times (from i=2 to i=n)

**Line 2:** Store current element in `key`
- This is the value we're trying to insert into sorted portion

**Line 3:** Comment explaining what we're doing
- A[1 : i-1] is the sorted portion (left hand)
- We're inserting A[i] into this sorted portion

**Line 4:** Start comparing from position i-1 (rightmost of sorted portion)
- `j` will move left through the sorted portion

**Line 5:** While loop with two conditions:
- `j > 0`: Haven't reached beginning of array
- `A[j] > key`: Current element is larger than key (need to shift right)

**Line 6:** Shift A[j] one position to the right
- Makes room for key to be inserted

**Line 7:** Move j one position to the left
- Continue comparing with next element

**Line 8:** Insert key into correct position
- j+1 is the correct spot (either found smaller element or reached beginning)

---

### Example Trace

**Input:** A = [5, 2, 4, 6, 1, 3], n = 6

**Iteration i=2 (key=2):**
```
Initial: [5, 2, 4, 6, 1, 3]
         sorted: [5]  current: 2

Compare 2 with 5: 5 > 2, shift right
Result:  [5, 5, 4, 6, 1, 3]
Insert 2 at position 1
Final:   [2, 5, 4, 6, 1, 3]
         sorted: [2, 5]
```

**Iteration i=3 (key=4):**
```
Initial: [2, 5, 4, 6, 1, 3]
         sorted: [2, 5]  current: 4

Compare 4 with 5: 5 > 4, shift right
Result:  [2, 5, 5, 6, 1, 3]
Compare 4 with 2: 2 ≤ 4, stop
Insert 4 at position 2
Final:   [2, 4, 5, 6, 1, 3]
         sorted: [2, 4, 5]
```

**Iteration i=4 (key=6):**
```
Initial: [2, 4, 5, 6, 1, 3]
         sorted: [2, 4, 5]  current: 6

Compare 6 with 5: 5 ≤ 6, stop immediately
No shifts needed
Final:   [2, 4, 5, 6, 1, 3]
         sorted: [2, 4, 5, 6]
```

**Iteration i=5 (key=1):**
```
Initial: [2, 4, 5, 6, 1, 3]
         sorted: [2, 4, 5, 6]  current: 1

Compare 1 with 6: 6 > 1, shift right
Compare 1 with 5: 5 > 1, shift right
Compare 1 with 4: 4 > 1, shift right
Compare 1 with 2: 2 > 1, shift right
Result:  [2, 2, 4, 5, 6, 3]
Insert 1 at position 1
Final:   [1, 2, 4, 5, 6, 3]
         sorted: [1, 2, 4, 5, 6]
```

**Iteration i=6 (key=3):**
```
Initial: [1, 2, 4, 5, 6, 3]
         sorted: [1, 2, 4, 5, 6]  current: 3

Compare 3 with 6: 6 > 3, shift right
Compare 3 with 5: 5 > 3, shift right
Compare 3 with 4: 4 > 3, shift right
Compare 3 with 2: 2 ≤ 3, stop
Insert 3 at position 3
Final:   [1, 2, 3, 4, 5, 6]
         sorted: [1, 2, 3, 4, 5, 6]
```

**Done!** Array is fully sorted.

---

### Loop Invariants: Proving Correctness

**What is a loop invariant?**
A statement that is true before each iteration of a loop.

**Why use loop invariants?**
To prove that an algorithm is correct (does what it's supposed to do).

**The three properties to prove:**

1. **Initialization:** True before first iteration
2. **Maintenance:** If true before iteration k, remains true before iteration k+1
3. **Termination:** When loop ends, invariant + termination condition = correctness

**Analogy to mathematical induction:**
- Initialization = Base case
- Maintenance = Inductive step
- Termination = What we wanted to prove

---

### Loop Invariant for Insertion Sort

**Statement:**
> At the start of each iteration of the for loop (lines 1-8), the subarray A[1 : i-1] consists of the elements originally in A[1 : i-1], but in sorted order.

**Proof:**

**1. Initialization (i = 2):**
- Before first iteration, i = 2
- Subarray A[1 : i-1] = A[1 : 1] = just A[1]
- A single element is always sorted ✓
- Contains original element from A[1] ✓
- **Loop invariant holds before first iteration**

**2. Maintenance (iteration i → i+1):**
- **Assume:** A[1 : i-1] is sorted and contains original elements
- **During iteration i:**
  - key = A[i]
  - While loop shifts elements A[i-1], A[i-2], ... right
  - Stops when finds correct position for key
  - Inserts key into correct position
- **After iteration i:**
  - A[1 : i] is sorted and contains original elements
  - Incrementing i to i+1 preserves invariant
- **Loop invariant holds before next iteration**

**3. Termination (i = n+1):**
- Loop terminates when i > n (i.e., i = n+1)
- Substitute i = n+1 into loop invariant:
  - A[1 : n] consists of original elements in sorted order
- **This is exactly what we wanted to prove!**
- **Algorithm is correct** ✓

---

### Pseudocode Conventions (Important!)

**1. Indentation = block structure**
```
for i = 1 to n
  statement1    // inside for loop
  statement2    // inside for loop
statement3      // outside for loop
```

**2. Loop counters retain value after exit**
```
for i = 1 to n
  // do something
// After loop: i = n+1 (not n!)
```

**3. Comments use "//"**
```
x = 5  // This is a comment
```

**4. Arrays can use any indexing**
- Usually 1-origin: A[1], A[2], ..., A[n]
- Sometimes 0-origin: A[0], A[1], ..., A[n-1]
- We'll specify explicitly

**5. Subarray notation A[i : j]**
- Means elements A[i], A[i+1], ..., A[j]
- Inclusive on both ends

**6. Objects use dot notation**
```
x.attribute    // Access attribute of object x
x.f.g          // Cascade: (x.f).g
```

**7. Pointers and NIL**
- Variables are pointers to objects/arrays
- NIL means "points to nothing"
- Assignment copies pointer, not data

**8. Parameter passing**
- Primitives: passed by value (copy)
- Objects/arrays: passed by pointer (reference)
- Changes to object attributes are visible to caller

---

## 📊 Section 2.2: Analyzing Algorithms

### What This Section Teaches

**Core concepts:**
1. RAM (Random Access Machine) model
2. Counting primitive operations
3. Best-case, worst-case, average-case analysis
4. Order of growth (asymptotic notation preview)

**Why it matters:** You need to predict how long algorithms will take before implementing them.

---

### The RAM Model

**What is it?**
A simplified computer model for analyzing algorithms.

**Key assumptions:**
1. **Instructions execute one at a time** (no parallelism)
2. **Each instruction takes constant time:**
   - Arithmetic: +, -, ×, /, %
   - Comparison: <, >, ≤, ≥, ==, ≠
   - Assignment: =
   - Array access: A[i]
   - Control flow: if, while, for, return
3. **Memory access is constant time** (no cache effects)
4. **Data types are reasonable size** (not arbitrarily large integers)

**What we ignore:**
- Cache effects
- Virtual memory
- Parallel processing
- Instruction pipelining

**Why this model?**
- Simple enough to analyze
- Accurate enough for practical predictions
- Focuses on algorithm, not hardware

---

### Analyzing Insertion Sort

**Goal:** Express running time as function of input size n

**Approach:** Count how many times each line executes

**The algorithm with costs:**
```
INSERTION-SORT(A, n)
                                    cost    times
1  for i = 2 to n                   c₁      n
2    key = A[i]                     c₂      n-1
3    // Insert A[i] into sorted     0       n-1
4    j = i - 1                      c₄      n-1
5    while j > 0 and A[j] > key     c₅      Σᵢ₌₂ⁿ tᵢ
6      A[j+1] = A[j]                c₆      Σᵢ₌₂ⁿ (tᵢ-1)
7      j = j - 1                    c₇      Σᵢ₌₂ⁿ (tᵢ-1)
8    A[j+1] = key                   c₈      n-1
```

**Notation:**
- cᵢ = cost of executing line i once
- tᵢ = number of times while loop test executes for iteration i

**Key insight:** tᵢ depends on the input!

---

### Best-Case Analysis

**When does best case occur?**
Array is already sorted!

**Why?**
- While loop condition (line 5) always false on first check
- No shifting needed
- tᵢ = 1 for all i (just one comparison per iteration)

**Calculating T(n):**
```
T(n) = c₁·n + c₂·(n-1) + c₄·(n-1) + c₅·(n-1) + c₈·(n-1)
     = (c₁ + c₂ + c₄ + c₅ + c₈)·n - (c₂ + c₄ + c₅ + c₈)
     = an + b  [for some constants a, b]
```

**Result:** T(n) = Θ(n) - **linear time**

**Example:** [1, 2, 3, 4, 5] → Already sorted, minimal work

---

### Worst-Case Analysis

**When does worst case occur?**
Array is reverse sorted!

**Why?**
- While loop compares with ALL elements in sorted portion
- Maximum shifting
- tᵢ = i for all i (compare with all i-1 elements, plus one extra test)

**Calculating T(n):**
```
Σᵢ₌₂ⁿ tᵢ = Σᵢ₌₂ⁿ i = 2 + 3 + ... + n = n(n+1)/2 - 1

Σᵢ₌₂ⁿ (tᵢ-1) = Σᵢ₌₂ⁿ (i-1) = 1 + 2 + ... + (n-1) = n(n-1)/2

T(n) = c₁·n + c₂·(n-1) + c₄·(n-1) + c₅·(n(n+1)/2 - 1) 
       + c₆·(n(n-1)/2) + c₇·(n(n-1)/2) + c₈·(n-1)
     = (c₅/2 + c₆/2 + c₇/2)·n² + (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)·n 
       - (c₂ + c₄ + c₅ + c₈)
     = an² + bn + c  [for some constants a, b, c]
```

**Result:** T(n) = Θ(n²) - **quadratic time**

**Example:** [5, 4, 3, 2, 1] → Reverse sorted, maximum work

---

### Average-Case Analysis

**Assumption:** All permutations equally likely

**Key observation:** On average, half the elements in sorted portion are larger than key

**Calculating:**
- tᵢ ≈ i/2 on average
- Similar analysis to worst case, but with factor of 1/2

**Result:** T(n) = Θ(n²) - **still quadratic!**

**Important:** Average case has same order of growth as worst case for insertion sort

---

### Order of Growth

**Key idea:** Focus on highest-order term, ignore constants

**Why?**
- For large n, highest-order term dominates
- Constants depend on hardware/implementation
- We want hardware-independent analysis

**Example:**
```
T(n) = 5n² + 3n + 2

For large n:
- 5n² dominates
- 3n becomes negligible
- 2 becomes negligible

So: T(n) = Θ(n²)
```

**Comparison:**
```
n = 10:   T(n) = 500 + 30 + 2 = 532
n = 100:  T(n) = 50000 + 300 + 2 = 50302  (n² term is 99.4%)
n = 1000: T(n) = 5000000 + 3000 + 2 = 5003002  (n² term is 99.94%)
```

---

## 🔧 Section 2.3: Designing Algorithms - Divide and Conquer

### What This Section Teaches

**Core concepts:**
1. Divide-and-conquer paradigm
2. Merge sort algorithm
3. Analyzing recursive algorithms
4. Recurrence relations

**Why it matters:** Learn to design algorithms that are fundamentally faster than naive approaches

---

### The Divide-and-Conquer Paradigm

**Three steps:**

**1. Divide:** Break problem into smaller subproblems
- Subproblems are smaller instances of same problem
- Usually divide into roughly equal parts

**2. Conquer:** Solve subproblems recursively
- Base case: solve directly if small enough
- Recursive case: apply same algorithm to subproblems

**3. Combine:** Merge solutions to subproblems into solution for original problem

**Key insight:** Often, the "combine" step is where the magic happens!

---

### Merge Sort Algorithm

**High-level idea:**
1. Divide array into two halves
2. Recursively sort each half
3. Merge the two sorted halves

**Why it works:**
- Merging two sorted arrays is easy (linear time)
- Recursion handles the sorting

---

### The MERGE Procedure

**Purpose:** Merge two sorted subarrays into one sorted array

**Input:**
- Array A
- Indices p, q, r where p ≤ q < r
- A[p : q] is sorted
- A[q+1 : r] is sorted

**Output:**
- A[p : r] is sorted

**Algorithm:**
```
MERGE(A, p, q, r)
1  nL = q - p + 1        // length of A[p : q]
2  nR = r - q            // length of A[q+1 : r]
3  let L[0 : nL-1] and R[0 : nR-1] be new arrays
4  for i = 0 to nL - 1
5    L[i] = A[p + i]     // copy A[p : q] to L
6  for j = 0 to nR - 1
7    R[j] = A[q + j + 1] // copy A[q+1 : r] to R
8  i = 0                 // index for L
9  j = 0                 // index for R
10 k = p                 // index for A
11 while i < nL and j < nR
12   if L[i] ≤ R[j]
13     A[k] = L[i]
14     i = i + 1
15   else
16     A[k] = R[j]
17     j = j + 1
18   k = k + 1
19 while i < nL          // copy remaining L elements
20   A[k] = L[i]
21   i = i + 1
22   k = k + 1
23 while j < nR          // copy remaining R elements
24   A[k] = R[j]
25   j = j + 1
26   k = k + 1
```

**Key steps:**

**Lines 1-7:** Copy subarrays to temporary arrays L and R
- L holds A[p : q]
- R holds A[q+1 : r]

**Lines 8-10:** Initialize indices
- i for L (starts at 0)
- j for R (starts at 0)
- k for A (starts at p)

**Lines 11-18:** Main merge loop
- Compare L[i] with R[j]
- Copy smaller element to A[k]
- Increment appropriate index
- Continue until one array exhausted

**Lines 19-26:** Copy remaining elements
- One array will be exhausted first
- Copy remaining elements from other array

---

### MERGE Example

**Input:**
```
A = [2, 4, 5, 7, 1, 2, 3, 6]
p = 0, q = 3, r = 7

A[p : q] = [2, 4, 5, 7]  (sorted)
A[q+1 : r] = [1, 2, 3, 6]  (sorted)
```

**Step-by-step:**

**Initial:**
```
L = [2, 4, 5, 7]
R = [1, 2, 3, 6]
i = 0, j = 0, k = 0
```

**Iteration 1:** L[0]=2, R[0]=1 → 1 < 2, copy R[0]
```
A = [1, 4, 5, 7, 1, 2, 3, 6]
i = 0, j = 1, k = 1
```

**Iteration 2:** L[0]=2, R[1]=2 → 2 ≤ 2, copy L[0]
```
A = [1, 2, 5, 7, 1, 2, 3, 6]
i = 1, j = 1, k = 2
```

**Iteration 3:** L[1]=4, R[1]=2 → 2 < 4, copy R[1]
```
A = [1, 2, 2, 7, 1, 2, 3, 6]
i = 1, j = 2, k = 3
```

**Iteration 4:** L[1]=4, R[2]=3 → 3 < 4, copy R[2]
```
A = [1, 2, 2, 3, 1, 2, 3, 6]
i = 1, j = 3, k = 4
```

**Iteration 5:** L[1]=4, R[3]=6 → 4 < 6, copy L[1]
```
A = [1, 2, 2, 3, 4, 2, 3, 6]
i = 2, j = 3, k = 5
```

**Iteration 6:** L[2]=5, R[3]=6 → 5 < 6, copy L[2]
```
A = [1, 2, 2, 3, 4, 5, 3, 6]
i = 3, j = 3, k = 6
```

**Iteration 7:** L[3]=7, R[3]=6 → 6 < 7, copy R[3]
```
A = [1, 2, 2, 3, 4, 5, 6, 6]
i = 3, j = 4, k = 7
```

**R exhausted, copy remaining L:**
```
A = [1, 2, 2, 3, 4, 5, 6, 7]
```

**Done!**

---

### The MERGE-SORT Procedure

**Algorithm:**
```
MERGE-SORT(A, p, r)
1  if p ≥ r              // base case: 0 or 1 element
2    return
3  q = ⌊(p + r) / 2⌋     // midpoint
4  MERGE-SORT(A, p, q)   // sort left half
5  MERGE-SORT(A, q+1, r) // sort right half
6  MERGE(A, p, q, r)     // merge sorted halves
```

**Line-by-line:**

**Line 1-2:** Base case
- If p ≥ r, subarray has ≤ 1 element
- Already sorted, return immediately

**Line 3:** Divide
- Find midpoint q
- Divides A[p : r] into A[p : q] and A[q+1 : r]

**Line 4:** Conquer left
- Recursively sort A[p : q]

**Line 5:** Conquer right
- Recursively sort A[q+1 : r]

**Line 6:** Combine
- Merge the two sorted halves

---

### MERGE-SORT Example

**Input:** A = [5, 2, 4, 7, 1, 3, 2, 6]

**Recursion tree:**

```
                    [5,2,4,7,1,3,2,6]
                    /              \
            [5,2,4,7]              [1,3,2,6]
            /      \                /      \
        [5,2]    [4,7]          [1,3]    [2,6]
        /  \      /  \          /  \      /  \
      [5] [2]   [4] [7]       [1] [3]   [2] [6]
       |   |     |   |         |   |     |   |
      [5] [2]   [4] [7]       [1] [3]   [2] [6]  (base case)
        \  /      \  /          \  /      \  /
        [2,5]    [4,7]          [1,3]    [2,6]  (merge)
            \      /                \      /
            [2,4,5,7]              [1,2,3,6]    (merge)
                    \              /
                    [1,2,2,3,4,5,6,7]          (final merge)
```

**Key observations:**
- Recursion depth: lg n (binary splits)
- Each level does O(n) work (merging)
- Total: O(n lg n)

---

### Analyzing MERGE-SORT

**Recurrence relation:**
```
T(n) = 2T(n/2) + Θ(n)

Where:
- 2T(n/2): two recursive calls on half-size arrays
- Θ(n): time to merge
```

**Solving the recurrence:**

**Method 1: Recursion tree**

```
Level 0:           n                    = n
Level 1:        n/2  n/2                = n
Level 2:      n/4 n/4 n/4 n/4           = n
...
Level lg n:   1 1 1 ... 1 (n times)     = n

Total levels: lg n + 1
Work per level: n
Total work: n(lg n + 1) = Θ(n lg n)
```

**Method 2: Master theorem (preview)**
```
T(n) = aT(n/b) + f(n)

For merge sort: a=2, b=2, f(n)=Θ(n)
Result: T(n) = Θ(n lg n)
```

**Conclusion:** Merge sort runs in Θ(n lg n) time in all cases!

---

### Comparing Insertion Sort vs Merge Sort

| Aspect | Insertion Sort | Merge Sort |
|--------|----------------|------------|
| Best case | Θ(n) | Θ(n lg n) |
| Worst case | Θ(n²) | Θ(n lg n) |
| Average case | Θ(n²) | Θ(n lg n) |
| Space | O(1) | O(n) |
| Stable? | Yes | Yes |
| In-place? | Yes | No |
| Good for small n? | Yes | No |
| Good for large n? | No | Yes |

**When to use each:**
- **Insertion sort:** Small arrays, nearly sorted data
- **Merge sort:** Large arrays, guaranteed performance

**Crossover point:** Usually around n = 10-50

---

## 🎯 Problem-Solving Framework

### How to Approach Chapter 2 Problems

**Type 1: Trace Algorithm Execution**
**Pattern:** "Show the operation of [algorithm] on array..."

**Approach:**
1. Write down initial array
2. For each iteration:
   - Show current state
   - Show what gets compared
   - Show what gets moved
   - Show result after iteration
3. Show final sorted array

**Example:** Exercise 2.1-1

---

**Type 2: Modify Algorithm**
**Pattern:** "Rewrite [algorithm] to sort into [different order]..."

**Approach:**
1. Understand original algorithm
2. Identify what needs to change
3. Modify comparison operators or loop direction
4. Verify with example

**Example:** Exercise 2.1-2

---

**Type 3: Prove Correctness**
**Pattern:** "Using loop invariants, prove..."

**Approach:**
1. State loop invariant clearly
2. Prove initialization (base case)
3. Prove maintenance (inductive step)
4. Prove termination (conclusion)
5. Explain why this proves correctness

**Example:** Exercise 2.1-3

---

**Type 4: Analyze Running Time**
**Pattern:** "What is the running time of..."

**Approach:**
1. Count loop iterations
2. Determine cost per iteration
3. Sum up total cost
4. Express in Θ notation
5. Consider best/worst/average cases

**Example:** Exercise 2.2-1

---

**Type 5: Design New Algorithm**
**Pattern:** "Write pseudocode for..."

**Approach:**
1. Understand problem requirements
2. Choose appropriate technique (iterative, recursive, divide-and-conquer)
3. Write clear pseudocode
4. Analyze running time
5. Verify correctness

**Example:** Exercise 2.3-1

---

**Type 6: Solve Recurrence**
**Pattern:** "Solve the recurrence..."

**Approach:**
1. Identify pattern (recursion tree, substitution, master theorem)
2. Draw recursion tree if helpful
3. Sum work at each level
4. Express final answer in Θ notation

**Example:** Exercise 2.3-2

---

## 💡 Key Concepts Summary

### Loop Invariants
```
1. Initialization: True before first iteration
2. Maintenance: True before → True after
3. Termination: Invariant + exit condition = correctness
```

### Analyzing Algorithms
```
1. Count operations
2. Express as function of n
3. Focus on highest-order term
4. Use Θ notation
```

### Divide and Conquer
```
1. Divide: Break into subproblems
2. Conquer: Solve recursively
3. Combine: Merge solutions
```

### Recurrence Relations
```
T(n) = aT(n/b) + f(n)

Where:
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = work to divide and combine
```

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Identify problem type
- [ ] Recall relevant algorithm/technique
- [ ] Plan your approach

### While Solving
- [ ] Show all work clearly
- [ ] Use proper notation
- [ ] Verify with examples
- [ ] State conclusions explicitly

### Common Mistakes
- ❌ Forgetting base case in recursion
- ❌ Off-by-one errors in loops
- ❌ Not proving all three loop invariant properties
- ❌ Ignoring constants in analysis (keep until final Θ)
- ❌ Confusing best/worst/average case

---

**You're ready to master Chapter 2! 🎉**

---

**End of Guide**
