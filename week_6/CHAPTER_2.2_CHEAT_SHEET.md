# Chapter 2.2 Quick Reference: Analyzing Algorithms

**One-page cheat sheet for midterm**

---

## 🎯 The RAM Model

### Key Assumptions
```
✓ Sequential execution (one instruction at a time)
✓ Constant-time operations (arithmetic, data access)
✓ Constant-time array indexing
✓ Simple instructions only
```

### What It Includes
```
Arithmetic: +, -, ×, ÷, mod, floor, ceiling
Data: load, store, copy
Control: if-else, loops, function calls
```

---

## 🔑 Analysis Process

### Five Steps

**1. Count operations**
```
How many times does each line execute?
```

**2. Express as function**
```
T(n) = (cost × times for each line)
```

**3. Identify dominant term**
```
What grows fastest?
```

**4. Drop constants and lower-order terms**
```
an² + bn + c → n²
```

**5. Express in Θ-notation**
```
T(n) = Θ(n²)
```

---

## 📊 Case Analysis

### Three Cases

**Best Case:**
- Minimum running time
- Best possible input
- Example: Already sorted for insertion sort

**Worst Case:**
- Maximum running time
- Worst possible input
- Example: Reverse sorted for insertion sort

**Average Case:**
- Expected running time
- Random input (all equally likely)
- Often similar to worst case

---

## 🧮 Essential Formulas

### Summations
```
Σᵢ₌₁ⁿ i = n(n+1)/2 ≈ n²/2

Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6 ≈ n³/3

Σᵢ₌₁ⁿ c = cn (constant sum)
```

### Simplification
```
an² + bn + c = Θ(n²)
an + b = Θ(n)
a = Θ(1)
```

---

## 📋 Selection Sort

### Algorithm
```
SELECTION-SORT(A, n)
1  for i = 1 to n - 1
2      min_index = i
3      for j = i + 1 to n
4          if A[j] < A[min_index]
5              min_index = j
6      swap A[i] with A[min_index]
```

### Loop Invariant
> A[1 : i-1] contains the i-1 smallest elements in sorted order

### Running Time
```
Best case:  Θ(n²)
Worst case: Θ(n²)
Average:    Θ(n²)

All cases same! (always scans fully)
```

### Why n-1 Iterations?
```
After n-1 iterations, n-1 smallest in place
Last element must be largest
No need to select it
```

---

## 🎯 Algorithm Comparison

| Algorithm | Best | Worst | Average | When to Use |
|-----------|------|-------|---------|-------------|
| **Insertion** | Θ(n) | Θ(n²) | Θ(n²) | Nearly sorted data |
| **Selection** | Θ(n²) | Θ(n²) | Θ(n²) | Minimize swaps |

---

## 💡 Linear Search

### Running Time
```
Best case:  Θ(1)  - found at position 1
Worst case: Θ(n)  - not found or at end
Average:    Θ(n)  - check (n+1)/2 elements
```

### Average Case Calculation
```
Expected comparisons = (1/n)(1 + 2 + ... + n)
                     = (1/n) × n(n+1)/2
                     = (n+1)/2
                     = Θ(n)
```

---

## 📝 Exercise Quick Reference

### 2.2-1: Express in Θ-Notation
```
n³/1000 + 100n² - 100n + 3
Dominant: n³/1000
Answer: Θ(n³)
```

### 2.2-2: Selection Sort
```
Pseudocode: Find min, swap, repeat
Invariant: A[1:i-1] has i-1 smallest
Why n-1: Last element auto-correct
Time: Always Θ(n²)
```

### 2.2-3: Linear Search
```
Average: (n+1)/2 checks → Θ(n)
Worst: n checks → Θ(n)
Both linear
```

### 2.2-4: Improve Best Case
```
Check if sorted first (Θ(n))
If yes, return immediately
Best case becomes Θ(n)
```

---

## ⚠️ Common Pitfalls

### Analysis
- ❌ Keeping constants in Θ-notation
- ❌ Including lower-order terms
- ❌ Wrong summation formulas
- ❌ Miscounting loop iterations

### Selection Sort
- ❌ Thinking best case is better
- ❌ Running loop n times (should be n-1)
- ❌ Wrong loop invariant

### Linear Search
- ❌ Confusing average with worst
- ❌ Wrong probability calculation
- ❌ Forgetting "not found" case

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **What is RAM model?**
   - Sequential, constant-time operations

2. **Simplify 5n² + 3n + 7?**
   - Θ(n²)

3. **Selection sort best case?**
   - Θ(n²) (same as worst!)

4. **Linear search average?**
   - Θ(n) (check n/2 elements)

5. **Why focus on worst case?**
   - Upper bound guarantee

---

## 🚀 Exam Checklist

### For Analysis
- [ ] Count loop iterations
- [ ] Handle nested loops
- [ ] Sum correctly
- [ ] Simplify to Θ-notation

### For Design
- [ ] Write pseudocode
- [ ] State loop invariant
- [ ] Analyze all cases
- [ ] Compare with alternatives

### For Comparison
- [ ] Analyze each algorithm
- [ ] Express in Θ-notation
- [ ] Consider all cases
- [ ] Choose based on requirements

---

**You got this! 🎉**

---

**End of Cheat Sheet**
