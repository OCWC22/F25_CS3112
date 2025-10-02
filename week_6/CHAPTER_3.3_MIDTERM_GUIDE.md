# Chapter 3.3 Midterm Survival Guide: Asymptotic Notation & Function Growth

**Course:** CS3112 - Introduction to Algorithms  
**Topic:** Standard Notations and Common Functions  
**Purpose:** Connect the dots for midterm prep - JIT learning approach

---

## 🎯 Core Mental Model: What Chapter 3.3 Is Really About

### The Big Picture
Chapter 3.3 teaches you **how to compare and manipulate growth rates** of functions. Every problem type falls into one of these categories:

1. **Proving relationships** between functions (monotonicity, composition)
2. **Manipulating asymptotic notation** (Θ, O, Ω, o, ω)
3. **Working with special functions** (factorials, logs, exponentials)
4. **Understanding growth hierarchies** (which functions grow faster?)

---

## 📊 Problem Type Taxonomy: How to Recognize & Solve Each Type

### Type 1: Monotonicity Proofs (Problem 3.3-1)

**What it asks:** Prove properties about monotonically increasing functions

**Recognition pattern:**
- Keywords: "monotonically increasing", "nonnegative"
- Asks about sums, compositions, or products of functions

**Mental model:**
- Monotonically increasing = always going up (or staying flat)
- f(n) ≤ f(n+1) for all n

**Solution approach:**
1. Write down the definition: f(n₁) ≤ f(n₂) whenever n₁ ≤ n₂
2. For sums/products: use algebra to show the property holds
3. For composition: use chain reasoning (if outer and inner both increase, composition increases)

**Example: f(n) + g(n) is monotonically increasing**
```
Given: f, g are monotonically increasing
Prove: h(n) = f(n) + g(n) is monotonically increasing

Let n₁ ≤ n₂
Then: f(n₁) ≤ f(n₂)  [f is monotonic]
      g(n₁) ≤ g(n₂)  [g is monotonic]
      
Add inequalities:
      f(n₁) + g(n₁) ≤ f(n₂) + g(n₂)
      h(n₁) ≤ h(n₂)  ✓
```

**Key insight:** Monotonicity is preserved under addition and composition, but be careful with subtraction!

---

### Type 2: Floor/Ceiling Arithmetic (Problem 3.3-2)

**What it asks:** Prove ⌊αn⌋ + ⌈(1-α)n⌉ = n

**Recognition pattern:**
- Floor ⌊x⌋ = largest integer ≤ x
- Ceiling ⌈x⌉ = smallest integer ≥ x
- Involves splitting n into two parts

**Mental model:**
- Floor "rounds down", ceiling "rounds up"
- The fractional parts must cancel out

**Solution approach:**
1. Write n = ⌊n⌋ + {n} where {n} is the fractional part
2. Apply floor/ceiling definitions
3. Show fractional parts sum to 0 or 1
4. Use the property: ⌊x⌋ + ⌈y⌉ = ⌊x+y⌋ + 1 if {x} + {y} ≥ 1

**Key insight:** 
```
⌊αn⌋ + ⌈(1-α)n⌉ = ⌊αn⌋ + ⌈n - αn⌉
                  = ⌊αn⌋ + n - ⌊αn⌋  [ceiling and floor cancel]
                  = n
```

---

### Type 3: Asymptotic Notation with Polynomials (Problem 3.3-3)

**What it asks:** Show (n + o(n))^k = Θ(n^k)

**Recognition pattern:**
- Little-o notation: o(n) means "grows slower than n"
- Polynomial expressions with asymptotic terms
- Need to prove Θ (tight bound)

**Mental model:**
- o(n) is negligible compared to n
- When you raise (n + tiny) to a power, the tiny part stays tiny

**Solution approach:**
1. Expand using binomial theorem (or just reason about dominance)
2. Show the o(n) term doesn't affect the leading term
3. Prove both upper bound (O) and lower bound (Ω)

**Example:**
```
(n + o(n))^k = (n(1 + o(1)))^k    [factor out n]
             = n^k · (1 + o(1))^k
             = n^k · (1 + o(1))    [constant power doesn't change o(1)]
             = n^k + o(n^k)
             = Θ(n^k)              [o(n^k) is absorbed]
```

**Key insight:** Lower-order terms don't matter for asymptotic bounds!

---

### Type 4: Proving Asymptotic Equations (Problem 3.3-4)

**What it asks:** Prove specific equations from the textbook

**Recognition pattern:**
- References equation numbers (3.21, 3.26-3.28)
- Usually involves logs, exponentials, or factorials

**Common equations to know:**
```
lg(Θ(n)) = Θ(lg n)
lg(n!) = Θ(n lg n)
n! = o(n^n)
n! = ω(2^n)
lg(lg n) = o(lg n)
```

**Solution approach:**
1. Look up the equation in the textbook
2. Use definitions of Θ, O, Ω, o, ω
3. Find constants c₁, c₂, n₀ that satisfy the definition

**Example: lg(Θ(n)) = Θ(lg n)**
```
Let f(n) ∈ Θ(n)
Then: c₁n ≤ f(n) ≤ c₂n for n ≥ n₀

Take logs:
lg(c₁n) ≤ lg(f(n)) ≤ lg(c₂n)
lg c₁ + lg n ≤ lg(f(n)) ≤ lg c₂ + lg n

For large n, the constants lg c₁, lg c₂ are absorbed:
lg(f(n)) = Θ(lg n)  ✓
```

---

### Type 5: Polynomial Bounding (Problem 3.3-5)

**What it asks:** Is ⌊lg n⌋! polynomially bounded?

**Recognition pattern:**
- "Polynomially bounded" means f(n) = O(n^k) for some k
- Usually involves factorials or iterated logs

**Mental model:**
- Polynomially bounded = grows no faster than some polynomial
- Factorials grow faster than any polynomial
- But factorials of logs might be different!

**Solution approach:**
1. Understand what "polynomially bounded" means: ∃k, c, n₀: f(n) ≤ c·n^k
2. Estimate the growth rate of the function
3. Compare to polynomial growth

**Example: Is ⌊lg n⌋! polynomially bounded?**
```
⌊lg n⌋! = 1 · 2 · 3 · ... · ⌊lg n⌋

How big is this?
- ⌊lg n⌋ ≈ log₂ n
- So we're computing (log₂ n)!

Using Stirling's approximation:
k! ≈ (k/e)^k · √(2πk)

So: (lg n)! ≈ (lg n / e)^(lg n)
           = (lg n)^(lg n) / e^(lg n)
           = (lg n)^(lg n) / n^(lg e)

Is this O(n^k) for some k?
- (lg n)^(lg n) grows faster than any polynomial in lg n
- But it's still subpolynomial in n!

Actually: (lg n)! = 2^(Θ(lg n · lg lg n))
This is NOT polynomially bounded because it's superpolynomial.

Answer: NO, ⌊lg n⌋! is NOT polynomially bounded.
```

**Key insight:** Factorials grow extremely fast, even factorials of logs!

---

### Type 6: Comparing Iterated Functions (Problem 3.3-6)

**What it asks:** Which is larger: lg(lg* n) or lg*(lg n)?

**Recognition pattern:**
- Iterated logarithm: lg* n = number of times you apply lg to get to 1
- Composition vs. iteration

**Mental model:**
- lg* n grows VERY slowly (inverse Ackermann-like)
- lg(lg* n) = log of a tiny number
- lg*(lg n) = iterate on a smaller starting point

**Solution approach:**
1. Compute concrete values for small n
2. Reason about growth rates
3. Determine which dominates asymptotically

**Example:**
```
Let's compute for n = 2^16 = 65536:

lg n = 16
lg* n = 5  (because lg* 65536 = 5)

lg(lg* n) = lg 5 ≈ 2.32

lg*(lg n) = lg* 16 = 4

So lg*(lg n) > lg(lg* n) for this n.

As n → ∞:
- lg* n grows to infinity (but VERY slowly)
- lg(lg* n) also grows to infinity
- lg*(lg n) = lg* n - 1  (approximately)

Therefore: lg*(lg n) is asymptotically larger.
```

**Key insight:** Iteration (lg*) grows faster than composition (lg of lg*)!

---

### Type 7: Golden Ratio & Recurrences (Problems 3.3-7, 3.3-8)

**What it asks:** Prove properties of φ and Fibonacci formula

**Recognition pattern:**
- Golden ratio φ = (1 + √5) / 2
- Fibonacci numbers
- Characteristic equations

**Mental model:**
- Fibonacci recurrence: Fₙ = Fₙ₋₁ + Fₙ₋₂
- Characteristic equation: x² = x + 1
- φ and φ̂ are the two roots

**Solution approach (3.3-7):**
1. Write characteristic equation: x² - x - 1 = 0
2. Apply quadratic formula
3. Verify by direct substitution

**Solution approach (3.3-8):**
1. Use strong induction (two base cases)
2. Base cases: F₀ = 0, F₁ = 1
3. Inductive step: Use φ² = φ + 1 property
4. Conclude by induction

**Key insight:** The property φ² = φ + 1 is the bridge between the recurrence and the closed form!

---

### Type 8: Logarithmic Implications (Problem 3.3-9)

**What it asks:** Show k lg k = Θ(n) implies k = Θ(n/lg n)

**Recognition pattern:**
- Solving for a variable in asymptotic notation
- Involves logarithms
- "Implies" means derive one bound from another

**Mental model:**
- If k lg k ≈ n, then k ≈ n / lg k
- But lg k ≈ lg(n/lg n) ≈ lg n - lg lg n ≈ lg n
- So k ≈ n / lg n

**Solution approach:**
1. Start with k lg k = Θ(n)
2. Solve for k approximately
3. Substitute back to verify
4. Use asymptotic notation properties

**Example:**
```
Given: k lg k = Θ(n)

This means: c₁n ≤ k lg k ≤ c₂n

Divide by lg k:
c₁n / lg k ≤ k ≤ c₂n / lg k

So: k = Θ(n / lg k)

Now, what is lg k?
From k lg k = Θ(n), we have k = Θ(n / lg k)
So: lg k = lg(Θ(n / lg k)) = Θ(lg(n / lg k))
         = Θ(lg n - lg lg k)
         = Θ(lg n)  [since lg lg k = o(lg n)]

Therefore: k = Θ(n / lg k) = Θ(n / lg n)  ✓
```

**Key insight:** When solving for variables in asymptotic notation, iterate to find consistency!

---

## 🧠 Universal Problem-Solving Framework

### Step 1: Identify the Problem Type
- Read the problem carefully
- Match to one of the 8 types above
- Note key words: "prove", "show", "which is larger", "bounded"

### Step 2: Recall the Relevant Definitions
- Asymptotic notation: Θ, O, Ω, o, ω
- Function properties: monotonicity, composition, limits
- Special functions: factorials, logs, exponentials

### Step 3: Choose Your Proof Technique
- **Direct proof:** Use definitions and algebra
- **Induction:** For recursive/sequential statements
- **Contradiction:** Assume opposite and derive absurdity
- **Limit comparison:** Take lim(n→∞) f(n)/g(n)

### Step 4: Write the Proof
- State what you're proving clearly
- Show each step with justification
- Use proper mathematical notation
- Conclude explicitly

### Step 5: Verify with Examples
- Plug in concrete values (n = 10, 100, 1000)
- Check edge cases (n = 1, n = 2)
- Ensure your answer makes intuitive sense

---

## 📚 Essential Definitions & Properties

### Asymptotic Notation (The Big 5)

**Θ-notation (Theta): Tight bound**
```
f(n) = Θ(g(n)) ⟺ ∃c₁, c₂, n₀: 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n) for all n ≥ n₀
```
Meaning: f grows at the same rate as g (sandwiched between two multiples)

**O-notation (Big-O): Upper bound**
```
f(n) = O(g(n)) ⟺ ∃c, n₀: 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀
```
Meaning: f grows no faster than g

**Ω-notation (Omega): Lower bound**
```
f(n) = Ω(g(n)) ⟺ ∃c, n₀: 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀
```
Meaning: f grows at least as fast as g

**o-notation (little-o): Strict upper bound**
```
f(n) = o(g(n)) ⟺ lim(n→∞) f(n)/g(n) = 0
```
Meaning: f grows strictly slower than g

**ω-notation (little-omega): Strict lower bound**
```
f(n) = ω(g(n)) ⟺ lim(n→∞) f(n)/g(n) = ∞
```
Meaning: f grows strictly faster than g

### Key Relationships
```
f(n) = Θ(g(n)) ⟺ f(n) = O(g(n)) AND f(n) = Ω(g(n))
f(n) = o(g(n)) ⟹ f(n) = O(g(n))
f(n) = ω(g(n)) ⟹ f(n) = Ω(g(n))
```

---

### Growth Rate Hierarchy (Slowest to Fastest)

```
1 < lg lg n < lg n < (lg n)² < √n < n < n lg n < n² < n³ < 2ⁿ < n! < nⁿ
```

**Memorize this!** It's the foundation for comparing functions.

**Special cases:**
- lg* n (iterated log) grows slower than lg lg n
- (lg n)! is between n and 2ⁿ
- Fibonacci grows like φⁿ where φ ≈ 1.618

---

### Logarithm Properties (Critical for Chapter 3.3)

```
lg(ab) = lg a + lg b
lg(a/b) = lg a - lg b
lg(aᵇ) = b lg a
lg(1/a) = -lg a
lg 1 = 0
lg n! = Θ(n lg n)  [Stirling's approximation]
```

**Change of base:**
```
logₐ n = (lg n) / (lg a)
```

**Iterated logarithm:**
```
lg* n = min{i ≥ 0 : lg⁽ⁱ⁾ n ≤ 1}
```
Where lg⁽ⁱ⁾ means apply lg i times.

---

### Factorial Approximations

**Stirling's approximation:**
```
n! = √(2πn) · (n/e)ⁿ · (1 + Θ(1/n))
```

**Asymptotic bounds:**
```
n! = ω(2ⁿ)     [factorial grows faster than exponential]
n! = o(nⁿ)     [factorial grows slower than power tower]
lg(n!) = Θ(n lg n)
```

---

### Golden Ratio Properties

**Definition:**
```
φ = (1 + √5) / 2 ≈ 1.618
φ̂ = (1 - √5) / 2 ≈ -0.618
```

**Key property:**
```
φ² = φ + 1
φ̂² = φ̂ + 1
```

**Binet's formula:**
```
Fₙ = (φⁿ - φ̂ⁿ) / √5
```

**Asymptotic behavior:**
```
Fₙ = Θ(φⁿ)
```

---

## 🎓 Exam Strategy: How to Approach Chapter 3.3 Problems

### Before the Exam
1. **Memorize the growth hierarchy** (1 < lg lg n < lg n < ... < nⁿ)
2. **Know the Big 5 definitions** (Θ, O, Ω, o, ω)
3. **Practice limit comparisons** (lim f(n)/g(n))
4. **Review logarithm properties** (product, quotient, power rules)
5. **Understand proof templates** (induction, direct, contradiction)

### During the Exam
1. **Read carefully** - identify the problem type
2. **Write down definitions** - don't try to remember everything
3. **Start with what you know** - use given information
4. **Show your work** - partial credit is real
5. **Check your answer** - plug in n = 10 or n = 100

### Time Management
- **Easy problems (3.3-1, 3.3-2):** 5-7 minutes each
- **Medium problems (3.3-3, 3.3-4, 3.3-9):** 10-15 minutes each
- **Hard problems (3.3-5, 3.3-6, 3.3-7, 3.3-8):** 15-20 minutes each

### Common Mistakes to Avoid
1. **Confusing O with Θ** - O is upper bound, Θ is tight bound
2. **Forgetting base cases** - induction needs them!
3. **Ignoring constants** - they matter for definitions, not for final answers
4. **Mixing up lg and ln** - lg is log₂, ln is logₑ
5. **Assuming without proof** - justify every step

---

## 🔥 Quick Reference: Problem-Solving Checklist

### For Monotonicity Problems
- [ ] Write down the definition of monotonically increasing
- [ ] Consider two arbitrary points n₁ < n₂
- [ ] Use algebra to show f(n₁) ≤ f(n₂)
- [ ] State conclusion clearly

### For Asymptotic Notation Problems
- [ ] Identify which notation is being used (Θ, O, Ω, o, ω)
- [ ] Write down the formal definition
- [ ] Find the constants c, c₁, c₂, n₀
- [ ] Verify the inequality holds for all n ≥ n₀

### For Comparison Problems
- [ ] Compute lim(n→∞) f(n)/g(n)
- [ ] If limit = 0: f = o(g)
- [ ] If limit = c > 0: f = Θ(g)
- [ ] If limit = ∞: f = ω(g)

### For Induction Problems
- [ ] State what you're proving (P(n))
- [ ] Prove base case(s)
- [ ] State inductive hypothesis (assume P(k))
- [ ] Prove inductive step (show P(k+1))
- [ ] Conclude by induction

### For Logarithm Problems
- [ ] Apply log properties (product, quotient, power)
- [ ] Simplify step by step
- [ ] Check if you need change of base
- [ ] Verify with a concrete example

---

## 💡 Intuition Builders: Why These Concepts Matter

### Why Asymptotic Notation?
- **Real-world impact:** Tells you if your algorithm will scale
- **Simplifies analysis:** Ignore constants and low-order terms
- **Universal language:** Every CS paper uses this notation

### Why Growth Hierarchies?
- **Algorithm comparison:** Which algorithm is faster for large n?
- **Trade-off analysis:** Is O(n log n) worth the extra complexity over O(n²)?
- **Practical limits:** n! algorithms are infeasible for n > 20

### Why Recurrence Relations?
- **Divide-and-conquer:** Merge sort, quick sort, binary search
- **Dynamic programming:** Fibonacci, knapsack, shortest paths
- **Closed-form solutions:** Binet's formula avoids recursion

### Why Logarithms?
- **Binary search:** O(lg n) is why search is so fast
- **Tree heights:** Balanced trees have height O(lg n)
- **Bit complexity:** lg n bits needed to represent n

---

## 🚀 Practice Problems: Test Your Understanding

### Warm-up (5 minutes each)
1. Is 2ⁿ⁺¹ = O(2ⁿ)? Why or why not?
2. Rank these functions: n², 2ⁿ, n lg n, lg n, n!
3. True or false: n² = O(n³)?
4. True or false: n³ = Θ(n²)?
5. Compute lg* 65536

### Medium (10 minutes each)
6. Prove: If f(n) = O(g(n)) and g(n) = O(h(n)), then f(n) = O(h(n))
7. Show that (lg n)! is not polynomially bounded
8. Prove: n lg n = o(n²)
9. Is √(lg n) = o(lg n)? Prove it.
10. Solve for k: k² lg k = Θ(n)

### Hard (15-20 minutes each)
11. Prove: If f(n) and g(n) are monotonically increasing, then f(g(n)) is monotonically increasing
12. Show that Σᵢ₌₁ⁿ i² = Θ(n³)
13. Prove Binet's formula using induction
14. Compare: lg(n!) vs. n lg n
15. Is (lg n)^(lg n) polynomially bounded?

---

## 📖 Textbook Equation Reference

### Equation 3.14 (Binomial Expansion)
```
(x + y)ⁿ = Σₖ₌₀ⁿ (n choose k) xᵏ yⁿ⁻ᵏ
```

### Equation 3.21 (Stirling's Approximation)
```
n! = √(2πn) (n/e)ⁿ (1 + Θ(1/n))
```

### Equations 3.26-3.28 (Logarithm Bounds)
```
lg(n!) = Θ(n lg n)          [3.26]
n! = o(nⁿ)                  [3.27]
n! = ω(2ⁿ)                  [3.28]
```

---

## 🎯 Final Checklist: Are You Ready?

### Conceptual Understanding
- [ ] I can explain what Θ, O, Ω, o, ω mean in plain English
- [ ] I understand the growth hierarchy (1 < lg n < n < n² < 2ⁿ < n!)
- [ ] I know when to use induction vs. direct proof
- [ ] I can compare two functions using limits

### Technical Skills
- [ ] I can manipulate logarithms (product, quotient, power rules)
- [ ] I can apply asymptotic notation definitions
- [ ] I can prove monotonicity properties
- [ ] I can solve recurrence relations

### Problem-Solving
- [ ] I can identify problem types from the question
- [ ] I know which proof technique to use
- [ ] I can verify my answers with examples
- [ ] I can manage my time during the exam

### Resources
- [ ] I have reviewed all homework problems
- [ ] I have practiced with textbook exercises
- [ ] I have created my own cheat sheet
- [ ] I have studied with classmates

---

## 🔗 Connections to Other Topics

### Chapter 2 (Divide and Conquer)
- Recurrence relations → Asymptotic analysis
- Merge sort: T(n) = 2T(n/2) + Θ(n) → T(n) = Θ(n lg n)

### Chapter 4 (Recurrences)
- Master theorem uses asymptotic notation
- Fibonacci recurrence → Golden ratio

### Chapter 7 (Quicksort)
- Average case: Θ(n lg n)
- Worst case: Θ(n²)

### Chapter 15 (Dynamic Programming)
- Fibonacci: exponential → linear with memoization
- Asymptotic analysis guides optimization

---

## 💪 Confidence Builders: You Got This!

### What You Already Know
- You've solved 3.3-7 and 3.3-8 (golden ratio, Binet's formula)
- You understand induction (strong and weak)
- You can manipulate algebraic expressions
- You know basic calculus (limits)

### What You're Learning
- How to formalize your intuition about "faster" and "slower"
- How to prove mathematical statements rigorously
- How to analyze algorithms systematically
- How to think like a computer scientist

### What You'll Be Able to Do
- Analyze any algorithm's running time
- Compare algorithms objectively
- Design efficient solutions
- Ace your midterm! 🎉

---

**Remember:** Asymptotic analysis is a tool for understanding scalability. Don't just memorize—understand the *why* behind each concept. Good luck on your midterm! 🚀

---

**End of Guide**
