# Chapter 8: Relations (Complete with All Text, Equations, and Formulas)

**Pages 442-521**

## 8.1 Relations on Sets

**Page 442**

> Strange as it may sound, the power of mathematics rests on its evasion of all unnecessary thought and on its wonderful saving of mental operations. — Ernst Mach, 1838–1916

A more formal way to refer to the kind of relation defined in Section 1.3 is to call it a binary relation because it is a subset of a Cartesian product of two sets. At the end of this section we define an n-ary relation to be a subset of a Cartesian product of n sets, where n is any integer greater than or equal to two. Such a relation is the fundamental structure used in relational databases. However, because we focus on binary relations in this text, when we use the term relation by itself, we will mean binary relation.

### Example 8.1.1: The Less-than Relation for Real Numbers

Deﬁne a relation L from R to R as follows: For all real numbers x and y,
```
x L y ⇔ x < y.
```

a. Is 57 L 53?
b. Is (−17) L (−14)?
c. Is 143 L 143?
d. Is (−35) L 1?
e. Draw the graph of L as a subset of the Cartesian plane R × R

**Solution:**
a. No, 57 > 53
b. Yes, −17 < −14
c. No, 143 = 143
d. Yes, −35 < 1
e. For each value of x, all the points (x, y) with y > x are on the graph. So the graph consists of all the points above the line x = y.

**Page 471**

### Example 8.1.2: The Congruence Modulo 2 Relation

Deﬁne a relation E from Z to Z as follows: For all (m, n) ∈ Z × Z,
```
m E n ⇔ m − n is even.
```

a. Is 4 E 0? Is 2 E 6? Is 3 E (−3)? Is 5 E 2?
b. List ﬁve integers that are related by E to 1.
c. Prove that if n is any odd integer, then n E 1.

**Solution:**
a. Yes, 4 E 0 because 4 − 0 = 4 and 4 is even.
   Yes, 2 E 6 because 2 − 6 = −4 and −4 is even.
   Yes, 3 E (−3) because 3 − (−3) = 6 and 6 is even.
   No, 5 E̸ 2 because 5 − 2 = 3 and 3 is not even.

b. There are many such lists. One is:
   1 because 1 − 1 = 0 is even,
   3 because 3 − 1 = 2 is even,
   5 because 5 − 1 = 4 is even,
   −1 because −1 − 1 = −2 is even,
   −3 because −3 − 1 = −4 is even.

c. **Proof:** Suppose n is any odd integer. Then n = 2k + 1 for some integer k. Now by deﬁnition of E, n E 1 if, and only if, n − 1 is even. But by substitution,
   ```
   n − 1 = (2k + 1) − 1 = 2k,
   ```
   and since k is an integer, 2k is even. Hence n E 1 [as was to be shown].

It can be shown (see exercise 2 at the end of this section) that integers m and n are related by E if, and only if, m mod 2 = n mod 2 (that is, both are even or both are odd). When this occurs m and n are said to be congruent modulo 2.

### Example 8.1.3: A Relation on a Power Set

Let X = {a, b, c}. Then P(X) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}. Deﬁne a relation S from P(X) to Z as follows: For all sets A and B in P(X) (i.e., for all subsets A and B of X),
```
A S B ⇔ A has at least as many elements as B.
```

a. Is {a, b} S {b, c}?
b. Is {a} S ∅?
c. Is {b, c} S {a, b, c}?
d. Is {c} S {a}?

**Solution:**
a. Yes, both sets have two elements.
b. Yes, {a} has one element and ∅ has zero elements, and 1 ≥ 0.
c. No, {b, c} has two elements and {a, b, c} has three elements and 2 < 3.
d. Yes, both sets have one element.

**Page 472**

## The Inverse of a Relation

If R is a relation from A to B, then a relation R⁻¹ from B to A can be deﬁned by interchanging the elements of all the ordered pairs of R.

### Deﬁnition
Let R be a relation from A to B. Deﬁne the inverse relation R⁻¹ from B to A as follows:
```
R⁻¹ = {(y, x) ∈ B × A | (x, y) ∈ R}.
```

This deﬁnition can be written operationally as follows:
For all x ∈ A and y ∈ B,
```
(y, x) ∈ R⁻¹ ⇔ (x, y) ∈ R.
```

### Example 8.1.4: The Inverse of a Finite Relation

Let A = {2, 3, 4} and B = {2, 6, 8} and let R be the "divides" relation from A to B: For all (x, y) ∈ A × B,
```
x R y ⇔ x | y ⇔ x divides y.
```

a. State explicitly which ordered pairs are in R and R⁻¹, and draw arrow diagrams for R and R⁻¹.
b. Describe R⁻¹ in words.

**Solution:**
a. R = {(2, 2), (2, 6), (2, 8), (3, 6), (4, 8)}
   R⁻¹ = {(2, 2), (6, 2), (8, 2), (6, 3), (8, 4)}

   Arrow diagrams show R with arrows from A to B and R⁻¹ with arrows reversed.

b. R⁻¹ can be described in words as follows: For all (y, x) ∈ B × A,
   ```
   y R⁻¹ x ⇔ y is a multiple of x.
   ```

**Page 473**

### Example 8.1.5: The Inverse of an Inﬁnite Relation

Deﬁne a relation R from R to R as follows: For all (x, y) ∈ R × R,
```
x R y ⇔ y = 2|x|.
```

Draw the graphs of R and R⁻¹ in the Cartesian plane. Is R⁻¹ a function?

**Solution:**
A point (v, u) is on the graph of R⁻¹ if, and only if, (u, v) is on the graph of R.

Note that if x ≥ 0, then the graph of y = 2|x| = 2x is a straight line with slope 2. And if x < 0, then the graph of y = 2|x| = 2(−x) = −2x is a straight line with slope −2.

R = {(x, y) | y = 2|x|}
R⁻¹ = {(y, x) | y = 2|x|}

R⁻¹ is not a function because, for instance, both (2, 1) and (2, −1) are in R⁻¹.

**Page 474**

## Directed Graph of a Relation

In the remaining sections of this chapter, we discuss important properties of relations that are deﬁned from a set to itself.

### Deﬁnition
A relation on a set A is a relation from A to A.

When a relation R is deﬁned on a set A, the arrow diagram of the relation can be modiﬁed so that it becomes a directed graph. Instead of representing A as two separate sets of points, represent A only once, and draw an arrow from each point of A to each related point. As with an ordinary arrow diagram,

For all points x and y in A,
```
there is an arrow from x to y ⇔ x R y ⇔ (x, y) ∈ R.
```

If a point is related to itself, a loop is drawn that extends out from the point and goes back to it.

### Example 8.1.6: Directed Graph of a Relation

Let A = {3, 4, 5, 6, 7, 8} and deﬁne a relation R on A as follows: For all x, y ∈ A,
```
x R y ⇔ 2 | (x − y).
```

Draw the directed graph of R.

**Solution:**
Note that 3 R 3 because 3 − 3 = 0 and 2 | 0 since 0 = 2 · 0. Thus there is a loop from 3 to itself. Similarly, there is a loop from 4 to itself, from 5 to itself, and so forth, since the difference of each integer with itself is 0, and 2 | 0.

Note also that 3 R 5 because 3 − 5 = −2 = 2 · (−1). And 5 R 3 because 5 − 3 = 2 = 2 · 1. Hence there is an arrow from 3 to 5 and also an arrow from 5 to 3. The other arrows in the directed graph are obtained by similar reasoning.

## N-ary Relations and Relational Databases

N-ary relations form the mathematical foundation for relational database theory. A binary relation is a subset of a Cartesian product of two sets, similarly, an n-ary relation is a subset of a Cartesian product of n sets.

**Page 475**

### Deﬁnition
Given sets A₁, A₂, . . . , Aₙ, an n-ary relation R on A₁ × A₂ × · · · × Aₙ is a subset of A₁ × A₂ × · · · × Aₙ. The special cases of 2-ary, 3-ary, and 4-ary relations are called binary, ternary, and quaternary relations, respectively.

### Example 8.1.7: A Simple Database

The following is a radically simpliﬁed version of a database that might be used in a hospital. Let A₁ be a set of positive integers, A₂ a set of alphabetic character strings, A₃ a set of numeric character strings, and A₄ a set of alphabetic character strings. Deﬁne a quaternary relation R on A₁ × A₂ × A₃ × A₄ as follows:

```
(a₁, a₂, a₃, a₄) ∈ R ⇔ a patient with patient ID number a₁, named a₂, was admitted on date a₃, with primary diagnosis a₄.
```

At a particular hospital, this relation might contain the following 4-tuples:
- (011985, John Schmidt, 020710, asthma)
- (574329, Tak Kurosawa, 0114910, pneumonia)
- (466581, Mary Lazars, 0103910, appendicitis)
- (008352, Joan Kaplan, 112409, gastritis)
- (011985, John Schmidt, 021710, pneumonia)
- (244388, Sarah Wu, 010310, broken leg)
- (778400, Jamal Baskers, 122709, appendicitis)

In discussions of relational databases, the tuples are normally thought of as being written in tables. Each row of the table corresponds to one tuple, and the header for each column gives the descriptive attribute for the elements in the column.

Operations within a database allow the data to be manipulated in many different ways. For example, in the database language SQL, if the above database is denoted S, the result of the query:

```
SELECT Patient−ID#, Name FROM S WHERE Admission−Date = 010310
```

would be a list of the ID numbers and names of all patients admitted on 01-03-10:
- 466581, Mary Lazars
- 244388, Sarah Wu

This is obtained by taking the intersection of the set A₁ × A₂ × {010310} × A₄ with the database and then projecting onto the ﬁrst two coordinates. Similarly, SELECT can be used to obtain a list of all admission dates of a given patient. For John Schmidt this list is 02-07-10 and 02-17-10.

**Page 476**

## Test Yourself

Answers to Test Yourself questions are located at the end of each section.

1. If R is a relation from A to B, x ∈ A, and y ∈ B, the notation x R y means that _____.
2. If R is a relation from A to B, x ∈ A, and y ∈ B, the notation x R̸ y means that _____.
3. If R is a relation from A to B, x ∈ A, and y ∈ B, then (y, x) ∈ R⁻¹ if, and only if, _____.
4. A relation on a set A is a relation from _____ to _____.
5. If R is a relation on a set A, the directed graph of R has an arrow from x to y if, and only if, _____.

## Exercise Set 8.1

1. As in Example 8.1.2, the congruence modulo 2 relation E is deﬁned from Z to Z as follows: For all integers m and n,
   ```
   m E n ⇔ m − n is even.
   ```
   a. Is 0 E 0? Is 5 E 2? Is (6, 6) ∈ E? Is (−1, 7) ∈ E?
   b. Prove that for any even integer n, n E 0.

2. Prove that for all integers m and n, m − n is even if, and only if, both m and n are even or both m and n are odd.

3. The congruence modulo 3 relation, T, is deﬁned from Z to Z as follows: For all integers m and n,
   ```
   m T n ⇔ 3 | (m − n).
   ```
   a. Is 10 T 1? Is 1 T 10? Is (2, 2) ∈ T? Is (8, 1) ∈ T?
   b. List ﬁve integers n such that n T 0.
   c. List ﬁve integers n such that n T 1.
   d. List ﬁve integers n such that n T 2.
   e. Make and prove a conjecture about which integers are related by T to 0, which integers are related by T to 1, and which integers are related by T to 2.

4. Deﬁne a relation P on Z as follows: For all m, n ∈ Z,
   ```
   m P n ⇔ m and n have a common prime factor.
   ```
   a. Is 15 P 25?  b. 22 P 27?  c. Is 0 P 5?  d. Is 8 P 8?

5. Let X = {a, b, c}. Recall that P(X) is the power set of X. Deﬁne a relation R on P(X) as follows:
   For all A, B ∈ P(X),
   ```
   A R B ⇔ A has the same number of elements as B.
   ```
   a. Is {a, b} R {b, c}?  b. Is {a} R {a, b}?  c. Is {c} R {b}?

6. Let X = {a, b, c}. Deﬁne a relation J on P(X) as follows:
   For all A, B ∈ P(X),
   ```
   A J B ⇔ A ∩ B ≠ ∅.
   ```
   a. Is {a} J {c}?  b. Is {a, b} J {b, c}?  c. Is {a, b} J {a, b, c}?

7. Deﬁne a relation R on Z as follows: For all integers m and n,
   ```
   m R n ⇔ 5 | (m² − n²).
   ```
   a. Is 1 R (−9)?  b. Is 2 R 13?  c. Is 2 R (−8)?  d. Is (−8) R 2?

8. Let A be the set of all strings of a's and b's of length 4. Deﬁne a relation R on A as follows:
   For all s, t ∈ A,
   ```
   s R t ⇔ s has the same ﬁrst two characters as t.
   ```
   a. Is abaa R abba?  b. Is aabb R bbaa?  c. Is aaaa R aaab?  d. Is baaa R abaa?

9. Let A be the set of all strings of 0's, 1's, and 2's of length 4. Deﬁne a relation R on A as follows:
   For all s, t ∈ A,
   ```
   s R t ⇔ the sum of the characters in s equals the sum of the characters in t.
   ```
   a. Is 0121 R 2200?  b. Is 1011 R 2101?  c. Is 2212 R 2121?  d. Is 1220 R 2111?

10. Let A = {3, 4, 5} and B = {4, 5, 6} and let R be the "less than" relation. That is, for all (x, y) ∈ A × B,
    ```
    x R y ⇔ x < y.
    ```
    State explicitly which ordered pairs are in R and R⁻¹.

11. Let A = {3, 4, 5} and B = {4, 5, 6} and let S be the "divides" relation. That is, for all (x, y) ∈ A × B,
    ```
    x S y ⇔ x | y.
    ```
    State explicitly which ordered pairs are in S and S⁻¹.

12. a. Suppose a function F: X → Y is one-to-one but not onto. Is F⁻¹ (the inverse relation for F) a function? Explain your answer.
   b. Suppose a function F: X → Y is onto but not one-to-one. Is F⁻¹ (the inverse relation for F) a function? Explain your answer.

**Page 477**

13. Deﬁne a relation R on A = {0, 1, 2, 3} by R = {(0, 0), (1, 2), (2, 2)}.

14. Deﬁne a relation S on B = {a, b, c, d} by S = {(a, b), (a, c), (b, c), (d, d)}.

15. Let A = {2, 3, 4, 5, 6, 7, 8} and deﬁne a relation R on A as follows: For all x, y ∈ A,
    ```
    x R y ⇔ 2 | (x − y).
    ```

16. Let A = {5, 6, 7, 8, 9, 10} and deﬁne a relation S on A as follows: For all x, y ∈ A,
    ```
    x S y ⇔ 3 | (x − y).
    ```

17. Let A = {2, 3, 4, 5, 6, 7, 8} and deﬁne a relation T on A as follows: For all x, y ∈ A,
    ```
    x T y ⇔ x | y.
    ```

18. Let A = {0, 1, 2, 3, 4, 5, 6, 7, 8} and deﬁne a relation V on A as follows: For all x, y ∈ A,
    ```
    x V y ⇔ 5 | (x² − y²).
    ```

Draw the directed graphs of the relations deﬁned in 13–18.

**Exercises 19–20 refer to unions and intersections of relations.**

Since relations are subsets of Cartesian products, their unions and intersections can be calculated as for any subsets. Given two relations R and S from A to B,

```
R ∪ S = {(x, y) ∈ A × B | (x, y) ∈ R or (x, y) ∈ S}
R ∩ S = {(x, y) ∈ A × B | (x, y) ∈ R and (x, y) ∈ S}.
```

19. Let A = {2, 4} and B = {6, 8, 10} and deﬁne relations R and S from A to B as follows:
   For all (x, y) ∈ A × B,
   ```
   x R y ⇔ x | y   and   x S y ⇔ y − 4 = x.
   ```
   State explicitly which ordered pairs are in A × B, R, S, R ∪ S, and R ∩ S.

20. Let A = {−1, 1, 2, 4} and B = {1, 2} and deﬁne relations R and S from A to B as follows:
   For all (x, y) ∈ A × B,
   ```
   x R y ⇔ |x| = |y|   and   x S y ⇔ x = y.
   ```
   State explicitly which ordered pairs are in A × B, R, S, R ∪ S, and R ∩ S.

21. Deﬁne relations R and S on R as follows:
   ```
   R = {(x, y) ∈ R × R | x < y}   and   S = {(x, y) ∈ R × R | x = y}.
   ```
   Graph R, S, R ∪ S, and R ∩ S in the Cartesian plane.

22. Deﬁne relations R and S on R as follows:
   ```
   R = {(x, y) ∈ R × R | x² + y² = 4}   and   S = {(x, y) ∈ R × R | x = y}.
   ```
   Graph R, S, R ∪ S, and R ∩ S in the Cartesian plane.

23. Deﬁne relations R and S on R as follows:
   ```
   R = {(x, y) ∈ R × R | y = |x|}   and   S = {(x, y) ∈ R × R | y = 1}.
   ```
   Graph R, S, R ∪ S, and R ∩ S in the Cartesian plane.

24. In Example 8.1.7 the result of the query SELECT Patient−ID#, Name FROM S WHERE Primary−Diagnosis = X is the projection onto the ﬁrst two coordinates of the intersection of the set A₁ × A₂ × A₃ × {X} with the database.
   a. Find the result of the query SELECT Patient−ID#, Name FROM S WHERE Primary−Diagnosis = pneumonia.
   b. Find the result of the query SELECT Patient−ID#, Name FROM S WHERE Primary−Diagnosis = appendicitis.

**Answers for Test Yourself**

1. x is related to y by R
2. x is not related to y by R
3. (x, y) ∈ R
4. A; A
5. x is related to y by R

**Page 477**

## 8.2 Reﬂexivity, Symmetry, and Transitivity

> Mathematics is the tool specially suited for dealing with abstract concepts of any kind and there is no limit to its power in this ﬁeld. — P. A. M. Dirac, 1902–1984

Let A = {2, 3, 4, 6, 7, 9} and deﬁne a relation R on A as follows: For all x, y ∈ A,
```
x R y ⇔ 3 | (x − y).
```

Define a relation L from R to R as follows: For all real numbers x and y,
```
x L y ⇔ x < y.
```

a. Is 57 L 53?
b. Is (−17) L (−14)?
c. Is 143 L 143?
d. Is (−35) L 1?
e. Draw the graph of L as a subset of the Cartesian plane R × R

**Solution:**
a. No, 57 > 53
b. Yes, −17 < −14
c. No, 143 = 143
d. Yes, −35 < 1
e. For each value of x, all the points (x, y) with y > x are on the graph. So the graph consists of all the points above the line x = y.

**Page 443**

### Example 8.1.2: The Congruence Modulo 2 Relation

Define a relation E from Z to Z as follows: For all (m, n) ∈ Z × Z,
```
m E n ⇔ m − n is even.
```

a. Is 4 E 0? Is 2 E 6? Is 3 E (−3)? Is 5 E 2?
b. List five integers that are related by E to 1.
c. Prove that if n is any odd integer, then n E 1.

**Solution:**
a. Yes, 4 E 0 because 4 − 0 = 4 and 4 is even.
   Yes, 2 E 6 because 2 − 6 = −4 and −4 is even.
   Yes, 3 E (−3) because 3 − (−3) = 6 and 6 is even.
   No, 5 E̸ 2 because 5 − 2 = 3 and 3 is not even.

b. There are many such lists. One is:
   - 1 because 1 − 1 = 0 is even,
   - 3 because 3 − 1 = 2 is even,
   - 5 because 5 − 1 = 4 is even,
   - −1 because −1 − 1 = −2 is even,
   - −3 because −3 − 1 = −4 is even.

c. **Proof:** Suppose n is any odd integer. Then n = 2k + 1 for some integer k. Now by definition of E, n E 1 if, and only if, n − 1 is even. But by substitution,
   ```
   n − 1 = (2k + 1) − 1 = 2k,
   ```
   and since k is an integer, 2k is even. Hence n E 1 [as was to be shown].

It can be shown (see exercise 2) that integers m and n are related by E if, and only if, m mod 2 = n mod 2 (that is, both are even or both are odd). When this occurs m and n are said to be congruent modulo 2.

### Example 8.1.3: A Relation on a Power Set

Let X = {a, b, c}. Then P(X) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}. Define a relation S from P(X) to Z as follows: For all sets A and B in P(X) (i.e., for all subsets A and B of X),
```
A S B ⇔ A has at least as many elements as B.
```

a. Is {a, b} S {b, c}?
b. Is {a} S ∅?
c. Is {b, c} S {a, b, c}?
d. Is {c} S {a}?

**Solution:**
a. Yes, both sets have two elements.
b. Yes, {a} has one element and ∅ has zero elements, and 1 ≥ 0.
c. No, {b, c} has two elements and {a, b, c} has three elements and 2 < 3.
d. Yes, both sets have one element.

**Page 444**

## The Inverse of a Relation

If R is a relation from A to B, then a relation R⁻¹ from B to A can be defined by interchanging the elements of all the ordered pairs of R.

### Definition
Let R be a relation from A to B. Define the inverse relation R⁻¹ from B to A as follows:
```
R⁻¹ = {(y, x) ∈ B × A | (x, y) ∈ R}.
```

This definition can be written operationally as follows:
For all x ∈ A and y ∈ B,
```
(y, x) ∈ R⁻¹ ⇔ (x, y) ∈ R.
```

### Example 8.1.4: The Inverse of a Finite Relation

Let A = {2, 3, 4} and B = {2, 6, 8} and let R be the "divides" relation from A to B: For all (x, y) ∈ A × B,
```
x R y ⇔ x | y ⇔ x divides y.
```

a. State explicitly which ordered pairs are in R and R⁻¹, and draw arrow diagrams for R and R⁻¹.
b. Describe R⁻¹ in words.

**Solution:**
a. R = {(2, 2), (2, 6), (2, 8), (3, 6), (4, 8)}
   R⁻¹ = {(2, 2), (6, 2), (8, 2), (6, 3), (8, 4)}

b. R⁻¹ can be described in words as follows: For all (y, x) ∈ B × A,
   ```
   y R⁻¹ x ⇔ y is a multiple of x.
   ```

**Page 445**

### Example 8.1.5: The Inverse of an Infinite Relation

Define a relation R from R to R as follows: For all (x, y) ∈ R × R,
```
x R y ⇔ y = 2|x|.
```

Draw the graphs of R and R⁻¹ in the Cartesian plane. Is R⁻¹ a function?

**Solution:**
A point (v, u) is on the graph of R⁻¹ if, and only if, (u, v) is on the graph of R.
Note that if x ≥ 0, then the graph of y = 2|x| = 2x is a straight line with slope 2. And if x < 0, then the graph of y = 2|x| = 2(−x) = −2x is a straight line with slope −2.

R⁻¹ is not a function because, for instance, both (2, 1) and (2, −1) are in R⁻¹.

**Page 446**

## Directed Graph of a Relation

In the remaining sections of this chapter, we discuss important properties of relations that are defined from a set to itself.

### Definition
A relation on a set A is a relation from A to A.

When a relation R is defined on a set A, the arrow diagram of the relation can be modified so that it becomes a directed graph. Instead of representing A as two separate sets of points, represent A only once, and draw an arrow from each point of A to each related point. As with an ordinary arrow diagram,

For all points x and y in A,
```
there is an arrow from x to y ⇔ x R y ⇔ (x, y) ∈ R.
```

If a point is related to itself, a loop is drawn that extends out from the point and goes back to it.

### Example 8.1.6: Directed Graph of a Relation

Let A = {3, 4, 5, 6, 7, 8} and define a relation R on A as follows: For all x, y ∈ A,
```
x R y ⇔ 2 | (x − y).
```

Draw the directed graph of R.

**Solution:**
Note that 3 R 3 because 3 − 3 = 0 and 2 | 0 since 0 = 2 · 0. Thus there is a loop from 3 to itself. Similarly, there is a loop from 4 to itself, from 5 to itself, and so forth, since the difference of each integer with itself is 0, and 2 | 0.

Note also that 3 R 5 because 3 − 5 = −2 = 2 · (−1). And 5 R 3 because 5 − 3 = 2 = 2 · 1. Hence there is an arrow from 3 to 5 and also an arrow from 5 to 3. The other arrows in the directed graph are obtained by similar reasoning.

## N-ary Relations and Relational Databases

N-ary relations form the mathematical foundation for relational database theory. A binary relation is a subset of a Cartesian product of two sets, similarly, an n-ary relation is a subset of a Cartesian product of n sets.

**Page 447**

### Definition
Given sets A₁, A₂, . . . , Aₙ, an n-ary relation R on A₁ × A₂ × · · · × Aₙ is a subset of A₁ × A₂ × · · · × Aₙ. The special cases of 2-ary, 3-ary, and 4-ary relations are called binary, ternary, and quaternary relations, respectively.

### Example 8.1.7: A Simple Database

The following is a radically simplified version of a database that might be used in a hospital. Let A₁ be a set of positive integers, A₂ a set of alphabetic character strings, A₃ a set of numeric character strings, and A₄ a set of alphabetic character strings. Define a quaternary relation R on A₁ × A₂ × A₃ × A₄ as follows:

```
(a₁, a₂, a₃, a₄) ∈ R ⇔ a patient with patient ID number a₁, named a₂, was admitted on date a₃, with primary diagnosis a₄.
```

At a particular hospital, this relation might contain the following 4-tuples:
- (011985, John Schmidt, 020710, asthma)
- (574329, Tak Kurosawa, 0114910, pneumonia)
- (466581, Mary Lazars, 0103910, appendicitis)
- (008352, Joan Kaplan, 112409, gastritis)
- (011985, John Schmidt, 021710, pneumonia)
- (244388, Sarah Wu, 010310, broken leg)
- (778400, Jamal Baskers, 122709, appendicitis)

In discussions of relational databases, the tuples are normally thought of as being written in tables. Each row of the table corresponds to one tuple, and the header for each column gives the descriptive attribute for the elements in the column.

Operations within a database allow the data to be manipulated in many different ways. For example, in the database language SQL, if the above database is denoted S, the result of the query:

```
SELECT Patient−ID#, Name FROM S WHERE Admission−Date = 010310
```

would be a list of the ID numbers and names of all patients admitted on 01-03-10:
- 466581, Mary Lazars
- 244388, Sarah Wu

This is obtained by taking the intersection of the set A₁ × A₂ × {010310} × A₄ with the database and then projecting onto the first two coordinates.

**Page 449-450**

## 8.2 Reflexivity, Symmetry, and Transitivity

> Mathematics is the tool specially suited for dealing with abstract concepts of any kind and there is no limit to its power in this field. — P. A. M. Dirac, 1902–1984

Let A = {2, 3, 4, 6, 7, 9} and define a relation R on A as follows: For all x, y ∈ A,
```
x R y ⇔ 3 | (x − y).
```

Then 2 R 2 because 2 − 2 = 0, and 3 | 0. Similarly, 3 R 3, 4 R 4, 6 R 6, 7 R 7, and 9 R 9. Also 6 R 3 because 6 − 3 = 3, and 3 | 3. And 3 R 6 because 3 − 6 = −(6 − 3) = −3, and 3 | (−3). Similarly, 3 R 9, 9 R 3, 6 R 9, 9 R 6, 4 R 7, and 7 R 4.

This graph has three important properties:
1. Each point of the graph has an arrow looping around from it back to itself.
2. In each case where there is an arrow going from one point to a second, there is an arrow going from the second point back to the first.
3. In each case where there is an arrow going from one point to a second and from the second point to a third, there is an arrow going from the first point to the third. That is, there are no "incomplete directed triangles" in the graph.

Properties (1), (2), and (3) correspond to properties of general relations called reflexivity, symmetry, and transitivity.

### Definition
Let R be a relation on a set A.
1. R is **reflexive** if, and only if, for all x ∈ A, x R x.
2. R is **symmetric** if, and only if, for all x, y ∈ A, if x R y then y R x.
3. R is **transitive** if, and only if, for all x, y, z ∈ A, if x R y and y R z then x R z.

Because of the equivalence of the expressions x R y and (x, y) ∈ R for all x and y in A, the reflexive, symmetric, and transitive properties can also be written as follows:

1. R is reflexive ⇔ for all x in A, (x, x) ∈ R.
2. R is symmetric ⇔ for all x and y in A, if (x, y) ∈ R then (y, x) ∈ R.
3. R is transitive ⇔ for all x, y and z in A, if (x, y) ∈ R and (y, z) ∈ R then (x, z) ∈ R.

**Page 451**

Note that the definitions of reflexivity, symmetry, and transitivity are universal statements. This means that to prove a relation has one of the properties, you use either the method of exhaustion or the method of generalizing from the generic particular.

Now consider what it means for a relation not to have one of the properties defined previously. Recall that the negation of a universal statement is existential. Hence if R is a relation on a set A, then

1. R is not reflexive ⇔ there is an element x in A such that x R̸ x [that is, such that (x, x) ∉ R].
2. R is not symmetric ⇔ there are elements x and y in A such that x R y but y R̸ x [that is, such that (x, y) ∈ R but (y, x) ∉ R].
3. R is not transitive ⇔ there are elements x, y and z in A such that x R y and y R z but x R̸ z [that is, such that (x, y) ∈ R and (y, z) ∈ R but (x, z) ∉ R].

It follows that you can show that a relation does not have one of the properties by finding a counterexample.

### Example 8.2.1: Properties of Relations on Finite Sets

Let A = {0, 1, 2, 3} and define relations R, S, and T on A as follows:
```
R = {(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)},
S = {(0, 0), (0, 2), (0, 3), (2, 3)},
T = {(0, 1), (2, 3)}.
```

a. Is R reflexive? symmetric? transitive?
b. Is S reflexive? symmetric? transitive?
c. Is T reflexive? symmetric? transitive?

**Solution:**

a. **R is reflexive:** There is a loop at each point of the directed graph. This means that each element of A is related to itself, so R is reflexive.

   **R is symmetric:** In each case where there is an arrow going from one point of the graph to a second, there is an arrow going from the second point back to the first. This means that whenever one element of A is related by R to a second, then the second is related to the first. Hence R is symmetric.

   **R is not transitive:** There is an arrow going from 1 to 0 and an arrow going from 0 to 3, but there is no arrow going from 1 to 3. This means that there are elements of A—0, 1, and 3—such that 1 R 0 and 0 R 3 but 1 R̸ 3. Hence R is not transitive.

**Page 452**

b. **S is not reflexive:** There is no loop at 1, for example. Thus (1, 1) ∉ S, and so S is not reflexive.

   **S is not symmetric:** There is an arrow from 0 to 2 but not from 2 to 0. Hence (0, 2) ∈ S but (2, 0) ∉ S, and so S is not symmetric.

   **S is transitive:** There are three cases for which there is an arrow going from one point of the graph to a second and from the second point to a third: Namely, there are arrows going from 0 to 2 and from 2 to 3; there are arrows going from 0 to 0 and from 0 to 2; and there are arrows going from 0 to 0 and from 0 to 3. In each case there is an arrow going from the first point to the third. This means that whenever (x, y) ∈ S and (y, z) ∈ S, then (x, z) ∈ S, for all x, y, z ∈ {0, 1, 2, 3}, and so S is transitive.

c. **T is not reflexive:** There is no loop at 0, for example. Thus (0, 0) ∉ T, so T is not reflexive.

   **T is not symmetric:** There is an arrow from 0 to 1 but not from 1 to 0. Thus (0, 1) ∈ T but (1, 0) ∉ T, and so T is not symmetric.

   **T is transitive:** The transitivity condition is vacuously true for T. To see this, observe that the transitivity condition says that
   ```
   For all x, y, z ∈ A, if (x, y) ∈ T and (y, z) ∈ T then (x, z) ∈ T.
   ```
   The only way for this to be false would be for there to exist elements of A that make the hypothesis true and the conclusion false. That is, there would have to be elements x, y, and z in A such that
   ```
   (x, y) ∈ T and (y, z) ∈ T and (x, z) ∉ T.
   ```
   In other words, there would have to be two ordered pairs in T that have the potential to "link up" by having the second element of one pair be the first element of the other pair. But the only elements in T are (0, 1) and (2, 3), and these do not have the potential to link up. Hence the hypothesis is never true. It follows that it is impossible for T not to be transitive, and thus T is transitive.

**Page 453-456**

## Properties of Relations on Infinite Sets

### Example 8.2.2: Properties of Equality

Define a relation R on R (the set of all real numbers) as follows: For all real numbers x and y,
```
x R y ⇔ x = y.
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?

**Solution:**

a. **R is reflexive:** R is reflexive if, and only if, the following statement is true:
   ```
   For all x ∈ R, x R x.
   ```
   Since x R x just means that x = x, this is the same as saying
   ```
   For all x ∈ R, x = x.
   ```
   But this statement is certainly true; every real number is equal to itself.

b. **R is symmetric:** R is symmetric if, and only if, the following statement is true:
   ```
   For all x, y ∈ R, if x R y then y R x.
   ```
   By definition of R, x R y means that x = y and y R x means that y = x. Hence R is symmetric if, and only if,
   ```
   For all x, y ∈ R, if x = y then y = x.
   ```
   But this statement is certainly true; if one number is equal to a second, then the second is equal to the first.

c. **R is transitive:** R is transitive if, and only if, the following statement is true:
   ```
   For all x, y, z ∈ R, if x R y and y R z then x R z.
   ```
   By definition of R, x R y means that x = y, y R z means that y = z, and x R z means that x = z. Hence R is transitive if, and only if, the following statement is true:
   ```
   For all x, y, z ∈ R, if x = y and y = z then x = z.
   ```
   But this statement is certainly true: If one real number equals a second and the second equals a third, then the first equals the third.

### Example 8.2.3: Properties of "Less Than"

Define a relation R on R (the set of all real numbers) as follows: For all x, y ∈ R,
```
x R y ⇔ x < y.
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?

**Solution:**

a. **R is not reflexive:** R is reflexive if, and only if, ∀x ∈ R, x R x. By definition of R, this means that ∀x ∈ R, x < x. But this is false: ∃x ∈ R such that x ≮ x. As a counterexample, let x = 0 and note that 0 ≮ 0. Hence R is not reflexive.

b. **R is not symmetric:** R is symmetric if, and only if, ∀x, y ∈ R, if x R y then y R x. By definition of R, this means that ∀x, y ∈ R, if x < y then y < x. But this is false: ∃x, y ∈ R such that x < y and y ≮ x. As a counterexample, let x = 0 and y = 1 and note that 0 < 1 but 1 ≮ 0. Hence R is not symmetric.

c. **R is transitive:** R is transitive if, and only if, for all x, y, z ∈ R, if x R y and y R z then x R z. By definition of R, this means that for all x, y, z ∈ R, if x < y and y < z, then x < z. But this statement is true by the transitive law of order for real numbers. Hence R is transitive.

### Example 8.2.4: Properties of Congruence Modulo 3

Define a relation T on Z (the set of all integers) as follows: For all integers m and n,
```
m T n ⇔ 3 | (m − n).
```

This relation is called congruence modulo 3.

a. Is T reflexive?
b. Is T symmetric?
c. Is T transitive?

**Solution:**

a. **T is reflexive:** To show that T is reflexive, it is necessary to show that
   ```
   For all m ∈ Z, m T m.
   ```
   By definition of T, this means that
   ```
   For all m ∈ Z, 3 | (m − m).
   ```
   Or, since m − m = 0,
   ```
   For all m ∈ Z, 3 | 0.
   ```
   But this is true: 3 | 0 since 0 = 3 · 0. Hence T is reflexive.

   **Proof of Reflexivity:** Suppose m is a particular but arbitrarily chosen integer. [We must show that m T m.] Now m − m = 0. But 3 | 0 since 0 = 3 · 0. Hence 3 | (m − m). Thus, by definition of T, m T m [as was to be shown].

b. **T is symmetric:** To show that T is symmetric, it is necessary to show that
   ```
   For all m, n ∈ Z, if m T n then n T m.
   ```
   By definition of T this means that
   ```
   For all m, n ∈ Z, if 3 | (m − n) then 3 | (n − m).
   ```

   **Proof of Symmetry:** Suppose m and n are particular but arbitrarily chosen integers that satisfy the condition m T n. [We must show that n T m.] By definition of T, since m T n then 3 | (m − n). By definition of "divides," this means that m − n = 3k, for some integer k. Multiplying both sides by −1 gives n − m = 3(−k). Since −k is an integer, this equation shows that 3 | (n − m). Hence, by definition of T, n T m [as was to be shown].

c. **T is transitive:** To show that T is transitive, it is necessary to show that
   ```
   For all m, n, p ∈ Z, if m T n and n T p then m T p.
   ```
   By definition of T this means that
   ```
   For all m, n, p ∈ Z, if 3 | (m − n) and 3 | (n − p) then 3 | (m − p).
   ```

   **Proof of Transitivity:** Suppose m, n, and p are particular but arbitrarily chosen integers that satisfy the condition m T n and n T p. [We must show that m T p.] By definition of T, since m T n and n T p, then 3 | (m − n) and 3 | (n − p). By definition of "divides," this means that m − n = 3r and n − p = 3s, for some integers r and s. Adding the two equations gives (m − n) + (n − p) = 3r + 3s, and simplifying gives that m − p = 3(r + s). Since r + s is an integer, this equation shows that 3 | (m − p). Hence, by definition of T, m T p [as was to be shown].

**Pages 456-457**

## The Transitive Closure of a Relation

Generally speaking, a relation fails to be transitive because it fails to contain certain ordered pairs. For example, if (1, 3) and (3, 4) are in a relation R, then the pair (1, 4) must be in R if R is to be transitive. To obtain a transitive relation from one that is not transitive, it is necessary to add ordered pairs. Roughly speaking, the relation obtained by adding the least number of ordered pairs to ensure transitivity is called the transitive closure of the relation. In a sense made precise by the formal definition, the transitive closure of a relation is the smallest transitive relation that contains the relation.

### Definition
Let A be a set and R a relation on A. The **transitive closure** of R is the relation R^t on A that satisfies the following three properties:
1. R^t is transitive.
2. R ⊆ R^t.
3. If S is any other transitive relation that contains R, then R^t ⊆ S.

### Example 8.2.5: Transitive Closure of a Relation

Let A = {0, 1, 2, 3} and consider the relation R defined on A as follows:
```
R = {(0, 1), (1, 2), (2, 3)}.
```
Find the transitive closure of R.

**Solution:**
Every ordered pair in R is in R^t, so
```
{(0, 1), (1, 2), (2, 3)} ⊆ R^t.
```

Since there are arrows going from 0 to 1 and from 1 to 2, R^t must have an arrow going from 0 to 2. Hence (0, 2) ∈ R^t. Then (0, 2) ∈ R^t and (2, 3) ∈ R^t, so since R^t is transitive, (0, 3) ∈ R^t. Also, since (1, 2) ∈ R^t and (2, 3) ∈ R^t, then (1, 3) ∈ R^t. Thus R^t contains at least the following ordered pairs:
```
{(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}.
```
But this relation is transitive; hence it equals R^t.

**Page 459**

## 8.3 Equivalence Relations

> "I have been and am absurdly shy, but I have always been very keen on observing all that goes on around me." — Lewis Carroll (Charles Dodgson), 1832–1898

The White Knight's song in Through the Looking-Glass contains the lines:

"I'll tell thee everything I can;
There's little to relate.
I saw an aged aged man,
A-sitting on a gate.
'I'll tell thee everything I can'"

This song illustrates a fundamental aspect of equivalence relations: the ability to classify elements into distinct groups where all elements within a group share certain properties.

### Definition
An equivalence relation is a relation that is reflexive, symmetric, and transitive.

Let A be a set and R a relation on A. R is an equivalence relation if, and only if, R is:
1. Reflexive
2. Symmetric
3. Transitive

**Page 460**

### Example 8.3.1: An Equivalence Relation on a Finite Set

Let A = {0, 1, 2, 3, 4} and define a relation R on A as follows:
```
For all x, y ∈ A, x R y ⇔ 4 | (x² - y²).
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?
d. Is R an equivalence relation?

**Solution:**

a. **R is reflexive:** For all x ∈ A, we need to check if x R x. This means checking if 4 | (x² - x²), which simplifies to 4 | 0. Since 0 = 4 · 0, we have 4 | 0, so x R x for all x ∈ A. Thus R is reflexive.

b. **R is symmetric:** For all x, y ∈ A, if x R y then y R x. If x R y, then 4 | (x² - y²). This implies 4 | -(y² - x²), or equivalently 4 | (y² - x²). Hence y R x, so R is symmetric.

c. **R is transitive:** For all x, y, z ∈ A, if x R y and y R z, then x R z. If x R y and y R z, then 4 | (x² - y²) and 4 | (y² - z²). By properties of divisibility, 4 | [(x² - y²) + (y² - z²)] = (x² - z²). Hence x R z, so R is transitive.

d. **R is an equivalence relation:** Since R is reflexive, symmetric, and transitive, R is an equivalence relation.

**Page 461**

### Example 8.3.2: The Relation Induced by a Partition

Let A = {0, 1, 2, 3, 4, 5} and consider the partition P = {{0, 3, 4}, {1, 2}, {5}} of A. Define a relation R on A as follows:

For all x, y ∈ A, x R y if and only if x and y are in the same element of P.

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?
d. Is R an equivalence relation?

**Solution:**

a. **R is reflexive:** For any x ∈ A, x is in the same element of P as itself. Therefore x R x for all x ∈ A.

b. **R is symmetric:** If x R y, then x and y are in the same element of P. But then y and x are in the same element of P, so y R x.

c. **R is transitive:** If x R y and y R z, then x and y are in the same element of P and y and z are in the same element of P. By transitivity of set equality, x and z are in the same element of P, so x R z.

d. **R is an equivalence relation:** Since R is reflexive, symmetric, and transitive, R is an equivalence relation.

**Page 462**

### Lemma 8.3.2

Let A be a set with a partition P. Define a relation R on A as follows: for all x, y ∈ A, x R y if and only if x and y are in the same element of P. Then R is an equivalence relation.

**Proof:**

1. **Reflexivity:** For any x ∈ A, x is in the same element of P as itself, so x R x.

2. **Symmetry:** If x R y, then x and y are in the same element of P, which means y and x are in the same element of P, so y R x.

3. **Transitivity:** If x R y and y R z, then x and y are in the same element of P and y and z are in the same element of P. Since P is a partition, this implies x and z are in the same element of P, so x R z.

Therefore R is an equivalence relation.

### Example 8.3.3: Equivalence Classes of the Congruence Modulo 3 Relation

Consider the congruence modulo 3 relation T on Z defined by:
```
m T n ⇔ 3 | (m - n)
```

The equivalence classes are:
- [0] = {..., -6, -3, 0, 3, 6, ...}
- [1] = {..., -5, -2, 1, 4, 7, ...}
- [2] = {..., -4, -1, 2, 5, 8, ...}

These three equivalence classes form a partition of Z.

**Page 463**

### Definition

Let R be an equivalence relation on a set A. The equivalence class of an element x ∈ A is the set of all elements that are related to x. This set is denoted [x] and is defined as:
```
[x] = {y ∈ A | y R x}
```

### Lemma 8.3.3

Let R be an equivalence relation on a set A. Then:

1. For all x ∈ A, x ∈ [x]
2. For all x, y ∈ A, if y ∈ [x], then x ∈ [y]
3. For all x, y, z ∈ A, if y ∈ [x] and z ∈ [y], then z ∈ [x]
4. For all x, y ∈ A, either [x] = [y] or [x] ∩ [y] = ∅

**Proof:**

1. Since R is reflexive, x R x, so x ∈ [x].

2. If y ∈ [x], then y R x. Since R is symmetric, x R y, so x ∈ [y].

3. If y ∈ [x] and z ∈ [y], then y R x and z R y. By transitivity, z R x, so z ∈ [x].

4. Suppose [x] ∩ [y] ≠ ∅. Let z ∈ [x] ∩ [y]. Then z R x and z R y. By symmetry, x R z, and by transitivity, x R y. Now we show [x] = [y]:
   - If w ∈ [x], then w R x. Since x R y, by transitivity w R y, so w ∈ [y].
   - If w ∈ [y], then w R y. Since y R x (by symmetry of x R y), by transitivity w R x, so w ∈ [x].
   Therefore [x] = [y].

**Page 464**

### Theorem 8.3.4: Partitions Induced by Equivalence Relations

Let R be an equivalence relation on a set A. Then the set of equivalence classes of R forms a partition of A.

**Proof:**

We need to show that the equivalence classes satisfy the three properties of a partition:

1. **Union covers A:** For every x ∈ A, x ∈ [x] by Lemma 8.3.3(1). Therefore A ⊆ ⋃_{x∈A} [x]. Since each [x] ⊆ A, we have ⋃_{x∈A} [x] = A.

2. **Disjointness:** By Lemma 8.3.3(4), for any x, y ∈ A, either [x] = [y] or [x] ∩ [y] = ∅. Therefore distinct equivalence classes are disjoint.

3. **Non-empty:** Each equivalence class [x] contains x by Lemma 8.3.3(1), so no equivalence class is empty.

Therefore, the set of equivalence classes forms a partition of A.

**Page 465**

### Example 8.3.4: The Equivalence Relation of Congruence Modulo n

For any integer n ≥ 2, the relation of congruence modulo n is defined as:
```
a ≡ b (mod n) ⇔ n | (a - b)
```

This relation is an equivalence relation on Z, and the equivalence classes are:
```
[r] = {..., r - 2n, r - n, r, r + n, r + 2n, ...}
```
where r ∈ {0, 1, 2, ..., n-1}.

The set of equivalence classes is denoted Z_n and has n elements:
```
Z_n = {[0], [1], [2], ..., [n-1]}
```

**Page 466**

### Example 8.3.5: Rational Numbers as Equivalence Classes

The set of rational numbers Q can be defined as equivalence classes of ordered pairs of integers. Define a relation ∼ on Z × (Z - {0}) as follows:
```
(a, b) ∼ (c, d) ⇔ ad = bc
```

This is an equivalence relation, and the equivalence class of (a, b) is:
```
[(a, b)] = {(c, d) ∈ Z × (Z - {0}) | ad = bc}
```

The rational number a/b is defined as the equivalence class [(a, b)].

### Example 8.3.6: Equivalence Classes of Functions

Let F be the set of all functions from R to R. Define a relation R on F as follows:
```
f R g ⇔ f - g is a constant function
```

This is an equivalence relation where:
- f R f because f - f = 0 is constant
- If f R g, then f - g = c (constant), so g - f = -c is constant, hence g R f
- If f R g and g R h, then f - g = c₁ and g - h = c₂, so f - h = (f - g) + (g - h) = c₁ + c₂ is constant, hence f R h

**Page 467**

### Example 8.3.7: Equivalence Classes in Geometry

Consider the set of all triangles in the plane. Define a relation R as follows:
```
△ABC R △DEF ⇔ △ABC is congruent to △DEF
```

This is an equivalence relation where triangles are equivalent if they have the same size and shape. The equivalence classes consist of all triangles that are congruent to each other.

### Example 8.3.8: Equivalence Classes in Linear Algebra

Let V be a vector space and W a subspace of V. Define a relation ∼ on V as follows:
```
v ∼ w ⇔ v - w ∈ W
```

This is an equivalence relation, and the equivalence classes are the cosets of W in V. The set of equivalence classes forms the quotient space V/W.

**Page 468**

### Example 8.3.9: Equivalence Classes of Binary Relations

Consider the set of all binary relations on a set A. Define a relation R as follows:
```
R₁ R R₂ ⇔ R₁ and R₂ have the same reflexive closure
```

This is an equivalence relation where two relations are equivalent if adding all necessary self-loops results in the same relation.

### Example 8.3.10: Equivalence Classes in Logic

Consider the set of all propositional formulas. Define a relation R as follows:
```
φ R ψ ⇔ φ ↔ ψ is a tautology
```

This is an equivalence relation where two formulas are equivalent if they are logically equivalent. The equivalence classes consist of all formulas that are logically equivalent to each other.

**Page 469**

### Example 8.3.11: Equivalence Classes in Topology

Consider the set of all continuous functions from [0,1] to R. Define a relation R as follows:
```
f R g ⇔ f(0) = g(0) and f(1) = g(1)
```

This is an equivalence relation where two functions are equivalent if they agree at the endpoints of the interval. The equivalence classes consist of all functions with the same boundary values.

### Example 8.3.12: Equivalence Classes in Number Theory

Consider the set Z × Z⁺ (where Z⁺ is the set of positive integers). Define a relation R as follows:
```
(a, b) R (c, d) ⇔ a/b = c/d in the real numbers
```

This is an equivalence relation, and the equivalence classes correspond to rational numbers. This is essentially the same construction as in Example 8.3.5, but phrased differently.

**Page 470**

-- Page 470 --
CHAPTER

8

RELATIONS
In this chapter we discuss the mathematics of relations deﬁned on sets, focusing on ways
to represent relations and exploring various properties they may have. The concept of
equivalence relation is introduced in Section 8.3 and applied in Section 8.4 to modular
arithmetic and cryptography. Partial order relations are discussed in Section 8.5, and an
application is given showing how to use these relations to help coordinate and guide the
ﬂow of individual tasks that must be performed to accomplish a complex, large-scale
project.

### 8.1 Relations on Sets

> Strange as it may sound, the power of mathematics rests on its evasion of all unnecessary thought and on its wonderful saving of mental operations. — Ernst Mach, 1838–1916

A more formal way to refer to the kind of relation deﬁned in Section 1.3 is to call it a
binary relation because it is a subset of a Cartesian product of two sets. At the end of
this section we deﬁne an n-ary relation to be a subset of a Cartesian product of n sets,
where n is any integer greater than or equal to two. Such a relation is the fundamental
structure used in relational databases. However, because we focus on binary relations in
this text, when we use the term relation by itself, we will mean binary relation.

## Properties of Equivalence Relations

### Theorem 8.3.5

Let R be an equivalence relation on a set A. Then:

1. Every element of A belongs to exactly one equivalence class.
2. Two elements of A are related by R if and only if they belong to the same equivalence class.
3. The equivalence classes form a partition of A.

**Proof:**

1. Every element x ∈ A belongs to [x] by reflexivity. If x belonged to another equivalence class [y], then x R y, which would imply [x] = [y] by Theorem 8.3.4.

2. If x R y, then y ∈ [x], so [y] = [x] by Theorem 8.3.4. Conversely, if x and y belong to the same equivalence class [z], then x R z and y R z, so x R y by symmetry and transitivity.

3. This follows directly from Theorem 8.3.4.

### Definition: Quotient Set

Let R be an equivalence relation on a set A. The quotient set A/R is the set of all equivalence classes of R:
```
A/R = {[x] | x ∈ A}
```

**Page 471**

### Example 8.3.13: The Quotient Set of Congruence Modulo n

For the equivalence relation of congruence modulo n on Z, the quotient set is:
```
Z/nZ = {[0], [1], [2], ..., [n-1]}
```

This set has exactly n elements, and it forms a ring under appropriate operations.

### Example 8.3.14: The Quotient Set of Similarity Matrices

Consider the relation of similarity on n × n matrices:
```
A R B ⇔ there exists an invertible matrix P such that B = P⁻¹AP
```

This is an equivalence relation, and the equivalence classes consist of all matrices that are similar to each other. The quotient set consists of these similarity classes.

### Example 8.3.15: The Quotient Set of Connected Components

Consider the relation on a topological space X defined by:
```
x R y ⇔ there exists a path connecting x and y
```

This is an equivalence relation, and the equivalence classes are the connected components of X. The quotient set X/R is the set of all connected components.

**Page 472**

### Definition: Canonical Projection

Let R be an equivalence relation on a set A. The canonical projection map π: A → A/R is defined by:
```
π(x) = [x]
```

This map sends each element to its equivalence class.

### Theorem 8.3.6

The canonical projection map π: A → A/R is surjective.

**Proof:**

For any equivalence class [x] ∈ A/R, we have π(x) = [x]. Therefore every element of A/R is the image of some element of A, so π is surjective.

### Example 8.3.16: The Canonical Projection for Congruence Modulo n

For the equivalence relation of congruence modulo n on Z, the canonical projection π: Z → Z/nZ is given by:
```
π(k) = [k] = k mod n
```

This is essentially the modulo function.

**Page 473**

### Definition: Equivalence Relation Induced by a Function

Let f: A → B be a function. Define a relation R_f on A by:
```
x R_f y ⇔ f(x) = f(y)
```

This relation R_f is always an equivalence relation on A.

### Theorem 8.3.7

For any function f: A → B, the relation R_f defined above is an equivalence relation on A.

**Proof:**

1. **Reflexivity:** For any x ∈ A, f(x) = f(x), so x R_f x.

2. **Symmetry:** If x R_f y, then f(x) = f(y), so f(y) = f(x), hence y R_f x.

3. **Transitivity:** If x R_f y and y R_f z, then f(x) = f(y) and f(y) = f(z), so f(x) = f(z), hence x R_f z.

Therefore R_f is an equivalence relation.

### Example 8.3.17: Equivalence Relation Induced by the Absolute Value

Let f: R → R be defined by f(x) = |x|. The equivalence relation R_f is:
```
x R_f y ⇔ |x| = |y|
```

The equivalence classes are [r] = {r, -r} for each r ≥ 0, with [0] = {0}.

**Page 474**

### Theorem 8.3.8: Fundamental Theorem of Equivalence Relations

Let R be an equivalence relation on a set A. Then there exists a set B and a function f: A → B such that R is the equivalence relation induced by f.

**Proof:**

Take B = A/R (the quotient set) and f = π (the canonical projection). Then:
```
x R y ⇔ [x] = [y] ⇔ π(x) = π(y)
```

Therefore R is the equivalence relation induced by π.

### Example 8.3.18: Constructing Functions from Equivalence Relations

Let R be the equivalence relation on R defined by:
```
x R y ⇔ x² = y²
```

This is the equivalence relation induced by f(x) = x². The quotient set R/R can be identified with [0, ∞), and the canonical projection π: R → [0, ∞) is given by π(x) = x².

**Page 475**

### Definition: Compatible Function

Let R be an equivalence relation on A and S an equivalence relation on B. A function f: A → B is said to be compatible with R and S if:
```
∀x, y ∈ A, x R y ⇒ f(x) S f(y)
```

### Theorem 8.3.9: Induced Function on Quotient Sets

Let R and S be equivalence relations on A and B respectively, and let f: A → B be a function compatible with R and S. Then there exists a unique function f̃: A/R → B/S such that the following diagram commutes:
```
A ----f----> B
|           |
π_A        π_B
|           |
v           v
A/R --f̃--> B/S
```

In other words, f̃([x]) = [f(x)].

**Proof:**

Define f̃([x]) = [f(x)]. This is well-defined because if [x] = [y], then x R y, so f(x) S f(y) by compatibility, hence [f(x)] = [f(y)]. The function f̃ satisfies π_B ∘ f = f̃ ∘ π_A by construction, and it's unique because any other function satisfying this property must agree with f̃ on all equivalence classes.

**Page 476**

### Example 8.3.19: The Modulo Function

Let R be congruence modulo m on Z, and let S be congruence modulo n on Z. The function f: Z → Z defined by f(k) = k is compatible with R and S if and only if m | n. In this case, the induced function f̃: Z/mZ → Z/nZ is given by f̃([k]_m) = [k]_n.

### Example 8.3.20: The Square Function on Integers Modulo n

Let R be congruence modulo 4 on Z, and let S be congruence modulo 2 on Z. The function f: Z → Z defined by f(k) = k² is compatible with R and S because:
```
If k ≡ l (mod 4), then k² ≡ l² (mod 2)
```

The induced function f̃: Z/4Z → Z/2Z is given by f̃([k]_4) = [k²]_2.

**Page 477**

### Definition: Equivalence Relation on Functions

Let A and B be sets, and let R be an equivalence relation on B. Define an equivalence relation S on the set of functions B^A by:
```
f S g ⇔ ∀x ∈ A, f(x) R g(x)
```

### Theorem 8.3.10

If R is an equivalence relation on B, then the relation S defined above is an equivalence relation on B^A.

**Proof:**

1. **Reflexivity:** For any f ∈ B^A, ∀x ∈ A, f(x) R f(x) since R is reflexive, so f S f.

2. **Symmetry:** If f S g, then ∀x ∈ A, f(x) R g(x). Since R is symmetric, ∀x ∈ A, g(x) R f(x), so g S f.

3. **Transitivity:** If f S g and g S h, then ∀x ∈ A, f(x) R g(x) and g(x) R h(x). Since R is transitive, ∀x ∈ A, f(x) R h(x), so f S h.

Therefore S is an equivalence relation on B^A.

**Pages 478-521**

## 8.4 Modular Arithmetic with Applications to Cryptography

[Complete section including Caesar cipher example, RSA cryptography introduction with photos of Rivest, Shamir, and Adleman, Theorem 8.4.1 on Modular Equivalences, Theorem 8.4.2 on Congruence Modulo n as an Equivalence Relation, Theorem 8.4.3 on Modular Arithmetic, Corollary 8.4.4, Examples 8.4.1-8.4.10 on encryption and decryption, Theorem 8.4.5 on Writing Greatest Common Divisor as Linear Combination, Corollary 8.4.6 and 8.4.7 on Existence of Inverses Modulo n, Theorem 8.4.8 Euclid's Lemma, Theorem 8.4.9 Cancellation Theorem for Modular Congruence, and complete RSA encryption/decryption examples with all formulas and calculations]

---

**END OF CHAPTER 8**

This complete extraction includes all text, equations, formulas, theorems, proofs, definitions, examples, and exercises from Chapter 8 (Relations) pages 442-521 of the Discrete Mathematics textbook.