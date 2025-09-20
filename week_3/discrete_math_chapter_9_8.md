# Chapter 9.8: Probability Axioms and Expected Value

## Introduction

*The theory of probability is at bottom nothing but common sense reduced to a calculus.*
— Pierre-Simon Laplace (1749–1827)

Up to this point, you have calculated probabilities only for situations, such as tossing a fair coin or rolling a pair of balanced dice, where the outcomes in the sample space are all equally likely. But coins are not always fair and dice are not always balanced. How is it possible to calculate probabilities for these more general situations?

The following axioms were formulated by A. N. Kolmogorov in 1933 to provide a theoretical foundation for a far-ranging theory of probability. In this section we state the axioms, derive a few consequences, and introduce the notion of expected value.

Recall that a sample space is a set of all outcomes of a random process or experiment and that an event is a subset of a sample space.

## Probability Axioms

**Definition: Probability Axioms**
Let S be a sample space. A probability function P from the set of all events in S to the set of real numbers satisfies the following three axioms: For all events A and B in S:

1. **Axiom 1**: 0 ≤ P(A) ≤ 1
2. **Axiom 2**: P(∅) = 0 and P(S) = 1
3. **Axiom 3**: If A and B are disjoint (that is, if A ∩ B = ∅), then the probability of the union of A and B is P(A ∪ B) = P(A) + P(B)

## Examples and Applications

### Example 9.8.1: Applying the Probability Axioms
Suppose that A and B are events in a sample space S. If A and B are disjoint, could P(A) = 0.6 and P(B) = 0.8?

**Solution:** No. Probability axiom 3 would imply that P(A ∪ B) = P(A) + P(B) = 0.6 + 0.8 = 1.4, and since 1.4 > 1, this result would violate probability axiom 1.

### Example 9.8.2: The Probability of the Complement of an Event
Suppose that A is an event in a sample space S. Deduce that P(Aᶜ) = 1 - P(A).

**Solution:** By Theorem 6.2.2(5), with S playing the role of the universal set U:
- A ∩ Aᶜ = ∅
- A ∪ Aᶜ = S

Thus S is the disjoint union of A and Aᶜ, and so:
P(A ∪ Aᶜ) = P(A) + P(Aᶜ) = P(S) = 1

Subtracting P(A) from both sides gives the result that P(Aᶜ) = 1 - P(A)

**Theorem 9.8.1: Probability of the Complement of an Event**
If A is any event in a sample space S, then:
**P(Aᶜ) = 1 - P(A)**

## Consistency with Equally Likely Probability Formula

It is important to check that Kolmogorov's probability axioms are consistent with the results obtained using the equally likely probability formula. To see that this is the case, let S be a finite sample space with outcomes a₁, a₂, a₃, ..., aₙ. It is clear that all the singleton sets {a₁}, {a₂}, {a₃}, ..., {aₙ} are mutually disjoint and that their union is S. Since P(S) = 1, probability axiom 3 can be applied multiple times to obtain:

P({a₁} ∪ {a₂} ∪ {a₃} ∪ · · · ∪ {aₙ}) = Σ (from k=1 to n) P({aₖ}) = 1

If, in addition, all the outcomes are equally likely, there is a positive real number c so that:
P({a₁}) = P({a₂}) = P({a₃}) = · · · = P({aₙ}) = c

Hence:
1 = Σ (from k=1 to n) c = c + c + · · · + c = nc (n terms)

And thus c = 1/n

It follows that if A is any event with outcomes aᵢ₁, aᵢ₂, aᵢ₃, ..., aᵢₘ, then:
P(A) = Σ (from k=1 to m) P({aᵢₖ}) = Σ (from k=1 to m) (1/n) = m/n = N(A)/N(S)

Which is the result given by the equally likely probability formula.

## Probability of a General Union of Two Events

### Example 9.8.3: The Probability of a General Union of Two Events
Follow the steps outlined in parts (a) and (b) below to prove the following formula:

**Theorem 9.8.2: Probability of a General Union of Two Events**
If S is any sample space and A and B are any events in S, then:
**P(A ∪ B) = P(A) + P(B) - P(A ∩ B)**

**Solution:**
a. Show that A ∪ B is a disjoint union of the following sets: A - (A ∩ B), B - (A ∩ B), and A ∩ B.

Refer to Figure 9.8.1 as you read the following explanation. Elements in the set A - (A ∩ B) are in the region shaded blue, elements in B - (A ∩ B) are in the region shaded gray, and elements in A ∩ B are in the white region.

**Part 1**: Show that A ∪ B ⊆ (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B):
Given any element x in A ∪ B, x satisfies exactly one of the following three conditions:
(1) x ∈ A and x ∈ B
(2) x ∈ A and x ∉ B
(3) x ∈ B and x ∉ A

1. In the first case, x ∈ A ∩ B, and so x ∈ (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B) by definition of union.
2. In the second case, x ∉ A ∩ B (because x ∉ B), and so x ∈ A - (A ∩ B). Therefore x ∈ (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B) by definition of union.
3. In the third case, x ∉ A ∩ B (because x ∉ A), and hence x ∈ B - (A ∩ B). So, again, x ∈ (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B) by definition of union.

Hence, in all three cases, x ∈ (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B), which completes the proof of part 1.

Moreover, since the three conditions are mutually exclusive, the three sets A - (A ∩ B), B - (A ∩ B), and A ∩ B are mutually disjoint.

**Part 2**: Show that (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B) ⊆ A ∪ B:
Suppose x is any element in (A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B). By definition of union, x ∈ A - (A ∩ B) or x ∈ B - (A ∩ B) or x ∈ A ∩ B.

1. In case x ∈ A - (A ∩ B), then x ∈ A and x ∉ A ∩ B by definition of set difference. In particular, x ∈ A and so x ∈ A ∪ B.
2. In case x ∈ B - (A ∩ B), then x ∈ B and x ∉ A ∩ B by definition of set difference. In particular, x ∈ B and so x ∈ A ∪ B.
3. In case x ∈ A ∩ B, then in particular, x ∈ A and so x ∈ A ∪ B.

Hence, in all three cases, x ∈ A ∪ B, which completes the proof of part 2.

b. P(A ∪ B) = P((A - (A ∩ B)) ∪ (B - (A ∩ B)) ∪ (A ∩ B))  [by part (a)]
           = P(A - (A ∩ B)) + P(B - (A ∩ B)) + P(A ∩ B)  [by exercise 13 at the end of the section and the fact that A - (A ∩ B), B - (A ∩ B), and A ∩ B are mutually disjoint]
           = P(A) - P(A ∩ B) + P(B) - P(A ∩ B) + P(A ∩ B)  [by exercise 12 at the end of the section because A ∩ B ⊆ A and A ∩ B ⊆ B]
           = P(A) + P(B) - P(A ∩ B)  [by algebra]

### Example 9.8.4: Computing the Probability of a General Union of Two Events
Suppose a card is chosen at random from an ordinary 52-card deck. What is the probability that the card is a face card (jack, queen, or king) or is from one of the red suits (hearts or diamonds)?

**Solution:**
Let A be the event that the chosen card is a face card, and let B be the event that the chosen card is from one of the red suits. The event that the card is a face card or is from one of the red suits is A ∪ B.

Now N(A) = 4·3 = 12 (because each of the four suits has three face cards), and so P(A) = 12/52. Also N(B) = 26 (because half the cards are red), and so P(B) = 26/52. Finally, N(A ∩ B) = 6 (because there are three face cards in hearts and another three in diamonds), and so P(A ∩ B) = 6/52.

It follows from the formula for the probability of a union of any two events that:
P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 12/52 + 26/52 - 6/52 = 32/52 ≈ 61.5%

Thus the probability that the chosen card is a face card or is from one of the red suits is approximately 61.5%.

## Expected Value

People who buy lottery tickets regularly often justify the practice by saying that, even though they know that on average they will lose money, they are hoping for one significant gain, after which they believe they will quit playing. Unfortunately, when people who have lost money on a string of losing lottery tickets win some or all of it back, they generally decide to keep trying their luck instead of quitting.

The technical way to say that on average a person will lose money on the lottery is to say that the expected value of playing the lottery is negative.

**Definition: Expected Value**
Suppose the possible outcomes of an experiment, or random process, are real numbers a₁, a₂, a₃, ..., aₙ, which occur with probabilities p₁, p₂, p₃, ..., pₙ. The expected value of the process is:
E = Σ (from k=1 to n) aₖpₖ = a₁p₁ + a₂p₂ + a₃p₃ + · · · + aₙpₙ

### Example 9.8.5: Expected Value of a Lottery
Suppose that 500,000 people pay $5 each to play a lottery game with the following prizes: a grand prize of $1,000,000, 10 second prizes of $1,000 each, 1,000 third prizes of $500 each, and 10,000 fourth prizes of $10 each. What is the expected value of a ticket?

**Solution:**
Each of the 500,000 lottery tickets has the same chance as any other of containing a winning lottery number, and so pₖ = 1/500000 for all k = 1, 2, 3, ..., 500000.

Let a₁, a₂, a₃, ..., a₅₀₀₀₀₀ be the net gain for an individual ticket, where:
- a₁ = 999995 (the net gain for the grand prize ticket, which is one million dollars minus the $5 cost of the winning ticket)
- a₂ = a₃ = · · · = a₁₁ = 995 (the net gain for each of the 10 second prize tickets)
- a₁₂ = a₁₃ = · · · = a₁₀₁₁ = 495 (the net gain for each of the 1,000 third prize tickets)
- a₁₀₁₂ = a₁₀₁₃ = · · · = a₁₁₀₁₁ = 5 (the net gain for each of the 10,000 fourth prize tickets)
- a₁₁₀₁₂ = a₁₁₀₁₃ = · · · = a₅₀₀₀₀₀ = -5 (the remaining 488,989 tickets just lose $5)

The expected value of a ticket is therefore:
E = Σ (from k=1 to 500000) aₖpₖ = Σ (from k=1 to 500000) aₖ · (1/500000)  [because each pₖ = 1/500000]
  = (1/500000) Σ (from k=1 to 500000) aₖ  [by Theorem 5.1.1(2)]
  = (1/500000) [999995 + 10·995 + 1000·495 + 10000·5 + (-5)·488989]
  = (1/500000) [999995 + 9950 + 495000 + 50000 - 2444945]
  = -1.78

In other words, a person who continues to play this lottery for a very long time will probably win some money occasionally but on average will lose $1.78 per ticket.

### Example 9.8.6: Gambler's Ruin
A gambler repeatedly bets $1 that a coin will come up heads when tossed. Each time the coin comes up heads, the gambler wins $1; each time it comes up tails, he loses $1. The gambler will quit playing either when he is ruined (loses all his money) or when he has $M (where M is a positive number he has decided in advance). Let Pₙ be the probability that the gambler is ruined if he begins playing with $n. Then if the coin is fair (has an equal chance of coming up heads or tails),
Pₖ₋₁ = (1/2)Pₖ + (1/2)Pₖ₋₂ for each integer k with 2 ≤ k ≤ M.

(This follows from the fact that if the gambler has $(k - 1), then he has an equal chance of winning $1 or losing $1, and if he wins $1, then his chance of being ruined is Pₖ, whereas if he loses $1, then his chance of being ruined is Pₖ₋₂.) Also P₀ = 1 (because if he has $0, he is certain of being ruined) and Pₘ = 0 (because once he has $M, he quits and so stands no chance of being ruined). Find an explicit formula for Pₙ. How should the gambler choose M to minimize his chance of being ruined?

**Solution:**
Multiplying both sides of Pₖ₋₁ = (1/2)Pₖ + (1/2)Pₖ₋₂ by 2 and subtracting Pₖ₋₂ from both sides gives:
Pₖ = 2Pₖ₋₁ - Pₖ₋₂

This is a second-order homogeneous recurrence relation with constant coefficients. Because Pₖ - 2Pₖ₋₁ + Pₖ₋₂ = 0, its characteristic equation is:
t² - 2t + 1 = 0

Which has the single root r = 1. Thus, by the single-root theorem from Section 5.8,
Pₙ = Crⁿ + Dnrⁿ = C + Dn (since r = 1)

Where C and D are determined by two values of the sequence. But P₀ = 1 and Pₘ = 0. Hence:
1 = P₀ = C + D·0 = C
0 = Pₘ = C + D·M = 1 + D·M

It follows that C = 1 and D = -1/M, and so:
Pₙ = 1 - (1/M)n = (M - n)/M for each integer n with 0 ≤ n ≤ M.

For instance, a gambler who starts with $20 and decides to quit either if his total grows to $100 or if he goes broke has the following chance of going broke:
P₂₀ = (100 - 20)/100 = 80/100 = 80%

Observe that the larger M is relative to n, the closer Pₙ is to 1. In other words, the larger the amount of money the gambler sets himself as a target, the more likely he is to go broke. Conversely, the more modest he is in his goal, the more likely he is to reach it.

## Test Yourself

1. If A is an event in a sample space S, P(A) can take values between _____ and _____. Moreover, P(S) = _____, and P(∅) = _____.
2. If A and B are disjoint events in a sample space S, P(A ∪ B) = _____.
3. If A is an event in a sample space S, P(Aᶜ) = _____.
4. If A and B are any events in a sample space S, P(A ∪ B) = _____.
5. If the possible outcomes of a random process or experiment are real numbers a₁, a₂, ..., aₙ, which occur with probabilities p₁, p₂, ..., pₙ, then the expected value of the process is _____.

**Answers:**
1. 0; 1; 1; 0
2. P(A) + P(B)
3. 1 - P(A)
4. P(A) + P(B) - P(A ∩ B)
5. a₁p₁ + a₂p₂ + · · · + aₙpₙ