# Chapter 7: Functions (Complete)

**Pages 411-470**

## Introduction

This chapter explores the mathematical concept of functions - one of the most fundamental structures in mathematics and computer science. We begin with basic definitions and properties, then examine special types of functions like one-to-one and onto functions, inverse functions, and function composition. The chapter culminates with an important discussion of cardinality and its applications to computability.

---

## 7.1 Functions Defined on General Sets

**Page 411**

> The desire to economize time and mental effort in arithmetical computations, and to eliminate human liability to error is probably as old as the science of arithmetic itself.
> — Howard Aiken (designer of the Harvard Mark I computer), 1964

In this chapter we give a careful mathematical definition of the term function, and we explain how functions model many phenomena in computer science and other disciplines. We also establish terminology and notation that occur in discussions of functions throughout mathematics and computer science, and we develop skill in using the terminology and notation correctly.

In Section 7.1 we use an arrow diagram to illustrate how to transform the word function into a mathematical object. We then give a formal definition of function in terms of Cartesian products and show how to use it to prove various results about specific functions. In Section 7.2 we define one-to-one and onto and show how to prove that functions do or do not have these properties. We apply the properties of one-to-one and onto to define the inverse of a function in Section 7.3 and to explore composition of functions and its properties. Finally, in Section 7.4, we discuss the meaning of the phrase "the number of elements in a set," and we discover that this simple sounding concept leads to surprising and important results about infinite sets and the nature of computability.

### Definition: Function

Let X and Y be nonempty sets. A **function** f from X to Y, denoted f : X → Y, is a relation from X to Y that satisfies the following two properties:

1. **Every element of X is related to some element of Y.**
2. **No element of X is related to more than one element of Y.**

In other words, a function f from X to Y is a relation from X to Y such that:
- ∀x ∈ X, ∃y ∈ Y such that (x, y) ∈ f
- ∀x ∈ X and ∀y, z ∈ Y, if (x, y) ∈ f and (x, z) ∈ f then y = z

**Page 412**

When we write y = f(x), we say:
- "y is the value of f at x"
- "y is the image of x under f"
- "y is the output of f for the input x"
- "f maps x to y"
- "f transforms x into y"
- "f sends x to y"

A function f from X to Y assigns to each element x ∈ X a unique element y ∈ Y. The element y is denoted f(x), read "f of x." Symbolically we write:

```
x ↦ f(x)    or    f: x ↦ y
```

### Domain, Co-domain, and Range

**Definition:** Let f: X → Y be a function.
- The set X is called the **domain** of f
- The set Y is called the **co-domain** of f
- The set of all values of the function is called the **range** of f:
  ```
  range of f = {y ∈ Y | y = f(x) for some x ∈ X}
  ```

### Arrow Diagrams

**Page 413**

An **arrow diagram** is a visual representation of a function where:
- The domain X and co-domain Y are represented as ovals
- Each element of X has exactly one arrow pointing to an element of Y
- Multiple elements of X may point to the same element of Y
- Some elements of Y may have no arrows pointing to them

### Example 7.1.1: Functions and Relations Given as Sets of Ordered Pairs

Let X = {a, b, c} and Y = {1, 2, 3, 4}. Define:
- f = {(a, 2), (b, 4), (c, 2)}
- g = {(a, 2), (b, 3), (c, 4)}

a. Is f a function from X to Y? Yes - every element of X appears exactly once as a first element.
b. Is g a function from X to Y? Yes - every element of X appears exactly once as a first element.

### Example 7.1.2: Functions and Relations Given by Directed Graphs

**Page 414**

Is the relation represented by each directed graph a function?

a. Domain = {a, b, c}, Co-domain = {x, y, z}
   If element b has two outgoing arrows (to y and z): NOT a function

b. Domain = {a, b, c}, Co-domain = {v, w, x, y, z}
   If each element has exactly one outgoing arrow: YES, it's a function

### Function Machines

**Page 415**

A function can be thought of as a machine that takes an input x and produces a unique output f(x):

```
Input: x → [Function Machine f] → Output: f(x)
```

### Example 7.1.3: Equality of Functions

Let f: R → R and g: R → R be defined by:
```
f(x) = |x|    for all x ∈ R

g(x) = { x     if x ≥ 0
       { -x    if x < 0
```

Does f = g?

**Solution:** Yes. For all x ∈ R:
- If x ≥ 0: g(x) = x = |x| = f(x)
- If x < 0: g(x) = -x = |x| = f(x)

Therefore f(x) = g(x) for all x ∈ R, so f = g.

### Example 7.1.4: The Identity Function

**Page 416**

The **identity function** on a set X, denoted I_X, is defined by:
```
I_X(x) = x    for all x ∈ X
```

For example, if X = {1, 2, 3}:
```
I_X(1) = 1, I_X(2) = 2, I_X(3) = 3
```

### Sequences as Functions

A sequence is a function whose domain is either:
- The set {1, 2, 3, ..., n} for some n ∈ Z⁺
- The set Z⁺ of all positive integers

We write a_n instead of f(n) for the value of the sequence at n.

### Example 7.1.5: Functions Defined by Formulas

**Page 417**

Define f: R → R by the formula:
```
f(x) = x² - 2x + 1
```

Then:
- f(0) = 0² - 2(0) + 1 = 1
- f(1) = 1² - 2(1) + 1 = 0
- f(2) = 2² - 2(2) + 1 = 1
- f(-1) = (-1)² - 2(-1) + 1 = 4

### Example 7.1.6: Functions Defined on Subsets of R

The function g: R - {1} → R defined by:
```
g(x) = x/(x-1)
```

is well-defined because x ≠ 1 for all x in the domain.

### Functions Acting on Sets

**Page 418**

If f: X → Y and A ⊆ X, then:
```
f(A) = {y ∈ Y | y = f(x) for some x ∈ A}
```

This is called the **image of A under f**.

### Example 7.1.7: The Image of a Set

Let f: {1, 2, 3, 4, 5} → {a, b, c, d} be defined by:
```
f(1) = c, f(2) = b, f(3) = a, f(4) = d, f(5) = c
```

Find f({1, 3, 5}).

**Solution:**
```
f({1, 3, 5}) = {f(1), f(3), f(5)} = {c, a, c} = {a, c}
```

### Boolean Functions

**Page 419**

A **Boolean function** is a function whose co-domain is {0, 1}.

### Example 7.1.8: A Boolean Function

Define f: {0, 1}³ → {0, 1} by:
```
f(x₁, x₂, x₃) = (x₁ + x₂ + x₃) mod 2
```

This function outputs 1 if an odd number of inputs are 1, and 0 otherwise.

### Checking Whether a Function Is Well-Defined

**Page 420**

To prove a function is well-defined, show:
1. Every element of the domain is assigned a value
2. No element of the domain is assigned more than one value

For functions defined by formulas, this often means checking that the formula doesn't involve division by zero or other undefined operations.

### Example 7.1.9: A Function That Is Not Well-Defined

Attempting to define h: R → R by h(x) = 1/x fails because h(0) is undefined.

To fix this, we could define h: R - {0} → R by h(x) = 1/x.

---

## 7.2 One-to-One and Onto, Inverse Functions

**Page 421**

> I never did very well in math — I could never seem to persuade the teacher that I hadn't meant my answers literally.
> — Calvin Trillin

Imagine you are the manager of a company that has four employees—Alanis, Ben, Camilla, and Damon—and four jobs to fill. Suppose that Alanis and Ben can fill job 1, Camilla and Damon can fill job 2, Alanis and Damon can fill job 3, and Ben and Camilla can fill job 4.

**Page 422**

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

### Example 7.3.1: Composition of Functions Defined by Formulas

Let f: Z → Z be defined by f(n) = n² and g: Z → Z be defined by g(n) = n + 1.
Find (g ∘ f) and (f ∘ g).

**Solution:**
```
(g ∘ f)(n) = g(f(n)) = g(n²) = n² + 1
(f ∘ g)(n) = f(g(n)) = f(n + 1) = (n + 1)²
```

Note that g ∘ f ≠ f ∘ g (composition is not commutative).

### Example 7.3.2: Composition with the Identity Function

**Page 433**

**Theorem:** If f: X → Y and I_X is the identity on X and I_Y is the identity on Y, then:
```
f ∘ I_X = f    and    I_Y ∘ f = f
```

**Proof:** For all x ∈ X:
```
(f ∘ I_X)(x) = f(I_X(x)) = f(x)
(I_Y ∘ f)(x) = I_Y(f(x)) = f(x)
```

### Theorem 7.3.1: Composition of One-to-One Functions

If f: X → Y and g: Y → Z are both one-to-one, then g ∘ f is one-to-one.

**Proof:**
Suppose (g ∘ f)(x₁) = (g ∘ f)(x₂) for some x₁, x₂ ∈ X.
Then g(f(x₁)) = g(f(x₂)).
Since g is one-to-one, f(x₁) = f(x₂).
Since f is one-to-one, x₁ = x₂.
Therefore g ∘ f is one-to-one. ■

**Page 434**

### Theorem 7.3.2: Composition of Onto Functions

If f: X → Y and g: Y → Z are both onto, then g ∘ f is onto.

**Proof:**
Let z ∈ Z be arbitrary.
Since g is onto, there exists y ∈ Y such that g(y) = z.
Since f is onto, there exists x ∈ X such that f(x) = y.
Therefore (g ∘ f)(x) = g(f(x)) = g(y) = z.
Thus g ∘ f is onto. ■

### Inverse Functions

**Page 435**

**Definition:** Let f: X → Y be a bijection. The **inverse function** of f, denoted f⁻¹: Y → X, is defined by:

```
f⁻¹(y) = x ⟺ f(x) = y
```

### Theorem 7.3.3: Properties of Inverse Functions

If f: X → Y is a bijection with inverse f⁻¹: Y → X, then:
1. f⁻¹ ∘ f = I_X
2. f ∘ f⁻¹ = I_Y

**Proof:**
1. For all x ∈ X: (f⁻¹ ∘ f)(x) = f⁻¹(f(x)) = x = I_X(x)
2. For all y ∈ Y: (f ∘ f⁻¹)(y) = f(f⁻¹(y)) = y = I_Y(y) ■

### Example 7.3.3: Finding an Inverse Function

**Page 436**

Define f: R → R by f(x) = 4x - 1. Find f⁻¹.

**Solution:**
Let y = f(x) = 4x - 1. Solve for x:
```
y = 4x - 1
y + 1 = 4x
x = (y + 1)/4
```
Therefore f⁻¹(y) = (y + 1)/4.

Verify:
- (f⁻¹ ∘ f)(x) = f⁻¹(4x - 1) = ((4x - 1) + 1)/4 = x ✓
- (f ∘ f⁻¹)(y) = f((y + 1)/4) = 4((y + 1)/4) - 1 = y ✓

### One-to-One Correspondences

**Page 437**

**Definition:** A function f: X → Y is a **one-to-one correspondence** if:
1. f is one-to-one
2. f is onto

This is equivalent to saying f is a bijection.

### Example 7.3.4: Showing Functions are Inverses

Let f: R⁺ → R⁺ be defined by f(x) = x² and g: R⁺ → R⁺ be defined by g(x) = √x.
Show that g = f⁻¹.

**Solution:**
For all x ∈ R⁺:
- (g ∘ f)(x) = g(x²) = √(x²) = x
- (f ∘ g)(x) = f(√x) = (√x)² = x

Therefore g = f⁻¹. ■

### Theorem 7.3.4: The Inverse of a Composition

**Page 438**

If f: X → Y and g: Y → Z are both bijections, then:
```
(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹
```

**Proof:** We show that (f⁻¹ ∘ g⁻¹) ∘ (g ∘ f) = I_X:
```
(f⁻¹ ∘ g⁻¹) ∘ (g ∘ f) = f⁻¹ ∘ (g⁻¹ ∘ g) ∘ f
                        = f⁻¹ ∘ I_Y ∘ f
                        = f⁻¹ ∘ f
                        = I_X
```

### Example 7.3.5: Composition of Functions on Finite Sets

**Page 439**

Let X = {1, 2, 3}, Y = {a, b, c, d}, and Z = {α, β, γ}.
Define f: X → Y and g: Y → Z by:
```
f(1) = b, f(2) = d, f(3) = a
g(a) = β, g(b) = β, g(c) = α, g(d) = γ
```

Find g ∘ f.

**Solution:**
```
(g ∘ f)(1) = g(f(1)) = g(b) = β
(g ∘ f)(2) = g(f(2)) = g(d) = γ
(g ∘ f)(3) = g(f(3)) = g(a) = β
```

### Associativity of Function Composition

**Page 440**

### Theorem 7.3.5: Associativity of Composition

If f: W → X, g: X → Y, and h: Y → Z, then:
```
h ∘ (g ∘ f) = (h ∘ g) ∘ f
```

**Proof:** For all w ∈ W:
```
[h ∘ (g ∘ f)](w) = h((g ∘ f)(w)) = h(g(f(w)))
[(h ∘ g) ∘ f](w) = (h ∘ g)(f(w)) = h(g(f(w)))
```
Therefore h ∘ (g ∘ f) = (h ∘ g) ∘ f. ■

---

## 7.4 Cardinality with Applications to Computability

**Page 441**

> Without mathematics, there's nothing you can do. Everything around you is mathematics.
> — Shakuntala Devi

### Introduction to Cardinality

The cardinality of a set is, roughly speaking, the "number of elements" in the set. For finite sets, this is straightforward. For infinite sets, the concept becomes more subtle and leads to surprising results.

### Definition: Finite Set

A set A is **finite** if, and only if, it is the empty set or there is a one-to-one correspondence from {1, 2, 3, ..., n} to A for some positive integer n.

The integer n is called the **cardinality** of A, denoted |A| = n.

### Definition: Same Cardinality

**Page 442**

Sets A and B have the **same cardinality** if, and only if, there is a one-to-one correspondence from A to B.

We write |A| = |B|.

### Properties of Cardinality

**Theorem 7.4.1:** The "has the same cardinality as" relation is:
1. **Reflexive:** For any set A, |A| = |A|
2. **Symmetric:** For any sets A and B, if |A| = |B| then |B| = |A|
3. **Transitive:** For any sets A, B, and C, if |A| = |B| and |B| = |C| then |A| = |C|

### Definition: Countable and Uncountable Sets

**Page 443**

A set is **countably infinite** if it has the same cardinality as Z⁺ (the positive integers).

A set is **countable** if it is finite or countably infinite.

A set is **uncountable** if it is not countable.

### Example 7.4.1: The Set of Even Positive Integers Is Countably Infinite

**Page 444**

Show that the set E = {2, 4, 6, 8, ...} of even positive integers is countably infinite.

**Solution:** Define f: Z⁺ → E by f(n) = 2n.
- f is one-to-one: If f(n₁) = f(n₂), then 2n₁ = 2n₂, so n₁ = n₂.
- f is onto: For any 2k ∈ E, we have f(k) = 2k.

Therefore E is countably infinite. ■

### Example 7.4.2: The Set of All Integers Is Countably Infinite

**Page 445**

Show that Z (all integers) is countably infinite.

**Solution:** List the integers as: 0, 1, -1, 2, -2, 3, -3, ...

Define f: Z⁺ → Z by:
```
f(n) = { n/2        if n is even
       { -(n-1)/2   if n is odd
```

This gives: f(1) = 0, f(2) = 1, f(3) = -1, f(4) = 2, f(5) = -2, ...

f is a one-to-one correspondence, so Z is countably infinite. ■

### Theorem 7.4.2: The Set of Positive Rational Numbers Is Countable

**Page 446-447**

**Proof:** Arrange the positive rational numbers in a grid:

```
1/1  2/1  3/1  4/1  5/1  ...
1/2  2/2  3/2  4/2  5/2  ...
1/3  2/3  3/3  4/3  5/3  ...
1/4  2/4  3/4  4/4  5/4  ...
...
```

Count them diagonally, skipping duplicates:
1/1, 1/2, 2/1, 3/1, 1/3, 1/4, 2/3, 3/2, 4/1, ...

This creates a one-to-one correspondence with Z⁺. ■

### Cantor's Theorem: The Real Numbers Are Uncountable

**Page 448-449**

**Theorem 7.4.3 (Cantor, 1874):** The set of real numbers between 0 and 1 is uncountable.

**Proof (by contradiction using diagonalization):**

Suppose the real numbers between 0 and 1 can be listed:
```
r₁ = 0.a₁₁a₁₂a₁₃...
r₂ = 0.a₂₁a₂₂a₂₃...
r₃ = 0.a₃₁a₃₂a₃₃...
...
```

Construct a new number d = 0.d₁d₂d₃... where:
```
dᵢ = { 5 if aᵢᵢ ≠ 5
     { 6 if aᵢᵢ = 5
```

Then d differs from rᵢ in the i-th decimal place for every i, so d is not in the list.
This contradiction shows the set is uncountable. ■

### Consequences

**Page 450**

**Corollary 7.4.4:** The set of all real numbers R is uncountable.

**Proof:** The interval (0, 1) is uncountable and is a subset of R. Any set containing an uncountable subset must itself be uncountable. ■

**Theorem 7.4.5:** Any subset of a countable set is countable.

**Theorem 7.4.6:** Any set with an uncountable subset is uncountable.

---

## 7.4 (continued) Cardinality with Applications to Computability

**Page 451**

### Hilbert's Grand Hotel

David Hilbert illustrated properties of infinite sets with a thought experiment about a hotel with infinitely many rooms.

**Paradox 1:** Even though every room is occupied, we can always accommodate one more guest by moving each guest from room n to room n+1.

**Paradox 2:** We can accommodate infinitely many new guests by moving each guest from room n to room 2n, leaving all odd-numbered rooms vacant.

### The Schröder-Bernstein Theorem

**Page 452**

**Theorem (Schröder-Bernstein):** If there exists a one-to-one function from A to B and a one-to-one function from B to A, then A and B have the same cardinality.

This theorem allows us to prove sets have the same cardinality without explicitly constructing a bijection.

### Example 7.4.3: Cardinality of Intervals

Show that the intervals (0, 1) and (0, 2) have the same cardinality.

**Solution:** Define f: (0, 1) → (0, 2) by f(x) = 2x.
- f is one-to-one: If 2x₁ = 2x₂, then x₁ = x₂
- f is onto: For any y ∈ (0, 2), let x = y/2 ∈ (0, 1), then f(x) = y

Therefore |(0, 1)| = |(0, 2)|. ■

### Example 7.4.4: The Cardinality of the Real Line

**Page 453**

Show that the interval (0, 1) has the same cardinality as R (all real numbers).

**Solution:** Define f: (0, 1) → R by:
```
f(x) = tan(π(x - 1/2))
```

This maps (0, 1) bijectively onto R:
- As x → 0⁺, f(x) → -∞
- As x → 1⁻, f(x) → +∞
- f is continuous and strictly increasing

Therefore |(0, 1)| = |R|. ■

### The Continuum Hypothesis

**Page 454**

**Definition:** A set has cardinality ℵ₀ (aleph-null) if it is countably infinite.

**Definition:** A set has cardinality c (the continuum) if it has the same cardinality as R.

**The Continuum Hypothesis (CH):** There is no set whose cardinality is strictly between ℵ₀ and c.

Kurt Gödel (1940) and Paul Cohen (1963) proved that CH is independent of the standard axioms of set theory (ZFC).

### Power Sets and Cardinality

**Page 455**

**Theorem 7.4.7 (Cantor's Theorem):** For any set A, |A| < |P(A)| where P(A) is the power set of A.

**Proof:**
1. The function f: A → P(A) defined by f(a) = {a} is one-to-one, so |A| ≤ |P(A)|.

2. Suppose g: A → P(A) is any function. Define:
   ```
   B = {x ∈ A | x ∉ g(x)}
   ```

   If B = g(a) for some a ∈ A, then:
   - If a ∈ B, then a ∉ g(a) = B (contradiction)
   - If a ∉ B = g(a), then a ∈ B (contradiction)

   Therefore g is not onto, so no function from A to P(A) is onto.
   Thus |A| < |P(A)|. ■

### The Hierarchy of Infinities

**Page 456**

Cantor's theorem implies an infinite hierarchy of infinite cardinalities:
```
|ℕ| < |P(ℕ)| < |P(P(ℕ))| < |P(P(P(ℕ)))| < ...
```

We have:
- |ℕ| = ℵ₀
- |P(ℕ)| = 2^ℵ₀ = c (the cardinality of the continuum)
- |P(P(ℕ))| = 2^c
- And so on...

### Applications to Computability

**Page 457**

### Example 7.4.5: The Set of Computer Programs Is Countable

**Theorem:** The set of all computer programs in any programming language is countable.

**Proof:**
Every program is a finite string of characters from a finite alphabet.
- Let Sₙ = set of all programs of length n
- Each Sₙ is finite
- The set of all programs = ⋃_{n=1}^∞ Sₙ
- A countable union of finite sets is countable

Therefore the set of all programs is countable. ■

### Example 7.4.6: Existence of Non-Computable Functions

**Page 458**

**Theorem:** There exist functions from ℕ to {0, 1} that are not computable by any algorithm.

**Proof:**
- The set of all functions from ℕ to {0, 1} has cardinality 2^ℵ₀ (uncountable)
- The set of all computer programs is countable (cardinality ℵ₀)
- Since ℵ₀ < 2^ℵ₀, there are more functions than programs
- Therefore, there exist functions that no program can compute. ■

### The Halting Problem

**Page 459**

**Definition:** The **halting problem** asks whether there exists an algorithm that can determine, for any program P and input I, whether P halts when run on input I.

**Theorem (Turing, 1936):** The halting problem is undecidable - no algorithm can solve it.

**Proof sketch:**
Suppose algorithm HALT(P, I) returns true if program P halts on input I.
Consider the program:
```
DIAGONAL(P):
    if HALT(P, P):
        loop forever
    else:
        halt
```

What does DIAGONAL(DIAGONAL) do?
- If it halts, then HALT(DIAGONAL, DIAGONAL) = true, so it loops forever
- If it loops forever, then HALT(DIAGONAL, DIAGONAL) = false, so it halts

This contradiction shows HALT cannot exist. ■

### Example 7.4.7: Countability and Database Theory

**Page 460**

In database theory, we often need to know whether certain sets of queries or data structures are countable or uncountable.

**Example:** The set of all SQL queries is countable (each query is a finite string).

**Example:** The set of all possible database states over an infinite domain is uncountable.

This has implications for query optimization and database design - we can enumerate all possible queries but not all possible database states.

---

## Summary of Chapter 7

**Page 461-470**

### Key Concepts

**Functions:**
- A function f: X → Y assigns to each element x ∈ X exactly one element y ∈ Y
- Domain, co-domain, and range
- Functions as sets of ordered pairs
- Function composition

**Special Types of Functions:**
- One-to-one (injective): Different inputs give different outputs
- Onto (surjective): Every element of the co-domain is mapped to
- Bijection: Both one-to-one and onto
- Inverse functions exist for bijections

**Cardinality:**
- Finite sets have cardinality n for some n ∈ ℕ
- Countably infinite sets have the same cardinality as ℕ
- Uncountable sets (like ℝ) are "larger" than countable sets
- Cantor's diagonalization argument
- The hierarchy of infinities

**Applications:**
- Hash functions and collision handling
- The pigeonhole principle
- Computability and the existence of non-computable functions
- The halting problem

### Important Theorems

1. **Composition preserves properties:**
   - The composition of one-to-one functions is one-to-one
   - The composition of onto functions is onto
   - The composition of bijections is a bijection

2. **Cardinality results:**
   - ℚ is countable
   - ℝ is uncountable
   - For any set A, |A| < |P(A)|
   - Any subset of a countable set is countable

3. **Computability results:**
   - The set of all programs is countable
   - The set of all functions ℕ → {0, 1} is uncountable
   - Therefore, non-computable functions exist
   - The halting problem is undecidable

### Problem-Solving Strategies

**To prove a function is one-to-one:**
- Assume f(x₁) = f(x₂) and show x₁ = x₂
- Or show the contrapositive: if x₁ ≠ x₂ then f(x₁) ≠ f(x₂)

**To prove a function is onto:**
- Given arbitrary y in the co-domain, find x in the domain such that f(x) = y
- Often involves solving the equation f(x) = y for x

**To find an inverse function:**
1. Verify the function is a bijection
2. Set y = f(x) and solve for x in terms of y
3. The inverse is f⁻¹(y) = [expression for x]

**To prove a set is countable:**
- Find a bijection with ℕ (or a subset of ℕ)
- Or show it's a subset of a known countable set
- Or express it as a countable union of finite sets

**To prove a set is uncountable:**
- Use Cantor's diagonalization
- Or show it contains an uncountable subset
- Or show there's a bijection with a known uncountable set

### Exercises and Applications

Throughout this chapter, we've seen applications to:
- Computer science (hash functions, computability)
- Database theory (query languages, data structures)
- Cryptography (one-way functions)
- Algorithm analysis (pigeonhole principle)
- Pure mathematics (set theory, analysis)

The concepts of functions and cardinality form the foundation for much of discrete mathematics and theoretical computer science. Understanding these ideas is essential for advanced study in algorithms, complexity theory, database systems, and mathematical logic.

### Historical Notes

- Georg Cantor (1845-1918): Developed the theory of infinite sets and cardinality
- David Hilbert (1862-1943): Hilbert's Hotel paradox, formalization of mathematics
- Alan Turing (1912-1954): Proved the undecidability of the halting problem
- Kurt Gödel (1906-1978): Incompleteness theorems, work on the continuum hypothesis
- Paul Cohen (1934-2007): Proved independence of the continuum hypothesis

These mathematicians' work on functions and cardinality has profoundly influenced our understanding of computation, infinity, and the foundations of mathematics itself.

---

## End of Chapter 7

This completes Chapter 7 on Functions. The chapter has covered fundamental concepts about functions, their properties, composition, inverses, and the deep theory of cardinality with its surprising applications to computability. These concepts form the mathematical foundation for understanding algorithms, data structures, databases, and the theoretical limits of computation.