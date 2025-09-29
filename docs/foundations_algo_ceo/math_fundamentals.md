# Math Fundamentals for Algorithm Analysis

I'll break this down step-by-step, focusing on the algebra, calculus, and discrete math basics you need to solve recurrences and analyze algorithms. Since you're a busy CEO with no math background, I'll keep it simple, practical, and tied to real algorithm examples (like the Master Theorem). We'll build from basics to what's directly useful – no fluff.

Think of this as your "algorithm math toolkit." Most problems use 80% of these concepts; the rest is pattern recognition.

## 1. Algebra Fundamentals (The Building Blocks)
Algebra is about manipulating numbers and expressions. For algorithms, it's mostly exponents, logs, and polynomials – no solving for x needed.

### Exponents (Powers)
- **What it is:** n^k means multiply n by itself k times. E.g., 2^3 = 2×2×2=8.
- **Key rules:**
  - n^a × n^b = n^(a+b) (add exponents).
  - n^a / n^b = n^(a-b) (subtract exponents).
  - (n^a)^b = n^(a×b) (multiply exponents).
- **Why for algorithms:** Recurrences like T(n) = a T(n/b) involve n^(log_b a), which is your "growth rate."
- **Example in action:** n^(log₄2) = n^0.5 = √n. This tells you how your "teams" scale in divide-and-conquer.
- **Practice:** Calculate 2^4 = 16, 3^2 = 9, 10^0 = 1.

### Logarithms (Logs)
- **What it is:** Log_b a asks: "What power raises b to get a?" E.g., log₂ 8 = 3 because 2^3=8.
- **Key rules:**
  - Log_b (x×y) = log_b x + log_b y (logs add for multiplication).
  - Log_b (x/y) = log_b x - log_b y.
  - Log_b (x^k) = k × log_b x.
  - Change of base: log_b a = log_c a / log_c b.
- **Why for algorithms:** Central to Master Theorem – log_b a measures "branching efficiency."
- **Common logs in algorithms:**
  - log₂ n (binary, like halving in binary search).
  - log₁₀ n (common, but less used in CS).
- **Example in action:** log₄ 2 = 0.5 because 4^0.5=2. This leads to √n growth.
- **Practice:** Compute log₂ 16 = 4 (2^4=16), log₄ 2 = 0.5 (4^0.5=2).

### Polynomials
- **What it is:** Expressions like n^2 + 3n + 1 (linear terms + constants).
- **Why for algorithms:** f(n) in recurrences is often polynomial (e.g., n, n^2).
- **Basic ops:** Add/subtract like terms; multiply by distributing.

## 2. Discrete Math Fundamentals (Counting & Structures)
Discrete math deals with countable things – perfect for algorithms, where we count steps or sizes.

### Asymptotic Notation (Big O, Theta, Omega)
- **What it is:** Describes how functions grow as n gets huge (ignores constants).
  - **Big O (O):** "Grows at most this fast" – upper bound. E.g., O(n) means ≤ some constant × n.
  - **Big Theta (Θ):** "Grows exactly this fast" – tight bound. E.g., Θ(n log n) for merge sort.
  - **Big Omega (Ω):** "Grows at least this fast" – lower bound.
- **Why for algorithms:** Compare growth rates in Master Theorem cases.
- **Simple hierarchy (slowest to fastest):** Constants (1) < logs (log n) < roots (√n) < linear (n) < quadratic (n^2) < exponential (2^n).
- **Example:** n vs √n: n grows faster, so Case 3 in Master Theorem.

### Induction (Proving Patterns)
- **What it is:** Prove something true for all n by showing base case (n=1) + inductive step (assume n, prove n+1).
- **Why for algorithms:** Prove recurrences correct (e.g., T(n) = Θ(n log n) for merge sort).
- **Simple example:** Prove sum of first n numbers = n(n+1)/2.
  - Base: n=1, 1=1(2)/2=1.
  - Assume true for n, then n+1: n(n+1)/2 + (n+1) = (n+1)(n/2 +1) = (n+1)(n+2)/2.

### Recurrences (Self-Defining Equations)
- **What it is:** Equations like T(n) = 2T(n/2) + n (merge sort).
- **Why for algorithms:** Describe divide-and-conquer running time.
- **Basic solving:** Use Master Theorem for common forms; substitution for others.

## 3. Calculus Basics (Rates of Change)
Calculus helps understand growth – useful for asymptotic analysis, but you can skip derivatives if basic.

### Limits
- **What it is:** What happens to a function as n → ∞. E.g., lim (n→∞) (n/2) = ∞.
- **Why for algorithms:** Proves Big O/Theta. E.g., show n^2 / n = n → ∞, so n^2 grows faster.

### Derivatives (Optional for Beginners)
- **What it is:** Rate of change. Derivative of n^2 is 2n (slope).
- **Why for algorithms:** Understand growth rates (e.g., polynomial vs. exponential).
- **Simple rule:** Power rule – d/dn (n^k) = k n^(k-1).

## 4. Key Theorems and Formulas for Algorithms
These are the "cookbook" tools for solving recurrences.

### Master Theorem (Core for Divide-and-Conquer)
- **Formula:** For T(n) = a T(n/b) + f(n):
  - Case 1: f(n) = O(n^{log_b a - ε}) → T(n) = Θ(n^{log_b a}).
  - Case 2: f(n) = Θ(n^{log_b a} log^k n) → T(n) = Θ(n^{log_b a} log^{k+1} n).
  - Case 3: f(n) = Ω(n^{log_b a + ε}) and regularity → T(n) = Θ(f(n)).
- **Why you need it:** Solves 90% of algorithm recurrences.
- **Example:** T(n)=2T(n/4)+1 → log₄2=0.5, f(n)=1 < n^0.5 → Case 1 → Θ(√n).

### Logarithm Properties
- log_b 1 = 0.
- log_b b = 1.
- log_b (1/a) = -log_b a.

### Summations (For Loop Analysis)
- **Formula:** Sum_{i=1 to n} i = n(n+1)/2.
- **Geometric:** Sum_{i=0 to n} r^i = (r^{n+1}-1)/(r-1).

## How to Apply This to Solve Algorithms
1. **Identify the recurrence** from the algorithm (e.g., merge sort: T(n)=2T(n/2)+n).
2. **Compute log_b a** (e.g., log₂2=1).
3. **Compare f(n) to n^{log_b a}** using growth hierarchy.
4. **Pick Master Theorem case** and apply.
5. **Verify with small n** (e.g., n=4,8,16).

**Best Practice for CEOs:**  
- Memorize the 3 cases + growth hierarchy.  
- Practice 5-10 problems/week.  
- Use business analogies (teams vs. meetings).  
- Resources: Your hw_4.5.md file, "Introduction to Algorithms" (skim chapters 2-4).

This toolkit covers 95% of what you need. Start with exponents and logs – the rest builds on them. If you master these, solving recurrences becomes pattern matching! Let me know if you want examples for any part.
