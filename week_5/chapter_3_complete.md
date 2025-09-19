# Chapter 3: Characterizing Running Times

**Pages 85-118**

## Introduction

**Page 85**

The order of growth of the running time of an algorithm, defined in Chapter 2, gives a simple way to characterize the algorithm's efficiency and also allows us to compare it with alternative algorithms. Once the input size n becomes large enough, merge sort, with its Θ(n lg n) worst-case running time, beats insertion sort, whose worst-case running time is Θ(n²). Although we can sometimes determine the exact running time of an algorithm, as we did for insertion sort in Chapter 2, the extra precision is rarely worth the effort of computing it. For large enough inputs, the multiplicative constants and lower-order terms of an exact running time are dominated by the effects of the input size itself.

When we look at input sizes large enough to make relevant only the order of growth of the running time, we are studying the **asymptotic efficiency** of algorithms. That is, we are concerned with how the running time of an algorithm increases with the size of the input in the limit, as the size of the input increases without bound. Usually, an algorithm that is asymptotically more efficient is the best choice for all but very small inputs.

This chapter gives several standard methods for simplifying the asymptotic analysis of algorithms. The next section presents informally the three most commonly used types of "asymptotic notation," of which we have already seen an example in Θ-notation. It also shows one way to use these asymptotic notations to reason about the worst-case running time of insertion sort. Then we look at asymptotic notations more formally and present several notational conventions used

**Page 86**

throughout this book. The last section reviews the behavior of functions that commonly arise when analyzing algorithms.

---

## 3.1 O-notation, Ω-notation, and Θ-notation

**Page 86**

When we analyzed the worst-case running time of insertion sort in Chapter 2, we started with the complicated expression

(c₅/2 + c₆/2 + c₇/2)n² + (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)n - (c₂ + c₄ + c₅ + c₈)

We then discarded the lower-order terms (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)n and c₂ + c₄ + c₅ + c₈, and we also ignored the coefficient c₅/2 + c₆/2 + c₇/2 of n². That left just the factor n², which we put into Θ-notation as Θ(n²). We use this style to characterize running times of algorithms: discard the lower-order terms and the coefficient of the leading term, and use a notation that focuses on the rate of growth of the running time.

Θ-notation is not the only such "asymptotic notation." In this section, we'll see other forms of asymptotic notation as well. We start with intuitive looks at these notations, revisiting insertion sort to see how we can apply them. In the next section, we'll see the formal definitions of our asymptotic notations, along with conventions for using them.

Before we get into specifics, bear in mind that the asymptotic notations we'll see are designed so that they characterize functions in general. It so happens that the functions we are most interested in denote the running times of algorithms. But asymptotic notation can apply to functions that characterize some other aspect of algorithms (the amount of space they use, for example), or even to functions that have nothing whatsoever to do with algorithms.

### O-notation

**Page 87**

O-notation characterizes an upper bound on the asymptotic behavior of a function. In other words, it says that a function grows no faster than a certain rate, based on the highest-order term. Consider, for example, the function 7n³ + 100n² - 20n + 6. Its highest-order term is 7n³, and so we say that this function's rate of growth is n³. Because this function grows no faster than n³, we can write that it is O(n³). You might be surprised that we can also write that the function 7n³ + 100n² - 20n + 6 is O(n⁴). Why? Because the function grows more slowly than n⁴, we are correct in saying that it grows no faster. As you might have guessed, this function is also O(n⁵), O(n⁶), and so on. More generally, it is O(nᶜ) for any constant c ≥ 3.

### Ω-notation

Ω-notation characterizes a lower bound on the asymptotic behavior of a function. In other words, it says that a function grows at least as fast as a certain rate, based — as in O-notation—on the highest-order term. Because the highest-order term in the function 7n³ + 100n² - 20n + 6 grows at least as fast as n³, this function is Ω(n³). This function is also Ω(n²) and Ω(n). More generally, it is Ω(nᶜ) for any constant c ≤ 3.

### Θ-notation

Θ-notation characterizes a tight bound on the asymptotic behavior of a function. It says that a function grows precisely at a certain rate, based —once again—on the highest-order term. Put another way, Θ-notation characterizes the rate of growth of the function to within a constant factor from above and to within a constant factor from below. These two constant factors need not be equal.

If you can show that a function is both O(f(n)) and Ω(f(n)) for some function f(n), then you have shown that the function is Θ(f(n)). (The next section states this fact as a theorem.) For example, since the function 7n³ + 100n² - 20n + 6 is both O(n³) and Ω(n³), it is also Θ(n³).

**Page 88**

### Example: Insertion sort

Let's revisit insertion sort and see how to work with asymptotic notation to characterize its Θ(n²) worst-case running time without evaluating summations as we did in Chapter 2. Here is the INSERTION-SORT procedure once again:

```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i - 1].
4      j = i - 1
5      while j > 0 and A[j] > key
6          A[j + 1] = A[j]
7          j = j - 1
8      A[j + 1] = key
```

What can we observe about how the pseudocode operates? The procedure has nested loops. The outer loop is a for loop that runs n - 1 times, regardless of the values being sorted. The inner loop is a while loop, but the number of iterations it makes depends on the values being sorted. The loop variable j starts at i - 1 and decreases by 1 in each iteration until either it reaches 0 or A[j] ≤ key. For a given value of i, the while loop might iterate 0 times, i - 1 times, or anywhere in between. The body of the while loop (lines 6-7) takes constant time per iteration of the while loop.

**Page 89**

![Figure 3.1: The Ω(n²) lower bound for insertion sort. If the first n/3 positions contain the n/3 largest values, each of these values must move through each of the middle n/3 positions, one position at a time, to end up somewhere in the last n/3 positions. Since each of n/3 values moves through at least each of n/3 positions, the time taken in this case is at least proportional to (n/3)(n/3) = n²/9, or Ω(n²).]

These observations suffice to deduce an O(n²) running time for any case of INSERTION-SORT, giving us a blanket statement that covers all inputs. The running time is dominated by the inner loop. Because each of the n - 1 iterations of the outer loop causes the inner loop to iterate at most i - 1 times, and because i is at most n, the total number of iterations of the inner loop is at most (n - 1)(n - 1), which is less than n². Since each iteration of the inner loop takes constant time, the total time spent in the inner loop is at most a constant times n², or O(n²).

With a little creativity, we can also see that the worst-case running time of INSERTION-SORT is Ω(n²). By saying that the worst-case running time of an algorithm is Ω(n²), we mean that for every input size n above a certain threshold, there is at least one input of size n for which the algorithm takes at least cn² time, for some positive constant c. It does not necessarily mean that the algorithm takes at least cn² time for all inputs.

Let's now see why the worst-case running time of INSERTION-SORT is Ω(n²). For a value to end up to the right of where it started, it must have been moved in line 6. In fact, for a value to end up k positions to the right of where it started, line 6 must have executed k times. As Figure 3.1 shows, let's assume that n is a multiple of 3 so that we can divide the array A into groups of n/3 positions. Suppose that in the input to INSERTION-SORT, the n/3 largest values occupy the first

**Page 90**

n/3 array positions A[1 : n/3]. (It does not matter what relative order they have within the first n/3 positions.) Once the array has been sorted, each of these n/3 values ends up somewhere in the last n/3 positions A[2n/3 + 1 : n]. For that to happen, each of these n/3 values must pass through each of the middle n/3 positions A[n/3 + 1 : 2n/3]. Each of these n/3 values passes through these middle n/3 positions one position at a time, by at least n/3 executions of line 6. Because at least n/3 values have to pass through at least n/3 positions, the time taken by INSERTION-SORT in the worst case is at least proportional to (n/3)(n/3) = n²/9, which is Ω(n²).

Because we have shown that INSERTION-SORT runs in O(n²) time in all cases and that there is an input that makes it take Ω(n²) time, we can conclude that the worst-case running time of INSERTION-SORT is Θ(n²). It does not matter that the constant factors for upper and lower bounds might differ. What matters is that we have characterized the worst-case running time to within constant factors (discounting lower-order terms). This argument does not show that INSERTION-SORT runs in Θ(n²) time in all cases. Indeed, we saw in Chapter 2 that the best-case running time is Θ(n).

### Exercises

**3.1-1**
Modify the lower-bound argument for insertion sort to handle input sizes that are not necessarily a multiple of 3.

**3.1-2**
Using reasoning similar to what we used for insertion sort, analyze the running time of the selection sort algorithm from Exercise 2.2-2.

**3.1-3**
Suppose that α is a fraction in the range 0 < α < 1. Show how to generalize the lower-bound argument for insertion sort to consider an input in which the αn largest values start in the first αn positions. What additional restriction do you need to put on α? What value of α

**Page 91**

maximizes the number of times that the αn largest values must pass through each of the middle (1 - 2α)n array positions?

---

## 3.2 Asymptotic notation: formal definitions

**Page 91**

Having seen asymptotic notation informally, let's get more formal. The notations we use to describe the asymptotic running time of an algorithm are defined in terms of functions whose domains are typically the set N of natural numbers or the set R of real numbers. Such notations are convenient for describing a running-time function T(n). This section defines the basic asymptotic notations and also introduces some common "proper" notational abuses.

![Figure 3.2: Graphic examples of the O, Ω, and Θ notations. In each part, the value of n₀ shown is the minimum possible value, but any greater value also works. (a) O-notation gives an upper bound for a function to within a constant factor. We write f(n) = O(g(n)) if there are positive constants n₀ and c such that at and to the right of n₀, the value of f(n) always lies on or below cg(n). (b) Ω-notation gives a lower bound for a function to within a constant factor. We write f(n) = Ω(g(n)) if there are positive constants n₀ and c such that at and to the right of n₀, the value of f(n) always lies on or above cg(n). (c) Θ-notation bounds a function to within constant factors. We write f(n) = Θ(g(n)) if there exist positive constants n₀, c₁, and c₂ such that at and to the right of n₀, the value of f(n) always lies between c₁g(n) and c₂g(n) inclusive.]

### O-notation

As we saw in Section 3.1, O-notation describes an asymptotic upper bound. We use O-notation to give an upper bound on a function, to

**Page 92**

within a constant factor.

Here is the formal definition of O-notation. For a given function g(n), we denote by O(g(n)) (pronounced "big-oh of g of n" or sometimes just "oh of g of n") the set of functions

O(g(n)) = {f(n) : there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n₀}.¹

A function f(n) belongs to the set O(g(n)) if there exists a positive constant c such that f(n) ≤ cg(n) for sufficiently large n. Figure 3.2(a) shows the intuition behind O-notation. For all values n at and to the right of n₀, the value of the function f(n) is on or below cg(n).

The definition of O(g(n)) requires that every function f(n) in the set O(g(n)) be asymptotically nonnegative: f(n) must be nonnegative whenever n is sufficiently large. (An asymptotically positive function is one that is positive for all sufficiently large n.) Consequently, the function g(n) itself must be asymptotically nonnegative, or else the set O(g(n)) is empty. We therefore assume that every function used within O-notation is asymptotically nonnegative. This assumption holds for the other asymptotic notations defined in this chapter as well.

You might be surprised that we define O-notation in terms of sets. Indeed, you might expect that we would write "f(n) ∈ O(g(n))" to indicate that f(n) belongs to the set O(g(n)). Instead, we usually write "f(n) = O(g(n))" and say "f(n) is big-oh of g(n)" to express the same notion. Although it may seem confusing at first to abuse equality in this way, we'll see later in this section that doing so has its advantages.

Let's explore an example of how to use the formal definition of O-notation to justify our practice of discarding lower-order terms and ignoring the constant coefficient of the highest-order term. We'll show that 4n² + 100n + 500 = O(n²), even though the lower-order terms have much larger coefficients than the leading term. We need to find positive constants c and n₀ such that 4n² + 100n + 500 ≤ cn² for all n ≥ n₀. Dividing both sides by n² gives 4 + 100/n + 500/n² ≤ c. This inequality is satisfied for many choices of c and n₀. For example, if we choose n₀ = 1,

**Page 93**

then this inequality holds for c = 604. If we choose n₀ = 10, then c = 19 works, and choosing n₀ = 100 allows us to use c = 5.05.

We can also use the formal definition of O-notation to show that the function n³ - 100n² does not belong to the set O(n²), even though the coefficient of n² is a large negative number. If we had n³ - 100n² = O(n²), then there would be positive constants c and n₀ such that n³ - 100n² ≤ cn² for all n ≥ n₀. Again, we divide both sides by n², giving n - 100 ≤ c. Regardless of what value we choose for the constant c, this inequality does not hold for any value of n > c + 100.

### Ω-notation

Just as O-notation provides an asymptotic upper bound on a function, Ω-notation provides an asymptotic lower bound. For a given function g(n), we denote by Ω(g(n)) (pronounced "big-omega of g of n" or sometimes just "omega of g of n") the set of functions

Ω(g(n)) = {f(n) : there exist positive constants c and n₀ such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n₀}.

Figure 3.2(b) shows the intuition behind Ω-notation. For all values n at or to the right of n₀, the value of f(n) is on or above cg(n).

We've already shown that 4n² + 100n + 500 = O(n²). Now let's show that 4n² + 100n + 500 = Ω(n²). We need to find positive constants c and n₀ such that 4n² + 100n + 500 ≥ cn² for all n ≥ n₀. As before, we divide both sides by n², giving 4 + 100/n + 500/n² ≥ c. This inequality holds when n₀ is any positive integer and c = 4.

What if we had subtracted the lower-order terms from the 4n² term instead of adding them? What if we had a small coefficient for the n² term? The function would still be Ω(n²). For example, let's show that n²/100 - 100n - 500 = Ω(n²). Dividing by n² gives 1/100 - 100/n - 500/n²

**Page 94**

≥ c. We can choose any value for n₀ that is at least 10,005 and find a positive value for c. For example, when n₀ = 10,005, we can choose c = 2.49 × 10⁻⁹. Yes, that's a tiny value for c, but it is positive. If we select a larger value for n₀, we can also increase c. For example, if n₀ = 100,000, then we can choose c = 0.0089. The higher the value of n₀, the closer to the coefficient 1/100 we can choose c.

### Θ-notation

We use Θ-notation for asymptotically tight bounds. For a given function g(n), we denote by Θ(g(n)) ("theta of g of n") the set of functions

Θ(g(n)) = {f(n) : there exist positive constants c₁, c₂, and n₀ such that 0 ≤ c₁g(n) ≤ f(n) ≤ c₂g(n) for all n ≥ n₀}.

Figure 3.2(c) shows the intuition behind Θ-notation. For all values of n at and to the right of n₀, the value of f(n) lies at or above c₁g(n) and at or below c₂g(n). In other words, for all n ≥ n₀, the function f(n) is equal to g(n) to within constant factors.

The definitions of O-, Ω-, and Θ-notations lead to the following theorem, whose proof we leave as Exercise 3.2-4.

### Theorem 3.1

For any two functions f(n) and g(n), we have f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n)).
▪

We typically apply Theorem 3.1 to prove asymptotically tight bounds from asymptotic upper and lower bounds.

### Asymptotic notation and running times

When you use asymptotic notation to characterize an algorithm's running time, make sure that the asymptotic notation you use is as precise as possible without overstating which running time it applies to.

**Page 95**

Here are some examples of using asymptotic notation properly and improperly to characterize running times.

Let's start with insertion sort. We can correctly say that insertion sort's worst-case running time is O(n²), Ω(n²), and—due to Theorem 3.1—Θ(n²). Although all three ways to characterize the worst-case running times are correct, the Θ(n²) bound is the most precise and hence the most preferred. We can also correctly say that insertion sort's best-case running time is O(n), Ω(n), and Θ(n), again with Θ(n) the most precise and therefore the most preferred.

Here is what we cannot correctly say: insertion sort's running time is Θ(n²). That is an overstatement because by omitting "worst-case" from the statement, we're left with a blanket statement covering all cases. The error here is that insertion sort does not run in Θ(n²) time in all cases since, as we've seen, it runs in Θ(n) time in the best case. We can correctly say that insertion sort's running time is O(n²), however, because in all cases, its running time grows no faster than n². When we say O(n²) instead of Θ(n²), there is no problem in having cases whose running time grows more slowly than n². Likewise, we cannot correctly say that insertion sort's running time is Θ(n), but we can say that its running time is Ω(n).

How about merge sort? Since merge sort runs in Θ(n lg n) time in all cases, we can just say that its running time is Θ(n lg n) without specifying worst-case, best-case, or any other case.

People occasionally conflate O-notation with Θ-notation by mistakenly using O-notation to indicate an asymptotically tight bound. They say things like "an O(n lg n)-time algorithm runs faster than an O(n²)-time algorithm." Maybe it does, maybe it doesn't. Since O-notation denotes only an asymptotic upper bound, that so-called O(n²)-time algorithm might actually run in Θ(n) time. You should be careful to choose the appropriate asymptotic notation. If you want to indicate an asymptotically tight bound, use Θ-notation.

**Page 96**

We typically use asymptotic notation to provide the simplest and most precise bounds possible. For example, if an algorithm has a running time of 3n² + 20n in all cases, we use asymptotic notation to write that its running time is Θ(n²). Strictly speaking, we are also correct in writing that the running time is O(n³) or Θ(3n² + 20n). Neither of these expressions is as useful as writing Θ(n²) in this case, however: O(n³) is less precise than Θ(n²) if the running time is 3n² + 20n, and Θ(3n² + 20n) introduces complexity that obscures the order of growth. By writing the simplest and most precise bound, such as Θ(n²), we can categorize and compare different algorithms. Throughout the book, you will see asymptotic running times that are almost always based on polynomials and logarithms: functions such as n, n lg² n, n² lg n, or n^(1/2). You will also see some other functions, such as exponentials, lg lg n, and lg*n (see Section 3.3). It is usually fairly easy to compare the rates of growth of these functions. Problem 3-3 gives you good practice.

### Asymptotic notation in equations and inequalities

Although we formally define asymptotic notation in terms of sets, we use the equal sign (=) instead of the set membership sign (∈) within formulas. For example, we wrote that 4n² + 100n + 500 = O(n²). We might also write 2n² + 3n + 1 = 2n² + Θ(n). How do we interpret such formulas?

When the asymptotic notation stands alone (that is, not within a larger formula) on the right-hand side of an equation (or inequality), as in 4n² + 100n + 500 = O(n²), the equal sign means set membership: 4n² + 100n + 500 ∈ O(n²). In general, however, when asymptotic notation appears in a formula, we interpret it as standing for some anonymous function that we do not care to name. For example, the formula 2n² + 3n + 1 = 2n² + Θ(n) means that 2n² + 3n + 1 = 2n² + f(n), where f(n) ∈ Θ(n). In this case, we let f(n) = 3n + 1, which indeed belongs to Θ(n).

**Page 97**

Using asymptotic notation in this manner can help eliminate inessential detail and clutter in an equation. For example, in Chapter 2 we expressed the worst-case running time of merge sort as the recurrence

T(n) = 2T(n/2) + Θ(n).

If we are interested only in the asymptotic behavior of T(n), there is no point in specifying all the lower-order terms exactly, because they are all understood to be included in the anonymous function denoted by the term Θ(n).

The number of anonymous functions in an expression is understood to be equal to the number of times the asymptotic notation appears. For example, in the expression

∑(i=1 to n) O(i),

there is only a single anonymous function (a function of i). This expression is thus not the same as O(1) + O(2) + ⋯ + O(n), which doesn't really have a clean interpretation.

In some cases, asymptotic notation appears on the left-hand side of an equation, as in

2n² + Θ(n) = Θ(n²).

Interpret such equations using the following rule: No matter how the anonymous functions are chosen on the left of the equal sign, there is a way to choose the anonymous functions on the right of the equal sign to make the equation valid. Thus, our example means that for any function f(n) ∈ Θ(n), there is some function g(n) ∈ Θ(n²) such that 2n² + f(n) = g(n) for all n. In other words, the right-hand side of an equation provides a coarser level of detail than the left-hand side.

We can chain together a number of such relationships, as in

2n² + 3n + 1 = 2n² + Θ(n)
            = Θ(n²).

**Page 98**

By the rules above, interpret each equation separately. The first equation says that there is some function f(n) ∈ Θ(n) such that 2n² + 3n + 1 = 2n² + f(n) for all n. The second equation says that for any function g(n) ∈ Θ(n) (such as the f(n) just mentioned), there is some function h(n) ∈ Θ(n²) such that 2n² + g(n) = h(n) for all n. This interpretation implies that 2n² + 3n + 1 = Θ(n²), which is what the chaining of equations intuitively says.

### Proper abuses of asymptotic notation

Besides the abuse of equality to mean set membership, which we now see has a precise mathematical interpretation, another abuse of asymptotic notation occurs when the variable tending toward ∞ must be inferred from context. For example, when we say O(g(n)), we can assume that we're interested in the growth of g(n) as n grows, and if we say O(g(m)) we're talking about the growth of g(m) as m grows. The free variable in the expression indicates what variable is going to ∞.

The most common situation requiring contextual knowledge of which variable tends to ∞ occurs when the function inside the asymptotic notation is a constant, as in the expression O(1). We cannot infer from the expression which variable is going to ∞, because no variable appears there. The context must disambiguate. For example, if the equation using asymptotic notation is f(n) = O(1), it's apparent that the variable we're interested in is n. Knowing from context that the variable of interest is n, however, allows us to make perfect sense of the expression by using the formal definition of O-notation: the expression f(n) = O(1) means that the function f(n) is bounded from above by a constant as n goes to ∞. Technically, it might be less ambiguous if we explicitly indicated the variable tending to ∞ in the asymptotic notation itself, but that would clutter the notation. Instead, we simply ensure that the context makes it clear which variable (or variables) tend to ∞.

When the function inside the asymptotic notation is bounded by a positive constant, as in T(n) = O(1), we often abuse asymptotic notation in yet another way, especially when stating recurrences. We may write something like T(n) = O(1) for n < 3. According to the

**Page 99**

formal definition of O-notation, this statement is meaningless, because the definition only says that T(n) is bounded above by a positive constant c for n ≥ n₀ for some n₀ > 0. The value of T(n) for n < n₀ need not be so bounded. Thus, in the example T(n) = O(1) for n < 3, we cannot infer any constraint on T(n) when n < 3, because it might be that n₀ > 3.

What is conventionally meant when we say T(n) = O(1) for n < 3 is that there exists a positive constant c such that T(n) ≤ c for n < 3. This convention saves us the trouble of naming the bounding constant, allowing it to remain anonymous while we focus on more important variables in an analysis. Similar abuses occur with the other asymptotic notations. For example, T(n) = Θ(1) for n < 3 means that T(n) is bounded above and below by positive constants when n < 3.

Occasionally, the function describing an algorithm's running time may not be defined for certain input sizes, for example, when an algorithm assumes that the input size is an exact power of 2. We still use asymptotic notation to describe the growth of the running time, understanding that any constraints apply only when the function is defined. For example, suppose that f(n) is defined only on a subset of the natural or nonnegative real numbers. Then f(n) = O(g(n)) means that the bound 0 ≤ T(n) ≤ cg(n) in the definition of O-notation holds for all n ≥ n₀ over the domain of f(n), that is, where f(n) is defined. This abuse is rarely pointed out, since what is meant is generally clear from context.

In mathematics, it's okay — and often desirable — to abuse a notation, as long as we don't misuse it. If we understand precisely what is meant by the abuse and don't draw incorrect conclusions, it can simplify our mathematical language, contribute to our higher-level understanding, and help us focus on what really matters.

### o-notation

The asymptotic upper bound provided by O-notation may or may not be asymptotically tight. The bound 2n² = O(n²) is asymptotically tight, but the bound 2n = O(n²) is not. We use o-notation to denote an upper

**Page 100**

bound that is not asymptotically tight. We formally define o(g(n)) ("little-oh of g of n") as the set

o(g(n)) = {f(n) : for any positive constant c > 0, there exists a constant n₀ > 0 such that 0 ≤ f(n) < cg(n) for all n ≥ n₀}.

For example, 2n = o(n²), but 2n² ≠ o(n²).

The definitions of O-notation and o-notation are similar. The main difference is that in f(n) = O(g(n)), the bound 0 ≤ f(n) ≤ cg(n) holds for some constant c > 0, but in f(n) = o(g(n)), the bound 0 ≤ f(n) < cg(n) holds for all constants c > 0. Intuitively, in o-notation, the function f(n) becomes insignificant relative to g(n) as n gets large:

lim(n→∞) f(n)/g(n) = 0.

Some authors use this limit as a definition of the o-notation, but the definition in this book also restricts the anonymous functions to be asymptotically nonnegative.

### ω-notation

By analogy, ω-notation is to Ω-notation as o-notation is to O-notation. We use ω-notation to denote a lower bound that is not asymptotically tight. One way to define it is by

f(n) ∈ ω(g(n)) if and only if g(n) ∈ o(f(n)).

Formally, however, we define ω(g(n)) ("little-omega of g of n") as the set

ω(g(n)) = {f(n) : for any positive constant c > 0, there exists a constant n₀ > 0 such that 0 ≤ cg(n) < f(n) for all n ≥ n₀}.

Where the definition of o-notation says that f(n) < cg(n), the definition of ω-notation says the opposite: that cg(n) < f(n). For examples of ω-notation, we have n²/2 = ω(n), but n²/2 ≠ ω(n²). The relation f(n) = ω(g(n)) implies that

**Page 101**

lim(n→∞) f(n)/g(n) = ∞,

if the limit exists. That is, f(n) becomes arbitrarily large relative to g(n) as n gets large.

### Comparing functions

Many of the relational properties of real numbers apply to asymptotic comparisons as well. For the following, assume that f(n) and g(n) are asymptotically positive.

**Transitivity:**
- f(n) = Θ(g(n)) and g(n) = Θ(h(n)) imply f(n) = Θ(h(n)),
- f(n) = O(g(n)) and g(n) = O(h(n)) imply f(n) = O(h(n)),
- f(n) = Ω(g(n)) and g(n) = Ω(h(n)) imply f(n) = Ω(h(n)),
- f(n) = o(g(n)) and g(n) = o(h(n)) imply f(n) = o(h(n)),
- f(n) = ω(g(n)) and g(n) = ω(h(n)) imply f(n) = ω(h(n)).

**Reflexivity:**
- f(n) = Θ(f(n)),
- f(n) = O(f(n)),
- f(n) = Ω(f(n)).

**Symmetry:**
- f(n) = Θ(g(n)) if and only if g(n) = Θ(f(n)).

**Transpose symmetry:**
- f(n) = O(g(n)) if and only if g(n) = Ω(f(n)),

**Page 102**

- f(n) = o(g(n)) if and only if g(n) = ω(f(n)).

Because these properties hold for asymptotic notations, we can draw an analogy between the asymptotic comparison of two functions f and g and the comparison of two real numbers a and b:

- f(n) = O(g(n)) is like a ≤ b,
- f(n) = Ω(g(n)) is like a ≥ b,
- f(n) = Θ(g(n)) is like a = b,
- f(n) = o(g(n)) is like a < b,
- f(n) = ω(g(n)) is like a > b.

We say that f(n) is **asymptotically smaller** than g(n) if f(n) = o(g(n)), and f(n) is **asymptotically larger** than g(n) if f(n) = ω(g(n)).

One property of real numbers, however, does not carry over to asymptotic notation:

**Trichotomy:** For any two real numbers a and b, exactly one of the following must hold: a < b, a = b, or a > b.

Although any two real numbers can be compared, not all functions are asymptotically comparable. That is, for two functions f(n) and g(n), it may be the case that neither f(n) = O(g(n)) nor f(n) = Ω(g(n)) holds. For example, we cannot compare the functions n and n^(1 + sin n) using asymptotic notation, since the value of the exponent in n^(1 + sin n) oscillates between 0 and 2, taking on all values in between.

### Exercises

**3.2-1**
Let f(n) and g(n) be asymptotically nonnegative functions. Using the basic definition of Θ-notation, prove that max{f(n), g(n)} = Θ(f(n) + g(n)).

**3.2-2**

**Page 103**

Explain why the statement, "The running time of algorithm A is at least O(n²)," is meaningless.

**3.2-3**
Is 2^(n+1) = O(2^n)? Is 2^(2n) = O(2^n)?

**3.2-4**
Prove Theorem 3.1.

**3.2-5**
Prove that the running time of an algorithm is Θ(g(n)) if and only if its worst-case running time is O(g(n)) and its best-case running time is Ω(g(n)).

**3.2-6**
Prove that o(g(n)) ∩ ω(g(n)) is the empty set.

**3.2-7**
We can extend our notation to the case of two parameters n and m that can go to ∞ independently at different rates. For a given function g(n, m), we denote by O(g(n, m)) the set of functions

O(g(n, m)) = {f(n, m) : there exist positive constants c, n₀, and m₀ such that 0 ≤ f(n, m) ≤ cg(n, m) for all n ≥ n₀ or m ≥ m₀}.

Give corresponding definitions for Ω(g(n, m)) and Θ(g(n, m)).

---

## 3.3 Standard notations and common functions

**Page 103**

This section reviews some standard mathematical functions and notations and explores the relationships among them. It also illustrates the use of the asymptotic notations.

### Monotonicity

**Page 104**

A function f(n) is **monotonically increasing** if m ≤ n implies f(m) ≤ f(n). Similarly, it is **monotonically decreasing** if m ≤ n implies f(m) ≥ f(n). A function f(n) is **strictly increasing** if m < n implies f(m) < f(n) and **strictly decreasing** if m < n implies f(m) > f(n).

### Floors and ceilings

For any real number x, we denote the greatest integer less than or equal to x by ⌊x⌋ (read "the floor of x") and the least integer greater than or equal to x by ⌈x⌉ (read "the ceiling of x"). The floor function is monotonically increasing, as is the ceiling function.

Floors and ceilings obey the following properties. For any integer n, we have

⌊n⌋ = n = ⌈n⌉.

For all real x, we have

x - 1 < ⌊x⌋ ≤ x ≤ ⌈x⌉ < x + 1.                      (3.3)

We also have

⌊x⌋ + ⌈n - x⌉ = n for any integer n and real x,       (3.4)

or equivalently,

⌈x⌉ + ⌊n - x⌋ = n.

For any real number x ≥ 0 and integers a, b > 0, we have

⌊⌊x/a⌋/b⌋ = ⌊x/ab⌋,                                  (3.5)
⌈⌈x/a⌉/b⌉ = ⌈x/ab⌉,                                  (3.6)
⌈a/b⌉ ≤ (a + (b - 1))/b,                             (3.7)
⌊a/b⌋ ≥ (a - (b - 1))/b.                             (3.8)

For any integer n and real number x, we have

x ≤ n implies ⌊x⌋ ≤ n,                               (3.9)
n ≤ x implies n ≤ ⌈x⌉.                               (3.10)

**Page 105**

### Modular arithmetic

For any integer a and any positive integer n, the value a mod n is the remainder (or residue) of the quotient a/n:

a mod n = a - n⌊a/n⌋.                                 (3.11)

It follows that

0 ≤ a mod n < n,                                      (3.12)

even when a is negative.

Given a well-defined notion of the remainder of one integer when divided by another, it is convenient to provide special notation to indicate equality of remainders. If (a mod n) = (b mod n), we write a ≡ b (mod n) and say that a is **equivalent** to b, modulo n. In other words, a ≡ b (mod n) if a and b have the same remainder when divided by n. Equivalently, a ≡ b (mod n) if and only if n is a divisor of b - a. We write a ≢ b (mod n) if a is not equivalent to b, modulo n.

### Polynomials

Given a nonnegative integer d, a **polynomial in n of degree d** is a function p(n) of the form

p(n) = ∑(i=0 to d) aᵢnⁱ,

where the constants a₀, a₁, …, aₐ are the **coefficients** of the polynomial and aₐ ≠ 0. A polynomial is **asymptotically positive** if and only if aₐ > 0. For an asymptotically positive polynomial p(n) of degree d, we have p(n) = Θ(nᵈ). For any real constant a ≥ 0, the function nᵃ is monotonically increasing, and for any real constant a ≤ 0, the function nᵃ is monotonically decreasing. We say that a function f(n) is **polynomially bounded** if f(n) = O(nᵏ) for some constant k.

**Page 106**

### Exponentials

For all real a > 0, m, and n, we have the following identities:

- a⁰ = 1,
- a¹ = a,
- a⁻¹ = 1/a,
- (aᵐ)ⁿ = aᵐⁿ,
- (aᵐ)ⁿ = (aⁿ)ᵐ,
- aᵐaⁿ = aᵐ⁺ⁿ.

For all n and a ≥ 1, the function aⁿ is monotonically increasing in n. When convenient, we assume that 0⁰ = 1.

We can relate the rates of growth of polynomials and exponentials by the following fact. For all real constants a > 1 and b, we have

lim(n→∞) nᵇ/aⁿ = 0,                                   (3.13)

from which we can conclude that

nᵇ = o(aⁿ).

Thus, any exponential function with a base strictly greater than 1 grows faster than any polynomial function.

Using e to denote 2.71828 …, the base of the natural-logarithm function, we have for all real x,

eˣ = 1 + x + x²/2! + x³/3! + ⋯ = ∑(i=0 to ∞) xⁱ/i!,  (3.14)

where "!" denotes the factorial function defined later in this section. For all real x, we have the inequality

eˣ ≥ 1 + x,                                           (3.15)

**Page 107**

where equality holds only when x = 0. When |x| ≤ 1, we have the approximation

1 + x ≤ eˣ ≤ 1 + x + x².                              (3.16)

When x → 0, the approximation of eˣ by 1 + x is quite good:

eˣ = 1 + x + Θ(x²).

(In this equation, the asymptotic notation is used to describe the limiting behavior as x → 0 rather than as x → ∞.) We have for all x,

lim(n→∞) (1 + x/n)ⁿ = eˣ.                             (3.17)

### Logarithms

We use the following notations:
- lg n = log₂ n (binary logarithm),
- ln n = logₑ n (natural logarithm),
- lgᵏ n = (lg n)ᵏ (exponentiation),
- lg lg n = lg(lg n) (composition).

We adopt the following notational convention: in the absence of parentheses, a logarithm function applies only to the next term in the formula, so that lg n + 1 means (lg n) + 1 and not lg(n + 1).

For any constant b > 1, the function log_b n is undefined if n ≤ 0, strictly increasing if n > 0, negative if 0 < n < 1, positive if n > 1, and 0 if n = 1. For all real a > 0, b > 0, c > 0, and n, we have

a = b^(log_b a),                                       (3.18)
log_c(ab) = log_c a + log_c b,                        (3.19)
log_b aⁿ = n log_b a,                                 (3.20)

**Page 108**

log_b a = 1/log_a b,                                  (3.21)
log_b a = (log_c a)/(log_c b),                        (3.22)
a^(log_b c) = c^(log_b a),                            (3.23)

where, in each equation above, logarithm bases are not 1.

By equation (3.19), changing the base of a logarithm from one constant to another changes the value of the logarithm by only a constant factor. Consequently, we often use the notation "lg n" when we don't care about constant factors, such as in O-notation. Computer scientists find 2 to be the most natural base for logarithms because so many algorithms and data structures involve splitting a problem into two parts.

There is a simple series expansion for ln(1 + x) when |x| < 1:

ln(1 + x) = x - x²/2 + x³/3 - x⁴/4 + x⁵/5 - ⋯.

We also have the following inequalities for x > -1:

x/(1 + x) ≤ ln(1 + x) ≤ x,                            (3.24)

where equality holds only for x = 0.

We say that a function f(n) is **polylogarithmically bounded** if f(n) = O(lgᵏ n) for some constant k. We can relate the growth of polynomials and polylogarithms by substituting lg n for n and 2ᵃ for a in equation (3.13). For all real constants a > 0 and b, we have

lgᵇ n = o(nᵃ).                                        (3.25)

Thus, any positive polynomial function grows faster than any polylogarithmic function.

**Page 109**

### Factorials

The notation n! (read "n factorial") is defined for integers n ≥ 0 as

n! = {1                if n = 0,
     {n · (n - 1)!     if n > 0.

Thus, n! = 1 · 2 · 3 ⋯ n.

A weak upper bound on the factorial function is n! ≤ nⁿ, since each of the n terms in the factorial product is at most n. **Stirling's approximation**,

n! = √(2πn)(n/e)ⁿ(1 + Θ(1/n)),                       (3.26)

where e is the base of the natural logarithm, gives us a tighter upper bound, and a lower bound as well. Exercise 3.3-4 asks you to prove the three facts

n! = o(nⁿ),                                           (3.27)
n! = ω(2ⁿ),                                           (3.28)
lg(n!) = Θ(n lg n),                                   (3.29)

where Stirling's approximation is helpful in proving equation (3.28). The following equation also holds for all n ≥ 1:

n! = √(2πn)(n/e)ⁿe^(αₙ),                              (3.30)

where

1/(12n + 1) < αₙ < 1/(12n).

### Functional iteration

We use the notation f⁽ⁱ⁾(n) to denote the function f(n) iteratively applied i times to an initial value of n. Formally, let f(n) be a function over the reals. For nonnegative integers i, we recursively define

**Page 110**

f⁽ⁱ⁾(n) = {n             if i = 0,
          {f(f⁽ⁱ⁻¹⁾(n))  if i > 0.

For example, if f(n) = 2n, then f⁽ⁱ⁾(n) = 2ⁱn.

### The iterated logarithm function

We use the notation lg*n (read "log star of n") to denote the iterated logarithm, defined as follows. Let lg⁽ⁱ⁾ n be as defined above, with f(n) = lg n. Because the logarithm of a nonpositive number is undefined, lg⁽ⁱ⁾ n is defined only if lg⁽ⁱ⁻¹⁾ n > 0. Be sure to distinguish lg⁽ⁱ⁾ n (the logarithm function applied i times in succession, starting with argument n) from lgⁱ n (the logarithm of n raised to the ith power). Then we define the iterated logarithm function as

lg*n = min{i ≥ 0 : lg⁽ⁱ⁾ n ≤ 1}.

The iterated logarithm is a very slowly growing function:
- lg* 2 = 1,
- lg* 4 = 2,
- lg* 16 = 3,
- lg* 65536 = 4,
- lg*(2^65536) = 5.

Since the number of atoms in the observable universe is estimated to be about 10⁸⁰, which is much less than 2^65536 ≈ 10^19,728, we rarely encounter an input size n for which lg* n > 5.

### Fibonacci numbers

We define the Fibonacci numbers Fᵢ, for i ≥ 0, as follows:

**Page 111**

F₀ = 0,
F₁ = 1,
Fᵢ = Fᵢ₋₁ + Fᵢ₋₂ for i ≥ 2.

Thus, after the first two, each Fibonacci number is the sum of the two previous ones, yielding the sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ….

Fibonacci numbers are related to the **golden ratio** φ and its conjugate φ̂, which are the two roots of the equation

x² = x + 1.

As Exercise 3.3-7 asks you to prove, the golden ratio is given by

φ = (1 + √5)/2 = 1.61803…                             (3.31)

and its conjugate, by

φ̂ = (1 - √5)/2 = -0.61803….                          (3.32)

Specifically, we have

Fᵢ = (φⁱ - φ̂ⁱ)/√5,                                   (3.33)

which can be proved by induction (Exercise 3.3-8). Since |φ̂| < 1, we have

|φ̂ⁱ|/√5 < 1/√5 < 1/2,

which implies that

**Page 112**

Fᵢ = ⌊φⁱ/√5 + 1/2⌋,                                   (3.34)

which is to say that the ith Fibonacci number Fᵢ is equal to φⁱ/√5 rounded to the nearest integer. Thus, Fibonacci numbers grow exponentially.

### Exercises

**3.3-1**
Show that if f(n) and g(n) are monotonically increasing functions, then so are the functions f(n) + g(n) and f(g(n)), and if f(n) and g(n) are in addition nonnegative, then f(n) · g(n) is monotonically increasing.

**3.3-2**
Prove that ⌊αn⌋ + ⌈(1 - α)n⌉ = n for any integer n and real number α in the range 0 ≤ α ≤ 1.

**3.3-3**
Use equation (3.14) or other means to show that (n + o(n))ᵏ = Θ(nᵏ) for any real constant k. Conclude that ⌈n⌉ᵏ = Θ(nᵏ) and ⌊n⌋ᵏ = Θ(nᵏ).

**3.3-4**
Prove the following:
a. Equation (3.21).
b. Equations (3.26)-(3.28).
c. lg(Θ(n)) = Θ(lg n).

★ **3.3-5**
Is the function ⌈lg n⌉! polynomially bounded? Is the function ⌈lg lg n⌉! polynomially bounded?

★ **3.3-6**
Which is asymptotically larger: lg(lg* n) or lg*(lg n)?

**Page 113**

**3.3-7**
Show that the golden ratio φ and its conjugate φ̂ both satisfy the equation x² = x + 1.

**3.3-8**
Prove by induction that the ith Fibonacci number satisfies the equation

Fᵢ = (φⁱ - φ̂ⁱ)/√5,

where φ is the golden ratio and φ̂ is its conjugate.

**3.3-9**
Show that k lg k = Θ(n) implies k = Θ(n/lg n).

---

## Problems

**Page 113**

**3-1 Asymptotic behavior of polynomials**

Let

p(n) = ∑(i=0 to d) aᵢnⁱ,

where aₐ > 0, be a degree-d polynomial in n, and let k be a constant. Use the definitions of the asymptotic notations to prove the following properties.

a. If k ≥ d, then p(n) = O(nᵏ).
b. If k ≤ d, then p(n) = Ω(nᵏ).
c. If k = d, then p(n) = Θ(nᵏ).
d. If k > d, then p(n) = o(nᵏ).
e. If k < d, then p(n) = ω(nᵏ).

**3-2**

**Page 114**

**Relative asymptotic growths**

Indicate, for each pair of expressions (A, B) in the table below whether A is O, o, Ω, ω, or Θ of B. Assume that k ≥ 1, ϵ > 0, and c > 1 are constants. Write your answer in the form of the table with "yes" or "no" written in each box.

| A | B | O | o | Ω | ω | Θ |
|---|---|---|---|---|---|---|
| lgᵏ n | nᵉ |   |   |   |   |   |
| nᵏ | cⁿ |   |   |   |   |   |
| √n | n^(sin n) |   |   |   |   |   |
| 2ⁿ | 2^(n/2) |   |   |   |   |   |
| n^(lg c) | c^(lg n) |   |   |   |   |   |
| lg(n!) | lg(nⁿ) |   |   |   |   |   |

**3-3 Ordering by asymptotic growth rates**

a. Rank the following functions by order of growth. That is, find an arrangement g₁, g₂, …, g₃₀ of the functions satisfying g₁ = Ω(g₂), g₂ = Ω(g₃), …, g₂₉ = Ω(g₃₀). Partition your list into equivalence classes such that functions f(n) and g(n) belong to the same class if and only if f(n) = Θ(g(n)).

lg(lg* n)   2^(lg* n)   (√2)^(lg n)   n²   n!   (lg n)!   (3/2)ⁿ   n³   lg² n   lg(n!)   2^(2ⁿ)   n^(1/lg n)
n·2ⁿ   n^(lg lg n)   ln ln n   lg* n   n   2^(lg n)   (lg n)^(lg n)   eⁿ   4^(lg n)   (n+1)!   √(lg n)
lg*(lg n)   2^(√(2 lg n))   n   2ⁿ   n lg n   2^(2^(n+1))

b. Give an example of a single nonnegative function f(n) such that for all functions gᵢ(n) in part (a), f(n) is neither O(gᵢ(n)) nor Ω(gᵢ(n)).

**Page 115**

**3-4 Asymptotic notation properties**

Let f(n) and g(n) be asymptotically positive functions. Prove or disprove each of the following conjectures.

a. f(n) = O(g(n)) implies g(n) = O(f(n)).
b. f(n) + g(n) = Θ(min{f(n), g(n)}).
c. f(n) = O(g(n)) implies lg f(n) = O(lg g(n)), where lg g(n) ≥ 1 and f(n) ≥ 1 for all sufficiently large n.
d. f(n) = O(g(n)) implies 2^f(n) = O(2^g(n)).
e. f(n) = O((f(n))²).
f. f(n) = O(g(n)) implies g(n) = Ω(f(n)).
g. f(n) = Θ(f(n/2)).
h. f(n) + o(f(n)) = Θ(f(n)).

**3-5 Manipulating asymptotic notation**

Let f(n) and g(n) be asymptotically positive functions. Prove the following identities:

a. Θ(Θ(f(n))) = Θ(f(n)).
b. Θ(f(n)) + O(f(n)) = Θ(f(n)).
c. Θ(f(n)) + Θ(g(n)) = Θ(f(n) + g(n)).
d. Θ(f(n)) · Θ(g(n)) = Θ(f(n) · g(n)).
e. Argue that for any real constants a₁, b₁ > 0 and integer constants k₁, k₂, the following asymptotic bound holds:

(a₁n)^k₁ lg^k₂ n = Θ(n^k₁ lg^k₂ n).

★ f. Prove that for S ⊆ Z, we have

**Page 116**

Θ(∑(k∈S) f(k)) = ∑(k∈S) Θ(f(k)),

assuming that both sums converge.

★ g. Show that for S ⊆ Z, the following asymptotic bound does not necessarily hold, even assuming that both products converge, by giving a counterexample:

Θ(∏(k∈S) f(k)) ≠ ∏(k∈S) Θ(f(k)).

**3-6 Variations on O and Ω**

Some authors define Ω-notation in a slightly different way than this textbook does. We'll use the nomenclature Ω̃ (read "omega infinity") for this alternative definition. We say that f(n) = Ω̃(g(n)) if there exists a positive constant c such that f(n) ≥ cg(n) ≥ 0 for infinitely many integers n.

a. Show that for any two asymptotically nonnegative functions f(n) and g(n), we have f(n) = O(g(n)) or f(n) = Ω̃(g(n)) (or both).
b. Show that there exist two asymptotically nonnegative functions f(n) and g(n) for which neither f(n) = O(g(n)) nor f(n) = Ω(g(n)) holds.
c. Describe the potential advantages and disadvantages of using Ω̃-notation instead of Ω-notation to characterize the running times of programs.

Some authors also define O in a slightly different manner. We'll use O' for the alternative definition: f(n) = O'(g(n)) if and only if |f(n)| = O(g(n)).

d. What happens to each direction of the "if and only if" in Theorem 3.1 on page 56 if we substitute O' for O but still use Ω?

Some authors define Õ (read "soft-oh") to mean O with logarithmic factors ignored:

Õ(g(n)) = {f(n) : there exist positive constants c, k, and n₀

**Page 117**

such that 0 ≤ f(n) ≤ cg(n) lg^k(n) for all n ≥ n₀}.

e. Define Ω̃ and Θ̃ in a similar manner. Prove the corresponding analog to Theorem 3.1.

**3-7 Iterated functions**

We can apply the iteration operator * used in the lg* function to any monotonically increasing function f(n) over the reals. For a given constant c ∈ R, we define the iterated function f*_c by

f*_c(n) = min{i ≥ 0 : f^(i)(n) ≤ c},

which need not be well defined in all cases. In other words, the quantity f*_c(n) is the minimum number of iterated applications of the function f required to reduce its argument down to c or less.

For each of the functions f(n) and constants c in the table below, give as tight a bound as possible on f*_c(n). If there is no i such that f^(i)(n) ≤ c, write "undefined" as your answer.

| | f(n) | c | f*_c(n) |
|---|------|---|---------|
| a. | n-1 | 0 | |
| b. | lg n | 1 | |
| c. | n/2 | 1 | |
| d. | n/2 | 2 | |
| e. | √n | 2 | |
| f. | √n | 1 | |
| g. | n^(1/3) | 2 | |

---

## Chapter notes

**Page 117-118**

Knuth [259] traces the origin of the O-notation to a number-theory text by P. Bachmann in 1892. The o-notation was invented by E. Landau in 1909 for his discussion of the distribution of prime numbers. The Ω and Θ notations were advocated by Knuth [265] to correct the popular, but technically sloppy, practice in the literature of using O-notation for both upper and lower bounds. As noted earlier in this chapter, many people continue to use the O-notation where the Θ-notation is more technically precise. The soft-oh notation in Problem 3-6 was introduced by Babai, Luks, and Seress [31], although it was originally written as Õ. Some authors now define Õ as ignoring factors that are logarithmic in g(n), rather than in n. With this definition, we can say that n² lg³ n = Õ(n²), but with the definition in Problem 3-6, this statement is not true.

Further discussion of the history and development of asymptotic notations appears in works by Knuth [259, 265] and Brassard and Bratley [70].

Not all authors define the asymptotic notations in the same way, although the various definitions agree in most common situations. Some of the alternative definitions encompass functions that are not asymptotically nonnegative, as long as their absolute values are appropriately bounded.

Equation (3.29) is due to Robbins [381]. Other properties of elementary mathematical functions can be found in any good mathematical reference, such as Abramowitz and Stegun [1] or Zwillinger [468], or in a calculus book, such as Apostol [19] or Thomas et al. [433]. Knuth [259] and Graham, Knuth, and Patashnik [199] contain a wealth of material on discrete mathematics as used in computer science.

---

## Footnotes

¹ Within set notation, a colon means "such that."