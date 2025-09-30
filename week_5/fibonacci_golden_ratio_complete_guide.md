# Complete Guide: Fibonacci, Golden Ratio, and Mathematical Foundations

**Purpose:** Build intuitive understanding from absolute zero  
**Audience:** Someone who has never seen Fibonacci or φ before  
**Approach:** First principles → Intuition → Formal math → Applications

---

## Table of Contents

1. [Foundation: What You Need First](#foundation)
2. [The Fibonacci Sequence](#fibonacci-sequence)
3. [The Golden Ratio φ](#golden-ratio)
4. [The Conjugate φ̂ (and what "conjugate" means)](#conjugate)
5. [Why φ² = φ + 1 (The Magic Equation)](#magic-equation)
6. [Binet's Formula (Closed Form)](#binets-formula)
7. [Complete Worked Example: Problem 3.3-7](#worked-example)
8. [Mathematical Toolkit](#toolkit)
9. [When and Why You Use These Techniques](#applications)

---

<a name="foundation"></a>
## 1. Foundation: What You Need First

### 1.1 Numbers and Variables

**Numbers** are quantities: 1, 2, 3, -5, 0.5, π, √2

**Variables** are placeholders for unknown numbers: x, y, n

**Equations** state that two expressions are equal:
```
2x + 3 = 7
```

**Solving** means finding what value makes it true:
```
2x + 3 = 7
2x = 4
x = 2  ✓
```

### 1.2 Powers (Exponents)

**Definition:** x^n means "multiply x by itself n times"

```
x^1 = x
x^2 = x · x
x^3 = x · x · x
x^4 = x · x · x · x
```

**Examples:**
```
2^3 = 2 · 2 · 2 = 8
5^2 = 5 · 5 = 25
10^4 = 10,000
```

**Special cases:**
```
x^0 = 1 (for any x ≠ 0)
x^1 = x
```

### 1.3 Square Roots

**Definition:** √a is the number that, when squared, gives a

```
√4 = 2    because 2² = 4
√9 = 3    because 3² = 9
√16 = 4   because 4² = 16
```

**Irrational square roots:**
```
√2 ≈ 1.414...  (never ends, never repeats)
√5 ≈ 2.236...  (also irrational)
```

### 1.4 Polynomials

**Definition:** An expression with variables raised to whole number powers

**General form:**
```
a_n·x^n + a_(n-1)·x^(n-1) + ... + a_2·x² + a_1·x + a_0
```

**Examples:**
```
x² + 3x + 2        (degree 2, called "quadratic")
x³ - 5x² + x - 7   (degree 3, called "cubic")
2x + 5             (degree 1, called "linear")
```

**Degree** = highest power of x

### 1.5 Polynomial Equations

**Definition:** Setting a polynomial equal to something (usually 0)

```
x² - 5x + 6 = 0
```

**Roots/Solutions:** Values of x that make the equation true

**Example:**
```
x² - 5x + 6 = 0
This factors as: (x - 2)(x - 3) = 0
So x = 2 or x = 3 are the roots
```

**Check:**
```
x = 2: 2² - 5(2) + 6 = 4 - 10 + 6 = 0 ✓
x = 3: 3² - 5(3) + 6 = 9 - 15 + 6 = 0 ✓
```

---

<a name="fibonacci-sequence"></a>
## 2. The Fibonacci Sequence

### 2.1 What is a Sequence?

**Sequence:** An ordered list of numbers

```
1, 2, 3, 4, 5, ...        (counting numbers)
2, 4, 6, 8, 10, ...       (even numbers)
1, 4, 9, 16, 25, ...      (perfect squares)
```

**Notation:** We write F_n to mean "the nth term"
```
F_1 = first term
F_2 = second term
F_3 = third term
```

### 2.2 The Fibonacci Definition

**The Fibonacci sequence** is defined by a simple rule:

**Starting values:**
```
F_0 = 0
F_1 = 1
```

**Rule for all other terms:**
```
F_n = F_(n-1) + F_(n-2)
```

**In words:** "Each term is the sum of the two previous terms"

### 2.3 Building the Sequence Step by Step

Let's compute the first several terms:

```
F_0 = 0                    (given)
F_1 = 1                    (given)
F_2 = F_1 + F_0 = 1 + 0 = 1
F_3 = F_2 + F_1 = 1 + 1 = 2
F_4 = F_3 + F_2 = 2 + 1 = 3
F_5 = F_4 + F_3 = 3 + 2 = 5
F_6 = F_5 + F_4 = 5 + 3 = 8
F_7 = F_6 + F_5 = 8 + 5 = 13
F_8 = F_7 + F_6 = 13 + 8 = 21
F_9 = F_8 + F_7 = 21 + 13 = 34
F_10 = F_9 + F_8 = 34 + 21 = 55
```

**The sequence:**
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

### 2.4 What is a Recurrence Relation?

**Recurrence relation:** A formula that defines each term using previous terms

The Fibonacci recurrence is:
```
F_n = F_(n-1) + F_(n-2)
```

**Why "recurrence"?** Because it "recurs" - it refers back to itself!

**Other examples:**
```
a_n = 2·a_(n-1)           (each term is double the previous)
    → 1, 2, 4, 8, 16, 32, ...

b_n = b_(n-1) + 3         (add 3 each time)
    → 1, 4, 7, 10, 13, 16, ...
```

### 2.5 Why Fibonacci Matters

**Historical origin:** Leonardo Fibonacci (1202) modeled rabbit population growth

**Modern appearances:**
- Nature: spiral patterns in shells, flowers, pinecones
- Art: proportions in classical architecture
- Computer science: algorithm analysis, data structures
- Finance: Fibonacci retracements in technical analysis

**Key property:** The ratio of consecutive terms approaches a constant!
```
F_2/F_1 = 1/1 = 1.000
F_3/F_2 = 2/1 = 2.000
F_4/F_3 = 3/2 = 1.500
F_5/F_4 = 5/3 = 1.667
F_6/F_5 = 8/5 = 1.600
F_7/F_6 = 13/8 = 1.625
F_8/F_7 = 21/13 = 1.615
F_9/F_8 = 34/21 = 1.619
F_10/F_9 = 55/34 = 1.618
```

This ratio approaches **1.618...** which is the **golden ratio φ**!

---

<a name="golden-ratio"></a>
## 3. The Golden Ratio φ

### 3.1 What is the Golden Ratio?

**The golden ratio** (denoted φ, Greek letter "phi") is a special number approximately equal to 1.618.

**Exact value:**
```
φ = (1 + √5) / 2
```

**Numerical approximation:**
```
φ ≈ 1.618033988749...
```

It's an **irrational number** (decimal never ends, never repeats).

### 3.2 Where Does φ Come From? (Geometric Definition)

**Original definition:** Divide a line segment into two parts such that:

```
The ratio of the whole to the larger part
equals
The ratio of the larger part to the smaller part
```

**Picture:**
```
|------------ a + b ------------|
|------- a -------|--- b ---|

Condition: (a + b)/a = a/b
```

**Solving this equation:**
```
(a + b)/a = a/b
Let φ = a/b (the ratio we want)
Then: (a + b)/a = φ
      a/a + b/a = φ
      1 + 1/φ = φ
      φ + 1 = φ²
      φ² = φ + 1  ← The golden ratio equation!
```

### 3.3 The Golden Ratio Equation

**Key equation:**
```
φ² = φ + 1
```

Or in standard form:
```
φ² - φ - 1 = 0
```

This is a **quadratic equation** (degree 2 polynomial).

### 3.4 Solving for φ (Using Quadratic Formula)

**Quadratic formula:** For ax² + bx + c = 0:
```
x = (-b ± √(b² - 4ac)) / (2a)
```

**Our equation:** x² - x - 1 = 0
```
a = 1
b = -1
c = -1
```

**Applying the formula:**
```
x = (-(-1) ± √((-1)² - 4(1)(-1))) / (2(1))
x = (1 ± √(1 + 4)) / 2
x = (1 ± √5) / 2
```

**Two solutions:**
```
x₁ = (1 + √5) / 2 ≈ 1.618  ← This is φ (golden ratio)
x₂ = (1 - √5) / 2 ≈ -0.618 ← This is φ̂ (conjugate)
```

### 3.5 Why φ is Special

**Properties:**
```
φ² = φ + 1           (defining property)
φ³ = φ² + φ = (φ+1) + φ = 2φ + 1
φ⁴ = φ³ + φ² = (2φ+1) + (φ+1) = 3φ + 2
```

**Pattern:** φⁿ can always be written as Aφ + B where A and B are Fibonacci numbers!

**Reciprocal property:**
```
1/φ = φ - 1
```

**Proof:**
```
φ² = φ + 1
Divide by φ:
φ = 1 + 1/φ
1/φ = φ - 1 ✓
```

**Numerical check:**
```
1/1.618 ≈ 0.618 = 1.618 - 1 ✓
```

---

<a name="conjugate"></a>
## 4. The Conjugate φ̂ (and What "Conjugate" Means)

### 4.1 What is the Conjugate?

When we solved φ² - φ - 1 = 0, we got **two** solutions:

```
φ = (1 + √5) / 2 ≈ 1.618
φ̂ = (1 - √5) / 2 ≈ -0.618
```

**φ̂** (phi-hat) is called the **conjugate** of the golden ratio.

### 4.2 What Does "Conjugate" Mean?

**In general:** For expressions involving square roots, the conjugate is formed by changing the sign in front of the square root.

**Examples:**
```
Expression          Conjugate
-----------         ----------
a + √b              a - √b
3 + √7              3 - √7
(1 + √5)/2          (1 - √5)/2
x + √y              x - √y
```

**Why this matters:** Conjugates have special algebraic properties that make them useful.

### 4.3 Why Do We Care About the Conjugate?

**Reason 1: It's also a solution**
Both φ and φ̂ satisfy the same equation x² = x + 1.

**Reason 2: They work together in formulas**
The Fibonacci closed form (Binet's formula) needs BOTH:
```
F_n = (φⁿ - φ̂ⁿ) / √5
```

**Reason 3: The conjugate "cancels out" for large n**
Since |φ̂| < 1, the term φ̂ⁿ → 0 as n → ∞.

### 4.4 Properties of φ and φ̂

**Sum:**
```
φ + φ̂ = (1 + √5)/2 + (1 - √5)/2
      = (1 + √5 + 1 - √5)/2
      = 2/2
      = 1
```

**Product:**
```
φ · φ̂ = [(1 + √5)/2] · [(1 - √5)/2]
      = (1 + √5)(1 - √5) / 4
      = (1 - 5) / 4          [difference of squares: (a+b)(a-b) = a² - b²]
      = -4/4
      = -1
```

**These come from Vieta's formulas:** For x² - x - 1 = 0:
- Sum of roots = -(-1)/1 = 1 ✓
- Product of roots = -1/1 = -1 ✓

### 4.5 Both Satisfy the Same Equation

**For φ:**
```
φ² = φ + 1 ✓
```

**For φ̂:**
```
φ̂² = φ̂ + 1 ✓
```

**Why?** Because they're both roots of x² - x - 1 = 0!

### 4.6 Numerical Values

```
φ ≈ 1.618033988749894848...
φ̂ ≈ -0.618033988749894848...
```

**Notice:** φ̂ = -1/φ (approximately)

**Exact relation:**
```
φ̂ = 1 - φ
```

**Proof:**
```
φ + φ̂ = 1  (from sum property)
φ̂ = 1 - φ ✓
```

---

<a name="magic-equation"></a>
## 5. Why φ² = φ + 1 (The Magic Equation)

### 5.1 Three Ways to Understand This Equation

#### Method 1: Geometric (Rectangle Division)

**Golden rectangle:** A rectangle where length/width = φ

If you cut off a square, the remaining rectangle has the same proportions!

```
|-------- φ --------|
|                   |  1
|-------|-----------|
   1       φ-1

Condition: φ/1 = 1/(φ-1)
Solving: φ(φ-1) = 1
         φ² - φ = 1
         φ² = φ + 1 ✓
```

#### Method 2: Algebraic (From Fibonacci)

If we assume F_n grows like rⁿ for some constant r:
```
F_n = F_(n-1) + F_(n-2)
rⁿ = rⁿ⁻¹ + rⁿ⁻²
```

Divide by rⁿ⁻²:
```
r² = r + 1 ✓
```

So the growth rate must satisfy this equation!

#### Method 3: Direct Verification

**Claim:** φ = (1 + √5)/2 satisfies φ² = φ + 1

**Compute φ²:**
```
φ² = [(1 + √5)/2]²
   = (1 + √5)² / 4
   = (1 + 2√5 + 5) / 4    [expand (a+b)² = a² + 2ab + b²]
   = (6 + 2√5) / 4
   = (3 + √5) / 2
```

**Compute φ + 1:**
```
φ + 1 = (1 + √5)/2 + 1
      = (1 + √5)/2 + 2/2
      = (1 + √5 + 2)/2
      = (3 + √5)/2
```

**Compare:**
```
φ² = (3 + √5)/2
φ + 1 = (3 + √5)/2
Therefore: φ² = φ + 1 ✓
```

### 5.2 Why This Equation is Powerful

**Consequence 1:** We can compute any power of φ using addition!
```
φ² = φ + 1
φ³ = φ · φ² = φ(φ + 1) = φ² + φ = (φ + 1) + φ = 2φ + 1
φ⁴ = φ · φ³ = φ(2φ + 1) = 2φ² + φ = 2(φ + 1) + φ = 3φ + 2
φ⁵ = φ · φ⁴ = φ(3φ + 2) = 3φ² + 2φ = 3(φ + 1) + 2φ = 5φ + 3
```

**Pattern:** φⁿ = F_n·φ + F_(n-1) where F_n is the nth Fibonacci number!

**Consequence 2:** Powers of φ grow like Fibonacci numbers
```
φ¹ ≈ 1.618
φ² ≈ 2.618
φ³ ≈ 4.236
φ⁴ ≈ 6.854
φ⁵ ≈ 11.090
```

Compare to Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21...

The ratio φⁿ/F_n approaches √5 as n grows!

---

<a name="binets-formula"></a>
## 6. Binet's Formula (Closed Form)

### 6.1 The Problem with Recurrence

**Computing F_100 using recurrence:**
```
F_100 = F_99 + F_98
```

But to get F_99, you need F_98 and F_97...
And to get F_98, you need F_97 and F_96...

You'd have to compute ALL previous Fibonacci numbers! That's slow.

**Question:** Can we compute F_n directly without computing F_1, F_2, ..., F_(n-1)?

**Answer:** YES! Using Binet's formula.

### 6.2 Binet's Formula

**Formula:**
```
F_n = (φⁿ - φ̂ⁿ) / √5
```

Where:
- φ = (1 + √5)/2 ≈ 1.618
- φ̂ = (1 - √5)/2 ≈ -0.618
- √5 ≈ 2.236

**This gives F_n directly!** No need to compute previous terms.

### 6.3 Why Does This Work?

**Step 1:** The general solution to F_n = F_(n-1) + F_(n-2) is:
```
F_n = A·φⁿ + B·φ̂ⁿ
```

for some constants A and B.

**Why?** Because φ and φ̂ are the roots of the characteristic equation r² = r + 1.

**Step 2:** Find A and B using initial conditions:
```
F_0 = 0: A·φ⁰ + B·φ̂⁰ = A + B = 0
F_1 = 1: A·φ¹ + B·φ̂¹ = A·φ + B·φ̂ = 1
```

**From first equation:** B = -A

**Substitute into second:**
```
A·φ - A·φ̂ = 1
A(φ - φ̂) = 1
A = 1/(φ - φ̂)
```

**Compute φ - φ̂:**
```
φ - φ̂ = (1 + √5)/2 - (1 - √5)/2
      = (1 + √5 - 1 + √5)/2
      = 2√5/2
      = √5
```

**Therefore:**
```
A = 1/√5
B = -1/√5
```

**Final formula:**
```
F_n = (1/√5)·φⁿ - (1/√5)·φ̂ⁿ
    = (φⁿ - φ̂ⁿ) / √5 ✓
```

### 6.4 Verifying Binet's Formula

**Check F_0:**
```
F_0 = (φ⁰ - φ̂⁰) / √5
    = (1 - 1) / √5
    = 0 ✓
```

**Check F_1:**
```
F_1 = (φ¹ - φ̂¹) / √5
    = (φ - φ̂) / √5
    = √5 / √5
    = 1 ✓
```

**Check F_2:**
```
F_2 = (φ² - φ̂²) / √5
```

We know φ² = φ + 1 and φ̂² = φ̂ + 1, so:
```
F_2 = ((φ + 1) - (φ̂ + 1)) / √5
    = (φ - φ̂) / √5
    = √5 / √5
    = 1 ✓
```

**Check F_5:**
```
φ⁵ ≈ 11.090
φ̂⁵ ≈ -0.090
F_5 = (11.090 - (-0.090)) / 2.236
    = 11.180 / 2.236
    ≈ 5 ✓
```

### 6.5 Why the Conjugate Term Vanishes

**Key observation:** |φ̂| < 1

```
φ̂ ≈ -0.618
|φ̂| ≈ 0.618 < 1
```

**Therefore:**
```
φ̂¹⁰ ≈ 0.008
φ̂²⁰ ≈ 0.00006
φ̂⁵⁰ ≈ 10⁻¹⁶
```

**For large n:** φ̂ⁿ ≈ 0

**Approximation:**
```
F_n ≈ φⁿ / √5  (for large n)
```

**This is why F_n grows exponentially with base φ!**

---

<a name="worked-example"></a>
## 7. Complete Worked Example: Problem 3.3-7

### Problem Statement

**Show that the golden ratio φ and its conjugate φ̂ both satisfy the equation:**
```
x² = x + 1
```

---

### Solution Method 1: Using the Quadratic Formula

**Step 1:** Rewrite in standard form
```
x² = x + 1
x² - x - 1 = 0
```

**Step 2:** Identify coefficients
```
a = 1, b = -1, c = -1
```

**Step 3:** Apply quadratic formula
```
x = (-b ± √(b² - 4ac)) / (2a)
x = (-(-1) ± √((-1)² - 4(1)(-1))) / (2(1))
x = (1 ± √(1 + 4)) / 2
x = (1 ± √5) / 2
```

**Step 4:** Write the two solutions
```
x₁ = (1 + √5) / 2 = φ
x₂ = (1 - √5) / 2 = φ̂
```

**Conclusion:** Since φ and φ̂ are the roots of x² - x - 1 = 0, they both satisfy x² = x + 1. ✓

---

### Solution Method 2: Direct Verification for φ

**Given:** φ = (1 + √5) / 2

**Claim:** φ² = φ + 1

**Compute Left Side (φ²):**
```
φ² = [(1 + √5) / 2]²
   = (1 + √5)² / 4
```

**Expand (1 + √5)²:**
```
(1 + √5)² = 1² + 2(1)(√5) + (√5)²
          = 1 + 2√5 + 5
          = 6 + 2√5
```

**Therefore:**
```
φ² = (6 + 2√5) / 4
   = 2(3 + √5) / 4
   = (3 + √5) / 2
```

**Compute Right Side (φ + 1):**
```
φ + 1 = (1 + √5) / 2 + 1
      = (1 + √5) / 2 + 2/2
      = (1 + √5 + 2) / 2
      = (3 + √5) / 2
```

**Compare:**
```
Left side:  φ² = (3 + √5) / 2
Right side: φ + 1 = (3 + √5) / 2
```

**Conclusion:** φ² = φ + 1 ✓

---

### Solution Method 3: Direct Verification for φ̂

**Given:** φ̂ = (1 - √5) / 2

**Claim:** φ̂² = φ̂ + 1

**Compute Left Side (φ̂²):**
```
φ̂² = [(1 - √5) / 2]²
   = (1 - √5)² / 4
```

**Expand (1 - √5)²:**
```
(1 - √5)² = 1² - 2(1)(√5) + (√5)²
          = 1 - 2√5 + 5
          = 6 - 2√5
```

**Therefore:**
```
φ̂² = (6 - 2√5) / 4
   = 2(3 - √5) / 4
   = (3 - √5) / 2
```

**Compute Right Side (φ̂ + 1):**
```
φ̂ + 1 = (1 - √5) / 2 + 1
      = (1 - √5) / 2 + 2/2
      = (1 - √5 + 2) / 2
      = (3 - √5) / 2
```

**Compare:**
```
Left side:  φ̂² = (3 - √5) / 2
Right side: φ̂ + 1 = (3 - √5) / 2
```

**Conclusion:** φ̂² = φ̂ + 1 ✓

---

### Why This Matters

**Connection to Fibonacci:**

The equation x² = x + 1 is the **characteristic equation** for the Fibonacci recurrence.

If we assume F_n = xⁿ and substitute into F_n = F_(n-1) + F_(n-2):
```
xⁿ = xⁿ⁻¹ + xⁿ⁻²
```

Divide by xⁿ⁻²:
```
x² = x + 1 ✓
```

So φ and φ̂ are the "growth rates" of Fibonacci!

---

<a name="toolkit"></a>
## 8. Mathematical Toolkit

### 8.1 Quadratic Formula (MEMORIZE THIS)

**For:** ax² + bx + c = 0

**Solution:**
```
x = (-b ± √(b² - 4ac)) / (2a)
```

**The discriminant:** Δ = b² - 4ac
- If Δ > 0: two distinct real roots
- If Δ = 0: one repeated real root
- If Δ < 0: two complex (non-real) roots

### 8.2 Vieta's Formulas

**For:** x² + px + q = 0 with roots r₁, r₂

```
r₁ + r₂ = -p
r₁ · r₂ = q
```

**For:** x² - x - 1 = 0 (our equation)
```
φ + φ̂ = -(-1) = 1 ✓
φ · φ̂ = -1 ✓
```

### 8.3 Algebraic Identities

**Square of sum:**
```
(a + b)² = a² + 2ab + b²
```

**Square of difference:**
```
(a - b)² = a² - 2ab + b²
```

**Difference of squares:**
```
(a + b)(a - b) = a² - b²
```

**Example:**
```
(1 + √5)(1 - √5) = 1² - (√5)² = 1 - 5 = -4
```

### 8.4 Working with Square Roots

**Multiplication:**
```
√a · √b = √(ab)
Example: √2 · √3 = √6
```

**Division:**
```
√a / √b = √(a/b)
Example: √8 / √2 = √4 = 2
```

**Squaring:**
```
(√a)² = a
Example: (√5)² = 5
```

**Rationalizing denominators:**
```
1/√a = √a/a
Example: 1/√5 = √5/5
```

### 8.5 Recurrence Relations

**Linear homogeneous recurrence:**
```
a_n = c₁·a_(n-1) + c₂·a_(n-2)
```

**Characteristic equation:**
```
r² = c₁·r + c₂
or
r² - c₁·r - c₂ = 0
```

**General solution:**
```
a_n = A·r₁ⁿ + B·r₂ⁿ
```

where r₁, r₂ are roots, A, B determined by initial conditions.

---

<a name="applications"></a>
## 9. When and Why You Use These Techniques

### 9.1 When to Use Characteristic Equation Method

**✓ Use when:**
- Linear recurrence with constant coefficients
- Want closed-form formula
- Need asymptotic behavior
- Proving identities

**✗ Don't use when:**
- Nonlinear recurrence (e.g., a_n = a_(n-1) · a_(n-2))
- Variable coefficients
- Non-homogeneous (has extra terms)

### 9.2 Real-World Applications

**Computer Science:**
- Algorithm analysis (divide-and-conquer recurrences)
- Data structure analysis (tree heights, path lengths)
- Complexity theory

**Nature:**
- Spiral patterns (shells, galaxies)
- Plant growth (leaf arrangements, flower petals)
- Population dynamics

**Art & Architecture:**
- Golden rectangle in classical design
- Proportions in Renaissance art
- Modern design aesthetics

**Finance:**
- Fibonacci retracements in technical analysis
- Elliott wave theory
- Market timing strategies

### 9.3 Problem-Solving Checklist

**When you see a recurrence:**
1. ☐ Identify if it's linear and homogeneous
2. ☐ Write the characteristic equation
3. ☐ Solve for roots using quadratic formula
4. ☐ Write general solution: a_n = A·r₁ⁿ + B·r₂ⁿ
5. ☐ Use initial conditions to find A and B
6. ☐ Verify with small values

**When you see φ or golden ratio:**
1. ☐ Remember φ² = φ + 1
2. ☐ Use φ = (1 + √5)/2 for exact calculations
3. ☐ Use φ ≈ 1.618 for approximations
4. ☐ Don't forget the conjugate φ̂ in formulas

**When verifying an equation:**
1. ☐ Compute left side completely
2. ☐ Compute right side completely
3. ☐ Simplify both sides
4. ☐ Show they're equal

---

## 10. Summary: The Big Picture

### The Story So Far

1. **Fibonacci sequence** is defined by F_n = F_(n-1) + F_(n-2)
2. **To find a formula**, we assume F_n = xⁿ
3. **This gives** x² = x + 1 (characteristic equation)
4. **Solving gives** two roots: φ and φ̂
5. **General solution** is F_n = A·φⁿ + B·φ̂ⁿ
6. **Using initial conditions** gives Binet's formula
7. **For large n**, φ̂ⁿ vanishes, so F_n ≈ φⁿ/√5

### Key Equations to Remember

```
φ = (1 + √5) / 2 ≈ 1.618
φ̂ = (1 - √5) / 2 ≈ -0.618
φ² = φ + 1
φ + φ̂ = 1
φ · φ̂ = -1
F_n = (φⁿ - φ̂ⁿ) / √5
```

### The Power of This Approach

**Instead of computing:**
```
F_100 = F_99 + F_98 = (F_98 + F_97) + F_98 = ...
```

**We can directly compute:**
```
F_100 = (φ¹⁰⁰ - φ̂¹⁰⁰) / √5
```

This is the power of closed-form solutions!

---

## Practice Problems

### Problem 1: Verify the Formula
Show that φ³ = 2φ + 1 using φ² = φ + 1.

### Problem 2: Compute Fibonacci
Use Binet's formula to compute F_6. Verify it matches the recurrence.

### Problem 3: New Recurrence
Solve G_n = 3G_(n-1) - 2G_(n-2) with G_0 = 1, G_1 = 2.

### Problem 4: Ratio Limit
Prove that lim(n→∞) F_n/F_(n-1) = φ using Binet's formula.

---

**You now have everything you need to understand Fibonacci, φ, and related problems from first principles!**
