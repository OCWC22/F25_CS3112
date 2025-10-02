# Chapter 3.3 Midterm Cheat Sheet

**One-page reference for asymptotic notation and function growth**

---

## 🎯 The Big 5 Asymptotic Notations

| Notation | Meaning | Definition | Limit Test |
|----------|---------|------------|------------|
| **Θ(g(n))** | Tight bound | ∃c₁,c₂,n₀: c₁g(n) ≤ f(n) ≤ c₂g(n) | lim f/g = c > 0 |
| **O(g(n))** | Upper bound | ∃c,n₀: f(n) ≤ c·g(n) | lim f/g ≤ c |
| **Ω(g(n))** | Lower bound | ∃c,n₀: f(n) ≥ c·g(n) | lim f/g ≥ c > 0 |
| **o(g(n))** | Strict upper | ∀c>0, ∃n₀: f(n) < c·g(n) | lim f/g = 0 |
| **ω(g(n))** | Strict lower | ∀c>0, ∃n₀: f(n) > c·g(n) | lim f/g = ∞ |

**Key relationship:** f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))

---

## 📊 Growth Rate Hierarchy (Memorize This!)

```
Slowest → Fastest

1  <  lg lg n  <  lg* n  <  lg n  <  (lg n)²  <  √n  <  n  <  n lg n  
   <  n²  <  n³  <  2ⁿ  <  n!  <  nⁿ
```

**Special cases:**
- lg* n (iterated log): grows slower than lg lg n for large n
- (lg n)!: between n and 2ⁿ
- Fibonacci Fₙ: grows like φⁿ where φ ≈ 1.618

---

## 🧮 Essential Formulas

### Logarithms
```
lg(ab) = lg a + lg b
lg(a/b) = lg a - lg b
lg(aᵇ) = b lg a
lg(1/a) = -lg a
logₐ n = (lg n) / (lg a)  [change of base]
```

### Factorials
```
n! = √(2πn) · (n/e)ⁿ · (1 + Θ(1/n))  [Stirling's]
lg(n!) = Θ(n lg n)
n! = ω(2ⁿ)  [factorial > exponential]
n! = o(nⁿ)   [factorial < power tower]
```

### Golden Ratio
```
φ = (1 + √5) / 2 ≈ 1.618
φ̂ = (1 - √5) / 2 ≈ -0.618
φ² = φ + 1  [KEY PROPERTY]
φ̂² = φ̂ + 1
Fₙ = (φⁿ - φ̂ⁿ) / √5  [Binet's formula]
```

### Floor/Ceiling
```
⌊x⌋ = largest integer ≤ x
⌈x⌉ = smallest integer ≥ x
⌊x⌋ + ⌈-x⌉ = 0
⌊αn⌋ + ⌈(1-α)n⌉ = n  [for 0 ≤ α ≤ 1]
```

---

## 🔍 Problem Recognition Guide

### Type 1: Monotonicity
**Keywords:** "monotonically increasing", "nonnegative"  
**Approach:** Write definition, use n₁ ≤ n₂, show f(n₁) ≤ f(n₂)  
**Watch out:** Products need nonnegativity!

### Type 2: Floor/Ceiling
**Keywords:** ⌊⌋, ⌈⌉, "integer"  
**Approach:** Use properties, analyze fractional parts  
**Verify:** Plug in concrete values

### Type 3: Asymptotic with Polynomials
**Keywords:** "o(n)", "Θ(nᵏ)", "polynomially bounded"  
**Approach:** Factor out dominant term, show lower-order terms negligible  
**Key:** (n + o(n))ᵏ = Θ(nᵏ)

### Type 4: Prove Equations
**Keywords:** "prove equation (3.X)", "show that"  
**Approach:** Use definitions, Stirling's, log properties  
**Common:** lg(n!) = Θ(n lg n), n! = ω(2ⁿ)

### Type 5: Polynomial Bounding
**Keywords:** "polynomially bounded", "O(nᵏ) for some k"  
**Approach:** Estimate growth, compare to nᵏ  
**Key:** ⌊lg n⌋! is NOT, ⌊lg lg n⌋! is YES

### Type 6: Comparing Functions
**Keywords:** "which is larger", "asymptotically"  
**Approach:** Compute lim f(n)/g(n), use concrete values  
**Key:** lg*(lg n) > lg(lg* n)

### Type 7: Golden Ratio/Fibonacci
**Keywords:** "golden ratio", "Fibonacci", "φ"  
**Approach:** Use φ² = φ + 1, strong induction  
**Key:** Binet's formula connects closed form to recurrence

### Type 8: Logarithmic Implications
**Keywords:** "implies", "solve for", logarithms  
**Approach:** Manipulate equation, iterate to consistency  
**Key:** k lg k = Θ(n) ⟹ k = Θ(n/lg n)

---

## 🛠️ Proof Techniques

### Direct Proof
1. Start with definitions
2. Use algebra/inequalities
3. Show what's required
4. State conclusion

### Induction
1. **Base case:** Verify for n = 0, 1 (or 2)
2. **Hypothesis:** Assume true for k (or k and k+1 for strong)
3. **Inductive step:** Prove for k+1 (or k+2)
4. **Conclude:** By induction, true for all n

### Limit Comparison
1. Compute lim(n→∞) f(n)/g(n)
2. If 0: f = o(g)
3. If c > 0: f = Θ(g)
4. If ∞: f = ω(g)

### Contradiction
1. Assume opposite
2. Derive contradiction
3. Conclude original statement true

---

## ⚡ Quick Facts

### Asymptotic Arithmetic
```
Θ(f) + Θ(g) = Θ(f + g)
Θ(f) · Θ(g) = Θ(f · g)
Θ(cf) = Θ(f)  [constant c]
o(f) + o(g) = o(f + g)
```

### Common Limits
```
lim n/2ⁿ = 0
lim lg n / n = 0
lim nᵏ / 2ⁿ = 0  [any k]
lim (lg n)ᵏ / n = 0  [any k]
```

### Useful Inequalities
```
2ⁿ ≤ n! ≤ nⁿ
lg n! ≤ n lg n
n! ≥ (n/2)^(n/2)
(1 + 1/n)ⁿ → e
```

### Iterated Logarithm
```
lg* n = min{i ≥ 0 : lg⁽ⁱ⁾ n ≤ 1}
lg* 2 = 1
lg* 4 = 2
lg* 16 = 3
lg* 65536 = 5
lg*(lg n) ≈ lg* n - 1
```

---

## 🎓 Exam Strategy

### Before You Start
- [ ] Read all problems first
- [ ] Identify problem types
- [ ] Start with easiest
- [ ] Budget time (5-20 min per problem)

### While Solving
- [ ] Write down definitions
- [ ] Show all work
- [ ] Justify each step
- [ ] Check with concrete values

### Common Mistakes
- ❌ Confusing O with Θ
- ❌ Forgetting base cases in induction
- ❌ Ignoring nonnegativity for products
- ❌ Mixing up lg (log₂) and ln (logₑ)
- ❌ Assuming without proof

### Time Savers
- ✅ Memorize growth hierarchy
- ✅ Know Big 5 definitions cold
- ✅ Practice limit comparisons
- ✅ Use Stirling's for factorials
- ✅ Verify with n = 10, 100, 1000

---

## 🧠 Mental Models

### Asymptotic Notation = Inequality Sets
- Θ: sandwiched between two multiples
- O: bounded above
- Ω: bounded below
- o: strictly smaller
- ω: strictly larger

### Growth Rates = Scalability
- O(1): constant - best case
- O(lg n): logarithmic - very fast (binary search)
- O(n): linear - acceptable
- O(n lg n): linearithmic - good (merge sort)
- O(n²): quadratic - slow for large n
- O(2ⁿ): exponential - infeasible for n > 30
- O(n!): factorial - infeasible for n > 20

### Logarithms = Divide-by-2 Count
- lg n = how many times to divide n by 2 to reach 1
- lg* n = how many times to apply lg to reach ≤ 1
- lg(n!) = sum of logs = Θ(n lg n)

### Factorials = Product of Decreasing Terms
- n! = n · (n-1) · ... · 1
- Grows faster than 2ⁿ (eventually)
- Grows slower than nⁿ (always)
- Stirling's gives precise approximation

---

## 📝 Formula Sheet

### Must Memorize
```
Θ definition: c₁g(n) ≤ f(n) ≤ c₂g(n)
O definition: f(n) ≤ c·g(n)
Ω definition: f(n) ≥ c·g(n)

Growth: 1 < lg n < n < n lg n < n² < 2ⁿ < n! < nⁿ

Logs: lg(ab) = lg a + lg b, lg(aᵇ) = b lg a

Factorial: lg(n!) = Θ(n lg n)

Golden ratio: φ² = φ + 1, Fₙ = (φⁿ - φ̂ⁿ)/√5
```

### Good to Know
```
Stirling's: n! ≈ √(2πn) · (n/e)ⁿ

Binomial: (x+y)ⁿ = Σ(n choose k)xᵏyⁿ⁻ᵏ

Floor/Ceiling: ⌊αn⌋ + ⌈(1-α)n⌉ = n

Limits: lim nᵏ/2ⁿ = 0, lim lg n/n = 0
```

---

## 🚀 Last-Minute Review

### 5 Minutes Before Exam
1. **Growth hierarchy:** 1 < lg n < n < n² < 2ⁿ < n!
2. **Big 5:** Θ (tight), O (upper), Ω (lower), o (strict upper), ω (strict lower)
3. **Key formulas:** lg(n!) = Θ(n lg n), φ² = φ + 1
4. **Proof techniques:** Induction (base + hypothesis + step), limits (f/g)
5. **Common mistakes:** O ≠ Θ, need nonnegativity for products

### Confidence Boosters
- You've solved 3.3-7 and 3.3-8 ✓
- You understand induction ✓
- You can manipulate logs ✓
- You know the growth hierarchy ✓
- **You got this!** 💪

---

## 🎯 Problem-Solving Checklist

For any problem:
1. [ ] Identify problem type
2. [ ] Write down relevant definitions
3. [ ] Choose proof technique
4. [ ] Show all work with justification
5. [ ] Verify with concrete example
6. [ ] State conclusion clearly

**Remember:** Partial credit is real! Show your work even if you're not 100% sure.

---

**Good luck on your midterm! 🎉**

---

**End of Cheat Sheet**
