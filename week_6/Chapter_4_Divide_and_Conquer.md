# Chapter 4: Divide-and-Conquer

## Chapter 4 Overview

Recall the divide-and-conquer paradigm, which we used for merge sort:

- **Divide** the problem into one or more subproblems that are smaller instances of the same problem.
- **Conquer** the subproblems by solving them recursively.
- **Base case**: If the subproblems are small enough, just solve them by brute force.
- **Combine** the subproblem solutions to form a solution to the original problem.

We look at two algorithms for multiplying square matrices, based on divide-and-conquer.

## Analyzing Divide-and-Conquer Algorithms

Use a recurrence to characterize the running time of a divide-and-conquer algorithm. Solving the recurrence gives us the asymptotic running time.

A recurrence is a function defined in terms of:
- one or more base cases, and
- itself, with smaller arguments.

A recurrence could have 0, 1, or more functions that satisfy it. Well defined if at least 1 function satisfies; otherwise, ill defined.

### Algorithmic Recurrences

Interested in recurrences that describe running times of algorithms.

A recurrence T(n) is algorithmic if for every sufficiently large threshold constant n₀ > 0:

- For all n < n₀, T(n) = Ω(1). [Can consider the running time constant for small problem sizes.]
- For all n ≥ n₀, every path of recursion terminates in a defined base case within a finite number of recursive invocations. [The recursive algorithm terminates.]

## Conventions

- Will often state recurrences without base cases. When analyzing algorithms, assume that if no base case is given, the recurrence is algorithmic. Allows us to pick any sufficiently large threshold constant n₀ without changing the asymptotic behavior of the solution.
- Ceilings and floors in divide-and-conquer recurrences don't change the asymptotic solution → often state algorithmic recurrences without floors and ceilings, even though to be precise, they should be there. [Example: recurrence for merge sort is really T(n) = T(⌈n/2⌉) + T(⌊n/2⌋) + Ω(n).]
- Some recurrences are inequalities rather than equations.
- Example: T(n) ≤ 2T(n/2) + Ω(n) gives only an upper bound on T(n), so state the solution using O-notation rather than Θ-notation.

## Examples of Recurrences

### n×n Matrix Multiplication
Breaking into 8 subproblems of size n/2 × n/2:
T(n) = 8T(n/2) + Ω(1). Solution: T(n) = Θ(n³).

### Strassen's Algorithm
For n×n matrix multiplication by breaking into 7 subproblems of size n/2 × n/2:
T(n) = 7T(n/2) + Ω(1). Solution: T(n) = Θ(n^lg₇) = O(n².⁸¹).

### Uneven Split Algorithm
Breaks a problem of size n into one subproblem of size n/3 and another of size 2n/3, taking Ω(n) time to divide and combine:
T(n) = T(n/3) + T(2n/3) + Ω(n). Solution: T(n) = Θ(n lg n).

### Order-Statistic Algorithm
Breaks a problem of size n into one subproblem of size n/5 and another of size 7n/10, taking Ω(n) time to divide and combine:
T(n) = T(n/5) + T(7n/10) + Ω(n). Solution: T(n) = Θ(n).

### Recursive Linear Search
Creates one subproblem with one element less than the original problem. Time to divide and combine is Ω(1):
T(n) = T(n-1) + Ω(1). Solution: T(n) = Θ(n).

## Methods for Solving Recurrences

The chapter contains four methods for solving recurrences. Each gives asymptotic bounds.

1. **Substitution method**: Guess the solution, then use induction to prove that it's correct.
2. **Recursion-tree method**: Draw out a recursion tree, determine the costs at each level, and sum them up. Useful for coming up with a guess for the substitution method.
3. **Master method**: A cookbook method for recurrences of the form T(n) = aT(n/b) + f(n), where a > 0 and b > 1 are constants, subject to certain conditions. Requires memorizing three cases, but applies to many divide-and-conquer algorithms.
4. **Akra-Bazzi method**: A general method for solving divide-and-conquer recurrences. Requires calculus, but applies to recurrences beyond those solved by the master method. [We do not cover the Akra-Bazzi method.]

In this course, we concentrate only on two acceptable ways of solving recurrences: the substitution method and the master method.

## Multiplying Square Matrices

Input: Three n×n (square) matrices, A = (aᵢⱼ), B = (bᵢⱼ), and C = (cᵢⱼ).

Result: The matrix product A×B is added into C, so that:
```
cᵢⱼ = cᵢⱼ + Σₖ₌₁ⁿ aᵢₖ bₖⱼ
```
for i, j = 1, 2, ..., n.

If only the product A×B is needed, then zero out all entries of C beforehand.

### Matrix-Multiply Algorithm
```python
Matrix-Multiply(A, B, C, n)
1 for i = 1 to n
2   for j = 1 to n
3     for k = 1 to n  // compute entries in each of n rows
4       C[i][j] = C[i][j] + A[i][k] * B[k][j]  // add in one more term
```

Time: Θ(n³) because of triply nested loops.

## Simple Divide-and-Conquer Algorithm

For simplicity, assume that C is initialized to 0, so computing C = A×B.

If n > 1, partition each of A, B, C into four n/2 × n/2 matrices:

```
A = [A₁₁ A₁₂]    B = [B₁₁ B₁₂]    C = [C₁₁ C₁₂]
    [A₂₁ A₂₂]        [B₂₁ B₂₂]        [C₂₁ C₂₂]
```

Rewrite C = A×B as:
```
[C₁₁ C₁₂] = [A₁₁ A₁₂] × [B₁₁ B₁₂]
[C₂₁ C₂₂]   [A₂₁ A₂₂]   [B₂₁ B₂₂]
```

Giving the four equations:
- C₁₁ = A₁₁×B₁₁ + A₁₂×B₂₁
- C₁₂ = A₁₁×B₁₂ + A₁₂×B₂₂
- C₂₁ = A₂₁×B₁₁ + A₂₂×B₂₁
- C₂₂ = A₂₁×B₁₂ + A₂₂×B₂₂

Each of these equations multiplies two n/2 × n/2 matrices and then adds their n/2 × n/2 products. Assume that n is an exact power of 2, so that submatrix dimensions are always integer.

### MATRIX-MULTIPLY-RECURSIVE Algorithm
```python
MATRIX-MULTIPLY-RECURSIVE(A, B, C, n)
1 if n == 1
2   C[1][1] = C[1][1] + A[1][1] * B[1][1]
3   return
4 // Divide
5 partition A, B, and C into n/2 × n/2 submatrices
6 A11, A12, A21, A22; B11, B12, B21, B22; C11, C12, C21, C22 respectively
7 // Conquer
8 MATRIX-MULTIPLY-RECURSIVE(A11, B11, C11, n/2)
9 MATRIX-MULTIPLY-RECURSIVE(A11, B12, C12, n/2)
10 MATRIX-MULTIPLY-RECURSIVE(A21, B11, C21, n/2)
11 MATRIX-MULTIPLY-RECURSIVE(A21, B12, C22, n/2)
12 MATRIX-MULTIPLY-RECURSIVE(A12, B21, C11, n/2)
13 MATRIX-MULTIPLY-RECURSIVE(A12, B22, C12, n/2)
14 MATRIX-MULTIPLY-RECURSIVE(A22, B21, C21, n/2)
15 MATRIX-MULTIPLY-RECURSIVE(A22, B22, C22, n/2)
```

### Analysis
Let T(n) be the time to multiply two n×n matrices.

**Base case**: n = 1. Perform one scalar multiplication: Θ(1).

**Recursive case**: n > 1.
- Dividing takes Θ(1) time, using index calculations.
- Conquering makes 8 recursive calls, each multiplying n/2 × n/2 matrices → 8T(n/2).
- No combine step, because C is updated in place.

Recurrence (omitting the base case) is T(n) = 8T(n/2) + Θ(1). Can use master method to show that it has solution T(n) = Θ(n³).

Asymptotically, no better than the obvious method.

## Strassen's Algorithm

Idea: Make the recursion tree less bushy. Perform only 7 recursive multiplications of n/2 × n/2 matrices, rather than 8. Will cost several additions/subtractions of n/2 × n/2 matrices.

Since a subtraction is a "negative addition," just refer to all additions and subtractions as additions.

### The Algorithm
1. Same base case as before, when n = 1.
2. When n > 1, partition each of the matrices into four n/2 × n/2 submatrices. Time: Θ(1), using index calculations.
3. Create 10 matrices S₁, S₂, ..., S₁₀. Each is n/2 × n/2 and is the sum or difference of two matrices created in previous step. Time: Θ(n²) to create all 10 matrices.
4. Create and zero the entries of 7 matrices P₁, P₂, ..., P₇, each n/2 × n/2. Time: Θ(n²).
5. Using the submatrices of A and B and the matrices S₁, S₂, ..., S₁₀, recursively compute P₁, P₂, ..., P₇. Time: 7T(n/2).
6. Update the four n/2 × n/2 submatrices C₁₁, C₁₂, C₂₁, C₂₂ of C by adding and subtracting various combinations of the Pᵢ. Time: Θ(n²).

### Analysis
Recurrence will be T(n) = 7T(n/2) + Θ(n²). By the master method, solution is T(n) = Θ(n^lg₇). Since lg₇ ≈ 2.81, the running time is O(n².⁸¹), beating the Θ(n³) running time of the straightforward algorithm.

## Substitution Method

To solve T(n) = 2T(n/2) + Θ(n) with a guess of T(n) = Θ(n lg n):

**Upper bound**: Show T(n) ≤ c n lg n for some c > 0.

Assume T(n/2) ≤ c (n/2) lg(n/2) = c (n/2) (lg n - 1) = c (n/2) lg n - c n/2.

Then T(n) ≤ 2[c (n/2) lg n - c n/2] + c n = c n lg n - c n + c n = c n lg n.

**Lower bound**: Show T(n) ≥ c n lg n for some c > 0.

Assume T(n/2) ≥ c (n/2) lg(n/2) = c (n/2) (lg n - 1) = c (n/2) lg n - c n/2.

Then T(n) ≥ 2[c (n/2) lg n - c n/2] + c n = c n lg n - c n + c n = c n lg n.

### Making a Good Guess

Use recursion trees to generate a guess. Then verify by substitution method.

### Avoiding Pitfalls

Be careful when using asymptotic notation. A false proof for the recurrence T(n) = 2T(⌊n/2⌋) + Θ(n), that T(n) = O(n):

```
T(n) ≤ 2 O(⌊n/2⌋) + Θ(n)
     = 2 O(n) + Θ(n)
     = O(n)  // wrong!
```

This "proof" changes the constant in the Θ-notation. Can see this by using an explicit constant. Assume T(n) ≤ c n for all n ≥ n₀:

```
T(n) ≤ 2(c ⌊n/2⌋) + Θ(n)
     ≤ c n + Θ(n)
```

But c n + Θ(n) > c n.

## Recursion Trees

Use to generate a guess. Then verify by substitution method.

### Example: T(n) = 3T(n/4) + Θ(n²)

Draw out a recursion tree for T(n) = 3T(n/4) + c n²:

```
         c n²
      /   |   \
   c (n/4)²  c (n/4)²  c (n/4)²
   / \      / \      / \
...   ...  ...  ...  ...  ...
```

For simplicity, assume that n is a power of 4 and the base case is T(1) = Θ(1).

Subproblem size for nodes at depth i is n/4ⁱ. Get to base case when n/4ⁱ = 1 → n = 4ⁱ → i = log₄ n.

Each level has 3 times as many nodes as the level above, so that depth i has 3ⁱ nodes. Each internal node at depth i has cost c (n/4ⁱ)² → total cost at depth i (except for leaves) is 3ⁱ c (n/4ⁱ)² = (3/16)ⁱ c n².

Bottom level has depth log₄ n → number of leaves is 3^log₄ n = n^log₄ 3. Since each leaf contributes Θ(1), total cost of leaves is Θ(n^log₄ 3).

Add up costs over all levels to determine cost for the entire tree:

```
T(n) = c n² + Σ_{i=0}^{log₄ n - 1} (3/16)ⁱ c n² + Θ(n^log₄ 3)
     = c n² (1 + Σ_{i=0}^{log₄ n - 1} (3/16)ⁱ) + Θ(n^log₄ 3)
     = c n² (1 / (1 - 3/16)) + Θ(n^log₄ 3)
     = c n² (16/13) + Θ(n^log₄ 3)
     = O(n²)
```

Use substitution method to verify O(n²) upper bound. Show that T(n) ≤ d n² for constant d > 0:

```
T(n) ≤ 3T(n/4) + c n²
     ≤ 3 d (n/4)² + c n²
     = 3 d (n²/16) + c n²
     = d n² + c n²
     = (d + c) n²
```

By choosing d ≥ 16c/13. [Again, we get to name but not choose c, and we get to name and choose d.]

That gives an upper bound of O(n²). The lower bound of Ω(n²) is obvious because the recurrence contains a Θ(n²) term. Hence, T(n) = Θ(n²).

## Master Method

Used for many divide-and-conquer master recurrences of the form:
T(n) = a T(n/b) + f(n)

Where a ≥ 1, b > 1, and f(n) is an asymptotically nonnegative function defined over all sufficiently large positive numbers.

Master recurrences describe recursive algorithms that divide a problem of size n into a subproblems, each of size n/b. Each recursive subproblem takes time T(n/b) (unless it's a base case). Call f(n) the driving function.

### Master Theorem (Theorem 4.1)

Let a, b, n₀ > 0 be constants, f(n) be a driving function defined and nonnegative on all sufficiently large reals. Define recurrence T(n) on n ∈ ℕ by:
T(n) = a T(n/b) + f(n)

Then you can solve the recurrence by comparing n^logᵦ a vs. f(n):

**Case 1**: f(n) = O(n^logᵦ a - ε) for some constant ε > 0.
(f(n) is polynomially smaller than n^logᵦ a)
Solution: T(n) = Θ(n^logᵦ a)

**Case 2**: f(n) = Θ(n^logᵦ a lgᵏ n), where k ≥ 0 is a constant.
(f(n) is within a polylog factor of n^logᵦ a, but not smaller.)
Solution: T(n) = Θ(n^logᵦ a lgᵏ⁺¹ n)

**Case 3**: f(n) = Ω(n^logᵦ a + ε) for some constant ε > 0 and f(n) satisfies the regularity condition a f(n/b) ≤ c f(n) for some constant c < 1 and all sufficiently large n.
(f(n) is polynomially greater than n^logᵦ a)
Solution: T(n) = Θ(f(n))

### Examples

**T(n) = 5T(n/2) + Θ(n²)**
n^log₂ 5 vs. n²
Since log₂ 5 ≈ 2.32 < 2, use case 1 → T(n) = Θ(n^log₂ 5)

**T(n) = 27T(n/3) + Θ(n³ lg n)**
n^log₃ 27 = n³ vs. n³ lg n
Use case 2 with k = 1 → T(n) = Θ(n³ lg² n)

**T(n) = 5T(n/2) + Θ(n³)**
n^log₂ 5 vs. n³
Now log₂ 5 + ε < 3 for some constant ε > 0
Check regularity condition: a f(n/b) = 5 (n/2)³ = 5 n³/8 = c n³ for c = 5/8 < 1
Use case 3 → T(n) = Θ(n³)

**T(n) = 27T(n/3) + Θ(n³ / lg n)**
n^log₃ 27 = n³ vs. n³ / lg n = n³ lg⁻¹ n ≠ Θ(n³ lgᵏ n) for any k ≥ 0.
Cannot use the master method.
