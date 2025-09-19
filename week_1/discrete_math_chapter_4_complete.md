# Chapter 4: Elementary Number Theory and Methods of Proof (Complete)

**Pages 180-250**

## 4.1 Direct Proof and Counterexample I: Introduction

**Page 180**

### Method of Direct Proof

1. Express the statement to be proved in the form "∀x ∈ D, if P(x) then Q(x)."
2. Start the proof by supposing x is a particular but arbitrarily chosen element of D for which the hypothesis P(x) is true.
3. Show that the conclusion Q(x) is true by using definitions, previously established results, and the rules for logical inference.

### Existential Instantiation

If the existence of a certain kind of object is assumed or has been deduced then it can be given a name, as long as that name is not currently being used to denote something else.

**Page 181-182**

### Example 4.1.7: A Direct Proof of a Theorem

**Prove that the sum of any two even integers is even.**

**Formal Restatement:** ∀ integers m and n, if m and n are even then m + n is even.

**Starting Point:** Suppose m and n are any even integers.

**To Show:** m + n is even.

Since m and n are even:
- m = 2r, for some integer r
- n = 2s, for some integer s

Then:
```
m + n = 2r + 2s        (by substitution)
      = 2(r + s)       (by factoring out 2)
```

Let t = r + s. Since t is an integer (sum of integers):
```
m + n = 2t    where t is an integer
```

Therefore, m + n is even by definition of even.

### Theorem 4.1.1

**The sum of any two even integers is even.**

---

## 4.2 Direct Proof and Counterexample II: Rational Numbers

**Page 191**

### Definition

A real number r is **rational** if, and only if:
```
r is rational ⇔ ∃ integers a and b such that r = a/b and b ≠ 0
```

A real number that is not rational is **irrational**.

### Zero Product Property

If neither of two real numbers is zero, then their product is also not zero.

**Page 193-194**

### Theorem 4.2.2: Sum of Rational Numbers

**The sum of any two rational numbers is rational.**

**Proof:**
Suppose r and s are rational numbers. Then:
- r = a/b for integers a, b with b ≠ 0
- s = c/d for integers c, d with d ≠ 0

Then:
```
r + s = a/b + c/d
      = ad/bd + bc/bd      (common denominator)
      = (ad + bc)/bd       (adding fractions)
```

Let p = ad + bc and q = bd. Then:
- p is an integer (sum and product of integers)
- q is an integer (product of integers)
- q ≠ 0 (by zero product property since b ≠ 0 and d ≠ 0)

Therefore:
```
r + s = p/q    where p, q are integers and q ≠ 0
```

Thus r + s is rational. ■

---

## 4.3 Direct Proof and Counterexample III: Divisibility

**Page 198**

### Definition of Divisibility

If n and d are integers and d ≠ 0:
```
d | n ⇔ ∃ integer k such that n = dk
```

We can also say:
- n is divisible by d
- n is a multiple of d
- d is a factor of n
- d is a divisor of n
- d divides n

### Non-divisibility

For all integers n and d with d ≠ 0:
```
d ∤ n ⇔ n/d is not an integer
```

**Page 199**

### Theorem 4.3.1: A Positive Divisor of a Positive Integer

**For all integers a and b, if a and b are positive and a | b, then a ≤ b.**

**Proof:**
Suppose a and b are positive integers and a | b.
Then ∃ integer k such that:
```
b = ak
```

Since a > 0 and b > 0, we have k > 0.
Since k is a positive integer:
```
k ≥ 1
```
Multiplying by a:
```
ak ≥ a
```
Therefore:
```
b = ak ≥ a
```
Thus a ≤ b. ■

### Theorem 4.3.2: Divisors of 1

**The only divisors of 1 are 1 and −1.**

**Proof:**
Since 1·1 = 1 and (−1)(−1) = 1, both 1 and −1 divide 1.

Suppose m | 1. Then ∃ integer n such that:
```
1 = mn
```

Either m, n > 0 or m, n < 0.

If m, n > 0: By Theorem 4.3.1, m ≤ 1. Since m is positive integer and m ≤ 1, we have m = 1.

If m, n < 0: Then (−m)(−n) = mn = 1 where −m > 0. By same reasoning, −m = 1, so m = −1.

Therefore, the only divisors of 1 are 1 and −1. ■

**Page 201-202**

### Theorem 4.3.3: Transitivity of Divisibility

**For all integers a, b, and c, if a | b and b | c, then a | c.**

**Proof:**
Suppose a | b and b | c. Then:
```
b = ar    for some integer r
c = bs    for some integer s
```

By substitution:
```
c = bs
  = (ar)s
  = a(rs)
```

Let k = rs. Since k is an integer:
```
c = ak    where k is an integer
```

Therefore a | c. ■

### Theorem 4.3.5: Unique Factorization of Integers (Fundamental Theorem of Arithmetic)

Given any integer n > 1, there exist:
- positive integer k
- distinct primes p₁, p₂, ..., pₖ
- positive integers e₁, e₂, ..., eₖ

such that:
```
n = p₁^e₁ · p₂^e₂ · p₃^e₃ · ... · pₖ^eₖ
```

This factorization is unique except for order.

---

## 4.4 Division into Cases and Quotient-Remainder Theorem

**Page 208**

### Theorem 4.4.1: The Quotient-Remainder Theorem

Given any integer n and positive integer d, there exist unique integers q and r such that:
```
n = dq + r    and    0 ≤ r < d
```

### Definition: div and mod

Given integer n and positive integer d:
```
n div d = q  and  n mod d = r  ⇔  n = dq + r  where 0 ≤ r < d
```

Also:
```
n mod d = n − d·(n div d)
```

**Page 211**

### Parity Property

Any integer n can be written as either:
```
n = 2q    (even)
or
n = 2q + 1    (odd)
```
for some integer q.

### Theorem 4.4.2: Consecutive Integers Have Opposite Parity

**Any two consecutive integers have opposite parity.**

**Proof:**
Let m and m+1 be consecutive integers.

**Case 1:** m is even
Then m = 2k for some integer k.
So m + 1 = 2k + 1, which is odd.

**Case 2:** m is odd
Then m = 2k + 1 for some integer k.
So m + 1 = (2k + 1) + 1 = 2k + 2 = 2(k + 1), which is even.

In both cases, one is even and the other is odd. ■

**Page 213**

### Representations Modulo d

For any integer n and positive integer d, n can be written as one of:
```
dq, dq + 1, dq + 2, ..., dq + (d−1)
```
for some integer q.

**Page 214-215**

### Theorem 4.4.3: Square of Odd Integer

**The square of any odd integer has the form 8m + 1 for some integer m.**

**Proof:**
Any odd integer n has the form 4q + 1 or 4q + 3.

**Case 1:** n = 4q + 1
```
n² = (4q + 1)²
   = 16q² + 8q + 1
   = 8(2q² + q) + 1
```
Let m = 2q² + q. Then n² = 8m + 1.

**Case 2:** n = 4q + 3
```
n² = (4q + 3)²
   = 16q² + 24q + 9
   = 16q² + 24q + 8 + 1
   = 8(2q² + 3q + 1) + 1
```
Let m = 2q² + 3q + 1. Then n² = 8m + 1. ■

### Definition: Absolute Value

For any real number x:
```
|x| = { x    if x ≥ 0
      { −x   if x < 0
```

### Theorem 4.4.6: The Triangle Inequality

**For all real numbers x and y:**
```
|x + y| ≤ |x| + |y|
```

---

## 4.5 Floor and Ceiling

**Page 219**

### Definitions

**Floor of x:** ⌊x⌋ = unique integer n such that:
```
n ≤ x < n + 1
```

**Ceiling of x:** ⌈x⌉ = unique integer n such that:
```
n − 1 < x ≤ n
```

### Examples

```
⌊25/4⌋ = ⌊6.25⌋ = 6
⌈25/4⌉ = ⌈6.25⌉ = 7

⌊0.999⌋ = 0
⌈0.999⌉ = 1

⌊−2.01⌋ = −3
⌈−2.01⌉ = −2
```

**Page 221-222**

### Theorem 4.5.1

**For all real numbers x and all integers m:**
```
⌊x + m⌋ = ⌊x⌋ + m
```

**Proof:**
Let n = ⌊x⌋. Then:
```
n ≤ x < n + 1
```

Adding m to all parts:
```
n + m ≤ x + m < n + m + 1
```

Since n + m is an integer:
```
⌊x + m⌋ = n + m = ⌊x⌋ + m
```
■

### Theorem 4.5.2: Floor of n/2

**For any integer n:**
```
⌊n/2⌋ = { n/2        if n is even
        { (n−1)/2    if n is odd
```

**Proof:**
**Case 1:** n = 2k + 1 (odd)
```
⌊n/2⌋ = ⌊(2k + 1)/2⌋
      = ⌊k + 1/2⌋
      = k
      = (n−1)/2
```

**Case 2:** n = 2k (even)
```
⌊n/2⌋ = ⌊2k/2⌋
      = ⌊k⌋
      = k
      = n/2
```
■

**Page 223-224**

### Theorem 4.5.3: Quotient and Remainder Using Floor

If n is any integer and d is a positive integer, and if:
```
q = ⌊n/d⌋    and    r = n − d⌊n/d⌋
```

Then:
```
n = dq + r    and    0 ≤ r < d
```

**Proof:**
By substitution:
```
dq + r = d⌊n/d⌋ + (n − d⌊n/d⌋) = n
```

Since q = ⌊n/d⌋, by definition of floor:
```
q ≤ n/d < q + 1
```

Multiplying by d:
```
dq ≤ n < dq + d
```

Subtracting dq:
```
0 ≤ n − dq < d
```

But r = n − dq, so:
```
0 ≤ r < d
```
■

### Formulas for div and mod using Floor

For nonnegative integer n and positive integer d:
```
n div d = ⌊n/d⌋
n mod d = n − d⌊n/d⌋
```

---

## 4.6 Indirect Argument: Contradiction and Contraposition

**Page 226**

### Method of Proof by Contradiction

1. Suppose the statement to be proved is false (suppose its negation is true)
2. Show this supposition leads to a contradiction
3. Conclude the statement is true

### Theorem 4.6.1: No Greatest Integer

**There is no greatest integer.**

**Proof by Contradiction:**
Suppose there is a greatest integer N.
Then N ≥ n for all integers n.

Let M = N + 1.
- M is an integer (sum of integers)
- M > N (since M = N + 1)

So M is an integer greater than N.
This contradicts that N is the greatest integer.
Therefore, there is no greatest integer. ■

**Page 227**

### Theorem 4.6.2: No Integer Both Even and Odd

**There is no integer that is both even and odd.**

**Proof by Contradiction:**
Suppose integer n is both even and odd.
Then:
```
n = 2a    for some integer a    (n is even)
n = 2b + 1    for some integer b    (n is odd)
```

Therefore:
```
2a = 2b + 1
2a − 2b = 1
2(a − b) = 1
a − b = 1/2
```

But a − b must be an integer (difference of integers).
And 1/2 is not an integer.
Contradiction! Therefore, no integer is both even and odd. ■

**Page 228-229**

### Theorem 4.6.3: Sum of Rational and Irrational

**The sum of any rational number and any irrational number is irrational.**

**Proof by Contradiction:**
Suppose r is rational, s is irrational, but r + s is rational.

Then:
```
r = a/b    for integers a, b with b ≠ 0
r + s = c/d    for integers c, d with d ≠ 0
```

Solving for s:
```
s = (r + s) − r
  = c/d − a/b
  = (bc − ad)/(bd)
```

Since bc − ad and bd are integers and bd ≠ 0, s is rational.
This contradicts that s is irrational.
Therefore, r + s must be irrational. ■

### Method of Proof by Contraposition

To prove "If P(x) then Q(x)":
1. Form contrapositive: "If not Q(x) then not P(x)"
2. Prove the contrapositive directly

### Proposition 4.6.4

**For all integers n, if n² is even then n is even.**

**Proof by Contraposition:**
We prove: If n is odd, then n² is odd.

Suppose n is odd. Then n = 2k + 1 for some integer k.
```
n² = (2k + 1)²
   = 4k² + 4k + 1
   = 2(2k² + 2k) + 1
```

Since 2k² + 2k is an integer, n² = 2·(integer) + 1, so n² is odd.
Therefore, by contraposition, if n² is even then n is even. ■

---

[The chapter continues with sections 4.7 and 4.8, but this shows the complete mathematical detail for the main sections]