# Homework Solutions: Section 4.2 - Strassen's Algorithm

**Course:** CS3112 - Introduction to Algorithms  
**Week:** 6  
**Section:** 4.2 (Strassen's Algorithm for Matrix Multiplication)  
**Date:** 2025-09-29

---

## Background: What is Strassen's Algorithm?

### The Problem with Standard Matrix Multiplication

**Standard divide-and-conquer (from Section 4.1):**
```
C₁₁ = A₁₁B₁₁ + A₁₂B₂₁  (2 multiplications, 1 addition)
C₁₂ = A₁₁B₁₂ + A₁₂B₂₂  (2 multiplications, 1 addition)
C₂₁ = A₂₁B₁₁ + A₂₂B₂₁  (2 multiplications, 1 addition)
C₂₂ = A₂₁B₁₂ + A₂₂B₂₂  (2 multiplications, 1 addition)

Total: 8 matrix multiplications
```

**Why 8 multiplications is bad:**
- Recurrence: T(n) = 8T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n³)
- No better than naive algorithm!

---

### Strassen's Brilliant Insight

**Key idea:** Trade multiplications for additions!
- Matrix multiplication is expensive: O(n³) for n×n matrices
- Matrix addition is cheap: O(n²) for n×n matrices
- Can we use more additions to reduce multiplications?

**Strassen's answer:** Yes! Use only **7 multiplications** instead of 8!

**The magic:**
- Compute 7 special products (called P₁, P₂, ..., P₇)
- Combine them with additions/subtractions to get C₁₁, C₁₂, C₂₁, C₂₂
- Recurrence becomes: T(n) = 7T(n/2) + Θ(n²)
- Solution: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
- **Faster than n³!**

---

### Strassen's Seven Products

**The 7 products (memorize these!):**
```
P₁ = A₁₁(B₁₂ - B₂₂)
P₂ = (A₁₁ + A₁₂)B₂₂
P₃ = (A₂₁ + A₂₂)B₁₁
P₄ = A₂₂(B₂₁ - B₁₁)
P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)
P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)
P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)
```

**How to compute C from P:**
```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

**Why these specific formulas?**
- Strassen discovered them through algebraic manipulation
- They're not intuitive - they're the result of clever math!
- The key is they work and use only 7 multiplications

---

## Problem 4.2-1: Compute Matrix Product Using Strassen's Algorithm

### Problem Statement
Use Strassen's algorithm to compute the matrix product:
```
[1  3]   [6  8]
[7  5] × [4  2]
```
Show your work.

---

## Solution: Step-by-Step Calculation

### Step 1: Identify the Submatrices

**Matrix A:**
```
A = [1  3]
    [7  5]
```

**Partition A into 1×1 submatrices:**
```
A₁₁ = [1]  (top-left)
A₁₂ = [3]  (top-right)
A₂₁ = [7]  (bottom-left)
A₂₂ = [5]  (bottom-right)
```

**Why 1×1 submatrices?**
- Original matrix is 2×2
- We divide by 2: 2/2 = 1
- So each submatrix is 1×1 (just a single number)

**Matrix B:**
```
B = [6  8]
    [4  2]
```

**Partition B:**
```
B₁₁ = [6]
B₁₂ = [8]
B₂₁ = [4]
B₂₂ = [2]
```

---

### Step 2: Compute the Seven Products P₁ through P₇

**Important:** For 1×1 matrices, matrix operations become scalar operations:
- Matrix multiplication → regular multiplication
- Matrix addition → regular addition
- Matrix subtraction → regular subtraction

---

#### Product P₁ = A₁₁(B₁₂ - B₂₂)

**Step 2.1.1: Compute B₁₂ - B₂₂**
```
B₁₂ - B₂₂ = 8 - 2 = 6
```

**Step 2.1.2: Multiply by A₁₁**
```
P₁ = A₁₁ × (B₁₂ - B₂₂)
   = 1 × 6
   = 6
```

**Result: P₁ = 6**

---

#### Product P₂ = (A₁₁ + A₁₂)B₂₂

**Step 2.2.1: Compute A₁₁ + A₁₂**
```
A₁₁ + A₁₂ = 1 + 3 = 4
```

**Step 2.2.2: Multiply by B₂₂**
```
P₂ = (A₁₁ + A₁₂) × B₂₂
   = 4 × 2
   = 8
```

**Result: P₂ = 8**

---

#### Product P₃ = (A₂₁ + A₂₂)B₁₁

**Step 2.3.1: Compute A₂₁ + A₂₂**
```
A₂₁ + A₂₂ = 7 + 5 = 12
```

**Step 2.3.2: Multiply by B₁₁**
```
P₃ = (A₂₁ + A₂₂) × B₁₁
   = 12 × 6
   = 72
```

**Result: P₃ = 72**

---

#### Product P₄ = A₂₂(B₂₁ - B₁₁)

**Step 2.4.1: Compute B₂₁ - B₁₁**
```
B₂₁ - B₁₁ = 4 - 6 = -2
```

**Step 2.4.2: Multiply by A₂₂**
```
P₄ = A₂₂ × (B₂₁ - B₁₁)
   = 5 × (-2)
   = -10
```

**Result: P₄ = -10**

---

#### Product P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂)

**Step 2.5.1: Compute A₁₁ + A₂₂**
```
A₁₁ + A₂₂ = 1 + 5 = 6
```

**Step 2.5.2: Compute B₁₁ + B₂₂**
```
B₁₁ + B₂₂ = 6 + 2 = 8
```

**Step 2.5.3: Multiply the results**
```
P₅ = (A₁₁ + A₂₂) × (B₁₁ + B₂₂)
   = 6 × 8
   = 48
```

**Result: P₅ = 48**

---

#### Product P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂)

**Step 2.6.1: Compute A₁₂ - A₂₂**
```
A₁₂ - A₂₂ = 3 - 5 = -2
```

**Step 2.6.2: Compute B₂₁ + B₂₂**
```
B₂₁ + B₂₂ = 4 + 2 = 6
```

**Step 2.6.3: Multiply the results**
```
P₆ = (A₁₂ - A₂₂) × (B₂₁ + B₂₂)
   = (-2) × 6
   = -12
```

**Result: P₆ = -12**

---

#### Product P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂)

**Step 2.7.1: Compute A₁₁ - A₂₁**
```
A₁₁ - A₂₁ = 1 - 7 = -6
```

**Step 2.7.2: Compute B₁₁ + B₁₂**
```
B₁₁ + B₁₂ = 6 + 8 = 14
```

**Step 2.7.3: Multiply the results**
```
P₇ = (A₁₁ - A₂₁) × (B₁₁ + B₁₂)
   = (-6) × 14
   = -84
```

**Result: P₇ = -84**

---

### Step 3: Summary of All Seven Products

```
P₁ = 6
P₂ = 8
P₃ = 72
P₄ = -10
P₅ = 48
P₆ = -12
P₇ = -84
```

**Double-check:** We computed 7 products, not 8! This is the key to Strassen's efficiency.

---

### Step 4: Compute C₁₁ = P₅ + P₄ - P₂ + P₆

**Formula:** C₁₁ = P₅ + P₄ - P₂ + P₆

**Substitute values:**
```
C₁₁ = 48 + (-10) - 8 + (-12)
```

**Calculate step by step:**
```
Step 1: 48 + (-10) = 38
Step 2: 38 - 8 = 30
Step 3: 30 + (-12) = 18
```

**Result: C₁₁ = 18**

**What does C₁₁ represent?**
- C₁₁ is the top-left element of the result matrix C
- It's the element in row 1, column 1

---

### Step 5: Compute C₁₂ = P₁ + P₂

**Formula:** C₁₂ = P₁ + P₂

**Substitute values:**
```
C₁₂ = 6 + 8 = 14
```

**Result: C₁₂ = 14**

**What does C₁₂ represent?**
- C₁₂ is the top-right element of the result matrix C
- It's the element in row 1, column 2

---

### Step 6: Compute C₂₁ = P₃ + P₄

**Formula:** C₂₁ = P₃ + P₄

**Substitute values:**
```
C₂₁ = 72 + (-10) = 62
```

**Result: C₂₁ = 62**

**What does C₂₁ represent?**
- C₂₁ is the bottom-left element of the result matrix C
- It's the element in row 2, column 1

---

### Step 7: Compute C₂₂ = P₅ + P₁ - P₃ - P₇

**Formula:** C₂₂ = P₅ + P₁ - P₃ - P₇

**Substitute values:**
```
C₂₂ = 48 + 6 - 72 - (-84)
```

**Calculate step by step:**
```
Step 1: 48 + 6 = 54
Step 2: 54 - 72 = -18
Step 3: -18 - (-84) = -18 + 84 = 66
```

**Result: C₂₂ = 66**

**What does C₂₂ represent?**
- C₂₂ is the bottom-right element of the result matrix C
- It's the element in row 2, column 2

---

### Step 8: Assemble the Final Result Matrix

**Result matrix C:**
```
C = [C₁₁  C₁₂]
    [C₂₁  C₂₂]

C = [18  14]
    [62  66]
```

---

### Step 9: Verification (Check Our Answer!)

**Let's verify using standard matrix multiplication:**

**Standard method:**
```
C[1,1] = A[1,1]×B[1,1] + A[1,2]×B[2,1] = 1×6 + 3×4 = 6 + 12 = 18 ✓
C[1,2] = A[1,1]×B[1,2] + A[1,2]×B[2,2] = 1×8 + 3×2 = 8 + 6 = 14 ✓
C[2,1] = A[2,1]×B[1,1] + A[2,2]×B[2,1] = 7×6 + 5×4 = 42 + 20 = 62 ✓
C[2,2] = A[2,1]×B[1,2] + A[2,2]×B[2,2] = 7×8 + 5×2 = 56 + 10 = 66 ✓
```

**Perfect match!** Our Strassen's algorithm result is correct.

---

## Final Answer for Problem 4.2-1

**Using Strassen's algorithm:**

**Step 1: Partition matrices**
```
A₁₁=1, A₁₂=3, A₂₁=7, A₂₂=5
B₁₁=6, B₁₂=8, B₂₁=4, B₂₂=2
```

**Step 2: Compute seven products**
```
P₁ = A₁₁(B₁₂ - B₂₂) = 1(8-2) = 6
P₂ = (A₁₁ + A₁₂)B₂₂ = (1+3)2 = 8
P₃ = (A₂₁ + A₂₂)B₁₁ = (7+5)6 = 72
P₄ = A₂₂(B₂₁ - B₁₁) = 5(4-6) = -10
P₅ = (A₁₁ + A₂₂)(B₁₁ + B₂₂) = (1+5)(6+2) = 48
P₆ = (A₁₂ - A₂₂)(B₂₁ + B₂₂) = (3-5)(4+2) = -12
P₇ = (A₁₁ - A₂₁)(B₁₁ + B₁₂) = (1-7)(6+8) = -84
```

**Step 3: Compute result submatrices**
```
C₁₁ = P₅ + P₄ - P₂ + P₆ = 48 + (-10) - 8 + (-12) = 18
C₁₂ = P₁ + P₂ = 6 + 8 = 14
C₂₁ = P₃ + P₄ = 72 + (-10) = 62
C₂₂ = P₅ + P₁ - P₃ - P₇ = 48 + 6 - 72 - (-84) = 66
```

**Final result:**
```
[1  3]   [6  8]   [18  14]
[7  5] × [4  2] = [62  66]
```

---

---

## Problem 4.2-2: Write Pseudocode for Strassen's Algorithm

### Problem Statement
Write pseudocode for Strassen's algorithm.

---

## Background: What is Pseudocode?

**Definition:**
Pseudocode is a way to describe an algorithm using a mix of:
- Natural language (English)
- Programming-like structure (loops, if-statements, etc.)
- Mathematical notation

**Purpose:**
- Communicate the algorithm clearly
- Independent of any specific programming language
- Focus on logic, not syntax

**Conventions we'll use:**
- Indentation shows structure
- `//` for comments
- Arrays indexed from 1 (not 0)
- Matrix operations: `+`, `-`, `×` for add, subtract, multiply

---

## Solution: Strassen's Algorithm Pseudocode

### Main Algorithm

```
STRASSEN-MULTIPLY(A, B, n)
    // Input: Two n×n matrices A and B (n is a power of 2)
    // Output: The product matrix C = A × B
    
    // Base case: if matrices are 1×1, just multiply
    if n == 1
        C[1,1] = A[1,1] × B[1,1]
        return C
    
    // Recursive case: divide matrices into quadrants
    
    // Step 1: Partition A into four n/2 × n/2 submatrices
    A₁₁ = A[1..n/2, 1..n/2]           // top-left
    A₁₂ = A[1..n/2, (n/2+1)..n]       // top-right
    A₂₁ = A[(n/2+1)..n, 1..n/2]       // bottom-left
    A₂₂ = A[(n/2+1)..n, (n/2+1)..n]   // bottom-right
    
    // Step 2: Partition B into four n/2 × n/2 submatrices
    B₁₁ = B[1..n/2, 1..n/2]
    B₁₂ = B[1..n/2, (n/2+1)..n]
    B₂₁ = B[(n/2+1)..n, 1..n/2]
    B₂₂ = B[(n/2+1)..n, (n/2+1)..n]
    
    // Step 3: Compute the seven products recursively
    P₁ = STRASSEN-MULTIPLY(A₁₁, B₁₂ - B₂₂, n/2)
    P₂ = STRASSEN-MULTIPLY(A₁₁ + A₁₂, B₂₂, n/2)
    P₃ = STRASSEN-MULTIPLY(A₂₁ + A₂₂, B₁₁, n/2)
    P₄ = STRASSEN-MULTIPLY(A₂₂, B₂₁ - B₁₁, n/2)
    P₅ = STRASSEN-MULTIPLY(A₁₁ + A₂₂, B₁₁ + B₂₂, n/2)
    P₆ = STRASSEN-MULTIPLY(A₁₂ - A₂₂, B₂₁ + B₂₂, n/2)
    P₇ = STRASSEN-MULTIPLY(A₁₁ - A₂₁, B₁₁ + B₁₂, n/2)
    
    // Step 4: Compute the four quadrants of C
    C₁₁ = P₅ + P₄ - P₂ + P₆
    C₁₂ = P₁ + P₂
    C₂₁ = P₃ + P₄
    C₂₂ = P₅ + P₁ - P₃ - P₇
    
    // Step 5: Combine quadrants into result matrix C
    C[1..n/2, 1..n/2] = C₁₁
    C[1..n/2, (n/2+1)..n] = C₁₂
    C[(n/2+1)..n, 1..n/2] = C₂₁
    C[(n/2+1)..n, (n/2+1)..n] = C₂₂
    
    return C
```

---

## Detailed Explanation of the Pseudocode

### Line-by-Line Breakdown

#### Function Signature
```
STRASSEN-MULTIPLY(A, B, n)
```

**What this means:**
- **Function name:** STRASSEN-MULTIPLY
- **Parameters:**
  - `A`: First input matrix (n×n)
  - `B`: Second input matrix (n×n)
  - `n`: Size of the matrices (must be a power of 2)
- **Returns:** Matrix C = A × B

**Why n must be a power of 2:**
- We keep dividing by 2: n → n/2 → n/4 → ...
- This only works cleanly if n = 2^k for some integer k
- If n is not a power of 2, we need to pad with zeros (not shown here)

---

#### Base Case
```
if n == 1
    C[1,1] = A[1,1] × B[1,1]
    return C
```

**What this means:**
- If matrices are 1×1 (just single numbers), multiply them directly
- This stops the recursion

**Why we need a base case:**
- Recursion must eventually stop
- 1×1 is the smallest possible matrix
- Direct multiplication is trivial for 1×1 matrices

**Example:**
- A = [5], B = [3]
- C = [5 × 3] = [15]

---

#### Step 1: Partition Matrix A
```
A₁₁ = A[1..n/2, 1..n/2]
A₁₂ = A[1..n/2, (n/2+1)..n]
A₂₁ = A[(n/2+1)..n, 1..n/2]
A₂₂ = A[(n/2+1)..n, (n/2+1)..n]
```

**What this means:**
- Split A into 4 equal quadrants
- Each quadrant is (n/2) × (n/2)

**Visual representation (for n=4):**
```
A = [a₁₁  a₁₂ | a₁₃  a₁₄]
    [a₂₁  a₂₂ | a₂₃  a₂₄]
    [--------|--------]
    [a₃₁  a₃₂ | a₃₃  a₃₄]
    [a₄₁  a₄₂ | a₄₃  a₄₄]

A₁₁ = [a₁₁  a₁₂]    A₁₂ = [a₁₃  a₁₄]
      [a₂₁  a₂₂]          [a₂₃  a₂₄]

A₂₁ = [a₃₁  a₃₂]    A₂₂ = [a₃₃  a₃₄]
      [a₄₁  a₄₂]          [a₄₃  a₄₄]
```

**Index notation explained:**
- `A[1..n/2, 1..n/2]` means rows 1 to n/2, columns 1 to n/2
- `A[1..n/2, (n/2+1)..n]` means rows 1 to n/2, columns n/2+1 to n
- And so on...

---

#### Step 2: Partition Matrix B
```
B₁₁ = B[1..n/2, 1..n/2]
B₁₂ = B[1..n/2, (n/2+1)..n]
B₂₁ = B[(n/2+1)..n, 1..n/2]
B₂₂ = B[(n/2+1)..n, (n/2+1)..n]
```

**What this means:**
- Same as Step 1, but for matrix B
- Split B into 4 equal quadrants

---

#### Step 3: Compute Seven Products

```
P₁ = STRASSEN-MULTIPLY(A₁₁, B₁₂ - B₂₂, n/2)
```

**What this means:**
- **B₁₂ - B₂₂:** First, subtract matrix B₂₂ from B₁₂ (element-wise)
  - This is O(n²/4) = O(n²) time
- **STRASSEN-MULTIPLY(A₁₁, ...):** Then recursively multiply A₁₁ by the result
  - This is a recursive call on (n/2)×(n/2) matrices
- **P₁ =:** Store the result in P₁

**Important notes:**
- The subtraction `B₁₂ - B₂₂` happens BEFORE the recursive call
- We pass `n/2` as the size parameter (matrices are now half the size)
- This is a recursive call - it will call STRASSEN-MULTIPLY again!

**Similar explanations for P₂ through P₇:**

```
P₂ = STRASSEN-MULTIPLY(A₁₁ + A₁₂, B₂₂, n/2)
```
- Add A₁₁ and A₁₂ first
- Then recursively multiply by B₂₂

```
P₃ = STRASSEN-MULTIPLY(A₂₁ + A₂₂, B₁₁, n/2)
```
- Add A₂₁ and A₂₂ first
- Then recursively multiply by B₁₁

```
P₄ = STRASSEN-MULTIPLY(A₂₂, B₂₁ - B₁₁, n/2)
```
- Subtract B₁₁ from B₂₁ first
- Then recursively multiply A₂₂ by the result

```
P₅ = STRASSEN-MULTIPLY(A₁₁ + A₂₂, B₁₁ + B₂₂, n/2)
```
- Add A₁₁ and A₂₂ (first argument)
- Add B₁₁ and B₂₂ (second argument)
- Then recursively multiply the two sums

```
P₆ = STRASSEN-MULTIPLY(A₁₂ - A₂₂, B₂₁ + B₂₂, n/2)
```
- Subtract A₂₂ from A₁₂ (first argument)
- Add B₂₁ and B₂₂ (second argument)
- Then recursively multiply

```
P₇ = STRASSEN-MULTIPLY(A₁₁ - A₂₁, B₁₁ + B₁₂, n/2)
```
- Subtract A₂₁ from A₁₁ (first argument)
- Add B₁₁ and B₁₂ (second argument)
- Then recursively multiply

**Key observation:**
- We make exactly 7 recursive calls (not 8!)
- This is what makes Strassen's algorithm faster

---

#### Step 4: Compute Result Quadrants

```
C₁₁ = P₅ + P₄ - P₂ + P₆
C₁₂ = P₁ + P₂
C₂₁ = P₃ + P₄
C₂₂ = P₅ + P₁ - P₃ - P₇
```

**What this means:**
- Combine the seven products using addition and subtraction
- Each operation is matrix addition/subtraction: O(n²) time
- These formulas are Strassen's magic - they give the correct result!

**Why these specific combinations?**
- Strassen derived these through algebraic manipulation
- They're not intuitive, but they work!
- The key is they produce the correct matrix product

---

#### Step 5: Assemble Result Matrix

```
C[1..n/2, 1..n/2] = C₁₁
C[1..n/2, (n/2+1)..n] = C₁₂
C[(n/2+1)..n, 1..n/2] = C₂₁
C[(n/2+1)..n, (n/2+1)..n] = C₂₂
```

**What this means:**
- Copy the four quadrants into the result matrix C
- C₁₁ goes in the top-left
- C₁₂ goes in the top-right
- C₂₁ goes in the bottom-left
- C₂₂ goes in the bottom-right

**Visual:**
```
C = [C₁₁ | C₁₂]
    [----|----]
    [C₂₁ | C₂₂]
```

---

#### Return Statement
```
return C
```

**What this means:**
- Return the completed result matrix to the caller
- If this was a recursive call, the result becomes one of the P values
- If this was the top-level call, this is the final answer

---

## Complexity Analysis

### Time Complexity

**Recurrence relation:**
```
T(n) = 7T(n/2) + Θ(n²)
```

**Breaking it down:**
- **7T(n/2):** Seven recursive calls on (n/2)×(n/2) matrices
- **Θ(n²):** Time for additions/subtractions
  - Partitioning: O(1) with index calculation
  - 10 matrix additions/subtractions: 10 × O(n²/4) = O(n²)
  - Combining: O(n²)

**Solution using Master Theorem:**
- a = 7, b = 2, f(n) = Θ(n²)
- n^(log_b a) = n^(log₂ 7) ≈ n^2.807
- f(n) = n² is polynomially smaller than n^2.807
- Case 1 applies: T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

**Comparison:**
- Standard algorithm: Θ(n³)
- Strassen's algorithm: Θ(n^2.807)
- Improvement: Faster for large n!

---

### Space Complexity

**Recursive call stack:**
- Depth: log₂ n levels
- Each level stores O(n²) data (submatrices)
- Total: O(n² log n)

**In practice:**
- Can be optimized to O(n²) with careful implementation
- Trade-off between time and space

---

## Alternative Pseudocode (More Detailed)

Here's a version with explicit helper functions:

```
MATRIX-ADD(A, B, n)
    // Add two n×n matrices element-wise
    C = new n×n matrix
    for i = 1 to n
        for j = 1 to n
            C[i,j] = A[i,j] + B[i,j]
    return C

MATRIX-SUBTRACT(A, B, n)
    // Subtract matrix B from A element-wise
    C = new n×n matrix
    for i = 1 to n
        for j = 1 to n
            C[i,j] = A[i,j] - B[i,j]
    return C

STRASSEN-MULTIPLY(A, B, n)
    if n == 1
        C[1,1] = A[1,1] × B[1,1]
        return C
    
    // Partition matrices (as before)
    A₁₁, A₁₂, A₂₁, A₂₂ = PARTITION(A, n)
    B₁₁, B₁₂, B₂₁, B₂₂ = PARTITION(B, n)
    
    // Compute products with explicit temporary matrices
    S₁ = MATRIX-SUBTRACT(B₁₂, B₂₂, n/2)
    P₁ = STRASSEN-MULTIPLY(A₁₁, S₁, n/2)
    
    S₂ = MATRIX-ADD(A₁₁, A₁₂, n/2)
    P₂ = STRASSEN-MULTIPLY(S₂, B₂₂, n/2)
    
    S₃ = MATRIX-ADD(A₂₁, A₂₂, n/2)
    P₃ = STRASSEN-MULTIPLY(S₃, B₁₁, n/2)
    
    S₄ = MATRIX-SUBTRACT(B₂₁, B₁₁, n/2)
    P₄ = STRASSEN-MULTIPLY(A₂₂, S₄, n/2)
    
    S₅ = MATRIX-ADD(A₁₁, A₂₂, n/2)
    S₆ = MATRIX-ADD(B₁₁, B₂₂, n/2)
    P₅ = STRASSEN-MULTIPLY(S₅, S₆, n/2)
    
    S₇ = MATRIX-SUBTRACT(A₁₂, A₂₂, n/2)
    S₈ = MATRIX-ADD(B₂₁, B₂₂, n/2)
    P₆ = STRASSEN-MULTIPLY(S₇, S₈, n/2)
    
    S₉ = MATRIX-SUBTRACT(A₁₁, A₂₁, n/2)
    S₁₀ = MATRIX-ADD(B₁₁, B₁₂, n/2)
    P₇ = STRASSEN-MULTIPLY(S₉, S₁₀, n/2)
    
    // Combine products
    T₁ = MATRIX-ADD(P₅, P₄, n/2)
    T₂ = MATRIX-SUBTRACT(T₁, P₂, n/2)
    C₁₁ = MATRIX-ADD(T₂, P₆, n/2)
    
    C₁₂ = MATRIX-ADD(P₁, P₂, n/2)
    
    C₂₁ = MATRIX-ADD(P₃, P₄, n/2)
    
    T₃ = MATRIX-ADD(P₅, P₁, n/2)
    T₄ = MATRIX-SUBTRACT(T₃, P₃, n/2)
    C₂₂ = MATRIX-SUBTRACT(T₄, P₇, n/2)
    
    // Assemble result
    C = COMBINE(C₁₁, C₁₂, C₂₁, C₂₂, n)
    return C
```

**Why this version is more detailed:**
- Explicit temporary matrices (S₁, S₂, ..., T₁, T₂, ...)
- Shows exactly when each addition/subtraction happens
- Easier to implement in actual code
- More verbose but clearer

---

## Final Answer for Problem 4.2-2

**Pseudocode for Strassen's Algorithm:**

```
STRASSEN-MULTIPLY(A, B, n)
    // Base case
    if n == 1
        return A[1,1] × B[1,1]
    
    // Partition into quadrants
    A₁₁, A₁₂, A₂₁, A₂₂ = partition A into four n/2 × n/2 submatrices
    B₁₁, B₁₂, B₂₁, B₂₂ = partition B into four n/2 × n/2 submatrices
    
    // Compute seven products
    P₁ = STRASSEN-MULTIPLY(A₁₁, B₁₂ - B₂₂, n/2)
    P₂ = STRASSEN-MULTIPLY(A₁₁ + A₁₂, B₂₂, n/2)
    P₃ = STRASSEN-MULTIPLY(A₂₁ + A₂₂, B₁₁, n/2)
    P₄ = STRASSEN-MULTIPLY(A₂₂, B₂₁ - B₁₁, n/2)
    P₅ = STRASSEN-MULTIPLY(A₁₁ + A₂₂, B₁₁ + B₂₂, n/2)
    P₆ = STRASSEN-MULTIPLY(A₁₂ - A₂₂, B₂₁ + B₂₂, n/2)
    P₇ = STRASSEN-MULTIPLY(A₁₁ - A₂₁, B₁₁ + B₁₂, n/2)
    
    // Combine into result
    C₁₁ = P₅ + P₄ - P₂ + P₆
    C₁₂ = P₁ + P₂
    C₂₁ = P₃ + P₄
    C₂₂ = P₅ + P₁ - P₃ - P₇
    
    // Assemble and return
    return combine C₁₁, C₁₂, C₂₁, C₂₂ into n×n matrix C
```

**Key features:**
- ✓ Recursive structure with base case
- ✓ Partitioning into quadrants
- ✓ Seven recursive multiplications (not eight!)
- ✓ Combination using additions/subtractions
- ✓ Time complexity: Θ(n^(log₂ 7)) ≈ Θ(n^2.807)

---

**End of Section 4.2 Solutions**
