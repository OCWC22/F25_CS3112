# Chapter 3.2 Problems: Complete Step-by-Step Solutions

**Problems:** 3.2-1 through 3.2-7  
**Focus:** Asymptotic notation definitions and proofs

---

## Problem 3.2-1: Prove max{f(n), g(n)} = Θ(f(n) + g(n))

### Problem Statement
Let f(n) and g(n) be asymptotically nonnegative functions. Using the basic definition of Θ-notation, prove that max{f(n), g(n)} = Θ(f(n) + g(n)).

---

### Understanding the Problem

**What we're proving:**
The maximum of two functions grows at the same rate as their sum.

**Why this matters:**
- When analyzing algorithms with multiple phases, the slowest phase dominates
- Shows that max and sum are asymptotically equivalent
- Useful for analyzing parallel algorithms

**Intuition:**
- The max is at least half the sum (one function is at least half)
- The max is at most the full sum (can't exceed both functions combined)

---

### Solution

**Claim:** max{f(n), g(n)} = Θ(f(n) + g(n))

**Proof:**

Let h(n) = max{f(n), g(n)}.

To prove h(n) = Θ(f(n) + g(n)), we must show:
1. h(n) = O(f(n) + g(n))  [upper bound]
2. h(n) = Ω(f(n) + g(n))  [lower bound]

---

### Part 1: Upper Bound (h(n) = O(f(n) + g(n)))

**Goal:** Show ∃c, n₀: h(n) ≤ c·(f(n) + g(n)) for all n ≥ n₀

**Proof:**

For any n, by definition of max:
```
h(n) = max{f(n), g(n)}
```

**Case 1:** If f(n) ≥ g(n), then h(n) = f(n)
```
h(n) = f(n) ≤ f(n) + g(n)  [since g(n) ≥ 0]
```

**Case 2:** If g(n) ≥ f(n), then h(n) = g(n)
```
h(n) = g(n) ≤ f(n) + g(n)  [since f(n) ≥ 0]
```

In both cases:
```
h(n) ≤ f(n) + g(n)
```

Therefore, with c = 1 and n₀ = 1:
```
h(n) ≤ 1·(f(n) + g(n)) for all n ≥ 1
```

**Conclusion:** h(n) = O(f(n) + g(n)) ✓

---

### Part 2: Lower Bound (h(n) = Ω(f(n) + g(n)))

**Goal:** Show ∃c, n₀: h(n) ≥ c·(f(n) + g(n)) for all n ≥ n₀

**Proof:**

By definition of max:
```
h(n) = max{f(n), g(n)} ≥ f(n)  [max is at least f]
h(n) = max{f(n), g(n)} ≥ g(n)  [max is at least g]
```

Adding these two inequalities:
```
h(n) + h(n) ≥ f(n) + g(n)
2·h(n) ≥ f(n) + g(n)
h(n) ≥ (1/2)·(f(n) + g(n))
```

Therefore, with c = 1/2 and n₀ = 1:
```
h(n) ≥ (1/2)·(f(n) + g(n)) for all n ≥ 1
```

**Conclusion:** h(n) = Ω(f(n) + g(n)) ✓

---

### Part 3: Combining Results

Since we have shown:
- h(n) = O(f(n) + g(n))  [upper bound]
- h(n) = Ω(f(n) + g(n))  [lower bound]

By the definition of Θ-notation:
```
h(n) = Θ(f(n) + g(n))
```

**Therefore:**
```
max{f(n), g(n)} = Θ(f(n) + g(n)) ✓
```

---

### Verification with Examples

**Example 1:** f(n) = n, g(n) = n²
```
max{n, n²} = n² for n ≥ 1
f(n) + g(n) = n + n² = Θ(n²)

Is max = Θ(sum)?
max = n² = Θ(n²) ✓
sum = n + n² = Θ(n²) ✓
Yes! ✓
```

**Example 2:** f(n) = 2n, g(n) = 3n
```
max{2n, 3n} = 3n
f(n) + g(n) = 2n + 3n = 5n = Θ(n)

Is max = Θ(sum)?
max = 3n = Θ(n) ✓
sum = 5n = Θ(n) ✓
Yes! ✓
```

**Example 3:** f(n) = n lg n, g(n) = n
```
max{n lg n, n} = n lg n for n ≥ 2
f(n) + g(n) = n lg n + n = Θ(n lg n)

Is max = Θ(sum)?
max = n lg n = Θ(n lg n) ✓
sum = n lg n + n = Θ(n lg n) ✓
Yes! ✓
```

---

### Key Insights

1. **The max is sandwiched:**
   ```
   (1/2)(f + g) ≤ max{f, g} ≤ (f + g)
   ```

2. **Why (1/2)?**
   - At least one of f or g is ≥ (f+g)/2
   - The max picks the larger one
   - So max ≥ (f+g)/2

3. **Practical meaning:**
   - When combining two algorithms, the slower one dominates
   - The total time is proportional to the slower algorithm
   - Example: O(n) + O(n²) = O(n²)

4. **Generalization:**
   ```
   max{f₁, f₂, ..., fₖ} = Θ(f₁ + f₂ + ... + fₖ)
   ```
   (when all functions are asymptotically nonnegative)

---

## Problem 3.2-2: Why "at least O(n²)" is meaningless

### Problem Statement
Explain why the statement, "The running time of algorithm A is at least O(n²)," is meaningless.

---

### Understanding the Problem

**What we're analyzing:**
A statement that mixes "at least" (lower bound language) with O-notation (upper bound notation).

**Why this matters:**
- Common mistake in algorithm analysis
- Shows importance of precise mathematical language
- Helps avoid confusion in technical communication

---

### Solution

**The statement:** "The running time of algorithm A is at least O(n²)"

**Why it's meaningless:**

---

### Step 1: Understand O-notation

**Definition of O(n²):**
```
T(n) = O(n²) means:
∃c, n₀ > 0: T(n) ≤ c·n² for all n ≥ n₀
```

**In plain English:**
"The running time grows **no faster than** n²"

**O-notation gives an UPPER BOUND (≤)**

---

### Step 2: Understand "at least"

**"At least" means:**
- Greater than or equal to (≥)
- A LOWER BOUND
- Minimum value

**Examples:**
- "At least 5" means ≥ 5
- "At least 100 mph" means ≥ 100 mph

---

### Step 3: Identify the Contradiction

**The statement says:**
```
"The running time is at least [no faster than n²]"
```

**This is like saying:**
```
"The speed is at least [at most 60 mph]"
```

**Or:**
```
"The temperature is at least [no more than 32°F]"
```

**These are MEANINGLESS!**

---

### Step 4: Why It's Logically Inconsistent

**Breaking it down:**

1. O(n²) is a **set** of functions
2. O(n²) contains ALL functions that grow no faster than n²
3. This includes: O(1), O(n), O(n²), O(n^1.5), etc.

**The statement claims:**
```
T(n) is at least [something in O(n²)]
```

**But O(n²) includes O(1)!**

So the statement could mean:
```
"T(n) is at least O(1)"
```

Which means:
```
"T(n) is at least [bounded by a constant]"
```

**This tells us NOTHING useful!**

Every function is "at least O(1)" in this (meaningless) interpretation.

---

### Step 5: What They Probably Meant

**Correct alternatives:**

**Option 1:** Use Ω for lower bounds
```
✓ "The running time is at least Ω(n²)"
  Meaning: T(n) ≥ c·n² for some c, n₀
```

**Option 2:** Use "at most" with O
```
✓ "The running time is at most O(n²)"
  Meaning: T(n) ≤ c·n² for some c, n₀
```

**Option 3:** Use Θ for tight bounds
```
✓ "The running time is Θ(n²)"
  Meaning: c₁·n² ≤ T(n) ≤ c₂·n² for some c₁, c₂, n₀
```

**Option 4:** Just use O correctly
```
✓ "The running time is O(n²)"
  Meaning: T(n) ≤ c·n² for some c, n₀
```

---

### Summary Table

| Statement | Meaning | Valid? |
|-----------|---------|--------|
| "T(n) is O(n²)" | T(n) ≤ c·n² | ✓ Valid |
| "T(n) is at most O(n²)" | T(n) ≤ c·n² | ✓ Valid (redundant) |
| "T(n) is Ω(n²)" | T(n) ≥ c·n² | ✓ Valid |
| "T(n) is at least Ω(n²)" | T(n) ≥ c·n² | ✓ Valid (redundant) |
| "T(n) is Θ(n²)" | c₁·n² ≤ T(n) ≤ c₂·n² | ✓ Valid |
| **"T(n) is at least O(n²)"** | ??? | ✗ **MEANINGLESS** |
| "T(n) is at most Ω(n²)" | ??? | ✗ Meaningless |

---

### Key Insights

1. **O is for upper bounds (≤)**
   - Don't use "at least" with O
   - Use "at most" if you must add words

2. **Ω is for lower bounds (≥)**
   - Don't use "at most" with Ω
   - Use "at least" if you must add words

3. **Θ is for tight bounds (=)**
   - Already implies both upper and lower
   - No need for "at least" or "at most"

4. **The notation already implies the bound direction!**
   - O means ≤ (already "at most")
   - Ω means ≥ (already "at least")
   - Adding words creates confusion

---

## Problem 3.2-3: Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?

### Problem Statement
Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?

---

### Part 1: Is 2^(n+1) = O(2^n)?

**Claim:** YES, 2^(n+1) = O(2^n)

---

#### Method 1: Direct Algebraic Proof

**Step 1: Simplify 2^(n+1)**
```
2^(n+1) = 2^n · 2^1 = 2 · 2^n
```

**Step 2: Apply O-notation definition**

We need to show: ∃c, n₀: 2^(n+1) ≤ c · 2^n for all n ≥ n₀

From Step 1:
```
2^(n+1) = 2 · 2^n
```

So:
```
2^(n+1) = 2 · 2^n ≤ 2 · 2^n for all n ≥ 1
```

**With c = 2 and n₀ = 1:**
```
2^(n+1) ≤ c · 2^n for all n ≥ n₀
```

**Conclusion:** 2^(n+1) = O(2^n) ✓

---

#### Method 2: Limit Test

**Compute:**
```
lim(n→∞) 2^(n+1) / 2^n
```

**Simplify:**
```
= lim(n→∞) 2^(n+1) / 2^n
= lim(n→∞) 2^(n+1-n)
= lim(n→∞) 2^1
= 2
```

**Interpretation:**
Since the limit is a positive constant (2), we have:
```
2^(n+1) = Θ(2^n)
```

And Θ(2^n) implies O(2^n).

**Conclusion:** 2^(n+1) = O(2^n) ✓

---

#### Method 3: Ratio Analysis

**For all n:**
```
2^(n+1) / 2^n = 2
```

The ratio is constant!

This means 2^(n+1) is always exactly 2 times 2^n.

**Therefore:**
```
2^(n+1) = 2 · 2^n ≤ 2 · 2^n
```

**Conclusion:** 2^(n+1) = O(2^n) with c = 2 ✓

---

#### Verification with Examples

| n | 2^n | 2^(n+1) | Ratio |
|---|-----|---------|-------|
| 1 | 2 | 4 | 2 |
| 2 | 4 | 8 | 2 |
| 3 | 8 | 16 | 2 |
| 4 | 16 | 32 | 2 |
| 10 | 1024 | 2048 | 2 |

The ratio is always 2! ✓

---

### Part 2: Is 2^(2n) = O(2^n)?

**Claim:** NO, 2^(2n) ≠ O(2^n)

---

#### Method 1: Direct Algebraic Proof

**Step 1: Simplify 2^(2n)**
```
2^(2n) = 2^(n·2) = (2^n)^2
```

**Step 2: Try to apply O-notation definition**

For 2^(2n) = O(2^n) to be true, we need:
```
∃c, n₀: 2^(2n) ≤ c · 2^n for all n ≥ n₀
```

Substituting:
```
(2^n)^2 ≤ c · 2^n
```

**Divide both sides by 2^n (which is positive):**
```
2^n ≤ c
```

**Problem:** 2^n grows to infinity as n → ∞!

No constant c can bound 2^n for all n ≥ n₀.

**Conclusion:** 2^(2n) ≠ O(2^n) ✗

---

#### Method 2: Limit Test

**Compute:**
```
lim(n→∞) 2^(2n) / 2^n
```

**Simplify:**
```
= lim(n→∞) 2^(2n) / 2^n
= lim(n→∞) 2^(2n-n)
= lim(n→∞) 2^n
= ∞
```

**Interpretation:**
Since the limit is infinity, we have:
```
2^(2n) = ω(2^n)
```

And ω(2^n) means it's NOT O(2^n).

**Conclusion:** 2^(2n) ≠ O(2^n) ✗

---

#### Method 3: Ratio Analysis

**For all n:**
```
2^(2n) / 2^n = 2^n
```

The ratio grows exponentially!

| n | 2^n | 2^(2n) | Ratio |
|---|-----|--------|-------|
| 1 | 2 | 4 | 2 |
| 2 | 4 | 16 | 4 |
| 3 | 8 | 64 | 8 |
| 4 | 16 | 256 | 16 |
| 10 | 1024 | 1,048,576 | 1024 |

The ratio grows without bound!

**Conclusion:** 2^(2n) ≠ O(2^n) ✗

---

### Summary and Key Insights

**Results:**
```
2^(n+1) = O(2^n)   ✓  (actually Θ(2^n))
2^(2n) ≠ O(2^n)    ✗  (actually ω(2^n))
```

**Why the difference?**

**Constant in exponent:** 2^(n+c) = O(2^n)
- Adding a constant to the exponent just multiplies by 2^c
- 2^(n+1) = 2 · 2^n
- 2^(n+5) = 32 · 2^n
- Constant factors don't change asymptotic class

**Variable in exponent:** 2^(cn) ≠ O(2^n) for c > 1
- Multiplying the exponent by c raises to power c
- 2^(2n) = (2^n)^2 = exponential of exponential
- 2^(3n) = (2^n)^3
- This changes the asymptotic class

**General rule:**
```
a^(n+c) = Θ(a^n)     [constant shift: OK]
a^(cn) = ω(a^n)      [constant multiple: NOT OK for c > 1]
```

**Intuition:**
- Exponentials are sensitive to the exponent
- Adding to exponent: linear effect (multiply by constant)
- Multiplying exponent: exponential effect (raise to power)

---

## Problem 3.2-4: Prove Theorem 3.1

### Problem Statement
Prove Theorem 3.1.

**Note:** The exact statement of Theorem 3.1 varies by textbook edition. Common versions include:
- Transitivity properties
- Reflexivity properties
- Symmetry properties
- Transpose symmetry

I'll prove all major properties.

---

### Property 1: Transitivity

**Theorem:** If f(n) = Θ(g(n)) and g(n) = Θ(h(n)), then f(n) = Θ(h(n))

**Proof:**

**Given:**
- f(n) = Θ(g(n)): ∃c₁, c₂, n₁ > 0: c₁g(n) ≤ f(n) ≤ c₂g(n) for all n ≥ n₁
- g(n) = Θ(h(n)): ∃c₃, c₄, n₂ > 0: c₃h(n) ≤ g(n) ≤ c₄h(n) for all n ≥ n₂

**To prove:** f(n) = Θ(h(n))

**Step 1: Establish upper bound**

From f(n) ≤ c₂g(n) and g(n) ≤ c₄h(n):
```
f(n) ≤ c₂g(n) ≤ c₂(c₄h(n)) = (c₂c₄)h(n)
```

Let c₆ = c₂c₄. Then:
```
f(n) ≤ c₆h(n) for all n ≥ max{n₁, n₂}
```

**Step 2: Establish lower bound**

From f(n) ≥ c₁g(n) and g(n) ≥ c₃h(n):
```
f(n) ≥ c₁g(n) ≥ c₁(c₃h(n)) = (c₁c₃)h(n)
```

Let c₅ = c₁c₃. Then:
```
f(n) ≥ c₅h(n) for all n ≥ max{n₁, n₂}
```

**Step 3: Combine**

With c₅ = c₁c₃, c₆ = c₂c₄, and n₀ = max{n₁, n₂}:
```
c₅h(n) ≤ f(n) ≤ c₆h(n) for all n ≥ n₀
```

**Conclusion:** f(n) = Θ(h(n)) ✓

**Similar proofs work for O, Ω, o, ω.**

---

### Property 2: Reflexivity

**Theorem:** f(n) = Θ(f(n))

**Proof:**

**To prove:** ∃c₁, c₂, n₀: c₁f(n) ≤ f(n) ≤ c₂f(n) for all n ≥ n₀

**Choose:** c₁ = 1, c₂ = 1, n₀ = 1

Then:
```
1·f(n) ≤ f(n) ≤ 1·f(n) for all n ≥ 1
```

This is trivially true!

**Conclusion:** f(n) = Θ(f(n)) ✓

**Similar proofs work for O and Ω:**
- f(n) = O(f(n)) with c = 1
- f(n) = Ω(f(n)) with c = 1

---

### Property 3: Symmetry

**Theorem:** f(n) = Θ(g(n)) if and only if g(n) = Θ(f(n))

**Proof:**

**(⟹) Forward direction:**

Assume f(n) = Θ(g(n)).

By definition: ∃c₁, c₂, n₀: c₁g(n) ≤ f(n) ≤ c₂g(n) for all n ≥ n₀

Rearranging:
```
c₁g(n) ≤ f(n)  ⟹  g(n) ≤ (1/c₁)f(n)
f(n) ≤ c₂g(n)  ⟹  (1/c₂)f(n) ≤ g(n)
```

So:
```
(1/c₂)f(n) ≤ g(n) ≤ (1/c₁)f(n)
```

Let c₃ = 1/c₂ and c₄ = 1/c₁. Then:
```
c₃f(n) ≤ g(n) ≤ c₄f(n) for all n ≥ n₀
```

Therefore g(n) = Θ(f(n)). ✓

**(⟸) Backward direction:**

By symmetry of the argument, if g(n) = Θ(f(n)), then f(n) = Θ(g(n)). ✓

**Conclusion:** f(n) = Θ(g(n)) ⟺ g(n) = Θ(f(n)) ✓

---

### Property 4: Transpose Symmetry

**Theorem:** f(n) = O(g(n)) if and only if g(n) = Ω(f(n))

**Proof:**

**(⟹) Forward direction:**

Assume f(n) = O(g(n)).

By definition: ∃c, n₀: f(n) ≤ c·g(n) for all n ≥ n₀

Rearranging:
```
f(n) ≤ c·g(n)
(1/c)·f(n) ≤ g(n)
```

Let c' = 1/c. Then:
```
c'·f(n) ≤ g(n) for all n ≥ n₀
```

By definition of Ω: g(n) = Ω(f(n)). ✓

**(⟸) Backward direction:**

Assume g(n) = Ω(f(n)).

By definition: ∃c, n₀: c·f(n) ≤ g(n) for all n ≥ n₀

Rearranging:
```
c·f(n) ≤ g(n)
f(n) ≤ (1/c)·g(n)
```

Let c' = 1/c. Then:
```
f(n) ≤ c'·g(n) for all n ≥ n₀
```

By definition of O: f(n) = O(g(n)). ✓

**Conclusion:** f(n) = O(g(n)) ⟺ g(n) = Ω(f(n)) ✓

**Similarly:** f(n) = o(g(n)) ⟺ g(n) = ω(f(n))

---

### Summary of Properties

| Property | Statement | Notations |
|----------|-----------|-----------|
| Transitivity | f=Θ(g), g=Θ(h) ⟹ f=Θ(h) | Θ, O, Ω, o, ω |
| Reflexivity | f=Θ(f) | Θ, O, Ω |
| Symmetry | f=Θ(g) ⟺ g=Θ(f) | Θ only |
| Transpose Symmetry | f=O(g) ⟺ g=Ω(f) | O↔Ω, o↔ω |

---

## Problem 3.2-5: Θ(g(n)) ⟺ worst-case O(g(n)) and best-case Ω(g(n))

### Problem Statement
Prove that the running time of an algorithm is Θ(g(n)) if and only if its worst-case running time is O(g(n)) and its best-case running time is Ω(g(n)).

---

### Understanding the Problem

**Notation:**
- T(n, I) = running time on input I of size n
- T_worst(n) = max{T(n, I) : |I| = n}
- T_best(n) = min{T(n, I) : |I| = n}

**What we're proving:**
```
T(n) = Θ(g(n)) ⟺ [T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))]
```

**Why this matters:**
- Shows relationship between average, best, and worst cases
- Tight bound means all cases have same asymptotic behavior
- Useful for analyzing algorithm efficiency

---

### Solution

**Claim:** T(n) = Θ(g(n)) ⟺ [T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))]

---

### Part 1: Forward Direction (⟹)

**Assume:** T(n) = Θ(g(n))

**To prove:** T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))

**Proof:**

By definition of Θ:
```
T(n) = Θ(g(n)) means:
∃c₁, c₂, n₀: c₁g(n) ≤ T(n, I) ≤ c₂g(n) for all inputs I with |I| = n ≥ n₀
```

**Step 1: Prove T_worst(n) = O(g(n))**

Since T(n, I) ≤ c₂g(n) for all inputs I:
```
T_worst(n) = max{T(n, I)} ≤ c₂g(n)
```

Therefore T_worst(n) = O(g(n)) with c = c₂. ✓

**Step 2: Prove T_best(n) = Ω(g(n))**

Since T(n, I) ≥ c₁g(n) for all inputs I:
```
T_best(n) = min{T(n, I)} ≥ c₁g(n)
```

Therefore T_best(n) = Ω(g(n)) with c = c₁. ✓

**Conclusion:** T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n)). ✓

---

### Part 2: Backward Direction (⟸)

**Assume:** T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))

**To prove:** T(n) = Θ(g(n))

**Proof:**

By assumptions:
- T_worst(n) = O(g(n)): ∃c₂, n₁: T_worst(n) ≤ c₂g(n) for n ≥ n₁
- T_best(n) = Ω(g(n)): ∃c₁, n₂: T_best(n) ≥ c₁g(n) for n ≥ n₂

**Step 1: Establish bounds on T(n, I)**

For any input I of size n:
```
T_best(n) ≤ T(n, I) ≤ T_worst(n)  [by definition of min and max]
```

**Step 2: Apply the assumptions**

For n ≥ max{n₁, n₂}:
```
c₁g(n) ≤ T_best(n) ≤ T(n, I) ≤ T_worst(n) ≤ c₂g(n)
```

Therefore:
```
c₁g(n) ≤ T(n, I) ≤ c₂g(n) for all inputs I with |I| = n ≥ max{n₁, n₂}
```

**Step 3: Conclude**

By definition of Θ:
```
T(n) = Θ(g(n)) ✓
```

---

### Part 3: Combining Results

Since we've proven both directions:
```
T(n) = Θ(g(n)) ⟺ [T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))] ✓
```

---

### Interpretation and Examples

**What this theorem means:**

1. **Tight bound requires consistency:**
   - If T(n) = Θ(g(n)), then best and worst cases grow at same rate
   - No huge gap between best and worst

2. **Converse also true:**
   - If best and worst have same asymptotic growth, then T(n) is tight

**Example 1: Merge Sort**
```
T_best(n) = Θ(n lg n)
T_worst(n) = Θ(n lg n)

Therefore: T(n) = Θ(n lg n) ✓
```

**Example 2: Quicksort**
```
T_best(n) = Θ(n lg n)
T_worst(n) = Θ(n²)

Therefore: T(n) ≠ Θ(...) [no tight bound for all cases]
```

**Example 3: Linear Search**
```
T_best(n) = Θ(1)      [found immediately]
T_worst(n) = Θ(n)     [found at end]

Therefore: T(n) ≠ Θ(...) [no tight bound]
```

---

### Key Insights

1. **Θ means consistent performance:**
   - Best and worst cases have same growth rate
   - Predictable behavior

2. **Gap between best and worst:**
   - Large gap ⟹ no tight bound
   - Small gap ⟹ possible tight bound

3. **Practical implications:**
   - Θ(g(n)) algorithms are more predictable
   - Easier to analyze and optimize

---

## Problem 3.2-6: Prove o(g(n)) ∩ ω(g(n)) = ∅

### Problem Statement
Prove that o(g(n)) ∩ ω(g(n)) is the empty set.

---

### Understanding the Problem

**What we're proving:**
No function can be both o(g(n)) and ω(g(n)) simultaneously.

**Why this matters:**
- Shows that o and ω are mutually exclusive
- A function can't grow both strictly slower AND strictly faster
- Fundamental property of asymptotic notation

**Intuition:**
- o(g(n)): f grows strictly slower than g
- ω(g(n)): f grows strictly faster than g
- Can't be both!

---

### Solution

**Claim:** o(g(n)) ∩ ω(g(n)) = ∅

**Proof by contradiction:**

---

### Step 1: Assume the Opposite

Assume there exists a function f(n) such that:
```
f(n) ∈ o(g(n)) AND f(n) ∈ ω(g(n))
```

---

### Step 2: Apply Definition of o(g(n))

By definition of little-o:
```
f(n) ∈ o(g(n)) means:
∀c > 0, ∃n₁ > 0: 0 ≤ f(n) < c·g(n) for all n ≥ n₁
```

**In particular, choose c = 1:**
```
∃n₁: f(n) < 1·g(n) for all n ≥ n₁
```

So:
```
f(n) < g(n) for all n ≥ n₁  ... (1)
```

---

### Step 3: Apply Definition of ω(g(n))

By definition of little-omega:
```
f(n) ∈ ω(g(n)) means:
∀c > 0, ∃n₂ > 0: 0 ≤ c·g(n) < f(n) for all n ≥ n₂
```

**In particular, choose c = 2:**
```
∃n₂: 2·g(n) < f(n) for all n ≥ n₂
```

So:
```
f(n) > 2g(n) for all n ≥ n₂  ... (2)
```

---

### Step 4: Derive the Contradiction

Let n₀ = max{n₁, n₂}.

For all n ≥ n₀, both (1) and (2) must hold:
```
f(n) < g(n)    [from (1)]
f(n) > 2g(n)   [from (2)]
```

From these two inequalities:
```
g(n) > f(n) > 2g(n)
```

This implies:
```
g(n) > 2g(n)
```

Dividing by g(n) (which is positive):
```
1 > 2
```

**This is a contradiction!** ⚡

---

### Step 5: Conclude

Since assuming f(n) ∈ o(g(n)) ∩ ω(g(n)) leads to a contradiction, no such f(n) can exist.

**Therefore:**
```
o(g(n)) ∩ ω(g(n)) = ∅ ✓
```

---

### Alternative Proof Using Limits

**Proof:**

Assume f(n) ∈ o(g(n)) ∩ ω(g(n)).

**From o(g(n)):**
```
lim(n→∞) f(n)/g(n) = 0
```

**From ω(g(n)):**
```
lim(n→∞) f(n)/g(n) = ∞
```

**Contradiction:** A limit cannot be both 0 and ∞! ⚡

**Therefore:** o(g(n)) ∩ ω(g(n)) = ∅ ✓

---

### Visualization

```
Functions relative to g(n):

ω(g(n)): grows FASTER than g(n)
         ↑
         |  [f(n) >> g(n)]
         |
Θ(g(n)): grows SAME as g(n)
         |  [f(n) ≈ g(n)]
         |
o(g(n)): grows SLOWER than g(n)
         ↓  [f(n) << g(n)]

o and ω are on opposite sides!
They cannot overlap.
```

---

### Key Insights

1. **Mutually exclusive:**
   - o(g) and ω(g) have no overlap
   - A function is either slower, same, or faster—not multiple

2. **Analogy to real numbers:**
   - Like saying a number can't be both < 5 and > 10
   - Logically impossible

3. **What about O and Ω?**
   - O(g) ∩ Ω(g) = Θ(g) [NOT empty!]
   - O and Ω can overlap (at Θ)
   - But o and ω cannot

4. **Complete picture:**
   ```
   o(g) ∩ ω(g) = ∅        [empty]
   O(g) ∩ Ω(g) = Θ(g)     [not empty]
   ```

---

## Problem 3.2-7: Extending to Two Parameters

### Problem Statement
We can extend our notation to the case of two parameters n and m that can go to ∞ independently at different rates. For a given function g(n, m), we denote by O(g(n, m)) the set of functions:

```
O(g(n,m)) = {f(n,m) : ∃c, n₀, m₀ > 0 such that
             0 ≤ f(n,m) ≤ c·g(n,m) for all n ≥ n₀ or m ≥ m₀}
```

Give corresponding definitions for Ω(g(n, m)) and Θ(g(n, m)).

---

### Understanding the Problem

**Why two parameters?**
- Some algorithms depend on multiple input sizes
- Example: matrix multiplication with dimensions n×m
- Example: graph algorithms with |V| vertices and |E| edges

**Key change:**
- Single parameter: "for all n ≥ n₀"
- Two parameters: "for all n ≥ n₀ **or** m ≥ m₀"

**Interpretation:**
The bound holds when **at least one** of the parameters is large enough.

---

### Solution

---

### Definition 1: Ω(g(n, m))

**By analogy with single-parameter Ω:**

```
Ω(g(n,m)) = {f(n,m) : ∃c, n₀, m₀ > 0 such that
             0 ≤ c·g(n,m) ≤ f(n,m) for all n ≥ n₀ or m ≥ m₀}
```

**In words:**
- f(n,m) is bounded below by c·g(n,m)
- The bound holds when n is large enough OR m is large enough (or both)

**Meaning:**
f(n,m) grows at least as fast as g(n,m) when at least one parameter is large.

---

### Definition 2: Θ(g(n, m))

**By analogy with single-parameter Θ:**

```
Θ(g(n,m)) = {f(n,m) : ∃c₁, c₂, n₀, m₀ > 0 such that
             0 ≤ c₁·g(n,m) ≤ f(n,m) ≤ c₂·g(n,m) 
             for all n ≥ n₀ or m ≥ m₀}
```

**In words:**
- f(n,m) is sandwiched between c₁·g(n,m) and c₂·g(n,m)
- The bound holds when n is large enough OR m is large enough (or both)

**Meaning:**
f(n,m) grows at the same rate as g(n,m) when at least one parameter is large.

---

### Alternative Interpretation: "AND" vs "OR"

**The given definition uses "OR":**
```
for all n ≥ n₀ or m ≥ m₀
```

**Alternative (stricter) definition uses "AND":**
```
for all n ≥ n₀ and m ≥ m₀
```

**Difference:**

**"OR" version:**
- Bound holds when **at least one** parameter is large
- More lenient
- Easier to satisfy

**"AND" version:**
- Bound holds when **both** parameters are large
- More strict
- Harder to satisfy

**Which to use?**
- The problem specifies "OR"
- Follow the given definition
- But be aware both interpretations exist in literature

---

### Examples

**Example 1: Matrix multiplication**

```
f(n, m) = n·m  [time to multiply n×m matrix by m×1 vector]

Claim: f(n, m) = Θ(n·m)

Proof:
1·(n·m) ≤ n·m ≤ 1·(n·m) for all n ≥ 1 or m ≥ 1

So c₁ = 1, c₂ = 1, n₀ = 1, m₀ = 1 ✓
```

**Example 2: Nested loops**

```
f(n, m) = n² + m²  [two independent nested loops]

Claim: f(n, m) = O(n² + m²)

Proof:
n² + m² ≤ 1·(n² + m²) for all n ≥ 1 or m ≥ 1

So c = 1, n₀ = 1, m₀ = 1 ✓
```

**Example 3: Graph algorithm**

```
f(n, m) = n + m  [BFS with n vertices, m edges]

Claim: f(n, m) = Θ(n + m)

Proof:
1·(n + m) ≤ n + m ≤ 1·(n + m) for all n ≥ 1 or m ≥ 1

So c₁ = 1, c₂ = 1, n₀ = 1, m₀ = 1 ✓
```

---

### Extending to o and ω

**For completeness:**

**o(g(n, m)):**
```
o(g(n,m)) = {f(n,m) : ∀c > 0, ∃n₀, m₀ > 0 such that
             0 ≤ f(n,m) < c·g(n,m) for all n ≥ n₀ or m ≥ m₀}
```

**ω(g(n, m)):**
```
ω(g(n,m)) = {f(n,m) : ∀c > 0, ∃n₀, m₀ > 0 such that
             0 ≤ c·g(n,m) < f(n,m) for all n ≥ n₀ or m ≥ m₀}
```

---

### Key Insights

1. **Natural generalization:**
   - Same structure as single-parameter
   - Just add more threshold parameters

2. **"OR" vs "AND":**
   - "OR": at least one parameter large
   - "AND": both parameters large
   - Problem specifies "OR"

3. **Practical applications:**
   - Matrix operations
   - Graph algorithms
   - String matching
   - Any algorithm with multiple input sizes

4. **Further generalization:**
   - Can extend to 3+ parameters
   - Same pattern: O(g(n₁, n₂, ..., nₖ))

---

## Summary: Problem-Solving Patterns

### Pattern Recognition

| Problem Type | Keywords | Approach |
|--------------|----------|----------|
| Prove Θ | "prove", "max", "Θ" | Show upper + lower bounds |
| Meaningless | "explain why", "meaningless" | Identify logical error |
| True/False | "Is ... = O(...)?", "True or false" | Use limit test or definitions |
| Prove theorem | "Prove Theorem", "show that" | Use definitions, algebra |
| If-and-only-if | "if and only if", "⟺" | Prove both directions |
| Empty set | "intersection", "∅" | Proof by contradiction |
| Extend definitions | "extend", "two parameters" | Generalize carefully |

### Universal Strategy

1. **Understand what you're proving**
2. **Write down relevant definitions**
3. **Choose proof technique** (direct, contradiction, limits)
4. **Execute proof with clear steps**
5. **Verify with examples**

### Common Proof Techniques

**For bounds:**
- Direct: Use definitions with algebra
- Limits: Compute lim f/g
- Examples: Verify with concrete values

**For if-and-only-if:**
- Prove ⟹ direction
- Prove ⟸ direction
- Combine

**For impossibility:**
- Assume opposite
- Derive contradiction
- Conclude

---

**You're now ready to tackle any Chapter 3.2 problem! 🚀**

---

**End of Solutions**
