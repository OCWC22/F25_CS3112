# Chapter 2.3 Quick Reference: Merge Sort & Divide-and-Conquer

**One-page cheat sheet for midterm**

---

## 🎯 Divide-and-Conquer Method

### Three Steps
```
1. DIVIDE:   Break into smaller subproblems
2. CONQUER:  Solve subproblems recursively
3. COMBINE:  Merge solutions
```

### Base Case
```
If problem small enough, solve directly
```

---

## 🔑 Merge Sort

### Main Algorithm
```
MERGE-SORT(A, p, r)
1  if p ≥ r
2      return
3  q = ⌊(p + r)/2⌋
4  MERGE-SORT(A, p, q)
5  MERGE-SORT(A, q+1, r)
6  MERGE(A, p, q, r)
```

### Merge Procedure
```
MERGE(A, p, q, r)
1. Copy A[p:q] to L, A[q+1:r] to R
2. Compare L[i] vs R[j]
3. Copy smaller to A[k]
4. Repeat until one exhausted
5. Copy remaining elements
```

---

## 📊 Running Time

### Merge Sort
```
Recurrence: T(n) = 2T(n/2) + Θ(n)
Solution: T(n) = Θ(n lg n)

Best case:  Θ(n lg n)
Worst case: Θ(n lg n)
Average:    Θ(n lg n)

All cases same!
```

### Comparison
```
Insertion Sort: Θ(n²) worst case
Merge Sort:     Θ(n lg n) all cases

For large n: n lg n << n²
Merge sort much faster!
```

---

## 🧮 Key Formulas

### Recursion Tree
```
Height: lg n + 1 levels
Nodes at level i: 2^i
Cost per level: cn (constant!)
Total: cn × lg n = Θ(n lg n)
```

### Recurrence Solution
```
T(n) = 2T(n/2) + n
     = n lg n + n
     = Θ(n lg n)
```

---

## 💡 Binary Search

### Algorithm
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

### Running Time
```
Recurrence: T(n) = T(n/2) + Θ(1)
Solution: T(n) = Θ(lg n)

Much faster than linear search!
```

---

## 📋 Exercise Quick Reference

### 2.3-1: Trace Merge Sort
```
Input: [3, 41, 52, 26, 38, 57, 9, 49]
Divide to: [3][41][52][26][38][57][9][49]
Merge up to: [3, 9, 26, 38, 41, 49, 52, 57]
```

### 2.3-2: Base Case
```
"if p ≥ r" vs "if p ≠ r"
p > r never occurs with correct calls
p ≠ r sufficient
```

### 2.3-3: MERGE Invariant
```
A[p:k-1] has k-p smallest, sorted
L[i], R[j] are next candidates
Cleanup loops handle remainder
```

### 2.3-4: Solve Recurrence
```
T(n) = 2T(n/2) + n
Prove: T(n) = n lg n (by induction)
Result: Θ(n lg n)
```

### 2.3-5: Recursive Insertion
```
T(n) = T(n-1) + Θ(n)
Solution: Θ(n²)
Same as iterative
```

### 2.3-6: Binary Search
```
Eliminate half each time
T(n) = T(n/2) + Θ(1)
Result: Θ(lg n)
```

### 2.3-7: Binary in Insertion
```
Comparisons: Θ(n lg n) ✓
Shifts: Θ(n²) ✗
Total: Θ(n²) (no improvement)
```

### 2.3-8: Two-Sum
```
Sort: Θ(n lg n)
Two-pointer: Θ(n)
Total: Θ(n lg n) ✓
```

---

## 🎯 Algorithm Comparison

| Algorithm | Best | Worst | Average | Space |
|-----------|------|-------|---------|-------|
| **Insertion** | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) |
| **Selection** | Θ(n²) | Θ(n²) | Θ(n²) | Θ(1) |
| **Merge** | Θ(n lg n) | Θ(n lg n) | Θ(n lg n) | Θ(n) |

---

## ⚠️ Common Pitfalls

### Merge Sort
- ❌ Wrong base case (p == r only)
- ❌ Wrong midpoint calculation
- ❌ Forgetting cleanup loops in MERGE
- ❌ Wrong recurrence (T(n) = T(n/2) + n)

### Binary Search
- ❌ Not handling "not found" case
- ❌ Infinite loop (wrong bounds update)
- ❌ Off-by-one errors

### Analysis
- ❌ Thinking binary search fixes insertion sort
- ❌ Forgetting shifting cost
- ❌ Wrong recurrence solution

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **Merge sort recurrence?**
   - T(n) = 2T(n/2) + Θ(n)

2. **Merge sort time?**
   - Θ(n lg n) all cases

3. **Binary search time?**
   - Θ(lg n)

4. **Binary search in insertion sort?**
   - Still Θ(n²) (shifts dominate)

5. **Two-sum time?**
   - Θ(n lg n) (sort + scan)

---

## 🚀 Exam Checklist

### For Merge Sort
- [ ] Understand divide-conquer-combine
- [ ] Know both procedures
- [ ] Can trace execution
- [ ] Know running time

### For Binary Search
- [ ] Understand halving strategy
- [ ] Can write pseudocode
- [ ] Know Θ(lg n) time
- [ ] Understand why it's fast

### For Analysis
- [ ] Write recurrences correctly
- [ ] Solve using appropriate method
- [ ] Express in Θ-notation
- [ ] Compare algorithms

---

**You got this! 🎉**

---

**End of Cheat Sheet**
