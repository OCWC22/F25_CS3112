# Discrete Mathematics Chapter 4 - Complete Notes

## Chapter 4.1: Direct Proof and Counterexample I: Introduction

### Theorem 4.1.1
Every integer is a rational number.

### Definitions
- **Even Integer**: An integer n is even if, and only if, n equals twice some integer. In other words, n is even ⇔ ∃ an integer k such that n = 2k.
- **Odd Integer**: An integer n is odd if, and only if, n equals twice some integer plus 1. In other words, n is odd ⇔ ∃ an integer k such that n = 2k + 1.
- **Prime Number**: A prime number is a positive integer greater than 1 that cannot be written as a product of two smaller positive integers. Formally, if n is a positive integer with n > 1, then n is prime ⇔ for all positive integers r and s, if n = r·s, then r = 1 or s = 1.
- **Composite Number**: A positive integer greater than 1 that is not prime is composite. Formally, if n is a positive integer with n > 1, then n is composite ⇔ ∃ positive integers r and s such that n = r·s and r ≠ 1 and s ≠ 1.

### Proof Methods
1. **Direct Proof**: Start with hypothesis, derive conclusion through logical steps.
2. **Counterexample**: To disprove a universal statement, find one example where it's false.
3. **Method of Exhaustion**: Check all cases when domain is small and finite.

### Method of Generalizing from the Generic Particular
To prove a universal statement ∀x ∈ D, P(x):
1. Suppose x is a particular but arbitrarily chosen element of D.
2. Show that x satisfies the property P(x).

### Examples

**Example 4.1.1**: Prove that the sum of any two even integers is even.
- Let m and n be even integers. Then m = 2k and n = 2l for some integers k and l.
- m + n = 2k + 2l = 2(k + l), which is even.

**Example 4.1.2**: Prove that the sum of any two odd integers is even.
- Let m and n be odd integers. Then m = 2k + 1 and n = 2l + 1 for some integers k and l.
- m + n = (2k + 1) + (2l + 1) = 2(k + l + 1), which is even.

**Example 4.1.3**: Prove that for all integers m and n, if m and n are both odd or both even, then m - n is even.
- Case 1: Both even - m = 2k, n = 2l, so m - n = 2(k - l) which is even.
- Case 2: Both odd - m = 2k + 1, n = 2l + 1, so m - n = 2(k - l) which is even.

**Example 4.1.4**: Prove that the product of any even integer with any odd integer is even.
- Let m be even, n be odd. Then m = 2k, n = 2l + 1.
- m·n = (2k)(2l + 1) = 2(k(2l + 1)), which is even.

**Example 4.1.5**: For all integers n, if n² is even, then n is even.
- Contrapositive approach: If n is odd, then n² is odd.
- If n is odd, n = 2k + 1, so n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd.

**Example 4.1.6**: There is a prime number between 50 and 60.
- Check each number: 51 (3×17), 52 (2×26), 53 (prime), 54 (2×27), 55 (5×11), 56 (2×28), 57 (3×19), 58 (2×29), 59 (prime).
- Both 53 and 59 are prime.

**Example 4.1.7**: For all integers n, 4n² + 4n + 1 is odd.
- Proof: 4n² + 4n + 1 = (2n + 1)². Since 2n + 1 is odd, its square is odd.
- Alternative: 4n² + 4n + 1 = 4(n² + n) + 1 = 2[2(n² + n)] + 1, which is odd.

**Example 4.1.8**: There exist integers m and n such that 15m + 12n = 3.
- Choose m = 1, n = -1: 15(1) + 12(-1) = 15 - 12 = 3.

**Example 4.1.9**: There exist integers m and n such that 15m + 12n = 2.
- Suppose 15m + 12n = 2 for some integers m, n.
- Then 15m + 12n = 3(5m + 4n) = 2, so 5m + 4n = 2/3, not an integer. Contradiction.
- Therefore, no such integers exist.

### Common Mistakes in Proof Writing
1. **Arguing from examples**: One example doesn't prove a universal statement.
2. **Using the same variable**: Avoid reusing variables for different purposes.
3. **Jumping to conclusions**: Each step must follow logically from the previous ones.
4. **Begging the question**: Assuming what you're trying to prove.
5. **Misuse of the word if**: Be careful about necessary vs. sufficient conditions.

### Test Yourself Questions
1. An even integer is an integer that equals twice some integer.
2. An odd integer is an integer that equals twice some integer plus 1.
3. A prime number is an integer greater than 1 that is not a product of two smaller positive integers.
4. To prove a universal statement is false, you give a counterexample.
5. To prove an existential statement is true, you exhibit a particular but arbitrarily chosen element of the set that satisfies the given property.
6. To prove a universal conditional statement is true, you show that for a particular but arbitrarily chosen element of the domain that makes the hypothesis true, the conclusion is also true.

### Exercise Set 4.1

**Questions 1-15: Understanding Definitions**
1. Is 12 divisible by 2?
2. Is 0 divisible by 2?
3. Is 306 divisible by 2?
4. Is 9 divisible by 2?
5. Is 2·3 + 1 divisible by 2?
6. Is 2·0 + 1 divisible by 2?
7. Is 2(-1) + 1 divisible by 2?
8. Is 2·1 + 1 divisible by 2?
9. Is 2·1 + 1 divisible by 2?
10. Is 5 a prime number?
11. Is 4 a prime number?
12. Is 1 a prime number?
13. Is 7 a prime number?
14. Is 6 a prime number?
15. Is 13 a prime number?

**Questions 16-30: Finding Counterexamples**
16. For all integers n, if n > 2 then there is a prime number strictly between n and 2n.
17. For all integers n, if n > 1 then there is a prime number strictly between n and n².
18. For all integers n, if n > 1 then n² - n + 41 is prime.
19. For all integers n, if n > 0 then 2n² + 5n + 2 is prime.
20. For all integers n, if n > 0 then 2n² + 7n + 3 is prime.
21. For all integers n, if n > 0 then 2n² + 11n + 15 is prime.
22. For all integers n, if n > 0 then 2n² + 13n + 21 is prime.
23. For all integers n, if n > 0 then 2n² + 17n + 35 is prime.
24. For all integers n, if n > 0 then 2n² + 19n + 45 is prime.
25. For all integers n, if n > 0 then 2n² + 23n + 55 is prime.
26. For all integers n, if n > 0 then 2n² + 29n + 70 is prime.
27. For all integers n, if n > 0 then 2n² + 31n + 77 is prime.
28. For all integers n, if n > 0 then 2n² + 37n + 91 is prime.
29. For all integers n, if n > 0 then 2n² + 41n + 105 is prime.
30. For all integers n, if n > 0 then 2n² + 43n + 119 is prime.

**Questions 31-63: Proving Statements**
31. Prove that if n is any even integer, then (-1)ⁿ = 1.
32. Prove that if n is any odd integer, then (-1)ⁿ = -1.
33. Suppose a is any integer. Prove that 2a + 7 is odd.
34. Suppose k is any odd integer. Prove that k² + 2k + 1 is even.
35. Suppose m and n are any positive integers. Prove that m - n is even if, and only if, m and n are both even or both odd.
36. Prove that for all integers a, b, and c, if a + b is even and b + c is even, then a + c is even.
37. Prove that for all integers n, if n is even, then n² - 1 is odd.
38. Prove that for all integers n, if n is odd, then n² - 1 is even.
39. Prove that for all integers a, b, and c, if a - b is odd and b - c is odd, then a - c is even.
40. Prove that for all integers m and n, if m - n is even, then m² - n² is even.
41. Prove that for all integers m and n, if m and n have the same parity, then m - n is even.
42. Prove that for all integers m and n, if m - n is even, then m and n have the same parity.
43. Prove that for all integers m and n, if m² + n² is even, then m and n have the same parity.
44. Prove that for all integers a, b, c, and d, if a and b have the same parity and c and d have the same parity, then a + c and b + d have the same parity.
45. Prove that for all integers n, n² + n is even.
46. Prove that for all integers n, if n is odd, then n³ is odd.
47. Prove that for all integers n, if n² is odd, then n is odd.
48. Prove that for all integers m and n, if mn is even, then m is even or n is even.
49. Prove that for all integers n, 7n² - 3n is even.
50. Prove that for all integers n, 2n³ + 6n + 3 is odd.
51. Prove that for all integers a and b, if a is even or b is even, then a + b is even if, and only if, a and b have the same parity.
52. Prove that for all integers n, if n is even, then 3n² - 5n + 7 is odd.
53. Prove that for all integers a, b, and c, if a + b + c is even, then a, b, c are all even or exactly one is even.
54. Prove that for all integers m and n, if m² - n² is even, then m and n have the same parity.
55. Every positive integer can be expressed as a sum of three or fewer perfect squares.
56. (Two integers are consecutive if, and only if, one is one more than the other.) Any product of four consecutive integers is one less than a perfect square.
57. If m and n are positive integers and mn is a perfect square, then m and n are perfect squares.
58. The difference of the squares of any two consecutive integers is odd.
59. For all nonnegative real numbers a and b, √(ab) = √a · √b.
60. For all nonnegative real numbers a and b, √(a + b) = √a + √b.
61. Suppose that integers m and n are perfect squares. Then √m + √n + 2√(mn) is also a perfect square. Why?
62. If p is a prime number, must 2^p - 1 also be prime? Prove or give a counterexample.
63. If n is a nonnegative integer, must 2^(2n) + 1 be prime? Prove or give a counterexample.

## Chapter 4.2: Direct Proof and Counterexample II: Rational Numbers

### Definition
A real number r is rational if, and only if, it can be expressed as a quotient of two integers with a nonzero denominator. A real number that is not rational is irrational.

More formally, if r is a real number, then:
r is rational ⇔ ∃ integers a and b such that r = a/b and b ≠ 0.

### Example 4.2.1: Determining Whether Numbers Are Rational or Irrational
a. Is 10/3 a rational number?
b. Is -5/39 a rational number?
c. Is 0.281 a rational number?
d. Is 7 a rational number?
e. Is 0 a rational number?
f. Is 2/0 a rational number?
g. Is 2/0 an irrational number?
h. Is 0.12121212... a rational number (where the digits 12 are assumed to repeat forever)?
i. If m and n are integers and neither m nor n is zero, is (m + n)/mn a rational number?

### Zero Product Property
If neither of two real numbers is zero, then their product is also not zero.

### Theorem 4.2.1
Every integer is a rational number.

### Theorem 4.2.2
The sum of any two rational numbers is rational.

**Proof:**
Suppose r and s are rational numbers. [We must show that r + s is rational.] Then, by definition of rational, r = a/b and s = c/d for some integers a, b, c, and d with b ≠ 0 and d ≠ 0. Thus:

r + s = a/b + c/d = (ad + bc)/bd

Let p = ad + bc and q = bd. Then p and q are integers because products and sums of integers are integers and because a, b, c, and d are all integers. Also q ≠ 0 by the zero product property. Thus:

r + s = p/q where p and q are integers and q ≠ 0.

Therefore, r + s is rational by definition of a rational number.

### Example 4.2.2: A Sum of Rationals Is Rational
Prove that the sum of any two rational numbers is rational.

**Formal Restatement:** ∀ real numbers r and s, if r and s are rational then r + s is rational.

**Starting Point:** Suppose r and s are rational numbers.

**To Show:** r + s is rational.

**Proof:**
Since r and s are rational, r = a/b and s = c/d for some integers a, b, c, and d with b ≠ 0 and d ≠ 0. Thus:

r + s = a/b + c/d = (ad + bc)/bd

Let p = ad + bc and q = bd. Then p and q are integers because products and sums of integers are integers. Also q ≠ 0 by the zero product property. Thus r + s is a rational number.

### Example 4.2.3: Deriving Additional Results about Even and Odd Integers
Suppose that you have already proved the following properties of even and odd integers:
1. The sum, product, and difference of any two even integers are even.
2. The sum and difference of any two odd integers are even.
3. The product of any two odd integers is odd.
4. The product of any even integer and any odd integer is even.
5. The sum of any odd integer and any even integer is odd.
6. The difference of any odd integer minus any even integer is odd.
7. The difference of any even integer minus any odd integer is odd.

Use the properties listed above to prove that if a is any even integer and b is any odd integer, then (a² + b² + 1)/2 is an integer.

**Solution:**
Suppose a is any even integer and b is any odd integer. By property 3, b² is odd, and by property 1, a² is even. Then by property 5, a² + b² is odd, and because 1 is also odd, the sum (a² + b²) + 1 = a² + b² + 1 is even by property 2. Hence, by definition of even, there exists an integer k such that a² + b² + 1 = 2k. Dividing both sides by 2 gives (a² + b² + 1)/2 = k, which is an integer. Thus (a² + b² + 1)/2 is an integer.

### Corollary 4.2.3
The double of a rational number is rational.

**Proof:**
Suppose r is any rational number. Then 2r = r + r is a sum of two rational numbers. So, by Theorem 4.2.2, 2r is rational.

### More on Generalizing from the Generic Particular
Some people like to think of the method of generalizing from the generic particular as a challenge process. If you claim a property holds for all elements in a domain, then someone can challenge your claim by picking any element in the domain whatsoever and asking you to prove that that element satisfies the property. To prove your claim, you must be able to meet all such challenges. That is, you must have a way to convince the challenger that the property is true for an arbitrarily chosen element in the domain.

For example, suppose "A" claims that every integer is a rational number. "B" challenges this claim by asking "A" to prove it for n = 7. "A" observes that:

7 = 7/1

which is a quotient of integers and hence rational.

"B" accepts this explanation but challenges again with n = -12. "A" responds that:

-12 = -12/1

which is a quotient of integers and hence rational.

Next "B" tries to trip up "A" by challenging with n = 0, but "A" answers that:

0 = 0/1

which is a quotient of integers and hence rational.

As you can see, "A" is able to respond effectively to all "B"s challenges because "A" has a general procedure for putting integers into the form of rational numbers: "A" just divides whatever integer "B" gives by 1. That is, no matter what integer n "B" gives "A", "A" writes:

n = n/1

which is a quotient of integers and hence rational.

This discussion proves Theorem 4.2.1: Every integer is a rational number.

### Properties of Even and Odd Integers (for Reference)
1. The sum, product, and difference of any two even integers are even.
2. The sum and difference of any two odd integers are even.
3. The product of any two odd integers is odd.
4. The product of any even integer and any odd integer is even.
5. The sum of any odd integer and any even integer is odd.
6. The difference of any odd integer minus any even integer is odd.
7. The difference of any even integer minus any odd integer is odd.

### Test Yourself Questions
1. To show that a real number is rational, we must show that we can write it as _____.
2. An irrational number is a _____ that is _____.
3. Zero is a rational number because _____.

### Exercise Set 4.2

**Questions 1-10: Rational Number Identification**
1. Write -35/6 as a ratio of two integers.
2. Write 4.6037 as a ratio of two integers.
3. Write 4/5 + 2/9 as a ratio of two integers.
4. Write 0.37373737... as a ratio of two integers.
5. Write 0.56565656... as a ratio of two integers.
6. Write 320.5492492492... as a ratio of two integers.
7. Write 52.4672167216721... as a ratio of two integers.
8. The zero product property, says that if a product of two real numbers is 0, then one of the numbers must be 0.
   a. Write this property formally using quantifiers and variables.
   b. Write the contrapositive of your answer to part (a).
   c. Write an informal version (without quantifier symbols or variables) for your answer to part (b).
9. Assume that a and b are both integers and that a ≠ 0 and b ≠ 0. Explain why (b - a)/(ab²) must be a rational number.
10. Assume that m and n are both integers and that n ≠ 0. Explain why (5m + 12n)/(4n) must be a rational number.

**Questions 11-14: Formal Proofs**
11. Prove that every integer is a rational number.
12. Fill in the blanks in the following proof that the square of any rational number is rational:
    Proof: Suppose that r is (a) _____. By definition of rational, r = a/b for some (b) _____ with b ≠ 0. By substitution, r² = (c) _____ = a²/b². Since a and b are both integers, so are the products a² and (d) _____. Also b² ≠ 0 by the (e) _____. Hence r² is a ratio of two integers with a nonzero denominator, and so (f) _____ by definition of rational.
13. Consider the statement: The negative of any rational number is rational.
    a. Write the statement formally using a quantifier and a variable.
    b. Determine whether the statement is true or false and justify your answer.
14. Consider the statement: The square of any rational number is a rational number.
    a. Write the statement formally using a quantifier and a variable.
    b. Determine whether the statement is true or false and justify your answer.

**Questions 15-34: True/False with Proofs**
15. The product of any two rational numbers is a rational number.
16. The quotient of any two rational numbers is a rational number.
17. The difference of any two rational numbers is a rational number.
18. If r and s are any two rational numbers, then (r + s)/2 is rational.
19. For all real numbers a and b, if a < b then a < (a + b)/2 < b. (You may use the properties of inequalities in T17–T27 of Appendix A.)
20. Given any two rational numbers r and s with r < s, there is another rational number between r and s. (Hint: Use the results of exercises 18 and 19.)
21. True or false? If m is any even integer and n is any odd integer, then m² + 3n is odd. Explain.
22. True or false? If a is any odd integer, then a² + a is even. Explain.
23. True or false? If k is any even integer and m is any odd integer, then (k + 2)² - (m - 1)² is even. Explain.
24. For any rational numbers r and s, 2r + 3s is rational.
25. If r is any rational number, then 3r² - 2r + 4 is rational.
26. For any rational number s, 5s³ + 8s² - 7 is rational.
27. It is a fact that if n is any nonnegative integer, then 1 + 1/2 + 1/2² + 1/2³ + ··· + 1/2ⁿ = (1 - (1/2ⁿ⁺¹))/(1 - (1/2)). (A more general form of this statement is proved in Section 5.2). Is the right-hand side of this equation rational? If so, express it as a ratio of two integers.
28. Suppose a, b, c, and d are integers and a ≠ c. Suppose also that x is a real number that satisfies the equation (ax + b)/(cx + d) = 1. Must x be rational? If so, express x as a ratio of two integers.
29. Suppose a, b, and c are integers and x, y, and z are nonzero real numbers that satisfy the following equations: xy/(x + y) = a, yz/(y + z) = b, and xz/(x + z) = c. Is x rational? If so, express it as a ratio of two integers.
30. Prove that if one solution for a quadratic equation of the form x² + bx + c = 0 is rational (where b and c are rational), then the other solution is also rational. (Use the fact that if the solutions of the equation are r and s, then x² + bx + c = (x - r)(x - s).)
31. Prove that if a real number c satisfies a polynomial equation of the form r₃x³ + r₂x² + r₁x + r₀ = 0, where r₀, r₁, r₂, and r₃ are rational numbers, then c satisfies an equation of the form n₃x³ + n₂x² + n₁x + n₀ = 0, where n₀, n₁, n₂, and n₃ are integers.
    Definition: A number c is called a root of a polynomial p(x) if, and only if, p(c) = 0.
32. Prove that for all real numbers c, if c is a root of a polynomial with rational coefficients, then c is a root of a polynomial with integer coefficients.
33. When expressions of the form (x - r)(x - s) are multiplied out, a quadratic polynomial is obtained. For instance, (x - 2)(x - (-7)) = (x - 2)(x + 7) = x² + 5x - 14.
    a. What can be said about the coefficients of the polynomial obtained by multiplying out (x - r)(x - s) when both r and s are odd integers? when both r and s are even integers? when one of r and s is even and the other is odd?
    b. It follows from part (a) that x² - 1253x + 255 cannot be written as a product of two polynomials with integer coefficients. Explain why this is so.
34. Observe that (x - r)(x - s)(x - t) = x³ - (r + s + t)x² + (rs + rt + st)x - rst.
    a. Derive a result for cubic polynomials similar to the result in part (a) of exercise 33 for quadratic polynomials.
    b. Can x³ + 7x² - 8x - 27 be written as a product of three polynomials with integer coefficients? Explain.

**Questions 35-39: Finding Proof Errors**
35. "Proof: Any two rational numbers produce a rational number when added together. So if r and s are particular but arbitrarily chosen rational numbers, then r + s is rational."
36. "Proof: Let rational numbers r = 1/4 and s = 1/2 be given. Then r + s = 1/4 + 1/2 = 3/4, which is a rational number. This is what was to be shown."
37. "Proof: Suppose r and s are rational numbers. By definition of rational, r = a/b for some integers a and b with b ≠ 0, and s = a/b for some integers a and b with b ≠ 0. Then r + s = a/b + a/b = 2a/b. Let p = 2a. Then p is an integer since it is a product of integers. Hence r + s = p/b, where p and b are integers and b ≠ 0. Thus r + s is a rational number by definition of rational. This is what was to be shown."
38. "Proof: Suppose r and s are rational numbers. Then r = a/b and s = c/d for some integers a, b, c, and d with b ≠ 0 and d ≠ 0 (by definition of rational). Then r + s = a/b + c/d. But this is a sum of two fractions, which is a fraction. So r + s is a rational number since a rational number is a fraction."
39. "Proof: Suppose r and s are rational numbers. If r + s is rational, then by definition of rational r + s = a/b for some integers a and b with b ≠ 0. Also since r and s are rational, r = i/j and s = m/n for some integers i, j, m, and n with j ≠ 0 and n ≠ 0. It follows that r + s = i/j + m/n = (in + jm)/(jn) = a/b, which is a quotient of two integers with a nonzero denominator. Hence it is a rational number. This is what was to be shown."

## Chapter 4.3: Direct Proof and Counterexample III: Divisibility

### Introduction
The essential quality of a proof is to compel belief. — Pierre de Fermat

When you were first introduced to the concept of division in elementary school, you were probably taught that 12 divided by 3 is 4 because if you separate 12 objects into groups of 3, you get 4 groups with nothing left over.

You may also have been taught to describe this fact by saying that "12 is evenly divisible by 3" or "3 divides 12 evenly."

The notion of divisibility is the central concept of one of the most beautiful subjects in advanced mathematics: number theory, the study of properties of integers.

### Definition
If n and d are integers and d ≠ 0 then:
n is divisible by d if, and only if, n equals d times some integer.

Instead of "n is divisible by d," we can say that:
- n is a multiple of d, or
- d is a factor of n, or
- d is a divisor of n, or
- d divides n.

The notation d | n is read "d divides n." Symbolically, if n and d are integers and d ≠ 0:
d | n ⇔ ∃ an integer k such that n = dk.

### Example 4.3.1: Divisibility
a. Is 21 divisible by 3?
b. Does 5 divide 40?
c. Does 7 | 42?
d. Is 32 a multiple of −16?
e. Is 6 a factor of 54?
f. Is 7 a factor of −7?

**Solution:**
a. Yes, 21 = 3 · 7.
b. Yes, 40 = 5 · 8.
c. Yes, 42 = 7 · 6.
d. Yes, 32 = (−16)· (−2).
e. Yes, 54 = 6· 9.
f. Yes, −7 = 7 · (−1).

### Example 4.3.2: Divisors of Zero
If k is any nonzero integer, does k divide 0?

**Solution:**
Yes, because 0 = k · 0.

### Two Useful Properties of Divisibility
Two useful properties of divisibility are (1) that if one positive integer divides a second positive integer, then the first is less than or equal to the second, and (2) that the only divisors of 1 are 1 and −1.

### Theorem 4.3.1: A Positive Divisor of a Positive Integer
For all integers a and b, if a and b are positive and a divides b, then a ≤ b.

**Proof:**
Suppose a and b are positive integers and a divides b. [We must show that a ≤ b.] Then there exists an integer k so that b = ak. By property T25 of Appendix A, k must be positive because both a and b are positive. It follows that:
1 ≤ k
because every positive integer is greater than or equal to 1. Multiplying both sides by a gives:
a ≤ ka = b
because multiplying both sides of an inequality by a positive number preserves the inequality by property T20 of Appendix A. Thus a ≤ b [as was to be shown].

### Theorem 4.3.2: Divisors of 1
The only divisors of 1 are 1 and −1.

**Proof:**
Since 1· 1 = 1 and (−1)(−1) = 1, both 1 and −1 are divisors of 1. Now suppose m is any integer that divides 1. Then there exists an integer n such that 1 = mn. By Theorem T25 in Appendix A, either both m and n are positive or both m and n are negative. If both m and n are positive, then m is a positive integer divisor of 1. By Theorem 4.3.1, m ≤ 1, and, since the only positive integer that is less than or equal to 1 is 1 itself, it follows that m = 1. On the other hand, if both m and n are negative, then, by Theorem T12 in Appendix A, (−m)(−n) = mn = 1. In this case −m is a positive integer divisor of 1, and so, by the same reasoning, −m = 1 and thus m = −1. Therefore there are only two possibilities: either m = 1 or m = −1. So the only divisors of 1 are 1 and −1.

### Example 4.3.3: Divisibility of Algebraic Expressions
a. If a and b are integers, is 3a + 3b divisible by 3?
b. If k and m are integers, is 10km divisible by 5?

**Solution:**
a. Yes. By the distributive law of algebra, 3a + 3b = 3(a + b) and a + b is an integer because it is a sum of two integers.
b. Yes. By the associative law of algebra, 10km = 5 · (2km) and 2km is an integer because it is a product of three integers.

### Formal Definition Using Existential Quantifier
When the definition of divides is rewritten formally using the existential quantifier, the result is:
d | n ⇔ ∃ an integer k such that n = dk.

### Nondivisibility Definition
Since the negation of an existential statement is universal, it follows that d does not divide n (denoted d ∤ n) if, and only if, ∀ integers k, n ≠ dk, or, in other words, the quotient n/d is not an integer.

For all integers n and d:
d ∤ n ⇔ n/d is not an integer.

### Example 4.3.4: Checking Nondivisibility
Does 4 | 15?

**Solution:**
No, 15/4 = 3.75, which is not an integer.

### Caution About Notation
Be careful to distinguish between the notation a | b and the notation a/b. The notation a | b stands for the sentence "a divides b," which means that there is an integer k such that b = ak. Dividing both sides by a gives b/a = k, an integer. Thus, when a ≠ 0, a | b if, and only if, b/a is an integer. On the other hand, the notation a/b stands for the number a/b which is the result of dividing a by b and which may or may not be an integer. In particular, be sure to avoid writing things like:
4 | (3 + 5) = 4 | 8
If read out loud, this becomes, "4 divides the quantity 3 plus 5 equals 4 divides 8," which is nonsense.

### Example 4.3.5: Prime Numbers and Divisibility
An alternative way to define a prime number is to say that an integer n > 1 is prime if, and only if, its only positive integer divisors are 1 and itself.

### Proving Properties of Divisibility
One of the most useful properties of divisibility is that it is transitive. If one number divides a second and the second number divides a third, then the first number divides the third.

### Example 4.3.6: Transitivity of Divisibility
Prove that for all integers a, b, and c, if a | b and b | c, then a | c.

**Solution:**
Since the statement to be proved is already written formally, you can immediately pick out the starting point, or first sentence of the proof, and the conclusion that must be shown.

**Starting Point:** Suppose a, b, and c are particular but arbitrarily chosen integers such that a | b and b | c.

**To Show:** a | c.

You need to show that a | c, or, in other words, that c = a · (some integer).

But since a | b, b = ar for some integer r. (Equation 4.3.1)

And since b | c, c = bs for some integer s. (Equation 4.3.2)

Equation 4.3.2 expresses c in terms of b, and equation 4.3.1 expresses b in terms of a. Thus if you substitute 4.3.1 into 4.3.2, you will have an equation that expresses c in terms of a.

c = bs = (ar)s = a(rs) by the associative law for multiplication.

Hence c = a(rs).

Now you are almost finished. You have expressed c as a · (something). It remains only to verify that that something is an integer. But of course it is, because it is a product of two integers.

### Theorem 4.3.3: Transitivity of Divisibility
For all integers a, b, and c, if a divides b and b divides c, then a divides c.

**Proof:**
Suppose a, b, and c are [particular but arbitrarily chosen] integers such that a divides b and b divides c. [We must show that a divides c.] By definition of divisibility:
b = ar and c = bs for some integers r and s.

By substitution:
c = bs = (ar)s = a(rs) by basic algebra.

Let k = rs. Then k is an integer since it is a product of integers, and therefore:
c = ak where k is an integer.

Thus a divides c by definition of divisibility. [This is what was to be shown.]

### Theorem 4.3.4: Divisibility by a Prime
Any integer n > 1 is divisible by a prime number.

**Proof:**
Suppose n is a [particular but arbitrarily chosen] integer that is greater than 1. [We must show that there is a prime number that divides n.] If n is prime, then n is divisible by a prime number (namely itself), and we are done. If n is not prime, then, as discussed in Example 4.1.2b:
n = r₀s₀ where r₀ and s₀ are integers and 1 < r₀ < n and 1 < s₀ < n.

It follows by definition of divisibility that r₀ | n.

If r₀ is prime, then r₀ is a prime number that divides n, and we are done. If r₀ is not prime, then:
r₀ = r₁s₁ where r₁ and s₁ are integers and 1 < r₁ < r₀ and 1 < s₁ < r₀.

It follows by the definition of divisibility that r₁ | r₀. But we already know that r₀ | n. Consequently, by transitivity of divisibility, r₁ | n.

If r₁ is prime, then r₁ is a prime number that divides n, and we are done. If r₁ is not prime, then:
r₁ = r₂s₂ where r₂ and s₂ are integers and 1 < r₂ < r₁ and 1 < s₂ < r₁.

It follows by definition of divisibility that r₂ | r₁. But we already know that r₁ | n. Consequently, by transitivity of divisibility, r₂ | n.

If r₂ is prime, then r₂ is a prime number that divides n, and we are done. If r₂ is not prime, then we may repeat the previous process by factoring r₂ as r₃s₃.

We may continue in this way, factoring successive factors of n until we find a prime factor. We must succeed in a finite number of steps because each new factor is both less than the previous one (which is less than n) and greater than 1, and there are fewer than n integers strictly between 1 and n. Thus we obtain a sequence r₀, r₁, r₂, ..., rₖ, where k ≥ 0, 1 < rₖ < rₖ₋₁ < · · · < r₂ < r₁ < r₀ < n, and rᵢ | n for each i = 0, 1, 2, ..., k. The condition for termination is that rₖ should be prime. Hence rₖ is a prime number that divides n. [This is what we were to show.]

### Counterexamples and Divisibility
To show that a proposed divisibility property is not universally true, you need only find one pair of integers for which it is false.

### Example 4.3.7: Checking a Proposed Divisibility Property
Is the following statement true or false? For all integers a and b, if a | b and b | a then a = b.

**Solution:**
This statement is false. Can you think of a counterexample just by concentrating for a minute or so?

The following discussion describes a mental process that may take just a few seconds. It is helpful to be able to use it consciously, however, to solve more difficult problems.

To discover the truth or falsity of a statement such as the one given above, start off much as you would if you were trying to prove it.

**Starting Point:** Suppose a and b are integers such that a | b and b | a.

Ask yourself, "Must it follow that a = b, or could it happen that a ≠ b for some a and b?"

Focus on the supposition. What does it mean? By definition of divisibility, the conditions a | b and b | a mean that:
b = ka and a = lb for some integers k and l.

Must it follow that a = b, or can you find integers a and b that satisfy these equations for which a ≠ b? The equations imply that:
b = ka = k(lb) = (kl)b.

Since b | a, b ≠ 0, and so you can cancel b from the extreme left and right sides to obtain:
1 = kl.

In other words, k and l are divisors of 1. But, by Theorem 4.3.2, the only divisors of 1 are 1 and −1. Thus k and l are both 1 or are both −1. If k = l = 1, then b = a. But if k = l = −1, then b = −a and so a ≠ b. This analysis suggests that you can find a counterexample by taking b = −a. Here is a formal answer:

**Proposed Divisibility Property:** For all integers a and b, if a | b and b | a then a = b.

**Counterexample:** Let a = 2 and b = −2. Then a | b since 2 | (−2) and b | a since (−2) | 2, but a ≠ b since 2 ≠ −2.

Therefore, the statement is false.

### The Unique Factorization of Integers Theorem
The most comprehensive statement about divisibility of integers is contained in the unique factorization of integers theorem. Because of its importance, this theorem is also called the fundamental theorem of arithmetic. Although Euclid, who lived about 300 B.C., seems to have been acquainted with the theorem, it was first stated precisely by the great German mathematician Carl Friedrich Gauss (rhymes with house) in 1801.

The unique factorization of integers theorem says that any integer greater than 1 either is prime or can be written as a product of prime numbers in a way that is unique except, perhaps, for the order in which the primes are written. For example:
72 = 2·2·2·3·3 = 2·3·3·2·2 = 3·2·2·3·2
and so forth. The three 2's and two 3's may be written in any order, but any factorization of 72 as a product of primes must contain exactly three 2's and two 3's—no other collection of prime numbers besides three 2's and two 3's multiplies out to 72.

### Note About Why 1 is Not Prime
This theorem is the reason the number 1 is not allowed to be prime. If 1 were prime, then factorizations would not be unique. For example, 6 = 2 · 3 = 1 · 2 · 3, and so forth.

### Theorem 4.3.5: Unique Factorization of Integers Theorem (Fundamental Theorem of Arithmetic)
Given any integer n > 1, there exist a positive integer k, distinct prime numbers p₁, p₂, ..., pₖ, and positive integers e₁, e₂, ..., eₖ such that:
n = p₁ᵉ¹ p₂ᵉ² p₃ᵉ³ ... pₖᵉᵏ,

and any other expression for n as a product of prime numbers is identical to this except, perhaps, for the order in which the factors are written.

The proof of the unique factorization theorem is outlined in the exercises for Sections 5.4 and 8.4.

### Standard Factored Form
Because of the unique factorization theorem, any integer n > 1 can be put into a standard factored form in which the prime factors are written in ascending order from left to right.

### Definition: Standard Factored Form
Given any integer n > 1, the standard factored form of n is an expression of the form:
n = p₁ᵉ¹ p₂ᵉ² p₃ᵉ³ · · · pₖᵉᵏ,

where k is a positive integer; p₁, p₂, ..., pₖ are prime numbers; e₁, e₂, ..., eₖ are positive integers; and p₁ < p₂ < · · · < pₖ.

### Example 4.3.8: Writing Integers in Standard Factored Form
Write 3,300 in standard factored form.

**Solution:**
First find all the factors of 3,300. Then write them in ascending order:
3,300 = 100· 33 = 4· 25· 3 · 11
= 2 · 2 · 5· 5 · 3 · 11 = 2² · 3¹ · 5² · 11¹.

### Example 4.3.9: Using Unique Factorization to Solve a Problem
Suppose m is an integer such that:
8 ·7 · 6 · 5 · 4· 3 · 2· m = 17· 16· 15· 14· 13· 12· 11· 10.

Does 17 | m?

**Solution:**
Since 17 is one of the prime factors of the right-hand side of the equation, it is also a prime factor of the left-hand side (by the unique factorization of integers theorem). But 17 does not equal any prime factor of 8, 7, 6, 5, 4, 3, or 2 (because it is too large). Hence 17 must occur as one of the prime factors of m, and so 17 | m.

### Test Yourself Questions
1. To show that a nonzero integer d divides an integer n, we must show that _____.
2. To say that d divides n means the same as saying that _____ is divisible by _____.
3. If a and b are positive integers and a | b, then _____ is less than or equal to _____.
4. For all integers n and d, d ∤ n if, and only if, _____.
5. If a and b are integers, the notation a | b denotes _____ and the notation a/b denotes _____.
6. The transitivity of divisibility theorem says that for all integers a, b, and c, if _____ then _____.
7. The divisibility by a prime theorem says that every integer greater than 1 is _____.
8. The unique factorization of integers theorem says that any integer greater than 1 is either _____ or can be written as _____ in a way that is unique except possibly for the _____ in which the numbers are written.

### Exercise Set 4.3

**Questions 1-13: Basic Divisibility**
1. Is 52 divisible by 13?
2. Does 7 | 56?
3. Does 5 | 0?
4. Does 3 divide (3k + 1)(3k + 2)(3k + 3)?
5. Is 6m(2m + 10) divisible by 4?
6. Is 29 a multiple of 3?
7. Is −3 a factor of 66?
8. Is 6a(a + b) a multiple of 3a?
9. Is 4 a factor of 2a · 34b?
10. Does 7 | 34?
11. Does 13 | 73?
12. If n = 4k + 1, does 8 divide n² − 1?
13. If n = 4k + 3, does 8 divide n² − 1?

**Questions 14-18: Formal Proofs**
14. Fill in the blanks in the following proof that for all integers a and b, if a | b then a | (−b).
    Proof: Suppose a and b are any integers such that (a) _____. By definition of divisibility, there exists an integer r such that (b) _____. By substitution, −b = −ar = a(−r). Let t = (c) _____. Then t is an integer because t = (−1) ·r, and both −1 and r are integers. Thus, by substitution, −b = at, where r is an integer, and so by definition of divisibility, (d) _____, as was to be shown.
15. Prove that for all integers a, b, and c, if a | b and a | c then a | (b + c).
16. Prove that for all integers a, b, and c, if a | b and a | c then a | (b − c).
17. Consider the following statement: The negative of any multiple of 3 is a multiple of 3.
    a. Write the statement formally using a quantifier and a variable.
    b. Determine whether the statement is true or false and justify your answer.
18. Show that the following statement is false: For all integers a and b, if 3 | (a + b) then 3 | (a − b).

**Questions 19-31: True/False with Proofs**
19. For all integers a, b, and c, if a divides b then a divides bc.
20. The sum of any three consecutive integers is divisible by 3. (Two integers are consecutive if, and only if, one is one more than the other.)
21. The product of any two even integers is a multiple of 4.
22. A necessary condition for an integer to be divisible by 6 is that it be divisible by 2.
23. A sufficient condition for an integer to be divisible by 8 is that it be divisible by 16.
24. For all integers a, b, and c, if a | b and a | c then a | (2b − 3c).
25. For all integers a, b, and c, if a is a factor of c then ab is a factor of c.
26. For all integers a, b, and c, if ab | c then a | c and b | c.
27. For all integers a, b, and c, if a | (b + c) then a | b or a | c.
28. For all integers a, b, and c, if a | bc then a | b or a | c.
29. For all integers a and b, if a | b then a² | b².
30. For all integers a and n, if a | n² and a ≤ n then a | n.
31. For all integers a and b, if a | 10b then a | 10 or a | b.

**Questions 32-49: Applied Problems**
32. A fast-food chain has a contest in which a card with numbers on it is given to each customer who makes a purchase. If some of the numbers on the card add up to 100, then the customer wins $100. A certain customer receives a card containing the numbers 72, 21, 15, 36, 69, 81, 9, 27, 42, and 63. Will the customer win $100? Why or why not?
33. Is it possible to have a combination of nickels, dimes, and quarters that add up to $4.72? Explain.
34. Is it possible to have 50 coins, made up of pennies, dimes, and quarters, that add up to $3? Explain.
35. Two athletes run a circular track at a steady pace so that the first completes one round in 8 minutes and the second in 10 minutes. If they both start from the same spot at 4 P.M., when will be the first time they return to the start together?
36. It can be shown (see exercises 44–48) that an integer is divisible by 3 if, and only if, the sum of its digits is divisible by 3. An integer is divisible by 9 if, and only if, the sum of its digits is divisible by 9. An integer is divisible by 5 if, and only if, its right-most digit is a 5 or a 0. And an integer is divisible by 4 if, and only if, the number formed by its right-most two digits is divisible by 4. Check the following integers for divisibility by 3, 4, 5 and 9.
    a. 637,425,403,705,125
    b. 12,858,306,120,312
    c. 517,924,440,926,512
    d. 14,328,083,360,232
37. Use the unique factorization theorem to write the following integers in standard factored form.
    a. 1,176
    b. 5,733
    c. 3,675
38. Suppose that in standard factored form a = p₁ᵉ¹ p₂ᵉ² · · · pₖᵉᵏ, where k is a positive integer; p₁, p₂, ..., pₖ are prime numbers; and e₁, e₂, ..., eₖ are positive integers.
    a. What is the standard factored form for a²?
    b. Find the least positive integer n such that 2⁵ · 3 · 5² · 7³ · n is a perfect square. Write the resulting product as a perfect square.
    c. Find the least positive integer m such that 2² · 3⁵ · 7 · 11 · m is a perfect square. Write the resulting product as a perfect square.
39. Suppose that in standard factored form a = p₁ᵉ¹ p₂ᵉ² · · · pₖᵉᵏ, where k is a positive integer; p₁, p₂, ..., pₖ are prime numbers; and e₁, e₂, ..., eₖ are positive integers.
    a. What is the standard factored form for a³?
    b. Find the least positive integer k such that 2⁴ · 3⁵ · 7 · 11² · k is a perfect cube (i.e., equals an integer to the third power). Write the resulting product as a perfect cube.
40. a. If a and b are integers and 12a = 25b, does 12 | b? does 25 | a? Explain.
    b. If x and y are integers and 10x = 9y, does 10 | y? does 9 | x? Explain.
41. How many zeros are at the end of 45⁸ · 88⁵? Explain how you can answer this question without actually computing the number. (Hint: 10 = 2 · 5.)
42. If n is an integer and n > 1, then n! is the product of n and every other positive integer that is less than n. For example, 5! = 5 · 4 · 3 · 2 · 1.
    a. Write 6! in standard factored form.
    b. Write 20! in standard factored form.
    c. Without computing the value of (20!)² determine how many zeros are at the end of this number when it is written in decimal form. Justify your answer.
43. In a certain town 2/3 of the adult men are married to 3/5 of the adult women. Assume that all marriages are monogamous (no one is married to more than one other person). Also assume that there are at least 100 adult men in the town. What is the least possible number of adult men in the town? of adult women in the town?
44. Prove that if n is any nonnegative integer whose decimal representation ends in 0, then 5 | n. (Hint: If the decimal representation of a nonnegative integer n ends in d₀, then n = 10m + d₀ for some integer m.)
45. Prove that if n is any nonnegative integer whose decimal representation ends in 5, then 5 | n.
46. Prove that if the decimal representation of a nonnegative integer n ends in d₁d₀ and if 4 | (10d₁ + d₀), then 4 | n. (Hint: If the decimal representation of a nonnegative integer n ends in d₁d₀, then there is an integer s such that n = 100s + 10d₁ + d₀.)
47. Prove that for any nonnegative integer n, if the sum of the digits of n is divisible by 9, then n is divisible by 9.
48. Prove that for any nonnegative integer n, if the sum of the digits of n is divisible by 3, then n is divisible by 3.
49. Given a positive integer n written in decimal form, the alternating sum of the digits of n is obtained by starting with the right-most digit, subtracting the digit immediately to its left, adding the next digit to the left, subtracting the next digit, and so forth. For example, the alternating sum of the digits of 180,928 is 8 − 2 + 9 − 0 + 8 − 1 = 22. Justify the fact that for any nonnegative integer n, if the alternating sum of the digits of n is divisible by 11, then n is divisible by 11.

## Chapter 4.4: Direct Proof and Counterexample IV: Division into Cases and the Quotient-Remainder Theorem

### Introduction
Be especially critical of any statement following the word "obviously." — Anna Pell Wheeler 1883–1966

When you divide 11 by 4, you get a quotient of 2 and a remainder of 3.
```
  2 ← quotient
4)11
  8
  3 ← remainder
```

Another way to say this is that 11 equals 2 groups of 4 with 3 left over:
```
xxxx    xxxx    xxx
↑       ↑       ↑
2 groups of 4   3 left over
```

Or, 11 = 2· 4 + 3.
        ↑     ↑
    2 groups of 4   3 left over

Of course, the number left over (3) is less than the size of the groups (4) because if 4 or more were left over, another group of 4 could be separated off.

The quotient-remainder theorem says that when any integer n is divided by any positive integer d, the result is a quotient q and a nonnegative remainder r that is smaller than d.

### Theorem 4.4.1: The Quotient-Remainder Theorem
Given any integer n and positive integer d, there exist unique integers q and r such that:
n = dq + r and 0 ≤ r < d.

The proof that there exist integers q and r with the given properties is in Section 5.4; the proof that q and r are unique is outlined in exercise 18 in Section 4.7.

### Illustration on Number Line
If n is positive, the quotient-remainder theorem can be illustrated on the number line as follows:
```
0    d    2d    3d    qd    n
                        r
```

If n is negative, the picture changes. Since n = dq + r, where r is nonnegative, d must be multiplied by a negative integer q to go below n. Then the nonnegative integer r is added to come back up to n. This is illustrated as follows:
```
qd    n    -3d    -2d    -d    0     r
```

### Key Concepts from Chapter 4.3
- Definition of divisibility: d | n ⇔ ∃ an integer k such that n = dk
- Theorem 4.3.1: A positive divisor of a positive integer
- Theorem 4.3.2: Divisors of 1
- Theorem 4.3.3: Transitivity of divisibility
- Theorem 4.3.4: Divisibility by a prime
- Theorem 4.3.5: Unique factorization of integers theorem
- Standard factored form of integers
- Properties of divisors and multiples

### Complete Theorem Summary for Chapter 4.3:
1. **Theorem 4.3.1**: For all integers a and b, if a and b are positive and a divides b, then a ≤ b.
2. **Theorem 4.3.2**: The only divisors of 1 are 1 and −1.
3. **Theorem 4.3.3**: For all integers a, b, and c, if a divides b and b divides c, then a divides c.
4. **Theorem 4.3.4**: Any integer n > 1 is divisible by a prime number.
5. **Theorem 4.3.5**: Given any integer n > 1, there exist a positive integer k, distinct prime numbers p₁, p₂, ..., pₖ, and positive integers e₁, e₂, ..., eₖ such that n = p₁ᵉ¹ p₂ᵉ² p₃ᵉ³ ... pₖᵉᵏ, and any other expression for n as a product of prime numbers is identical to this except, perhaps, for the order in which the factors are written.

### All Key Equations and Formulas:
- **Divisibility Definition**: d | n ⇔ ∃ an integer k such that n = dk
- **Nondivisibility**: d ∤ n ⇔ n/d is not an integer
- **Standard Factored Form**: n = p₁ᵉ¹ p₂ᵉ² p₃ᵉ³ · · · pₖᵉᵏ where p₁ < p₂ < · · · < pₖ
- **Quotient-Remainder**: n = dq + r where 0 ≤ r < d

### Common Mistakes to Avoid
- Confusing the notation a | b (divides) with a/b (division)
- Assuming that if a | bc, then a | b or a | c (this is not always true)
- Forgetting that divisibility is transitive
- Misapplying the unique factorization theorem
- Not distinguishing between a | b and a/b

### Important Definitions
- **Divisibility**: d | n ⇔ ∃ an integer k such that n = dk
- **Standard factored form**: n = p₁ᵉ¹ p₂ᵉ² p₃ᵉ³ · · · pₖᵉᵏ where p₁ < p₂ < · · · < pₖ
- **Prime factorization**: expressing a number as a product of prime factors
- **Nondivisibility**: d ∤ n when n/d is not an integer