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

### Example 4.4.1: The Quotient-Remainder Theorem
For each of the following values of n and d, find integers q and r such that n = dq + r and 0 ≤ r < d.
a. n = 54, d = 4
b. n = −54, d = 4
c. n = 54, d = 70

**Solution:**
a. 54 = 4· 13 + 2; hence q = 13 and r = 2.
b. −54 = 4 ·(−14) + 2; hence q = −14 and r = 2.
c. 54 = 70· 0 + 54; hence q = 0 and r = 54.

### div and mod
A number of computer languages have built-in functions that enable you to compute many values of q and r for the quotient-remainder theorem. These functions are called div and mod in Pascal, are called / and % in C and C++, are called / and % in Java, and are called / (or \) and mod in .NET. The functions give the values that satisfy the quotient-remainder theorem when a nonnegative integer n is divided by a positive integer d and the result is assigned to an integer variable. However, they do not give the values that satisfy the quotient-remainder theorem when a negative integer n is divided by a positive integer d.

### Definition
Given an integer n and a positive integer d,
n div d = the integer quotient obtained when n is divided by d, and
n mod d = the nonnegative integer remainder obtained when n is divided by d.

Symbolically, if n and d are integers and d > 0, then
n div d = q and n mod d = r ⇔ n = dq + r
where q and r are integers and 0 ≤ r < d.

Note that it follows from the quotient-remainder theorem that n mod d equals one of the integers from 0 through d − 1 (since the remainder of the division of n by d must be one of these integers). Note also that a necessary and sufficient condition for an integer n to be divisible by an integer d is that n mod d = 0. You are asked to prove this in the exercises at the end of this section.

You can also use a calculator to compute values of div and mod. For instance, to compute n div d for a nonnegative integer n and a positive integer d, you just divide n by d and ignore the part of the answer to the right of the decimal point. To find n mod d, you can use the fact that if n = dq + r, then r = n − dq. Thus n = d ·(n div d) + n mod d, and so
n mod d = n − d · (n div d).

Hence, to find n mod d compute n div d, multiply by d, and subtract the result from n.

### Example 4.4.2: Computing div and mod
Compute 32 div 9 and 32 mod 9 by hand and with a calculator.

**Solution:**
Performing the division by hand gives the following results:
```
3 ← 32 div 9
9)32
  27
   5 ← 32 mod 9
```

If you use a four-function calculator to divide 32 by 9, you obtain an expression like 3.555555556. Discarding the fractional part gives 32 div 9 = 3, and so
32 mod 9 = 32 − 9 · (32 div 9) = 32 − 27 = 5.

A calculator with a built-in integer-part function iPart allows you to input a single expression for each computation:
32 div 9 = iPart(32/9) and
32 mod 9 = 32 − 9 · iPart (32/9) = 5.

### Example 4.4.3: Computing the Day of the Week
Suppose today is Tuesday, and neither this year nor next year is a leap year. What day of the week will it be 1 year from today?

**Solution:**
There are 365 days in a year that is not a leap year, and each week has 7 days.

Now
365 div 7 = 52 and 365 mod 7 = 1
because 365 = 52· 7 + 1. Thus 52 weeks, or 364 days, from today will be a Tuesday, and so 365 days from today will be 1 day later, namely Wednesday.

More generally, if DayT is the day of the week today and DayN is the day of the week in N days, then
DayN = (DayT + N ) mod 7,
where Sunday = 0, Monday = 1, . . . , Saturday = 6.

### Example 4.4.4: Solving a Problem about mod
Suppose m is an integer. If m mod 11 = 6, what is 4m mod 11?

**Solution:**
Because m mod 11 = 6, the remainder obtained when m is divided by 11 is 6. This means that there is some integer q so that
m = 11q + 6.
Thus
4m = 44q + 24 = 44q + 22 + 2 = 11(4q + 2) + 2.

Since 4q + 2 is an integer (because products and sums of integers are integers) and since 2 < 11, the remainder obtained when 4m is divided by 11 is 2. Therefore,
4m mod 11 = 2.

### Representations of Integers
In Section 4.1 we defined an even integer to have the form twice some integer. At that time we could have defined an odd integer to be one that was not even. Instead, because it was more useful for proving theorems, we specified that an odd integer has the form twice some integer plus one. The quotient-remainder theorem brings these two ways of describing odd integers together by guaranteeing that any integer is either even or odd.

To see why, let n be any integer, and consider what happens when n is divided by 2. By the quotient-remainder theorem (with d = 2), there exist unique integers q and r such that
n = 2q + r and 0 ≤ r < 2.

But the only integers that satisfy 0 ≤ r < 2 are r = 0 and r = 1. It follows that given any integer n, there exists an integer q with
n = 2q + 0 or n = 2q + 1.

In the case that n = 2q + 0 = 2q, n is even. In the case that n = 2q + 1, n is odd. Hence n is either even or odd, and, because of the uniqueness of q and r, n cannot be both even and odd.

The parity of an integer refers to whether the integer is even or odd. For instance, 5 has odd parity and 28 has even parity. We call the fact that any integer is either even or odd the parity property.

### Example 4.4.5: Consecutive Integers Have Opposite Parity
Prove that given any two consecutive integers, one is even and the other is odd.

**Solution:**
Two integers are called consecutive if, and only if, one is one more than the other. So if one integer is m, the next consecutive integer is m + 1.

To prove the given statement, start by supposing that you have two particular but arbitrarily chosen consecutive integers. If the smaller is m, then the larger will be m + 1.

How do you know for sure that one of these is even and the other is odd? You might imagine some examples: 4, 5; 12, 13; 1,073, 1,074. In the first two examples, the smaller of the two integers is even and the larger is odd; in the last example, it is the reverse. These observations suggest dividing the analysis into two cases.

Case 1: The smaller of the two integers is even.
Case 2: The smaller of the two integers is odd.

In the first case, when m is even, it appears that the next consecutive integer is odd. Is this always true? If an integer m is even, must m + 1 necessarily be odd? Of course the answer is yes. Because if m is even, then m = 2k for some integer k, and so m + 1 = 2k + 1, which is odd.

In the second case, when m is odd, it appears that the next consecutive integer is even. Is this always true? If an integer m is odd, must m + 1 necessarily be even? Again, the answer is yes. For if m is odd, then m = 2k + 1 for some integer k, and so m + 1 = (2k + 1) + 1 = 2k + 2 = 2(k + 1), which is even.

This discussion is summarized on the following page.

### Theorem 4.4.2: The Parity Property
Any two consecutive integers have opposite parity.

**Proof:**
Suppose that two [particular but arbitrarily chosen] consecutive integers are given; call them m and m + 1. [We must show that one of m and m + 1 is even and that the other is odd.] By the parity property, either m is even or m is odd. [We break the proof into two cases depending on whether m is even or odd.]

Case 1 (m is even): In this case, m = 2k for some integer k, and so m + 1 = 2k + 1, which is odd [by definition of odd]. Hence in this case, one of m and m + 1 is even and the other is odd.

Case 2 (m is odd): In this case, m = 2k + 1 for some integer k, and so m + 1 = (2k + 1) + 1 = 2k + 2 = 2(k + 1). But k + 1 is an integer because it is a sum of two integers. Therefore, m + 1 equals twice some integer, and thus m + 1 is even. Hence in this case also, one of m and m + 1 is even and the other is odd.

It follows that regardless of which case actually occurs for the particular m and m + 1 that are chosen, one of m and m + 1 is even and the other is odd. [This is what was to be shown.]

The division into cases in a proof is like the transfer of control for an if-then-else statement in a computer program. If m is even, control transfers to case 1; if not, control transfers to case 2. For any given integer, only one of the cases will apply. You must consider both cases, however, to obtain a proof that is valid for an arbitrarily given integer whether even or not.

There are times when division into more than two cases is called for. Suppose that at some stage of developing a proof, you know that a statement of the form
A1 or A2 or A3 or . . . or An
is true, and suppose you want to deduce a conclusion C. By definition of or, you know that at least one of the statements Ai is true (although you may not know which). In this situation, you should use the method of division into cases. First assume A1 is true and deduce C; next assume A2 is true and deduce C; and so forth until you have assumed An is true and deduced C. At that point, you can conclude that regardless of which statement Ai happens to be true, the truth of C follows.

### Method of Proof by Division into Cases
To prove a statement of the form "If A1 or A2 or . . . or An, then C," prove all of the following:
If A1, then C,
If A2, then C,
..
.
If An, then C.

This process shows that C is true regardless of which of A1, A2, . . . , An happens to be the case.

Proof by division into cases is a generalization of the argument form shown in Example 2.3.7, whose validity you were asked to establish in exercise 21 of Section 2.3. This method of proof was combined with the quotient-remainder theorem for d = 2 to prove Theorem 4.4.2. Allowing d to take on additional values makes it possible to obtain a variety of other results. We begin by showing what happens when a = 4.

### Example 4.4.6: Representations of Integers Modulo 4
Show that any integer can be written in one of the four forms
n = 4q or n = 4q + 1 or n = 4q + 2 or n = 4q + 3
for some integer q.

**Solution:**
Given any integer n, apply the quotient-remainder theorem to n with d = 4. This implies that there exist an integer quotient q and a remainder r such that
n = 4q + r and 0 ≤ r < 4.

But the only nonnegative remainders r that are less than 4 are 0, 1, 2, and 3. Hence
n = 4q or n = 4q + 1 or n = 4q + 2 or n = 4q + 3
for some integer q.

The next example illustrates how the alternative representations for integers modulo 4 can help establish a result in number theory. The solution is broken into two parts: a discussion and a formal proof. These correspond to the stages of actual proof development. Very few people, when asked to prove an unfamiliar theorem, immediately write down the kind of formal proof you find in a mathematics text. Most need to experiment with several possible approaches before they find one that works. A formal proof is much like the ending of a mystery story—the part in which the action of the story is systematically reviewed and all the loose ends are carefully tied together.

### Example 4.4.7: The Square of an Odd Integer
Prove: The square of any odd integer has the form 8m + 1 for some integer m.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: ∀ odd integers n, ∃ an integer m such that n² = 8m + 1.

From this, you can immediately identify the starting point and what is to be shown.
Starting Point: Suppose n is a particular but arbitrarily chosen odd integer.
To Show: ∃ an integer m such that n² = 8m + 1.

This looks tough. Why should there be an integer m with the property that n² = 8m + 1? That would say that (n² − 1)/8 is an integer, or that 8 divides n² − 1. Perhaps you could make use of the fact that n² − 1 = (n − 1)(n + 1). Does 8 divide (n − 1)(n + 1)? Since n is odd, both (n − 1) and (n + 1) are even. That means that their product is divisible by 4. But that's not enough. You need to show that the product is divisible by 8. This seems to be a blind alley.

You could try another tack. Since n is odd, you could represent n as 2q + 1 for some integer q. Then n² = (2q + 1)² = 4q² + 4q + 1 = 4(q² + q) + 1. It is clear from this analysis that n² can be written in the form 4m + 1, but it may not be clear that it can be written as 8m + 1. This also seems to be a blind alley.

Yet another possibility is to use the result of Example 4.4.6. That example showed that any integer can be written in one of the four forms 4q, 4q + 1, 4q + 2, or 4q + 3. Two of these, 4q + 1 and 4q + 3, are odd. Thus any odd integer can be written in the form 4q + 1 or 4q + 3 for some integer q. You could try breaking into cases based on these two different forms.

It turns out that this last possibility works! In each of the two cases, the conclusion follows readily by direct calculation. The details are shown in the following formal proof:

### Theorem 4.4.3
The square of any odd integer has the form 8m + 1 for some integer m.

**Proof:**
Suppose n is a [particular but arbitrarily chosen] odd integer. By the quotient-remainder theorem, n can be written in one of the forms
4q or 4q + 1 or 4q + 2 or 4q + 3
for some integer q. In fact, since n is odd and 4q and 4q + 2 are even, n must have one of the forms
4q + 1 or 4q + 3.

Case 1 (n = 4q + 1 for some integer q): [We must find an integer m such that n² = 8m + 1.] Since n = 4q + 1,
n² = (4q + 1)² by substitution
= (4q + 1)(4q + 1)
= 16q² + 8q + 1
= 8(2q² + q) + 1 by the laws of algebra.

Let m = 2q² + q. Then m is an integer since 2 and q are integers and sums and products of integers are integers. Thus, substituting,
n² = 8m + 1 where m is an integer.

Case 2 (n = 4q + 3 for some integer q): [We must find an integer m such that n² = 8m + 1.] Since n = 4q + 3,
n² = (4q + 3)² by substitution
= (4q + 3)(4q + 3)
= 16q² + 24q + 9
= 16q² + 24q + (8 + 1)
= 8(2q² + 3q + 1) + 1 by the laws of algebra.

[The motivation for the choice of algebra steps was the desire to write the expression in the form 8 · (some integer) + 1.]

Let m = 2q² + 3q + 1. Then m is an integer since 1, 2, 3, and q are integers and sums and products of integers are integers. Thus, substituting,
n² = 8m + 1 where m is an integer.

Cases 1 and 2 show that given any odd integer, whether of the form 4q + 1 or 4q + 3, n² = 8m + 1 for some integer m. [This is what we needed to show.]

Note that the result of Theorem 4.4.3 can also be written, "For any odd integer n, n² mod 8 = 1."

In general, according to the quotient-remainder theorem, if an integer n is divided by an integer d, the possible remainders are 0, 1, 2, . . ., (d − 1). This implies that n can be written in one of the forms
dq, dq + 1, dq + 2, , . . . , dq + (d − 1)
for some integer q.

Many properties of integers can be obtained by giving d a variety of different values and analyzing the cases that result.

### Absolute Value and the Triangle Inequality
The triangle inequality is one of the most important results involving absolute value. It has applications in many areas of mathematics.

### Definition
For any real number x, the absolute value of x, denoted |x|, is defined as follows:
|x| = { x if x ≥ 0
      { -x if x < 0

The triangle inequality says that the absolute value of the sum of two numbers is less than or equal to the sum of their absolute values. We give a proof based on the following two facts, both of which are derived using division into cases. We state both as lemmas. A lemma is a statement that does not have much intrinsic interest but is helpful in deriving other results.

### Lemma 4.4.4
For all real numbers r, −|r | ≤ r ≤ |r |.

**Proof:**
Suppose r is any real number. We divide into cases according to whether r ≥ 0 or r < 0.

Case 1 (r ≥ 0): In this case, by definition of absolute value, |r | = r. Also, since r is positive and −|r | is negative, −|r | < r. Thus it is true that
−|r | ≤ r ≤ |r |.

Case 2 (r < 0): In this case, by definition of absolute value, |r | = −r. Multiplying both sides by −1 gives that −|r | = r. Also, since r is negative and |r | is positive, r < |r |. Thus it is also true in this case that
−|r | ≤ r ≤ |r |.

Hence, in either case,
−|r | ≤ r ≤ |r |
[as was to be shown].

### Lemma 4.4.5
For all real numbers r, | − r | = |r |.

**Proof:**
Suppose r is any real number. By Theorem T23 in Appendix A, if r > 0, then −r < 0, and if r < 0, then −r > 0. Thus
|−r| = { −r if −r > 0
       {  0 if −r = 0
       { −(−r) if −r < 0
by definition of absolute value

= { −r if −r > 0
  {  0 if −r = 0
  {  r if −r < 0
because −(−r) = r by Theorem T4 in Appendix A

= { −r if r < 0
  {  0 if r = 0
  {  r if r > 0
because, by Theorem T24 in Appendix A, when −r > 0, then r < 0, when −r < 0, then r > 0, and when −r = 0, then r = 0

= { r if r ≥ 0
  { −r if r < 0
by reformatting the previous result

= |r | by definition of absolute value.

Lemmas 4.4.4 and 4.4.5 now provide a basis for proving the triangle inequality.

### Theorem 4.4.6: The Triangle Inequality
For all real numbers x and y, |x + y| ≤ |x| + |y|.

**Proof:**
Suppose x and y are any real numbers.

Case 1 (x + y ≥ 0): In this case, |x + y| = x + y, and so, by Lemma 4.4.4,
x ≤ |x| and y ≤ |y|.

Hence, by Theorem T26 of Appendix A,
|x + y| = x + y ≤ |x| + |y|.

Case 2 (x + y < 0): In this case, |x + y| = −(x + y) = (−x) + (−y), and so, by Lemmas 4.4.4 and 4.4.5,
−x ≤ | − x| = |x| and − y ≤ | − y| = |y|.

It follows, by Theorem T26 of Appendix A, that
|x + y| = (−x) + (−y) ≤ |x| + |y|.

Hence in both cases |x + y| ≤ |x| + |y| [as was to be shown].

### Test Yourself Questions
1. The quotient-remainder theorem says that for all integers n and d with d ≥ 0, there exist _____ q and r such that _____ and _____.
2. If n and d are integers with d > 0, n div d is _____ and n mod d is _____.
3. The parity of an integer indicates whether the integer is _____.
4. According to the quotient-remainder theorem, if an integer n is divided by a positive integer d, the possible remainders are _____. This implies that n can be written in one of the forms _____ for some integer q.
5. To prove a statement of the form "If A1 or A2 or A3, then C," prove _____ and _____ and _____.
6. The triangle inequality says that for all real numbers x and y, _____.

### Exercise Set 4.4

For each of the values of n and d given in 1-6, find integers q and r such that n = dq + r and 0 ≤ r < d.
1. n = 70, d = 9
2. n = 62, d = 7
3. n = 36, d = 40
4. n = 3, d = 11
5. n = −45, d = 11
6. n = −27, d = 8

Evaluate the expressions in 7-10.
7. a. 43 div 9
   b. 43 mod 9
8. a. 50 div 7
   b. 50 mod 7
9. a. 28 div 5
   b. 28 mod 5
10. a. 30 div 2
    b. 30 mod 2

11. Check the correctness of formula (4.4.1) given in Example 4.4.3 for the following values of DayT and N.
    a. DayT = 6 (Saturday) and N = 15
    b. DayT = 0 (Sunday) and N = 7
    c. DayT = 4 (Thursday) and N = 12

12. Justify formula (4.4.1) for general values of DayT and N.
13. On a Monday a friend says he will meet you again in 30 days. What day of the week will that be?
14. If today is Tuesday, what day of the week will it be 1,000 days from today?
15. January 1, 2000, was a Saturday, and 2000 was a leap year. What day of the week will January 1, 2050, be?
16. Suppose d is a positive integer and n is any integer. If d | n, what is the remainder obtained when the quotient-remainder theorem is applied to n with divisor d?

17. Prove that the product of any two consecutive integers is even.
18. The result of exercise 17 suggests that the second apparent blind alley in the discussion of Example 4.4.7 might not be a blind alley after all. Write a new proof of Theorem 4.4.3 based on this observation.
19. Prove that for all integers n, n² − n + 3 is odd.
20. Suppose a is an integer. If a mod 7 = 4, what is 5a mod 7? In other words, if division of a by 7 gives a remainder of 4, what is the remainder when 5a is divided by 7?
21. Suppose b is an integer. If b mod 12 = 5, what is 8b mod 12? In other words, if division of b by 12 gives a remainder of 5, what is the remainder when 8b is divided by 12?
22. Suppose c is an integer. If c mod 15 = 3, what is 10c mod 15? In other words, if division of c by 15 gives a remainder of 3, what is the remainder when 10c is divided by 15?
23. Prove that for all integers n, if n mod 5 = 3 then n² mod 5 = 4.
24. Prove that for all integers m and n, if m mod 5 = 2 and n mod 3 = 6 then mn mod 5 = 1.
25. Prove that for all integers a and b, if a mod 7 = 5 and b mod 7 = 6 then ab mod 7 = 2.
26. Prove that a necessary and sufficient condition for a nonnegative integer n to be divisible by a positive integer d is that n mod d = 0.
27. Show that any integer n can be written in one of the three forms n = 3q or n = 3q + 1 or n = 3q + 2 for some integer q.
28. a. Use the quotient-remainder theorem with d = 3 to prove that the product of any three consecutive integers is divisible by 3.
    b. Use the mod notation to rewrite the result of part (a).
29. a. Use the quotient-remainder theorem with d = 3 to prove that the square of any integer has the form 3k or 3k + 1 for some integer k.
    b. Use the mod notation to rewrite the result of part (a).
30. a. Use the quotient-remainder theorem with d = 3 to prove that the product of any two consecutive integers has the form 3k or 3k + 2 for some integer k.
    b. Use the mod notation to rewrite the result of part (a).
31. a. Prove that for all integers m and n, m + n and m − n are either both odd or both even.
    b. Find all solutions to the equation m² − n² = 56 for which both m and n are positive integers.
    c. Find all solutions to the equation m² − n² = 88 for which both m and n are positive integers.
32. Given any integers a, b, and c, if a − b is even and b − c is even, what can you say about the parity of 2a − (b + c)? Prove your answer.
33. Given any integers a, b, and c, if a − b is odd and b − c is even, what can you say about the parity of a − c? Prove your answer.
34. Given any integer n, if n > 3, could n, n + 2, and n + 4 all be prime? Prove or give a counterexample.

Prove each of the statements in 35-46.
35. The fourth power of any integer has the form 8m or 8m + 1 for some integer m.
36. The product of any four consecutive integers is divisible by 8.
37. The square of any integer has the form 4k or 4k + 1 for some integer k.
38. For any integer n, n² + 5 is not divisible by 4.
39. The sum of any four consecutive integers has the form 4k + 2 for some integer k.
40. For any integer n, n(n − 1)(n + 2) is divisible by 4.
41. For all integers m, m² = 5k, or m² = 5k + 1, or m² = 5k + 4 for some integer k.
42. Every prime number except 2 and 3 has the form 6q + 1 or 6q + 5 for some integer q.
43. If n is an odd integer, then n⁴ mod 16 = 1.
44. For all real numbers x and y, |x| · |y| = |xy|.
45. For all real numbers r and c with c ≥ 0, if −c ≤ r ≤ c, then |r | ≤ c.
46. For all real numbers r and c with c ≥ 0, if |r | ≤ c, then −c ≤ r ≤ c.

47. A matrix M has 3 rows and 4 columns.
```
⎡
a11 a12 a13 a14
⎣a21 a22 a23 a24 ⎦
a31 a32 a33 a34
```
The 12 entries in the matrix are to be stored in row major form in locations 7,609 to 7,620 in a computer's memory. This means that the entries in the first row (reading left to right) are stored first, then the entries in the second row, and finally the entries in the third row.
    a. Which location will a22 be stored in?
    b. Write a formula (in i and j) that gives the integer n so that aij is stored in location 7,609 + n.
    c. Find formulas (in n) for r and s so that ars is stored in location 7,609 + n.

48. Let M be a matrix with m rows and n columns, and suppose that the entries of M are stored in a computer's memory in row major form (see exercise 47) in locations N, N + 1, N + 2, . . . , N + mn − 1. Find formulas in k for r and s so that ars is stored in location N + k.

49. If m, n, and d are integers, d > 0, and m mod d = n mod d, does it necessarily follow that m = n? That m − n is divisible by d? Prove your answers.
50. If m, n, and d are integers, d > 0, and d | (m − n), what is the relation between m mod d and n mod d? Prove your answer.
51. If m, n, a, b, and d are integers, d > 0, and m mod d = a and n mod d = b, is (m + n) mod d = a + b? Is (m + n) mod d = (a + b) mod d? Prove your answers.
52. If m, n, a, b, and d are integers, d > 0, and m mod d = a and n mod d = b, is (mn) mod d = ab? Is (mn) mod d = ab mod d? Prove your answers.
53. Prove that if m, d, and k are integers and d > 0, then (m + dk) mod d = m mod d.

### Answers for Test Yourself
1. integers; n = dq + r; 0 ≤ r < d 2. the quotient obtained when n is divided by d; the nonnegative remainder obtained when n is divided by d 3. odd or even 4. 0, 1, 2, . . ., (d − 1); dq, dq + 1, dq + 2, . . ., dq + (d − 1) 5. If A1, then C; If A2, then C; If A3, then C 6. |x + y| ≤ |x| + |y|

## Chapter 4.5: Direct Proof and Counterexample V: Floor and Ceiling

### Introduction
Proof serves many purposes simultaneously. In being exposed to the scrutiny and judgment of a new audience, [a] proof is subject to a constant process of criticism and revalidation. Errors, ambiguities, and misunderstandings are cleared up by constant exposure. Proof is respectability. Proof is the seal of authority. Proof, in its best instances, increases understanding by revealing the heart of the matter. Proof suggests new mathematics. The novice who studies proofs gets closer to the creation of new mathematics. Proof is mathematical power, the electric voltage of the subject which vitalizes the static assertions of the theorems. Finally, proof is ritual, and a celebration of the power of pure reason. — Philip J. Davis and Reuben Hersh, The Mathematical Experience, 1981

Imagine a real number sitting on a number line. The floor and ceiling of the number are the integers to the immediate left and to the immediate right of the number (unless the number is, itself, an integer, in which case its floor and ceiling both equal the number itself). Many computer languages have built-in functions that compute floor and ceiling automatically. These functions are very convenient to use when writing certain kinds of computer programs. In addition, the concepts of floor and ceiling are important in analyzing the efficiency of many computer algorithms.

### Definitions

**Floor Function:**
Given any real number x, the floor of x, denoted ⌊x⌋, is defined as follows:
⌊x⌋ = that unique integer n such that n ≤ x < n + 1.
Symbolically, if x is a real number and n is an integer, then
⌊x⌋ = n ⇔ n ≤ x < n + 1.

**Ceiling Function:**
Given any real number x, the ceiling of x, denoted ⌈x⌉, is defined as follows:
⌈x⌉ = that unique integer n such that n − 1 < x ≤ n.
Symbolically, if x is a real number and n is an integer, then
⌈x⌉ = n ⇔ n − 1 < x ≤ n.

### Example 4.5.1: Computing Floors and Ceilings
Compute ⌊x⌋ and ⌈x⌉ for each of the following values of x:
a. 25/4
b. 0.999
c. −2.01

**Solution:**
a. 25/4 = 6.25 and 6 < 6.25 < 7; hence ⌊25/4⌋ = 6 and ⌈25/4⌉ = 7.
b. 0 < 0.999 < 1; hence ⌊0.999⌋ = 0 and ⌈0.999⌉ = 1.
c. −3 < −2.01 < −2; hence ⌊−2.01⌋ = −3 and ⌈−2.01⌉ = −2.
Note that on some calculators ⌊x⌋ is denoted INT (x).

### Example 4.5.2: An Application
The 1,370 students at a college are given the opportunity to take buses to an out-of-town game. Each bus holds a maximum of 40 passengers.
a. For reasons of economy, the athletic director will send only full buses. What is the maximum number of buses the athletic director will send?
b. If the athletic director is willing to send one partially filled bus, how many buses will be needed to allow all the students to take the trip?

**Solution:**
a. ⌊1370/40⌋ = ⌊34.25⌋ = 34
b. ⌈1370/40⌉ = ⌈34.25⌉ = 35

### Example 4.5.3: Some General Values of Floor
If k is an integer, what are ⌊k⌋ and ⌊k + 1/2⌋? Why?

**Solution:**
Suppose k is an integer. Then
⌊k⌋ = k because k is an integer and k ≤ k < k + 1,
and
⌊k + 1/2⌋ = k because k is an integer and k ≤ k + 1/2 < k + 1.

### Example 4.5.4: Disproving an Alleged Property of Floor
Is the following statement true or false?
For all real numbers x and y, ⌊x + y⌋ = ⌊x⌋ + ⌊y⌋.

**Solution:**
The statement is false. As a counterexample, take x = y = 1/2. Then
⌊x⌋ + ⌊y⌋ = ⌊1/2⌋ + ⌊1/2⌋ = 0 + 0 = 0,
whereas
⌊x + y⌋ = ⌊1/2 + 1/2⌋ = ⌊1⌋ = 1.
Hence ⌊x + y⌋ ≠ ⌊x⌋ + ⌊y⌋.

### Theorem 4.5.1: Floor Addition with Integers
For all real numbers x and all integers m, ⌊x + m⌋ = ⌊x⌋ + m.

**Proof:**
Suppose a real number x and an integer m are given. [We must show that ⌊x + m⌋ = ⌊x⌋ + m.] Let n = ⌊x⌋. By definition of floor,
n is an integer and n ≤ x < n + 1.

This double inequality enables you to compute the value of ⌊x + m⌋ in terms of n by adding m to all sides:
n + m ≤ x + m < n + m + 1.
Thus the left-hand side of the equation to be shown is
⌊x + m⌋ = n + m.
On the other hand, since n = ⌊x⌋, the right-hand side of the equation to be shown is
⌊x⌋ + m = n + m
also. Thus ⌊x + m⌋ = ⌊x⌋ + m.

### Theorem 4.5.2: The Floor of n/2
For any integer n,
⌊n/2⌋ = {n/2 if n is even
        {(n−1)/2 if n is odd.

**Proof:**
Suppose n is a [particular but arbitrarily chosen] integer. By the quotient-remainder theorem, either n is odd or n is even.

Case 1 (n is odd): In this case, n = 2k + 1 for some integer k. [We must show that ⌊n/2⌋ = (n − 1)/2.] But the left-hand side of the equation to be shown is
⌊n/2⌋ = ⌊(2k + 1)/2⌋ = ⌊2k/2 + 1/2⌋ = ⌊k + 1/2⌋ = k
because k is an integer and k ≤ k + 1/2 < k + 1. And the right-hand side of the equation to be shown is
(n − 1)/2 = (2k + 1 − 1)/2 = 2k/2 = k
also. So since both the left-hand and right-hand sides equal k, they are equal to each other. That is, ⌊n/2⌋ = (n − 1)/2 [as was to be shown].

Case 2 (n is even): In this case, n = 2k for some integer k. [We must show that ⌊n/2⌋ = n/2.] The rest of the proof of this case is left as an exercise.

### Theorem 4.5.3: Quotient-Remainder with Floor
If n is any integer and d is a positive integer, and if q = ⌊n/d⌋ and r = n − d⌊n/d⌋, then
n = dq + r and 0 ≤ r < d.

**Proof:**
Suppose n is any integer, d is a positive integer, q = ⌊n/d⌋, and r = n − d⌊n/d⌋. [We must show that n = dq + r and 0 ≤ r < d.] By substitution,
dq + r = d⌊n/d⌋ + (n − d⌊n/d⌋) = n.
So it remains only to show that 0 ≤ r < d. But q = ⌊n/d⌋. Thus, by definition of floor,
q ≤ n/d < q + 1.
Then
dq ≤ n < dq + d  by multiplying all parts by d
0 ≤ n − dq < d  by subtracting dq from all parts
and so
But
r = n − d⌊n/d⌋ = n − dq.
Hence
0 ≤ r < d  by substitution.
[This is what was to be shown.]

### Example 4.5.6: Computing div and mod
Use the floor notation to compute 3850 div 17 and 3850 mod 17.

**Solution:**
By formula (4.5.1),
3850 div 17 = ⌊3850/17⌋ = ⌊226.4705882 . . .⌋ = 226
3850 mod 17 = 3850 − 17·⌊3850/17⌋
= 3850 − 17·226
= 3850 − 3842 = 8.

### Key Applications and Properties

1. **div and mod using floor:**
For a nonnegative integer n and a positive integer d,
n div d = ⌊n/d⌋ and n mod d = n − d⌊n/d⌋.

2. **Divisibility condition:**
d divides n if, and only if, n mod d = 0, or, in other words, n = d⌊n/d⌋.

### Test Yourself Questions
1. Given any real number x, the floor of x is the unique integer n such that _____.
2. Given any real number x, the ceiling of x is the unique integer n such that _____.

### Exercise Set 4.5

Compute ⌊x⌋ and ⌈x⌉ for each of the values of x in 1-4.
1. 37.999
2. 17/4
3. −14.00001
4. −32/5

5. Use the floor notation to express 259 div 11 and 259 mod 11.
6. If k is an integer, what is ⌈k⌉? Why?
7. If k is an integer, what is ⌈k + 1/2⌉? Why?
8. Seven pounds of raw material are needed to manufacture each unit of a certain product. Express the number of units that can be produced from n pounds of raw material using either the floor or the ceiling notation. Which notation is more appropriate?
9. Boxes, each capable of holding 36 units, are used to ship a product from the manufacturer to a wholesaler. Express the number of boxes that would be required to ship n units of the product using either the floor or the ceiling notation. Which notation is more appropriate?
10. If 0 = Sunday, 1 = Monday, 2 = Tuesday, . . . , 6 = Saturday, then January 1 of year n occurs on the day of the week given by the following formula:
⌊n + (n−1)/4 − (n−1)/100 + (n−1)/400⌋ mod 7.
a. Use this formula to find January 1 of
i. 2050
ii. 2100
iii. the year of your birth.
b. Interpret the different components of this formula.

11. State a necessary and sufficient condition for the floor of a real number to equal that number.
12. Prove that if n is any even integer, then ⌊n/2⌋ = n/2.
13. Suppose n and d are integers and d ≠ 0. Prove each of the following.
a. If d | n, then n = ⌊n/d⌋ · d.
b. If n = ⌊n/d⌋ · d, then d | n.
c. Use the floor notation to state a necessary and sufficient condition for an integer n to be divisible by an integer d.

Some of the statements in 14-22 are true and some are false. Prove each true statement and find a counterexample for each false statement, but do not use Theorem 4.5.1 in your proofs.
14. For all real numbers x and y, ⌊x − y⌋ = ⌊x⌋ − ⌊y⌋.
15. For all real numbers x, ⌊x − 1⌋ = ⌊x⌋ − 1.
16. For all real numbers x, ⌊x²⌋ = ⌊x⌋².
17. For all integers n,
⌊n/3⌋ = {n/3 if n mod 3 = 0
        {(n−1)/3 if n mod 3 = 1
        {(n−2)/3 if n mod 3 = 2
18. For all real numbers x and y, ⌈x + y⌉ = ⌈x⌉ + ⌈y⌉.
19. For all real numbers x, ⌈x − 1⌉ = ⌈x⌉ − 1.
20. For all real numbers x and y, ⌈xy⌉ = ⌈x⌉ · ⌈y⌉.
21. For all odd integers n, ⌈n/2⌉ = (n + 1)/2.
22. For all real numbers x and y, ⌈xy⌉ = ⌈x⌉ · ⌊y⌋.

Prove each of the statements in 23-29.
23. For any real number x, if x is not an integer, then ⌊x⌋ + ⌊−x⌋ = −1.
24. For any integer m and any real number x, if x is not an integer, then ⌊x⌋ + ⌊m − x⌋ = m − 1.
25. For all real numbers x, ⌊⌊x/2⌋/2⌋ = ⌊x/4⌋.
26. For all real numbers x, if x − ⌊x⌋ < 1/2 then ⌊2x⌋ = 2⌊x⌋.
27. For all real numbers x, if x − ⌊x⌋ ≥ 1/2 then ⌊2x⌋ = 2⌊x⌋ + 1.
28. For any odd integer n,
⌊n²/4⌋ = (n−1)(n+1)/4.
29. For any odd integer n,
⌈n²/4⌉ = (n² + 3)/4.

30. Find the mistake in the following "proof" that ⌊n/2⌋ = (n − 1)/2 if n is an odd integer.
"Proof: Suppose n is any odd integer. Then n = 2k + 1 for some integer k. Consequently,
⌊n/2⌋ = ⌊(2k + 1)/2⌋ = ⌊2k/2⌋ = ⌊k⌋ = k.
But n = 2k + 1. Solving for k gives k = (n − 1)/2.
Hence, by substitution, ⌊n/2⌋ = (n − 1)/2."

### Answers for Test Yourself
1. n ≤ x < n + 1 2. n − 1 < x ≤ n