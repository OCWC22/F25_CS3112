# Chapter 4.5 Quick Reference: Master Method

**One-page cheat sheet for midterm**

---

## 🎯 The Master Theorem

### Given: T(n) = aT(n/b) + f(n)

**Step 1:** Calculate **n^(log_b a)** (the watershed)

**Step 2:** Compare **f(n)** with **n^(log_b a)**

**Step 3:** Apply the matching case

---

## 🔑 The Three Cases

### Case 1: Leaves Dominate
```
Condition: f(n) = O(n^(log_b a - ε)) for some ε > 0
           (f(n) polynomially smaller)

Solution: T(n) = Θ(n^(log_b a))
```

**Example:** T(n) = 8T(n/2) + n²
- n^(log₂ 8) = n³
- n² < n³ (polynomially)
- **Answer: Θ(n³)**

---

### Case 2: All Levels Equal
```
Condition: f(n) = Θ(n^(log_b a) × (lg n)^k) for k ≥ 0
           (f(n) same rate, up to log factors)

Solution: T(n) = Θ(n^(log_b a) × (lg n)^(k+1))
```

**Most common:** k = 0
```
f(n) = Θ(n^(log_b a))
Solution: T(n) = Θ(n^(log_b a) × lg n)
```

**Example:** T(n) = 2T(n/2) + n
- n^(log₂ 2) = n
- n = n (equal, k=0)
- **Answer: Θ(n lg n)**

---

### Case 3: Root Dominates
```
Condition: 1. f(n) = Ω(n^(log_b a + ε)) for some ε > 0
              (f(n) polynomially larger)
           2. af(n/b) ≤ cf(n) for some c < 1
              (regularity condition)

Solution: T(n) = Θ(f(n))
```

**Example:** T(n) = 2T(n/2) + n²
- n^(log₂ 2) = n
- n² > n (polynomially)
- Regularity: 2(n/2)² = n²/2 ≤ (3/4)n² ✓
- **Answer: Θ(n²)**

---

## 📊 Quick Comparison Table

| f(n) vs n^(log_b a) | Separation | Case | Solution |
|---------------------|------------|------|----------|
| f(n) << n^(log_b a) | Polynomial | 1 | Θ(n^(log_b a)) |
| f(n) ≈ n^(log_b a) | Logarithmic | 2 | Θ(n^(log_b a) lg^(k+1) n) |
| f(n) >> n^(log_b a) | Polynomial + Reg | 3 | Θ(f(n)) |

---

## 🧮 Common Watersheds

| a | b | log_b a | n^(log_b a) |
|---|---|---------|-------------|
| 1 | 2 | 0 | 1 |
| 2 | 2 | 1 | n |
| 4 | 2 | 2 | n² |
| 8 | 2 | 3 | n³ |
| 7 | 2 | 2.807 | n^2.807 |
| 2 | 4 | 0.5 | √n |
| 3 | 4 | 0.793 | n^0.793 |

**Formula:** log_b a = (lg a) / (lg b)

---

## 📋 Famous Recurrences

### Merge Sort
```
T(n) = 2T(n/2) + n
n^(log₂ 2) = n
Case 2 (k=0)
Answer: Θ(n lg n)
```

### Binary Search
```
T(n) = T(n/2) + 1
n^(log₂ 1) = 1
Case 2 (k=0)
Answer: Θ(lg n)
```

### Strassen's Algorithm
```
T(n) = 7T(n/2) + n²
n^(log₂ 7) ≈ n^2.807
Case 1
Answer: Θ(n^2.807)
```

### Naive Matrix Multiplication
```
T(n) = 8T(n/2) + n²
n^(log₂ 8) = n³
Case 1
Answer: Θ(n³)
```

---

## 💡 Key Concepts

### Polynomially Smaller
```
f(n) = O(n^(log_b a - ε)) for ε > 0

Examples:
n² vs n³: YES (ε=1)
n vs n lg n: NO (only log difference)
```

### Polynomially Larger
```
f(n) = Ω(n^(log_b a + ε)) for ε > 0

Examples:
n³ vs n²: YES (ε=1)
n lg n vs n: NO (only log difference)
```

### Regularity Condition
```
af(n/b) ≤ cf(n) for c < 1

Check: Calculate af(n/b), compare with f(n)
Most polynomials satisfy this!
```

---

## 📝 Exercise Quick Reference

### 4.5-1: Same a, b, Different f(n)
```
All have a=2, b=4, so n^(log₄ 2) = √n

(a) f(n)=1:    1 << √n     → Case 1 → Θ(√n)
(b) f(n)=√n:   √n = √n     → Case 2 → Θ(√n lg n)
(c) f(n)=n:    n >> √n     → Case 3 → Θ(n)
(d) f(n)=n²:   n² >> √n    → Case 3 → Θ(n²)
```

### 4.5-2: Caesar's Algorithm
```
Beat Strassen: T(n) < Θ(n^2.807)
Recurrence: aT(n/4) + n²
Need: n^(log₄ a) < n^2.807
Answer: a ≤ 48
```

### 4.5-3: Binary Search
```
T(n) = T(n/2) + 1
n^(log₂ 1) = 1
Case 2 → Θ(lg n)
```

### 4.5-4: Logarithm Fails
```
f(n) = lg n
Regularity: Fails (ratio → 1)
Polynomial: Fails (lg n = o(n^ε))
```

### 4.5-5: Oscillating Function
```
f(n) = 2^(⌈lg n⌉)
Polynomial: OK
Regularity: Fails
```

---

## ⚠️ Common Pitfalls

### DON'T: Forget Regularity
```
✗ "f(n) > n^(log_b a), so Case 3"
✓ Must check af(n/b) ≤ cf(n) too!
```

### DON'T: Confuse Log and Polynomial
```
✗ "n lg n > n, so Case 3"
✓ Only log difference → Case 2!
```

### DON'T: Use Wrong Base
```
✗ Always use log₂
✓ Use log_b from recurrence
```

### DON'T: Apply to Wrong Form
```
✗ T(n) = T(n-1) + n
✓ Only for T(n) = aT(n/b) + f(n)
```

---

## 🎯 Decision Tree

```
Given: T(n) = aT(n/b) + f(n)

1. Calculate n^(log_b a)

2. Compare f(n) with n^(log_b a):

   ┌─ f(n) << n^(log_b a) (polynomial)?
   │  └─ Case 1 → Θ(n^(log_b a))
   │
   ├─ f(n) ≈ n^(log_b a) × (lg n)^k?
   │  └─ Case 2 → Θ(n^(log_b a) × (lg n)^(k+1))
   │
   └─ f(n) >> n^(log_b a) (polynomial)?
      ├─ Check regularity
      │  ├─ YES → Case 3 → Θ(f(n))
      │  └─ NO → Master Method fails
      └─ NO polynomial → Gap → Master Method fails
```

---

## 💪 Quick Self-Test

### Can you solve in 30 seconds?

1. **T(n) = 4T(n/2) + n → ?**
   - Θ(n²)

2. **T(n) = 2T(n/2) + n² → ?**
   - Θ(n²)

3. **T(n) = T(n/2) + 1 → ?**
   - Θ(lg n)

4. **When is regularity needed?**
   - Case 3 only

5. **n lg n vs n: which case?**
   - Case 2 (log difference)

---

## 🚀 Exam Checklist

### Before Applying
- [ ] Verify form: T(n) = aT(n/b) + f(n)
- [ ] Identify a, b, f(n)
- [ ] Calculate n^(log_b a)

### While Solving
- [ ] Compare f(n) with watershed
- [ ] Check polynomial separation
- [ ] If Case 3, verify regularity
- [ ] Apply correct formula

### After Solving
- [ ] State answer clearly
- [ ] Use Θ notation
- [ ] Double-check calculation

---

## 🎓 Key Takeaways

### The Power of Master Method
```
✓ Solves most D&C recurrences instantly
✓ No recursion trees needed
✓ No substitution proofs needed
✓ Just compare and apply!
```

### The Three Scenarios
```
Case 1: Leaves win → Θ(n^(log_b a))
Case 2: Tie → Θ(n^(log_b a) lg n)
Case 3: Root wins → Θ(f(n))
```

### Remember
```
✓ Polynomial separation required (Cases 1, 3)
✓ Regularity required (Case 3 only)
✓ Logarithmic factors → Case 2
✓ Some recurrences fall in gaps
```

---

**You got this! 🎉**

---

**End of Cheat Sheet**
