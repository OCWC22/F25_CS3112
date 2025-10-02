# Chapter 4.3 Quick Reference: Substitution Method

**One-page cheat sheet for midterm**

---

## 🎯 The Two-Step Process

### Step 1: GUESS the form
```
Convert O(f(n)) → T(n) ≤ cf(n)
Convert Ω(f(n)) → T(n) ≥ cf(n)
Use explicit constants!
```

### Step 2: PROVE by induction
```
1. Base case: Verify for small n
2. Hypothesis: Assume for k < n
3. Inductive step: Prove for n
```

---

## 🔑 Common Recurrence Patterns

| Recurrence | Guess | Result |
|------------|-------|--------|
| T(n) = T(n-1) + 1 | cn | Θ(n) |
| T(n) = T(n-1) + n | cn² | Θ(n²) |
| T(n) = T(n/2) + 1 | c lg n | Θ(lg n) |
| T(n) = T(n/2) + n | cn | Θ(n) |
| T(n) = 2T(n/2) + n | cn lg n | Θ(n lg n) |
| T(n) = 2T(n/3) + n | cn | Θ(n) |
| T(n) = 4T(n/2) + n | cn² | Θ(n²) |
| T(n) = 2T(n-1) + 1 | c·2ⁿ | Θ(2ⁿ) |

---

## 💡 The Lower-Order Term Trick

### When Simple Guess Fails

**Problem:** Get extra term
```
T(n) ≤ cn² + n  (want cn²)
```

**Solution:** Subtract lower-order term
```
Guess: T(n) ≤ cn² - dn
Proof: Gets cn² - 2dn + n ≤ cn² - dn ✓
```

### When to Use

**Subtract term when:**
- Recurrence adds term: +n, +1, etc.
- Simple guess gives extra positive term
- **Example:** T(n) = 4T(n/2) + n → cn² - dn

**Add term when:**
- Base case fails (lg 1 = 0)
- Need flexibility
- **Example:** cn lg n → cn lg n + b

---

## 📋 Exercise Quick Reference

### 4.3-1(a): T(n) = T(n-1) + n
```
Guess: T(n) ≤ cn²
Constraint: c ≥ 1
Proof: cn² - 2cn + c + n ≤ cn²
```

### 4.3-1(b): T(n) = T(n/2) + Θ(1)
```
Guess: T(n) ≤ c lg n + b
Constraint: c ≥ d
Handles base case with +b
```

### 4.3-1(c): T(n) = 2T(n/2) + n
```
Upper: T(n) ≤ cn lg n, c ≥ 1
Lower: T(n) ≥ cn lg n, c ≤ 1
Both work with c = 1
```

### 4.3-1(d): T(n) = 2T(n/2+17) + n
```
+17 doesn't affect asymptotic behavior
Same as merge sort: O(n lg n)
```

### 4.3-1(e): T(n) = 2T(n/3) + Θ(n)
```
Upper: T(n) ≤ cn, c ≥ 3d
Lower: T(n) ≥ cn, c ≤ 3d
Linear despite 2 subproblems!
```

### 4.3-1(f): T(n) = 4T(n/2) + Θ(n)
```
Simple cn² fails
Modified cn² - dn works (d ≥ 1)
```

### 4.3-2: Show Failure and Fix
```
T(n) = 4T(n/2) + n
Simple: cn² fails (gets cn² + n)
Fixed: cn² - dn works
```

### 4.3-3: Exponential with Constant
```
T(n) = 2T(n-1) + 1
Simple: c·2ⁿ fails (gets c·2ⁿ + 1)
Fixed: c·2ⁿ - d works (d ≥ 1)
```

---

## 🧮 Essential Techniques

### Logarithm Simplification
```
lg(n/2) = lg n - lg 2 = lg n - 1
lg(n/b) = lg n - lg b
```

### Algebraic Expansion
```
(n-1)² = n² - 2n + 1
(n/2)² = n²/4
```

### Inequality Manipulation
```
For O: Need ≤
For Ω: Need ≥
Solve for c to satisfy constraint
```

---

## ⚠️ Pitfalls to Avoid

### DON'T: Use O in Hypothesis
```
✗ T(n) = O(n lg n)
✗ T(n) ≤ 2·O(n/2)
```

### DO: Use Explicit Constants
```
✓ T(n) ≤ cn lg n
✓ T(k) ≤ ck lg k for k < n
```

### DON'T: Prove Wrong Thing
```
✗ Show T(n) ≤ cn + Θ(1), conclude O(n)
```

### DO: Prove Exact Form
```
✓ Show T(n) ≤ cn exactly
```

### DON'T: Forget Base Case
```
✗ Only prove inductive step
```

### DO: Verify Base Case
```
✓ Check T(1) or T(2) satisfies bound
```

---

## 🎯 Decision Tree: What to Guess

```
Recurrence Form:

T(n) = T(n-1) + f(n)
├─ f(n) = Θ(1)  → Guess Θ(n)
├─ f(n) = Θ(n)  → Guess Θ(n²)
└─ f(n) = Θ(n^k) → Guess Θ(n^(k+1))

T(n) = T(n/2) + f(n)
├─ f(n) = Θ(1)  → Guess Θ(lg n)
└─ f(n) = Θ(n^k) → Guess Θ(n^k)

T(n) = 2T(n/2) + f(n)
├─ f(n) = Θ(1)  → Guess Θ(n)
├─ f(n) = Θ(n)  → Guess Θ(n lg n)
└─ f(n) = Θ(n²) → Guess Θ(n²)

T(n) = aT(n/b) + f(n)
└─ Use Master Theorem intuition

T(n) = 2T(n-1) + f(n)
└─ Guess Θ(2ⁿ)
```

---

## 💪 Quick Self-Test

### Can you answer these?

1. **T(n) = T(n-1) + n → ?**
   - O(n²)

2. **T(n) = 2T(n/2) + n → ?**
   - Θ(n lg n)

3. **When to subtract lower-order term?**
   - When simple guess gives extra term

4. **Why not use O in hypothesis?**
   - Constants can change, invalid proof

5. **T(n) = 4T(n/2) + n needs what guess?**
   - cn² - dn (not just cn²)

---

## 🚀 Exam Checklist

### Before Starting
- [ ] Identify recurrence pattern
- [ ] Make educated guess
- [ ] Decide O, Ω, or Θ

### During Proof
- [ ] Use explicit constants
- [ ] State hypothesis clearly
- [ ] Show all algebra
- [ ] Verify inequality direction
- [ ] Check base case

### If Stuck
- [ ] Try subtracting lower-order term
- [ ] Try adding constant
- [ ] Check constant constraints
- [ ] Verify you're proving exact form

---

## 📖 Key Formulas

### Summations
```
Σ(i=1 to n) i = n(n+1)/2
Σ(i=1 to n) i² = n(n+1)(2n+1)/6
```

### Logarithms
```
lg(n/2) = lg n - 1
lg(ab) = lg a + lg b
lg(a/b) = lg a - lg b
```

### Geometric Series
```
Σ(i=0 to k) r^i = (r^(k+1) - 1)/(r - 1)
```

---

## 🎓 Last-Minute Tips

### 5 Minutes Before Exam

1. **Two steps:** Guess + Prove
2. **Use explicit constants:** cn, not O(n)
3. **Lower-order trick:** Subtract when fails
4. **Base case:** Always verify
5. **Θ = O + Ω:** Prove both bounds

### Confidence Boosters
- You know the patterns ✓
- You can modify guesses ✓
- You understand induction ✓
- **You got this!** 💪

---

**Good luck! 🎉**

---

**End of Cheat Sheet**
