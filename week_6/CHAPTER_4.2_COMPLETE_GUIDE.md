# Chapter 4.2 Complete Guide: Strassen's Algorithm

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 4.2 - Strassen's Algorithm for Matrix Multiplication  
**Purpose:** Master the first algorithm to beat Θ(n³) for matrix multiplication

---

## 🎯 What Chapter 4.2 Is Really About

### The Big Picture

Chapter 4.2 presents **one of the most remarkable algorithms in computer science**: Strassen's algorithm, which breaks the Θ(n³) barrier for matrix multiplication.

**Historical context:**
- Before 1969: Everyone thought Θ(n³) was optimal
- 1969: Volker Strassen publishes his algorithm
- Result: Θ(n^2.807) time - asymptotically faster!
- Impact: Showed that "obvious" complexity isn't always optimal

**Mental model:** This is about **trading expensive operations for cheap ones**
- Expensive: Matrix multiplication (Θ(n³))
- Cheap: Matrix addition (Θ(n²))
- Trade-off: Use 7 multiplications + 18 additions instead of 8 multiplications + 4 additions

---

## 🔑 The Core Insight

### Why Fewer Multiplications Matter

**Simple analogy:** Computing x² - y²

**Method 1 (obvious):**
```
Compute x²       (1 multiplication)
Compute y²       (1 multiplication)
Subtract         (1 subtraction)
Total: 2 multiplications, 1 subtraction
```

**Method 2 (clever):**
```
Use algebra: x² - y² = (x+y)(x-y)
Compute x+y      (1 addition)
Compute x-y      (1 subtraction)
Multiply         (1 multiplication)
Total: 1 multiplication, 2 additions
```

**For scalars:** Not much difference (3 operations either way)

**For matrices:** HUGE difference!
- Matrix multiplication: Θ(n³)
- Matrix addition: Θ(n²)
- Trading multiplication for addition is worth it!

---

## 📊 Standard vs Strassen Comparison

### Standard Divide-and-Conquer (from 4.1)

**Formulas:**
```
C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
C₁₂ = A₁₁·B₁₂ + A₁₂·B₂₂
C₂₁ = A₂₁·B₁₁ + A₂₂·B₂₁
C₂₂ = A₂₁·B₁₂ + A₂₂·B₂₂
```

**Operations:**
- **8 multiplications** (2 per equation)
- **4 additions** (1 per equation)

**Recurrence:** T(n) = 8T(n/2) + Θ(n²)
**Solution:** T(n) = Θ(n³)

---

### Strassen's Algorithm

**The 7 products:**
```
P₁ = A₁₁·(B₁₂ - B₂₂)
P₂ = (A₁₁ + A₁₂)·B₂₂
P₃ = (A₂₁ + A₂₂)·B₁₁
P₄ = A₂₂·(B₂₁ - B₁₁)
P₅ = (A₁₁ + A₂₂)·(B₁₁ + B₂₂)
P₆ = (A₁₂ - A₂₂)·(B₂₁ + B₂₂)
P₇ = (A₁₁ - A₂₁)·(B₁₁ + B₁₂)
```

**Combine to get C:**
```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

**Operations:**
- **7 multiplications** (one per P)
- **18 additions/subtractions** (10 for S matrices, 8 for combining)

**Recurrence:** T(n) = 7T(n/2) + Θ(n²)
**Solution:** T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

---

## 🧮 Why Strassen's Algorithm Works

### The Mathematics Behind It

**Key question:** How did Strassen find these formulas?

**Answer:** Algebraic manipulation and clever observation

**Verification (for C₁₁):**

Standard formula:
```
C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁
```

Strassen's formula:
```
C₁₁ = P₅ + P₄ - P₂ + P₆
```

**Expanding P₅, P₄, P₂, P₆:**
```
P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
   = A₁₁·B₁₁ + A₁₁·B₂₂ + A₂₂·B₁₁ + A₂₂·B₂₂

P₄ = A₂₂(B₂₁ - B₁₁)
   = A₂₂·B₂₁ - A₂₂·B₁₁

P₂ = (A₁₁ + A₁₂)B₂₂
   = A₁₁·B₂₂ + A₁₂·B₂₂

P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
   = A₁₂·B₂₁ + A₁₂·B₂₂ - A₂₂·B₂₁ - A₂₂·B₂₂
```

**Now compute C₁₁ = P₅ + P₄ - P₂ + P₆:**
```
C₁₁ = (A₁₁·B₁₁ + A₁₁·B₂₂ + A₂₂·B₁₁ + A₂₂·B₂₂)    [P₅]
    + (A₂₂·B₂₁ - A₂₂·B₁₁)                        [P₄]
    - (A₁₁·B₂₂ + A₁₂·B₂₂)                        [-P₂]
    + (A₁₂·B₂₁ + A₁₂·B₂₂ - A₂₂·B₂₁ - A₂₂·B₂₂)    [P₆]
```

**Collect terms (cancel what cancels):**
```
A₁₁·B₁₁: +1 (from P₅)                           = +A₁₁·B₁₁
A₁₁·B₂₂: +1 (from P₅) -1 (from P₂)              = 0
A₂₂·B₁₁: +1 (from P₅) -1 (from P₄)              = 0
A₂₂·B₂₂: +1 (from P₅) -1 (from P₆)              = 0
A₂₂·B₂₁: +1 (from P₄) -1 (from P₆)              = 0
A₁₂·B₂₂: -1 (from P₂) +1 (from P₆)              = 0
A₁₂·B₂₁: +1 (from P₆)                           = +A₁₂·B₂₁
```

**Result:**
```
C₁₁ = A₁₁·B₁₁ + A₁₂·B₂₁ ✓
```

**This matches the standard formula!** The magic is that most terms cancel out.

---

## 🎓 The Four-Step Algorithm

### Step 1: Base Case and Partition

**If n = 1:**
- Just multiply two scalars
- Return immediately
- Time: Θ(1)

**If n > 1:**
- Partition A, B, C into four (n/2)×(n/2) submatrices
- Time: Θ(1) with index calculation

---

### Step 2: Create Temporary Matrices

**Create 10 S matrices (sums/differences):**
```
S₁ = B₁₂ - B₂₂
S₂ = A₁₁ + A₁₂
S₃ = A₂₁ + A₂₂
S₄ = B₂₁ - B₁₁
S₅ = A₁₁ + A₂₂
S₆ = B₁₁ + B₂₂
S₇ = A₁₂ - A₂₂
S₈ = B₂₁ + B₂₂
S₉ = A₁₁ - A₂₁
S₁₀ = B₁₁ + B₁₂
```

**Cost:** 10 matrix additions/subtractions of (n/2)×(n/2) matrices
- Each operation: Θ((n/2)²) = Θ(n²/4)
- Total: 10 × Θ(n²/4) = Θ(n²)

**Also create 7 P matrices (initialized to zero):**
- Time: Θ(n²)

**Total for Step 2:** Θ(n²)

---

### Step 3: Compute Seven Products

**Recursively compute:**
```
P₁ = A₁₁ × S₁
P₂ = S₂ × B₂₂
P₃ = S₃ × B₁₁
P₄ = A₂₂ × S₄
P₅ = S₅ × S₆
P₆ = S₇ × S₈
P₇ = S₉ × S₁₀
```

**Cost:** 7 recursive calls on (n/2)×(n/2) matrices
- Time: 7T(n/2)

**Key:** Only 7 multiplications, not 8!

---

### Step 4: Combine Results

**Compute C submatrices:**
```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

**Cost:** 8 additions/subtractions of (n/2)×(n/2) matrices
- Total: 8 × Θ(n²/4) = Θ(n²)

---

### Total Time Analysis

**Recurrence:**
```
T(n) = 7T(n/2) + Θ(n²)

Where:
- 7T(n/2): Step 3 (seven recursive multiplications)
- Θ(n²): Steps 1, 2, 4 (partition + create temps + combine)
```

**Solution (Master Theorem):**
```
a = 7, b = 2, f(n) = Θ(n²)
n^(log₂ 7) ≈ n^2.807

f(n) = n² < n^2.807 (polynomially smaller)
Case 1: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
```

---

## 💡 Key Insights

### Why 7 Instead of 8 Makes a Difference

**Recursion tree comparison:**

**Standard (8 subproblems):**
```
Level 0: 1 problem,  cost n²
Level 1: 8 problems, cost 2n²
Level 2: 64 problems, cost 4n²
...
Leaves: 8^(lg n) = n³ leaves
Total: Θ(n³)
```

**Strassen (7 subproblems):**
```
Level 0: 1 problem,  cost n²
Level 1: 7 problems, cost (7/4)n²
Level 2: 49 problems, cost (49/16)n²
...
Leaves: 7^(lg n) = n^(lg 7) ≈ n^2.807 leaves
Total: Θ(n^2.807)
```

**The difference:**
- 8^(lg n) = (2³)^(lg n) = 2^(3 lg n) = (2^(lg n))³ = n³
- 7^(lg n) = n^(lg 7) ≈ n^2.807

**Key insight:** Reducing subproblems from 8 to 7 changes the exponent from 3 to 2.807!

---

### Trade-off: Multiplications vs Additions

**Standard algorithm:**
- 8 multiplications (expensive)
- 4 additions (cheap)
- Total: dominated by multiplications

**Strassen's algorithm:**
- 7 multiplications (expensive, but one fewer!)
- 18 additions (cheap, but many more)
- Total: still dominated by multiplications, but fewer of them!

**Why this works:**
- Addition is Θ(n²), multiplication is Θ(n³)
- For large n, n³ >> n²
- So reducing multiplications is worth increasing additions

**Numerical example (n = 1000):**
- Standard: 8 × 10⁹ operations
- Strassen: 7 × 10⁹ operations + 18 × 10⁶ operations
- Savings: ~1 billion operations!

---

## 🎯 Problem-Solving Framework

### Problem Type 1: Compute Using Strassen (Exercise 4.2-1)

**What it's asking:**
Execute Strassen's algorithm manually on small matrices

**Framework:**
1. Partition matrices into submatrices
2. Compute 7 products P₁ through P₇
3. Combine products to get C₁₁, C₁₂, C₂₁, C₂₂
4. Assemble final result
5. Verify with standard multiplication

**Key skill:** Following the formulas exactly, careful arithmetic

---

### Problem Type 2: Write Pseudocode (Exercise 4.2-2)

**What it's asking:**
Write clear pseudocode for Strassen's algorithm

**Framework:**
1. Base case (n = 1)
2. Partition step
3. Compute 7 products recursively
4. Combine results
5. Return assembled matrix

**Key skill:** Clear structure, proper recursion, correct formulas

---

### Problem Type 3: Generalize to k×k Base (Exercise 4.2-3)

**What it's asking:**
If we can multiply k×k matrices with m multiplications, what's the complexity for n×n?

**Framework:**
1. Understand the recurrence: T(n) = mT(n/k) + Θ(n²)
2. Solve using Master Theorem
3. Find condition for o(n^(lg 7))
4. Determine maximum k

**Key skill:** Recurrence manipulation, Master Theorem application

---

### Problem Type 4: Compare Algorithms (Exercise 4.2-4)

**What it's asking:**
Given different base case algorithms, which is best asymptotically?

**Framework:**
1. Write recurrence for each approach
2. Solve each recurrence
3. Compare exponents
4. Determine winner

**Key skill:** Comparative analysis, exponent comparison

---

### Problem Type 5: Apply to Different Problem (Exercise 4.2-5)

**What it's asking:**
Use Strassen's insight for complex number multiplication

**Framework:**
1. Identify standard method (4 real multiplications)
2. Find algebraic trick to reduce multiplications
3. Write algorithm using 3 multiplications
4. Verify correctness

**Key skill:** Applying algorithmic insight to new domain

---

### Problem Type 6: Use Subroutine (Exercise 4.2-6)

**What it's asking:**
Given fast squaring algorithm, design fast multiplication

**Framework:**
1. Express multiplication in terms of squaring
2. Use identity: (A+B)² - (A-B)² = 4AB
3. Count operations
4. Determine complexity

**Key skill:** Reducing one problem to another

---

## 📚 The Complete Strassen's Algorithm

### Pseudocode (Concise Version)

```
STRASSEN-MULTIPLY(A, B, n)
1  if n == 1
2    return A[1,1] × B[1,1]
3  
4  // Partition
5  A₁₁, A₁₂, A₂₁, A₂₂ = partition A
6  B₁₁, B₁₂, B₂₁, B₂₂ = partition B
7  
8  // Compute 7 products
9  P₁ = STRASSEN-MULTIPLY(A₁₁, B₁₂ - B₂₂, n/2)
10 P₂ = STRASSEN-MULTIPLY(A₁₁ + A₁₂, B₂₂, n/2)
11 P₃ = STRASSEN-MULTIPLY(A₂₁ + A₂₂, B₁₁, n/2)
12 P₄ = STRASSEN-MULTIPLY(A₂₂, B₂₁ - B₁₁, n/2)
13 P₅ = STRASSEN-MULTIPLY(A₁₁ + A₂₂, B₁₁ + B₂₂, n/2)
14 P₆ = STRASSEN-MULTIPLY(A₁₂ - A₂₂, B₂₁ + B₂₂, n/2)
15 P₇ = STRASSEN-MULTIPLY(A₁₁ - A₂₁, B₁₁ + B₁₂, n/2)
16 
17 // Combine
18 C₁₁ = P₅ + P₄ - P₂ + P₆
19 C₁₂ = P₁ + P₂
20 C₂₁ = P₃ + P₄
21 C₂₂ = P₅ + P₁ - P₃ - P₇
22 
23 return assemble(C₁₁, C₁₂, C₂₁, C₂₂)
```

---

### Memory Aid for the Formulas

**The 7 Products (pattern recognition):**

**P₁-P₄: Single submatrix from A or B**
```
P₁ = A₁₁ × (B₁₂ - B₂₂)    [A₁₁ alone]
P₂ = (A₁₁ + A₁₂) × B₂₂    [B₂₂ alone]
P₃ = (A₂₁ + A₂₂) × B₁₁    [B₁₁ alone]
P₄ = A₂₂ × (B₂₁ - B₁₁)    [A₂₂ alone]
```

**P₅-P₇: Diagonal sums**
```
P₅ = (A₁₁ + A₂₂) × (B₁₁ + B₂₂)    [main diagonal]
P₆ = (A₁₂ - A₂₂) × (B₂₁ + B₂₂)    [off-diagonal]
P₇ = (A₁₁ - A₂₁) × (B₁₁ + B₁₂)    [off-diagonal]
```

**Combining (pattern):**
```
C₁₁ = P₅ + P₄ - P₂ + P₆    [complex]
C₁₂ = P₁ + P₂              [simple: just 2 terms]
C₂₁ = P₃ + P₄              [simple: just 2 terms]
C₂₂ = P₅ + P₁ - P₃ - P₇    [complex]
```

**Mnemonic:** The diagonal elements (C₁₁, C₂₂) have complex formulas; off-diagonal (C₁₂, C₂₁) are simple.

---

## 📊 Complexity Analysis Deep Dive

### Recurrence Derivation

**Step 1 (Partition):** Θ(1) with index calculation

**Step 2 (Create S matrices):**
- 10 additions/subtractions of (n/2)×(n/2) matrices
- Cost: 10 × Θ(n²/4) = Θ(n²)

**Step 3 (Compute P matrices):**
- 7 recursive multiplications
- Cost: 7T(n/2)

**Step 4 (Combine):**
- 8 additions/subtractions for C submatrices
- Cost: 8 × Θ(n²/4) = Θ(n²)

**Total non-recursive work:**
```
Θ(1) + Θ(n²) + Θ(n²) = Θ(n²)
```

**Recurrence:**
```
T(n) = 7T(n/2) + Θ(n²)
```

---

### Solving with Master Theorem

**Form:** T(n) = aT(n/b) + f(n)

**Parameters:**
- a = 7 (subproblems)
- b = 2 (size reduction factor)
- f(n) = Θ(n²) (non-recursive work)

**Calculate critical exponent:**
```
log_b a = log₂ 7 = 2.8073549...
n^(log_b a) = n^2.807
```

**Compare f(n) with n^(log_b a):**
```
f(n) = n²
n^(log_b a) = n^2.807

n² < n^2.807 (polynomially smaller)
```

**Determine case:**
Is f(n) = O(n^(log_b a - ε)) for some ε > 0?
```
n² = O(n^(2.807 - ε))
Take ε = 0.5: n² = O(n^2.307) ✓
```

**Case 1 applies:**
```
T(n) = Θ(n^(log_b a)) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
```

---

### Comparison with Standard Algorithms

| Algorithm | Multiplications | Additions | Recurrence | Solution |
|-----------|----------------|-----------|------------|----------|
| Naive | n³ | n³ | - | Θ(n³) |
| Standard D&C | 8 per level | 4 per level | 8T(n/2) + Θ(n²) | Θ(n³) |
| Strassen | 7 per level | 18 per level | 7T(n/2) + Θ(n²) | Θ(n^2.807) |

**Speedup for large n:**
```
n³ / n^2.807 = n^0.193

For n = 1000: speedup ≈ 1000^0.193 ≈ 2.5×
For n = 10000: speedup ≈ 10000^0.193 ≈ 3.2×
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Number of Products
```
✗ "Need 8 products like standard algorithm"
✓ Strassen uses only 7 products!
```

### Mistake 2: Wrong Combination Formulas
```
✗ C₁₁ = P₁ + P₂ (too simple!)
✓ C₁₁ = P₅ + P₄ - P₂ + P₆ (correct)
```

### Mistake 3: Forgetting Additions Cost
```
✗ "18 additions are free"
✓ 18 additions take Θ(n²) time total
✓ But still cheaper than 8th multiplication
```

### Mistake 4: Thinking It's Always Better
```
✗ "Strassen always faster"
✓ Only for large n (overhead for small n)
✓ Practical crossover: n ≈ 100-1000
```

---

## 🚀 Practical Considerations

### When to Use Strassen

**Advantages:**
- Asymptotically faster: Θ(n^2.807) vs Θ(n³)
- Significant speedup for large matrices
- Theoretically elegant

**Disadvantages:**
- Higher constant factors (18 additions vs 4)
- More complex implementation
- Numerical stability issues (subtractions can amplify errors)
- Overhead not worth it for small n

**Practical cutoff:**
- Use naive algorithm for n < 100-1000
- Switch to Strassen for larger matrices
- Hybrid approach: Strassen at top levels, naive at bottom

---

### Modern Developments

**Even faster algorithms exist:**
- Coppersmith-Winograd (1990): Θ(n^2.376)
- Le Gall (2014): Θ(n^2.3728639)
- Theoretical lower bound: Ω(n²) (must read all inputs)
- Optimal exponent still unknown!

**But:**
- These algorithms have HUGE constants
- Only faster for astronomically large matrices
- Strassen is still practical for real use

---

**You're ready to master Chapter 4.2! 🎉**

---

**End of Guide**
