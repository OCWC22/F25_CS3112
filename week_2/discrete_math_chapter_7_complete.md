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
In terms of arrow diagrams, a one-to-one function can be thought of as a function that separates points. That is, it takes distinct points of the domain to distinct points of the co-domain. A function that is not one-to-one fails to separate points. That is, at least two points of the domain are taken to the same point of the co-domain. This is illustrated in Figure 7.2.1.

---

## 7.2 One-to-One and Onto, Inverse Functions

**Page 425-444**

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

In terms of arrow diagrams, a one-to-one function can be thought of as a function that separates points. That is, it takes distinct points of the domain to distinct points of the co-domain. A function that is not one-to-one fails to separate points. That is, at least two points of the domain are taken to the same point of the co-domain.

### Example 7.2.1 Identifying One-to-One Functions Defined on Finite Sets

a. Do either of the arrow diagrams in Figure 7.2.2 define one-to-one functions?

```
Domain of F   X         F         Co-domain of F   Y
                         a ----> 1
                         b ----> 2
                         c ----> 3
                         d ----> 4
                                 5

Domain of G   X         G         Co-domain of G   Y
a ----> 1
b ----> 2
c ----> 2
      ----> 3
              4
```

**Solution:** F is one-to-one but G is not. F is one-to-one because no two different elements of X are sent by F to the same element of Y. G is not one-to-one because the elements a and c are both sent by G to the same element of Y: G(a) = G(c) = w but a ≠ c.

b. Let X = {1, 2, 3} and Y = {a, b, c, d}. Define H: X → Y as follows: H(1) = c, H(2) = a, and H(3) = d. Define K: X → Y as follows: K(1) = d, K(2) = b, and K(3) = d. Is either H or K one-to-one?

**Solution:** H is one-to-one but K is not. H is one-to-one because each of the three elements of the domain of H is sent by H to a different element of the co-domain: H(1) ≠ H(2), H(1) ≠ H(3), and H(2) ≠ H(3). K, however, is not one-to-one because K(1) = K(3) = d but 1 ≠ 3.

### Example 7.2.2 Proving or Disproving That Functions Are One-to-One

Define f: R → R and g: Z → Z by the rules
f(x) = 4x - 1 for all x ∈ R
g(n) = n² for all n ∈ Z

a. Is f one-to-one? Prove or give a counterexample.
b. Is g one-to-one? Prove or give a counterexample.

**Solution:**
a. The function f: R → R is one-to-one.
**Proof:** Suppose x₁ and x₂ are real numbers such that f(x₁) = f(x₂). [We must show that x₁ = x₂.] By definition of f,
4x₁ - 1 = 4x₂ - 1.
Adding 1 to both sides gives 4x₁ = 4x₂, and dividing both sides by 4 gives x₁ = x₂, which is what was to be shown.

b. The function g: Z → Z is not one-to-one.
**Counterexample:** Let n₁ = 2 and n₂ = -2. Then by definition of g,
g(n₁) = g(2) = 2² = 4 and also g(n₂) = g(-2) = (-2)² = 4.
Hence g(n₁) = g(n₂) but n₁ ≠ n₂, and so g is not one-to-one.

### Application: Hash Functions

Imagine a set of student records, each of which includes the student's social security number, and suppose the records are to be stored in a table in which a record can be located if the social security number is known. One way to do this would be to place the record with social security number n into position n of the table. However, since social security numbers have nine digits, this method would require a table with 999,999,999 positions. The problem is that creating such a table for a small set of records would be very wasteful of computer memory space. Hash functions are functions defined from larger to smaller sets of integers, frequently using the mod function, which provide part of the solution to this problem.

### Example 7.2.3 A Hash Function

Suppose there are no more than seven student records. Define a function Hash from the set of all social security numbers (ignoring hyphens) to the set {0, 1, 2, 3, 4, 5, 6} as follows:
Hash(n) = n mod 7 for all social security numbers n.

```
Table 7.2.1
0 | 356-63-3102
1 |
2 | 513-40-8716
3 | 223-79-9061
4 |
5 | 328-34-3419
6 |
```

To use your calculator to find n mod 7, use the formula n mod 7 = n - 7 · (n div 7). For instance, since 328343419/7 = 46906202.71...,
Hash(328-34-3419) = 328343419 - (7 · 46906202) = 5.

**Problem:** Suppose the social security number for another record to be stored is 908-37-1011. Find the position in Table 7.2.1 into which this record would be placed.

**Solution:** When you compute Hash you find that Hash(908-37-1011) = 2, which is already occupied by the record with social security number 513-40-8716. Searching downward from position 2, you find that position 3 is also occupied but position 4 is free. Therefore, you place the record with social security number 908-37-1011 into position 4.

### Onto Functions

It was noted in Section 7.1 that there may be an element of the co-domain of a function that is not the image of any element in the domain. On the other hand, every element of a function's co-domain may be the image of some element of its domain. Such a function is called onto or surjective. When a function is onto, its range is equal to its co-domain.

### Definition: Onto Function

Let F be a function from a set X to a set Y. F is onto (or surjective) if, and only if, given any element y in Y, it is possible to find an element x in X with the property that y = F(x).

Symbolically:
F: X → Y is onto ⇔ ∀y ∈ Y, ∃x ∈ X such that F(x) = y.

To obtain a precise statement of what it means for a function not to be onto, take the negation of the definition of onto:
F: X → Y is not onto ⇔ ∃y in Y such that ∀x ∈ X, F(x) ≠ y.
That is, there is some element in Y that is not the image of any element in X.

### Example 7.2.4 Identifying Onto Functions Defined on Finite Sets

a. Do either of the arrow diagrams in Figure 7.2.4 define onto functions?

```
Domain of F   X         F         Co-domain of F   Y
a ----> 1
b ----> 2
c ----> 3
d ----> 4
              5

Domain of G   X         G         Co-domain of G   Y
              a ----> 1
              b ----> 2
              c ----> 3
              d ----> 4
                      5
```

**Solution:** F is not onto because b ≠ F(x) for any x in X. G is onto because each element of Y equals G(x) for some x in X: a = G(3), b = G(1), c = G(2) = G(4), and d = G(5).

b. Let X = {1, 2, 3, 4} and Y = {a, b, c}. Define H: X → Y as follows: H(1) = c, H(2) = a, H(3) = c, H(4) = b. Define K: X → Y as follows: K(1) = c, K(2) = b, K(3) = b, and K(4) = c. Is either H or K onto?

**Solution:** H is onto but K is not. H is onto because each of the three elements of the co-domain of H is the image of some element of the domain of H: a = H(2), b = H(4), and c = H(1) = H(3). K, however, is not onto because a ≠ K(x) for any x in {1, 2, 3, 4}.

### Example 7.2.5 Proving or Disproving That Functions Are Onto

Define f: R → R and h: Z → Z by the rules
f(x) = 4x - 1 for all x ∈ R
h(n) = 4n - 1 for all n ∈ Z

a. Is f onto? Prove or give a counterexample.
b. Is h onto? Prove or give a counterexample.

**Solution:**
a. The function f: R → R is onto.
**Proof:** Let y ∈ R. [We must show that ∃x in R such that f(x) = y.] Let x = (y + 1)/4. Then x is a real number since sums and quotients (other than by 0) of real numbers are real numbers. It follows that
f(x) = f((y + 1)/4) = 4 · ((y + 1)/4) - 1 = (y + 1) - 1 = y
[This is what was to be shown.]

b. The function h: Z → Z is not onto.
**Counterexample:** The co-domain of h is Z and 0 ∈ Z. But h(n) ≠ 0 for any integer n. For if h(n) = 0, then 4n - 1 = 0, which implies that 4n = 1 and so n = 1/4. But 1/4 is not an integer. Hence there is no integer n for which h(n) = 0, and thus h is not onto.

### Relations between Exponential and Logarithmic Functions

For positive numbers b ≠ 1, the exponential function with base b, denoted exp_b, is the function from R to R⁺ defined as follows: For all real numbers x,
exp_b(x) = b^x
where b⁰ = 1 and b⁻ˣ = 1/b^x.

**Laws of Exponents:**
If b and c are any positive real numbers and u and v are any real numbers, the following laws of exponents hold true:
1. b^u b^v = b^(u+v)
2. (b^u)^v = b^(uv)
3. b^u/b^v = b^(u-v)
4. (bc)^u = b^u c^u

For any positive real number b with b ≠ 1:
- If b^u = b^v then u = v for all real numbers u and v
- If log_b u = log_b v then u = v for all positive real numbers u and v

### Theorem 7.2.1 Properties of Logarithms

For any positive real numbers b, c and x with b ≠ 1 and c ≠ 1:
a. log_b(xy) = log_b x + log_b y
b. log_b(x/y) = log_b x - log_b y
c. log_b(x^a) = a log_b x
d. log_c x = log_b x / log_b c

### Example 7.2.6 Using the One-to-Oneness of the Exponential Function

Use the definition of logarithm, the laws of exponents, and the one-to-oneness of the exponential function to prove part (d) of Theorem 7.2.1: For any positive real numbers b, c, and x, with b ≠ 1 and c ≠ 1,
log_c x = log_b x / log_b c

**Proof:** Suppose positive real numbers b, c, and x are given. Let
(1) u = log_b c
(2) v = log_c x
(3) w = log_b x

Then, by definition of logarithm,
(1') c = b^u
(2') x = c^v
(3') x = b^w

Substituting (1') into (2') and using one of the laws of exponents gives
x = c^v = (b^u)^v = b^(uv)

But by (3'), x = b^w also. Hence b^(uv) = b^w, and so by the one-to-oneness of the exponential function, uv = w. Substituting from (1), (2), and (3) gives that (log_b c)(log_c x) = log_b x. And dividing both sides by log_b c (which is nonzero because c ≠ 1) results in log_c x = log_b x / log_b c.

### Example 7.2.7 Computing Logarithms with Base 2 on a Calculator

In computer science it is often necessary to compute logarithms with base 2. Most calculators do not have keys to compute logarithms with base 2 but do have keys to compute logarithms with base 10 (called common logarithms and often denoted simply log) and logarithms with base e (called natural logarithms and usually denoted ln). Suppose your calculator shows that ln 5 ≅ 1.609437912 and ln 2 ≅ 0.6931471806. Use Theorem 7.2.1(d) to find an approximate value for log₂ 5.

**Solution:** By Theorem 7.2.1(d),
log₂ 5 = ln 5 / ln 2 ≅ 1.609437912 / 0.6931471806 ≅ 2.321928095.

### One-to-One Correspondences

Consider a function F: X → Y that is both one-to-one and onto. Given any element x in X, there is a unique corresponding element y = F(x) in Y (since F is a function). Also given any element y in Y, there is an element x in X such that F(x) = y (since F is onto) and there is only one such x (since F is one-to-one). Thus, a function that is one-to-one and onto sets up a pairing between the elements of X and the elements of Y that matches each element of X with exactly one element of Y and each element of Y with exactly one element of X. Such a pairing is called a one-to-one correspondence or bijection.

### Definition: One-to-One Correspondence

A one-to-one correspondence (or bijection) from a set X to a set Y is a function F: X → Y that is both one-to-one and onto.

### Example 7.2.8 A Function from a Power Set to a Set of Strings

Let P({a, b}) be the set of all subsets of {a, b} and let S be the set of all strings of length 2 made up of 0's and 1's. Then P({a, b}) = {∅, {a}, {b}, {a, b}} and S = {00, 01, 10, 11}. Define a function h from P({a, b}) to S as follows: Given any subset A of {a, b}, a is either in A or not in A, and b is either in A or not in A. If a is in A, write a 1 in the first position of the string h(A). If a is not in A, write a 0 in the first position of the string h(A). Similarly, if b is in A, write a 1 in the second position of the string h(A). If b is not in A, write a 0 in the second position of the string h(A).

```
h       Subset       Status of a   Status of b   String
        ∅           not in        not in        00
        {a}         in            not in        10
        {b}         not in        in            01
        {a, b}      in            in            11
```

Is h a one-to-one correspondence?

**Solution:** The arrow diagram shows clearly that h is a one-to-one correspondence. It is onto because each element of S has an arrow pointing to it. It is one-to-one because each element of S has no more than one arrow pointing to it.

### Example 7.2.9 A String-Reversing Function

Let T be the set of all finite strings of x's and y's. Define g: T → T by the rule:
For all strings s ∈ T, g(s) = the string obtained by writing the characters of s in reverse order.

Is g a one-to-one correspondence from T to itself?

**Solution:** The answer is yes. To show that g is a one-to-one correspondence, it is necessary to show that g is one-to-one and onto.

**Proof that g is one-to-one:** Suppose that for some strings s₁ and s₂ in T, g(s₁) = g(s₂). [We must show that s₁ = s₂.] Now to say that g(s₁) = g(s₂) is the same as saying that the string obtained by writing the characters of s₁ in reverse order equals the string obtained by writing the characters of s₂ in reverse order. But if s₁ and s₂ are equal when written in reverse order, then they must be equal to start with. In other words, s₁ = s₂ [as was to be shown].

**Proof that g is onto:** Suppose t is a string in T. [We must find a string s in T such that g(s) = t.] Let s = g(t). By definition of g, s = g(t) is the string in T obtained by writing the characters of t in reverse order. But when the order of the characters of a string is reversed once and then reversed again, the original string is recovered. Thus g(s) = g(g(t)) = the string obtained by writing the characters of t in reverse order and then writing those characters in reverse order again = t. [This is what was to be shown.]

### Example 7.2.10 A Function of Two Variables

Define a function F: R × R → R × R as follows: For all (x, y) ∈ R × R,
F(x, y) = (x + y, x - y).

Is F a one-to-one correspondence from R × R to itself?

**Solution:** The answer is yes. To show that F is a one-to-one correspondence, you need to show both that F is one-to-one and that F is onto.

**Proof that F is one-to-one:** Suppose that (x₁, y₁) and (x₂, y₂) are any ordered pairs in R × R such that F(x₁, y₁) = F(x₂, y₂). [We must show that (x₁, y₁) = (x₂, y₂).] By definition of F, (x₁ + y₁, x₁ - y₁) = (x₂ + y₂, x₂ - y₂). For two ordered pairs to be equal, both the first and second components must be equal. Thus x₁, y₁, x₂, and y₂ satisfy the following system of equations:
x₁ + y₁ = x₂ + y₂  (1)
x₁ - y₁ = x₂ - y₂  (2)

Adding equations (1) and (2) gives that 2x₁ = 2x₂, and so x₁ = x₂. Substituting x₁ = x₂ into equation (1) yields x₁ + y₁ = x₁ + y₂, and so y₁ = y₂. Thus, by definition of equality of ordered pairs, (x₁, y₁) = (x₂, y₂) [as was to be shown].

**Proof that F is onto:** Suppose (u, v) is any ordered pair in the co-domain of F. [We will show that there is an ordered pair in the domain of F that is sent to (u, v) by F.] Let r = (u + v)/2 and s = (u - v)/2. Then (r, s) is an ordered pair of real numbers and so is in the domain of F. In addition:
F(r, s) = F((u + v)/2, (u - v)/2) = ((u + v)/2 + (u - v)/2, (u + v)/2 - (u - v)/2) = ((2u)/2, (2v)/2) = (u, v) [This is what was to be shown.]

### Inverse Functions

If F is a one-to-one correspondence from a set X to a set Y, then there is a function from Y to X that "undoes" the action of F; that is, it sends each element of Y back to the element of X that it came from. This function is called the inverse function for F.

### Theorem 7.2.2

Suppose F: X → Y is a one-to-one correspondence; that is, suppose F is one-to-one and onto. Then there is a function F⁻¹: Y → X that is defined as follows:
Given any element y in Y, F⁻¹(y) = that unique element x in X such that F(x) equals y.
In other words, F⁻¹(y) = x ⇔ y = F(x).

### Definition: Inverse Function

The function F⁻¹ of Theorem 7.2.2 is called the inverse function for F.

### Example 7.2.11 Finding an Inverse Function for a Function Given by an Arrow Diagram

Define the inverse function for the one-to-one correspondence h given in Example 7.2.8.

The arrow diagram for h⁻¹ is obtained by tracing the h-arrows back from S to P({a, b}):

```
P({a, b})        h⁻¹        S
∅ ----------------> 00
{a} --------------> 10
{b} --------------> 01
{a, b} -----------> 11
```

h⁻¹(00) = ∅, h⁻¹(10) = {a}, h⁻¹(01) = {b}, h⁻¹(11) = {a, b}

### Example 7.2.12 Finding an Inverse Function for a Function Given in Words

Define the inverse function for the one-to-one correspondence g given in Example 7.2.9.

**Solution:** The function g: T → T is defined by the rule: For all strings t in T, g(t) = the string obtained by writing the characters of t in reverse order.

Now if the characters of t are written in reverse order and then written in reverse order again, the original string is recovered. Thus given any string t in T, g⁻¹(t) = the unique string that, when written in reverse order, equals t = the string obtained by writing the characters of t in reverse order = g(t). Hence g⁻¹: T → T is the same as g, or, in other words, g⁻¹ = g.

### Example 7.2.13 Finding an Inverse Function for a Function Given by a Formula

The function f: R → R defined by the formula f(x) = 4x - 1 for all real numbers x was shown to be one-to-one in Example 7.2.2 and onto in Example 7.2.5. Find its inverse function.

**Solution:** For any y in R, by definition of f⁻¹, f⁻¹(y) = that unique real number x such that f(x) = y. But f(x) = y ⇔ 4x - 1 = y ⇔ x = (y + 1)/4. Hence f⁻¹(y) = (y + 1)/4.

### Theorem 7.2.3

If X and Y are sets and F: X → Y is one-to-one and onto, then F⁻¹: Y → X is also one-to-one and onto.

**Proof:**
- F⁻¹ is one-to-one: Suppose y₁ and y₂ are elements of Y such that F⁻¹(y₁) = F⁻¹(y₂). [We must show that y₁ = y₂.] Let x = F⁻¹(y₁) = F⁻¹(y₂). Then x ∈ X, and by definition of F⁻¹, F(x) = y₁ since x = F⁻¹(y₁) and F(x) = y₂ since x = F⁻¹(y₂). Consequently, y₁ = y₂ since each is equal to F(x). This is what was to be shown.
- F⁻¹ is onto: Suppose x ∈ X. [We must show that there exists an element y in Y such that F⁻¹(y) = x.] Let y = F(x). Then y ∈ Y, and by definition of F⁻¹, F⁻¹(y) = x. This is what was to be shown.

### Example 7.2.14 Finding an Inverse Function for a Function of Two Variables

Define the inverse function F⁻¹: R × R → R × R for the one-to-one correspondence given in Example 7.2.10.

**Solution:** The solution to Example 7.2.10 shows that F((u + v)/2, (u - v)/2) = (u, v). Because F is one-to-one, this means that ((u + v)/2, (u - v)/2) is the unique ordered pair in the domain of F that is sent to (u, v) by F. Thus, F⁻¹ is defined as follows: For all (u, v) ∈ R × R, F⁻¹(u, v) = ((u + v)/2, (u - v)/2).

---

### Test Yourself

1. If F is a function from a set X to a set Y, then F is one-to-one if, and only if, _____.
2. If F is a function from a set X to a set Y, then F is not one-to-one if, and only if, _____.
3. If F is a function from a set X to a set Y, then F is onto if, and only if, _____.
4. If F is a function from a set X to a set Y, then F is not onto if, and only if, _____.
5. The following two statements are _____:
   ∀u, v ∈ U, if H(u) = H(v) then u = v.
   ∀u, v ∈ U, if u ≠ v then H(u) ≠ H(v).
6. Given a function F: X → Y and an infinite set X, to prove that F is one-to-one, you suppose that _____ and then you show that _____.
7. Given a function F: X → Y and an infinite set X, to prove that F is onto, you suppose that _____ and then you show that _____.
8. Given a function F: X → Y, to prove that F is not one-to-one, you _____.
9. Given a function F: X → Y, to prove that F is not onto, you _____.
10. A one-to-one correspondence from a set X to a set Y is a _____ that is _____.
11. If F is a one-to-one correspondence from a set X to a set Y and y is in Y, then F⁻¹(y) is _____.

---

### Exercise Set 7.2

1. The definition of one-to-one is stated in two ways:
   ∀x₁, x₂ ∈ X, if F(x₁) = F(x₂) then x₁ = x₂
   and
   ∀x₁, x₂ ∈ X, if x₁ ≠ x₂ then F(x₁) ≠ F(x₂).
   Why are these two statements logically equivalent?

2. Fill in each blank with the word most or least.
   a. A function F is one-to-one if, and only if, each element in the co-domain of F is the image of at _____ one element in the domain of F.
   b. A function F is onto if, and only if, each element in the co-domain of F is the image of at _____ one element in the domain of F.

3. When asked to state the definition of one-to-one, a student replies, "A function f is one-to-one if, and only if, every element of X is sent by f to exactly one element of Y." Give a counterexample to show that the student's reply is incorrect.

4. Let f: X → Y be a function. True or false? A sufficient condition for f to be one-to-one is that for all elements y in Y, there is at most one x in X with f(x) = y.

5. All but two of the following statements are correct ways to express the fact that a function f is onto. Find the two that are incorrect.
   a. f is onto ⇔ every element in its co-domain is the image of some element in its domain.
   b. f is onto ⇔ every element in its domain has a corresponding image in its co-domain.
   c. f is onto ⇔ ∀y ∈ Y, ∃x ∈ X such that f(x) = y.
   d. f is onto ⇔ ∀x ∈ X, ∃y ∈ Y such that f(x) = y.
   e. f is onto ⇔ the range of f is the same as the co-domain of f.

6. Let X = {1, 5, 9} and Y = {3, 4, 7}.
   a. Define f: X → Y by specifying that f(1) = 4, f(5) = 7, f(9) = 4. Is f one-to-one? Is f onto? Explain your answers.
   b. Define g: X → Y by specifying that g(1) = 7, g(5) = 3, g(9) = 4. Is g one-to-one? Is g onto? Explain your answers.

7. Let X = {a, b, c, d} and Y = {e, f, g}. Define functions F and G by the arrow diagrams below.
   ```
   Domain of F   X         F         Co-domain of F   Y
   a ----> e
   b ----> f
   c ----> g
   d ----> f

   Domain of G   X         G         Co-domain of G   Y
   a ----> e
   b ----> f
   c ----> g
   d ----> e
   ```
   a. Is F one-to-one? Why or why not? Is it onto? Why or why not?
   b. Is G one-to-one? Why or why not? Is it onto? Why or why not?

8. Let X = {a, b, c} and Y = {w, x, y, z}. Define functions H and K by the arrow diagrams below.
   ```
   Domain of H   X         H         Co-domain of H   Y
   a ----> w
   b ----> x
   c ----> y

   Domain of K   X         K         Co-domain of K   Y
   a ----> w
   b ----> x
   c ----> y
              z
   ```
   a. Is H one-to-one? Why or why not? Is it onto? Why or why not?
   b. Is K one-to-one? Why or why not? Is it onto? Why or why not?

9. Let X = {1, 2, 3}, Y = {1, 2, 3, 4}, and Z = {1, 2}.
   a. Define a function f: X → Y that is one-to-one but not onto.
   b. Define a function g: X → Z that is onto but not one-to-one.
   c. Define a function h: X → X that is neither one-to-one nor onto.
   d. Define a function k: X → X that is one-to-one and onto but is not the identity function on X.

10. a. Define f: Z → Z by the rule f(n) = 2n, for all integers n.
    (i) Is f one-to-one? Prove or give a counterexample.
    (ii) Is f onto? Prove or give a counterexample.
    b. Let 2Z denote the set of all even integers. That is, 2Z = {n ∈ Z | n = 2k, for some integer k}. Define h: Z → 2Z by the rule h(n) = 2n, for all integers n. Is h onto? Prove or give a counterexample.

11. a. Define g: Z → Z by the rule g(n) = 4n - 5, for all integers n.
    (i) Is g one-to-one? Prove or give a counterexample.
    (ii) Is g onto? Prove or give a counterexample.
    b. Define G: R → R by the rule G(x) = 4x - 5 for all real numbers x. Is G onto? Prove or give a counterexample.

12. a. Define F: Z → Z by the rule F(n) = 2 - 3n, for all integers n.
    (i) Is F one-to-one? Prove or give a counterexample.
    (ii) Is F onto? Prove or give a counterexample.
    b. Define G: R → R by the rule G(x) = 2 - 3x for all real numbers x. Is G onto? Prove or give a counterexample.

13. a. Define H: R → R by the rule H(x) = x², for all real numbers x.
    (i) Is H one-to-one? Prove or give a counterexample.
    (ii) Is H onto? Prove or give a counterexample.
    b. Define K: R_nonneg → R_nonneg by the rule K(x) = x², for all nonnegative real numbers x. Is K onto? Prove or give a counterexample.

14. Explain the mistake in the following "proof."
    **Theorem:** The function f: Z → Z defined by the formula f(n) = 4n + 3, for all integers n, is one-to-one.
    **"Proof":** Suppose any integer n is given. Then by definition of f, there is only one possible value for f(n), namely, 4n + 3. Hence f is one-to-one.

15-18. In each of these exercises, a function f is defined on a set of real numbers. Determine whether or not f is one-to-one and justify your answer.
    15. f(x) = (x + 1)/x, for all real numbers x ≠ 0
    16. f(x) = x²/(x + 1), for all real numbers x ≠ -1
    17. f(x) = (3x - 1)/x, for all real numbers x ≠ 0
    18. f(x) = (x + 1)/(x - 1), for all real numbers x ≠ 1

19. Referring to Example 7.2.3, assume that records with the following social security numbers are to be placed in sequence into Table 7.2.1. Find the position into which each record is placed.
    a. 417-30-2072
    b. 364-98-1703
    c. 283-09-0787

20. Define Floor: R → Z by the formula Floor(x) = ⌊x⌋, for all real numbers x.
    a. Is Floor one-to-one? Prove or give a counterexample.
    b. Is Floor onto? Prove or give a counterexample.

21. Let S be the set of all strings of 0's and 1's, and define l: S → Z_nonneg by l(s) = the length of s, for all strings s in S.
    a. Is l one-to-one? Prove or give a counterexample.
    b. Is l onto? Prove or give a counterexample.

22. Let S be the set of all strings of 0's and 1's, and define D: S → Z as follows: For all s ∈ S, D(s) = the number of 1's in s minus the number of 0's in s.
    a. Is D one-to-one? Prove or give a counterexample.
    b. Is D onto? Prove or give a counterexample.

23. Define F: P({a, b, c}) → Z as follows: For all A in P({a, b, c}), F(A) = the number of elements in A.
    a. Is F one-to-one? Prove or give a counterexample.
    b. Is F onto? Prove or give a counterexample.

24. Let S be the set of all strings of a's and b's, and define N: S → Z by N(s) = the number of a's in s, for all s ∈ S.
    a. Is N one-to-one? Prove or give a counterexample.
    b. Is N onto? Prove or give a counterexample.

25. Let S be the set of all strings in a's and b's, and define C: S → S by C(s) = as, for all s ∈ S. (C is called concatenation by a on the left.)
    a. Is C one-to-one? Prove or give a counterexample.
    b. Is C onto? Prove or give a counterexample.

26. Define S: Z⁺ → Z⁺ by the rule: For all integers n, S(n) = the sum of the positive divisors of n.
    a. Is S one-to-one? Prove or give a counterexample.
    b. Is S onto? Prove or give a counterexample.

27. Let D be the set of all finite subsets of positive integers, and define T: Z⁺ → D by the rule: For all integers n, T(n) = the set of all of the positive divisors of n.
    a. Is T one-to-one? Prove or give a counterexample.
    b. Is T onto? Prove or give a counterexample.

28. Define G: R × R → R × R as follows: G(x, y) = (2y, -x) for all (x, y) ∈ R × R.
    a. Is G one-to-one? Prove or give a counterexample.
    b. Is G onto? Prove or give a counterexample.

29. Define H: R × R → R × R as follows: H(x, y) = (x + 1, 2 - y) for all (x, y) ∈ R × R.
    a. Is H one-to-one? Prove or give a counterexample.
    b. Is H onto? Prove or give a counterexample.

30. Define J: Q × Q → R by the rule J(r, s) = r + √2s for all (r, s) ∈ Q × Q.
    a. Is J one-to-one? Prove or give a counterexample.
    b. Is J onto? Prove or give a counterexample.

31. Define F: Z⁺ × Z⁺ → Z⁺ and G: Z⁺ × Z⁺ → Z⁺ as follows: For all (n, m) ∈ Z⁺ × Z⁺, F(n, m) = 3ⁿ5ᵐ and G(n, m) = 3ⁿ6ᵐ.
    a. Is F one-to-one? Prove or give a counterexample.
    b. Is G one-to-one? Prove or give a counterexample.

32. a. Is log₈ 27 = log₂ 3? Why or why not?
    b. Is log₁₆ 9 = log₄ 3? Why or why not?

33-35. The properties of logarithm established in these exercises are used in Sections 11.4 and 11.5.
    33. Prove that for all positive real numbers b, x, and y with b ≠ 1, log_b(x/y) = log_b x - log_b y.
    34. Prove that for all positive real numbers b, x, and y with b ≠ 1, log_b(xy) = log_b x + log_b y.
    35. Prove that for all real numbers a, b, and x with b and x positive and b ≠ 1, log_b(xᵃ) = a log_b x.

36-37. Exercises 36 and 37 use the following definition: If f: R → R and g: R → R are functions, then the function (f + g): R → R is defined by the formula (f + g)(x) = f(x) + g(x) for all real numbers x.
    36. If f: R → R and g: R → R are both one-to-one, is f + g also one-to-one? Justify your answer.
    37. If f: R → R and g: R → R are both onto, is f + g also onto? Justify your answer.

38-39. Exercises 38 and 39 use the following definition: If f: R → R is a function and c is a nonzero real number, the function (c · f): R → R is defined by the formula (c · f)(x) = c · f(x) for all real numbers x.
    38. Let f: R → R be a function and c a nonzero real number. If f is one-to-one, is c · f also one-to-one? Justify your answer.
    39. Let f: R → R be a function and c a nonzero real number. If f is onto, is c · f also onto? Justify your answer.

40. Suppose F: X → Y is one-to-one.
    a. Prove that for all subsets A ⊆ X, F⁻¹(F(A)) = A.
    b. Prove that for all subsets A₁ and A₂ in X, F(A₁ ∩ A₂) = F(A₁) ∩ F(A₂).

41. Suppose F: X → Y is onto. Prove that for all subsets B ⊆ Y, F(F⁻¹(B)) = B.

42-43. Let X = {a, b, c, d, e} and Y = {s, t, u, v, w}. In each of 42 and 43 a one-to-one correspondence F: X → Y is defined by an arrow diagram. In each case draw an arrow diagram for F⁻¹.
    42. (Diagram showing F mapping X to Y)
    43. (Diagram showing F mapping X to Y)

44-55. Indicate which of the functions in the referenced exercise are one-to-one correspondences. For each function that is a one-to-one correspondence, find the inverse function.
    44. Exercise 10a
    45. Exercise 10b
    46. Exercise 11a
    47. Exercise 11b
    48. Exercise 12a
    49. Exercise 12b
    50. Exercise 21
    51. Exercise 22
    52. Exercise 15 with the co-domain taken to be the set of all real numbers not equal to 1.
    53. Exercise 16 with the co-domain taken to be the set of all real numbers.
    54. Exercise 17 with the co-domain taken to be the set of all real numbers not equal to 3.
    55. Exercise 18 with the co-domain taken to be the set of all real numbers not equal to 1.

56. In Example 7.2.8 a one-to-one correspondence was defined from the power set of {a, b} to the set of all strings of 0's and 1's that have length 2. Thus the elements of these two sets can be matched up exactly, and so the two sets have the same number of elements.
    a. Let X = {x₁, x₂, ..., xₙ} be a set with n elements. Use Example 7.2.8 as a model to define a one-to-one correspondence from P(X), the set of all subsets of X, to the set of all strings of 0's and 1's that have length n.
    b. Use the one-to-one correspondence of part (a) to deduce that a set with n elements has 2ⁿ subsets. (This provides an alternative proof of Theorem 6.3.1.)

57. Write a computer algorithm to check whether a function from one finite set to another is one-to-one. Assume the existence of an independent algorithm to compute values of the function.

58. Write a computer algorithm to check whether a function from one finite set to another is onto. Assume the existence of an independent algorithm to compute values of the function.

---

**Answers for Test Yourself**

1. for all x₁ and x₂ in X, if F(x₁) = F(x₂) then x₁ = x₂
2. there exist elements x₁ and x₂ in X such that F(x₁) = F(x₂) and x₁ ≠ x₂
3. for all y in Y, there exists at least one element x in X such that f(x) = y
4. there exists an element y in Y such that for all elements x in X, f(x) ≠ y
5. logically equivalent ways of expressing what it means for a function H to be one-to-one (The second is the contrapositive of the first.)
6. x₁ and x₂ are any [particular but arbitrarily chosen] elements in X with the property that F(x₁) = F(x₂); x₁ = x₂
7. y is any [particular but arbitrarily chosen] element in Y; there exists at least one element x in X such that F(x) = y
8. show that there are concrete elements x₁ and x₂ in X with the property that F(x₁) = F(x₂) and x₁ ≠ x₂
9. show that there is a concrete element y in Y with the property that F(x) ≠ y for any element x in X
10. function from X to Y; both one-to-one and onto
11. the unique element x in X such that F(x) = y (in other words, F⁻¹(y) is the unique preimage of y in X)