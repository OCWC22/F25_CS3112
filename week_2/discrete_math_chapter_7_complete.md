# Chapter 7: Functions (Complete)

**Pages 411-470**

## Introduction

This chapter explores the mathematical concept of functions - one of the most fundamental structures in mathematics and computer science. We begin with basic definitions and properties, then examine special types of functions like one-to-one and onto functions, inverse functions, and function composition. The chapter culminates with an important discussion of cardinality and its applications to computability.

---

## 7.1 Functions Defined on General Sets

**Page 411**

> The theory that has had the greatest development in recent times is without any doubt the theory of functions. — Vito Volterra, 1888

As used in ordinary language, the word function indicates dependence of one varying quantity on another. If your teacher tells you that your grade in a course will be a function of your performance on the exams, you interpret this to mean that the teacher has some rule for translating exam scores into grades. To each collection of exam scores there corresponds a certain grade.

In Section 1.3 we defined a function as a certain type of relation. In this chapter we focus on the more dynamic way functions are used in mathematics. The following is a restatement of the definition of function that includes additional terminology associated with the concept.

### Definition: Function

A function f from a set X to a set Y, denoted f : X → Y, is a relation from X, the domain, to Y, the co-domain, that satisfies two properties:

1. **Every element in X is related to some element in Y.**
2. **No element in X is related to more than one element in Y.**

Thus, given any element x in X, there is a unique element in Y that is related to x by f. If we call this element y, then we say that "f sends x to y" or "f maps x to y" and write x → y or f : x → y. The unique element to which f sends x is denoted f(x) and is called:

- f of x, or
- the output of f for the input x, or
- the value of f at x, or
- the image of x under f.

The set of all values of f taken together is called the range of f or the image of X under f. Symbolically,
range of f = image of X under f = {y ∈ Y | y = f(x), for some x in X}.

Given an element y in Y, there may exist elements in X with y as their image. If f(x) = y, then x is called a preimage of y or an inverse image of y. The set of all inverse images of y is called the inverse image of y. Symbolically,
the inverse image of y = {x ∈ X | f(x) = y}.

**Caution!** Use f(x) to refer to the value of the function f at x. Generally avoid using f(x) to refer to the function f itself.

In some mathematical contexts, the notation f(x) is used to refer both to the value of f at x and to the function f itself. Because using the notation this way can lead to confusion, we avoid it whenever possible. In this book, unless explicitly stated otherwise, the symbol f(x) always refers to the value of the function f at x and not to the function f itself.

The concept of function was developed over a period of centuries. A definition similar to that given above was first formulated for sets of numbers by the German mathematician Lejeune Dirichlet in 1837.

**Page 412**

### Arrow Diagrams

Recall from Section 1.3 that if X and Y are finite sets, you can define a function f from X to Y by drawing an arrow diagram. You make a list of elements in X and a list of elements in Y, and draw an arrow from each element in X to the corresponding element in Y, as shown in Figure 7.1.1.

```
X         f         Y
x1 ------------> y1
x2 ------------> y2
x3 ------------> y3
x4 ------------> y4
               y5
```

**This arrow diagram does define a function because**
1. Every element of X has an arrow coming out of it.
2. No element of X has two arrows coming out of it that point to two different elements of Y.

**Page 413**

### Example 7.1.1 Functions and Nonfunctions

Which of the arrow diagrams in Figure 7.1.2 define functions from X = {a, b, c} to Y = {1, 2, 3, 4}?

```
(a)
X         Y
a ----> 1
b       2
c ----> 3
       4

(b)
X         Y
a ----> 1
b ----> 2
c ----> 2
   ----> 3
       4

(c)
X         Y
a ----> 1
b ----> 2
c ----> 3
       4
```

**Solution**

Only (c) defines a function. In (a) there is an element of X, namely b, that is not sent to any element of Y; that is, there is no arrow coming out of b. And in (b) the element c is not sent to a unique element of Y; that is, there are two arrows coming out of c, one pointing to 2 and the other to 3.

### Example 7.1.2 A Function Defined by an Arrow Diagram

Let X = {a, b, c} and Y = {1, 2, 3, 4}. Define a function f from X to Y by the arrow diagram in Figure 7.1.3.

```
X         f         Y
a ----> 1
b ----> 2
c ----> 3
       4
```

a. Write the domain and co-domain of f.
b. Find f(a), f(b), and f(c).
c. What is the range of f?
d. Is c an inverse image of 2? Is b an inverse image of 3?
e. Find the inverse images of 2, 4, and 1.
f. Represent f as a set of ordered pairs.

**Solution**
a. domain of f = {a, b, c}, co-domain of f = {1, 2, 3, 4}
b. f(a) = 1, f(b) = 2, f(c) = 3
c. range of f = {1, 2, 3}
d. No, No
e. inverse image of 2 = {b}, inverse image of 4 = ∅, inverse image of 1 = {a}
f. {(a, 1), (b, 2), (c, 3)}

In Example 7.1.2 there are no arrows pointing to the 4. This illustrates the fact that although each element of the domain of a function must have an arrow pointing out from it, there can be elements of the co-domain to which no arrows point. Note also that each element of Y has at most one arrow pointing to it.

**Page 414**

### Theorem 7.1.1 A Test for Function Equality

If F: X → Y and G: X → Y are functions, then F = G if, and only if, F(x) = G(x) for all x ∈ X.

**Proof:**
Suppose F: X → Y and G: X → Y are functions, that is, F and G are binary relations from X to Y that satisfy the two additional function properties. Then F and G are subsets of X × Y, and for (x, y) to be in F means that y is the unique element related to x by F, which we denote as F(x). Similarly, for (x, y) to be in G means that y is the unique element related to x by G, which we denote as G(x).

Now suppose that F(x) = G(x) for all x ∈ X. Then if x is any element of X,
(x, y) ∈ F ⇔ y = F(x) ⇔ y = G(x) ⇔ (x, y) ∈ G
because F(x) = G(x)

So F and G consist of exactly the same elements and hence F = G.

Conversely, if F = G, then for all x ∈ X,
y = F(x) ⇔ (x, y) ∈ F ⇔ (x, y) ∈ G ⇔ y = G(x)
Thus, since both F(x) and G(x) equal y, we have that F(x) = G(x).

**Page 415**

### Example 7.1.3 Equality of Functions

a. Let J3 = {0, 1, 2}, and define functions f and g from J3 to J3 as follows: For all x in J3,
f(x) = (x² + x + 1) mod 3 and g(x) = (x + 2)² mod 3.

Does f = g?

b. Let F: R → R and G: R → R be functions. Define new functions F + G: R → R and G + F: R → R as follows: For all x ∈ R,
(F + G)(x) = F(x) + G(x) and (G + F)(x) = G(x) + F(x).

Does F + G = G + F?

**Solution**
a. Yes, the table of values shows that f(x) = g(x) for all x in J3.

| x | x² + x + 1 | f(x) = (x² + x + 1) mod 3 | (x + 2)² | g(x) = (x + 2)² mod 3 |
|---|------------|----------------------------|----------|------------------------|
| 0 | 1          | 1                          | 4        | 1                      |
| 1 | 3          | 0                          | 9        | 0                      |
| 2 | 7          | 1                          | 16       | 1                      |

b. Again the answer is yes. For all real numbers x,
(F + G)(x) = F(x) + G(x) = G(x) + F(x) = (G + F)(x)
by the commutative law for addition of real numbers.

**Page 416**

### Examples of Functions

The following examples illustrate some of the wide variety of different types of functions.

### Example 7.1.4 The Identity Function on a Set

Given a set X, define a function I_X from X to X by
I_X(x) = x for all x in X.

The function I_X is called the identity function on X because it sends each element of X to the element that is identical to it. Thus the identity function can be pictured as a machine that sends each piece of input directly to the output chute without changing it in any way.

Let X be any set and suppose that a_i_k_j and φ(z) are elements of X. Find I_X(a_i_k_j) and I_X(φ(z)).

**Solution** Whatever is input to the identity function comes out unchanged, so I_X(a_i_k_j) = a_i_k_j and I_X(φ(z)) = φ(z).

### Example 7.1.5 Sequences

The formal definition of sequences specifies that an infinite sequence is a function defined on the set of integers that are greater than or equal to a particular integer. For example, the sequence denoted
1, -1/2, 1/3, -1/4, 1/5, ..., (-1)ⁿ/(n+1), ...

can be thought of as the function f from the nonnegative integers to the real numbers that associates 0 → 1, 1 → -1/2, 2 → 1/3, 3 → -1/4, 4 → 1/5, and, in general, n → (-1)ⁿ/(n+1).

In other words, f: Z_nonneg → R is the function defined as follows:
Send each integer n ≥ 0 to f(n) = (-1)ⁿ/(n+1).

In fact, there are many functions that can be used to define a given sequence. For instance, express the sequence above as a function from the set of positive integers to the set of real numbers.

**Solution** Define g: Z⁺ → R by g(n) = (-1)ⁿ⁺¹/n for each n ∈ Z⁺. Then g(1) = 1, g(2) = -1/2, g(3) = 1/3 and in general g(n+1) = (-1)ⁿ⁺²/(n+1) = (-1)ⁿ/(n+1) = f(n).

**Page 417**

### One-to-One Functions

**Definition:** A function F: X → Y is **one-to-one** (or **injective**) if, and only if, for all elements x₁ and x₂ in X,
```
if F(x₁) = F(x₂), then x₁ = x₂
```

Equivalently:
```
if x₁ ≠ x₂, then F(x₁) ≠ F(x₂)
```

Symbolically: F is one-to-one ⟺ ∀x₁, x₂ ∈ X, [F(x₁) = F(x₂) → x₁ = x₂]

### Example 7.2.1: Proving a Function Is One-to-One

Define g: R → R by g(x) = 4x - 1 for all x ∈ R. Prove g is one-to-one.

**Proof:**
Suppose x₁, x₂ ∈ R and g(x₁) = g(x₂).
Then:
```
4x₁ - 1 = 4x₂ - 1
4x₁ = 4x₂
x₁ = x₂
```
Therefore g is one-to-one. ■

### Example 7.2.2: Proving a Function Is Not One-to-One

**Page 423**

Define h: R → R by h(x) = x² for all x ∈ R. Show h is not one-to-one.

**Proof:**
Counterexample: h(2) = 4 and h(-2) = 4, but 2 ≠ -2.
Therefore h is not one-to-one. ■

### Onto Functions

**Definition:** A function F: X → Y is **onto** (or **surjective**) if, and only if, given any element y ∈ Y, there is at least one element x ∈ X with F(x) = y.

Symbolically: F is onto ⟺ ∀y ∈ Y, ∃x ∈ X such that F(x) = y

Equivalently: F is onto ⟺ range of F = co-domain of F

### Example 7.2.3: Proving a Function Is Onto

**Page 424**

Define g: R → R by g(x) = 4x - 1. Prove g is onto.

**Proof:**
Let y ∈ R be arbitrary. We need to find x ∈ R such that g(x) = y.
Solving:
```
4x - 1 = y
4x = y + 1
x = (y + 1)/4
```
Since x = (y + 1)/4 is a real number, and g((y + 1)/4) = 4((y + 1)/4) - 1 = y + 1 - 1 = y,
we have shown that for every y ∈ R, there exists x ∈ R with g(x) = y.
Therefore g is onto. ■

### Example 7.2.4: A Function That Is Neither One-to-One Nor Onto

**Page 425**

Define f: R → R by f(x) = 2x² + 1. Show f is neither one-to-one nor onto.

**Not one-to-one:** f(1) = 3 and f(-1) = 3, but 1 ≠ -1.

**Not onto:** There is no x ∈ R such that f(x) = 0, since 2x² + 1 ≥ 1 for all x ∈ R.

### Bijections

**Definition:** A function F: X → Y is a **bijection** (or **one-to-one correspondence**) if, and only if, F is both one-to-one and onto.

### Example 7.2.5: A Bijection

The function f: R → R defined by f(x) = 3x + 4 is a bijection.

**Proof of one-to-one:** If f(x₁) = f(x₂), then 3x₁ + 4 = 3x₂ + 4, so x₁ = x₂.

**Proof of onto:** For any y ∈ R, let x = (y - 4)/3. Then f(x) = 3((y - 4)/3) + 4 = y.

### Inverse Image

**Page 426**

**Definition:** If f: X → Y and B ⊆ Y, the **inverse image** of B is:
```
f⁻¹(B) = {x ∈ X | f(x) ∈ B}
```

### Example 7.2.6: Finding Inverse Images

Let f: {1, 2, 3, 4, 5} → {a, b, c, d} be defined by:
```
f(1) = c, f(2) = b, f(3) = a, f(4) = a, f(5) = c
```

Find f⁻¹({a, c}).

**Solution:**
```
f⁻¹({a, c}) = {x | f(x) ∈ {a, c}} = {1, 3, 4, 5}
```

### Hash Functions

**Page 427-428**

A **hash function** h: S → Z_m takes strings as input and outputs integers in {0, 1, ..., m-1}.

Common hash functions:
1. **Division method:** h(x) = x mod m
2. **Middle square method:** Square x, extract middle digits, take mod m
3. **Folding method:** Break x into pieces, add them, take mod m

### Example 7.2.7: A Hash Function Using the Division Method

Let h(x) = x mod 11 for 4-digit student ID numbers.

```
h(0412) = 412 mod 11 = 5
h(9184) = 9184 mod 11 = 5  (collision!)
h(2541) = 2541 mod 11 = 1
```

### Example 7.2.8: The Pigeonhole Principle

**Page 429**

**Theorem (Pigeonhole Principle):** If n pigeons are placed into m pigeonholes and n > m, then at least one pigeonhole contains more than one pigeon.

More formally: If f: X → Y where X and Y are finite sets with |X| > |Y|, then f is not one-to-one.

### Application: Decimal Expansion of Fractions

**Page 430**

**Example 7.2.9:** The decimal expansion of any rational number is eventually periodic.

**Proof sketch:** When computing a/b by long division, there are only b possible remainders: 0, 1, 2, ..., b-1. By the pigeonhole principle, some remainder must repeat, causing the decimal expansion to become periodic.

For example: 1/7 = 0.142857142857... (period of 6)

---

## 7.3 The Composition of Functions

**Page 431**

> Composition, alone, can transport the aesthetic from a ground of ill-digested personal predilections to the level of unprejudiced perception of relations. Above all, with the new means of construction, the painter will free himself from the bodily-psychological inheritance...and from the personal.
> — Naum Gabo, "The Constructive Idea in Art," 1937

### Definition: Composition of Functions

Let f: X → Y and g: Y → Z be functions with the range of f a subset of the domain of g. The **composition** of g and f, denoted g ∘ f, is the function from X to Z defined by:

```
(g ∘ f)(x) = g(f(x))    for all x ∈ X
```

**Page 432**

### Example 7.1.11 A Boolean Function

Consider the three-place Boolean function defined from the set of all 3-tuples of 0's and 1's to {0, 1} as follows: For each triple (x₁, x₂, x₃) of 0's and 1's,
f(x₁, x₂, x₃) = (x₁ + x₂ + x₃) mod 2.

Describe f using an input/output table.

**Solution**
f(1, 1, 1) = (1 + 1 + 1) mod 2 = 3 mod 2 = 1
f(1, 1, 0) = (1 + 1 + 0) mod 2 = 2 mod 2 = 0

The rest of the values of f can be calculated similarly to obtain the following table.

```
Input   | Output
x₁ x₂ x₃ | (x₁ + x₂ + x₃) mod 2
---------|-------------------
1  1  1  | 1
1  1  0  | 0
1  0  1  | 0
1  0  0  | 1
0  1  1  | 0
0  1  0  | 1
0  0  1  | 1
0  0  0  | 0
```

### Checking Whether a Function Is Well Defined

It can sometimes happen that what appears to be a function defined by a rule is not really a function at all. To give an example, suppose we wrote, "Define a function f: R → R by specifying that for all real numbers x, f(x) is the real number y such that x² + y² = 1."

There are two distinct reasons why this description does not define a function. For almost all values of x, either (1) there is no y that satisfies the given equation or (2) there are two different values of y that satisfy the equation. For instance, when x = 2, there is no real number y such that 2² + y² = 1, and when x = 0, both y = -1 and y = 1 satisfy the equation 0² + y² = 1. In general, we say that a "function" is not well defined if it fails to satisfy at least one of the requirements for being a function.

**Page 423**

### Example 7.1.12 A Function That Is Not Well Defined

Recall that Q represents the set of all rational numbers. Suppose you read that a function f: Q → Z is to be defined by the formula
f(m/n) = m for all integers m and n with n ≠ 0.

That is, the integer associated by f to the number m/n is m. Is f well defined? Why?

**Solution**
The function f is not well defined. The reason is that fractions have more than one representation as quotients of integers. For instance, 1/2 = 3/6. Now if f were a function, then the definition of a function would imply that f(1/2) = f(3/6) since 1/2 = 3/6. But applying the formula for f, you find that
f(1/2) = 1 and f(3/6) = 3,
and so f(1/2) ≠ f(3/6).

This contradiction shows that f is not well defined and, therefore, is not a function.

**Note** that the phrase well-defined function is actually redundant; for a function to be well defined really means that it is worthy of being called a function.

**Page 424**

### Functions Acting on Sets

Given a function from a set X to a set Y, you can consider the set of images in Y of all the elements in a subset of X and the set of inverse images in X of all the elements in a subset of Y.

### Definition: Functions Acting on Sets

If f: X → Y is a function and A ⊆ X and C ⊆ Y, then
f(A) = {y ∈ Y | y = f(x) for some x in A}
and
f⁻¹(C) = {x ∈ X | f(x) ∈ C}.

f(A) is called the image of A, and f⁻¹(C) is called the inverse image of C.

**Note** For y ∈ Y, f⁻¹(y) = f⁻¹({y}).

### Example 7.1.13 The Action of a Function on Subsets of a Set

Let X = {1, 2, 3, 4} and Y = {a, b, c, d, e}, and define F: X → Y by the following arrow diagram:
```
1 ----> a
2 ----> b
3 ----> d
4 ----> b
       c
       e
```

Let A = {1, 4}, C = {a, b}, and D = {c, e}. Find F(A), F(X), F⁻¹(C), and F⁻¹(D).

**Solution**
F(A) = {a, b}
F(X) = {a, b, d}
F⁻¹(C) = {1, 2, 4}
F⁻¹(D) = ∅

**Page 425**

### Example 7.1.14 Interaction of a Function with Union

Let X and Y be sets, let F be a function from X to Y, and let A and B be any subsets of X. Prove that F(A ∪ B) ⊆ F(A) ∪ F(B).

**Solution**
The fact that X, Y, F, A, and B were formally introduced prior to the word "Prove" allows you to regard their existence and relationships as part of your background knowledge. Thus to prove that F(A ∪ B) ⊆ F(A) ∪ F(B), you only need show that if y is any element in F(A ∪ B), then y is an element of F(A) ∪ F(B).

**Proof:**
Suppose y ∈ F(A ∪ B). [We must show that y ∈ F(A) ∪ F(B).] By definition of function, y = F(x) for some x ∈ A ∪ B. By definition of union, x ∈ A or x ∈ B.

**Case 1**, x ∈ A: In this case, y = F(x) for some x in A. Hence y ∈ F(A), and so by definition of union, y ∈ F(A) ∪ F(B).

**Case 2**, x ∈ B: In this case, y = F(x) for some x in B. Hence y ∈ F(B), and so by definition of union, y ∈ F(A) ∪ F(B).

Thus in either case y ∈ F(A) ∪ F(B) [as was to be shown].

Exercise 38 asks you to prove the opposite containment from the one in example 7.1.14. Taken together, the example and the solution to the exercise establish the full equality that F(A ∪ B) = F(A) ∪ F(B).

---

### Test Yourself

Answers to Test Yourself questions are located at the end of each section.

1. Given a function f from a set X to a set Y, f(x) is _____.
2. Given a function f from a set X to a set Y, if f(x) = y, then y is called _____ or _____ or _____.
3. Given a function f from a set X to a set Y, the range of f (or the image of X under f) is _____.
4. Given a function f from a set X to a set Y, if f(x) = y, then x is called _____ or _____.
5. Given a function f from a set X to a set Y, if y ∈ Y, then f⁻¹(y) = _____ and is called _____.
6. Given functions f and g from a set X to a set Y, f = g if, and only if, _____.
7. Given positive real numbers x and b with b ≠ 1, log_b x = _____.
8. Given a function f from a set X to a set Y and a subset A of X, f(A) = _____.
9. Given a function f from a set X to a set Y and a subset C of Y, f⁻¹(C) = _____.

---

### Exercise Set 7.1

1. Let X = {1, 3, 5} and Y = {s, t, u, v}. Define f: X → Y by the following arrow diagram.
   ```
   X         f         Y
   1 ----> s
   3 ----> t
   5 ----> u
           v
   ```
   a. Write the domain of f and the co-domain of f.
   b. Find f(1), f(3), and f(5).
   c. What is the range of f?
   d. Is 3 an inverse image of s? Is 1 an inverse image of u?
   e. What is the inverse image of s? of u? of v?
   f. Represent f as a set of ordered pairs.

2. Let X = {1, 3, 5} and Y = {a, b, c, d}. Define g: X → Y by the following arrow diagram.
   ```
   X         g         Y
   1 ----> a
   3 ----> b
   5 ----> c
           d
   ```
   a. Write the domain of g and the co-domain of g.
   b. Find g(1), g(3), and g(5).
   c. What is the range of g?
   d. Is 3 an inverse image of a? Is 1 an inverse image of b?
   e. What is the inverse image of b? of c?
   f. Represent g as a set of ordered pairs.

3. Indicate whether the statements in parts (a)–(d) are true or false. Justify your answers.
   a. If two elements in the domain of a function are equal, then their images in the co-domain are equal.
   b. If two elements in the co-domain of a function are equal, then their preimages in the domain are also equal.
   c. A function can have the same output for more than one input.
   d. A function can have the same input for more than one output.

4. a. Find all functions from X = {a, b} to Y = {u, v}.
   b. Find all functions from X = {a, b, c} to Y = {u}.
   c. Find all functions from X = {a, b, c} to Y = {u, v}.

5. Let I_Z be the identity function defined on the set of all integers, and suppose that e, b_i, K(t), and u_k_j all represent integers. Find
   a. I_Z(e)
   b. I_Z(b_i)
   c. I_Z(K(t))
   d. I_Z(u_k_j)

6. Find functions defined on the set of nonnegative integers that define the sequences whose first six terms are given below.
   a. 1, -1/2, 1/3, -1/4, 1/5, -1/6
   b. 0, -2, 4, -6, 8, -10

7. Let A = {1, 2, 3, 4, 5} and define a function F: P(A) → Z as follows: For all sets X in P(A),
   F(X) = 0 if X has an even number of elements
         1 if X has an odd number of elements

   Find the following:
   a. F({1, 3, 4})
   b. F(∅)
   c. F({2, 3})
   d. F({2, 3, 4, 5})

8. Let J_5 = {0, 1, 2, 3, 4}, and define a function F: J_5 → J_5 as follows: For each x ∈ J_5, F(x) = (x³ + 2x + 4) mod 5.
   Find the following:
   a. F(0)
   b. F(1)
   c. F(2)
   d. F(3)
   e. F(4)

9. Define a function S: Z⁺ → Z⁺ as follows: For each positive integer n, S(n) = the sum of the positive divisors of n.
   Find the following:
   a. S(1)
   b. S(15)
   c. S(17)
   d. S(5)
   e. S(18)
   f. S(21)

10. Let D be the set of all finite subsets of positive integers. Define a function T: Z⁺ → D as follows: For each positive integer n, T(n) = the set of positive divisors of n.
    Find the following:
    a. T(1)
    b. T(15)
    c. T(17)
    d. T(5)
    e. T(18)
    f. T(21)

11. Define F: Z × Z → Z × Z as follows: For all ordered pairs (a, b) of integers, F(a, b) = (2a + 1, 3b - 2).
    Find the following:
    a. F(4, 4)
    b. F(2, 1)
    c. F(3, 2)
    d. F(1, 5)

12. Define G: J_5 × J_5 → J_5 × J_5 as follows: For all (a, b) ∈ J_5 × J_5, G(a, b) = ((2a + 1) mod 5, (3b - 2) mod 5).
    Find the following:
    a. G(4, 4)
    b. G(2, 1)
    c. G(3, 2)
    d. G(1, 5)

13. Let J_5 = {0, 1, 2, 3, 4}, and define functions f: J_5 → J_5 and g: J_5 → J_5 as follows: For each x ∈ J_5, f(x) = (x + 4)² mod 5 and g(x) = (x² + 3x + 1) mod 5. Is f = g? Explain.

14. Let J_5 = {0, 1, 2, 3, 4}, and define functions h: J_5 → J_5 and k: J_5 → J_5 as follows: For each x ∈ J_5, h(x) = (x + 3)³ mod 5 and k(x) = (x³ + 4x² + 2x + 2) mod 5. Is h = k? Explain.

15. Let F and G be functions from the set of all real numbers to itself. Define the product functions F · G: R → R and G · F: R → R as follows: For all x ∈ R,
    (F · G)(x) = F(x) · G(x)
    (G · F)(x) = G(x) · F(x)
    Does F · G = G · F? Explain.

16. Let F and G be functions from the set of all real numbers to itself. Define new functions F - G: R → R and G - F: R → R as follows: For all x ∈ R,
    (F - G)(x) = F(x) - G(x)
    (G - F)(x) = G(x) - F(x)
    Does F - G = G - F? Explain.

17. Use the definition of logarithm to fill in the blanks below.
    a. log₂ 8 = 3 because _____.
    b. log₅ 25 = 2 because _____.
    c. log₄ 4 = 1 because _____.
    d. log₃(3ⁿ) = n because _____.
    e. log₄ 1 = 0 because _____.

18. Find exact values for each of the following quantities. Do not use a calculator.
    a. log₃ 81
    b. log₂ 1024
    c. log₃ 27
    d. log₂(1/8)
    e. log₁₀ 10
    f. log₃(1/27)
    g. log₂(2ᵏ)

19. Use the definition of logarithm to prove that for any positive real number b with b ≠ 1, log_b b = 1.

20. Use the definition of logarithm to prove that for any positive real number b with b ≠ 1, log_b 1 = 0.

21. If b is any positive real number with b ≠ 1 and x is any real number, b⁻ˣ is defined as follows: b⁻ˣ = 1/bˣ. Use this definition and the definition of logarithm to prove that log_b(1/u) = -log_b(u) for all positive real numbers u and b, with b ≠ 1.

22. Use the unique factorization for the integers theorem (Section 4.3) and the definition of logarithm to prove that log₃(7) is irrational.

23. If b and y are positive real numbers such that log_b y = 3, what is log_{1/b}(y)? Why?

24. If b and y are positive real numbers such that log_b y = 2, what is log_{b²}(y)? Why?

25. Let A = {2, 3, 5} and B = {x, y}. Let p₁ and p₂ be the projections of A × B onto the first and second coordinates. That is, for each pair (a, b) ∈ A × B, p₁(a, b) = a and p₂(a, b) = b.
    a. Find p₁(2, y) and p₁(5, x). What is the range of p₁?
    b. Find p₂(2, y) and p₂(5, x). What is the range of p₂?

26. Observe that mod and div can be defined as functions from Z_nonneg × Z⁺ to Z. For each ordered pair (n, d) consisting of a nonnegative integer n and a positive integer d, let
    mod(n, d) = n mod d (the nonnegative remainder obtained when n is divided by d).
    div(n, d) = n div d (the integer quotient obtained when n is divided by d).

    Find each of the following:
    a. mod(67, 10) and div(67, 10)
    b. mod(59, 8) and div(59, 8)
    c. mod(30, 5) and div(30, 5)

27. Let S be the set of all strings of a's and b's.
    a. Define f: S → Z as follows: For each string s in S,
       f(s) = the number of b's to the left of the left-most a in s, or 0 if s contains no a's.
       Find f(aba), f(bbab) and f(b). What is the range of f?
    b. Define g: S → S as follows: For each string s in S,
       g(s) = the string obtained by writing the characters of s in reverse order.
       Find g(aba), g(bbab), and g(b). What is the range of g?

28. Consider the coding and decoding functions E and D defined in Example 7.1.9.
    a. Find E(0110) and D(111111000111).
    b. Find E(1010) and D(000000111111).

29. Consider the Hamming distance function defined in Example 7.1.10.
    a. Find H(10101, 00011)
    b. Find H(00110, 10111)

30. Draw arrow diagrams for the Boolean functions defined by the following input/output tables.
    a.
    ```
    Input | Output
    P  Q  R | S
    --------|----
    1  1  1 | 1
    1  1  0 | 1
    1  0  1 | 0
    1  0  0 | 0
    0  1  1 | 1
    0  1  0 | 0
    0  0  1 | 0
    0  0  0 | 0
    ```
    b.
    ```
    Input | Output
    P  Q  R | S
    --------|----
    1  1  1 | 1
    1  1  0 | 0
    1  0  1 | 1
    1  0  0 | 1
    0  1  1 | 0
    0  1  0 | 1
    0  0  1 | 0
    0  0  0 | 1
    ```

31. Fill in the following table to show the values of all possible two-place Boolean functions.
    | Input | f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 |
    |-------|--------------------------------------------------|
    | 1 1   |                                                  |
    | 1 0   |                                                  |
    | 0 1   |                                                  |
    | 0 0   |                                                  |

32. Consider the three-place Boolean function f defined by the following rule: For each triple (x₁, x₂, x₃) of 0's and 1's,
    f(x₁, x₂, x₃) = (4x₁ + 3x₂ + 2x₃) mod 2.
    a. Find f(1, 1, 1) and f(0, 0, 1).
    b. Describe f using an input/output table.

33. Student A tries to define a function g: Q → Z by the rule
    g(m/n) = m - n, for all integers m and n with n ≠ 0.
    Student B claims that g is not well defined. Justify student B's claim.

34. Student C tries to define a function h: Q → Q by the rule
    h(m/n) = m²/n, for all integers m and n with n ≠ 0.
    Student D claims that h is not well defined. Justify student D's claim.

35. Let J_5 = {0, 1, 2, 3, 4}. Then J_5 - {0} = {1, 2, 3, 4}. Student A tries to define a function R: J_5 - {0} → J_5 - {0} as follows: For each x ∈ J_5 - {0},
    R(x) is the number y so that (x · y) mod 5 = 1.
    Student B claims that R is not well defined. Who is right: student A or student B? Justify your answer.

36. Let J_4 = {0, 1, 2, 3}. Then J_4 - {0} = {1, 2, 3}. Student C tries to define a function S: J_4 - {0} → J_4 - {0} as follows: For each x ∈ J_4 - {0},
    S(x) is the number y so that (x · y) mod 4 = 1.
    Student F claims that S is not well defined. Who is right: student C or student F? Justify your answer.

37. On certain computers the integer data type goes from -2,147,483,648 through 2,147,483,647. Let S be the set of all integers from -2,147,483,648 through 2,147,483,647. Try to define a function f: S → S by the rule f(n) = n² for each n in S. Is f well defined? Why?

38. Let X = {a, b, c} and Y = {r, s, t, u, v, w}. Define f: X → Y as follows: f(a) = v, f(b) = v, and f(c) = t.
    a. Draw an arrow diagram for f.
    b. Let A = {a, b}, C = {t}, D = {u, v}, and E = {r, s}. Find f(A), f(X), f⁻¹(C), f⁻¹(D), f⁻¹(E), and f⁻¹(Y).

39. Let X = {1, 2, 3, 4} and Y = {a, b, c, d, e}. Define g: X → Y as follows: g(1) = a, g(2) = a, g(3) = a, and g(4) = d.
    a. Draw an arrow diagram for g.
    b. Let A = {2, 3}, C = {a}, and D = {b, c}. Find g(A), g(X), g⁻¹(C), g⁻¹(D), and g⁻¹(Y).

40. Let X and Y be sets, let A and B be any subsets of X, and let F be a function from X to Y. Fill in the blanks in the following proof that F(A) ∪ F(B) ⊆ F(A ∪ B).
    **Proof:** Let y be any element in F(A) ∪ F(B). [We must show that y is in F(A ∪ B).] By definition of union, (a) ___.
    **Case 1**, y ∈ F(A): In this case, by definition of F(A), y = F(x) for (b) ___ x ∈ A. Since A ⊆ A ∪ B, it follows from the definition of union that x ∈ (c) ___. Hence, y = F(x) for some x ∈ A ∪ B, and thus, by definition of F(A ∪ B), y ∈ (d) ___.
    **Case 2**, y ∈ F(B): In this case, by definition of F(B), (e) ___ x ∈ B. Since B ⊆ A ∪ B it follows from the definition of union that (f) ___.
    Therefore, regardless of whether y ∈ F(A) or y ∈ F(B), we have that y ∈ F(A ∪ B) [as was to be shown].

41-49. Let X and Y be sets, let A and B be any subsets of X, and let C and D be any subsets of Y. Determine which of the properties are true for all functions F from X to Y and which are false for at least one function F from X to Y. Justify your answers.
    41. If A ⊆ B then F(A) ⊆ F(B).
    42. F(A ∩ B) ⊆ F(A) ∩ F(B)
    43. F(A) ∩ F(B) ⊆ F(A ∩ B)
    44. For all subsets A and B of X, F(A - B) = F(A) - F(B).
    45. For all subsets C and D of Y, if C ⊆ D, then F⁻¹(C) ⊆ F⁻¹(D).
    46. For all subsets C and D of Y, F⁻¹(C ∪ D) = F⁻¹(C) ∪ F⁻¹(D).
    47. For all subsets C and D of Y, F⁻¹(C ∩ D) = F⁻¹(C) ∩ F⁻¹(D).
    48. For all subsets C and D of Y, F⁻¹(C - D) = F⁻¹(C) - F⁻¹(D).
    49. F(F⁻¹(C)) ⊆ C

50. Given a set S and a subset A, the characteristic function of A, denoted χ_A, is the function defined from S to Z with the property that for all u ∈ S,
    χ_A(u) = 1 if u ∈ A
           0 if u ∉ A.
    Show that each of the following holds for all subsets A and B of S and all u ∈ S.
    a. χ_A∩B(u) = χ_A(u) · χ_B(u)
    b. χ_A∪B(u) = χ_A(u) + χ_B(u) - χ_A(u) · χ_B(u)

51-53. Each of exercises 51–53 refers to the Euler phi function, denoted φ, which is defined as follows: For each integer n ≥ 1, φ(n) is the number of positive integers less than or equal to n that have no common factors with n except ±1. For example, φ(10) = 4 because there are four positive integers less than or equal to 10 that have no common factors with 10 except ±1; namely, 1, 3, 7, and 9.

51. Find each of the following:
    a. φ(15)
    b. φ(2)
    c. φ(5)
    d. φ(12)
    e. φ(11)
    f. φ(1)

52. Prove that if p is a prime number and n is an integer with n ≥ 1, then φ(pⁿ) = pⁿ - pⁿ⁻¹.

53. Prove that there are infinitely many integers n for which φ(n) is a perfect square.

---

**Answers for Test Yourself**

1. the unique output element in Y that is related to x by f
2. the value of f at x; the image of x under f; the output of f for the input x
3. the set of all y in Y such that f(x) = y for some x in X
4. an inverse image of y under f; a preimage of y
5. {x ∈ X | f(x) = y}; the inverse image of y
6. f(x) = g(x) for all x ∈ X
7. the exponent to which b must be raised to obtain x (Or: the real number y such that x = b^y)
8. {y ∈ Y | y = f(x) for some x ∈ A} (Or: {f(x) | x ∈ A})
9. {x ∈ X | f(x) ∈ C}

## 7.2 One-to-One and Onto, Inverse Functions

**Page 397**

> Don't accept a statement just because it is printed. — Anna Pell Wheeler, 1883–1966

In this section we discuss two important properties that functions may satisfy: the property of being one-to-one and the property of being onto. Functions that satisfy both properties are called one-to-one correspondences or one-to-one onto functions. When a function is a one-to-one correspondence, the elements of its domain and co-domain match up perfectly, and we can define an inverse function from the co-domain to the domain that "undoes" the action of the function.

### One-to-One Functions

In Section 7.1 we noted that a function may send several elements of its domain to the same element of its co-domain. In terms of arrow diagrams, this means that two or more arrows that start in the domain can point to the same element in the co-domain. On the other hand, if no two arrows that start in the domain point to the same element of the co-domain then the function is called one-to-one or injective. For a one-to-one function, each element of the range is the image of at most one element of the domain.

### Definition: One-to-One Function

Let F be a function from a set X to a set Y. F is one-to-one (or injective) if, and only if, for all elements x₁ and x₂ in X,
if F(x₁) = F(x₂), then x₁ = x₂,
or, equivalently,
if x₁ ≠ x₂, then F(x₁) ≠ F(x₂).

Symbolically,
F: X → Y is one-to-one ⇔ ∀x₁, x₂ ∈ X, if F(x₁) = F(x₂) then x₁ = x₂.

To obtain a precise statement of what it means for a function not to be one-to-one, take the negation of one of the equivalent versions of the definition above. Thus:

A function F: X → Y is not one-to-one ⇔ ∃ elements x₁ and x₂ in X with F(x₁) = F(x₂) and x₁ ≠ x₂.

That is, if elements x₁ and x₂ can be found that have the same function value but are not equal, then F is not one-to-one.

In terms of arrow diagrams, a one-to-one function can be thought of as a function that separates points. That is, it takes distinct points of the domain to distinct points of the co-domain. A function that is not one-to-one fails to separate points. That is, at least two points of the domain are taken to the same point of the co-domain. This is illustrated in Figure 7.2.1 on the next page.