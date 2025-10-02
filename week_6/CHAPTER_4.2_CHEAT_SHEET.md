# Chapter 4.2 Quick Reference: Strassen's Algorithm

**One-page cheat sheet for midterm**

---

## 🎯 The Big Idea

**Trade expensive operations for cheap ones:**
- Reduce multiplications (expensive: Θ(n³))
- Increase additions (cheap: Θ(n²))
- Result: Faster asymptotic time!

---

## 🔑 Strassen's Seven Products (MEMORIZE!)

```
P₁ = A₁₁(B₁₂ - B₂₂)
P₂ = (A₁₁ + A₁₂)B₂₂
P₃ = (A₂₁ + A₂₂)B₁₁
P₄ = A₂₂(B₂₁ - B₁₁)
P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)
```

---

## 🧮 Combining Products (MEMORIZE!)

```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

**Memory aid:**
- C₁₂ and C₂₁: Simple (2 terms each)
- C₁₁ and C₂₂: Complex (4 terms each)

---

## 📊 Complexity Comparison

| Algorithm | Recurrence | Solution | Exponent |
|-----------|------------|----------|----------|
| Naive | - | Θ(n³) | 3.000 |
| Standard D&C | 8T(n/2) + Θ(n²) | Θ(n³) | 3.000 |
| **Strassen** | **7T(n/2) + Θ(n²)** | **Θ(n^2.807)** | **2.807** |

**Key:** 7 subproblems instead of 8 makes all the difference!

---

## 💡 Why It Works

### The Math
```
Standard: 8 subproblems
log₂ 8 = 3 → Θ(n³)

Strassen: 7 subproblems
log₂ 7 ≈ 2.807 → Θ(n^2.807)
```

### The Trade-off
```
Standard: 8 multiplications, 4 additions
Strassen: 7 multiplications, 18 additions

Savings: 1 multiplication
Cost: 14 extra additions
Worth it: n³ >> n²
```

---

## 🎯 Exercise Quick Reference

### 4.2-1: Manual Computation
```
Given: [1 3] × [6 8]
       [7 5]   [4 2]

Compute P₁...P₇, then C₁₁...C₂₂
Result: [18 14]
        [62 66]
```

### 4.2-2: Pseudocode
```
Base case: n=1, scalar multiply
Partition: 4 submatrices each
Compute: 7 recursive products
Combine: Use formulas
```

### 4.2-3: k×k Base Case
```
For 3×3 base with k multiplications:
T(n) = kT(n/3) + Θ(n²)

For o(n^(lg 7)): need k ≤ 21
With k=21: T(n) = Θ(n^2.771)
```

### 4.2-4: Pan's Algorithms
```
68×68 with 132,464 mults: Θ(n^2.795)
70×70 with 143,640 mults: Θ(n^2.795)
72×72 with 155,424 mults: Θ(n^2.795)

All equal! Slightly better than Strassen.
```

### 4.2-5: Complex Numbers
```
Standard: 4 real multiplications
Trick: P₃ = (a+b)(c+d)
       ad+bc = P₃ - ac - bd
Result: 3 real multiplications
```

### 4.2-6: Squaring to Multiply
```
Create M = [0 A]
           [B 0]
Square: M² = [AB  0 ]
             [0   BA]
Extract AB from top-right
Time: Θ(n^α)
```

---

## 🧮 Master Theorem Quick Apply

### For T(n) = 7T(n/2) + Θ(n²)

**Step 1:** Calculate n^(log_b a)
```
log₂ 7 ≈ 2.807
n^2.807
```

**Step 2:** Compare f(n) with n^2.807
```
f(n) = n²
n² < n^2.807 → Case 1
```

**Step 3:** Result
```
T(n) = Θ(n^2.807)
```

---

## ⚠️ Common Mistakes

### During Computation
- ❌ Using 8 products instead of 7
- ❌ Wrong combination formulas
- ❌ Arithmetic errors with negatives
- ❌ Not verifying answer

### During Analysis
- ❌ Forgetting addition costs (Θ(n²))
- ❌ Thinking copying changes asymptotic time
- ❌ Confusing log₂ 7 with log₂ 8
- ❌ Assuming AB = BA (not true!)

---

## 💪 Quick Self-Test

### Can you answer these in 30 seconds?

1. **How many products in Strassen?**
   - 7 (not 8!)

2. **What's the recurrence?**
   - T(n) = 7T(n/2) + Θ(n²)

3. **What's the solution?**
   - T(n) = Θ(n^2.807)

4. **What's C₁₂?**
   - C₁₂ = P₁ + P₂

5. **Why is it faster?**
   - 7 subproblems → smaller exponent

---

## 📐 Essential Formulas

### Logarithms
```
log₂ 7 ≈ 2.807
log₂ 8 = 3.000
log₃ 21 ≈ 2.771
```

### Exponent Comparison
```
n^2.771 < n^2.795 < n^2.807 < n^3.000
```

### Speedup
```
n³ / n^2.807 = n^0.193
For n=1000: ~2.5× faster
```

---

## 🎓 Key Takeaways

### The Insight
```
Fewer subproblems → smaller exponent
8 → 7: Changes 3.000 → 2.807
```

### The Trade-off
```
-1 multiplication (save n³)
+14 additions (cost 14n²)
Net: Huge win for large n
```

### The Reality
```
Theory: Θ(n^2.807) beats Θ(n³)
Practice: Only for n > 100-1000
Hybrid: Strassen at top, naive at bottom
```

---

## 🚀 Exam Strategy

### For Manual Computation
- [ ] Write down all 7 product formulas
- [ ] Calculate carefully (watch negatives!)
- [ ] Use combination formulas exactly
- [ ] Verify with standard method

### For Pseudocode
- [ ] Include base case
- [ ] Show all 7 recursive calls
- [ ] Include combination step
- [ ] Comment clearly

### For Analysis
- [ ] Write recurrence
- [ ] Apply Master Theorem
- [ ] Calculate log_b a
- [ ] Compare exponents

---

**You got this! 🎉**

---

**End of Cheat Sheet**
