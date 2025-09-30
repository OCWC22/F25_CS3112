# Homework Solutions: Section 3.3 - Fibonacci Numbers and the Golden Ratio

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 3.3 (Growth of Functions - Fibonacci Numbers)  
**Date:** 2025-09-29

---

## Problem 3.3-7: Golden Ratio and its Conjugate

### Problem Statement
Show that the golden ratio φ and its conjugate φ̂ both satisfy the equation:
```
x² = x + 1
```

---

### Solution Overview
We need to prove that both φ and φ̂ are roots of the quadratic equation x² = x + 1.

---

### Step 1: Define the Golden Ratio and its Conjugate

**Definition of Golden Ratio (φ):**
```
φ = (1 + √5) / 2
```

**Definition of Conjugate (φ̂):**
```
φ̂ = (1 - √5) / 2
```

**Why these definitions?**
- The golden ratio φ (phi) appears naturally in Fibonacci sequences and many mathematical contexts
- The conjugate φ̂ (phi-hat) is the other root of the characteristic equation for Fibonacci numbers
- They differ only in the sign before √5

**Numerical values (for intuition):**
- φ ≈ 1.618...
- φ̂ ≈ -0.618...

---

### Step 2: Rewrite the Equation to Standard Form

**Original equation:**
```
x² = x + 1
```

**Standard quadratic form:**
```
x² - x - 1 = 0
```

**Why this matters:**
- Standard form allows us to use the quadratic formula
- We can identify coefficients: a = 1, b = -1, c = -1

---

### Step 3: Solve Using the Quadratic Formula

**Quadratic Formula:**
```
x = (-b ± √(b² - 4ac)) / (2a)
```

**Substitute our coefficients (a=1, b=-1, c=-1):**
```
x = (-(-1) ± √((-1)² - 4(1)(-1))) / (2(1))
x = (1 ± √(1 + 4)) / 2
x = (1 ± √5) / 2
```

**Two solutions:**
```
x₁ = (1 + √5) / 2 = φ     (golden ratio)
x₂ = (1 - √5) / 2 = φ̂     (conjugate)
```

**What this proves:**
- Both φ and φ̂ are roots of x² - x - 1 = 0
- Therefore, both satisfy x² = x + 1

---

### Step 4: Verify by Direct Substitution for φ

**Claim:** φ² = φ + 1

**Calculate φ²:**
```
φ² = ((1 + √5) / 2)²
   = (1 + √5)² / 4
   = (1 + 2√5 + 5) / 4
   = (6 + 2√5) / 4
   = (3 + √5) / 2
```

**Calculate φ + 1:**
```
φ + 1 = (1 + √5) / 2 + 1
      = (1 + √5) / 2 + 2/2
      = (1 + √5 + 2) / 2
      = (3 + √5) / 2
```

**Comparison:**
```
φ² = (3 + √5) / 2
φ + 1 = (3 + √5) / 2
```

**Therefore: φ² = φ + 1 ✓**

---

### Step 5: Verify by Direct Substitution for φ̂

**Claim:** φ̂² = φ̂ + 1

**Calculate φ̂²:**
```
φ̂² = ((1 - √5) / 2)²
   = (1 - √5)² / 4
   = (1 - 2√5 + 5) / 4
   = (6 - 2√5) / 4
   = (3 - √5) / 2
```

**Calculate φ̂ + 1:**
```
φ̂ + 1 = (1 - √5) / 2 + 1
      = (1 - √5) / 2 + 2/2
      = (1 - √5 + 2) / 2
      = (3 - √5) / 2
```

**Comparison:**
```
φ̂² = (3 - √5) / 2
φ̂ + 1 = (3 - √5) / 2
```

**Therefore: φ̂² = φ̂ + 1 ✓**

---

### Step 6: Additional Properties (Understanding Why This Matters)

**Why is this equation important for Fibonacci numbers?**

The Fibonacci recurrence relation is:
```
Fₙ = Fₙ₋₁ + Fₙ₋₂
```

If we assume a solution of the form Fₙ = xⁿ, we get:
```
xⁿ = xⁿ⁻¹ + xⁿ⁻²
```

Dividing by xⁿ⁻²:
```
x² = x + 1
```

This is exactly our equation! This means φ and φ̂ are the characteristic roots of the Fibonacci recurrence.

---

### Final Answer for Problem 3.3-7

**Proven:** Both φ = (1 + √5)/2 and φ̂ = (1 - √5)/2 satisfy x² = x + 1

**Methods used:**
1. ✓ Quadratic formula shows they are the two roots
2. ✓ Direct substitution for φ confirms φ² = φ + 1
3. ✓ Direct substitution for φ̂ confirms φ̂² = φ̂ + 1

---

---

## Problem 3.3-8: Binet's Formula for Fibonacci Numbers

### Problem Statement
Prove by induction that the i-th Fibonacci number satisfies:
```
Fᵢ = (φⁱ - φ̂ⁱ) / √5
```
where φ is the golden ratio and φ̂ is its conjugate.

**This formula is called Binet's Formula.**

---

### Solution Overview

We will use **mathematical induction** with a **strong induction** approach (using two base cases).

**Induction Structure:**
1. **Base Cases:** Verify F₀ and F₁
2. **Inductive Hypothesis:** Assume true for Fₖ and Fₖ₊₁
3. **Inductive Step:** Prove true for Fₖ₊₂
4. **Conclusion:** By induction, true for all i ≥ 0

---

### Preliminary: Recall Key Definitions

**Fibonacci Sequence:**
```
F₀ = 0
F₁ = 1
Fₙ = Fₙ₋₁ + Fₙ₋₂  for n ≥ 2
```

**Golden Ratio and Conjugate:**
```
φ = (1 + √5) / 2
φ̂ = (1 - √5) / 2
```

**Key Property (from Problem 3.3-7):**
```
φ² = φ + 1
φ̂² = φ̂ + 1
```

---

### Step 1: Base Case - Verify F₀

**What we need to show:**
```
F₀ = (φ⁰ - φ̂⁰) / √5 = 0
```

**Left side (definition):**
```
F₀ = 0
```

**Right side (Binet's formula):**
```
(φ⁰ - φ̂⁰) / √5 = (1 - 1) / √5 = 0 / √5 = 0
```

**Conclusion:**
```
F₀ = 0 = (φ⁰ - φ̂⁰) / √5 ✓
```

**Why this works:**
- Any number to the power 0 equals 1
- So φ⁰ = 1 and φ̂⁰ = 1
- Their difference is 0, matching F₀

---

### Step 2: Base Case - Verify F₁

**What we need to show:**
```
F₁ = (φ¹ - φ̂¹) / √5 = 1
```

**Left side (definition):**
```
F₁ = 1
```

**Right side (Binet's formula):**
```
(φ¹ - φ̂¹) / √5 = (φ - φ̂) / √5
```

**Calculate φ - φ̂:**
```
φ - φ̂ = (1 + √5)/2 - (1 - √5)/2
      = (1 + √5 - 1 + √5) / 2
      = (2√5) / 2
      = √5
```

**Therefore:**
```
(φ - φ̂) / √5 = √5 / √5 = 1
```

**Conclusion:**
```
F₁ = 1 = (φ¹ - φ̂¹) / √5 ✓
```

**Why this works:**
- The difference between φ and φ̂ is exactly √5
- Dividing by √5 gives us 1, matching F₁

---

### Step 3: Inductive Hypothesis (Strong Induction)

**Assume the formula holds for two consecutive Fibonacci numbers:**

For some k ≥ 1, assume:
```
Fₖ = (φᵏ - φ̂ᵏ) / √5     ... (Hypothesis 1)
Fₖ₊₁ = (φᵏ⁺¹ - φ̂ᵏ⁺¹) / √5   ... (Hypothesis 2)
```

**Why strong induction?**
- The Fibonacci recurrence uses TWO previous terms
- We need to assume both Fₖ and Fₖ₊₁ to prove Fₖ₊₂
- This is called "strong" because we assume more than one case

---

### Step 4: Inductive Step - Prove for Fₖ₊₂

**Goal:** Show that Fₖ₊₂ = (φᵏ⁺² - φ̂ᵏ⁺²) / √5

**Start with the Fibonacci recurrence:**
```
Fₖ₊₂ = Fₖ₊₁ + Fₖ
```

**Substitute using our inductive hypotheses:**
```
Fₖ₊₂ = (φᵏ⁺¹ - φ̂ᵏ⁺¹) / √5 + (φᵏ - φ̂ᵏ) / √5
```

**Combine fractions (same denominator):**
```
Fₖ₊₂ = (φᵏ⁺¹ - φ̂ᵏ⁺¹ + φᵏ - φ̂ᵏ) / √5
```

**Rearrange terms:**
```
Fₖ₊₂ = (φᵏ⁺¹ + φᵏ - φ̂ᵏ⁺¹ - φ̂ᵏ) / √5
```

**Factor out φᵏ and φ̂ᵏ:**
```
Fₖ₊₂ = (φᵏ(φ + 1) - φ̂ᵏ(φ̂ + 1)) / √5
```

**Why this factoring?**
- φᵏ⁺¹ = φᵏ · φ¹ = φᵏ · φ
- φᵏ = φᵏ · 1
- So: φᵏ⁺¹ + φᵏ = φᵏ · φ + φᵏ · 1 = φᵏ(φ + 1)
- Same logic for φ̂ terms

---

### Step 5: Apply the Key Property

**Recall from Problem 3.3-7:**
```
φ² = φ + 1
φ̂² = φ̂ + 1
```

**Substitute into our expression:**
```
Fₖ₊₂ = (φᵏ · φ² - φ̂ᵏ · φ̂²) / √5
```

**Simplify using exponent rules:**
```
Fₖ₊₂ = (φᵏ⁺² - φ̂ᵏ⁺²) / √5
```

**This is exactly what we wanted to prove!**

---

### Step 6: Conclusion of Induction

**What we've shown:**

1. ✓ **Base cases:** Formula holds for F₀ and F₁
2. ✓ **Inductive step:** If formula holds for Fₖ and Fₖ₊₁, then it holds for Fₖ₊₂
3. ✓ **By mathematical induction:** Formula holds for all i ≥ 0

**Therefore, Binet's Formula is proven:**
```
Fᵢ = (φⁱ - φ̂ⁱ) / √5  for all i ≥ 0
```

---

### Step 7: Understanding Why This Formula is Amazing

**Remarkable properties:**

1. **Closed-form solution:** We can compute Fᵢ directly without recursion
2. **Irrational to integer:** Despite φ and φ̂ being irrational, their combination always gives integers!
3. **Asymptotic behavior:** Since |φ̂| < 1, we have φ̂ⁱ → 0 as i → ∞

**Asymptotic approximation:**
```
Fᵢ ≈ φⁱ / √5  for large i
```

This means Fibonacci numbers grow exponentially at rate φ ≈ 1.618.

---

### Step 8: Verification with Examples

**Let's verify with F₂, F₃, F₄:**

**F₂ = 1 (by definition: F₂ = F₁ + F₀ = 1 + 0 = 1)**

Using Binet's formula:
```
F₂ = (φ² - φ̂²) / √5
   = ((3 + √5)/2 - (3 - √5)/2) / √5    [from Problem 3.3-7]
   = ((3 + √5 - 3 + √5)/2) / √5
   = (2√5/2) / √5
   = √5 / √5
   = 1 ✓
```

**F₃ = 2 (by definition: F₃ = F₂ + F₁ = 1 + 1 = 2)**

Using Binet's formula:
```
φ³ = φ² · φ = (φ + 1) · φ = φ² + φ = (φ + 1) + φ = 2φ + 1
   = 2(1 + √5)/2 + 1 = (1 + √5) + 1 = (2 + √5)

φ̂³ = φ̂² · φ̂ = (φ̂ + 1) · φ̂ = φ̂² + φ̂ = (φ̂ + 1) + φ̂ = 2φ̂ + 1
   = 2(1 - √5)/2 + 1 = (1 - √5) + 1 = (2 - √5)

F₃ = (φ³ - φ̂³) / √5
   = ((2 + √5) - (2 - √5)) / √5
   = (2√5) / √5
   = 2 ✓
```

**F₄ = 3 (by definition: F₄ = F₃ + F₂ = 2 + 1 = 3)**

Using Binet's formula:
```
φ⁴ = φ³ · φ = (2φ + 1) · φ = 2φ² + φ = 2(φ + 1) + φ = 3φ + 2
   = 3(1 + √5)/2 + 2 = (3 + 3√5)/2 + 4/2 = (7 + 3√5)/2

φ̂⁴ = φ̂³ · φ̂ = (2φ̂ + 1) · φ̂ = 2φ̂² + φ̂ = 2(φ̂ + 1) + φ̂ = 3φ̂ + 2
   = 3(1 - √5)/2 + 2 = (3 - 3√5)/2 + 4/2 = (7 - 3√5)/2

F₄ = (φ⁴ - φ̂⁴) / √5
   = ((7 + 3√5)/2 - (7 - 3√5)/2) / √5
   = ((6√5)/2) / √5
   = 3√5 / √5
   = 3 ✓
```

All examples check out!

---

### Final Answer for Problem 3.3-8

**Proven by mathematical induction:**

The i-th Fibonacci number satisfies Binet's Formula:
```
Fᵢ = (φⁱ - φ̂ⁱ) / √5
```

where:
- φ = (1 + √5) / 2 (golden ratio)
- φ̂ = (1 - √5) / 2 (conjugate)

**Proof technique:** Strong induction with two base cases
**Key insight:** The property φ² = φ + 1 (and similarly for φ̂) is essential for the inductive step

---

## Summary and Key Takeaways

### Problem 3.3-7 Takeaways
- The golden ratio and its conjugate are roots of x² = x + 1
- This equation arises naturally from the Fibonacci recurrence relation
- Both values can be verified by direct substitution or the quadratic formula

### Problem 3.3-8 Takeaways
- Binet's formula provides a closed-form expression for Fibonacci numbers
- Strong induction is necessary because Fibonacci uses two previous terms
- The key property φ² = φ + 1 makes the inductive step work
- Despite using irrational numbers, the formula always produces integers
- Fibonacci numbers grow exponentially at rate φ ≈ 1.618

### Connections to Algorithm Analysis
- Understanding Fibonacci growth helps analyze recursive algorithms
- The exponential growth rate φⁱ explains why naive recursive Fibonacci is slow
- Binet's formula shows Fᵢ = Θ(φⁱ), giving precise asymptotic bounds

---

**End of Solutions**
