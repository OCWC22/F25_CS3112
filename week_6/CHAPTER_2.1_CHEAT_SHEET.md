# Chapter 2.1 Quick Reference: Insertion Sort

**One-page cheat sheet for midterm**

---

## 🎯 The Algorithm

### Insertion Sort Pseudocode
```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      j = i - 1
4      while j > 0 and A[j] > key
5          A[j+1] = A[j]
6          j = j - 1
7      A[j+1] = key
```

### How It Works
```
1. Start at position 2 (position 1 already "sorted")
2. Save current element as key
3. Compare key with sorted elements (right to left)
4. Shift larger elements one position right
5. Insert key in correct position
6. Repeat for all elements
```

---

## 🔑 Loop Invariant

### The Invariant
> At the start of each iteration, A[1 : i-1] contains the elements originally in A[1 : i-1], but in sorted order.

### Three Properties

**1. Initialization:**
- i = 2, so A[1 : 1] = just A[1]
- Single element is sorted ✓

**2. Maintenance:**
- Before: A[1 : i-1] sorted
- Insert A[i] into correct position
- After: A[1 : i] sorted ✓

**3. Termination:**
- Loop ends at i = n + 1
- A[1 : n] is sorted ✓
- Algorithm correct!

---

## 📊 Running Time

| Case | When | Time |
|------|------|------|
| **Best** | Already sorted | Θ(n) |
| **Worst** | Reverse sorted | Θ(n²) |
| **Average** | Random order | Θ(n²) |

### Why?
```
Best: No shifts needed (while loop never executes)
Worst: Maximum shifts (1+2+3+...+(n-1) = n(n-1)/2)
Average: About half the shifts of worst case
```

---

## 💡 Key Concepts

### Why Start at i=2?
```
A[1] is already "sorted" (single element)
Start inserting from second element
```

### Why j > 0?
```
Prevents accessing A[0] (out of bounds)
Stops when reach beginning of array
```

### Why A[j+1] = key?
```
j is last position checked
j+1 is where key belongs
```

### Why Save key?
```
Shifting overwrites A[i]
Must save value before shifting
```

---

## 🔧 Common Modifications

### Sort Decreasing
```
Change: A[j] > key → A[j] < key
Effect: Shifts smaller elements right
Result: Largest to smallest
```

### Search Instead of Sort
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

---

## 📋 Exercise Quick Reference

### 2.1-1: Trace on [31, 41, 59, 26, 41, 58]
```
i=2: [31, 41, 59, 26, 41, 58]
i=3: [31, 41, 59, 26, 41, 58]
i=4: [26, 31, 41, 59, 41, 58]
i=5: [26, 31, 41, 41, 59, 58]
i=6: [26, 31, 41, 41, 58, 59]
```

### 2.1-2: SUM-ARRAY Invariant
```
Invariant: sum = A[1] + ... + A[i-1]
Init: sum = 0 (empty)
Maint: Add A[i]
Term: sum = total
```

### 2.1-3: Decreasing Sort
```
Change line 5: A[j] < key
Result: Sorts largest to smallest
```

### 2.1-4: Linear Search
```
Scan array left to right
Return index if found
Return NIL if not found
```

### 2.1-5: Binary Addition
```
carry = 0
for i = 0 to n-1:
    sum = A[i] + B[i] + carry
    C[i] = sum mod 2
    carry = ⌊sum/2⌋
C[n] = carry
```

---

## ⚠️ Common Pitfalls

### Algorithm Execution
- ❌ Starting loop at i=1
- ❌ Forgetting to save key
- ❌ Wrong insertion position
- ❌ Off-by-one in while condition

### Loop Invariants
- ❌ Only saying "sorted" (incomplete)
- ❌ Forgetting "original elements"
- ❌ Not proving all three properties
- ❌ Wrong termination value

### Modifications
- ❌ Changing wrong comparison
- ❌ Not testing modification
- ❌ Breaking loop invariant

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **Why start at i=2?**
   - A[1] already sorted

2. **What's the loop invariant?**
   - A[1:i-1] contains original elements, sorted

3. **Best case time?**
   - Θ(n)

4. **Worst case time?**
   - Θ(n²)

5. **How to sort decreasing?**
   - Change A[j] > key to A[j] < key

---

## 🎓 Pseudocode Conventions

### Arrays
```
A[i]      - element at position i
A[i : j]  - subarray from i to j (inclusive)
A[1 : n]  - entire array (1-indexed)
```

### Loops
```
for i = 1 to n     - n iterations
while condition    - until condition false
```

### Comments
```
// This is a comment
```

### Return
```
return value       - exit and return
return NIL         - return special "not found"
```

---

## 🚀 Exam Checklist

### Before Solving
- [ ] Read problem carefully
- [ ] Identify problem type
- [ ] Recall relevant concepts

### While Solving
- [ ] Show all work
- [ ] Use proper notation
- [ ] Verify with examples
- [ ] State conclusions

### For Loop Invariants
- [ ] State precisely
- [ ] Prove initialization
- [ ] Prove maintenance
- [ ] Prove termination
- [ ] Connect to correctness

---

**You got this! 🎉**

---

**End of Cheat Sheet**
