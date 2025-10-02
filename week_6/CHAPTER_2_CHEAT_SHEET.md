# Chapter 2 Quick Reference: Getting Started

**One-page cheat sheet for midterm**

---

## 🎯 The Three Core Skills

| Section | Skill | Key Concept |
|---------|-------|-------------|
| **2.1** | Understanding | Loop invariants prove correctness |
| **2.2** | Analyzing | Count operations, use Θ-notation |
| **2.3** | Designing | Divide-and-conquer for better algorithms |

---

## 📚 Insertion Sort (Section 2.1)

### Algorithm
```
for i = 2 to n
  key = A[i]
  j = i - 1
  while j > 0 and A[j] > key
    A[j+1] = A[j]
    j = j - 1
  A[j+1] = key
```

### Loop Invariant
> A[1 : i-1] contains original elements in sorted order

### Proof Structure
1. **Initialization:** True before first iteration
2. **Maintenance:** True before → True after
3. **Termination:** Invariant + exit = correctness

### Running Time
- **Best case:** Θ(n) - already sorted
- **Worst case:** Θ(n²) - reverse sorted
- **Average case:** Θ(n²)

---

## 📊 Analyzing Algorithms (Section 2.2)

### RAM Model
- Instructions execute sequentially
- Each operation takes constant time
- Focus on algorithm, not hardware

### Analysis Steps
1. Count loop iterations
2. Determine cost per iteration
3. Sum total cost
4. Express in Θ-notation

### Selection Sort
```
for i = 1 to n-1
  min_index = i
  for j = i+1 to n
    if A[j] < A[min_index]
      min_index = j
  swap A[i] with A[min_index]
```

**All cases:** Θ(n²) - always scans fully

---

## 🔧 Merge Sort (Section 2.3)

### Divide-and-Conquer
1. **Divide:** Split into subproblems
2. **Conquer:** Solve recursively
3. **Combine:** Merge solutions

### Algorithm
```
MERGE-SORT(A, p, r)
  if p ≥ r
    return
  q = ⌊(p+r)/2⌋
  MERGE-SORT(A, p, q)
  MERGE-SORT(A, q+1, r)
  MERGE(A, p, q, r)
```

### MERGE Procedure
```
Copy A[p:q] to L
Copy A[q+1:r] to R
i = 0, j = 0, k = p
while i < nL and j < nR
  if L[i] ≤ R[j]
    A[k] = L[i++]
  else
    A[k] = R[j++]
  k++
Copy remaining elements
```

### Recurrence
```
T(n) = 2T(n/2) + Θ(n)
Solution: T(n) = Θ(n lg n)
```

### Running Time
**All cases:** Θ(n lg n)

---

## 🎯 Algorithm Comparison

| Algorithm | Best | Worst | Average | Space | Stable? |
|-----------|------|-------|---------|-------|---------|
| Insertion | Θ(n) | Θ(n²) | Θ(n²) | O(1) | Yes |
| Selection | Θ(n²) | Θ(n²) | Θ(n²) | O(1) | No |
| Merge | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | O(n) | Yes |

---

## 💡 Problem Types

### Type 1: Trace Execution
**Keywords:** "illustrate", "show operation"  
**Approach:** Execute step-by-step, show each iteration

### Type 2: Modify Algorithm
**Keywords:** "rewrite", "modify"  
**Approach:** Change comparison or loop direction

### Type 3: Prove Correctness
**Keywords:** "prove", "loop invariant"  
**Approach:** Init + Maintenance + Termination

### Type 4: Analyze Time
**Keywords:** "running time", "Θ-notation"  
**Approach:** Count operations, sum, express in Θ

### Type 5: Design Algorithm
**Keywords:** "write pseudocode", "design"  
**Approach:** Choose technique, code, analyze

### Type 6: Solve Recurrence
**Keywords:** "solve recurrence"  
**Approach:** Expansion or substitution

---

## 🧮 Essential Formulas

### Summations
```
Σᵢ₌₁ⁿ i = n(n+1)/2 ≈ n²/2
Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6 ≈ n³/3
```

### Logarithms
```
lg n = log₂ n
lg(n!) = Θ(n lg n)
lg(2ⁿ) = n
```

### Recurrence Patterns
```
T(n) = T(n-1) + c → Θ(n)
T(n) = T(n-1) + cn → Θ(n²)
T(n) = 2T(n/2) + cn → Θ(n lg n)
```

---

## ⚠️ Common Mistakes

### Loop Invariants
- ❌ Forgetting termination property
- ❌ Not stating invariant clearly
- ❌ Skipping initialization proof

### Analysis
- ❌ Counting only worst case for all algorithms
- ❌ Forgetting constants until final answer
- ❌ Confusing best/worst/average cases

### Recursion
- ❌ Missing base case
- ❌ Wrong recurrence relation
- ❌ Off-by-one errors

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Identify problem type
- [ ] Recall relevant algorithm
- [ ] Plan approach

### While Solving
- [ ] Show all work
- [ ] Use proper notation
- [ ] Verify with examples
- [ ] State conclusions

### Time Management
- Trace: 5-10 min
- Modify: 5-10 min
- Prove: 10-15 min
- Analyze: 10-15 min
- Design: 15-20 min

---

## 💪 Quick Self-Test

### Can you answer these?

1. **What's the loop invariant for insertion sort?**
   - A[1:i-1] sorted, contains original elements

2. **Why is selection sort always Θ(n²)?**
   - Always scans entire unsorted portion

3. **What's merge sort's recurrence?**
   - T(n) = 2T(n/2) + Θ(n)

4. **Best case for insertion sort?**
   - Θ(n) - already sorted

5. **Why n-1 iterations for selection sort?**
   - Last element automatically in place

---

## 📋 Pseudocode Conventions

### Loops
```
for i = 1 to n        // n iterations
for i = 1 to n-1      // n-1 iterations
while condition       // variable iterations
```

### Arrays
```
A[i]        // element at position i
A[i : j]    // subarray from i to j (inclusive)
A[1 : n]    // entire array (1-indexed)
```

### Comments
```
// This is a comment
```

### Objects
```
x.attribute    // access attribute
x.f.g         // cascade: (x.f).g
```

---

## 🎓 Key Concepts

### Correctness
- Loop invariants prove algorithms work
- Three properties: init, maint, term
- Like mathematical induction

### Efficiency
- Focus on order of growth
- Drop constants and lower-order terms
- Use Θ, O, Ω notation

### Design
- Divide-and-conquer often better
- Recursion tree shows work per level
- Merge sort: Θ(n lg n) beats Θ(n²)

---

## 🏆 Last-Minute Review

### 5 Minutes Before Exam

1. **Loop invariant:** Init + Maint + Term
2. **Insertion sort:** Θ(n) to Θ(n²)
3. **Selection sort:** Always Θ(n²)
4. **Merge sort:** Always Θ(n lg n)
5. **Recurrence:** T(n) = 2T(n/2) + n → Θ(n lg n)

### Confidence Boosters
- You understand loop invariants ✓
- You can analyze algorithms ✓
- You know divide-and-conquer ✓
- You can trace algorithms ✓
- **You got this!** 💪

---

**Good luck! 🎉**

---

**End of Cheat Sheet**
