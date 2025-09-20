# Chapter 5: Sequences, Mathematical Induction, and Recursion (Complete)

**Pages 227-310**

## Introduction

One of the most important tasks of mathematics is to discover and characterize regular patterns, such as those associated with processes that are repeated. The main mathematical structure used in the study of repeated processes is the sequence, and the main mathematical tool used to verify conjectures about sequences is mathematical induction. In this chapter we introduce the notation and terminology of sequences, show how to use both ordinary and strong mathematical induction to prove properties about them, illustrate the various ways recursively defined sequences arise, describe a method for obtaining an explicit formula for a recursively defined sequence, and explain how to verify the correctness of such a formula. We also discuss a principle—the well-ordering principle for the integers—that is logically equivalent to the two forms of mathematical induction, and we show how to adapt mathematical induction to prove the correctness of computer algorithms. In the final section we discuss more general recursive definitions, such as the one used for the careful formulation of the concept of Boolean expression, and the idea of recursive function.

---

## 5.1 Sequences

**Page 255**

> A mathematician, like a painter or poet, is a maker of patterns.
> — G. H. Hardy, A Mathematician's Apology, 1940

Imagine that a person decides to count his ancestors. He has two parents, four grandparents, eight great-grandparents, and so forth, These numbers can be written in a row as

```
2, 4, 8, 16, 32, 64, 128, . . .
```

The symbol ". . ." is called an ellipsis. It is shorthand for "and so forth."

To express the pattern of the numbers, suppose that each is labeled by an integer giving its position in the row.

| Position in the row | 1 | 2 | 3 | 4 | 5 | 6 | 7... |
|-------------------|---|---|---|---|---|---|-----|
| Number of ancestors | 2 | 4 | 8 | 16 | 32 | 64 | 128 . . . |

The number corresponding to position 1 is 2, which equals 2¹. The number corresponding to position 2 is 4, which equals 2². For positions 3, 4, 5, 6, and 7, the corresponding numbers are 8, 16, 32, 64, and 128, which equal 2³, 2⁴, 2⁵, 2⁶, and 2⁷, respectively. For a general value of k, let Aₖ be the number of ancestors in the kth generation back. The pattern of computed values strongly suggests the following for each k:

```
Aₖ = 2ᵏ
```

**Page 256**

### Definition: Sequence

A sequence is a function whose domain is either all the integers between two given integers or all the integers greater than or equal to a given integer.

We typically represent a sequence as a set of elements written in a row. In the sequence denoted

```
aₘ, aₘ₊₁, aₘ₊₂, . . . , aₙ,
```

each individual element aₖ (read "a sub k") is called a term. The k in aₖ is called a subscript or index, m (which may be any integer) is the subscript of the initial term, and n (which must be greater than or equal to m) is the subscript of the final term. The notation

```
aₘ, aₘ₊₁, aₘ₊₂, . . .
```

denotes an infinite sequence. An explicit formula or general formula for a sequence is a rule that shows how the values of aₖ depend on k.

The following example shows that it is possible for two different formulas to give sequences with the same terms.

### Example 5.1.1 Finding Terms of Sequences Given by Explicit Formulas

Define sequences a₁, a₂, a₃, . . . and b₂, b₃, b₄, . . . by the following explicit formulas:

```
aₖ = k/(k+1) for all integers k ≥ 1,

bᵢ = (i-1)/i for all integers i ≥ 2.
```

Compute the first five terms of both sequences.

**Solution**

```
a₁ = 1/(1+1) = 1/2        b₂ = (2-1)/2 = 1/2
a₂ = 2/(2+1) = 2/3        b₃ = (3-1)/3 = 2/3
a₃ = 3/(3+1) = 3/4        b₄ = (4-1)/4 = 3/4
a₄ = 4/(4+1) = 4/5        b₅ = (5-1)/5 = 4/5
a₅ = 5/(5+1) = 5/6        b₆ = (6-1)/6 = 5/6
```

As you can see, the first terms of both sequences are 1/2, 2/3, 3/4, 4/5, 5/6; in fact, it can be shown that all terms of both sequences are identical.

**Page 257**

### Example 5.1.2 An Alternating Sequence

Compute the first six terms of the sequence c₀, c₁, c₂, . . . defined as follows:

```
cⱼ = (-1)ʲ for all integers j ≥ 0.
```

**Solution**

```
c₀ = (-1)⁰ = 1
c₁ = (-1)¹ = -1
c₂ = (-1)² = 1
c₃ = (-1)³ = -1
c₄ = (-1)⁴ = 1
c₅ = (-1)⁵ = -1
```

Thus the first six terms are 1, -1, 1, -1, 1, -1. By exercises 33 and 34 of Section 4.1, even powers of -1 equal 1 and odd powers of -1 equal -1. It follows that the sequence oscillates endlessly between 1 and -1.

In Examples 5.1.1 and 5.1.2 the task was to compute the first few values of a sequence given by an explicit formula. The next example treats the question of how to find an explicit formula for a sequence with given initial terms. Any such formula is a guess, but it is very useful to be able to make such guesses.

### Example 5.1.3 Finding an Explicit Formula to Fit Given Initial Terms

Find an explicit formula for a sequence that has the following initial terms:
```
1, -1/4, 1/9, -1/16, 1/25, -1/36,....
```

**Solution** Denote the general term of the sequence by aₖ and suppose the first term is a₁. Then observe that the denominator of each term is a perfect square. Thus the terms can be rewritten as

```
1/1², -1/2², 1/3², -1/4², 1/5², -1/6²
```

Note that the denominator of each term equals the square of the subscript of that term, and that the numerator equals ±1. Hence

```
aₖ = ±1/k²
```

Also the numerator oscillates back and forth between +1 and -1; it is +1 when k is odd and -1 when k is even. To achieve this oscillation, insert a factor of (-1)^(k+1) (or (-1)^(k-1)) into the formula for aₖ. [For when k is odd, k + 1 is even and thus (-1)^(k+1) = +1; and when k is even, k + 1 is odd and thus (-1)^(k+1) = -1.] Consequently, an explicit formula that gives the correct first six terms is

```
aₖ = (-1)^(k+1)/k² for all integers k ≥ 1.
```

**Page 258**

Note that making the first term a₀ would have led to the alternative formula

```
aₖ = (-1)^k/(k+1)² for all integers k ≥ 0.
```

You should check that this formula also gives the correct first six terms.

## Summation Notation

Consider again the example in which Aₖ = 2ᵏ represents the number of ancestors a person has in the kth generation back. What is the total number of ancestors for the past six generations? The answer is

```
A₁ + A₂ + A₃ + A₄ + A₅ + A₆ = 2¹ + 2² + 2³ + 2⁴ + 2⁵ + 2⁶ = 126.
```

It is convenient to use a shorthand notation to write such sums. In 1772 the French mathematician Joseph Louis Lagrange introduced the capital Greek letter sigma, Σ, to denote the word sum (or summation), and defined the summation notation as follows:

### Definition: Summation Notation

If m and n are integers and m ≤ n, the symbol

```
∑ₖ₌ₘⁿ aₖ,
```

read the summation from k equals m to n of a-sub-k, is the sum of all the terms aₘ, aₘ₊₁, aₘ₊₂, . . . , aₙ. We say that aₘ + aₘ₊₁ + aₘ₊₂ + . . . + aₙ is the expanded form of the sum, and we write

```
∑ₖ₌ₘⁿ aₖ = aₘ + aₘ₊₁ + aₘ₊₂ + · · · + aₙ.
```

We call k the index of the summation, m the lower limit of the summation, and n the upper limit of the summation.

### Example 5.1.4 Computing Summations

Let a₁ = -2, a₂ = -1, a₃ = 0, a₄ = 1, and a₅ = 2. Compute the following:

a. ∑ₖ₌₁⁵ aₖ    b. ∑ₖ₌₂² aₖ    c. ∑ₖ₌₁² a₂ₖ

**Solution**

a. ∑ₖ₌₁⁵ aₖ = a₁ + a₂ + a₃ + a₄ + a₅ = (-2) + (-1) + 0 + 1 + 2 = 0

b. ∑ₖ₌₂² aₖ = a₂ = -1

c. ∑ₖ₌₁² a₂ₖ = a₂·₁ + a₂·₂ = a₂ + a₄ = -1 + 1 = 0

**Page 259**

Oftentimes, the terms of a summation are expressed using an explicit formula. For instance, it is common to see summations such as

```
∑ₖ₌₁⁵ k²    or    ∑ᵢ₌₀⁸ (-1)ⁱ/(i+1)
```

### Example 5.1.5 When the Terms of a Summation Are Given by a Formula

Compute the following summation:

```
∑ₖ₌₁⁵ k²
```

**Solution**

```
∑ₖ₌₁⁵ k² = 1² + 2² + 3² + 4² + 5² = 55.
```

### Example 5.1.6 Changing from Summation Notation to Expanded Form

Write the following summation in expanded form:

```
∑ᵢ₌₀ⁿ (-1)ⁱ/(i+1)
```

**Solution**

```
∑ᵢ₌₀ⁿ (-1)ⁱ/(i+1) = (-1)⁰/(0+1) + (-1)¹/(1+1) + (-1)²/(2+1) + (-1)³/(3+1) + ... + (-1)ⁿ/(n+1)
                  = 1/1 + (-1)/2 + 1/3 + (-1)/4 + ... + (-1)ⁿ/(n+1)
                  = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)ⁿ/(n+1)
```

### Example 5.1.7 Changing from Expanded Form to Summation Notation

Express the following using summation notation:

```
1/n + 2/(n+1) + 3/(n+2) + ... + (n+1)/(2n)
```

**Solution**

The general term of this summation can be expressed as (k+1)/(n+k) for integers k from 0 to n. Hence

```
1/n + 2/(n+1) + 3/(n+2) + ... + (n+1)/(2n) = ∑ₖ₌₀ⁿ (k+1)/(n+k)
```

For small values of n, the expanded form of a sum may appear ambiguous. For instance, consider

```
1² + 2² + 3² + · · · + n².
```

This expression is intended to represent the sum of squares of consecutive integers starting with 1² and ending with n². Thus, if n = 1 the sum is just 1², if n = 2 the sum is 1² + 2², and if n = 3 the sum is 1² + 2² + 3².

**Page 260**

### Example 5.1.8 Evaluating a₁, a₂, a₃, . . . , aₙ for Small n

What is the value of the expression

```
1/(1·2) + 1/(2·3) + 1/(3·4) + · · · + 1/(n·(n+1))
```

when n = 1? n = 2? n = 3?

**Solution**

When n = 1, the expression equals 1/(1·2) = 1/2.

When n = 2, it equals 1/(1·2) + 1/(2·3) = 1/2 + 1/6 = 2/3.

When n = 3, it is 1/(1·2) + 1/(2·3) + 1/(3·4) = 1/2 + 1/6 + 1/12 = 3/4.

A more mathematically precise definition of summation, called a recursive definition, is the following:

If m is any integer, then

```
∑ₖ₌ₘᵐ aₖ = aₘ
```

and

```
∑ₖ₌ₘⁿ aₖ = ∑ₖ₌ₘⁿ⁻¹ aₖ + aₙ    for all integers n > m.
```

When solving problems, it is often useful to rewrite a summation using the recursive form of the definition, either by separating off the final term of a summation or by adding a final term to a summation.

### Example 5.1.9 Separating Off a Final Term and Adding On a Final Term

a. Rewrite ∑ᵢ₌₁ⁿ⁺¹ 1/i² by separating off the final term.

b. Write ∑ₖ₌₀ⁿ 2ᵏ + 2ⁿ⁺¹ as a single summation.

**Solution**

a. ∑ᵢ₌₁ⁿ⁺¹ 1/i² = ∑ᵢ₌₁ⁿ 1/i² + 1/(n+1)²

b. ∑ₖ₌₀ⁿ 2ᵏ + 2ⁿ⁺¹ = ∑ₖ₌₀ⁿ⁺¹ 2ᵏ

**Page 261**

### Example 5.1.10 A Telescoping Sum

Some sums can be transformed into telescoping sums, which then can be rewritten as a simple expression. For instance, observe that

```
1/k - 1/(k+1) = (k+1-k)/(k(k+1)) = 1/(k(k+1))
```

Use this identity to find a simple expression for

```
∑ₖ₌₁ⁿ 1/(k(k+1))
```

**Solution**

```
∑ₖ₌₁ⁿ 1/(k(k+1)) = ∑ₖ₌₁ⁿ (1/k - 1/(k+1))
                  = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/(n-1) - 1/n) + (1/n - 1/(n+1))
                  = 1 - 1/(n+1)
```

## Product Notation

**Page 263**

### Definition: Product Notation

If m and n are integers and m ≤ n, the symbol

```
∏ₖ₌ₘⁿ aₖ,
```

read the product from k equals m to n of a-sub-k, is the product of all the terms aₘ, aₘ₊₁, aₘ₊₂, . . . , aₙ. We write

```
∏ₖ₌ₘⁿ aₖ = aₘ · aₘ₊₁ · aₘ₊₂ · · · aₙ.
```

A recursive definition for the product notation is the following: If m is any integer, then

```
∏ₖ₌ₘᵐ aₖ = aₘ
```

and

```
∏ₖ₌ₘⁿ aₖ = (∏ₖ₌ₘⁿ⁻¹ aₖ) · aₙ    for all integers n > m.
```

### Example 5.1.11 Computing Products

Compute the following products:

a. ∏ₖ₌₁⁵ k

b. ∏ₖ₌₁¹ k/(k+1)

**Solution**

a. ∏ₖ₌₁⁵ k = 1 · 2 · 3 · 4 · 5 = 120

b. ∏ₖ₌₁¹ k/(k+1) = 1/(1+1) = 1/2

**Page 264**

### Theorem 5.1.1 Properties of Summations and Products

If aₘ, aₘ₊₁, aₘ₊₂, . . . and bₘ, bₘ₊₁, bₘ₊₂, . . . are sequences of real numbers and c is any real number, then the following equations hold for any integer n ≥ m:

1. ∑ₖ₌ₘⁿ aₖ + ∑ₖ₌ₘⁿ bₖ = ∑ₖ₌ₘⁿ (aₖ + bₖ)

2. c · ∑ₖ₌ₘⁿ aₖ = ∑ₖ₌ₘⁿ c·aₖ    (generalized distributive law)

3. (∏ₖ₌ₘⁿ aₖ) · (∏ₖ₌ₘⁿ bₖ) = ∏ₖ₌ₘⁿ (aₖ · bₖ)

### Example 5.1.12 Using Properties of Summation and Product

Let aₖ = k + 1 and bₖ = k - 1 for all integers k. Write each of the following expressions as a single summation or product:

a. ∑ₖ₌ₘⁿ aₖ + 2 · ∑ₖ₌ₘⁿ bₖ

b. (∏ₖ₌ₘⁿ aₖ) · (∏ₖ₌ₘⁿ bₖ)

**Solution**

a. ∑ₖ₌ₘⁿ aₖ + 2 · ∑ₖ₌ₘⁿ bₖ = ∑ₖ₌ₘⁿ (k + 1) + 2 · ∑ₖ₌ₘⁿ (k - 1)
                          = ∑ₖ₌ₘⁿ (k + 1) + ∑ₖ₌ₘⁿ 2·(k - 1)
                          = ∑ₖ₌ₘⁿ ((k + 1) + 2·(k - 1))
                          = ∑ₖ₌ₘⁿ (3k - 1)

b. (∏ₖ₌ₘⁿ aₖ) · (∏ₖ₌ₘⁿ bₖ) = ∏ₖ₌ₘⁿ (k + 1) · ∏ₖ₌ₘⁿ (k - 1)
                          = ∏ₖ₌ₘⁿ ((k + 1) · (k - 1))
                          = ∏ₖ₌ₘⁿ (k² - 1)

## Change of Variable

Observe that

```
∑ₖ₌₁³ k² = 1² + 2² + 3²
```

and also that

```
∑ᵢ₌₁³ i² = 1² + 2² + 3².
```

Hence

```
∑ₖ₌₁³ k² = ∑ᵢ₌₁³ i².
```

This equation illustrates the fact that the symbol used to represent the index of a summation can be replaced by any other symbol as long as the replacement is made in each location where the symbol occurs. As a consequence, the index of a summation is called a dummy variable. A dummy variable is a symbol that derives its entire meaning from its local context. Outside of that context (both before and after), the symbol may have another meaning entirely.

The appearance of a summation can be altered by more complicated changes of variable as well. For example, observe that

```
∑ⱼ₌₂⁴ (j - 1)² = (2 - 1)² + (3 - 1)² + (4 - 1)² = 1² + 2² + 3² = ∑ₖ₌₁³ k².
```

**Page 265**

### Example 5.1.13 Transforming a Sum by a Change of Variable

Transform the following summation by making the specified change of variable.

summation: ∑ₖ₌₀⁶ 1/(k+1)

change of variable: j = k + 1

**Solution**

First calculate the lower and upper limits of the new summation:

When k = 0, j = k + 1 = 0 + 1 = 1.
When k = 6, j = k + 1 = 6 + 1 = 7.

Thus the new sum goes from j = 1 to j = 7.

Next calculate the general term of the new summation. You will need to replace each occurrence of k by an expression in j:

Since j = k + 1, then k = j - 1.
Hence 1/(k+1) = 1/((j - 1) + 1) = 1/j.

Finally, put the steps together to obtain

```
∑ₖ₌₀⁶ 1/(k+1) = ∑ⱼ₌₁⁷ 1/j.
```

Equation (5.1.1) can be given an additional twist by noting that because the j in the right-hand summation is a dummy variable, it may be replaced by any other variable name, as long as the substitution is made in every location where j occurs. In particular, it is legal to substitute k in place of j to obtain

```
∑ⱼ₌₁⁷ 1/j = ∑ₖ₌₁⁷ 1/k.
```

Putting equations (5.1.1) and (5.1.2) together gives

```
∑ₖ₌₀⁶ 1/(k+1) = ∑ₖ₌₁⁷ 1/k.
```

Sometimes it is necessary to shift the limits of one summation in order to add it to another. An example is the algebraic proof of the binomial theorem, given in Section 9.7. A general procedure for making such a shift when the upper limit appears in the expression to be summed is illustrated in the next example.

**Page 266**

### Example 5.1.14 When the Upper Limit Appears in the Expression to Be Summed

a. Transform the following summation by making the specified change of variable.

summation: ∑ₖ₌₁ⁿ⁺¹ k/(n+k)

change of variable: j = k - 1

b. Transform the summation obtained in part (a) by changing all j's to k's.

**Solution**

a. When k = 1, then j = k - 1 = 1 - 1 = 0. (So the new lower limit is 0.)
When k = n + 1, then j = k - 1 = (n + 1) - 1 = n. (So the new upper limit is n.)

Since j = k - 1, then k = j + 1. Also note that n is a constant as far as the terms of the sum are concerned. It follows that

```
k/(n+k) = (j + 1)/(n + (j + 1))
```

and so the general term of the new summation is

```
(j + 1)/(n + (j + 1))
```

Therefore,

```
∑ₖ₌₁ⁿ⁺¹ k/(n+k) = ∑ⱼ₌₀ⁿ (j + 1)/(n + (j + 1))
```

b. Changing all the j's to k's in the right-hand side of equation (5.1.3) gives

```
∑ⱼ₌₀ⁿ (j + 1)/(n + (j + 1)) = ∑ₖ₌₀ⁿ (k + 1)/(n + (k + 1))
```

Combining equations (5.1.3) and (5.1.4) results in

```
∑ₖ₌₁ⁿ⁺¹ k/(n+k) = ∑ₖ₌₀ⁿ (k + 1)/(n + (k + 1))
```

## Factorial and "n Choose r" Notation

**Page 267**

### Definition: Factorial

For each positive integer n, the quantity n factorial denoted n!, is defined to be the product of all the integers from 1 to n:

```
n! = n · (n - 1) · · · 3 ·2 · 1.
```

Zero factorial, denoted 0!, is defined to be 1:

```
0! = 1.
```

The definition of zero factorial as 1 may seem odd, but, as you will see when you read Chapter 9, it is convenient for many mathematical formulas.

### Example 5.1.15 The First Ten Factorials

```
0! = 1          5! = 5·4·3·2·1 = 120
1! = 1          6! = 6·5·4·3·2·1 = 720
2! = 2·1 = 2    7! = 7·6·5·4·3·2·1 = 5,040
3! = 3·2·1 = 6  8! = 8·7·6·5·4·3·2·1 = 40,320
4! = 4·3·2·1 = 24  9! = 9·8·7·6·5·4·3·2·1 = 362,880
```

As you can see from the example above, the values of n! grow very rapidly. For instance, 40! ≈ 8.16 × 10⁴⁷, which is a number that is too large to be computed exactly using the standard integer arithmetic of the machine-specific implementations of many computer languages. (The symbol ≈ means "is approximately equal to.")

A recursive definition for factorial is the following: Given any nonnegative integer n,

```
n! = { 1           if n = 0
       n · (n - 1)! if n ≥ 1
}
```

**Page 268**

### Example 5.1.16 Computing with Factorials

Simplify the following expressions:

a. 8!/7!

b. 5!/(2!·3!)

c. 1/(2!·4!) + 1/(3!·3!)

d. (n+1)!/n!

e. n!/(n-3)!

**Solution**

a. 8!/7! = (8·7!)/7! = 8

b. 5!/(2!·3!) = (5·4·3!)/(2·1·3!) = (5·4)/(2·1) = 10

c. 1/(2!·4!) + 1/(3!·3!) = 1/(2!·4!) + 1/(3!·3!)
                      = 3/(3·2!·4!) + 4/(4·3!·3!)
                      = 3/(3!·4!) + 4/(3!·4!)
                      = 7/(3!·4!) = 7/144

d. (n+1)!/n! = ((n+1)·n!)/n! = n+1

e. n!/(n-3)! = (n·(n-1)·(n-2)·(n-3)!)/(n-3)! = n·(n-1)·(n-2) = n³ - 3n² + 2n

An important use for the factorial notation is in calculating values of quantities, called n choose r, that occur in many branches of mathematics, especially those connected with the study of counting techniques and probability.

**Page 269**

### Definition: n Choose r

Let n and r be integers with 0 ≤ r ≤ n. The symbol

```
(n r)
```

is read "n choose r" and represents the number of subsets of size r that can be chosen from a set with n elements.

Observe that the definition implies that (n r) will always be an integer because it is a number of subsets. In Section 9.5 we will explore many uses of n choose r for solving problems involving counting, and we will prove the following computational formula:

### Formula for Computing (n r)

For all integers n and r with 0 ≤ r ≤ n:

```
(n r) = n!/(r!(n-r)!)
```

In the meantime, we will provide a few experiences with using it. Because n choose r is always an integer, you can be sure that all the factors in the denominator of the formula will be canceled out by factors in the numerator. Many electronic calculators have keys for computing values of (n r). These are denoted in various ways such as nCr, C(n, r), Crⁿ, and Cn,r. The letter C is used because the quantities (n r) are also called combinations. Sometimes they are referred to as binomial coefficients because of the connection with the binomial theorem discussed in Section 9.7.

**Page 270**

### Example 5.1.17 Computing (n r) by Hand

Use the formula for computing (n r) to evaluate the following expressions:

a. (8 5)

b. (4 4)

c. (n+1 n)

**Solution**

a. (8 5) = 8!/(5!(8-5)!) = 8!/(5!3!) = (8·7·6·5·4·3·2·1)/((5·4·3·2·1)·(3·2·1))

Always cancel common factors before multiplying

= 56.

b. (4 4) = 4!/(4!(4-4)!) = 4!/(4!0!) = (4·3·2·1)/((4·3·2·1)(1)) = 1

The fact that 0! = 1 makes this formula computable. It gives the correct value because a set of size 4 has exactly one subset of size 4, namely itself.

c. (n+1 n) = (n+1)!/(n!((n+1)-n)!) = (n+1)!/(n!1!) = ((n+1)·n!)/n! = n+1

## Sequences in Computer Programming

An important data type in computer programming consists of finite sequences. In computer programming contexts, these are usually referred to as one-dimensional arrays. For example, consider a program that analyzes the wages paid to a sample of 50 workers. Such a program might compute the average wage and the difference between each individual wage and the average. This would require that each wage be stored in memory for retrieval later in the calculation. To avoid the use of entirely separate variable names for all of the 50 wages, each is written as a term of a one-dimensional array:

```
W[1], W[2], W[3], . . . , W[50].
```

Note that the subscript labels are written inside square brackets. The reason is that until relatively recently, it was impossible to type actual dropped subscripts on most computer keyboards.

The main difficulty programmers have when using one-dimensional arrays is keeping the labels straight.

**Page 271**

### Example 5.1.18 Dummy Variable in a Loop

The index variable for a for-next loop is a dummy variable. For example, the following three algorithm segments all produce the same output:

```
1. for i := 1 to n
   print a[i]
   next i

2. for j := 0 to n - 1
   print a[j + 1]
   next j

3. for k := 2 to n + 1
   print a[k - 1]
   next k
```

The recursive definitions for summation, product, and factorial lead naturally to computational algorithms. For instance, here are two sets of pseudocode to find the sum of a[1], a[2], . . . , a[n]. The one on the left exactly mimics the recursive definition by initializing the sum to equal a[1]; the one on the right initializes the sum to equal 0. In both cases the output is ∑ₖ₌₁ⁿ a[k].

```
s := a[1]                 s := 0
for k := 2 to n           for k := 1 to n
    s := s + a[k]             s := s + a[k]
next k                    next k
```

## Application: Algorithm to Convert from Base 10 to Base 2 Using Repeated Division by 2

Section 2.5 contains some examples of converting integers from decimal to binary notation. The method shown there, however, is only convenient to use with small numbers. A systematic algorithm to convert any nonnegative integer to binary notation uses repeated division by 2.

Suppose a is a nonnegative integer. Divide a by 2 using the quotient-remainder theorem to obtain a quotient q[0] and a remainder r[0]. If the quotient is nonzero, divide by 2 again to obtain a quotient q[1] and a remainder r[1]. Continue this process until a quotient of 0 is obtained. At each stage, the remainder must be less than the divisor, which is 2. Thus each remainder is either 0 or 1. The process is illustrated below for a = 38. (Read the divisions from the bottom up.)

```
   2
   2
   38
   2
   19
   2
   9
   2
   4
   2
   2
   0
   1
```

remainder = 1 = r[5]
remainder = 0 = r[4]
remainder = 0 = r[3]
remainder = 1 = r[2]
remainder = 1 = r[1]
remainder = 0 = r[0]

The results of all these divisions can be written as a sequence of equations:

```
38 = 19·2 + 0,
19 = 9·2 + 1,
9 = 4·2 + 1,
4 = 2·2 + 0,
2 = 1·2 + 0,
1 = 0·2 + 1.
```

By repeated substitution, then,

```
38 = 19·2 + 0
   = (9·2 + 1)·2 + 0 = 9·2² + 1·2 + 0
   = (4·2 + 1)·2² + 1·2 + 0 = 4·2³ + 1·2² + 1·2 + 0
   = (2·2 + 0)·2³ + 1·2² + 1·2 + 0 = 2·2⁴ + 0·2³ + 1·2² + 1·2 + 0
   = (1·2 + 0)·2⁴ + 0·2³ + 1·2² + 1·2 + 0 = 1·2⁵ + 0·2⁴ + 0·2³ + 1·2² + 1·2 + 0.
```

**Page 272**

Note that each coefficient of a power of 2 on the right-hand side of the previous page is one of the remainders obtained in the repeated division of 38 by 2. This is true for the left-most 1 as well, because 1 = 0·2 + 1. Thus

```
38₁₀ = 100110₂ = (r[5]r[4]r[3]r[2]r[1]r[0])₂.
```

In general, if a nonnegative integer a is repeatedly divided by 2 until a quotient of zero is obtained and the remainders are found to be r[0], r[1], . . . , r[k], then by the quotient-remainder theorem each r[i] equals 0 or 1, and by repeated substitution from the theorem,

```
a = 2ᵏ·r[k] + 2ᵏ⁻¹·r[k-1] + · · · + 2²·r[2] + 2¹·r[1] + 2⁰·r[0].
```

Thus the binary representation for a can be read from the equation:

```
a₁₀ = (r[k]r[k-1]· · · r[2]r[1]r[0])₂.
```

### Example 5.1.19 Converting from Decimal to Binary Notation Using Repeated Division by 2

Use repeated division by 2 to write the number 29₁₀ in binary notation.

**Solution**

```
   2
   2
   29
   2
   14
   2
   7
   2
   3
   0
   1
```

remainder = r[4] = 1
remainder = r[3] = 1
remainder = r[2] = 1
remainder = r[1] = 0
remainder = r[0] = 1

Hence 29₁₀ = (r[4]r[3]r[2]r[1]r[0])₂ = 11101₂.

The procedure we have described for converting from base 10 to base 2 is formalized in the following algorithm:

### Algorithm 5.1.1 Decimal to Binary Conversion Using Repeated Division by 2

**Input:** n [a nonnegative integer]

**Algorithm Body:**

```
q := n, i := 0
while (i = 0 or q ≠ 0)
    r[i] := q mod 2
    q := q div 2
    [r[i] and q can be obtained by calling the division algorithm.]
    i := i + 1
end while
```

**Output:** r[0], r[1], r[2], . . . , r[i-1] [a sequence of integers]

## Test Yourself

1. The notation ∑ₖ₌ₘⁿ aₖ is read "_____."

2. The expanded form of ∑ₖ₌ₘⁿ aₖ is _____.

3. The value of a₁ + a₂ + a₃ + · · · + aₙ when n = 2 is "_____."

4. The notation ∏ₖ₌ₘⁿ aₖ is read "_____."

5. If n is a positive integer, then n! = _____.

6. ∑ₖ₌ₘⁿ aₖ + c·∑ₖ₌ₘⁿ bₖ = _____.

7. (∏ₖ₌ₘⁿ aₖ)·(∏ₖ₌ₘⁿ bₖ) = _____.

## Exercise Set 5.1

Write the first four terms of the sequences defined by the formulas in 1–6.

1. aₖ = k/(10 + k), for all integers k ≥ 1.
2. bⱼ = (5 - j)/(5 + j), for all integers j ≥ 1.
3. cᵢ = (-1)ⁱ/(3ⁱ), for all integers i ≥ 0.
4. dₘ = 1 + 1/2ᵐ, for all integers m ≥ 0.
5. eₙ = (n 2)·2, for all integers n ≥ 0.
6. fₙ = (n 4)·4, for all integers n ≥ 1.

7. Let aₖ = 2k + 1 and bₖ = (k - 1)³ + k + 2 for all integers k ≥ 0. Show that the first three terms of these sequences are identical but that their fourth terms differ.

Compute the first fifteen terms of each of the sequences in 8 and 9, and describe the general behavior of these sequences in words. (A definition of logarithm is given in Section 7.1.)

8. gₙ = ⌊log₂ n⌋ for all integers n ≥ 1.
9. hₙ = n⌊log₂ n⌋ for all integers n ≥ 1.

Find explicit formulas for sequences of the form a₁, a₂, a₃, . . . with the initial terms given in 10–16.

10. -1, 1, -1, 1, -1, 1
11. 0, 1, -2, 3, -4, 5
12. 1, 1/4, 1/9, 1/16, 1/25, 1/36
13. 1, -1/2, -1/2, -1/3, -1/3, -1/4, -1/4, -1/5, -1/5, -1/6, -1/6, -1/7
14. 1/3, 4/9, 9/27, 16/81, 25/243, 36/729
15. 0, -1/2, 1/3, -1/4, 2/5, -2/6, 3/7, -3/8
16. 3, 6, 12, 24, 48, 96

Write each of 40–42 as a single summation.

40. ∑ᵢ₌₀ⁿ i³ + ∑ᵢ₌₀ⁿ (k + 1)³

41. ∑ₖ₌₁ⁿ k² + ∑ₖ₌₁ⁿ (k + 1)²

42. ∑ₖ₌₁ⁿ k(k + 1) + ∑ₖ₌₁ⁿ (k + 1)(k + 2)

Compute the summations and products in 19–28.

19. ∑ₖ₌₁⁵ k

20. ∑ₖ₌₀⁴ (2m)

21. ∑ⱼ₌₀³ (j + 1)·2ʲ

22. ∑ⱼ₌₀² (-1)ʲ/(j + 1)

23. ∑ᵢ₌₁³ i(i + 1)

24. ∑ᵢ₌₁⁴ i(i + 2)

25. ∑ₖ₌₁ⁿ (1 - 1/k)

26. ∑ₖ₌₁ⁿ (1/k - 1/(k+1))

27. ∑ᵢ₌₁ⁿ (i² - 1)·(i + 1)

28. ∑ᵢ₌₁ⁿ 2ⁱ/(i(i!))

Write the summations in 29–32 in expanded form.

29. ∑ₖ₌₁ⁿ (k² + 3)

30. ∑ₖ₌₀⁵ (2k + 2n⁺¹)

31. ∑ᵢ₌₁ⁿ⁺¹ i(i!)

32. ∑ᵢ₌₁ⁿ i/(i + 1)

Evaluate the summations and products in 33–36 for the indicated values of the variable.

33. 1/1² + 1/2² + 1/3² + . . . + 1/n²; n = 1

34. 1(1!) + 2(2!) + 3(3!) + . . . + m(m!); m = 2

35. (1·2)/(3·4) - (2·3)/(4·5) + (3·4)/(5·6) - (4·5)/(6·7) + (5·6)/(7·8) - (6·7)/(8·9); k = 3

36. (1·2)/(3·4) - (2·3)/(4·5) + (3·4)/(5·6) - . . . + ((m-1)·m)/((m+1)·(m+2)); m = 1

Rewrite 37–39 by separating off the final term.

37. ∑ᵢ₌₁ᵏ⁺¹ i(i!)

38. ∑ₖ₌₁ᵐ⁺¹ k²

39. ∑ₖ₌₁ⁿ⁺¹ k(k - 1)

Write each of 43–52 using summation or product notation.

43. 1² - 2² + 3² - 4² + 5² - 6² + 7²

44. (1³ - 1) - (2³ - 1) + (3³ - 1) - (4³ - 1) + (5³ - 1)

45. (2² - 1)·(3² - 1)·(4² - 1)

46. 1 - r + r² - r³ + r⁴ - r⁵

47. 1 - r + r² - r³ + r⁴ - r⁵

48. (1 - t)·(1 - t²)·(1 - t³)·(1 - t⁴)

49. 13 + 23 + 33 + · · · + n³

50. 2/2! + 3/3! + 4/4! + · · · + (n+1)/(n+1)!

51. n + (n - 1) + (n - 2) + · · · + 1

52. n + n/2 + n/3 + n/4 + · · · + n/n

Transform each of 53 and 54 by making the change of variable i = k + 1.

53. ∑ₖ₌₋₁ⁿ⁻¹ (k + 1)²

54. ∑ₖ₌₂ⁿ k(k - 1)

Transform each of 55–58 by making the change of variable j = i - 1.

55. ∑ᵢ₌₁ⁿ (i - 1)²

56. ∑ᵢ₌₁ⁿ i·nᵢ

57. ∑ᵢ₌₃ⁿ i/(n - i + 1)

58. ∑ᵢ₌₃ⁿ⁺² i/(i + 1)

Write each of 59–61 as a single summation or product.

59. 3·∑ₖ₌₁ⁿ (2k - 3) + ∑ₖ₌₁ⁿ (4 - 5k)

60. 2·∑ₖ₌₁ⁿ (3k² + 4) + 5·∑ₖ₌₁ⁿ (2k² - 1)

61. (∑ₖ₌₁ⁿ k/(k + 1))·(∏ₖ₌₁ⁿ (k + 1)/(k + 2))

Compute each of 62–76. Assume the values of the variables are restricted so that the expressions are defined.

62. 6!/3!

63. 4!/8!

64. 4!/0!

65. (n - 1)!/n!

66. n!/(n + 1)!

67. n!/(n - 1)!

68. ((n + 1)!)²/(n!)²

69. n!/(n - k + 1)!

70. n!/(n - k)!

71. (5 3)

72. (7 4)

73. (3 0)

74. (5 5)

75. (n n-1)

76. (n+1 n-1)

Fill in the blanks below so that each algorithm segment performs the same job as the one given previously.

77. a. Prove that n! + 2 is divisible by 2, for all integers n ≥ 2.
   b. Prove that n! + k is divisible by k, for all integers n ≥ 2 and k = 2, 3, . . . , n.
   c. Given any integer m ≥ 2, is it possible to find a sequence of m - 1 consecutive positive integers none of which is prime? Explain your answer.

78. Prove that for all nonnegative integers n and r with r + 1 ≤ n,
```
(n - r r + 1) = (n r + 1)·(r + 1)/(n - r)
```

79. Prove that if p is a prime number and r is an integer with 0 < r < p, then (p r) is divisible by p.

80. Suppose a[1], a[2], a[3], . . . , a[m] is a one-dimensional array and consider the following algorithm segment:

```
sum := 0
for k := 1 to m
    sum := sum + a[k]
next k
```

Use repeated division by 2 to convert (by hand) the integers in 81–83 from base 10 to base 2.

81. 90

82. 98

83. 205

Make a trace table to trace the action of Algorithm 5.1.1 on the input in 84–86.

84. 23

85. 28

86. 44

87. Write an informal description of an algorithm (using repeated division by 16) to convert a nonnegative integer from decimal notation to hexadecimal notation (base 16).

Use the algorithm you developed for exercise 87 to convert the integers in 88–90 to hexadecimal notation.

88. 287

89. 693

90. 2,301

91. Write a formal version of the algorithm you developed for exercise 87.

## Answers for Test Yourself

1. the summation from k equals m to n of a-sub-k
2. aₘ + aₘ₊₁ + aₘ₊₂ + · · · + aₙ
3. a₁ + a₂
4. the product from k equals m to n of a-sub-k
5. n · (n - 1) · · · 3 · 2 · 1 (Or: n · (n - 1)!)
6. ∑ₖ₌ₘⁿ (aₖ + cbₖ)
7. ∏ₖ₌ₘⁿ (aₖ·bₖ)

---

## 5.2 Mathematical Induction I

**Page 244**

> [Mathematical induction is] the standard proof technique in computer science.
> — Anthony Ralston, 1984

Mathematical induction is one of the more recently developed techniques of proof in the history of mathematics. It is used to check conjectures about the outcomes of processes that occur repeatedly and according to definite patterns. We introduce the technique with an example.

Some people claim that the United States penny is such a small coin that it should be abolished. They point out that frequently a person who drops a penny on the ground does not even bother to pick it up. Other people argue that abolishing the penny would not give enough flexibility for pricing merchandise. What prices could still be paid with exact change if the penny were abolished and another coin worth 3¢ were introduced? The answer is that the only prices that could not be paid with exact change would be 1¢, 2¢, 4¢, and 7¢. In other words,

Any whole number of cents of at least 8¢ can be obtained using 3¢ and 5¢ coins.

More formally:
For all integers n ≥ 8, n cents can be obtained using 3¢ and 5¢ coins.

**Page 246**

### Principle of Mathematical Induction

Let P(n) be a property that is defined for integers n, and let a be a fixed integer. Suppose the following two statements are true:

1. P(a) is true.
2. For all integers k ≥ a, if P(k) is true then P(k + 1) is true.

Then the statement
```
for all integers n ≥ a, P(n)
```
is true.

### Method of Proof by Mathematical Induction

**Page 247**

Consider a statement of the form, "For all integers n ≥ a, a property P(n) is true."

To prove such a statement, perform the following two steps:

**Step 1 (basis step):** Show that P(a) is true.

**Step 2 (inductive step):** Show that for all integers k ≥ a, if P(k) is true then P(k + 1) is true. To perform this step:
- Suppose that P(k) is true, where k is any particular but arbitrarily chosen integer with k ≥ a. [This supposition is called the **inductive hypothesis**.]
- Then show that P(k + 1) is true.

### Proposition 5.2.1

**For all integers n ≥ 8, n¢ can be obtained using 3¢ and 5¢ coins.**

**Proof (by mathematical induction):**

Let the property P(n) be the sentence: n¢ can be obtained using 3¢ and 5¢ coins.

**Show that P(8) is true:**
P(8) is true because 8¢ can be obtained using one 3¢ coin and one 5¢ coin.

**Show that for all integers k ≥ 8, if P(k) is true then P(k+1) is also true:**

Suppose that k is any integer with k ≥ 8 such that k¢ can be obtained using 3¢ and 5¢ coins. [P(k) - inductive hypothesis]

We must show that (k + 1)¢ can be obtained using 3¢ and 5¢ coins. [P(k + 1)]

**Case 1** (There is a 5¢ coin among those used to make up the k¢): In this case replace the 5¢ coin by two 3¢ coins; the result will be (k + 1)¢.

**Case 2** (There is no 5¢ coin among those used to make up the k¢): Then 3¢ coins are used exclusively. Since k ≥ 8, at least three 3¢ coins must be included. Replace three 3¢ coins by two 5¢ coins to obtain (k + 1)¢.

[Since we have proved the basis step and the inductive step, we conclude that the proposition is true.]

The following example shows how to use mathematical induction to prove a formula for the sum of the first n integers.

### Example 5.2.1 Sum of the First n Integers

Use mathematical induction to prove that
```
1 + 2 + ··· + n = n(n + 1)/2
```
for all integers n ≥ 1.

**Solution**

To construct a proof by induction, you must first identify the property P(n). In this case, P(n) is the equation

```
1 + 2 + ··· + n = n(n + 1)/2
```

← P(n)

[To see that P(n) is a sentence, note that its subject is "the sum of the integers from 1 to n" and its verb is "equals."]

In the basis step of the proof, you must show that the property is true for n = 1, or, in other words that P(1) is true. Now P(1) is obtained by substituting 1 in place of n in P(n). The left-hand side of P(1) is the sum of all the successive integers starting at 1 and ending at 1. This is just 1. Thus P(1) is

Note To write P(1), just copy P(n) and replace each n by 1.

```
1 = 1(1 + 1)/2
```

← basis (P(1))

Of course, this equation is true because the right-hand side is
```
1·2/2 = 1,
```
which equals the left-hand side.

In the inductive step, you assume that P(k) is true, for a particular but arbitrarily chosen integer k with k ≥ 1. [This assumption is the inductive hypothesis.] You must then show that P(k + 1) is true. What are P(k) and P(k + 1)? P(k) is obtained by substituting k for every n in P(n). Thus P(k) is

Note To write P(k), just copy P(n) and replace each n by k.

```
1 + 2 + ··· + k = k(k + 1)/2
```

← P(k)
inductive hypothesis

Similarly, P(k + 1) is obtained by substituting the quantity (k + 1) for every n that appears in P(n). Thus P(k + 1) is

Note To write P(k + 1), just copy P(n) and replace each n by (k + 1).

```
1 + 2 + · · · + (k + 1) = (k + 1)((k + 1) + 1)/2
```
or, equivalently,

```
1 + 2 + · · · + (k + 1) = (k + 1)(k + 2)/2
```

← P(k + 1)

Now the inductive hypothesis is the supposition that P(k) is true. How can this supposition be used to show that P(k + 1) is true? P(k + 1) is an equation, and the truth of an equation can be shown in a variety of ways. One of the most straightforward is to use the inductive hypothesis along with algebra and other known facts to transform separately the left-hand and right-hand sides until you see that they are the same. In this case, the left-hand side of P(k + 1) is

```
1 + 2 + · · · + (k + 1),
```

which equals

The next-to-last term is k because the terms are successive integers and the last term is k + 1.

```
(1 + 2 + · · · + k) + (k + 1)
```

But by substitution from the inductive hypothesis,

```
(1 + 2 + · · · + k) + (k + 1) = k(k + 1)/2 + (k + 1)
```

since the inductive hypothesis says that 1 + 2 + · · · + k = k(k + 1)/2

```
= k(k + 1)/2 + 2(k + 1)/2
= (k² + k + 2k + 2)/2
= (k² + 3k + 2)/2
```

by multiplying the numerator and denominator of the second term by 2 to obtain a common denominator

by multiplying out the two numerators
by adding fractions with the same denominator and combining like terms.

So the left-hand side of P(k + 1) is (k² + 3k + 2)/2. Now the right-hand side of P(k + 1) is

```
(k + 1)(k + 2)/2 = (k² + 3k + 2)/2
```

by multiplying out the numerator.

Thus the two sides of P(k + 1) are equal to each other, and so the equation P(k + 1) is true.

This discussion is summarized as follows:

### Theorem 5.2.2 Sum of the First n Integers

For all integers n ≥ 1,
```
1 + 2 + ··· + n = n(n + 1)/2
```

**Proof (by mathematical induction):**

Let the property P(n) be the equation
```
1 + 2 + 3 + ··· + n = n(n + 1)/2
```

← P(n)

**Show that P(1) is true:**
To establish P(1), we must show that
```
1 = 1(1 + 1)/2
```
← P(1)

But the left-hand side of this equation is 1 and the right-hand side is
```
1(1 + 1)/2 = 1·2/2 = 1
```
also. Hence P(1) is true.

**Show that for all integers k ≥ 1, if P(k) is true then P(k + 1) is also true:**

[Suppose that P(k) is true for a particular but arbitrarily chosen integer k ≥ 1. That is:]
Suppose that k is any integer with k ≥ 1 such that
```
1 + 2 + 3 + ··· + k = k(k + 1)/2
```
← P(k)
inductive hypothesis

[We must show that P(k + 1) is true. That is:]
We must show that
```
1 + 2 + 3 + · · · + (k + 1) = (k + 1)[(k + 1) + 1]/2
```
or, equivalently, that
```
1 + 2 + 3 + · · · + (k + 1) = (k + 1)(k + 2)/2
```
← P(k + 1)

[We will show that the left-hand side and the right-hand side of P(k + 1) are equal to the same quantity and thus are equal to each other.]
The left-hand side of P(k + 1) is
```
1 + 2 + 3 + · · · + (k + 1)
= 1 + 2 + 3 + · · · + k + (k + 1)
= k(k + 1)/2 + (k + 1)
```

by making the next-to-last term explicit
by substitution from the inductive hypothesis

```
= k(k + 1)/2 + 2(k + 1)/2
= (k² + k)/2 + (2k + 2)/2
= (k² + k + 2k + 2)/2
= (k² + 3k + 2)/2
```

by algebra.

And the right-hand side of P(k + 1) is
```
(k + 1)(k + 2)/2 = (k² + 3k + 2)/2
```

Thus the two sides of P(k + 1) are equal to the same quantity and so they are equal to each other. Therefore the equation P(k + 1) is true [as was to be shown].
[Since we have proved both the basis step and the inductive step, we conclude that the theorem is true.]

**Page 279**

3 . . . . . . 50

51 . . . . . . 98

99

100

→

→

→

→

→

→

→

→

1 2

→

The story is told that one of the greatest mathematicians of all time, Carl Friedrich Gauss (1777–1855), was given the problem of adding the numbers from 1 to 100 by his teacher when he was a young child. The teacher had asked his students to compute the sum, supposedly to gain himself some time to grade papers. But after just a few moments, Gauss produced the correct answer. Needless to say, the teacher was dumbfounded. How could young Gauss have calculated the quantity so rapidly? In his later years, Gauss explained that he had imagined the numbers paired according to the following schema.

sum is 101
sum is 101
sum is 101
sum is 101

The sum of the numbers in each pair is 101, and there are 50 pairs in all; hence the total sum is 50· 101 = 5,050.

• Definition Closed Form
If a sum with a variable number of terms is shown to be equal to a formula that does not contain either an ellipsis or a summation symbol, we say that it is written in closed form.

For example, writing 1 + 2 + 3 + · · · + n = n(n + 1)/2 expresses the sum 1 + 2 + 3 + · · · + n in closed form.

### Example 5.2.2 Applying the Formula for the Sum of the First n Integers

a. Evaluate 2 + 4 + 6 + · · · + 500.
b. Evaluate 5 + 6 + 7 + 8 + · · · + 50.
c. For an integer h ≥ 2, write 1 + 2 + 3 + · · · + (h − 1) in closed form.

**Solution**

a. 2 + 4 + 6 + · · · + 500 = 2· (1 + 2 + 3 + · · · + 250)
```
= 2· [250· 251/2]
= 62,750.
```

by applying the formula for the sum of the first n integers with n = 250

b. 5 + 6 + 7 + 8 + · · · + 50 = (1 + 2 + 3 + · · · + 50) − (1 + 2 + 3 + 4)
```
= [50· 51/2] − 10
= 1,265
```

by applying the formula for the sum of the first n integers with n = 50

c. 1 + 2 + 3 + · · · + (h − 1) = (h − 1) · [(h − 1) + 1]/2
```
= (h − 1)· h/2
```

by applying the formula for the sum of the first n integers with n = h − 1
since (h − 1) + 1 = h.

The next example asks for a proof of another famous and important formula in mathematics—the formula for the sum of a geometric sequence. In a geometric sequence, each term is obtained from the preceding one by multiplying by a constant factor. If the first term is 1 and the constant factor is r, then the sequence is 1, r, r², r³, . . . , rⁿ, . . . . The sum of the first n terms of this sequence is given by the formula

```
∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ − 1)/(r − 1)
```

for all integers n ≥ 0 and real numbers r not equal to 1. The expanded form of the formula is

```
r⁰ + r¹ + r² + · · · + rⁿ = (rⁿ⁺¹ − 1)/(r − 1),
```

and because r⁰ = 1 and r¹ = r, the formula for n ≥ 1 can be rewritten as

```
1 + r + r² + · · · + rⁿ = (rⁿ⁺¹ − 1)/(r − 1).
```

### Example 5.2.3 Sum of a Geometric Sequence

Prove that
```
∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ − 1)/(r − 1)
```
for all integers n ≥ 0 and all real numbers r except 1.

**Solution**

In this example the property P(n) is again an equation, although in this case it contains a real variable r:

```
∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ − 1)/(r − 1)
```

← the property (P(n))

Because r can be any real number other than 1, the proof begins by supposing that r is a particular but arbitrarily chosen real number not equal to 1. Then the proof continues by mathematical induction on n, starting with n = 0. In the basis step, you must show that P(0) is true; that is, you show the property is true for n = 0. So you substitute 0 for each n in P(n):

```
∑ᵢ₌₀⁰ rⁱ = (r⁰⁺¹ − 1)/(r − 1)
```

← basis (P(0))

In the inductive step, you suppose k is any integer with k ≥ 0 for which P(k) is true; that is, you suppose the property is true for n = k. So you substitute k for each n in P(n):

```
∑ᵢ₌₀ᵏ rⁱ = (rᵏ⁺¹ − 1)/(r − 1)
```

← inductive hypothesis (P(k))

Then you show that P(k + 1) is true; that is, you show the property is true for n = k + 1. So you substitute k + 1 for each n in P(n):

```
∑ᵢ₌₀ᵏ⁺¹ rⁱ = (r⁽ᵏ⁺¹⁾⁺¹ − 1)/(r − 1)
```
or, equivalently,

```
∑ᵢ₌₀ᵏ⁺¹ rⁱ = (rᵏ⁺² − 1)/(r − 1)
```

← to show (P(k + 1))

In the inductive step for this proof we use another common technique for showing that an equation is true: We start with the left-hand side and transform it step-by-step into the right-hand side using the inductive hypothesis together with algebra and other known facts.

### Theorem 5.2.3 Sum of a Geometric Sequence

For any real number r except 1, and any integer n ≥ 0,
```
∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ − 1)/(r − 1)
```

**Proof (by mathematical induction):**

Suppose r is a particular but arbitrarily chosen real number that is not equal to 1, and let the property P(n) be the equation
```
∑ᵢ₌₀ⁿ rⁱ = (rⁿ⁺¹ − 1)/(r − 1)
```

← P(n)

We must show that P(n) is true for all integers n ≥ 0. We do this by mathematical induction on n.

**Show that P(0) is true:**
To establish P(0), we must show that
```
∑ᵢ₌₀⁰ rⁱ = (r⁰⁺¹ − 1)/(r − 1)
```
← P(0)

The left-hand side of this equation is r⁰ = 1 and the right-hand side is
```
(r⁰⁺¹ − 1)/(r − 1) = (r − 1)/(r − 1) = 1
```
also because r¹ = r and r ≠ 1. Hence P(0) is true.

**Show that for all integers k ≥ 0, if P(k) is true then P(k + 1) is also true:**

[Suppose that P(k) is true for a particular but arbitrarily chosen integer k ≥ 0. That is:]

Let k be any integer with k ≥ 0, and suppose that
```
∑_{i=0}^{k} r^i = \frac{r^{k+1} - 1}{r - 1}
```

← P(k)
inductive hypothesis

[We must show that P(k + 1) is true. That is:] We must show that
```
∑_{i=0}^{k+1} r^i = \frac{r^{(k + 1) + 1} - 1}{r - 1}
```
or, equivalently, that
```
∑_{i=0}^{k+1} rⁱ = (r^{k+2} − 1)/(r − 1)
```

← P(k + 1)

[We will show that the left-hand side of P(k + 1) equals the right-hand side.]

The left-hand side of P(k + 1) is
```
∑_{i=0}^{k+1} rⁱ = ∑_{i=0}^k rⁱ + r^{k+1}
```

by writing the (k + 1)st term separately from the first k terms

```
= (r^{k+1} − 1)/(r − 1) + r^{k+1}
```

by substitution from the inductive hypothesis

```
= (r^{k+1} − 1)/(r − 1) + r^{k+1}(r − 1)/(r − 1)
```

by multiplying the numerator and denominator of the second term by (r − 1) to obtain a common denominator

```
= (r^{k+1} − 1 + r^{k+1}(r − 1))/(r − 1)
= (r^{k+1} − 1 + r^{k+2} − r^{k+1})/(r − 1)
= (r^{k+2} − 1)/(r − 1)
```

by adding fractions
by multiplying out and using the fact that r^{k+1} · r = r^{k+1} · r¹ = r^{k+2}

by canceling the r^{k+1}'s.

which is the right-hand side of P(k + 1) [as was to be shown.]
[Since we have proved the basis step and the inductive step, we conclude that the theorem is true.]

### Proving an Equality

The proofs of the basis and inductive steps in Examples 5.2.1 and 5.2.3 illustrate two different ways to show that an equation is true: (1) transforming the left-hand side and the right-hand side independently until they are seen to be equal, and (2) transforming one side of the equation until it is seen to be the same as the other side of the equation.

Sometimes people use a method that they believe proves equality but that is actually invalid. For example, to prove the basis step for Theorem 5.2.3, they perform the following steps:

```
∑_{i=0}^0 rⁱ = (r^{0+1} − 1)/(r − 1)
r⁰ = (r¹ − 1)/(r − 1)
1 = (r − 1)/(r − 1)
$1 = 1$
```

! Caution!

Don't do this!

The problem with this method is that starting from a statement and deducing a true conclusion does not prove that the statement is true. A true conclusion can also be deduced from a false statement. For instance, the steps below show how to deduce the true conclusion that $1 = 1$ from the false statement that 1 = 0:

```
1 = 0
0 = 1
1 + 0 = 0 + 1
$1 = 1$
```

← false

← true

When using mathematical induction to prove formulas, be sure to use a method that avoids invalid reasoning, both for the basis step and for the inductive step.

### Deducing Additional Formulas

The formula for the sum of a geometric sequence can be thought of as a family of different formulas in r, one for each real number r except 1.

### Example 5.2.4 Applying the Formula for the Sum of a Geometric Sequence

In each of (a) and (b) below, assume that m is an integer that is greater than or equal to 3. Write each of the sums in closed form.

a. 1 + 3 + 3² + · · · + 3^{m−2}
b. 3² + 3³ + 3⁴ + · · · + 3ᵐ

**Solution**

a. 1 + 3 + 3² + · · · + 3^{m−2} = (3^{(m−2)+1} − 1)/(3 − 1)
```
= (3^{m−1} − 1)/2
```

by applying the formula for the sum of a geometric sequence with r = 3 and n = m − 2

b. 3² + 3³ + 3⁴ + · · · + 3ᵐ = 3² · (1 + 3 + 3² + · · · + 3^{m−2})
```
= 9 · [(3^{m−1} − 1)/2]
```

by factoring out 3²
by part (a).

As with the formula for the sum of the first n integers, there is a way to think of the formula for the sum of the terms of a geometric sequence that makes it seem simple and intuitive. Let

```
S_n = 1 + r + r² + · · · + rⁿ.
```

Then
```
rS_n = r + r² + r³ + · · · + r^{n+1},
```
and so
```
rS_n − S_n = (r + r² + r³ + · · · + r^{n+1}) − (1 + r + r² + · · · + rⁿ)
= r^{n+1} − 1.
```

But
```
rS_n − S_n = (r − 1)S_n.
```

Equating the right-hand sides of equations (5.2.1) and (5.2.2) and dividing by r − 1 gives
```
S_n = (r^{n+1} − 1)/(r − 1).
```

This derivation of the formula is attractive and is quite convincing. However, it is not as logically airtight as the proof by mathematical induction. To go from one step to another in the previous calculations, the argument is made that each term among those indicated by the ellipsis (. . .) has such-and-such an appearance and when these are canceled such-and-such occurs. But it is impossible actually to see each such term and each such calculation, and so the accuracy of these claims cannot be fully checked. With mathematical induction it is possible to focus exactly on what happens in the middle of the ellipsis and verify without doubt that the calculations are correct.

## Test Yourself

1. Mathematical induction is a method for proving that a property defined for integers n is true for all values of n that are _____.

2. Let P(n) be a property defined for integers n and consider constructing a proof by mathematical induction for the statement "P(n) is true for all n ≥ a."
   (a) In the basis step one must show that _____.
   (b) In the inductive step one supposes that _____ for some particular but arbitrarily chosen value of an integer k ≥ a. This supposition is called the _____. One then has to show that _____.

## Exercise Set 5.2

1. Use mathematical induction (and the proof of Proposition 5.2.1 as a model) to show that any amount of money of at least 14¢ can be made up using 3¢ and 8¢ coins.

2. Use mathematical induction to show that any postage of at least 12¢ can be obtained using 3¢ and 7¢ stamps.

3. For each positive integer n, let P(n) be the formula
   1² + 2² + · · · + n² = n(n + 1)(2n + 1)/6
   a. Write P(1). Is P(1) true?
   b. Write P(k).
   c. Write P(k + 1).
   d. In a proof by mathematical induction that the formula holds for all integers n ≥ 1, what must be shown in the inductive step?

4. For each integer n with n ≥ 2, let P(n) be the formula
   ∑_{i=1}^{n-1} i(i + 1) = n(n − 1)(n + 1)/3
   a. Write P(2). Is P(2) true?
   b. Write P(k).
   c. Write P(k + 1).
   d. In a proof by mathematical induction that the formula holds for all integers n ≥ 2, what must be shown in the inductive step?

5. Fill in the missing pieces in the following proof that
   1 + 3 + 5 + · · · + (2n − 1) = n²
   for all integers n ≥ 1.

**Proof:** Let the property P(n) be the equation
   1 + 3 + 5 + · · · + (2n − 1) = n². ← P(n)

   Show that P(1) is true: To establish P(1), we must show
   that when 1 is substituted in place of n, the left-hand side
   equals the right-hand side. But when n = 1, the left-hand side is the sum of all the odd integers from 1 to 2·1 − 1, which is the sum of the odd integers from 1 to 1, which is just 1. The right-hand side is (a) , which also equals 1. So P(1) is true.

   Show that for all integers k ≥ 1, if P(k) is true then P(k + 1) is true: Let k be any integer with k ≥ 1.
   [Suppose P(k) is true. That is:]
   Suppose 1 + 3 + 5 + · · · + (2k − 1) = (b) . ← P(k)
   [This is the inductive hypothesis.]
   [We must show that P(k + 1) is true. That is:]
   We must show that
   (c) = (d) . ← P(k + 1)

   But the left-hand side of P(k + 1) is
   $1 + 3 + 5 + \cdots + (2(k + 1) - 1)$
   = 1 + 3 + 5 + · · · + (2k + 1)
   by algebra
   = [1 + 3 + 5 + · · · + (2k − 1)] + (2k + 1)
   the next-to-last term is 2k − 1 because (e)
   by (f)
   = k² + (2k + 1)
   = (k + 1)²

   which is the right-hand side of P(k + 1) [as was to be shown.]
   [Since we have proved the basis step and the inductive step, we
   conclude that the given statement is true.]

Prove each statement in 6–9 using mathematical induction. Do not derive them from Theorem 5.2.2 or Theorem 5.2.3.

6. For all integers n ≥ 1, 2 + 4 + 6 + · · · + 2n = n² + n.

7. For all integers n ≥ 1,
   1 + 6 + 11 + 16 + · · · + (5n − 4) = n(5n − 3)/2.

8. For all integers n ≥ 0, 1 + 2 + 2² + · · · + 2ⁿ = 2ⁿ⁺¹ − 1.

9. For all integers n ≥ 3,
   4³ + 4⁴ + 4⁵ + · · · + 4ⁿ = 4(4ⁿ − 16)/3.

Prove each of the statements in 10–17 by mathematical induction:

10. 1² + 2² + · · · + n² = n(n + 1)(2n + 1)/6, for all integers n ≥ 1.

11. 1³ + 2³ + · · · + n³ = [n(n + 1)/2]², for all integers n ≥ 1.

12. ∑_{i=1}^{n-1} i(i + 1) = n(n − 1)(n + 1)/3, for all integers n ≥ 2.

13. ∑_{i=1}^n i·2ⁱ = n·2^{n+2} + 2, for all integers n ≥ 0.

14. ∑_{i=1}^n i(i!) = (n + 1)! − 1, for all integers n ≥ 1.

15. (1 − 1/2)(1 − 1/3)(1 − 1/4)···(1 − 1/n) = 1/n, for all integers n ≥ 2.

16. ∏_{i=0}^n [1/(2i + 1) · 1/(2i + 2)] = 1/(2n + 2)!, for all integers n ≥ 0.

17. ∏_{i=0}^n 1/(2i + 1) × 1/(2i + 2) = 1/(2n + 2)!, for all integers n ≥ 0.

18. If x is a real number not divisible by π, then for all integers n ≥ 1,
   sin x + sin 3x + sin 5x + · · · + sin(2n − 1)x = (1 − cos 2nx)/(2 sin x).

19. (For students who have studied calculus) Use mathematical induction, the product rule from calculus, and the facts that d(x)/dx = 1 and that x^{k+1} = x·x^k to prove that for all integers n ≥ 1,
   d(xⁿ)/dx = nx^{n−1}.

Use the formula for the sum of the first n integers and/or the formula for the sum of a geometric sequence to evaluate the sums in 20–29 or to write them in closed form.

20. 4 + 8 + 12 + 16 + · · · + 200

21. 5 + 10 + 15 + 20 + · · · + 300

22. 3 + 4 + 5 + 6 + · · · + 1000

23. 7 + 8 + 9 + 10 + · · · + 600

24. 1 + 2 + 3 + · · · + (k − 1), where k is an integer and k ≥ 2.

25. a. 1 + 2 + 2² + · · · + 2^{25}
   b. 2 + 2² + 2³ + · · · + 2^{26}

26. 3 + 3² + 3³ + · · · + 3ⁿ, where n is an integer with n ≥ 1

27. 5³ + 5⁴ + 5⁵ + · · · + 5ᵏ, where k is any integer with k ≥ 3.

28. 1 + 1/2 + 1/4 + · · · + 1/2ⁿ, where n is a positive integer

29. 1 − 2 + 2² − 2³ + · · · + (−1)ⁿ 2ⁿ, where n is a positive integer

30. Find a formula in n, a, m, and d for the sum (a + md) + (a + (m + 1)d) + (a + (m + 2)d) + · · · + (a + (m + n)d), where m and n are integers, n ≥ 0, and a and d are real numbers. Justify your answer.

31. Find a formula in a, r, m, and n for the sum
   arᵐ + ar^{m+1} + ar^{m+2} + · · · + ar^{m+n}
   where m and n are integers, n ≥ 0, and a and r are real numbers. Justify your answer.

32. You have two parents, four grandparents, eight great-grandparents, and so forth.
   a. If all your ancestors were distinct, what would be the total number of your ancestors for the past 40 generations (counting your parents' generation as number one)? (Hint: Use the formula for the sum of a geometric sequence.)
   b. Assuming that each generation represents 25 years, how long is 40 generations?
   c. The total number of people who have ever lived is approximately 10 billion, which equals 10¹⁰ people. Compare this fact with the answer to part (a). What do you deduce?

Find the mistakes in the proof fragments in 33–35.

33. Theorem: For any integer n ≥ 1, 1² + 2² + · · · + n² = n(n + 1)(2n + 1)/6.
   "Proof (by mathematical induction): Certainly the theorem is true for n = 1 because 1² = 1 and 1(1 + 1)(2·1 + 1)/6 = 1. So the basis step is true. For the inductive step, suppose that for some integer k ≥ 1, k² = k(k + 1)(2k + 1)/6. We must show that (k + 1)² = (k + 1)((k + 1) + 1)(2(k + 1) + 1)/6."

34. Theorem: For any integer n ≥ 0, ∑_{i=0}^n i(i!) = (n + 1)! − 1.
   "Proof (by mathematical induction): Let the property P(n) be ∑_{i=0}^n i(i!) = (n + 1)! − 1. Show that P(1) is true: When n = 1, ∑_{i=0}^1 i(i!) = (1 + 1)! − 1, so 1(1!) = 2! − 1, and $1 = 1$. Thus P(1) is true."

35. Theorem: For any integer n ≥ 0, 1 + 2 + 2² + · · · + 2ⁿ = 2ⁿ⁺¹ − 1.
   "Proof (by mathematical induction): Let the property P(n) be 1 + 2 + 2² + · · · + 2ⁿ = 2ⁿ⁺¹ − 1. Show that P(0) is true: The left-hand side of P(0) is 1 + 2 + 2² + · · · + 2⁰ = 1 and the right-hand side is 2^{0+1} − 1 = 2 − $1 = 1$ also. So P(0) is true."

36. Use Theorem 5.2.2 to prove that if m and n are any positive integers and m is odd, then ∑_{k=0}^{m-1} (n + k) is divisible by m. Does the conclusion hold if m is even? Justify your answer.

37. Use Theorem 5.2.2 and the result of exercise 10 to prove that if p is any prime number with p ≥ 5, then the sum of squares of any p consecutive integers is divisible by p.

## Answers for Test Yourself

1. greater than or equal to some initial value 2. (a) P(a) is true (b) P(k) is true; inductive hypothesis; P(k + 1) is true

---

## 5.6 Defining Sequences Recursively

**Page 318**

> So, Nat'ralists observe, a Flea/Hath smaller Fleas that on him prey,/And these have smaller Fleas to bite 'em,/And so proceed ad inﬁnitum. — Jonathan Swift, 1733

A sequence can be deﬁned in a variety of different ways. One informal way is to write the ﬁrst few terms with the expectation that the general pattern will be obvious. We might say, for instance, "consider the sequence 3, 5, 7, . . .." Unfortunately, misunderstandings can occur when this approach is used. The next term of the sequence could be 9 if we mean a sequence of odd integers, or it could be 11 if we mean the sequence of odd prime numbers.

The second way to deﬁne a sequence is to give an explicit formula for its nth term. For example, a sequence a₀, a₁, a₂, . . . can be speciﬁed by writing:

```
aₙ = (-1)ⁿ/(n+1) for all integers n ≥ 0.
```

The advantage of deﬁning a sequence by such an explicit formula is that each term of the sequence is uniquely determined and can be computed in a ﬁxed, ﬁnite number of steps, by substitution.

The third way to deﬁne a sequence is to use recursion. This requires giving both an equation, called a recurrence relation, that deﬁnes each later term in the sequence by reference to earlier terms and also one or more initial values for the sequence.

Sometimes it is very diﬃcult or impossible to ﬁnd an explicit formula for a sequence, but it is possible to deﬁne the sequence using recursion. Note that deﬁning sequences recursively is similar to proving theorems by mathematical induction. The recurrence relation is like the inductive step and the initial conditions are like the basis step. Indeed, the fact that sequences can be deﬁned recursively is equivalent to the fact that mathematical induction works as a method of proof.

### Deﬁnition: Recurrence Relation and Initial Conditions

A recurrence relation for a sequence a₀, a₁, a₂, . . . is a formula that relates each term aₖ to certain of its predecessors aₖ₋₁, aₖ₋₂, . . . , aₖ₋ᵢ, where i is an integer with k − i ≥ 0. The initial conditions for such a recurrence relation specify the values of a₀, a₁, a₂, . . . , aᵢ₋₁, if i is a ﬁxed integer, or a₀, a₁, . . . , aₘ, where m is an integer with m ≥ 0, if i depends on k.

**Page 319**

### Example 5.6.1 Computing Terms of a Recursively Deﬁned Sequence

Deﬁne a sequence c₀, c₁, c₂, . . . recursively as follows: For all integers k ≥ 2,

(1) cₖ = cₖ₋₁ + kcₖ₋₂ + 1 (recurrence relation)
(2) c₀ = 1 and c₁ = 2 (initial conditions)

Find c₂, c₃, and c₄.

**Solution**

```
c₂ = c₁ + 2c₀ + 1
   = 2 + 2·1 + 1 = 5    [by substituting k = 2 into (1)]

c₃ = c₂ + 3c₁ + 1
   = 5 + 3·2 + 1 = 12   [by substituting k = 3 into (1)]

c₄ = c₃ + 4c₂ + 1
   = 12 + 4·5 + 1 = 33  [by substituting k = 4 into (1)]
```

### Example 5.6.2 Writing a Recurrence Relation in More Than One Way

Let s₀, s₁, s₂, . . . be a sequence that satisﬁes the following recurrence relation:

For all integers k ≥ 1, sₖ = 3sₖ₋₁ − 1.

Explain why the following statement is true:

For all integers k ≥ 0, sₖ₊₁ = 3sₖ − 1.

**Solution**

In informal language, the recurrence relation says that any term of the sequence equals 3 times the previous term minus 1. Now for any integer k ≥ 0, the term previous to sₖ₊₁ is sₖ. Thus for any integer k ≥ 0, sₖ₊₁ = 3sₖ − 1.

**Page 320**

### Example 5.6.3 Sequences That Satisfy the Same Recurrence Relation

Let a₁, a₂, a₃, . . . and b₁, b₂, b₃, . . . satisfy the recurrence relation that the kth term equals 3 times the (k − 1)st term for all integers k ≥ 2:

(1) aₖ = 3aₖ₋₁ and bₖ = 3bₖ₋₁.

But suppose that the initial conditions for the sequences are different:

(2) a₁ = 2 and b₁ = 1.

Find (a) a₂, a₃, a₄ and (b) b₂, b₃, b₄.

**Solution**

a. a₂ = 3a₁ = 3 · 2 = 6
   a₃ = 3a₂ = 3 · 6 = 18
   a₄ = 3a₃ = 3 · 18 = 54
   Thus a₁, a₂, a₃, . . . begins 2, 6, 18, 54, . . .

b. b₂ = 3b₁ = 3 · 1 = 3
   b₃ = 3b₂ = 3 · 3 = 9
   b₄ = 3b₃ = 3 · 9 = 27
   Thus b₁, b₂, b₃, . . . begins 1, 3, 9, 27, . . .

### Example 5.6.4 Showing That a Sequence Given by an Explicit Formula Satisﬁes a Certain Recurrence Relation

The sequence of Catalan numbers, named after the Belgian mathematician Eugène Catalan (1814–1894), arises in a remarkable variety of different contexts in discrete mathematics. It can be deﬁned as follows: For each integer n ≥ 1,

```
Cₙ = (1/(n+1)) · (2n choose n)
```

a. Find C₁, C₂, and C₃.
b. Show that this sequence satisﬁes the recurrence relation Cₖ = (4k−2)/(k+1) · Cₖ₋₁ for all integers k ≥ 2.

**Solution**

a. C₁ = (1/2) · (2 choose 1) = (1/2) · 2 = 1
   C₂ = (1/3) · (4 choose 2) = (1/3) · 6 = 2
   C₃ = (1/4) · (6 choose 3) = (1/4) · 20 = 5

b. To obtain the kth and (k − 1)st terms of the sequence, just substitute k and k − 1 in place of n in the explicit formula:

```
Cₖ = (1/(k+1)) · (2k choose k)
Cₖ₋₁ = (1/k) · (2(k-1) choose k-1) = (1/k) · (2k-2 choose k-1)
```

Then start with the right-hand side of the recurrence relation and transform it into the left-hand side:

For each integer k ≥ 2,

```
(4k-2)/(k+1) · Cₖ₋₁ = (4k-2)/(k+1) · (1/k) · (2k-2 choose k-1)
                  = (2(2k-1))/(k+1) · (1/k) · ((2k-2)!)/((k-1)!(k-1)!)
                  = (1/(k+1)) · (2(2k-1))/k · ((2k-2)!)/((k-1)!(k-1)!)
                  = (1/(k+1)) · (1/k) · 2(2k-1) · ((2k-2)!)/((k-1)!(k-1)!)
                  = (1/(k+1)) · (1/2) · (1/k) · 2k · (2k-1) · (2k-2)!/(k!(k-1)!)
                  = (1/(k+1)) · (1/k) · (2k)!/(k!(k-1)!)
                  = (1/(k+1)) · (2k)!/(k!k!)
                  = (1/(k+1)) · (2k choose k)
                  = Cₖ
```

**Page 321-322**

### Examples of Recursively Deﬁned Sequences

Recursion is one of the central ideas of computer science. To solve a problem recursively means to ﬁnd a way to break it down into smaller subproblems each having the same form as the original problem—and to do this in such a way that when the process is repeated many times, the last of the subproblems are small and easy to solve and the solutions of the subproblems can be woven together to form a solution to the original problem.

Probably the most diﬃcult part of solving problems recursively is to ﬁgure out how knowing the solution to smaller subproblems of the same type as the original problem will give you a solution to the problem as a whole. You suppose you know the solutions to smaller subproblems and ask yourself how you would best make use of that knowledge to solve the larger problem. The supposition that the smaller subproblems have already been solved has been called the recursive paradigm or the recursive leap of faith. Once you take this leap, you are right in the middle of the most diﬃcult part of the problem, but generally, the path to a solution from this point, though diﬃcult, is short. The recursive leap of faith is similar to the inductive hypothesis in a proof by mathematical induction.

### Example 5.6.5 The Tower of Hanoi

In 1883 a French mathematician, Édouard Lucas, invented a puzzle that he called The Tower of Hanoi (La Tour D'Hanoï). The puzzle consisted of eight disks of wood with holes in their centers, which were piled in order of decreasing size on one pole in a row of three. Those who played the game were supposed to move all the disks one by one from one pole to another, never placing a larger disk on top of a smaller one.

The directions to the puzzle claimed it was based on an old Indian legend: On the steps of the altar in the temple of Benares, for many, many years Brahmins have been moving a tower of 64 golden disks from one pole to another; one by one, never placing a larger on top of a smaller. When all the disks have been transferred the Tower and the Brahmins will fall, and it will be the end of the world.

The puzzle offered a prize of ten thousand francs (about $34,000 US today) to anyone who could move a tower of 64 disks by hand while following the rules of the game. Assuming that you transferred the disks as eﬃciently as possible, how many moves would be required to win the prize?

**Solution**

An elegant and eﬃcient way to solve this problem is to think recursively. Suppose that you, somehow or other, have found the most eﬃcient way possible to transfer a tower of k − 1 disks one by one from one pole to another, obeying the restriction that you never place a larger disk on top of a smaller one. What is the most eﬃcient way to transfer a tower of k disks from one pole to another? The answer is described as follows:

**Step 1**: Transfer the top k − 1 disks from pole A to pole B.
**Step 2**: Move the bottom disk from pole A to pole C.
**Step 3**: Transfer the top k − 1 disks from pole B to pole C.

To see that this sequence of moves is most eﬃcient, observe that to move the bottom disk of a stack of k disks from one pole to another, you must ﬁrst transfer the top k − 1 disks to a third pole to get them out of the way. Thus transferring the stack of k disks from pole A to pole C requires at least two transfers of the top k − 1 disks: one to transfer them off the bottom disk to free the bottom disk so that it can be moved and another to transfer them back on top of the bottom disk after the bottom disk has been moved to pole C.

Thus the minimum sequence of moves must include going from the initial position (a) to position (b) to position (c) to position (d). It follows that:

```
[the minimum number of moves needed to transfer a tower of k disks from pole A to pole C] =
[the minimum moves needed to go from position (a) to (b)] +
[the minimum moves needed to go from position (b) to (c)] +
[the minimum moves needed to go from position (c) to (d)]
```

For each integer n ≥ 1, let

```
mₙ = the minimum number of moves needed to transfer a tower of n disks from one pole to another
```

Note that the numbers mₙ are independent of the labeling of the poles. Also the values of mₙ are independent of the number of larger disks that may lie below the top n, provided these remain stationary while the top n are moved.

Going from position (a) to position (b) requires mₖ₋₁ moves, going from position (b) to position (c) requires just one move, and going from position (c) to position (d) requires mₖ₋₁ moves. By substitution, therefore,

```
mₖ = mₖ₋₁ + 1 + mₖ₋₁ = 2mₖ₋₁ + 1 for all integers k ≥ 2.
```

The initial condition is:

```
m₁ = 1 (only one move is needed to move one disk)
```

Hence the complete recursive speciﬁcation is:

(1) mₖ = 2mₖ₋₁ + 1 for all integers k ≥ 2 (recurrence relation)
(2) m₁ = 1 (initial condition)

Here is a computation of the next ﬁve terms:

```
m₂ = 2m₁ + 1 = 2·1 + 1 = 3
m₃ = 2m₂ + 1 = 2·3 + 1 = 7
m₄ = 2m₃ + 1 = 2·7 + 1 = 15
m₅ = 2m₄ + 1 = 2·15 + 1 = 31
m₆ = 2m₅ + 1 = 2·31 + 1 = 63
```

For the original problem with 64 disks, m₆₄ ≈ 1.844674 × 10¹⁹ seconds, which is approximately 584.5 billion years.

**Page 323-324**

### Example 5.6.6 The Fibonacci Numbers

One of the earliest examples of a recursively deﬁned sequence arises in the writings of Leonardo of Pisa, commonly known as Fibonacci, who was the greatest European mathematician of the Middle Ages. In 1202 Fibonacci posed the following problem:

A single pair of rabbits (male and female) is born at the beginning of a year. Assume the following conditions:

1. Rabbit pairs are not fertile during their ﬁrst month of life but thereafter give birth to one new male/female pair at the end of every month.
2. No rabbits die.

How many rabbits will there be at the end of the year?

**Solution**

The crucial observation is that the number of rabbit pairs born at the end of month k is the same as the number of pairs alive at the end of month k − 2. Because it is exactly the rabbit pairs that were alive at the end of month k − 2 that were fertile during month k. The rabbits born at the end of month k − 1 were not.

Now the number of rabbit pairs alive at the end of month k equals the ones alive at the end of month k − 1 plus the pairs newly born at the end of the month. Thus:

```
[the number of rabbit pairs alive at the end of month k] =
[the number of rabbit pairs alive at the end of month k − 1] +
[the number of rabbit pairs alive at the end of month k − 2]
```

For each integer n ≥ 1, let

```
Fₙ = the number of rabbit pairs alive at the end of month n
```

and let

```
F₀ = the initial number of rabbit pairs = 1
```

Then by substitution, for all integers k ≥ 2,

```
Fₖ = Fₖ₋₁ + Fₖ₋₂
```

Now F₀ = 1, as already noted, and F₁ = 1 also, because the ﬁrst pair of rabbits is not fertile until the second month. Hence the complete speciﬁcation is:

(1) Fₖ = Fₖ₋₁ + Fₖ₋₂ for all integers k ≥ 2 (recurrence relation)
(2) F₀ = 1, F₁ = 1 (initial conditions)

To answer Fibonacci's question, compute F₂ through F₁₂:

```
F₂ = F₁ + F₀ = 1 + 1 = 2
F₃ = F₂ + F₁ = 2 + 1 = 3
F₄ = F₃ + F₂ = 3 + 2 = 5
F₅ = F₄ + F₃ = 5 + 3 = 8
F₆ = F₅ + F₄ = 8 + 5 = 13
F₇ = F₆ + F₅ = 13 + 8 = 21
F₈ = F₇ + F₆ = 21 + 13 = 34
F₉ = F₈ + F₇ = 34 + 21 = 55
F₁₀ = F₉ + F₈ = 55 + 34 = 89
F₁₁ = F₁₀ + F₉ = 89 + 55 = 144
F₁₂ = F₁₁ + F₁₀ = 144 + 89 = 233
```

At the end of the twelfth month there are 233 rabbit pairs, or 466 rabbits in all.

**Page 325-326**

### Example 5.6.7 Compound Interest

On your twenty-ﬁrst birthday you get a letter informing you that on the day you were born an eccentric rich aunt deposited $100,000 in a bank account earning 4% interest compounded annually and she now intends to turn the account over to you, provided you can ﬁgure out how much it is worth. What is the amount currently in the account?

**Solution**

To approach this problem recursively, observe that:

```
[the amount in the account at the end of any particular year] =
[the amount in the account at the end of the previous year] +
[the interest earned on the account during the year]
```

Now the interest earned during the year equals the interest rate, 4% = 0.04 times the amount in the account at the end of the previous year. Thus:

```
[the amount in the account at the end of any particular year] =
[the amount in the account at the end of the previous year] + (0.04)·[the amount in the account at the end of the previous year]
```

For each positive integer n, let

```
Aₙ = the amount in the account at the end of year n
```

and let

```
A₀ = the initial amount in the account = $100,000
```

Then for any particular year k,

```
Aₖ = Aₖ₋₁ + (0.04)·Aₖ₋₁ = (1 + 0.04)·Aₖ₋₁ = (1.04)·Aₖ₋₁
```

Consequently, the sequence is speciﬁed as:

(1) Aₖ = (1.04)·Aₖ₋₁ for all integers k ≥ 1 (recurrence relation)
(2) A₀ = $100,000 (initial condition)

The value on your twenty-ﬁrst birthday can be computed by repeated substitution:

```
A₁ = 1.04·A₀ = 1.04·$100,000 = $104,000
A₂ = 1.04·A₁ = 1.04·$104,000 = $108,160
A₃ = 1.04·A₂ = 1.04·$108,160 = $112,486.40
...
A₂₁ = 1.04·A₂₀ ≈ $227,876.81
```

The amount in the account is $227,876.81 (to the nearest cent).

**Page 327-328**

### Example 5.6.8 Compound Interest with Compounding Several Times a Year

When an annual interest rate of i is compounded m times per year, the interest rate paid per period is i/m. For instance, if 3% = 0.03 annual interest is compounded quarterly, then the interest rate paid per quarter is 0.03/4 = 0.0075.

For each integer k ≥ 1, let Pₖ = the amount on deposit at the end of the kth period, assuming no additional deposits or withdrawals. Then the interest earned during the kth period equals the amount on deposit at the end of the (k − 1)st period times the interest rate for the period:

```
interest earned during kth period = Pₖ₋₁·(i/m)
```

The amount on deposit at the end of the kth period, Pₖ, equals the amount at the end of the (k − 1)st period, Pₖ₋₁, plus the interest earned during the kth period:

```
Pₖ = Pₖ₋₁ + Pₖ₋₁·(i/m) = Pₖ₋₁(1 + i/m)
```

Suppose $10,000 is left on deposit at 3% compounded quarterly.

a. How much will the account be worth at the end of one year, assuming no additional deposits or withdrawals?
b. The annual percentage yield (APY) is the percentage increase in the value of the account over a one-year period. What is the APY for this account?

**Solution**

a. For each integer n ≥ 1, let Pₙ = the amount on deposit after n consecutive quarters, and let P₀ = $10,000. Then by the formula above with i = 0.03 and m = 4:

(1) Pₖ = Pₖ₋₁(1 + 0.0075) = (1.0075)·Pₖ₋₁ for all integers k ≥ 1

The amount after one year (four quarters) is:

```
P₀ = $10,000
P₁ = 1.0075·P₀ = 1.0075·$10,000 = $10,075.00
P₂ = 1.0075·P₁ = 1.0075·$10,075 = $10,150.56
P₃ = 1.0075·P₂ = 1.0075·$10,150.56 = $10,226.69
P₄ = 1.0075·P₃ = 1.0075·$10,226.69 = $10,303.39
```

Hence after one year there is $10,303.39 in the account.

b. The percentage increase (APY) is:

```
($10,303.39 - $10,000)/$10,000 = 0.03034 = 3.034%
```

### Recursive Deﬁnitions of Sum and Product

Addition and multiplication are called binary operations because only two numbers can be added or multiplied at a time. Careful deﬁnitions of sums and products of more than two numbers use recursion.

**Deﬁnition: Recursive Summation and Product**

Given numbers a₁, a₂, . . . , aₙ, where n is a positive integer:

The summation from i = 1 to n of the aᵢ, denoted ∑ᵢ₌₁ⁿ aᵢ, is deﬁned as:

```
∑ᵢ₌₁¹ aᵢ = a₁
∑ᵢ₌₁ⁿ aᵢ = (∑ᵢ₌₁ⁿ⁻¹ aᵢ) + aₙ, if n > 1
```

The product from i = 1 to n of the aᵢ, denoted ∏ᵢ₌₁ⁿ aᵢ, is deﬁned as:

```
∏ᵢ₌₁¹ aᵢ = a₁
∏ᵢ₌₁ⁿ aᵢ = (∏ᵢ₌₁ⁿ⁻¹ aᵢ)·aₙ, if n > 1
```

**Page 329-332**

### Example 5.6.9 A Sum of Sums

Prove that for any positive integer n, if a₁, a₂, . . . , aₙ and b₁, b₂, . . . , bₙ are real numbers, then:

```
∑ᵢ₌₁ⁿ (aᵢ + bᵢ) = ∑ᵢ₌₁ⁿ aᵢ + ∑ᵢ₌₁ⁿ bᵢ
```

**Solution**

The proof is by mathematical induction. Let the property P(n) be the equation:

```
∑ᵢ₌₁ⁿ (aᵢ + bᵢ) = ∑ᵢ₌₁ⁿ aᵢ + ∑ᵢ₌₁ⁿ bᵢ
```

**Show that P(1) is true:** For n = 1, both sides equal a₁ + b₁.

**Show that for all integers k ≥ 1, if P(k) is true then P(k + 1) is also true:**

Suppose that for some k ≥ 1:

```
∑ᵢ₌₁ᵏ (aᵢ + bᵢ) = ∑ᵢ₌₁ᵏ aᵢ + ∑ᵢ₌₁ᵏ bᵢ
```

We must show that:

```
∑ᵢ₌₁ᵏ⁺¹ (aᵢ + bᵢ) = ∑ᵢ₌₁ᵏ⁺¹ aᵢ + ∑ᵢ₌₁ᵏ⁺¹ bᵢ
```

The left-hand side is:

```
∑ᵢ₌₁ᵏ⁺¹ (aᵢ + bᵢ) = [∑ᵢ₌₁ᵏ (aᵢ + bᵢ)] + (aₖ₊₁ + bₖ₊₁)
                  = [∑ᵢ₌₁ᵏ aᵢ + ∑ᵢ₌₁ᵏ bᵢ] + (aₖ₊₁ + bₖ₊₁)
                  = [∑ᵢ₌₁ᵏ aᵢ + aₖ₊₁] + [∑ᵢ₌₁ᵏ bᵢ + bₖ₊₁]
                  = ∑ᵢ₌₁ᵏ⁺¹ aᵢ + ∑ᵢ₌₁ᵏ⁺¹ bᵢ
```

which equals the right-hand side.

### Test Yourself

1. A recursive deﬁnition for a sequence consists of a _____ and _____.
2. A recurrence relation is an equation that deﬁnes each later term of a sequence by reference to _____ in the sequence.
3. Initial conditions for a recursive deﬁnition of a sequence consist of one or more of the _____ of the sequence.
4. To solve a problem recursively means to divide the problem into smaller subproblems of the same type as the initial problem, to suppose _____, and to ﬁgure out how to use the supposition to _____.
5. A crucial step for solving a problem recursively is to deﬁne a _____ in terms of which the recurrence relation and initial conditions can be speciﬁed.

**Answers:**
1. recurrence relation; initial conditions
2. earlier terms
3. values of the ﬁrst few terms
4. that the smaller subproblems have already been solved; solve the initial problem
5. sequence

---

## 5.7 Solving Recurrence Relations by Iteration

**Pages 332-345**

> The keener one's sense of logical deduction, the less often one makes hard and fast inferences. — Bertrand Russell, 1872–1970

Suppose you have a sequence that satisfies a certain recurrence relation and initial conditions. It is often helpful to know an explicit formula for the sequence, especially if you need to compute terms that are far out in the sequence or if you want to investigate properties of the sequence as a whole. In this section we discuss a method for finding explicit formulas for certain types of recursively defined sequences. The method is called iteration, and it consists of repeatedly applying the recurrence relation to earlier and earlier terms until a pattern can be discerned. When a pattern is found, mathematical induction is often used to prove that the pattern is correct.

The method of iteration is especially useful for solving recurrence relations that have the form
aₙ = caₙ₋₁ + f(n)
where c is a constant and f(n) is a function of n. The Fibonacci sequence satisfies a recurrence relation of this form with c = 1 and f(n) = aₙ₋₂, but since f(n) = aₙ₋₂ is not a function of n alone, the method of iteration cannot be applied directly to solve the Fibonacci recurrence relation.

### Example 5.7.1 Finding an Explicit Formula

Let a₀, a₁, a₂, . . . be the sequence defined recursively as follows: For all integers k ≥ 1,
(1) aₖ = aₖ₋₁ + 2    recurrence relation
(2) a₀ = 1            initial condition.

Use iteration to guess an explicit formula for the sequence.

**Solution**

Recall that to say
aₖ = aₖ₋₁ + 2 for all integers k ≥ 1

means
a⬜ = a⬜₋₁ + 2

no matter what positive integer is
placed into the box ⬜.

In particular,
a₁ = a₀ + 2,
a₂ = a₁ + 2,
a₃ = a₂ + 2,
and so forth. Now use the initial condition to begin a process of successive substitutions into these equations, not just of numbers (as was done in Section 5.6) but of numerical expressions.

The reason for using numerical expressions rather than numbers is that in these problems you are seeking a numerical pattern that underlies a general formula. The secret of success is to leave most of the arithmetic undone. However, you do need to eliminate parentheses as you go from one step to the next. Otherwise, you will soon end up with a bewilderingly large nest of parentheses. Also, it is nearly always helpful to use shorthand notations for regrouping additions, subtractions, and multiplications of numbers that repeat. Thus, for instance, you would write

5·2

instead of 2 + 2 + 2 + 2 + 2

and

2⁵

instead of 2 · 2 ·2 · 2· 2.

Notice that you don't lose any information about the number patterns when you use these shorthand notations.

Here's how the process works for the given sequence:
a₀ = 1

the initial condition

a₁ = a₀ + 2 = 1 + 2

by substitution

a₂ = a₁ + 2 = (1 + 2) + 2

= 1 + 2 + 2

eliminate parentheses

a₃ = a₂ + 2 = (1 + 2 + 2) + 2

= 1 + 2 + 2 + 2

eliminate parentheses again; write
3 · 2 instead of 2 + 2 + 2?

a₄ = a₃ + 2 = (1 + 2 + 2 + 2) + 2 = 1 + 2 + 2 + 2 + 2

Tip Do no
arithmetic except
• replace n · 1 and
1 · n by n
• reformat repeated
numbers
• get rid of
parentheses

eliminate parentheses again;
definitely write 4 · 2 instead of
2 + 2 + 2 + 2—the length of the
string of 2's is getting out of hand.

Since it appears helpful to use the shorthand k ·2 in place of 2 + 2 + · · · + 2 (k times),
we do so, starting again from a₀.
a₀ = 1

= 1 + 0·2

the initial condition

a₁ = a₀ + 2 = 1 + 2

= 1 + 1·2

by substitution

a₂ = a₁ + 2 = (1 + 2) + 2

= 1 + 2·2

a₃ = a₂ + 2 = (1 + 2 · 2) + 2 = 1 + 3 ·2

Guess:

a₄ = a₃ + 2 = (1 + 3 · 2) + 2 = 1 + 4 ·2

At this point it certainly seems likely that
the general pattern is 1 + n · 2; check
whether the next calculation supports this.

a₅ = a₄ + 2 = (1 + 4 · 2) + 2 = 1 + 5 ·2

It does! So go ahead and write an answer.
It's only a guess, after all.

.
.
.
aₙ = 1 + n · 2 = 1 + 2n

The answer obtained for this problem is just a guess. To be sure of the correctness of this guess, you will need to check it by mathematical induction. Later in this section, we will show how to do this.

A sequence like the one in Example 5.7.1, in which each term equals the previous term plus a fixed constant, is called an arithmetic sequence. In the exercises at the end of this section you are asked to show that the nth term of an arithmetic sequence always equals the initial value of the sequence plus n times the fixed constant.

### Definition

A sequence a₀, a₁, a₂, . . . is called an arithmetic sequence if, and only if, there is a constant d such that
aₖ = aₖ₋₁ + d

for all integers k ≥ 1.

It follows that,

aₙ = a₀ + dn

for all integers n ≥ 0.

### Example 5.7.2 An Arithmetic Sequence

Under the force of gravity, an object falling in a vacuum falls about 9.8 meters per second (m/sec) faster each second than it fell the second before. Thus, neglecting air resistance, a skydiver's speed upon leaving an airplane is approximately 9.8 m/sec one second after departure, 9.8 + 9.8 = 19.6 m/sec two seconds after departure, and so forth. If air resistance is neglected, how fast would the skydiver be falling 60 seconds after leaving the airplane?

**Solution**

Let sₙ be the skydiver's speed in m/sec n seconds after exiting the airplane if there were no air resistance. Thus s₀ is the initial speed, and since the diver would travel 9.8 m/sec faster each second than the second before,
sₖ = sₖ₋₁ + 9.8 m/sec

for all integers k ≥ 1.

It follows that s₀, s₁, s₂, . . . is an arithmetic sequence with a fixed constant of 9.8, and thus
sₙ = s₀ + (9.8)n

for each integer n ≥ 0.

Hence sixty seconds after exiting and neglecting air resistance, the skydiver would travel at a speed of
s₆₀ = 0 + (9.8)(60) = 588 m/sec.

Note that 588 m/sec is over half a kilometer per second or over a third of a mile per second, which is very fast for a human being to travel. Happily for the skydiver, taking air resistance into account cuts the speed considerably.

In an arithmetic sequence, each term equals the previous term plus a fixed constant. In a geometric sequence, each term equals the previous term times a fixed constant. Geometric sequences arise in a large variety of applications, such as compound interest certain models of population growth, radioactive decay, and the number of operations needed to execute certain computer algorithms.

### Example 5.7.3 The Explicit Formula for a Geometric Sequence

Let r be a fixed nonzero constant, and suppose a sequence a₀, a₁, a₂, . . . is defined recursively as follows:
aₖ = raₖ₋₁
a₀ = a.

for all integers k ≥ 1,

Use iteration to guess an explicit formula for this sequence.

**Solution**

a₀ = a

a₁ = ra₀ = ra

a₂ = ra₁ = r(ra) = r²a

a₃ = ra₂ = r(r²a) = r³a

.
.
.
Guess: aₙ = rⁿa

In the exercises at the end of this section, you are asked to prove that this formula is correct.

### Definition

A sequence a₀, a₁, a₂, . . . is called a geometric sequence if, and only if, there is a constant r such that
aₖ = raₖ₋₁

for all integers k ≥ 1.

It follows that,

aₙ = a₀rⁿ

for all integers n ≥ 0.

### Example 5.7.4 A Geometric Sequence

As shown in Example 5.6.7, if a bank pays interest at a rate of 4% per year compounded annually and Aₙ denotes the amount in the account at the end of year n, then Aₖ = (1.04)Aₖ₋₁, for all integers k ≥ 1, assuming no deposits or withdrawals during the year.

Suppose the initial amount deposited is $100,000, and assume that no additional deposits or withdrawals are made.

a. How much will the account be worth at the end of 21 years?
b. In how many years will the account be worth $1,000,000?

**Solution**

a. A₀, A₁, A₂, . . . is a geometric sequence with initial value 100,000 and constant multiplier 1.04. Hence,
Aₙ = $100,000·(1.04)ⁿ

for all integers n ≥ 0.

After 21 years, the amount in the account will be
A₂₁ = $100,000·(1.04)²¹ ∼= $227,876.81.

This is the same answer as that obtained in Example 5.6.7 but is computed much more easily (at least if a calculator with a powering key, such as ∧ or xʸ, is used).

b. Let t be the number of years needed for the account to grow to $1,000,000. Then
$1,000,000 = $100,000·(1.04)ᵗ.

Dividing both sides by 100,000 gives
10 = (1.04)ᵗ,

and taking natural logarithms of both sides results in

Note Properties of
logarithms are reviewed
in Section 7.2.

ln(10) = ln(1.04)ᵗ.

Then
ln(10) ∼= t ln(1.04)

because logᵦ(xᵃ) = a logᵦ(x)
(see exercise 35 of Section 7.2)

and so
t ∼= ln(10)/ln(1.04) ∼= 58.7

Hence the account will grow to $1,000,000 in approximately 58.7 years.

An important property of a geometric sequence with constant multiplier greater than 1 is that its terms increase very rapidly in size as the subscripts get larger and larger. For instance, the first ten terms of a geometric sequence with a constant multiplier of 10 are
1, 10, 10², 10³, 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹.

Thus, by its tenth term, the sequence already has the value 10⁹ = 1,000,000,000 = 1 billion. The following box indicates some quantities that are approximately equal to certain powers of 10.

10⁷ ∼= number of seconds in a year
10⁹ ∼= number of bytes of memory in a personal computer

10¹¹ ∼= number of neurons in a human brain
10¹⁷ ∼= age of the universe in seconds (according to one theory)

10³¹ ∼= number of seconds to process all possible positions of a checkers game if moves are processed at a rate of 1 per billionth of a second
10⁸¹ ∼= number of atoms in the universe

10¹¹¹ ∼= number of seconds to process all possible positions of a chess game if moves are processed at a rate of 1 per billionth of a second

### Using Formulas to Simplify Solutions Obtained by Iteration

Explicit formulas obtained by iteration can often be simplified by using formulas such as those developed in Section 5.2. For instance, according to the formula for the sum of a geometric sequence with initial term 1 (Theorem 5.2.3), for each real number r except r = 1,
1 + r + r² + · · · + rⁿ = (rⁿ⁺¹ − 1)/(r − 1)

for all integers n ≥ 0.

And according to the formula for the sum of the first n integers (Theorem 5.2.2),
1 + 2 + 3 + · · · + n = n(n + 1)/2

for all integers n ≥ 1.

### Example 5.7.5 An Explicit Formula for the Tower of Hanoi Sequence

Recall that the Tower of Hanoi sequence m₁, m₂, m₃, . . . of Example 5.6.5 satisfies the recurrence relation
mₖ = 2mₖ₋₁ + 1 for all integers k ≥ 2
and has the initial condition
m₁ = 1.

Use iteration to guess an explicit formula for this sequence, and make use of a formula from Section 5.2 to simplify the answer.

**Solution**

By iteration
m₁ = 1
m₂ = 2m₁ + 1 = 2 · 1 + 1

= 2¹ + 1,

m₃ = 2m₂ + 1 = 2(2¹ + 1) + 1

= 2² + 2 + 1,

m₄ = 2m₃ + 1 = 2(2² + 2 + 1) + 1

= 2³ + 2² + 2 + 1,

m₅ = 2m₄ + 1 = 2(2³ + 2² + 2 + 1) + 1 = 2⁴ + 2³ + 2² + 2 + 1.

These calculations show that each term up to m₅ is a sum of successive powers of 2, starting with 2⁰ = 1 and going up to 2ᵏ, where k is 1 less than the subscript of the term. The pattern would seem to continue to higher terms because each term is obtained from the preceding one by multiplying by 2 and adding 1; multiplying by 2 raises the exponent of each component of the sum by 1, and adding 1 adds back the 1 that was lost when the previous 1 was multiplied by 2. For instance, for n = 6,
m₆ = 2m₅ + 1 = 2(2⁴ + 2³ + 2² + 2 + 1) + 1 = 2⁵ + 2⁴ + 2³ + 2² + 2 + 1.

Thus it seems that, in general,
mₙ = 2ⁿ⁻¹ + 2ⁿ⁻² + · · · + 2² + 2 + 1.

By the formula for the sum of a geometric sequence (Theorem 5.2.3),
2ⁿ⁻¹ + 2ⁿ⁻² + · · · + 2² + 2 + 1 = (2ⁿ − 1)/(2 − 1) = 2ⁿ − 1.

Hence the explicit formula seems to be
mₙ = 2ⁿ − 1 for all integers n ≥ 1.

A common mistake people make when doing problems such as this is to misuse the laws of algebra. For instance, by the distributive law,
a · (b + c) = a · b + a · c

for all real numbers a, b, and c.

Thus, in particular, for a = 2, b = 2, and c = 1,
2 · (2 + 1) = 2 · 2 + 2 · 1 = 2² + 2.

It follows that
2 · (2 + 1) + 1 = (2² + 2) + 1 = 2² + 2 + 1.

Caution!
It is not true
that

2 · (2 + 1) + 1 = 2² + 1 + 1.
This is crossed out
because it is false.

### Example 5.7.6 Using the Formula for the Sum of the First n Positive Integers

Let Kₙ be the picture obtained by drawing n dots (which we call vertices) and joining each pair of vertices by a line segment (which we call an edge). (In Chapter 10 we discuss these objects in a more general context.) Then K₁, K₂, K₃, and K₄ are as follows:

K₁    K₂    K₃    K₄

Observe that K₅ may be obtained from K₄ by adding one vertex and drawing edges between this new vertex and all the vertices of K₄ (the old vertices). The reason this procedure gives the correct result is that each pair of old vertices is already joined by an edge, and adding the new edges joins each pair of vertices consisting of an old one and the new one.

New vertex

K₅

Thus

the number of edges of K₅ = 4 + the number of edges of K₄.

By the same reasoning, for all integers k ≥ 2, the number of edges of Kₖ is k − 1 more than the number of edges of Kₖ₋₁. That is, if for each integer n ≥ 1
sₙ = the number of edges of Kₙ,
then
sₖ = sₖ₋₁ + (k − 1) for all integers k ≥ 2.

Note that s₁, is the number of edges in K₁, which is 0, and use iteration to find an explicit formula for s₁, s₂, s₃, . . . .

**Solution**

Because
sₖ = sₖ₋₁ + (k − 1)

and

s₁ = 0

then, in particular,

s₂ = s₁ + 1 = 0 + 1

s₃ = s₂ + 2 = (0 + 1) + 2 = 0 + 1 + 2

s₄ = s₃ + 3 = (0 + 1 + 2) + 3 = 0 + 1 + 2 + 3

s₅ = s₄ + 4 = (0 + 1 + 2 + 3) + 4 = 0 + 1 + 2 + 3 + 4

.
.
.

Guess:

sₙ = 0 + 1 + 2 + · · · + (n − 1).

But by Theorem 5.2.2,
0 + 1 + 2 + 3 + · · · + (n − 1) = (n − 1)n/2.

Hence it appears that
sₙ = n(n − 1)/2.

### Checking the Correctness of a Formula by Mathematical Induction

As you can see from some of the previous examples, the process of solving a recurrence relation by iteration can involve complicated calculations. It is all too easy to make a mistake and come up with the wrong formula. That is why it is important to confirm your calculations by checking the correctness of your formula. The most common way to do this is to use mathematical induction.

### Example 5.7.7 Using Mathematical Induction to Verify the Correctness of a Solution to a Recurrence Relation

In Example 5.6.5 we obtained a formula for the Tower of Hanoi sequence. Use mathematical induction to show that this formula is correct.

**Solution**

What does it mean to show the correctness of a formula for a recursively defined sequence? Given a sequence of numbers that satisfies a certain recurrence relation and initial condition, your job is to show that each term of the sequence satisfies the proposed explicit formula. In this case, you need to prove the following statement:

If m₁, m₂, m₃, . . . is the sequence defined by
mₖ = 2mₖ₋₁ + 1 for all integers k ≥ 2, and
m₁ = 1,
then mₙ = 2ⁿ − 1 for all integers n ≥ 1.

**Proof of Correctness:**

Let m₁, m₂, m₃, . . . be the sequence defined by specifying that m₁ = 1 and mₖ = 2mₖ₊₁ + 1 for all integers k ≥ 2, and let the property P(n) be the equation
mₙ = 2ⁿ − 1

← P(n)

We will use mathematical induction to prove that for all integers n ≥ 1, P(n) is true.

**Show that P(1) is true:**
To establish P(1), we must show that
m₁ = 2¹ − 1.

← P(1)

But the left-hand side of P(1) is
m₁ = 1

by definition of m₁, m₂, m₃, . . .,

and the right-hand side of P(1) is
2¹ − 1 = 2 − 1 = 1.

Thus the two sides of P(1) equal the same quantity, and hence P(1) is true.

**Show that for all integers k ≥ 1, if P(k) is true then P (k + 1) is also true:**

[Suppose that P(k) is true for a particular but arbitrarily chosen integer k ≥ 1. That is:]
Suppose that k is any integer with k ≥ 1 such that
mₖ = 2ᵏ − 1.

← P(k)
inductive hypothesis

[We must show that P(k + 1) is true. That is:] We must show that
mₖ₊₁ = 2ᵏ⁺¹ − 1.

← P(k + 1)

But the left-hand side of P(k + 1) is
mₖ₊₁

= 2m_(ₖ₊₁)₋₁ + 1

by definition of m₁, m₂, m₃, . . .

= 2mₖ + 1
= 2(2ᵏ − 1) + 1

by substitution from the inductive hypothesis

= 2ᵏ⁺¹ − 2 + 1

by the distributive law and the fact that 2 · 2ᵏ = 2ᵏ⁺¹

= 2ᵏ⁺¹ − 1

by basic algebra

which equals the right-hand side of P(k + 1). [Since the basis and inductive steps have been proved, it follows by mathematical induction that the given formula holds for all integers n ≥ 1.]

### Discovering That an Explicit Formula Is Incorrect

The following example shows how the process of trying to verify a formula by mathematical induction may reveal a mistake.

### Example 5.7.8 Using Verification by Mathematical Induction to Find a Mistake

Let c₀, c₁, c₂, . . . be the sequence defined as follows:
cₖ = 2cₖ₋₁ + k
c₀ = 1.

for all integers k ≥ 1,

Suppose your calculations suggest that c₀, c₁, c₂, . . . satisfies the following explicit formula:
cₙ = 2ⁿ + n

for all integers n ≥ 0.

Is this formula correct?

**Solution**

Start to prove the statement by mathematical induction and see what develops.

The proposed formula passes the basis step of the inductive proof with no trouble, for on the one hand, c₀ = 1 by definition and on the other hand, 2⁰ + 0 = 1 + 0 = 1 also.

In the inductive step, you suppose
cₖ = 2ᵏ + k

for some integer k ≥ 0

This is the inductive hypothesis.

and then you must show that
cₖ₊₁ = 2ᵏ⁺¹ + (k + 1).

To do this, you start with cₖ₊₁, substitute from the recurrence relation, and then use the inductive hypothesis as follows:
cₖ₊₁ = 2cₖ + (k + 1)
= 2(2ᵏ + k) + (k + 1)
= 2ᵏ⁺¹ + 3k + 1

by the recurrence relation
by substitution from the inductive hypothesis
by basic algebra

To finish the verification, therefore, you need to show that
2ᵏ⁺¹ + 3k + 1 = 2ᵏ⁺¹ + (k + 1).

Now this equation is equivalent to
2k = 0

by subtracting 2ᵏ⁺¹ + k + 1 from both sides.

which is equivalent to
k = 0

by dividing both sides by 2.

But this is false since k may be any nonnegative integer.

Observe that when k = 0, then k + 1 = 1, and
c₁ = 2 · 1 + 1 = 3 and

2¹ + 1 = 3.

Thus the formula gives the correct value for c₁. However, when k = 1, then k + 1 = 2, and
c₂ = 2 ·3 + 2 = 8

whereas 2² + 2 = 4 + 2 = 6.

So the formula does not give the correct value for c₂. Hence the sequence c₀, c₁, c₂, . . . does not satisfy the proposed formula.

Once you have found a proposed formula to be false, you should look back at your calculations to see where you made a mistake, correct it, and try again.

### Test Yourself

1. To use iteration to find an explicit formula for a recursively defined sequence, start with the _____ and use successive substitution into the _____ to look for a numerical pattern.

2. At every step of the iteration process, it is important to eliminate _____.

3. If a single number, say a, is added to itself k times in one of the steps of the iteration, replace the sum by the expression _____.

4. If a single number, say a, is multiplied by itself k times in one of the steps of the iteration, replace the product by the expression _____.

5. A general arithmetic sequence a₀, a₁, a₂, . . . with initial value a₀ and fixed constant d satisfies the recurrence relation _____ and has the explicit formula _____.

6. A general geometric sequence a₀, a₁, a₂, . . . with initial value a₀ and fixed constant r satisfies the recurrence relation _____ and has the explicit formula _____.

7. When an explicit formula for a recursively defined sequence has been obtained by iteration, its correctness can be checked by _____.

### Exercise Set 5.7

1. The formula
n(n + 1)/2
1 + 2 + 3 + · · · + n =

is true for all integers n ≥ 1. Use this fact to solve each of the following problems:
a. If k is an integer and k ≥ 2, find a formula for the expression 1 + 2 + 3 + · · · + (k − 1).

b. If n is an integer and n ≥ 1, find a formula for the expression 3 + 2 + 4 + 6 + 8 + · · · + 2n.
c. If n is an integer and n ≥ 1, find a formula for the expression 3 + 3 · 2 + 3 · 3 + · · · + 3 · n + n.

2. The formula
1 + r + r² + · · · + rⁿ = (rⁿ⁺¹ − 1)/(r − 1)

is true for all real numbers r except r = 1 and for all integers n ≥ 0. Use this fact to solve each of the following problems:
a. If i is an integer and i ≥ 1, find a formula for the expression 1 + 2 + 2² + · · · + 2ⁱ⁻¹.
b. If n is an integer and n ≥ 1, find a formula for the expression 3ⁿ⁻¹ + 3ⁿ⁻² + · · · + 3² + 3 + 1.
c. If n is an integer and n ≥ 2, find a formula for the expression 2ⁿ + 2ⁿ⁻² · 3 + 2ⁿ⁻³ · 3 + · · · + 2² · 3 + 2 · 3 + 3
d. If n is an integer and n ≥ 1, find a formula for the expression
2ⁿ − 2ⁿ⁻¹ + 2ⁿ⁻² − 2ⁿ⁻³ + · · · + (−1)ⁿ⁻¹ · 2 + (−1)ⁿ.

In each of 3–15 a sequence is defined recursively. Use iteration to guess an explicit formula for the sequence. Use the formulas from Section 5.2 to simplify your answers whenever possible.

3. aₖ = kaₖ₋₁, for all integers k ≥ 1
a₀ = 1
4. bₖ = bₖ₋₁/(1 + bₖ₋₁), for all integers k ≥ 1
b₀ = 1
5. cₖ = 3cₖ₋₁ + 1, for all integers k ≥ 2
c₁ = 1
6. dₖ = 2dₖ₋₁ + 3, for all integers k ≥ 2
d₁ = 2
7. eₖ = 4eₖ₋₁ + 5, for all integers k ≥ 1
e₀ = 2
8. fₖ = fₖ₋₁ + 2ᵏ, for all integers k ≥ 2
f₁ = 1
9. gₖ = gₖ₋₁/(gₖ₋₁ + 2), for all integers k ≥ 2
g₁ = 1
10. hₖ = 2 − hₖ₋₁, for all integers k ≥ 1
h₀ = 1
11. pₖ = pₖ₋₁ + 2 · 3ᵏ
p₁ = 2
12. sₖ = sₖ₋₁ + 2ᵏ, for all integers k ≥ 1
s₀ = 3
13. tₖ = tₖ₋₁ + 3ᵏ + 1, for all integers k ≥ 1
t₀ = 0
14. xₖ = 3xₖ₋₁ + k, for all integers k ≥ 2
x₁ = 1
15. yₖ = yₖ₋₁ + k², for all integers k ≥ 2
y₁ = 1

16. Solve the recurrence relation obtained as the answer to exercise 18(c) of Section 5.6.

17. Solve the recurrence relation obtained as the answer to exercise 21(c) of Section 5.6.

18. Suppose d is a fixed constant and a₀, a₁, a₂, . . . is a sequence that satisfies the recurrence relation aₖ = aₖ₋₁ + d, for all integers k ≥ 1. Use mathematical induction to prove that aₙ = a₀ + nd, for all integers n ≥ 0.

19. A worker is promised a bonus if he can increase his productivity by 2 units a day every day for a period of 30 days. If on day 0 he produces 170 units, how many units must he produce on day 30 to qualify for the bonus?

20. A runner targets herself to improve her time on a certain course by 3 seconds a day. If on day 0 she runs the course in 3 minutes, how fast must she run it on day 14 to stay on target?

21. Suppose r is a fixed constant and a₀, a₁, a₂ . . . is a sequence that satisfies the recurrence relation aₖ = raₖ₋₁, for all integers k ≥ 1 and a₀ = a. Use mathematical induction to prove that aₙ = arⁿ, for all integers n ≥ 0.

22. As shown in Example 5.6.8, if a bank pays interest at a rate of i compounded m times a year, then the amount of money Pₖ at the end of k time periods (where one time period = 1/mth of a year) satisfies the recurrence relation
Pₖ = [1 + (i/m)]Pₖ₋₁ with initial condition P₀ = the initial amount deposited. Find an explicit formula for Pₙ.

23. Suppose the population of a country increases at a steady rate of 3% per year. If the population is 50 million at a certain time, what will it be 25 years later?

24. A chain letter works as follows: One person sends a copy of the letter to five friends, each of whom sends a copy to five friends, each of whom sends a copy to five friends, and so forth. How many people will have received copies of the letter after the twentieth repetition of this process, assuming no person receives more than one copy?

25. A certain computer algorithm executes twice as many operations when it is run with an input of size k as when it is run with an input of size k − 1 (where k is an integer that is greater than 1). When the algorithm is run with an input of size 1, it executes seven operations. How many operations does it execute when it is run with an input of size 25?

26. A person saving for retirement makes an initial deposit of $1,000 to a bank account earning interest at a rate of 3% per year compounded monthly, and each month she adds an additional $200 to the account.
a. For each nonnegative integer n, let Aₙ be the amount in the account at the end of n months. Find a recurrence relation relating Aₖ to Aₖ₋₁.
b. Use iteration to find an explicit formula for Aₙ.
c. Use mathematical induction to prove the correctness of the formula you obtained in part (b).
d. How much will the account be worth at the end of 20 years? At the end of 40 years?
e. In how many years will the account be worth $10,000?

27. A person borrows $3,000 on a bank credit card at a nominal rate of 18% per year, which is actually charged at a rate of 1.5% per month.
a. What is the annual percentage rate (APR) for the card? (See Example 5.6.8 for a definition of APR.)
b. Assume that the person does not place any additional charges on the card and pays the bank $150 each month to pay off the loan. Let Bₙ be the balance owed on the card after n months. Find an explicit formula for Bₙ.
c. How long will be required to pay off the debt?
d. What is the total amount of money the person will have paid for the loan?

In 28–42 use mathematical induction to verify the correctness of the formula you obtained in the referenced exercise.

28. Exercise 3
29. Exercise 4
30. Exercise 5
31. Exercise 6
32. Exercise 7
33. Exercise 8
34. Exercise 9
35. Exercise 10
36. Exercise 11
37. Exercise 12
38. Exercise 13
39. Exercise 14
40. Exercise 15
41. Exercise 16
42. Exercise 17

In each of 43–49 a sequence is defined recursively. (a) Use iteration to guess an explicit formula for the sequence. (b) Use strong mathematical induction to verify that the formula of part (a) is correct.

43. aₖ = 2aₖ₋₁/(2aₖ₋₁ − 1), for all integers k ≥ 1
a₀ = 2

44. bₖ = 2/bₖ₋₁, for all integers k ≥ 2
b₁ = 1

45. vₖ = v⌊ₖ/₂⌋ + v⌈ₖ/₂⌉ + 2, for all integers k ≥ 2,
v₁ = 1.

46. sₖ = 2sₖ₋₂, for all integers k ≥ 2,
s₀ = 1, s₁ = 2.

47. tₖ = k − tₖ₋₁, for all integers k ≥ 1,
t₀ = 0.

48. wₖ = wₖ₋₂ + k, for all integers k ≥ 3,
w₁ = 1, w₂ = 2.

49. uₖ = uₖ₋₂ · uₖ₋₁, for all integers k ≥ 2,
u₀ = u₁ = 2.

In 50 and 51 determine whether the given recursively defined sequence satisfies the explicit formula aₙ = (n − 1)², for all integers n ≥ 1.

50. aₖ = 2aₖ₋₁ + k − 1, for all integers k ≥ 2
a₁ = 0
51. aₖ = (aₖ₋₁ + 1)², for all integers k ≥ 2
a₁ = 0

52. A single line divides a plane into two regions. Two lines (by crossing) can divide a plane into four regions; three lines can divide it into seven regions (see the figure). Let Pₙ be the maximum number of regions into which n lines divide a plane, where n is a positive integer.

7
6

3
5
1
4
2

Line 3

Line 2

Line 1

a. Derive a recurrence relation for Pₖ in terms of Pₖ₋₁, for all integers k ≥ 2.
b. Use iteration to guess an explicit formula for Pₙ.

53. Compute
[1 1]
[0 1]ⁿ

for small values of n (up to about 5 or 6). Conjecture explicit formulas for the entries in this matrix, and prove your conjecture using mathematical induction.

54. In economics the behavior of an economy from one period to another is often modeled by recurrence relations. Let Yₖ be the income in period k and Cₖ be the consumption in period k. In one economic model, income in any period is assumed to be the sum of consumption in that period plus investment and government expenditures (which are assumed to be constant from period to period), and consumption in each period is assumed to be a linear function of the income of the preceding period. That is,
Yₖ = Cₖ + E

Cₖ = c + mYₖ₋₁

where E is the sum of investment
plus government expenditures
where c and m are constants.

Substituting the second equation into the first gives
Yₖ = E + c + mYₖ₋₁.

a. Use iteration on the above recurrence relation to obtain
Yₙ = (E + c)((mⁿ − 1)/(m − 1)) + mⁿY₀

for all integers n≥1.
b. (For students who have studied calculus) Show that if 0 < m < 1, then limₙ→∞ Yₙ = (E + c)/(1 − m).

### Answers for Test Yourself

1. initial conditions; recurrence relation
2. parentheses
3. k·a
4. aᵏ
5. aₖ = aₖ₋₁ + d; aₙ = a₀ + dn
6. aₖ = raₖ₋₁; aₙ = a₀rⁿ
7. mathematical induction

---