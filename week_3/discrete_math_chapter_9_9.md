# Chapter 9.9: Conditional Probability, Bayes' Formula, and Independent Events

## Introduction

*It is remarkable that a science which began with the consideration of games of chance should have become the most important object of human knowledge... The most important questions of life are, for the most part, really only problems of probability.*
— Pierre-Simon Laplace (1749–1827)

In this section we introduce the notion of conditional probability and discuss Bayes' Theorem and the kind of interesting results to which it leads. We then define the concept of independent events and give some applications.

## Conditional Probability

Imagine a couple with two children, each of whom is equally likely to be a boy or a girl. Now suppose you are given the information that one is a boy. What is the probability that the other child is a boy?

Figure 9.9.1 shows the four equally likely combinations of gender for the children. You can imagine that the first letter refers to the older child and the second letter to the younger.

```
BB    BG    GB    GG
```

The combinations where one of the children is a boy are shaded gray, and the combination where the other child is also a boy is shaded blue-gray. Given that you know one child is a boy, only the three combinations in the gray region could be the case, so you can think of the set of those outcomes as a new sample space with three elements, all of which are equally likely. Within the new sample space, there is one combination where the other child is a boy (in the region shaded blue-gray). Thus it would be reasonable to say that the likelihood that the other child is a boy, given that at least one is a boy, is 1/3 = 33⅓%.

Note that because the original sample space contained four outcomes,
P(at least one child is a boy and the other child is also a boy) / P(at least one child is a boy) = (1/4)/(3/4) = 1/3

A generalization of this observation forms the basis for the following definition.

**Definition 9.9.1: Conditional Probability**
Let A and B be events in a sample space S. If P(A) ≠ 0, then the conditional probability of B given A, denoted P(B | A), is:
**P(B | A) = P(A ∩ B) / P(A)**

### Example 9.9.1: Computing a Conditional Probability
A pair of fair dice, one blue and the other gray, are rolled. What is the probability that the sum of the numbers showing face up is 8, given that both of the numbers are even?

**Solution:**
The sample space is the set of all 36 outcomes obtained from rolling the two dice and noting the numbers showing face up on each. As in Section 9.1, denote by ab the outcome that the number showing face up on the blue die is a and the one on the gray die is b.

Let A be the event that both numbers are even and B the event that the sum of the numbers is 8. Then:
- A = {22, 24, 26, 42, 44, 46, 62, 64, 66}
- B = {26, 35, 44, 53, 62}
- A ∩ B = {26, 44, 62}

Because the dice are fair (so all outcomes are equally likely):
- P(A) = 9/36
- P(B) = 5/36
- P(A ∩ B) = 3/36

By definition of conditional probability:
P(B | A) = P(A ∩ B) / P(A) = (3/36) / (9/36) = 3/9 = 1/3

**Important Formulas Derived from Conditional Probability:**
1. **Formula 9.9.2**: P(A ∩ B) = P(B | A) · P(A)
2. **Formula 9.9.3**: P(A) = P(A ∩ B) / P(B | A)

### Example 9.9.2: Representing Conditional Probabilities with a Tree Diagram
An urn contains 5 blue and 7 gray balls. Let us say that 2 are chosen at random, one after the other, without replacement.

a. Find the following probabilities and illustrate them with a tree diagram: the probability that both balls are blue, the probability that the first ball is blue and the second is not blue, the probability that the first ball is not blue and the second ball is blue, and the probability that neither ball is blue.
b. What is the probability that the second ball is blue?
c. What is the probability that at least one of the balls is blue?
d. If the experiment of choosing two balls from the urn were repeated many times over, what would be the expected value of the number of blue balls?

**Solution:**
Let S denote the sample space of all possible choices of two balls from the urn, let B₁ be the event that the first ball is blue, and let B₂ be the event that the second ball is blue. Then B₁ᶜ is the event that the first ball is not blue and B₂ᶜ is the event that the second ball is not blue.

a. Because there are 12 balls of which 5 are blue and 7 are gray:
- P(B₁) = 5/12
- P(B₁ᶜ) = 7/12

If the first ball is blue, then the urn would contain 4 blue balls and 7 gray balls, and so:
- P(B₂ | B₁) = 4/11
- P(B₂ᶜ | B₁) = 7/11

where P(B₂ | B₁) is the probability that the second ball is blue given that the first ball is blue and P(B₂ᶜ | B₁) is the probability that the second ball is not blue given that the first ball is blue.

It follows from formula (9.9.2) that:
- P(B₁ ∩ B₂) = P(B₂ | B₁) · P(B₁) = (4/11) · (5/12) = 20/132
- P(B₁ ∩ B₂ᶜ) = P(B₂ᶜ | B₁) · P(B₁) = (7/11) · (5/12) = 35/132

Similarly, if the first ball is not blue, then the urn would contain 5 blue balls and 6 gray balls, and so:
- P(B₂ | B₁ᶜ) = 5/11
- P(B₂ᶜ | B₁ᶜ) = 6/11

where P(B₂ | B₁ᶜ) is the probability that the second ball is blue given that the first ball is not blue and P(B₂ᶜ | B₁ᶜ) is the probability that the second ball is not blue given that the first ball is not blue.

It follows from formula (9.9.2) that:
- P(B₁ᶜ ∩ B₂) = P(B₂ | B₁ᶜ) · P(B₁ᶜ) = (5/11) · (7/12) = 35/132
- P(B₁ᶜ ∩ B₂ᶜ) = P(B₂ᶜ | B₁ᶜ) · P(B₁ᶜ) = (6/11) · (7/12) = 42/132

The tree diagram in Figure 9.9.2 illustrates these results:
```
P(B₂|B₁) = 4/11         P(B₂ᶜ|B₁) = 7/11
B₁ ──────── B₂             B₁ ──────── B₂ᶜ
│           │              │           │
│           │              │           │
P(B₁) = 5/12│           20/132         35/132
│           │              │           │
│           │              │           │
P(B₁ᶜ) = 7/12│           35/132         42/132
│           │              │           │
│           │              │           │
B₁ᶜ ──────── B₂             B₁ᶜ ──────── B₂ᶜ
P(B₂|B₁ᶜ) = 5/11         P(B₂ᶜ|B₁ᶜ) = 6/11
```

b. The event that the second ball is blue can occur in one of two mutually exclusive ways: Either the first ball is blue and the second is also blue, or the first ball is gray and the second is blue. In other words, B₂ is the disjoint union of B₂ ∩ B₁ and B₂ ∩ B₁ᶜ.

Hence:
P(B₂) = P((B₂ ∩ B₁) ∪ (B₂ ∩ B₁ᶜ)) = P(B₂ ∩ B₁) + P(B₂ ∩ B₁ᶜ)  [by probability axiom 3]
     = 20/132 + 35/132 = 55/132 = 5/12

Thus the probability that the second ball is blue is 5/12, the same as the probability that the first ball is blue.

c. By formula 9.8.2, for the union of any two events:
P(B₁ ∪ B₂) = P(B₁) + P(B₂) - P(B₁ ∩ B₂) = 5/12 + 5/12 - 20/132 = 90/132 = 15/22

Thus the probability is 15/22, or approximately 68.2%, that at least one of the balls is blue.

d. The event that neither ball is blue is the complement of the event that at least one of the balls is blue, so:
P(0 blue balls) = 1 - P(at least one ball is blue) = 1 - 15/22 = 7/22  [by formula 9.8.1]

The event that one ball is blue can occur in one of two mutually exclusive ways: Either the second ball is blue and the first is not, or the first ball is blue and the second is not. Part (a) showed that the probability of the first way is 35/132, and the probability of the second way is also 35/132. Thus, by probability axiom 3:
P(1 blue ball) = 35/132 + 35/132 = 70/132

Finally, by part (a):
P(2 blue balls) = 20/132

Therefore:
the expected value of the number of blue balls = 0 · P(0 blue balls) + 1 · P(1 blue ball) + 2 · P(2 blue balls)
                                         = 0 · (7/22) + 1 · (70/132) + 2 · (20/132)
                                         = 110/132 ≈ 0.8

## Bayes' Theorem

Suppose that one urn contains 3 blue and 4 gray balls and a second urn contains 5 blue and 3 gray balls. A ball is selected by choosing one of the urns at random and then picking a ball at random from that urn. If the chosen ball is blue, what is the probability that it came from the first urn?

This problem can be solved by carefully interpreting all the information that is known and putting it together in just the right way. Let A be the event that the chosen ball is blue, B₁ the event that the ball came from the first urn, and B₂ the event that the ball came from the second urn.

Because 3 of the 7 balls in urn one are blue, and 5 of the 8 balls in urn two are blue:
- P(A | B₁) = 3/7
- P(A | B₂) = 5/8

And because the urns are equally likely to be chosen:
- P(B₁) = P(B₂) = 1/2

Moreover, by formula (9.9.2):
- P(A ∩ B₁) = P(A | B₁) · P(B₁) = (3/7) · (1/2) = 3/14
- P(A ∩ B₂) = P(A | B₂) · P(B₂) = (5/8) · (1/2) = 5/16

But A is the disjoint union of (A ∩ B₁) and (A ∩ B₂), so by probability axiom 3:
P(A) = P((A ∩ B₁) ∪ (A ∩ B₂)) = P(A ∩ B₁) + P(A ∩ B₂) = 3/14 + 5/16 = 59/112

Finally, by definition of conditional probability:
P(B₁ | A) = P(B₁ ∩ A) / P(A) = (3/14) / (59/112) = 336/826 ≈ 40.7%

Thus, if the chosen ball is blue, the probability is approximately 40.7% that it came from the first urn.

The steps used to derive the answer in the previous example can be generalized to prove Bayes' Theorem. Thomas Bayes was an English Presbyterian minister who devoted much of his energies to mathematics. The theorem that bears his name was published posthumously in 1763.

**Theorem 9.9.1: Bayes' Theorem**
Suppose that a sample space S is a union of mutually disjoint events B₁, B₂, B₃, ..., Bₙ, suppose A is an event in S, and suppose A and all the Bᵢ have nonzero probabilities. If k is an integer with 1 ≤ k ≤ n, then:
**P(Bₖ | A) = P(A | Bₖ)P(Bₖ) / [P(A | B₁)P(B₁) + P(A | B₂)P(B₂) + · · · + P(A | Bₙ)P(Bₙ)]**

### Example 9.9.3: Applying Bayes' Theorem
Most medical tests occasionally produce incorrect results, called false positives and false negatives. When a test is designed to determine whether a patient has a certain disease, a false positive result indicates that a patient has the disease when the patient does not have it. A false negative result indicates that a patient does not have the disease when the patient does have it.

When large-scale health screenings are performed for diseases with relatively low incidence, those who develop the screening procedures have to balance several considerations: the per-person cost of the screening, follow-up costs for further testing of false positives, and the possibility that people who have the disease will develop unwarranted confidence in the state of their health.

Consider a medical test that screens for a disease found in 5 people in 1,000. Suppose that the false positive rate is 3% and the false negative rate is 1%. Then 99% of the time a person who has the condition tests positive for it, and 97% of the time a person who does not have the condition tests negative for it.

a. What is the probability that a randomly chosen person who tests positive for the disease actually has the disease?
b. What is the probability that a randomly chosen person who tests negative for the disease does not indeed have the disease?

**Solution:**
Consider a person chosen at random from among those screened. Let A be the event that the person tests positive for the disease, B₁ the event that the person actually has the disease, and B₂ the event that the person does not have the disease. Then:
- P(A | B₁) = 0.99
- P(Aᶜ | B₁) = 0.01
- P(Aᶜ | B₂) = 0.97
- P(A | B₂) = 0.03

Also, because 5 people in 1,000 have the disease:
- P(B₁) = 0.005
- P(B₂) = 0.995

a. By Bayes' Theorem:
P(B₁ | A) = P(A | B₁)P(B₁) / [P(A | B₁)P(B₁) + P(A | B₂)P(B₂)]
          = (0.99)(0.005) / [(0.99)(0.005) + (0.03)(0.995)]
          = 0.00495 / (0.00495 + 0.02985)
          = 0.00495 / 0.0348
          ≈ 0.1422 ≈ 14.2%

Thus the probability that a person with a positive test result actually has the disease is approximately 14.2%.

b. By Bayes' Theorem:
P(B₂ | Aᶜ) = P(Aᶜ | B₂)P(B₂) / [P(Aᶜ | B₁)P(B₁) + P(Aᶜ | B₂)P(B₂)]
           = (0.97)(0.995) / [(0.01)(0.005) + (0.97)(0.995)]
           = 0.96515 / (0.00005 + 0.96515)
           = 0.96515 / 0.9652
           ≈ 0.999948 ≈ 99.995%

Thus the probability that a person with a negative test result does not have the disease is approximately 99.995%.

You might be surprised by these numbers, but they are fairly typical of the situation where the screening test is significantly less expensive than a more accurate test for the same disease yet produces positive results for nearly all people with the disease. Using the screening test limits the expense of unnecessarily using the more costly test to a relatively small percentage of the population being screened, while only rarely indicating that a person who has the disease is free of it.

## Independent Events

Suppose a coin is tossed twice. It seems intuitively clear that the outcome of the first toss does not depend in any way on the outcome of the second toss, and conversely. In other words, if, for instance, A is the event that a head is obtained on the first toss and B is the event that a head is obtained on the second toss, then if the coin is tossed randomly both times, events A and B should be independent in the sense that P(A | B) = P(A) and P(B | A) = P(B).

This intuitive idea of independence is supported by the following analysis. If the coin is fair, then the four outcomes HH, HT, TH, and TT are equally likely, and:
- A = {HH, HT}, B = {TH, HH}, A ∩ B = {HH}

Hence:
- P(A) = P(B) = 2/4 = 1/2

But also:
- P(A | B) = P(A ∩ B) / P(B) = (1/4) / (1/2) = 1/2
- P(B | A) = P(A ∩ B) / P(A) = (1/4) / (1/2) = 1/2

And thus P(A | B) = P(A) and P(B | A) = P(B).

To obtain the final form for the definition of independence, observe that:
- If P(B) ≠ 0 and P(A | B) = P(A), then P(A ∩ B) = P(A | B) · P(B) = P(A) · P(B)
- By the same argument, if P(A) ≠ 0 and P(B | A) = P(B), then P(A ∩ B) = P(A) · P(B)

Conversely (see exercise 18 at the end of this section):
- If P(A ∩ B) = P(A) · P(B) and P(A) ≠ 0, then P(B | A) = P(B)
- If P(A ∩ B) = P(A) · P(B) and P(B) ≠ 0, then P(A | B) = P(A)

Note: It would be natural to think that mutually disjoint events would be independent, but in fact almost the opposite is true: Mutually disjoint events with nonzero probabilities are dependent.

Thus, for convenience and to eliminate the requirement that the probabilities be nonzero, we use the following product formula to define independent events.

**Definition 9.9.2: Independent Events**
If A and B are events in a sample space S, then A and B are independent if, and only if:
**P(A ∩ B) = P(A) · P(B)**

### Example 9.9.4: Disjoint Events and Independence
Let A and B be events in a sample space S, and suppose A ∩ B = ∅, P(A) ≠ 0, and P(B) ≠ 0. Show that P(A ∩ B) ≠ P(A) · P(B).

**Solution:**
Because A ∩ B = ∅, P(A ∩ B) = 0 by probability axiom 2. But P(A) · P(B) ≠ 0 because neither P(A) nor P(B) equals zero. Thus P(A ∩ B) ≠ P(A) · P(B).

### Example 9.9.5: The Probability of A ∩ Bᶜ When A and B Are Independent Events
Suppose A and B are independent events in a sample space S. Show that A and Bᶜ are also independent.

**Solution:**
The solution for exercises 8 and 25 in Section 6.2 show that for all sets A and B:
1. (A ∩ B) ∪ (A ∩ Bᶜ) = A
2. (A ∩ B) ∩ (A ∩ Bᶜ) = ∅

It follows that probability axiom 3 may be applied to equation (1) to obtain:
P((A ∩ B) ∪ (A ∩ Bᶜ)) = P(A ∩ B) + P(A ∩ Bᶜ) = P(A)

Solving for P(A ∩ Bᶜ) gives that:
P(A ∩ Bᶜ) = P(A) - P(A ∩ B)
           = P(A) - P(A) · P(B)  [because A and B are independent]
           = P(A)(1 - P(B))      [by factoring out P(A)]
           = P(A) · P(Bᶜ)        [by formula 9.8.1]

Thus A and Bᶜ are independent events.

It follows immediately from Example 9.9.5 that if A and B are independent, then Aᶜ and B are also independent and so are Aᶜ and Bᶜ. These results are applied in Example 9.9.6.

### Example 9.9.6: Computing Probabilities of Intersections of Two Independent Events
A coin is loaded so that the probability of heads is 0.6. Suppose the coin is tossed twice. Although the probability of heads is greater than the probability of tails, there is no reason to believe that whether the coin lands heads or tails on one toss will affect whether it lands heads or tails on the other toss. Thus it is reasonable to assume that the results of the tosses are independent.

a. What is the probability of obtaining two heads?
b. What is the probability of obtaining one head?
c. What is the probability of obtaining no heads?
d. What is the probability of obtaining at least one head?

**Solution:**
The sample space S consists of the four outcomes {HH, HT, TH, TT}, which are not equally likely. Let E be the event that a head is obtained on the first toss, and let F be the event that a head is obtained on the second toss. Then P(E) = P(F) = 0.6, and it is to be assumed that E and F are independent.

a. The probability of obtaining two heads is P(E ∩ F). Because E and F are independent:
P(two heads) = P(E ∩ F) = P(E) · P(F) = (0.6)(0.6) = 0.36 = 36%

b. One head can be obtained in two mutually exclusive ways: head on the first toss and tail on the second, or tail on the first toss and head on the second. Thus, the event of obtaining exactly one head is (E ∩ Fᶜ) ∪ (Eᶜ ∩ F). Also (E ∩ Fᶜ) ∩ (Eᶜ ∩ F) = ∅, and, moreover, by the formula for the probability of the complement of an event:
P(Eᶜ) = P(Fᶜ) = 1 - 0.6 = 0.4

Hence:
P(one head) = P((E ∩ Fᶜ) ∪ (Eᶜ ∩ F))
            = P(E) · P(Fᶜ) + P(Eᶜ) · P(F)  [by Example 9.9.5 and exercise 22]
            = (0.6)(0.4) + (0.4)(0.6)
            = 0.48 = 48%

c. The probability of obtaining no heads is P(Eᶜ ∩ Fᶜ). By exercise 22:
P(no heads) = P(Eᶜ ∩ Fᶜ) = P(Eᶜ) · P(Fᶜ) = (0.4)(0.4) = 0.16 = 16%

d. There are two ways to solve this problem. One is to observe that because the event of obtaining one head and the event of obtaining two heads are mutually disjoint:
P(at least one head) = P(one head) + P(two heads)  [by parts (a) and (b)]
                    = 0.48 + 0.36 = 0.84 = 84%

The second way is to use the fact that the event of obtaining at least one head is the complement of the event of obtaining no heads. So:
P(at least one head) = 1 - P(no heads) = 1 - 0.16 = 0.84 = 84%  [by part (c)]

### Example 9.9.7: Expected Value of Tossing a Loaded Coin Twice
Suppose that a coin is loaded so that the probability of heads is 0.6, and suppose the coin is tossed twice. If this experiment is repeated many times, what is the expected value of the number of heads?

**Solution:**
Think of the outcomes of the coin tossings as just 0, 1, or 2 heads. Example 9.9.6 showed that the probabilities of these outcomes are 0.16, 0.48, and 0.36, respectively. Thus, by definition of expected value:
the expected number of heads = 0 · (0.16) + 1 · (0.48) + 2 · (0.36) = 1.2

## Independence for Multiple Events

What if a loaded coin is tossed more than twice? Suppose it is tossed ten times, or a hundred times. What are the probabilities of various numbers of heads? To answer this question, it is necessary to expand the notion of independence to more than two events.

For instance, we say three events A, B, and C are pairwise independent if, and only if:
- P(A ∩ B) = P(A) · P(B)
- P(A ∩ C) = P(A) · P(C)
- P(B ∩ C) = P(B) · P(C)

The next example shows that events can be pairwise independent without satisfying the condition P(A ∩ B ∩ C) = P(A) · P(B) · P(C). Conversely, they can satisfy the condition P(A ∩ B ∩ C) = P(A) · P(B) · P(C) without being pairwise independent.

### Example 9.9.8: Exploring Independence for Three Events
Suppose that a fair coin is tossed twice. Let A be the event that a head is obtained on the first toss, B the event that a head is obtained on the second toss, and C the event that either two heads or two tails are obtained. Show that A, B, and C are pairwise independent but do not satisfy the condition P(A ∩ B ∩ C) = P(A) · P(B) · P(C).

**Solution:**
Because there are four equally likely outcomes—HH, HT, TH, and TT—it is clear that P(A) = P(B) = P(C) = 1/2. You can also see that:
- A ∩ B = {HH}
- A ∩ C = {HH}
- B ∩ C = {HH}
- A ∩ B ∩ C = {HH}

Hence P(A ∩ B) = P(A ∩ C) = P(B ∩ C) = 1/4, and so P(A ∩ B) = P(A) · P(B), P(A ∩ C) = P(A) · P(C), and P(B ∩ C) = P(B) · P(C). Thus A, B, and C are pairwise independent.

But P(A ∩ B ∩ C) = P({HH}) = 1/4 ≠ (1/2)³ = P(A) · P(B) · P(C).

Because of situations like that in Example 9.9.8, four conditions must be included in the definition of independence for three events.

**Definition 9.9.3: Independence for Three Events**
Let A, B, and C be events in a sample space S. A, B, and C are pairwise independent if, and only if, they satisfy conditions 1–3 below. They are mutually independent if, and only if, they satisfy all four conditions below.

1. P(A ∩ B) = P(A) · P(B)
2. P(A ∩ C) = P(A) · P(C)
3. P(B ∩ C) = P(B) · P(C)
4. P(A ∩ B ∩ C) = P(A) · P(B) · P(C)

**Definition 9.9.4: Mutual Independence for n Events**
Events A₁, A₂, A₃, ..., Aₙ in a sample space S are mutually independent if, and only if, the probability of the intersection of any subset of the events is the product of the probabilities of the events in the subset.

### Example 9.9.9: Tossing a Loaded Coin Ten Times
A coin is loaded so that the probability of heads is 0.6 (and thus the probability of tails is 0.4). Suppose the coin is tossed ten times. As in Example 9.9.6, it is reasonable to assume that the results of the tosses are mutually independent.

a. What is the probability of obtaining eight heads?
b. What is the probability of obtaining at least eight heads?

**Solution:**
a. For each i = 1, 2, ..., 10, let Hᵢ be the event that a head is obtained on the ith toss, and let Tᵢ be the event that a tail is obtained on the ith toss. Suppose that the eight heads occur on the first eight tosses and that the remaining two tosses are tails. This is the event H₁ ∩ H₂ ∩ H₃ ∩ H₄ ∩ H₅ ∩ H₆ ∩ H₇ ∩ H₈ ∩ T₉ ∩ T₁₀. For simplicity, we denote it as HHHHHHHHTT.

By definition of mutually independent events:
P(HHHHHHHHTT) = (0.6)⁸(0.4)²

Because of the commutative law for multiplication, if the eight heads occur on any other of the ten tosses, the same number is obtained. For instance, if we denote the event H₁ ∩ H₂ ∩ T₃ ∩ H₄ ∩ H₅ ∩ H₆ ∩ H₇ ∩ H₈ ∩ T₉ ∩ H₁₀ by HHTHHHHHTH, then:
P(HHTHHHHHTH) = (0.6)²(0.4)(0.6)⁵(0.4)(0.6) = (0.6)⁸(0.4)²

Now there are as many different ways to obtain eight heads in ten tosses as there are subsets of eight elements (the toss numbers on which heads are obtained) that can be chosen from a set of ten elements. This number is C(10,8) = 10!/(8!2!) = 45.

It follows that, because the different ways of obtaining eight heads are all mutually exclusive:
P(eight heads) = C(10,8) · (0.6)⁸(0.4)² = 45 · (0.6)⁸(0.4)²

b. By reasoning similar to that in part (a):
- P(nine heads) = C(10,9) · (0.6)⁹(0.4)¹ = 10 · (0.6)⁹(0.4)
- P(ten heads) = C(10,10) · (0.6)¹⁰(0.4)⁰ = 1 · (0.6)¹⁰

Because obtaining eight, obtaining nine, and obtaining ten heads are mutually disjoint events:
P(at least eight heads) = P(eight heads) + P(nine heads) + P(ten heads)
                      = C(10,8) · (0.6)⁸(0.4)² + C(10,9) · (0.6)⁹(0.4) + C(10,10) · (0.6)¹⁰
                      = 45 · (0.6)⁸(0.4)² + 10 · (0.6)⁹(0.4) + (0.6)¹⁰
                      ≈ 0.167 = 16.7%

**Note:** Binomial probabilities occur in situations with multiple, mutually independent repetitions of a random process, all of which have the same two possible outcomes with the same probabilities on each repetition.

Note the occurrence of the binomial coefficients C(n,k) in solutions to problems like the one in Example 9.9.9. For that reason, probabilities of the form:
**P(exactly k successes in n trials) = C(n,k) · pᵏ · (1-p)ⁿ⁻ᵏ**

where 0 ≤ p ≤ 1, are called binomial probabilities.

## Exercise Set 9.9

1. Suppose P(A | B) = 1/2 and P(A ∩ B) = 1/6. What is P(B)?
2. Suppose P(X | Y) = 1/3 and P(Y) = 1/4. What is P(X ∩ Y)?
3. The instructor of a discrete mathematics class gave two tests. Twenty-five percent of the students received an A on the first test and 15% of the students received A's on both tests. What percent of the students who received A's on the first test also received A's on the second test?
4. a. Prove that if A and B are any events in a sample space S, with P(B) ≠ 0, then P(Aᶜ | B) = 1 - P(A | B).
b. Explain how this result justifies the following statements: (1) If the probability of a false positive on a test for a condition is 4%, then there is a 96% probability that a person who does not have the condition will have a negative test result. (2) If the probability of a false negative on a test for a condition is 1%, then there is a 99% probability that a person who does have the condition will test positive for it.
5. Suppose that A and B are events in a sample space S and that P(A), P(B), and P(A | B) are known. Derive a formula for P(A | Bᶜ).
6. An urn contains 25 red balls and 15 blue balls. Two are chosen at random, one after the other, without replacement.
   a. Use a tree diagram to help calculate the following probabilities: the probability that both balls are red, the probability that the first ball is red and the second is not, the probability that the first ball is not red and the second is red, the probability that neither ball is red.
   b. What is the probability that the second ball is red?
   c. What is the probability that at least one of the balls is red?
7. Redo exercise 6 assuming that the urn contains 30 red balls and 40 blue balls.
8. A pool of 10 semifinalists for a job consists of 7 men and 3 women. Because all are considered equally qualified, the names of two of the semifinalists are drawn, one after the other, at random, to become finalists for the job.
   a. What is the probability that both finalists are women?
   b. What is the probability that both finalists are men?
   c. What is the probability that one finalist is a woman and the other is a man?
9. Prove Bayes' Theorem for n = 2. That is, prove that if a sample space S is a union of mutually disjoint events B₁ and B₂, if A is an event in S with P(A) ≠ 0, and if k = 1 or k = 2, then P(Bₖ | A) = P(A | Bₖ)P(Bₖ) / [P(A | B₁)P(B₁) + P(A | B₂)P(B₂)].
10. Prove the full version of Bayes' Theorem.
11. One urn contains 12 blue balls and 7 white balls, and a second urn contains 8 blue balls and 19 white balls. An urn is selected at random, and a ball is chosen from the urn.
    a. What is the probability that the chosen ball is blue?
    b. If the chosen ball is blue, what is the probability that it came from the first urn?
12. Redo exercise 11 assuming that the first urn contains 4 blue balls and 16 white balls and the second urn contains 10 blue balls and 9 white balls.
13. One urn contains 10 red balls and 25 green balls, and a second urn contains 22 red balls and 15 green balls. A ball is chosen as follows: First an urn is selected by tossing a loaded coin with probability 0.4 of landing heads up and probability 0.6 of landing tails up. If the coin lands heads up, the first urn is chosen; otherwise, the second urn is chosen. Then a ball is picked at random from the chosen urn.
    a. What is the probability that the chosen ball is green?
    b. If the chosen ball is green, what is the probability that it was picked from the first urn?
14. A drug-screening test is used in a large population of people of whom 4% actually use drugs. Suppose that the false positive rate is 3% and the false negative rate is 2%. Thus a person who uses drugs tests positive for them 98% of the time, and a person who does not use drugs tests negative for them 97% of the time.
    a. What is the probability that a randomly chosen person who tests positive for drugs actually uses drugs?
    b. What is the probability that a randomly chosen person who tests negative for drugs does not use drugs?
15. Two different factories both produce a certain automobile part. The probability that a component from the first factory is defective is 2%, and the probability that a component from the second factory is defective is 5%. In a supply of 180 of the parts, 100 were obtained from the first factory and 80 from the second factory.
    a. What is the probability that a part chosen at random from the 180 is from the first factory?
    b. What is the probability that a part chosen at random from the 180 is from the second factory?
    c. What is the probability that a part chosen at random from the 180 is defective?
    d. If the chosen part is defective, what is the probability that it came from the first factory?
16. Three different suppliers—X, Y, and Z—provide produce for a grocery store. Twelve percent of produce from X is superior grade, 8% of produce from Y is superior grade and 15% of produce from Z is superior grade. The store obtains 20% of its produce from X, 45% from Y, and 35% from Z.
    a. If a piece of produce is purchased, what is the probability that it is superior grade?
    b. If a piece of produce in the store is superior grade, what is the probability that it is from X?
17. Prove that if A and B are events in a sample space S with the property that P(A | B) = P(A) and P(A) ≠ 0, then P(B | A) = P(B).
18. Prove that if P(A ∩ B) = P(A) · P(B), P(A) ≠ 0, and P(B) ≠ 0, then P(A | B) = P(A) and P(B | A) = P(B).
19. A pair of fair dice, one blue and the other gray, are rolled. Let A be the event that the number face up on the blue die is 2, and let B be the event that the number face up on the gray die is 4 or 5. Show that P(A | B) = P(A) and P(B | A) = P(B).
20. Suppose a fair coin is tossed three times. Let A be the event that a head appears on the first toss, and let B be the event that an even number of heads is obtained. Show that P(A | B) = P(A) and P(B | A) = P(B).
21. If A and B are events in a sample space S and A ∩ B = ∅, what must be true in order for A and B to be independent? Explain.
22. Prove that if A and B are independent events in a sample space S, then Aᶜ and B are also independent, and so are Aᶜ and Bᶜ.
23. A student taking a multiple-choice exam does not know the answers to two questions. All have five choices for the answer. For one of the two questions, the student can eliminate two answer choices as incorrect but has no idea about the other answer choices. For the other question, the student has no clue about the correct answer at all. Assume that whether the student chooses the correct answer on one of the questions does not affect whether the student chooses the correct answer on the other question.
    a. What is the probability that the student will answer both questions correctly?
    b. What is the probability that the student will answer exactly one of the questions correctly?
    c. What is the probability that the student will answer neither question correctly?
24. A company uses two proofreaders X and Y to check a certain manuscript. X misses 12% of typographical errors and Y misses 15%. Assume that the proofreaders work independently.
    a. What is the probability that a randomly chosen typographical error will be missed by both proofreaders?
    b. If the manuscript contains 1,000 typographical errors, what number can be expected to be missed?
25. A coin is loaded so that the probability of heads is 0.7 and the probability of tails is 0.3. Suppose that the coin is tossed twice and that the results of the tosses are independent.
    a. What is the probability of obtaining exactly two heads?
    b. What is the probability of obtaining exactly one head?
    c. What is the probability of obtaining no heads?
    d. What is the probability of obtaining at least one head?
26. Describe a sample space and events A, B, and C, where P(A ∩ B ∩ C) = P(A) · P(B) · P(C) but A, B, and C are not pairwise independent.
27. The example used to introduce conditional probability described a family with two children each of whom was equally likely to be a boy or a girl. The example showed that if it is known that one child is a boy, the probability that the other child is a boy is 1/3. Now imagine the same kind of family—two children each of whom is equally likely to be a boy or a girl. Suppose you meet one of the children and see that it is a boy. What is the probability that the other child is a boy? Explain. (Be careful. The answer may surprise you.)
28. A coin is loaded so that the probability of heads is 0.7 and the probability of tails is 0.3. Suppose that the coin is tossed ten times and that the results of the tosses are mutually independent.
    a. What is the probability of obtaining exactly seven heads?
    b. What is the probability of obtaining exactly ten heads?
    c. What is the probability of obtaining no heads?
    d. What is the probability of obtaining at least one head?
29. Suppose that ten items are chosen at random from a large batch delivered to a company. The manufacturer claims that just 3% of the items in the batch are defective. Assume that the batch is large enough so that even though the selection is made without replacement, the number 0.03 can be used to approximate the probability that any one of the ten items is defective. In addition, assume that because the items are chosen at random, the outcomes of the choices are mutually independent. Finally, assume that the manufacturer's claim is correct.
    a. What is the probability that none of the ten is defective?
    b. What is the probability that at least one of the ten is defective?
    c. What is the probability that exactly four of the ten are defective?
    d. What is the probability that at most two of the ten are defective?
30. Suppose the probability of a false positive result on a mammogram is 4% and that radiologists' interpretations of mammograms are mutually independent in the sense that whether or not a radiologist finds a positive result on one mammogram does not influence whether or not the radiologist finds a positive result on another mammogram. Assume that a woman has a mammogram every year for ten years.
    a. What is the probability that she will have no false positive results during that time?
    b. What is the probability that she will have at least one false positive result during that time?
    c. What is the probability that she will have exactly two false positive results during that time?
    d. Suppose that the probability of a false negative result on a mammogram is 2%, and assume that the probability that a randomly chosen woman has breast cancer is 0.0002.
       (i) If a woman has a positive test result one year, what is the probability that she actually has breast cancer?
       (ii) If a woman has a negative test result one year, what is the probability that she actually has breast cancer?
31. Empirical data indicate that approximately 103 out of every 200 children born are male. Hence the probability of a newborn being male is about 51.5%. Suppose that a family has six children, and suppose that the genders of all the children are mutually independent.
    a. What is the probability that none of the children is male?
    b. What is the probability that at least one of the children is male?
    c. What is the probability that exactly five of the children are male?
32. A person takes a multiple-choice exam in which each question has four possible answers. Suppose that the person has no idea about the answers to three of the questions and simply chooses randomly for each one.
    a. What is the probability that the person will answer all three questions correctly?
    b. What is the probability that the person will answer exactly two questions correctly?
    c. What is the probability that the person will answer exactly one question correctly?
    d. What is the probability that the person will answer no questions correctly?
    e. Suppose that the person gets one point of credit for each correct answer and that 1/3 point is deducted for each incorrect answer. What is the expected value of the person's score for the three questions?
33. In exercise 23 of Section 9.8, let Cₖ be the event that the gambler has k dollars, wins the next roll of the die, and is eventually ruined, let Dₖ be the event that the gambler has k dollars, loses the next roll of the die, and is eventually ruined, and let Pₙ be the probability that the gambler is eventually ruined. Use the probability axioms and the definition of conditional probability to derive the equation Pₖ₋₁ = (1/6)Pₖ + (5/6)Pₖ₋₂.

## Test Yourself

1. If A and B are any events in a sample space S and P(A) ≠ 0, then the conditional probability of B given A is P(B | A) = _____.

2. Bayes' theorem says that if a sample space S is a union of mutually disjoint events B₁, B₂, ..., Bₙ with nonzero probabilities, if A is an event in S with P(A) ≠ 0, and if k is an integer with 1 ≤ k ≤ n, then _____.

3. Events A and B in a sample space S are independent if, and only if, _____.

4. Events A, B, and C in a sample space S are mutually independent if, and only if, _____, _____, _____, and _____.

**Answers:**
1. P(A ∩ B) / P(A)
2. P(Bₖ | A) = P(A | Bₖ)P(Bₖ) / [P(A | B₁)P(B₁) + P(A | B₂)P(B₂) + · · · + P(A | Bₙ)P(Bₙ)]
3. P(A ∩ B) = P(A) · P(B)
4. P(A ∩ B) = P(A) · P(B); P(A ∩ C) = P(A) · P(C); P(B ∩ C) = P(B) · P(C); P(A ∩ B ∩ C) = P(A) · P(B) · P(C)