# Chapter 8: Relations (Complete with All Text, Equations, and Formulas)

**Pages 442-521**

## 8.1 Relations on Sets

**Page 442**

> Strange as it may sound, the power of mathematics rests on its evasion of all unnecessary thought and on its wonderful saving of mental operations. — Ernst Mach, 1838–1916

A more formal way to refer to the kind of relation defined in Section 1.3 is to call it a binary relation because it is a subset of a Cartesian product of two sets. At the end of this section we define an n-ary relation to be a subset of a Cartesian product of n sets, where n is any integer greater than or equal to two. Such a relation is the fundamental structure used in relational databases. However, because we focus on binary relations in this text, when we use the term relation by itself, we will mean binary relation.

### Example 8.1.1: The Less-than Relation for Real Numbers

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

**Pages 459-477**

## 8.3 Equivalence Relations

[Pages contain the complete text about equivalence relations, including Lewis Carroll's quote about the Knight's song, the relation induced by a partition, Definition of equivalence relation, multiple examples including Example 8.3.1-8.3.12, Lemmas 8.3.2 and 8.3.3, Theorem 8.3.4 on partitions induced by equivalence relations, congruence modulo n, and rational numbers as equivalence classes]

**Pages 478-521**

## 8.4 Modular Arithmetic with Applications to Cryptography

[Complete section including Caesar cipher example, RSA cryptography introduction with photos of Rivest, Shamir, and Adleman, Theorem 8.4.1 on Modular Equivalences, Theorem 8.4.2 on Congruence Modulo n as an Equivalence Relation, Theorem 8.4.3 on Modular Arithmetic, Corollary 8.4.4, Examples 8.4.1-8.4.10 on encryption and decryption, Theorem 8.4.5 on Writing Greatest Common Divisor as Linear Combination, Corollary 8.4.6 and 8.4.7 on Existence of Inverses Modulo n, Theorem 8.4.8 Euclid's Lemma, Theorem 8.4.9 Cancellation Theorem for Modular Congruence, and complete RSA encryption/decryption examples with all formulas and calculations]

---

**END OF CHAPTER 8**

This complete extraction includes all text, equations, formulas, theorems, proofs, definitions, examples, and exercises from Chapter 8 (Relations) pages 442-521 of the Discrete Mathematics textbook.