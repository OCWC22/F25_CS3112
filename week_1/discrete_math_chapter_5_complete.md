# Chapter 5: Sequences, Mathematical Induction, and Recursion (Complete)

**Pages 227-310**

## Introduction

One of the most important tasks of mathematics is to discover and characterize regular patterns, such as those associated with processes that are repeated. The main mathematical structure used in the study of repeated processes is the sequence, and the main mathematical tool used to verify conjectures about sequences is mathematical induction.

---

## 5.1 Sequences

**Page 227**

> A mathematician, like a painter or poet, is a maker of patterns.
> — G. H. Hardy, A Mathematician's Apology, 1940

Imagine that a person decides to count his ancestors. He has two parents, four grandparents, eight great-grandparents, and so forth. These numbers can be written in a row as:

```
2, 4, 8, 16, 32, 64, 128, ...
```

The symbol "..." is called an **ellipsis**. It is shorthand for "and so forth."

To express the pattern of the numbers, suppose that each is labeled by an integer giving its position in the row.

| Position in the row | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |
|-------------------|---|---|---|---|---|---|---|-----|
| Number of ancestors | 2 | 4 | 8 | 16 | 32 | 64 | 128 | ... |

**Page 228**

The number corresponding to position 1 is 2, which equals 2¹. The number corresponding to position 2 is 4, which equals 2². For positions 3, 4, 5, 6, and 7, the corresponding numbers are 8, 16, 32, 64, and 128, which equal 2³, 2⁴, 2⁵, 2⁶, and 2⁷, respectively. For a general value of k, let Aₖ be the number of ancestors in the kth generation back. The pattern of computed values strongly suggests the following for each k:

```
Aₖ = 2ᵏ
```

### Definition: Sequence

A **sequence** is a function whose domain is either all the integers between two given integers or all the integers greater than or equal to a given integer.

We typically represent a sequence as a set of elements written in a row. In the sequence denoted

```
aₘ, aₘ₊₁, aₘ₊₂, ..., aₙ
```

each individual element aₖ (read "a sub k") is called a **term**. The k in aₖ is called a **subscript** or **index**, m (which may be any integer) is the subscript of the initial term, and n (which must be greater than or equal to m) is the subscript of the final term. The notation

```
aₘ, aₘ₊₁, aₘ₊₂, ...
```

denotes an infinite sequence. An **explicit formula** or **general formula** for a sequence is a rule that shows how the values of aₖ depend on k.

### Example 5.1.1: Finding Terms of Sequences Given by Explicit Formulas

Define sequences a₁, a₂, a₃, ... and b₂, b₃, b₄, ... by the following explicit formulas:

```
aₖ = k/(k+1) for all integers k ≥ 1
bᵢ = (i-1)/i for all integers i ≥ 2
```

Compute the first five terms of both sequences.

**Solution:**
```
a₁ = 1/(1+1) = 1/2        b₂ = (2-1)/2 = 1/2
a₂ = 2/(2+1) = 2/3        b₃ = (3-1)/3 = 2/3
a₃ = 3/(3+1) = 3/4        b₄ = (4-1)/4 = 3/4
a₄ = 4/(4+1) = 4/5        b₅ = (5-1)/5 = 4/5
a₅ = 5/(5+1) = 5/6        b₆ = (6-1)/6 = 5/6
```

**Page 229**

### Example 5.1.2: An Alternating Sequence

Compute the first six terms of the sequence c₀, c₁, c₂, ... defined as follows:

```
cⱼ = (-1)ʲ for all integers j ≥ 0
```

**Solution:**
```
c₀ = (-1)⁰ = 1
c₁ = (-1)¹ = -1
c₂ = (-1)² = 1
c₃ = (-1)³ = -1
c₄ = (-1)⁴ = 1
c₅ = (-1)⁵ = -1
```

Thus the first six terms are 1, -1, 1, -1, 1, -1. By exercises 33 and 34 of Section 4.1, even powers of -1 equal 1 and odd powers of -1 equal -1. It follows that the sequence oscillates endlessly between 1 and -1.

### Example 5.1.3: Finding an Explicit Formula to Fit Given Initial Terms

Find an explicit formula for a sequence that has the following initial terms:
```
1, -1/4, 1/9, -1/16, 1/25, -1/36, ...
```

**Solution:** Denote the general term by aₖ and suppose the first term is a₁. The terms can be rewritten as:
```
1/1², -1/2², 1/3², -1/4², 1/5², -1/6²
```

Note that the denominator of each term equals the square of the subscript of that term, and that the numerator equals ±1. Hence:
```
aₖ = ±1/k²
```

The numerator oscillates between +1 and -1; it is +1 when k is odd and -1 when k is even. To achieve this oscillation, insert a factor of (-1)^(k+1). Consequently, an explicit formula is:
```
aₖ = (-1)^(k+1)/k² for all integers k ≥ 1
```

**Page 230**

## Summation Notation

Consider again the example where Aₖ = 2ᵏ represents the number of ancestors a person has in the kth generation back. The total number of ancestors for the past six generations is:

```
A₁ + A₂ + A₃ + A₄ + A₅ + A₆ = 2¹ + 2² + 2³ + 2⁴ + 2⁵ + 2⁶ = 126
```

### Definition: Summation Notation

If m and n are integers and m ≤ n, the symbol ∑ₖ₌ₘⁿ aₖ, read the summation from k equals m to n of a-sub-k, is the sum of all the terms aₘ, aₘ₊₁, aₘ₊₂, ..., aₙ.

We say that aₘ + aₘ₊₁ + aₘ₊₂ + ... + aₙ is the expanded form of the sum, and we write:

```
∑ₖ₌ₘⁿ aₖ = aₘ + aₘ₊₁ + aₘ₊₂ + ... + aₙ
```

We call k the **index of the summation**, m the **lower limit** of the summation, and n the **upper limit** of the summation.

### Recursive Definition of Summation

A more mathematically precise definition of summation, called a recursive definition, is:

If m is any integer, then:
```
∑ₖ₌ₘᵐ aₖ = aₘ

∑ₖ₌ₘⁿ aₖ = ∑ₖ₌ₘⁿ⁻¹ aₖ + aₙ    for all integers n > m
```

**Page 232-233**

### Example 5.1.10: A Telescoping Sum

Some sums can be transformed into telescoping sums. For instance, observe that:
```
1/k - 1/(k+1) = (k+1-k)/(k(k+1)) = 1/(k(k+1))
```

Use this identity to find a simple expression for:
```
∑ₖ₌₁ⁿ 1/(k(k+1))
```

**Solution:**
```
∑ₖ₌₁ⁿ 1/(k(k+1)) = ∑ₖ₌₁ⁿ (1/k - 1/(k+1))
                  = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/(n-1) - 1/n) + (1/n - 1/(n+1))
                  = 1 - 1/(n+1)
```

## Product Notation

**Page 233**

### Definition: Product Notation

If m and n are integers and m ≤ n, the symbol ∏ₖ₌ₘⁿ aₖ, read the product from k equals m to n of a-sub-k, is the product of all the terms aₘ, aₘ₊₁, aₘ₊₂, ..., aₙ.

We write:
```
∏ₖ₌ₘⁿ aₖ = aₘ · aₘ₊₁ · aₘ₊₂ · ... · aₙ
```

A recursive definition for the product notation is:
```
∏ₖ₌ₘᵐ aₖ = aₘ

∏ₖ₌ₘⁿ aₖ = (∏ₖ₌ₘⁿ⁻¹ aₖ) · aₙ    for all integers n > m
```

**Page 234**

### Theorem 5.1.1: Properties of Summations and Products

If aₘ, aₘ₊₁, aₘ₊₂, ... and bₘ, bₘ₊₁, bₘ₊₂, ... are sequences of real numbers and c is any real number, then the following equations hold for any integer n ≥ m:

1. ∑ₖ₌ₘⁿ aₖ + ∑ₖ₌ₘⁿ bₖ = ∑ₖ₌ₘⁿ (aₖ + bₖ)

2. c · ∑ₖ₌ₘⁿ aₖ = ∑ₖ₌ₘⁿ c·aₖ    (generalized distributive law)

3. (∏ₖ₌ₘⁿ aₖ) · (∏ₖ₌ₘⁿ bₖ) = ∏ₖ₌ₘⁿ (aₖ · bₖ)

## Factorial and "n Choose r" Notation

**Page 237**

### Definition: Factorial

For each positive integer n, the quantity n factorial denoted n!, is defined to be the product of all the integers from 1 to n:
```
n! = n · (n-1) · ... · 3 · 2 · 1
```

Zero factorial, denoted 0!, is defined to be 1:
```
0! = 1
```

### Recursive Definition for Factorial

Given any nonnegative integer n:
```
n! = {
    1           if n = 0
    n · (n-1)!  if n ≥ 1
}
```

**Page 238**

### Definition: n Choose r

Let n and r be integers with 0 ≤ r ≤ n. The symbol (n r) is read "n choose r" and represents the number of subsets of size r that can be chosen from a set with n elements.

### Formula for Computing (n r)

For all integers n and r with 0 ≤ r ≤ n:
```
(n r) = n! / (r!(n-r)!)
```

The quantities (n r) are also called **combinations** or **binomial coefficients**.

**Page 240-242**

## Algorithm to Convert from Base 10 to Base 2 Using Repeated Division by 2

If a nonnegative integer a is repeatedly divided by 2 until a quotient of zero is obtained and the remainders are found to be r[0], r[1], ..., r[k], then by repeated substitution:

```
a = 2ᵏ·r[k] + 2^(k-1)·r[k-1] + ... + 2²·r[2] + 2¹·r[1] + 2⁰·r[0]
```

Thus the binary representation for a can be read:
```
a₁₀ = (r[k]r[k-1]...r[2]r[1]r[0])₂
```

### Algorithm 5.1.1: Decimal to Binary Conversion Using Repeated Division by 2

**Input:** n [a nonnegative integer]

**Algorithm Body:**
```
q := n, i := 0
while (i = 0 or q ≠ 0)
    r[i] := q mod 2
    q := q div 2
    i := i + 1
end while
```

**Output:** r[0], r[1], r[2], ..., r[i-1] [a sequence of integers]

---

## 5.2 Mathematical Induction I

**Page 244**

> [Mathematical induction is] the standard proof technique in computer science.
> — Anthony Ralston, 1984

Mathematical induction is one of the more recently developed techniques of proof in the history of mathematics. It is used to check conjectures about the outcomes of processes that occur repeatedly and according to definite patterns.

### Example: Coins Problem

**Claim:** For all integers n ≥ 8, n cents can be obtained using 3¢ and 5¢ coins.

More formally: For all integers n ≥ 8, P(n) is true, where P(n) is the sentence "n cents can be obtained using 3¢ and 5¢ coins."

**Page 246**

## Principle of Mathematical Induction

Let P(n) be a property that is defined for integers n, and let a be a fixed integer. Suppose the following two statements are true:

1. P(a) is true.
2. For all integers k ≥ a, if P(k) is true then P(k+1) is true.

Then the statement
```
for all integers n ≥ a, P(n)
```
is true.

## Method of Proof by Mathematical Induction

**Page 247**

Consider a statement of the form, "For all integers n ≥ a, a property P(n) is true."

To prove such a statement, perform the following two steps:

**Step 1 (basis step):** Show that P(a) is true.

**Step 2 (inductive step):** Show that for all integers k ≥ a, if P(k) is true then P(k+1) is true. To perform this step:
- Suppose that P(k) is true, where k is any particular but arbitrarily chosen integer with k ≥ a. [This supposition is called the **inductive hypothesis**.]
- Then show that P(k+1) is true.

### Proposition 5.2.1

**For all integers n ≥ 8, n¢ can be obtained using 3¢ and 5¢ coins.**

**Proof (by mathematical induction):**

Let the property P(n) be the sentence: n¢ can be obtained using 3¢ and 5¢ coins.

**Show that P(8) is true:**
P(8) is true because 8¢ can be obtained using one 3¢ coin and one 5¢ coin.

**Show that for all integers k ≥ 8, if P(k) is true then P(k+1) is also true:**

Suppose that k is any integer with k ≥ 8 such that k¢ can be obtained using 3¢ and 5¢ coins. [P(k) - inductive hypothesis]

We must show that (k+1)¢ can be obtained using 3¢ and 5¢ coins. [P(k+1)]

**Case 1** (There is a 5¢ coin among those used to make up the k¢): In this case replace the 5¢ coin by two 3¢ coins; the result will be (k+1)¢.

**Case 2** (There is no 5¢ coin among those used to make up the k¢): Then 3¢ coins are used exclusively. Since k ≥ 8, at least three 3¢ coins must be included. Replace three 3¢ coins by two 5¢ coins to obtain (k+1)¢.

[The chapter continues with more sections on mathematical induction, strong mathematical induction, recursion, and other related topics through page 310]