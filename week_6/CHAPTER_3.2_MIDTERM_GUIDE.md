# Chapter 3.2 Midterm Guide: Asymptotic Notation Mastery

**Course:** CS3112 - Introduction to Algorithms  
**Topic:** Asymptotic Notation (Θ, O, Ω, o, ω)  
**Purpose:** Master asymptotic notation for midterm - JIT learning approach

---

## 🎯 Core Mental Model: What Chapter 3.2 Is Really About

### The Big Picture
Chapter 3.2 teaches you **how to formally describe and compare algorithm running times** using mathematical notation. Think of it as learning the "language" of algorithm analysis.

**Key insight:** Asymptotic notation is like comparing speeds:
- **O(g(n))**: "At most as fast as g(n)" (upper bound) → like ≤
- **Ω(g(n))**: "At least as fast as g(n)" (lower bound) → like ≥
- **Θ(g(n))**: "Exactly as fast as g(n)" (tight bound) → like =
- **o(g(n))**: "Strictly slower than g(n)" (strict upper) → like <
- **ω(g(n))**: "Strictly faster than g(n)" (strict lower) → like >

---

## 📊 The Big 5 Notations: Deep Understanding

### Θ-notation (Theta): Tight Bound

**Intuition:** f(n) grows at the same rate as g(n)

**Formal definition:**
```
Θ(g(n)) = {f(n) : ∃c₁, c₂, n₀ > 0 such that 
           0 ≤ c₁·g(n) ≤ f(n) ≤ c₂·g(n) for all n ≥ n₀}
```

**What this means:**
- f(n) is "sandwiched" between two multiples of g(n)
- f(n) grows neither faster nor slower than g(n)
- Most precise bound

**Visual:**
```
    c₂·g(n)  ←  upper bound
       ↑
    f(n)     ←  our function (sandwiched)
       ↓
    c₁·g(n)  ←  lower bound
```

**Example:**
```
f(n) = 3n² + 5n + 2

Claim: f(n) = Θ(n²)

Proof:
- Upper bound: 3n² + 5n + 2 ≤ 3n² + 5n² + 2n² = 10n² for n ≥ 1
  So c₂ = 10, and f(n) ≤ c₂·n²

- Lower bound: 3n² + 5n + 2 ≥ 3n² for n ≥ 1
  So c₁ = 3, and f(n) ≥ c₁·n²

Therefore: 3n² ≤ f(n) ≤ 10n² for n ≥ 1
Thus: f(n) = Θ(n²) ✓
```

---

### O-notation (Big-O): Upper Bound

**Intuition:** f(n) grows no faster than g(n)

**Formal definition:**
```
O(g(n)) = {f(n) : ∃c, n₀ > 0 such that 
           0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀}
```

**What this means:**
- f(n) is bounded above by some multiple of g(n)
- f(n) might grow slower than g(n), but never faster
- Gives worst-case guarantee

**Example:**
```
f(n) = 2n + 5

Claim: f(n) = O(n²)  [loose bound]
Proof: 2n + 5 ≤ 2n² + 5n² = 7n² for n ≥ 1
       So c = 7, n₀ = 1 ✓

Also: f(n) = O(n)    [tight bound]
Proof: 2n + 5 ≤ 2n + 5n = 7n for n ≥ 1
       So c = 7, n₀ = 1 ✓
```

**Key point:** O gives upper bound, but not necessarily tight!

---

### Ω-notation (Omega): Lower Bound

**Intuition:** f(n) grows at least as fast as g(n)

**Formal definition:**
```
Ω(g(n)) = {f(n) : ∃c, n₀ > 0 such that 
           0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀}
```

**What this means:**
- f(n) is bounded below by some multiple of g(n)
- f(n) might grow faster than g(n), but never slower
- Gives best-case guarantee

**Example:**
```
f(n) = 3n² + 5n

Claim: f(n) = Ω(n)   [loose bound]
Proof: 3n² + 5n ≥ 5n for n ≥ 1
       So c = 5, n₀ = 1 ✓

Also: f(n) = Ω(n²)   [tight bound]
Proof: 3n² + 5n ≥ 3n² for n ≥ 1
       So c = 3, n₀ = 1 ✓
```

---

### o-notation (little-o): Strict Upper Bound

**Intuition:** f(n) grows strictly slower than g(n)

**Formal definition:**
```
o(g(n)) = {f(n) : ∀c > 0, ∃n₀ > 0 such that 
           0 ≤ f(n) < c·g(n) for all n ≥ n₀}
```

**Limit definition (easier to use):**
```
f(n) = o(g(n)) ⟺ lim(n→∞) f(n)/g(n) = 0
```

**What this means:**
- f(n) becomes negligible compared to g(n)
- f(n) grows strictly slower (not just "no faster")
- The ratio f(n)/g(n) goes to zero

**Examples:**
```
n = o(n²)        ✓  (lim n/n² = lim 1/n = 0)
n² = o(n²)       ✗  (lim n²/n² = 1 ≠ 0)
lg n = o(n)      ✓  (lim lg n / n = 0)
n = o(n lg n)    ✓  (lim n/(n lg n) = lim 1/lg n = 0)
```

**Key difference from O:**
- O: "for some constant c" (∃c)
- o: "for all constants c" (∀c)

---

### ω-notation (little-omega): Strict Lower Bound

**Intuition:** f(n) grows strictly faster than g(n)

**Formal definition:**
```
ω(g(n)) = {f(n) : ∀c > 0, ∃n₀ > 0 such that 
           0 ≤ c·g(n) < f(n) for all n ≥ n₀}
```

**Limit definition (easier to use):**
```
f(n) = ω(g(n)) ⟺ lim(n→∞) f(n)/g(n) = ∞
```

**What this means:**
- f(n) dominates g(n)
- f(n) grows strictly faster (not just "no slower")
- The ratio f(n)/g(n) goes to infinity

**Examples:**
```
n² = ω(n)        ✓  (lim n²/n = lim n = ∞)
n² = ω(n²)       ✗  (lim n²/n² = 1 ≠ ∞)
n lg n = ω(n)    ✓  (lim (n lg n)/n = lim lg n = ∞)
2ⁿ = ω(n²)       ✓  (exponential dominates polynomial)
```

**Key relationship:**
```
f(n) = o(g(n)) ⟺ g(n) = ω(f(n))
```

---

## 🧮 Relationships Between Notations

### The Analogy to Real Numbers

| Asymptotic | Real Numbers | Meaning |
|------------|--------------|---------|
| f(n) = O(g(n)) | a ≤ b | f grows no faster than g |
| f(n) = Ω(g(n)) | a ≥ b | f grows no slower than g |
| f(n) = Θ(g(n)) | a = b | f grows at same rate as g |
| f(n) = o(g(n)) | a < b | f grows strictly slower than g |
| f(n) = ω(g(n)) | a > b | f grows strictly faster than g |

### Key Theorem
```
f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))
```

**Proof intuition:** Tight bound = both upper and lower bounds

---

## 📚 Problem Type Taxonomy for Chapter 3.2

### Type 1: Proving Θ-notation (Problem 3.2-1)

**Recognition:** "Prove that ... = Θ(...)" or "show max{f,g} = Θ(...)"

**Approach:**
1. Show upper bound: f(n) ≤ c₂·g(n)
2. Show lower bound: f(n) ≥ c₁·g(n)
3. Find constants c₁, c₂, n₀

**Template:**
```
Claim: f(n) = Θ(g(n))

Proof:
Upper bound (O):
  [Show f(n) ≤ c₂·g(n) for some c₂, n₀]
  
Lower bound (Ω):
  [Show f(n) ≥ c₁·g(n) for some c₁, n₀]
  
Conclusion:
  c₁·g(n) ≤ f(n) ≤ c₂·g(n) for n ≥ n₀
  Therefore f(n) = Θ(g(n)) ✓
```

---

### Type 2: Explaining Meaningless Statements (Problem 3.2-2)

**Recognition:** "Explain why ... is meaningless" or "what's wrong with..."

**Approach:**
1. Identify the logical error
2. Explain what the notation actually means
3. Show why the statement is contradictory or nonsensical

**Common errors:**
- Mixing "at least" with O (upper bound)
- Mixing "at most" with Ω (lower bound)
- Using = when meaning ∈
- Comparing incomparable functions

---

### Type 3: True/False with O-notation (Problem 3.2-3)

**Recognition:** "Is ... = O(...)?" or "True or false: ..."

**Approach:**
1. Use limit test: compute lim(n→∞) f(n)/g(n)
2. Or use definitions directly
3. Find counterexample if false

**Limit test guide:**
```
lim f(n)/g(n) = 0     ⟹  f = o(g)  [and f = O(g)]
lim f(n)/g(n) = c > 0 ⟹  f = Θ(g)  [and f = O(g) and f = Ω(g)]
lim f(n)/g(n) = ∞     ⟹  f = ω(g)  [and f = Ω(g)]
```

---

### Type 4: Proving Theorems (Problem 3.2-4)

**Recognition:** "Prove Theorem X.Y" or "Show that property P holds"

**Approach:**
1. State what needs to be proven
2. Use definitions of asymptotic notation
3. Apply algebraic manipulation
4. Conclude with clear statement

---

### Type 5: If-and-Only-If Proofs (Problem 3.2-5)

**Recognition:** "if and only if", "⟺", "iff"

**Approach:**
1. Prove forward direction (⟹)
2. Prove backward direction (⟸)
3. Both directions together prove ⟺

**Template:**
```
Claim: A ⟺ B

Proof:
(⟹) Assume A. Show B.
  [proof steps]
  Therefore B. ✓

(⟸) Assume B. Show A.
  [proof steps]
  Therefore A. ✓

Conclusion: A ⟺ B ✓
```

---

### Type 6: Set Theory Proofs (Problem 3.2-6)

**Recognition:** "intersection", "empty set", "∩", "∅"

**Approach:**
1. Assume the opposite (proof by contradiction)
2. Show this leads to a contradiction
3. Conclude the original statement

**For empty set:** Show no function can satisfy both conditions

---

### Type 7: Extending Definitions (Problem 3.2-7)

**Recognition:** "extend notation to...", "two parameters", "define..."

**Approach:**
1. Understand the single-parameter definition
2. Generalize to multiple parameters
3. Ensure logical consistency

---

## 🔍 How to Solve Each Problem: Step-by-Step

### Problem 3.2-1: max{f(n), g(n)} = Θ(f(n) + g(n))

**What the problem asks:**
Prove that the maximum of two functions is asymptotically equivalent to their sum.

**Why this matters:**
Shows that when combining algorithms, the dominant one determines the overall complexity.

**Step-by-step solution:**

**Step 1: Understand what we're proving**
```
max{f(n), g(n)} = Θ(f(n) + g(n))
```

This means:
- max{f,g} = O(f + g)  [upper bound]
- max{f,g} = Ω(f + g)  [lower bound]

**Step 2: Prove upper bound**

Let h(n) = max{f(n), g(n)}.

For all n:
```
h(n) = max{f(n), g(n)} ≤ f(n) + g(n)
```

Why? Because:
- If f(n) ≥ g(n), then h(n) = f(n) ≤ f(n) + g(n) ✓
- If g(n) ≥ f(n), then h(n) = g(n) ≤ f(n) + g(n) ✓

Therefore:
```
h(n) ≤ 1·(f(n) + g(n))
```

So h(n) = O(f(n) + g(n)) with c = 1, n₀ = 1. ✓

**Step 3: Prove lower bound**

For all n:
```
h(n) = max{f(n), g(n)} ≥ (1/2)·(f(n) + g(n))
```

Why? Because:
- max{f(n), g(n)} ≥ f(n)  [by definition of max]
- max{f(n), g(n)} ≥ g(n)  [by definition of max]

Adding these inequalities:
```
2·max{f(n), g(n)} ≥ f(n) + g(n)
max{f(n), g(n)} ≥ (1/2)·(f(n) + g(n))
```

Therefore:
```
h(n) ≥ (1/2)·(f(n) + g(n))
```

So h(n) = Ω(f(n) + g(n)) with c = 1/2, n₀ = 1. ✓

**Step 4: Conclude**

Since h(n) = O(f(n) + g(n)) and h(n) = Ω(f(n) + g(n)):
```
h(n) = Θ(f(n) + g(n))
```

Therefore:
```
max{f(n), g(n)} = Θ(f(n) + g(n)) ✓
```

**Key insight:** The max is at least half the sum (lower bound) and at most the full sum (upper bound).

---

### Problem 3.2-2: Why "at least O(n²)" is meaningless

**What the problem asks:**
Explain the logical error in saying "running time is at least O(n²)".

**Step-by-step explanation:**

**Step 1: Understand what O(n²) means**

O(n²) is an **upper bound**. It means:
```
T(n) = O(n²) means T(n) ≤ c·n² for some c, n₀
```

In plain English: "The running time grows no faster than n²"

**Step 2: Understand what "at least" means**

"At least" means **lower bound** (≥).

**Step 3: Identify the contradiction**

The statement "at least O(n²)" means:
```
"The running time is at least [no faster than n²]"
```

This is like saying: "The speed is at least [at most 60 mph]"

**This is meaningless!**

**Step 4: What the speaker probably meant**

They likely meant one of:
1. "The running time is at least Ω(n²)" [lower bound]
2. "The running time is at most O(n²)" [upper bound]
3. "The running time is Θ(n²)" [tight bound]

**Key insight:** 
- O is for upper bounds (≤)
- Ω is for lower bounds (≥)
- Don't mix "at least" with O!

**Correct statements:**
```
✓ "The running time is at most O(n²)"
✓ "The running time is O(n²)"
✓ "The running time is at least Ω(n²)"
✗ "The running time is at least O(n²)"  [MEANINGLESS]
```

---

### Problem 3.2-3: Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?

**What the problem asks:**
Determine if these exponential functions are in O of each other.

**Part 1: Is 2^(n+1) = O(2^n)?**

**Method 1: Direct calculation**
```
2^(n+1) = 2^n · 2^1 = 2 · 2^n
```

So:
```
2^(n+1) = 2 · 2^n ≤ 2 · 2^n for all n ≥ 1
```

With c = 2, n₀ = 1:
```
2^(n+1) ≤ c · 2^n
```

**Answer: YES, 2^(n+1) = O(2^n)** ✓

**Method 2: Limit test**
```
lim(n→∞) 2^(n+1) / 2^n = lim(n→∞) 2^(n+1-n) = lim(n→∞) 2^1 = 2
```

Since the limit is a positive constant, 2^(n+1) = Θ(2^n), which implies O(2^n). ✓

---

**Part 2: Is 2^(2n) = O(2^n)?**

**Method 1: Direct calculation**
```
2^(2n) = 2^(n·2) = (2^n)^2
```

For 2^(2n) = O(2^n) to be true, we need:
```
(2^n)^2 ≤ c · 2^n for some constant c and all n ≥ n₀
```

Dividing both sides by 2^n:
```
2^n ≤ c
```

But 2^n grows to infinity! No constant c can bound it.

**Answer: NO, 2^(2n) ≠ O(2^n)** ✗

**Method 2: Limit test**
```
lim(n→∞) 2^(2n) / 2^n = lim(n→∞) 2^(2n-n) = lim(n→∞) 2^n = ∞
```

Since the limit is infinity, 2^(2n) = ω(2^n), which means it's NOT O(2^n). ✗

**Key insight:**
- Constant factors in exponent: 2^(n+1) = O(2^n) ✓
- Variable factors in exponent: 2^(2n) ≠ O(2^n) ✗

**Summary:**
```
2^(n+1) = O(2^n)   ✓  (actually Θ(2^n))
2^(2n) = ω(2^n)    ✓  (grows much faster)
```

---

### Problem 3.2-4: Prove Theorem 3.1

**Note:** Theorem 3.1 states relationships between asymptotic notations. The exact statement depends on your textbook, but typically it's about transitivity, reflexivity, symmetry, or transpose symmetry.

**Common Theorem 3.1 statements:**

**Version A: Transitivity**
```
If f(n) = Θ(g(n)) and g(n) = Θ(h(n)), then f(n) = Θ(h(n))
```

**Proof:**

Given:
- f(n) = Θ(g(n)): ∃c₁, c₂, n₁: c₁g(n) ≤ f(n) ≤ c₂g(n) for n ≥ n₁
- g(n) = Θ(h(n)): ∃c₃, c₄, n₂: c₃h(n) ≤ g(n) ≤ c₄h(n) for n ≥ n₂

To prove: f(n) = Θ(h(n))

From the first inequality:
```
c₁g(n) ≤ f(n) ≤ c₂g(n)
```

Substitute the bounds on g(n):
```
c₁(c₃h(n)) ≤ f(n) ≤ c₂(c₄h(n))
(c₁c₃)h(n) ≤ f(n) ≤ (c₂c₄)h(n)
```

Let c₅ = c₁c₃ and c₆ = c₂c₄, and n₀ = max{n₁, n₂}.

Then:
```
c₅h(n) ≤ f(n) ≤ c₆h(n) for all n ≥ n₀
```

Therefore f(n) = Θ(h(n)). ✓

---

**Version B: Transpose Symmetry**
```
f(n) = O(g(n)) if and only if g(n) = Ω(f(n))
```

**Proof:**

(⟹) Assume f(n) = O(g(n)).

By definition: ∃c, n₀: f(n) ≤ c·g(n) for n ≥ n₀

Rearranging: (1/c)·f(n) ≤ g(n)

Let c' = 1/c. Then: c'·f(n) ≤ g(n) for n ≥ n₀

By definition of Ω: g(n) = Ω(f(n)). ✓

(⟸) Assume g(n) = Ω(f(n)).

By definition: ∃c, n₀: c·f(n) ≤ g(n) for n ≥ n₀

Rearranging: f(n) ≤ (1/c)·g(n)

Let c' = 1/c. Then: f(n) ≤ c'·g(n) for n ≥ n₀

By definition of O: f(n) = O(g(n)). ✓

Therefore: f(n) = O(g(n)) ⟺ g(n) = Ω(f(n)). ✓

---

### Problem 3.2-5: Θ(g(n)) ⟺ worst-case O(g(n)) and best-case Ω(g(n))

**What the problem asks:**
Prove that an algorithm has tight bound Θ(g(n)) if and only if its worst-case is O(g(n)) and best-case is Ω(g(n)).

**Step-by-step proof:**

**Notation:**
- T(n) = running time function
- T_worst(n) = worst-case running time
- T_best(n) = best-case running time

**Claim:**
```
T(n) = Θ(g(n)) ⟺ [T_worst(n) = O(g(n)) AND T_best(n) = Ω(g(n))]
```

**Proof:**

**(⟹) Forward direction:**

Assume T(n) = Θ(g(n)).

By definition: ∃c₁, c₂, n₀: c₁g(n) ≤ T(n) ≤ c₂g(n) for all n ≥ n₀

Since T_worst(n) ≥ T(n) for all inputs:
```
T_worst(n) ≥ T(n) ≥ c₁g(n)
```
Wait, this is wrong. Let me reconsider.

Actually, T_worst(n) is the maximum over all inputs of size n:
```
T_worst(n) = max{T(n, input) : |input| = n}
```

Since T(n) = Θ(g(n)), we have:
```
T(n) ≤ c₂g(n) for all inputs of size n
```

Therefore:
```
T_worst(n) = max{T(n, input)} ≤ c₂g(n)
```

So T_worst(n) = O(g(n)). ✓

Similarly, since T(n) ≥ c₁g(n):
```
T_best(n) = min{T(n, input)} ≥ c₁g(n)
```

So T_best(n) = Ω(g(n)). ✓

**(⟸) Backward direction:**

Assume T_worst(n) = O(g(n)) and T_best(n) = Ω(g(n)).

By definition:
- T_worst(n) ≤ c₂g(n) for n ≥ n₁
- T_best(n) ≥ c₁g(n) for n ≥ n₂

For any input of size n:
```
T_best(n) ≤ T(n, input) ≤ T_worst(n)
```

Therefore:
```
c₁g(n) ≤ T(n, input) ≤ c₂g(n) for n ≥ max{n₁, n₂}
```

This holds for all inputs, so T(n) = Θ(g(n)). ✓

**Conclusion:** T(n) = Θ(g(n)) ⟺ [T_worst = O(g(n)) AND T_best = Ω(g(n))]. ✓

**Key insight:** Tight bound means worst and best cases have the same asymptotic growth.

---

### Problem 3.2-6: o(g(n)) ∩ ω(g(n)) = ∅

**What the problem asks:**
Prove that no function can be both o(g(n)) and ω(g(n)) simultaneously.

**Step-by-step proof:**

**Claim:** o(g(n)) ∩ ω(g(n)) = ∅ (empty set)

**Proof by contradiction:**

Assume there exists a function f(n) such that:
```
f(n) ∈ o(g(n)) AND f(n) ∈ ω(g(n))
```

**From f(n) ∈ o(g(n)):**

By definition of little-o:
```
lim(n→∞) f(n)/g(n) = 0
```

This means: for any ε > 0, ∃n₁: f(n) < ε·g(n) for all n ≥ n₁

**From f(n) ∈ ω(g(n)):**

By definition of little-omega:
```
lim(n→∞) f(n)/g(n) = ∞
```

This means: for any M > 0, ∃n₂: f(n) > M·g(n) for all n ≥ n₂

**The contradiction:**

Choose ε = 1 and M = 2.

From o(g(n)): ∃n₁: f(n) < 1·g(n) for n ≥ n₁
From ω(g(n)): ∃n₂: f(n) > 2·g(n) for n ≥ n₂

Let n₀ = max{n₁, n₂}. Then for n ≥ n₀:
```
f(n) < g(n)  [from o(g(n))]
f(n) > 2g(n) [from ω(g(n))]
```

This implies: g(n) > 2g(n), which means g(n) < 0.

But g(n) is asymptotically positive (by assumption), so g(n) > 0 for large n.

**Contradiction!** ⚡

Therefore, no such f(n) can exist.

**Conclusion:** o(g(n)) ∩ ω(g(n)) = ∅. ✓

**Key insight:** A function can't simultaneously grow strictly slower AND strictly faster than another function.

**Intuition:** It's like saying a number is both less than 5 and greater than 10 simultaneously—impossible!

---

### Problem 3.2-7: Extending to Two Parameters

**What the problem asks:**
Extend O, Ω, Θ notation to functions of two parameters n and m.

**Given definition for O(g(n,m)):**
```
O(g(n,m)) = {f(n,m) : ∃c, n₀, m₀ > 0 such that
             0 ≤ f(n,m) ≤ c·g(n,m) for all n ≥ n₀ or m ≥ m₀}
```

**Step-by-step solution:**

**Understanding the given definition:**

The key change: "for all n ≥ n₀ **or** m ≥ m₀"

This means: the bound holds when **either** n is large **or** m is large (or both).

**Definition for Ω(g(n,m)):**

By analogy with single-parameter Ω:

```
Ω(g(n,m)) = {f(n,m) : ∃c, n₀, m₀ > 0 such that
             0 ≤ c·g(n,m) ≤ f(n,m) for all n ≥ n₀ or m ≥ m₀}
```

**Explanation:**
- f(n,m) is bounded below by c·g(n,m)
- The bound holds when n or m is sufficiently large

**Definition for Θ(g(n,m)):**

By analogy with single-parameter Θ:

```
Θ(g(n,m)) = {f(n,m) : ∃c₁, c₂, n₀, m₀ > 0 such that
             0 ≤ c₁·g(n,m) ≤ f(n,m) ≤ c₂·g(n,m) 
             for all n ≥ n₀ or m ≥ m₀}
```

**Explanation:**
- f(n,m) is sandwiched between two multiples of g(n,m)
- The bound holds when n or m is sufficiently large

**Alternative definition (stricter):**

Some texts use "and" instead of "or":

```
O(g(n,m)) = {f(n,m) : ∃c, n₀, m₀ > 0 such that
             0 ≤ f(n,m) ≤ c·g(n,m) for all n ≥ n₀ AND m ≥ m₀}
```

This requires **both** n and m to be large.

**Example:**

Consider f(n,m) = n² + m³.

**Claim:** f(n,m) = O(n² + m³)

**Proof:**
```
f(n,m) = n² + m³ ≤ 1·(n² + m³) for all n ≥ 1 or m ≥ 1
```

So c = 1, n₀ = 1, m₀ = 1. ✓

**Key insight:** Two-parameter notation handles algorithms whose complexity depends on multiple input sizes (e.g., matrix multiplication with different dimensions).

---

## 🎓 Universal Problem-Solving Strategy

### Step 1: Identify the Problem Type
- Proving Θ? → Show upper and lower bounds
- Meaningless statement? → Identify logical error
- True/False? → Use limit test or definitions
- If-and-only-if? → Prove both directions
- Set theory? → Use contradiction
- Extending definitions? → Generalize carefully

### Step 2: Choose Your Tool

**For proving bounds:**
- Direct: Use definitions with algebra
- Limits: Compute lim f(n)/g(n)
- Contradiction: Assume opposite, derive absurdity

**For limit test:**
```
lim f/g = 0   → f = o(g)
lim f/g = c>0 → f = Θ(g)
lim f/g = ∞   → f = ω(g)
```

### Step 3: Write Clear Proof
1. State what you're proving
2. Show each step with justification
3. Use proper notation
4. Conclude explicitly

### Step 4: Verify
- Check with concrete values
- Ensure constants work
- Verify n₀ is valid

---

## 💡 Common Mistakes to Avoid

### Mistake 1: Confusing O with Θ
```
✗ "The algorithm is O(n²)" when you mean Θ(n²)
✓ Use Θ for tight bounds, O for upper bounds
```

### Mistake 2: Mixing "at least" with O
```
✗ "At least O(n²)" [meaningless!]
✓ "At least Ω(n²)" or "At most O(n²)"
```

### Mistake 3: Forgetting asymptotic positivity
```
✗ Applying definitions to negative functions
✓ Ensure f(n), g(n) > 0 for large n
```

### Mistake 4: Wrong limit interpretation
```
✗ lim f/g = 0 means f = O(g) only
✓ lim f/g = 0 means f = o(g) [stricter!]
```

### Mistake 5: Using = when meaning ∈
```
✗ Treating f(n) = O(g(n)) as equality
✓ Remember: = means ∈ in this context
```

---

## 🚀 Exam Strategy for Chapter 3.2

### Before the Exam
- [ ] Memorize all 5 definitions (Θ, O, Ω, o, ω)
- [ ] Know the real number analogy (≤, ≥, =, <, >)
- [ ] Practice limit tests
- [ ] Understand if-and-only-if proofs
- [ ] Review set theory basics

### During the Exam
- [ ] Read carefully (O vs Ω vs Θ)
- [ ] Write down definitions first
- [ ] Use limit test when possible
- [ ] Show all work
- [ ] Verify with examples

### Time Management
- **Easy (3.2-2, 3.2-3):** 5-7 minutes
- **Medium (3.2-1, 3.2-4, 3.2-7):** 10-15 minutes
- **Hard (3.2-5, 3.2-6):** 15-20 minutes

---

## 📋 Quick Reference

### The Big 5 Definitions
```
Θ(g): c₁g ≤ f ≤ c₂g  [tight bound, =]
O(g): f ≤ cg          [upper bound, ≤]
Ω(g): cg ≤ f          [lower bound, ≥]
o(g): lim f/g = 0     [strict upper, <]
ω(g): lim f/g = ∞     [strict lower, >]
```

### Key Relationships
```
f = Θ(g) ⟺ f = O(g) AND f = Ω(g)
f = o(g) ⟺ g = ω(f)
f = O(g) ⟺ g = Ω(f)
```

### Proof Templates
```
Θ: Show upper + lower bounds
O: Show f ≤ cg
Ω: Show cg ≤ f
o: Show lim f/g = 0
ω: Show lim f/g = ∞
```

---

**You got this! Master these 7 problems and you'll ace the asymptotic notation section! 🎉**

---

**End of Guide**
