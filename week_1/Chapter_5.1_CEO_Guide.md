# Chapter 5.1 CEO Guide: Sequences & Summations

## CORE DEFINITIONS

### 1. SEQUENCE
**What:** Function with consecutive integer inputs
**Notation:** aₖ = value at position k
**CEO Analogy:** Customer pipeline - each customer (k) has a value (aₖ)
**Example:** aₖ = 2k → {2, 4, 6, 8, ...}

### 2. SUMMATION (Σ)
**What:** Σ(k=m to n) aₖ = aₘ + aₘ₊₁ + ... + aₙ
**CEO Analogy:** Total revenue from store m to store n
**Memory:** Σ = "Add them all up"
- Bottom number = start
- Top number = stop
- Right side = what to add

**Example:**
```
Σ(k=1 to 4) k² = 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
```

### 3. PRODUCT (Π)
**What:** Π(k=m to n) aₖ = aₘ · aₘ₊₁ · ... · aₙ
**CEO Analogy:** Compound growth rate over periods
**Memory:** Π = "Multiply them all"

**Example:**
```
Π(k=2 to 5) k = 2 × 3 × 4 × 5 = 120
```

### 4. FACTORIAL (n!)
**What:** n! = n × (n-1) × ... × 2 × 1, and 0! = 1
**CEO Analogy:** Ways to arrange n people in a line
**Memory:** n! = n × (n-1)!

**Values:**
- 0! = 1, 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120

**Simplification:** n!/(n-k)! = n(n-1)...(n-k+1)

### 5. BINOMIAL COEFFICIENT (n choose r)
**What:** C(n,r) = n!/(r!(n-r)!)
**CEO Analogy:** Ways to select r people from n for a committee
**Memory:** C(n,r) = C(n,n-r) (symmetry)

**Special cases:**
- C(n,0) = 1
- C(n,1) = n
- C(n,2) = n(n-1)/2

**Example:** C(5,2) = 5!/(2!3!) = (5×4)/(2×1) = 10

### 6. SUMMATION PROPERTIES
1. **Σ(aₖ + bₖ) = Σaₖ + Σbₖ** (split sums)
2. **c·Σaₖ = Σ(c·aₖ)** (factor out constants)
3. **(Πaₖ)·(Πbₖ) = Π(aₖ·bₖ)** (combine products)

---

## SOLVED PROBLEMS (Section 5.1 - Odd, Black, Non-Star)

### #1: aₖ = k/(10+k), k ≥ 1
```
a₁ = 1/11, a₂ = 1/6, a₃ = 3/13, a₄ = 2/7
```

### #3: cᵢ = (-1)ⁱ/3ⁱ, i ≥ 0
```
c₀ = 1, c₁ = -1/3, c₂ = 1/9, c₃ = -1/27
```

### #5: eₙ = ⌊n/2⌋ - 2, n ≥ 0
```
e₀ = -2, e₁ = -2, e₂ = -1, e₃ = -1
```

### #11: Find formula for 1, -2, 3, -4, 5, ...
```
aₖ = (-1)^(k+1) · k
```

### #13: Find formula for 1, -1/2, 1/3, -1/4, ...
```
aₖ = (-1)^(k+1) / k
```

### #15: Find formula for 0, 1/2, 2/3, 3/4, ...
```
aₙ = n/(n+1)
```

### #19: Σ(k+1) from k=1 to 4
```
= 2 + 3 + 4 + 5 = 14
```

### #21: Σ(1/2^k) from k=0 to 3
```
= 1 + 1/2 + 1/4 + 1/8 = 15/8
```

### #23: Σ i(i+1) from i=0 to 4
```
= 0 + 2 + 6 + 12 + 20 = 40
```

### #29: Expand Σ(-2)ⁱ from i=0 to 4
```
= 1 + (-2) + 4 + (-8) + 16 = 11
```

### #31: Expand Σ(1/2ⁱ) from i=0 to 4
```
= 1 + 1/2 + 1/4 + 1/8 + 1/16 = 31/16
```

### #33: Evaluate Σ(1/k²) for n=1
```
= 1/1² = 1
```

### #43: Write 1² - 2² + 3² - 4² + 5² - 6² + 7² as summation
```
Σ(k=1 to 7) (-1)^(k+1) · k²
```

### #45: Write (2²-1)·(3²-1)·(4²-1) as product
```
Π(k=2 to 4) (k² - 1)
```

### #62: Compute 4!/3!
```
= (4×3!)/3! = 4
```

### #65: Compute n!/(n-1)!
```
= n
```

### #67: Compute n!/(n-2)!
```
= n(n-1)
```

### #71: Compute C(5,3)
```
= 5!/(3!2!) = (5×4)/(2×1) = 10
```

### #73: Compute C(8,5)
```
= C(8,3) = 8!/(3!5!) = (8×7×6)/(3×2×1) = 56
```

### #75: Compute C(n,2)
```
= n!/(2!(n-2)!) = n(n-1)/2
```

---

## QUICK REFERENCE

### Common Formulas
- Σ(k=1 to n) k = n(n+1)/2
- Σ(k=1 to n) k² = n(n+1)(2n+1)/6
- Σ(k=1 to n) c = cn (constant c)

### Simplification Tips
1. **Cancel factorials early:** 10!/8! = 10×9
2. **Use symmetry:** C(8,5) = C(8,3)
3. **Factor constants:** Σ(3k) = 3·Σk

### Memory Hooks
- **Σ** = Financial audit (sum revenues)
- **Π** = Compound growth (multiply rates)
- **n!** = Lineup arrangements
- **C(n,r)** = Committee selection

---

## EXAM STRATEGY

1. **For sequences:** Plug in values, look for patterns
2. **For summations:** Expand first few terms, then simplify
3. **For factorials:** Cancel common terms before multiplying
4. **For combinations:** Use symmetry and cancel early

**Common mistakes:**
- Forgetting 0! = 1
- Not canceling factorials in fractions
- Mixing up Σ and Π notation
- Off-by-one errors in indices
