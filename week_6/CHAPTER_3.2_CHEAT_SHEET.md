# Chapter 3.2 Quick Reference: Asymptotic Notation

**One-page cheat sheet for midterm**

---

## 🎯 The Big 5: Definitions & Intuition

| Notation | Definition | Limit Test | Intuition | Like |
|----------|------------|------------|-----------|------|
| **Θ(g(n))** | c₁g ≤ f ≤ c₂g | lim f/g = c > 0 | Same rate | = |
| **O(g(n))** | f ≤ cg | lim f/g ≤ c | No faster | ≤ |
| **Ω(g(n))** | cg ≤ f | lim f/g ≥ c > 0 | No slower | ≥ |
| **o(g(n))** | f < cg (∀c) | lim f/g = 0 | Strictly slower | < |
| **ω(g(n))** | cg < f (∀c) | lim f/g = ∞ | Strictly faster | > |

---

## 🔑 Key Relationships

```
f = Θ(g) ⟺ f = O(g) AND f = Ω(g)
f = o(g) ⟺ g = ω(f)
f = O(g) ⟺ g = Ω(f)
o(g) ∩ ω(g) = ∅
O(g) ∩ Ω(g) = Θ(g)
```

---

## 📊 Properties (Theorem 3.1)

### Transitivity
```
f = Θ(g), g = Θ(h) ⟹ f = Θ(h)  [also O, Ω, o, ω]
```

### Reflexivity
```
f = Θ(f), f = O(f), f = Ω(f)
```

### Symmetry
```
f = Θ(g) ⟺ g = Θ(f)
```

### Transpose Symmetry
```
f = O(g) ⟺ g = Ω(f)
f = o(g) ⟺ g = ω(f)
```

---

## 🛠️ Problem-Solving Toolkit

### Proving Θ(g(n))
1. Show upper bound: f ≤ c₂g
2. Show lower bound: f ≥ c₁g
3. Combine: c₁g ≤ f ≤ c₂g

### Proving O(g(n))
- Direct: Show f ≤ cg
- Limit: Show lim f/g ≤ constant

### Proving Ω(g(n))
- Direct: Show cg ≤ f
- Limit: Show lim f/g ≥ constant > 0

### Proving o(g(n))
- Limit: Show lim f/g = 0
- Definition: Show f < cg for ALL c > 0

### Proving ω(g(n))
- Limit: Show lim f/g = ∞
- Definition: Show cg < f for ALL c > 0

---

## 💡 Quick Limit Test

```
lim(n→∞) f(n)/g(n) = ?

0       ⟹  f = o(g)  [and f = O(g)]
c > 0   ⟹  f = Θ(g)  [and f = O(g) and f = Ω(g)]
∞       ⟹  f = ω(g)  [and f = Ω(g)]
```

---

## 📝 Common Examples

### True Statements
```
✓ n = o(n²)
✓ n² = O(n²)
✓ n² = Θ(n²)
✓ n² = Ω(n)
✓ 2^(n+1) = Θ(2^n)
✓ max{f,g} = Θ(f+g)
```

### False Statements
```
✗ n² = o(n²)
✗ n² = ω(n²)
✗ 2^(2n) = O(2^n)
✗ "At least O(n²)" [meaningless!]
```

---

## ⚠️ Common Mistakes

### Mistake 1: Confusing O with Θ
```
✗ "Algorithm is O(n²)" when you mean Θ(n²)
✓ Use Θ for tight bounds
```

### Mistake 2: "At least" with O
```
✗ "At least O(n²)" [MEANINGLESS]
✓ "At least Ω(n²)" or "At most O(n²)"
```

### Mistake 3: Constant vs Variable in Exponent
```
✓ 2^(n+c) = Θ(2^n)  [constant: OK]
✗ 2^(cn) ≠ O(2^n)   [variable: NOT OK for c>1]
```

### Mistake 4: Wrong Limit Interpretation
```
✗ lim f/g = 0 means f = O(g) only
✓ lim f/g = 0 means f = o(g) [stricter!]
```

---

## 🎯 Problem Recognition

### Type 1: Prove max{f,g} = Θ(f+g)
**Approach:** Show (1/2)(f+g) ≤ max ≤ (f+g)

### Type 2: Explain Meaningless Statement
**Approach:** Identify mixing of bound directions

### Type 3: Is 2^(n+1) = O(2^n)?
**Approach:** Simplify or use limit test

### Type 4: Prove Theorem 3.1
**Approach:** Use definitions, algebra

### Type 5: If-and-only-if
**Approach:** Prove both ⟹ and ⟸

### Type 6: Empty Set
**Approach:** Proof by contradiction

### Type 7: Two Parameters
**Approach:** Generalize definitions

---

## 📐 Proof Templates

### Θ-notation Proof
```
Claim: f(n) = Θ(g(n))

Upper bound:
  f(n) ≤ c₂·g(n) for n ≥ n₀
  [show work]

Lower bound:
  f(n) ≥ c₁·g(n) for n ≥ n₀
  [show work]

Conclusion: f(n) = Θ(g(n)) ✓
```

### If-and-Only-If Proof
```
Claim: A ⟺ B

(⟹) Assume A. Show B.
  [proof steps]
  Therefore B. ✓

(⟸) Assume B. Show A.
  [proof steps]
  Therefore A. ✓

Conclusion: A ⟺ B ✓
```

### Contradiction Proof
```
Claim: Statement S is true

Assume: S is false
  [derive contradiction]
  Contradiction! ⚡

Conclusion: S must be true ✓
```

---

## 🚀 Exam Strategy

### Before Solving
- [ ] Read problem carefully
- [ ] Identify problem type
- [ ] Write down relevant definitions
- [ ] Choose proof technique

### While Solving
- [ ] Show all work
- [ ] Justify each step
- [ ] Use proper notation
- [ ] State conclusion clearly

### After Solving
- [ ] Verify with example
- [ ] Check constants work
- [ ] Ensure n₀ is valid

---

## 🧮 Essential Facts

### Asymptotic Arithmetic
```
Θ(f) + Θ(g) = Θ(f+g)
Θ(f) · Θ(g) = Θ(f·g)
Θ(cf) = Θ(f)  [constant c]
```

### Exponential Rules
```
a^(n+c) = Θ(a^n)     [constant shift]
a^(cn) = ω(a^n)      [for c > 1]
(a^n)^c = a^(cn)
```

### Max/Min Properties
```
max{f,g} = Θ(f+g)
min{f,g} = Θ(f+g)  [if f,g same order]
```

---

## 💪 Quick Self-Test

### Can you answer these in 30 seconds?

1. What's the difference between O and o?
2. Is n² = Θ(n²)? Why?
3. Is 2^(2n) = O(2^n)? Why not?
4. What does "at least O(n²)" mean? (Trick!)
5. If f = O(g) and g = O(h), what can you say about f and h?

### Answers
1. O: ≤ (some c), o: < (all c), lim=0
2. Yes, c₁=c₂=1 works
3. No, ratio = 2^n → ∞
4. Meaningless! (O is upper bound)
5. f = O(h) by transitivity

---

## 📋 Checklist for Each Problem

- [ ] Understand what's being asked
- [ ] Write down definitions
- [ ] Choose proof technique
- [ ] Execute proof step-by-step
- [ ] Verify with example
- [ ] State conclusion

---

## 🎓 Last-Minute Review

### 5 Minutes Before Exam

1. **Big 5:** Θ (=), O (≤), Ω (≥), o (<), ω (>)
2. **Limit test:** 0 → o, c → Θ, ∞ → ω
3. **Key relationship:** Θ = O ∩ Ω
4. **Common mistake:** "at least O" is meaningless
5. **Exponentials:** 2^(n+1) = Θ(2^n), but 2^(2n) ≠ O(2^n)

---

## 🏆 You Got This!

**Remember:**
- O, Ω, Θ are like ≤, ≥, =
- o, ω are like <, >
- Use limit test when possible
- Show all work for partial credit
- Verify with examples

**Confidence Boosters:**
- You understand the definitions ✓
- You can use limit tests ✓
- You know proof techniques ✓
- You've practiced all problem types ✓

**Good luck! 🎉**

---

**End of Cheat Sheet**
