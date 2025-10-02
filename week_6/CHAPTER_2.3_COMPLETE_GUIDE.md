# Chapter 2.3 Complete Guide: Designing Algorithms (Merge Sort)

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 2.3 - Designing Algorithms  
**Purpose:** Master divide-and-conquer and merge sort

---

## 🎯 What Chapter 2.3 Is Really About

### The Big Picture

Chapter 2.3 teaches you **divide-and-conquer** - a powerful design paradigm that beats simple iterative algorithms.

**Mental model:** Divide-and-conquer is like **organizing a large project**:
- Break into smaller tasks (divide)
- Complete each task (conquer)
- Combine results (combine)

**Why it's important:**
- **Better algorithms:** Θ(n lg n) beats Θ(n²)
- **Design paradigm:** Applies to many problems
- **Recursion:** Foundation for advanced algorithms
- **Analysis:** Introduces recurrences

**Key insight:** Breaking problems into smaller pieces can make them easier AND faster!

---

## 📚 The Divide-and-Conquer Method

### Three Steps

**1. DIVIDE**
- Break problem into smaller subproblems
- Subproblems are smaller instances of same problem

**2. CONQUER**
- Solve subproblems recursively
- If small enough, solve directly (base case)

**3. COMBINE**
- Merge subproblem solutions
- Create solution to original problem

---

### Example: Merge Sort

**DIVIDE:**
- Split array into two halves
- Find midpoint q = ⌊(p+r)/2⌋
- Create subarrays A[p:q] and A[q+1:r]

**CONQUER:**
- Recursively sort A[p:q]
- Recursively sort A[q+1:r]

**COMBINE:**
- Merge two sorted subarrays
- Result: sorted array A[p:r]

**BASE CASE:**
- If p ≥ r (0 or 1 element)
- Already sorted, return immediately

---

## 🎓 Merge Sort Algorithm

### The Main Procedure

```
MERGE-SORT(A, p, r)
1  if p ≥ r              // base case: 0 or 1 element
2      return
3  q = ⌊(p + r)/2⌋      // find midpoint
4  MERGE-SORT(A, p, q)   // sort left half
5  MERGE-SORT(A, q+1, r) // sort right half
6  MERGE(A, p, q, r)     // merge sorted halves
```

**Initial call:** MERGE-SORT(A, 1, n)

**Key features:**
- Recursive structure
- Divides in half each time
- Combines with merge operation
- In-place sorting (modifies A)

---

### The Merge Procedure

```
MERGE(A, p, q, r)
1   nL = q - p + 1                    // length of A[p:q]
2   nR = r - q                        // length of A[q+1:r]
3   let L[0:nL-1] and R[0:nR-1] be new arrays
4   for i = 0 to nL - 1               // copy left half
5       L[i] = A[p + i]
6   for j = 0 to nR - 1               // copy right half
7       R[j] = A[q + j + 1]
8   i = 0                             // index for L
9   j = 0                             // index for R
10  k = p                             // index for A
11  while i < nL and j < nR           // merge while both have elements
12      if L[i] ≤ R[j]
13          A[k] = L[i]
14          i = i + 1
15      else
16          A[k] = R[j]
17          j = j + 1
18      k = k + 1
19  while i < nL                      // copy remaining L
20      A[k] = L[i]
21      i = i + 1
22      k = k + 1
23  while j < nR                      // copy remaining R
24      A[k] = R[j]
25      j = j + 1
26      k = k + 1
```

**How it works:**
1. Copy subarrays to temporary arrays L and R
2. Compare smallest remaining elements from L and R
3. Copy smaller element back to A
4. Repeat until one array exhausted
5. Copy remaining elements from other array

---

### Complete Example

**Input:** [3, 41, 52, 26, 38, 57, 9, 49]

**Divide phase (top-down):**
```
[3, 41, 52, 26, 38, 57, 9, 49]
         ↓ split
[3, 41, 52, 26]    [38, 57, 9, 49]
    ↓ split            ↓ split
[3, 41]  [52, 26]  [38, 57]  [9, 49]
  ↓ split  ↓ split   ↓ split   ↓ split
[3] [41] [52] [26] [38] [57] [9] [49]  ← Base case (1 element each)
```

**Conquer phase (bottom-up merging):**
```
[3] [41] [52] [26] [38] [57] [9] [49]
  ↓ merge  ↓ merge   ↓ merge  ↓ merge
[3, 41]  [26, 52]  [38, 57]  [9, 49]
    ↓ merge            ↓ merge
[3, 26, 41, 52]    [9, 38, 49, 57]
         ↓ merge
[3, 9, 26, 38, 41, 49, 52, 57]  ← Final sorted array
```

---

### Detailed Merge Example

**Merge [3, 41] and [26, 52]:**

```
L = [3, 41]    R = [26, 52]    A = [_, _, _, _]
     ↑              ↑                 ↑
     i=0            j=0               k=0

Compare L[0]=3 vs R[0]=26: 3 < 26
Copy 3 to A[0]

L = [3, 41]    R = [26, 52]    A = [3, _, _, _]
        ↑           ↑                    ↑
        i=1         j=0                  k=1

Compare L[1]=41 vs R[0]=26: 26 < 41
Copy 26 to A[1]

L = [3, 41]    R = [26, 52]    A = [3, 26, _, _]
        ↑              ↑                     ↑
        i=1            j=1                   k=2

Compare L[1]=41 vs R[1]=52: 41 < 52
Copy 41 to A[2]

L = [3, 41]    R = [26, 52]    A = [3, 26, 41, _]
                   ↑                            ↑
        i=2 (done) j=1                          k=3

L exhausted, copy remaining R
Copy 52 to A[3]

Result: A = [3, 26, 41, 52] ✓
```

---

## 📊 Running Time Analysis

### Merge Procedure

**Operations:**
- Copy to L and R: Θ(n) where n = r - p + 1
- Merge back to A: Θ(n)
- Total: Θ(n)

**Key insight:** Merging n elements takes linear time!

---

### Merge Sort Recurrence

**Recurrence:**
```
T(n) = 2T(n/2) + Θ(n)
```

**Where:**
- 2T(n/2): Sort two halves (conquer)
- Θ(n): Divide + combine

**Base case:** T(1) = Θ(1)

---

### Solving the Recurrence

**Method 1: Recursion Tree**

```
Level 0:              cn                    Cost: cn
                     /  \
Level 1:          cn/2  cn/2                Cost: cn
                  / \   / \
Level 2:       cn/4 ... cn/4                Cost: cn
               ...
Level lg n:    c c c ... c (n nodes)        Cost: cn

Height: lg n + 1 levels
Cost per level: cn (constant!)
Total: cn × (lg n + 1) = cn lg n + cn = Θ(n lg n)
```

**Key insight:** Every level costs cn, and there are lg n levels!

---

**Method 2: Master Theorem (Chapter 4)**

```
T(n) = 2T(n/2) + Θ(n)

a = 2, b = 2, f(n) = n
n^(log_b a) = n^(log₂ 2) = n

f(n) = n = Θ(n) (Case 2, k=0)

Solution: T(n) = Θ(n lg n)
```

---

**Method 3: Substitution (Chapter 4)**

**Guess:** T(n) = cn lg n

**Prove by induction:**
```
T(n) = 2T(n/2) + cn
     ≤ 2·c(n/2)lg(n/2) + cn
     = cn lg(n/2) + cn
     = cn(lg n - 1) + cn
     = cn lg n - cn + cn
     = cn lg n ✓
```

---

### Final Result

**All cases:** T(n) = Θ(n lg n)

**Why all cases same?**
- Always divides in half
- Always merges all elements
- No early exit possible

**Comparison with insertion sort:**
```
Insertion sort: Θ(n²) worst case
Merge sort:     Θ(n lg n) all cases

For large n: n lg n << n²
Example (n=1000): 1000 lg 1000 ≈ 10,000
                  1000² = 1,000,000
Merge sort 100× faster!
```

---

## 🔑 Key Concepts

### Divide-and-Conquer Advantages

**1. Better asymptotic performance**
- Often achieves Θ(n lg n) or better
- Beats simple Θ(n²) algorithms

**2. Natural recursion**
- Elegant, concise code
- Easy to understand structure

**3. Parallelizable**
- Subproblems independent
- Can solve simultaneously

**4. Analyzable**
- Recurrences are systematic
- Standard solution methods

---

### Merge Sort Advantages

**1. Guaranteed performance**
- Always Θ(n lg n)
- No worst-case degradation

**2. Stable sort**
- Preserves relative order of equal elements
- Important for some applications

**3. Predictable**
- No input-dependent behavior
- Reliable for real-time systems

---

### Merge Sort Disadvantages

**1. Extra space**
- Needs Θ(n) auxiliary storage
- Not in-place like insertion sort

**2. Overhead for small n**
- Recursion overhead
- Constant factors larger

**3. Not adaptive**
- Doesn't benefit from partial sorting
- Always does full work

---

## 💡 Recursion Tree Intuition

### Visualizing Merge Sort

**Tree structure:**
```
                    [8 elements]
                   /            \
            [4 elements]      [4 elements]
            /        \        /        \
        [2 elem]  [2 elem] [2 elem]  [2 elem]
        /    \    /    \   /    \    /    \
       [1]  [1] [1]  [1] [1]  [1] [1]  [1]
```

**Levels:**
- Level 0: 1 problem of size n
- Level 1: 2 problems of size n/2
- Level 2: 4 problems of size n/4
- Level i: 2^i problems of size n/2^i
- Level lg n: n problems of size 1

**Cost per level:**
- Each level processes all n elements
- Cost: cn per level
- Total levels: lg n + 1
- Total cost: cn(lg n + 1) = Θ(n lg n)

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Trace Merge Sort

**Given:** Array to sort
**Task:** Show divide and merge steps

**Steps:**
1. Draw divide tree (top-down)
2. Show base cases (1-element arrays)
3. Show merge operations (bottom-up)
4. Verify final result

---

### Framework 2: Prove Merge Correctness

**Given:** MERGE procedure
**Task:** Prove it correctly merges sorted subarrays

**Steps:**
1. State loop invariant
2. Prove initialization
3. Prove maintenance
4. Prove termination
5. Handle remaining elements

---

### Framework 3: Analyze Recurrence

**Given:** Recursive algorithm
**Task:** Find running time

**Steps:**
1. Write recurrence relation
2. Identify base case
3. Solve using recursion tree or Master Theorem
4. Express in Θ-notation

---

### Framework 4: Design Divide-and-Conquer

**Given:** Problem description
**Task:** Design D&C algorithm

**Steps:**
1. Identify how to divide
2. Determine base case
3. Design combine step
4. Write pseudocode
5. Analyze running time

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Base Case
```
✗ if p == r (only 1 element)
✓ if p ≥ r (0 or 1 element)
```

### Mistake 2: Wrong Midpoint
```
✗ q = (p + r)/2 (might not be integer)
✓ q = ⌊(p + r)/2⌋ (floor function)
```

### Mistake 3: Wrong Merge Bounds
```
✗ MERGE(A, p, q, r) with q not between p and r
✓ p ≤ q < r required
```

### Mistake 4: Forgetting Remaining Elements
```
✗ Only one while loop in MERGE
✓ Three while loops (main + two cleanup)
```

### Mistake 5: Wrong Recurrence
```
✗ T(n) = T(n/2) + Θ(n) (only one subproblem)
✓ T(n) = 2T(n/2) + Θ(n) (two subproblems)
```

---

## 🚀 Exam Strategy

### For Tracing
- [ ] Draw divide tree
- [ ] Show all splits
- [ ] Show all merges
- [ ] Verify final result

### For Correctness Proofs
- [ ] State loop invariant
- [ ] Prove all three properties
- [ ] Handle all cases
- [ ] Connect to correctness

### For Analysis
- [ ] Write recurrence
- [ ] Identify parameters
- [ ] Solve using appropriate method
- [ ] Express in Θ-notation

### For Design
- [ ] Identify divide strategy
- [ ] Design combine step
- [ ] Write pseudocode
- [ ] Analyze running time

### Time Management
- Trace: 10-15 min
- Correctness: 15-20 min
- Analysis: 10-15 min
- Design: 20-30 min

---

**You're ready to master merge sort! 🎉**

---

**End of Guide**
