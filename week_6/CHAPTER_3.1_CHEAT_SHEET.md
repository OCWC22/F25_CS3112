# Chapter 3.1 Quick Reference: Characterizing Running Times

**One-page cheat sheet for midterm**

---

## 🎯 The Three Notations (Intuitive)

| Notation | Intuition | Example: 7n³ + 100n² - 20n + 6 |
|----------|-----------|--------------------------------|
| **O(n³)** | "No faster than n³" | Also O(n⁴), O(n⁵), ... |
| **Ω(n³)** | "At least as fast as n³" | Also Ω(n²), Ω(n), ... |
| **Θ(n³)** | "Precisely at rate n³" | Only Θ(n³) |

---

## 🔑 Key Relationships

```
f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))

O: upper bound (≤)
Ω: lower bound (≥)
Θ: tight bound (=)
```

---

## 📊 Insertion Sort Analysis

### Algorithm Structure
```
Outer loop: n-1 iterations (always)
Inner loop: 0 to i-1 iterations (depends on input)
```

### Upper Bound (O)
```
Max inner loop iterations: (n-1)n/2 < n²
Therefore: O(n²) ✓
```

### Lower Bound (Ω)
```
Bad input: n/3 large values in first n/3 positions
Operations: (n/3) × (n/3) = n²/9
Therefore: Ω(n²) ✓
```

### Tight Bound
```
Worst case: Θ(n²)  [O and Ω together]
Best case: Θ(n)    [already sorted]
```

---

## 📐 Selection Sort Analysis

### Algorithm Structure
```
Outer loop: n-1 iterations
Inner loop: n-i iterations (ALWAYS runs fully)
```

### All Cases
```
Comparisons: n(n-1)/2 for ANY input
Therefore: Θ(n²) in ALL cases ✓
```

### Key Difference
```
Insertion sort: Θ(n) to Θ(n²) depending on input
Selection sort: Always Θ(n²)
```

---

## 🛠️ Problem-Solving Toolkit

### Proving O (Upper Bound)
1. Count worst-case loop iterations
2. Show total ≤ c·f(n)
3. Conclude O(f(n))

### Proving Ω (Lower Bound)
1. Find a bad input
2. Count operations for that input
3. Show total ≥ c·f(n)
4. Conclude Ω(f(n))

### Proving Θ (Tight Bound)
1. Prove O(f(n))
2. Prove Ω(f(n))
3. Conclude Θ(f(n))

---

## 💡 Problem 3.1-1: Non-Multiple of 3

### Issue
Original used n/3, but what if n not divisible by 3?

### Solution
Use floor function: ⌊n/3⌋

### Counting
```
Operations: ⌊n/3⌋²
Bound: ⌊n/3⌋ ≥ n/4 for large n
Therefore: ⌊n/3⌋² ≥ n²/16 = Ω(n²) ✓
```

### Key Insight
Constant factor changes (1/9 → 1/16), but still Ω(n²)!

---

## 💡 Problem 3.1-2: Selection Sort

### Loop Analysis
```
Inner loop iterations:
i=1: n-1
i=2: n-2
...
i=n-1: 1

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2
```

### Key Observation
Inner loop ALWAYS runs fully (no early exit)

### Result
```
T(n) = Θ(n²) in ALL cases
```

---

## 💡 Problem 3.1-3: Parameterized Lower Bound

### Setup
```
First αn: large values
Middle (1-2α)n: pass through
Last αn: final positions
```

### Operations
```
f(α) = α(1-2α)n²
```

### Constraint
```
0 < α < 1/2  [middle section must exist]
```

### Optimization
```
f'(α) = 1 - 4α = 0
α = 1/4  [optimal]

Maximum: f(1/4) = 1/8
Operations: n²/8
```

### Key Insight
1/4, 1/2, 1/4 split is WORSE than 1/3, 1/3, 1/3!

---

## 📋 Quick Comparison

| Algorithm | Best | Worst | Average |
|-----------|------|-------|---------|
| Insertion Sort | Θ(n) | Θ(n²) | Θ(n²) |
| Selection Sort | Θ(n²) | Θ(n²) | Θ(n²) |

---

## 🎯 Common Patterns

### Nested Loops
```
for i = 1 to n
  for j = 1 to i
    [constant work]

Total: 1 + 2 + ... + n = n(n+1)/2 = Θ(n²)
```

### Always-Full Inner Loop
```
for i = 1 to n
  for j = i+1 to n
    [constant work]

Total: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = Θ(n²)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Confusing O with Θ
```
✗ "Algorithm is O(n²)" when you mean Θ(n²)
✓ O is upper bound, Θ is tight bound
```

### Mistake 2: Wrong Floor Handling
```
✗ Treating ⌊n/3⌋ as exactly n/3
✓ Use ⌊n/3⌋ ≥ n/4 for large n
```

### Mistake 3: Forgetting All Cases
```
✗ Analyzing only worst case for selection sort
✓ Selection sort is Θ(n²) in ALL cases
```

### Mistake 4: Wrong Optimization
```
✗ Forgetting constraint 0 < α < 1/2
✓ Check α = 1/4 satisfies constraint
```

---

## 🧮 Essential Formulas

### Sum of First n Integers
```
1 + 2 + ... + n = n(n+1)/2 ≈ n²/2
```

### Floor Function
```
⌊x⌋ ≥ x - 1
⌊n/3⌋ ≥ n/4  (for large n)
```

### Optimization
```
Maximize f(α) = α(1-2α):
f'(α) = 1 - 4α = 0
α = 1/4
```

---

## 🚀 Exam Strategy

### For Upper Bound (O)
- [ ] Count worst-case loop iterations
- [ ] Use summation formulas
- [ ] Show ≤ c·f(n)

### For Lower Bound (Ω)
- [ ] Construct bad input
- [ ] Count operations for that input
- [ ] Show ≥ c·f(n)

### For Tight Bound (Θ)
- [ ] Prove both O and Ω
- [ ] Conclude Θ

### For Optimization
- [ ] Express as function f(α)
- [ ] Take derivative
- [ ] Set f'(α) = 0
- [ ] Verify with f''(α)
- [ ] Check constraints

---

## 💪 Quick Self-Test

### Can you answer these in 30 seconds?

1. **Is 5n² = O(n³)?**
   - Yes! Grows no faster than n³

2. **Is 5n² = Θ(n³)?**
   - No! Grows slower than n³

3. **Why is insertion sort Ω(n²)?**
   - Bad input forces n²/9 operations

4. **Why is selection sort always Θ(n²)?**
   - Inner loop always runs fully

5. **What α maximizes α(1-2α)?**
   - α = 1/4

---

## 📖 Key Concepts

### Asymptotic Analysis
```
Focus on: highest-order term
Ignore: lower-order terms, constants
Goal: characterize growth rate
```

### Upper vs Lower Bounds
```
Upper (O): worst-case behavior
Lower (Ω): best-case for worst input
Tight (Θ): both bounds match
```

### Algorithm Comparison
```
Insertion sort: adaptive (fast on sorted)
Selection sort: non-adaptive (always slow)
```

---

## 🎓 Last-Minute Review

### 5 Minutes Before Exam

1. **Three notations:** O (≤), Ω (≥), Θ (=)
2. **Insertion sort:** Θ(n) best, Θ(n²) worst
3. **Selection sort:** Θ(n²) always
4. **Lower bound:** Find bad input, count operations
5. **Optimization:** f'(α) = 0, check constraints

---

## ✅ Checklist

- [ ] Understand O, Ω, Θ intuitively
- [ ] Can analyze nested loops
- [ ] Can construct bad inputs
- [ ] Can use floor function correctly
- [ ] Can optimize with calculus
- [ ] Know insertion vs selection sort

---

**You're ready for Chapter 3.1! 🎉**

---

**End of Cheat Sheet**
