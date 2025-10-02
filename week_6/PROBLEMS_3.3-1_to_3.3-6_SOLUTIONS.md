# Chapter 3.3 Problems: Complete Solutions Guide

**Problems:** 3.3-1 through 3.3-6  
**Focus:** Asymptotic notation, function growth, and comparisons

---

## Problem 3.3-1: Monotonicity Properties

### Problem Statement
Show that if f(n) and g(n) are monotonically increasing functions, then:
1. f(n) + g(n) is monotonically increasing
2. f(g(n)) is monotonically increasing
3. If f(n) and g(n) are nonnegative, then f(n) · g(n) is monotonically increasing

---

### Part 1: Sum of Monotonic Functions

**Claim:** If f(n) and g(n) are monotonically increasing, then h(n) = f(n) + g(n) is monotonically increasing.

**Proof:**

**Given:**
- f(n) is monotonically increasing: n₁ ≤ n₂ ⟹ f(n₁) ≤ f(n₂)
- g(n) is monotonically increasing: n₁ ≤ n₂ ⟹ g(n₁) ≤ g(n₂)

**To prove:** n₁ ≤ n₂ ⟹ h(n₁) ≤ h(n₂)

**Proof steps:**

Let n₁ ≤ n₂ be arbitrary.

Since f is monotonically increasing:
```
f(n₁) ≤ f(n₂)     ... (1)
```

Since g is monotonically increasing:
```
g(n₁) ≤ g(n₂)     ... (2)
```

Add inequalities (1) and (2):
```
f(n₁) + g(n₁) ≤ f(n₂) + g(n₂)
```

By definition of h:
```
h(n₁) ≤ h(n₂)
```

**Conclusion:** h(n) = f(n) + g(n) is monotonically increasing. ✓

**Key insight:** Addition preserves monotonicity because adding two non-decreasing sequences gives a non-decreasing sequence.

---

### Part 2: Composition of Monotonic Functions

**Claim:** If f(n) and g(n) are monotonically increasing, then h(n) = f(g(n)) is monotonically increasing.

**Proof:**

**Given:**
- f(n) is monotonically increasing: x₁ ≤ x₂ ⟹ f(x₁) ≤ f(x₂)
- g(n) is monotonically increasing: n₁ ≤ n₂ ⟹ g(n₁) ≤ g(n₂)

**To prove:** n₁ ≤ n₂ ⟹ h(n₁) ≤ h(n₂)

**Proof steps:**

Let n₁ ≤ n₂ be arbitrary.

Since g is monotonically increasing:
```
g(n₁) ≤ g(n₂)     ... (1)
```

Let x₁ = g(n₁) and x₂ = g(n₂).

From (1), we have x₁ ≤ x₂.

Since f is monotonically increasing and x₁ ≤ x₂:
```
f(x₁) ≤ f(x₂)
```

Substituting back:
```
f(g(n₁)) ≤ f(g(n₂))
```

By definition of h:
```
h(n₁) ≤ h(n₂)
```

**Conclusion:** h(n) = f(g(n)) is monotonically increasing. ✓

**Key insight:** Composition preserves monotonicity through the chain: n₁ ≤ n₂ ⟹ g(n₁) ≤ g(n₂) ⟹ f(g(n₁)) ≤ f(g(n₂))

**Visual intuition:**
```
n₁ ≤ n₂
  ↓ (apply g, which is increasing)
g(n₁) ≤ g(n₂)
  ↓ (apply f, which is increasing)
f(g(n₁)) ≤ f(g(n₂))
```

---

### Part 3: Product of Nonnegative Monotonic Functions

**Claim:** If f(n) and g(n) are nonnegative and monotonically increasing, then h(n) = f(n) · g(n) is monotonically increasing.

**Proof:**

**Given:**
- f(n) is nonnegative and monotonically increasing
- g(n) is nonnegative and monotonically increasing

**To prove:** n₁ ≤ n₂ ⟹ h(n₁) ≤ h(n₂)

**Proof steps:**

Let n₁ ≤ n₂ be arbitrary.

Since f and g are monotonically increasing:
```
f(n₁) ≤ f(n₂)     ... (1)
g(n₁) ≤ g(n₂)     ... (2)
```

Since f and g are nonnegative:
```
f(n₁) ≥ 0, f(n₂) ≥ 0, g(n₁) ≥ 0, g(n₂) ≥ 0
```

Multiply inequality (1) by g(n₁) ≥ 0:
```
f(n₁) · g(n₁) ≤ f(n₂) · g(n₁)     ... (3)
```

Multiply inequality (2) by f(n₂) ≥ 0:
```
f(n₂) · g(n₁) ≤ f(n₂) · g(n₂)     ... (4)
```

Combine (3) and (4) by transitivity:
```
f(n₁) · g(n₁) ≤ f(n₂) · g(n₂)
```

By definition of h:
```
h(n₁) ≤ h(n₂)
```

**Conclusion:** h(n) = f(n) · g(n) is monotonically increasing. ✓

**Why nonnegativity matters:**
- Multiplying an inequality by a negative number reverses the inequality
- Nonnegativity ensures we can multiply without reversing
- Example: If f(n) = -n (negative), then f(n)² = n² is NOT monotonically increasing for all n

**Key insight:** Products preserve monotonicity only when both functions are nonnegative.

---

## Problem 3.3-2: Floor and Ceiling Identity

### Problem Statement
Prove that ⌊αn⌋ + ⌈(1-α)n⌉ = n for any integer n and real number α in the range 0 ≤ α ≤ 1.

---

### Solution

**Definitions:**
- Floor: ⌊x⌋ = largest integer ≤ x
- Ceiling: ⌈x⌉ = smallest integer ≥ x

**Key property:**
For any real number x:
```
⌊x⌋ + ⌈-x⌉ = 0  if x is an integer
⌊x⌋ + ⌈-x⌉ = 0  if x is not an integer (fractional parts cancel)
```

**Proof:**

Let n be an integer and 0 ≤ α ≤ 1.

**Step 1: Rewrite the ceiling term**
```
⌈(1-α)n⌉ = ⌈n - αn⌉
```

**Step 2: Use the property ⌈x⌉ = -⌊-x⌋**
```
⌈n - αn⌉ = -⌊-(n - αn)⌋ = -⌊αn - n⌋
```

**Step 3: Apply the identity ⌊x + k⌋ = ⌊x⌋ + k for integer k**

Since n is an integer:
```
⌊αn - n⌋ = ⌊αn⌋ - n
```

**Step 4: Substitute back**
```
⌈(1-α)n⌉ = -⌊αn⌋ + n
```

**Step 5: Compute the sum**
```
⌊αn⌋ + ⌈(1-α)n⌉ = ⌊αn⌋ + (-⌊αn⌋ + n)
                  = n
```

**Conclusion:** ⌊αn⌋ + ⌈(1-α)n⌉ = n for all integers n and 0 ≤ α ≤ 1. ✓

---

### Alternative Proof (More Intuitive)

**Idea:** The fractional parts of αn and (1-α)n sum to 0 or 1.

Let αn = ⌊αn⌋ + {αn} where {αn} is the fractional part.

**Case 1: {αn} = 0 (αn is an integer)**
```
⌊αn⌋ = αn
⌈(1-α)n⌉ = ⌈n - αn⌉ = n - αn  (since n - αn is also an integer)
Sum = αn + (n - αn) = n ✓
```

**Case 2: {αn} > 0 (αn is not an integer)**
```
⌊αn⌋ = αn - {αn}
(1-α)n = n - αn = n - ⌊αn⌋ - {αn}

⌈(1-α)n⌉ = ⌈n - ⌊αn⌋ - {αn}⌉
         = n - ⌊αn⌋ + ⌈-{αn}⌉
         = n - ⌊αn⌋ + 0  (since 0 < {αn} < 1, so ⌈-{αn}⌉ = 0)
         = n - ⌊αn⌋

Sum = ⌊αn⌋ + (n - ⌊αn⌋) = n ✓
```

**Key insight:** The floor and ceiling operations ensure that the fractional parts are handled correctly, always summing to n.

---

### Example Verification

**Example 1: α = 0.5, n = 10**
```
⌊0.5 · 10⌋ + ⌈0.5 · 10⌉ = ⌊5⌋ + ⌈5⌉ = 5 + 5 = 10 ✓
```

**Example 2: α = 0.3, n = 10**
```
⌊0.3 · 10⌋ + ⌈0.7 · 10⌉ = ⌊3⌋ + ⌈7⌉ = 3 + 7 = 10 ✓
```

**Example 3: α = 0.4, n = 7**
```
⌊0.4 · 7⌋ + ⌈0.6 · 7⌉ = ⌊2.8⌋ + ⌈4.2⌉ = 2 + 5 = 7 ✓
```

**Example 4: α = 0.25, n = 9**
```
⌊0.25 · 9⌋ + ⌈0.75 · 9⌉ = ⌊2.25⌋ + ⌈6.75⌉ = 2 + 7 = 9 ✓
```

---

## Problem 3.3-3: Polynomial with Little-o

### Problem Statement
Use equation (3.14) or other means to show that (n + o(n))^k = Θ(n^k) for any real constant k. Conclude that ⌊n⌋^k = Θ(n^k) and ⌈n⌉^k = Θ(n^k).

---

### Part 1: Main Result

**Claim:** (n + o(n))^k = Θ(n^k) for any real constant k.

**Proof:**

**Step 1: Understand o(n)**

By definition, f(n) = o(n) means:
```
lim(n→∞) f(n)/n = 0
```

This means for any ε > 0, there exists n₀ such that for all n ≥ n₀:
```
|f(n)| < ε·n
```

**Step 2: Factor out n**

Let f(n) = o(n). Then:
```
(n + f(n))^k = n^k · (1 + f(n)/n)^k
```

**Step 3: Analyze (1 + f(n)/n)^k**

Since f(n)/n → 0 as n → ∞, we have:
```
(1 + f(n)/n)^k → 1^k = 1 as n → ∞
```

More precisely, for large n:
```
(1 + f(n)/n)^k = 1 + k·f(n)/n + O((f(n)/n)²)
                = 1 + o(1)
```

**Step 4: Establish bounds**

For sufficiently large n, we can bound (1 + f(n)/n)^k:

Choose ε = 1/2. Then for n ≥ n₀:
```
|f(n)/n| < 1/2
```

So:
```
1/2 < 1 + f(n)/n < 3/2
```

Raising to power k (assuming k > 0):
```
(1/2)^k < (1 + f(n)/n)^k < (3/2)^k
```

**Step 5: Apply to (n + f(n))^k**
```
(1/2)^k · n^k < (n + f(n))^k < (3/2)^k · n^k
```

Let c₁ = (1/2)^k and c₂ = (3/2)^k. Then:
```
c₁ · n^k ≤ (n + f(n))^k ≤ c₂ · n^k for all n ≥ n₀
```

**Conclusion:** (n + o(n))^k = Θ(n^k). ✓

**Key insight:** The o(n) term is negligible compared to n, so it doesn't affect the asymptotic growth rate.

---

### Part 2: Floor Function

**Claim:** ⌊n⌋^k = Θ(n^k)

**Proof:**

**Step 1: Bound the floor function**

For any real n:
```
n - 1 < ⌊n⌋ ≤ n
```

**Step 2: Raise to power k**

Assuming k > 0:
```
(n - 1)^k < ⌊n⌋^k ≤ n^k
```

**Step 3: Analyze (n - 1)^k**
```
(n - 1)^k = n^k · (1 - 1/n)^k
          = n^k · (1 - k/n + O(1/n²))
          = n^k · (1 + o(1))
```

For large n:
```
(n - 1)^k ≥ (1/2) · n^k  (for sufficiently large n)
```

**Step 4: Establish Θ bound**
```
(1/2) · n^k ≤ ⌊n⌋^k ≤ n^k
```

**Conclusion:** ⌊n⌋^k = Θ(n^k). ✓

**Alternative approach using Part 1:**
```
⌊n⌋ = n - {n}  where 0 ≤ {n} < 1
```

Since {n} = O(1) = o(n):
```
⌊n⌋ = n + o(n)
```

By Part 1:
```
⌊n⌋^k = (n + o(n))^k = Θ(n^k) ✓
```

---

### Part 3: Ceiling Function

**Claim:** ⌈n⌉^k = Θ(n^k)

**Proof:**

**Step 1: Bound the ceiling function**

For any real n:
```
n ≤ ⌈n⌉ < n + 1
```

**Step 2: Raise to power k**

Assuming k > 0:
```
n^k ≤ ⌈n⌉^k < (n + 1)^k
```

**Step 3: Analyze (n + 1)^k**
```
(n + 1)^k = n^k · (1 + 1/n)^k
          = n^k · (1 + k/n + O(1/n²))
          = n^k · (1 + o(1))
```

For large n:
```
(n + 1)^k ≤ 2 · n^k  (for sufficiently large n)
```

**Step 4: Establish Θ bound**
```
n^k ≤ ⌈n⌉^k ≤ 2 · n^k
```

**Conclusion:** ⌈n⌉^k = Θ(n^k). ✓

**Alternative approach using Part 1:**
```
⌈n⌉ = n + (1 - {n})  where 0 < 1 - {n} ≤ 1
```

Since 1 - {n} = O(1) = o(n):
```
⌈n⌉ = n + o(n)
```

By Part 1:
```
⌈n⌉^k = (n + o(n))^k = Θ(n^k) ✓
```

---

### Summary

**Main results:**
1. (n + o(n))^k = Θ(n^k) - lower-order terms don't matter
2. ⌊n⌋^k = Θ(n^k) - floor doesn't change asymptotic growth
3. ⌈n⌉^k = Θ(n^k) - ceiling doesn't change asymptotic growth

**Key insight:** Asymptotic notation ignores constant additive terms (like ±1) and lower-order terms (like o(n)).

---

## Problem 3.3-4: Prove Specific Equations

### Problem Statement
Prove the following:
- **a.** Equation (3.21)
- **b.** Equations (3.26)-(3.28)
- **c.** lg(Θ(n)) = Θ(lg n)

---

### Part a: Equation (3.21) - Stirling's Approximation

**Equation (3.21):**
```
n! = √(2πn) · (n/e)^n · (1 + Θ(1/n))
```

**Note:** This is Stirling's approximation. A full proof requires advanced calculus (Euler-Maclaurin formula). Here's the outline:

**Proof sketch:**

**Step 1: Take logarithms**
```
ln(n!) = ln(1) + ln(2) + ... + ln(n)
       = Σᵢ₌₁ⁿ ln(i)
```

**Step 2: Approximate sum with integral**
```
Σᵢ₌₁ⁿ ln(i) ≈ ∫₁ⁿ ln(x) dx
```

**Step 3: Evaluate integral**
```
∫₁ⁿ ln(x) dx = [x ln(x) - x]₁ⁿ
             = n ln(n) - n - (0 - 1)
             = n ln(n) - n + 1
```

**Step 4: Refine with Euler-Maclaurin**

Using the Euler-Maclaurin formula to correct the approximation:
```
ln(n!) = n ln(n) - n + (1/2)ln(n) + (1/2)ln(2π) + O(1/n)
```

**Step 5: Exponentiate**
```
n! = exp(n ln(n) - n + (1/2)ln(n) + (1/2)ln(2π) + O(1/n))
   = e^(n ln n) · e^(-n) · e^((1/2)ln n) · e^((1/2)ln(2π)) · e^(O(1/n))
   = n^n · e^(-n) · √n · √(2π) · (1 + O(1/n))
   = √(2πn) · (n/e)^n · (1 + Θ(1/n))
```

**Conclusion:** Equation (3.21) is proven (with advanced calculus). ✓

**For exam purposes:** You can cite Stirling's approximation as a known result.

---

### Part b: Equations (3.26)-(3.28)

**Equation (3.26): lg(n!) = Θ(n lg n)**

**Proof:**

**Upper bound (O):**

Using Stirling's approximation:
```
n! ≤ √(2πn) · (n/e)^n · 2  (for large n)
```

Taking logarithms:
```
lg(n!) ≤ lg(√(2πn)) + lg((n/e)^n) + lg(2)
       = (1/2)lg(2πn) + n lg(n/e) + 1
       = (1/2)lg(2π) + (1/2)lg(n) + n lg n - n lg e + 1
       = O(n lg n)  [since (1/2)lg n and constants are absorbed]
```

**Lower bound (Ω):**

For n ≥ 2:
```
n! = 1 · 2 · 3 · ... · n
   ≥ (n/2)^(n/2)  [at least half the terms are ≥ n/2]
```

Taking logarithms:
```
lg(n!) ≥ lg((n/2)^(n/2))
       = (n/2) · lg(n/2)
       = (n/2) · (lg n - 1)
       = (n/2) lg n - n/2
       = Ω(n lg n)
```

**Conclusion:** lg(n!) = Θ(n lg n). ✓

---

**Equation (3.27): n! = o(n^n)**

**Proof:**

We need to show:
```
lim(n→∞) n! / n^n = 0
```

**Step 1: Write out the ratio**
```
n! / n^n = (1 · 2 · 3 · ... · n) / (n · n · n · ... · n)
         = (1/n) · (2/n) · (3/n) · ... · (n/n)
```

**Step 2: Bound the product**

Each term i/n ≤ 1, and at least half the terms satisfy i/n ≤ 1/2:
```
n! / n^n ≤ (1/2)^(n/2) · 1^(n/2)
         = (1/2)^(n/2)
         → 0 as n → ∞
```

**Conclusion:** n! = o(n^n). ✓

**Intuition:** n! = n · (n-1) · ... · 1, while n^n = n · n · ... · n. The factorial has many small terms, so it grows slower.

---

**Equation (3.28): n! = ω(2^n)**

**Proof:**

We need to show:
```
lim(n→∞) n! / 2^n = ∞
```

**Step 1: Write out the ratio**
```
n! / 2^n = (1 · 2 · 3 · ... · n) / 2^n
         = (1/2) · (2/2) · (3/2) · ... · (n/2)
```

**Step 2: Bound the product**

For n ≥ 4, at least half the terms satisfy i/2 ≥ 2:
```
n! / 2^n ≥ (1/2) · 1 · 2 · 2 · ... · 2  [n/2 terms ≥ 2]
         ≥ (1/2) · 2^(n/2)
         = 2^(n/2 - 1)
         → ∞ as n → ∞
```

**Conclusion:** n! = ω(2^n). ✓

**Intuition:** Factorial grows faster than exponential because the multipliers keep increasing.

---

### Part c: lg(Θ(n)) = Θ(lg n)

**Claim:** lg(Θ(n)) = Θ(lg n)

**Proof:**

**Step 1: Understand the notation**

Let f(n) ∈ Θ(n). By definition:
```
∃c₁, c₂, n₀: c₁n ≤ f(n) ≤ c₂n for all n ≥ n₀
```

**Step 2: Take logarithms**

Since logarithm is monotonically increasing:
```
lg(c₁n) ≤ lg(f(n)) ≤ lg(c₂n)
```

**Step 3: Expand using log properties**
```
lg c₁ + lg n ≤ lg(f(n)) ≤ lg c₂ + lg n
```

**Step 4: Establish Θ bound**

For large n, the constants lg c₁ and lg c₂ become negligible:
```
lg c₁ + lg n = lg n + O(1) = Θ(lg n)
lg c₂ + lg n = lg n + O(1) = Θ(lg n)
```

Therefore:
```
lg(f(n)) = Θ(lg n)
```

**Conclusion:** lg(Θ(n)) = Θ(lg n). ✓

**Key insight:** Logarithms preserve asymptotic relationships, with constants absorbed.

---

## Problem 3.3-5: Polynomial Bounding

### Problem Statement
Is the function ⌊lg n⌋! polynomially bounded? Is the function ⌊lg lg n⌋! polynomially bounded?

---

### Definition: Polynomially Bounded

A function f(n) is **polynomially bounded** if:
```
∃k, c, n₀: f(n) ≤ c · n^k for all n ≥ n₀
```

In other words: f(n) = O(n^k) for some constant k.

---

### Part 1: Is ⌊lg n⌋! polynomially bounded?

**Answer: NO**

**Proof:**

**Step 1: Estimate ⌊lg n⌋!**

Let m = ⌊lg n⌋. Then:
```
m! = 1 · 2 · 3 · ... · m
```

**Step 2: Use Stirling's approximation**
```
m! ≈ √(2πm) · (m/e)^m
```

**Step 3: Substitute m = lg n**
```
(lg n)! ≈ √(2π lg n) · (lg n / e)^(lg n)
        = √(2π lg n) · (lg n)^(lg n) / e^(lg n)
```

**Step 4: Simplify e^(lg n)**
```
e^(lg n) = e^(log₂ n / log₂ e)
         = (e^(log₂ n))^(1/log₂ e)
         = n^(1/log₂ e)
         = n^(log_e 2)
         ≈ n^0.693
```

**Step 5: Analyze (lg n)^(lg n)**

This is the key term. We can write:
```
(lg n)^(lg n) = 2^(lg n · lg lg n)
```

**Step 6: Compare to polynomials**

For f(n) to be polynomially bounded, we need:
```
2^(lg n · lg lg n) ≤ c · n^k
```

Taking logarithms:
```
lg n · lg lg n ≤ lg c + k lg n
```

Dividing by lg n:
```
lg lg n ≤ (lg c / lg n) + k
```

As n → ∞, lg lg n → ∞, but the right side approaches k (a constant).

This is a contradiction!

**Conclusion:** ⌊lg n⌋! is NOT polynomially bounded. ✓

**Intuition:** Even though lg n grows slowly, its factorial grows superpolynomially.

---

### Part 2: Is ⌊lg lg n⌋! polynomially bounded?

**Answer: YES**

**Proof:**

**Step 1: Bound ⌊lg lg n⌋**

For any n:
```
⌊lg lg n⌋ ≤ lg lg n
```

**Step 2: Observe that lg lg n grows very slowly**

For practical values:
- n = 2^16 = 65536 ⟹ lg lg n = lg 16 = 4
- n = 2^256 ⟹ lg lg n = lg 256 = 8
- n = 2^65536 ⟹ lg lg n = lg 65536 = 16

**Step 3: Bound the factorial**

Let m = ⌊lg lg n⌋. Then:
```
m! ≤ m^m  [standard bound]
```

**Step 4: Substitute m = lg lg n**
```
(lg lg n)! ≤ (lg lg n)^(lg lg n)
```

**Step 5: Show this is polynomially bounded**

We need to find k such that:
```
(lg lg n)^(lg lg n) ≤ n^k
```

Taking logarithms:
```
(lg lg n) · lg(lg lg n) ≤ k lg n
```

Rearranging:
```
k ≥ (lg lg n · lg(lg lg n)) / lg n
```

**Step 6: Analyze the right side**

As n → ∞:
```
(lg lg n · lg(lg lg n)) / lg n → 0
```

Because:
- Numerator: lg lg n · lg(lg lg n) = o(lg n)
- Denominator: lg n

So for any k > 0 (say k = 1), the inequality holds for sufficiently large n.

**Conclusion:** ⌊lg lg n⌋! is polynomially bounded. ✓

**Specifically:** ⌊lg lg n⌋! = O(n) (or even O(√n) or O(lg n) for very large n).

**Intuition:** lg lg n grows so slowly that its factorial is essentially constant for practical purposes.

---

### Summary

| Function | Polynomially Bounded? | Reason |
|----------|----------------------|--------|
| ⌊lg n⌋! | NO | Grows like 2^(lg n · lg lg n), superpolynomial |
| ⌊lg lg n⌋! | YES | lg lg n is so small that its factorial is bounded |

**Key insight:** The iterated logarithm lg lg n grows so slowly that even its factorial remains polynomially bounded.

---

## Problem 3.3-6: Comparing Iterated Functions

### Problem Statement
Which is asymptotically larger: lg(lg* n) or lg*(lg n)?

---

### Definitions

**Iterated logarithm (lg*):**
```
lg* n = min{i ≥ 0 : lg^(i) n ≤ 1}
```

Where lg^(i) means applying lg i times.

**Examples:**
```
lg* 2 = 1     (lg 2 = 1)
lg* 4 = 2     (lg lg 4 = lg 2 = 1)
lg* 16 = 3    (lg lg lg 16 = lg lg 4 = lg 2 = 1)
lg* 65536 = 5 (lg^5 65536 = 1)
```

---

### Solution

**Answer: lg*(lg n) is asymptotically larger**

**Proof:**

**Step 1: Compute concrete values**

Let's compute for n = 2^16 = 65536:

```
lg n = 16
lg* n = 5  (because lg^5 65536 = 1)

lg(lg* n) = lg 5 ≈ 2.32

lg*(lg n) = lg* 16 = 4  (because lg^4 16 = 1)
```

So for this n: lg*(lg n) > lg(lg* n).

**Step 2: Analyze asymptotic behavior**

As n → ∞:

**For lg(lg* n):**
- lg* n grows to infinity (but very slowly)
- lg(lg* n) also grows to infinity
- But lg(lg* n) grows like lg(lg* n), which is very slow

**For lg*(lg n):**
- lg n grows to infinity
- lg*(lg n) is the iterated log of lg n
- We have: lg*(lg n) ≈ lg* n - 1

**Step 3: Compare growth rates**

For large n:
```
lg*(lg n) ≈ lg* n - 1
lg(lg* n) = lg(lg* n)
```

Since lg* n → ∞, we need to compare:
```
lg* n - 1  vs.  lg(lg* n)
```

Let m = lg* n. Then we're comparing:
```
m - 1  vs.  lg m
```

For m ≥ 4, we have m - 1 > lg m.

**Step 4: Formal limit**
```
lim(n→∞) lg(lg* n) / lg*(lg n) = lim(m→∞) lg m / (m - 1) = 0
```

**Conclusion:** lg*(lg n) is asymptotically larger than lg(lg* n). ✓

**In asymptotic notation:**
```
lg(lg* n) = o(lg*(lg n))
```

---

### Intuition

**Why lg*(lg n) is larger:**

1. **Iteration vs. Composition:**
   - lg*(lg n) applies lg* to a smaller starting point (lg n instead of n)
   - But lg* is an iteration count, which grows faster than a single log application

2. **Approximate relationship:**
   ```
   lg*(lg n) ≈ lg* n - 1
   ```
   This is because applying lg once reduces the iteration count by about 1.

3. **Concrete example:**
   ```
   n = 2^65536
   lg n = 65536
   lg* n = 6
   
   lg(lg* n) = lg 6 ≈ 2.58
   lg*(lg n) = lg* 65536 = 5
   ```

**Visual representation:**
```
Function         | n = 2^16 | n = 2^256 | n = 2^65536
-----------------|----------|-----------|-------------
lg* n            |    5     |     6     |      7
lg(lg* n)        |   2.32   |    2.58   |     2.81
lg*(lg n)        |    4     |     5     |      6
```

**Key insight:** Iteration (lg*) grows faster than composition (lg of lg*) because iteration counts steps, while composition applies a single operation.

---

## Summary: Problem-Solving Patterns

### Pattern 1: Monotonicity Proofs
1. Write down the definition
2. Consider arbitrary n₁ ≤ n₂
3. Use algebra to show f(n₁) ≤ f(n₂)
4. Be careful with products (need nonnegativity)

### Pattern 2: Floor/Ceiling Identities
1. Use properties: ⌊x⌋ + ⌈y⌉ = ⌊x+y⌋ or ⌊x+y⌋ + 1
2. Analyze fractional parts
3. Verify with concrete examples

### Pattern 3: Asymptotic Notation with Polynomials
1. Factor out dominant terms
2. Show lower-order terms are negligible
3. Establish upper and lower bounds

### Pattern 4: Proving Textbook Equations
1. Look up the equation
2. Use definitions of Θ, O, Ω
3. Apply Stirling's approximation for factorials
4. Use logarithm properties

### Pattern 5: Polynomial Bounding
1. Understand the definition: f(n) = O(n^k) for some k
2. Estimate growth rate (Stirling's for factorials)
3. Compare to polynomial growth
4. Use limits if needed

### Pattern 6: Comparing Iterated Functions
1. Compute concrete values for intuition
2. Analyze asymptotic behavior
3. Use limits: lim f(n)/g(n)
4. Remember: iteration grows faster than composition

---

## Quick Reference: Key Facts

### Asymptotic Notation
- Θ: tight bound (sandwiched)
- O: upper bound
- Ω: lower bound
- o: strict upper bound (limit = 0)
- ω: strict lower bound (limit = ∞)

### Growth Hierarchy
```
1 < lg lg n < lg n < √n < n < n lg n < n² < 2ⁿ < n! < nⁿ
```

### Factorial Bounds
```
lg(n!) = Θ(n lg n)
n! = o(nⁿ)
n! = ω(2ⁿ)
```

### Logarithm Properties
```
lg(ab) = lg a + lg b
lg(a/b) = lg a - lg b
lg(aᵇ) = b lg a
```

### Iterated Logarithm
```
lg* n = number of times to apply lg to reach ≤ 1
lg* n grows VERY slowly
lg*(lg n) ≈ lg* n - 1
```

---

**End of Solutions**
