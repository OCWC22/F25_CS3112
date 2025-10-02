# Chapter 4.1 Quick Reference: Matrix Multiplication

**One-page cheat sheet for midterm**

---

## 🎯 Core Concepts

### Matrix Multiplication
```
C = A × B (both n×n)
c_ij = Σ(k=1 to n) a_ik · b_kj

Naive algorithm: Θ(n³)
```

### Divide-and-Conquer Strategy
```
1. Divide: Partition into 4 submatrices (n/2 × n/2)
2. Conquer: 8 recursive multiplications
3. Combine: Add results (in place)
```

---

## 📊 The Key Equations

### Matrix Partitioning
```
[A₁₁  A₁₂]   [B₁₁  B₁₂]   [C₁₁  C₁₂]
[A₂₁  A₂₂] × [B₂₁  B₂₂] = [C₂₁  C₂₂]
```

### Submatrix Formulas
```
C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂
C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁
C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂

Total: 8 multiplications, 4 additions
```

---

## 🔑 Recurrence Relations

### Standard Recurrence
```
T(n) = 8T(n/2) + Θ(n²)

Where:
- 8T(n/2): 8 recursive calls
- Θ(n²): partition + combine
```

### Solution
```
T(n) = Θ(n³)

Using Master Theorem:
- a = 8, b = 2, f(n) = n²
- n^(log₂ 8) = n³
- f(n) < n³ → Case 1
- T(n) = Θ(n³)
```

---

## 💡 Two Implementation Approaches

| Aspect | Index Calculation | Copying |
|--------|-------------------|---------|
| **Partition cost** | Θ(1) | Θ(n²) |
| **Space** | O(1) extra | O(n²) extra |
| **Recurrence** | 8T(n/2) + Θ(n²) | 8T(n/2) + Θ(n²) |
| **Solution** | Θ(n³) | Θ(n³) |
| **Practical** | Faster | Slower |

**Key insight:** Same asymptotic time, different constants!

---

## 📝 Exercise Quick Reference

### 4.1-1: Non-Powers of 2
```
Fix: Use ⌈n/2⌉ and ⌊n/2⌋
Recurrence: T(n) = 8T(⌈n/2⌉) + Θ(n²)
Solution: T(n) = Θ(n³)
```

### 4.1-2: Non-Square Matrices
```
(kn×n) × (n×kn) → kn×kn result → Θ(k²n³)
(n×kn) × (kn×n) → n×n result   → Θ(kn³)

Second is k times faster!
```

### 4.1-3: Copying Analysis
```
Copying adds Θ(n²) per level
But still T(n) = Θ(n³)
More space, same asymptotic time
```

### 4.1-4: Matrix Addition
```
Index:   T(n) = 4T(n/2) + Θ(1)   → Θ(n²)
Copying: T(n) = 4T(n/2) + Θ(n²) → Θ(n² lg n)
Iterative: Θ(n²) (best!)
```

---

## 🧮 Master Theorem Quick Apply

### For T(n) = aT(n/b) + f(n)

**Step 1:** Calculate n^(log_b a)
```
For our case: n^(log₂ 8) = n³
```

**Step 2:** Compare f(n) with n^(log_b a)
```
f(n) = n²
n^(log_b a) = n³
n² < n³ → Case 1
```

**Step 3:** Apply Case 1
```
If f(n) = O(n^(log_b a - ε)) for ε > 0
Then T(n) = Θ(n^(log_b a))

Result: T(n) = Θ(n³)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Number of Subproblems
```
✗ "4 submatrices → 4 recursive calls"
✓ Each output needs 2 products → 8 calls
```

### Mistake 2: Forgetting Addition Cost
```
✗ T(n) = 8T(n/2) + Θ(1)
✓ T(n) = 8T(n/2) + Θ(n²)
```

### Mistake 3: Thinking Copying Changes Θ
```
✗ "Copying makes it Θ(n⁴)"
✓ Still Θ(n³), just larger constants
```

### Mistake 4: Confusing with Merge Sort
```
✗ "Divide-and-conquer → Θ(n lg n)"
✓ Depends on # of subproblems!
   2 subproblems → Θ(n lg n)
   8 subproblems → Θ(n³)
```

---

## 🎯 Why No Improvement?

### The Problem
```
8 subproblems → exponential growth
Leaves dominate → Θ(n³)
```

### Recursion Tree
```
Level 0: 1 problem,  cost n²
Level 1: 8 problems, cost 2n²
Level 2: 64 problems, cost 4n²
...
Total: Θ(n³)
```

### What Would Help?
```
Reduce subproblems!
Strassen: 7 subproblems → Θ(n^2.807)
```

---

## 🚀 Problem-Solving Strategy

### For Recurrence Problems
1. Count recursive calls (usually 8)
2. Determine non-recursive work (usually Θ(n²))
3. Write T(n) = 8T(n/2) + Θ(n²)
4. Apply Master Theorem
5. Get Θ(n³)

### For Implementation Problems
1. Identify what changes (index vs copy)
2. Calculate new costs
3. Write new recurrence
4. Solve and compare

### For Design Problems
1. Follow divide-and-conquer template
2. Partition into submatrices
3. Recursive calls on subproblems
4. Combine results
5. Analyze recurrence

---

## 📋 Key Formulas

### Geometric Series
```
Σ(i=0 to k) rⁱ = (r^(k+1) - 1)/(r - 1)
```

### Ceiling/Floor
```
⌈n/2⌉ ≤ n/2 + 1
⌊n/2⌋ ≥ n/2 - 1
```

### Logarithms
```
log₂ 8 = 3
2^(lg n) = n
```

---

## 💪 Quick Self-Test

### Can you answer these?

1. **How many recursive calls?**
   - 8 (not 4!)

2. **What's the recurrence?**
   - T(n) = 8T(n/2) + Θ(n²)

3. **What's the solution?**
   - T(n) = Θ(n³)

4. **Why no improvement over naive?**
   - 8 subproblems → exponential growth

5. **Does copying change asymptotic time?**
   - No, still Θ(n³)

---

## 🎓 Exam Tips

### Before Solving
- [ ] Identify problem type
- [ ] Remember 8 subproblems
- [ ] Know Master Theorem

### While Solving
- [ ] Count subproblems carefully
- [ ] Include all costs
- [ ] Apply Master Theorem correctly
- [ ] Verify with small example

### Time Management
- Recurrence: 5-10 min
- Implementation: 10-15 min
- Design: 15-20 min

---

**You're ready for Chapter 4.1! 🎉**

---

**End of Cheat Sheet**
