# Chapter 9: Counting and Probability (Complete)

**Pages 516-590**

## End of Chapter 8: RSA Cryptography

**Page 516**

## 8.10 Application: The RSA Public-Key Cryptography System

It was observed that using cryptography on the Internet requires a different paradigm than traditional cryptography. In e-commerce, two parties who have no knowledge of each other need to transmit messages securely: you give a credit card number over the Internet and expect that only the seller will receive it.

The RSA public-key cryptography system is the most widely used public-key system today. It was invented by three MIT scientists, Ronald Rivest, Adi Shamir, and Leonard Adleman in 1977.

### Definition

A public-key cryptography system consists of three parts:

1. A method for encrypting messages being sent
2. A method for decrypting messages being received
3. A method for generating matching pairs of encryption and decryption keys, with the encryption key being public and the decryption key being private

The RSA system uses properties of modular arithmetic, the Euclidean algorithm, Fermat's little theorem, and the Chinese remainder theorem.

**Page 517**

### How RSA Works

In RSA, messages are encrypted and decrypted using modular exponentiation:

- **Key Generation:**
  1. Choose two large prime numbers p and q
  2. Compute n = pq (the modulus)
  3. Compute φ(n) = (p-1)(q-1) (Euler's totient function)
  4. Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1 (public exponent)
  5. Compute d such that de ≡ 1 (mod φ(n)) (private exponent)

- **Public Key:** (n, e)
- **Private Key:** (n, d)

- **Encryption:** C ≡ M^e (mod n)
- **Decryption:** M ≡ C^d (mod n)

### Example 8.10.1 Small RSA Example

Let p = 3, q = 11. Then:
- n = 33
- φ(n) = 2 × 10 = 20
- Choose e = 3 (since gcd(3, 20) = 1)
- Find d: 3d ≡ 1 (mod 20), so d = 7

Public key: (33, 3)
Private key: (33, 7)

To encrypt message M = 5:
C ≡ 5³ ≡ 125 ≡ 26 (mod 33)

To decrypt ciphertext C = 26:
M ≡ 26⁷ (mod 33)

**Page 518-519**

### Security of RSA

The security of RSA relies on:
1. The difficulty of factoring large numbers
2. The difficulty of computing φ(n) without knowing p and q
3. The difficulty of finding d without knowing φ(n)

### Fermat's Little Theorem (Key to RSA)

**Theorem 8.10.1 Fermat's Little Theorem**
If p is a prime number and a is any integer not divisible by p, then:
```
a^(p-1) ≡ 1 (mod p)
```

**Corollary:** For any integer a:
```
a^p ≡ a (mod p)
```

**Page 520**

### Why RSA Works

The correctness of RSA decryption follows from:

**Theorem 8.10.2**
For the RSA system with parameters n = pq, e, and d where ed ≡ 1 (mod φ(n)):
```
(M^e)^d ≡ M (mod n)
```

**Proof:** Since ed ≡ 1 (mod φ(n)), we have ed = 1 + kφ(n) for some integer k.

Thus:
```
(M^e)^d = M^(ed) = M^(1+kφ(n)) = M · (M^φ(n))^k
```

By Euler's theorem (generalization of Fermat's Little Theorem):
- If gcd(M, n) = 1, then M^φ(n) ≡ 1 (mod n)
- Therefore (M^e)^d ≡ M · 1^k ≡ M (mod n) ■

---

# Chapter 9: Counting and Probability

**Page 521**

## Introduction

> The theory of probability was originated by mathematicians of the seventeenth century in an attempt to answer certain questions arising in games of chance, such as how to divide the pot in a dice game that has to stop before either player has definitely won.
> — Morris Kline, 1985

The subject of probability arose principally in the seventeenth century in an exchange of letters between Blaise Pascal and Pierre de Fermat about "the problem of points." The essence of the problem is to determine how to divide the pot when a game of chance must be abandoned before either player has enough points to win.

### Historical Note

In 1654, a French nobleman, the Chevalier de Méré, asked Pascal why he lost money on a certain dice bet. This led Pascal to correspond with Fermat, and together they developed the mathematical theory of probability.

The basic framework: In a situation with a finite number of equally likely outcomes, the probability of an event is the ratio of the number of outcomes that are favorable to the event to the total number of outcomes.

### Chapter Overview

This chapter covers:
- **Section 9.1:** Introduction to Probability
- **Section 9.2:** Possibility Trees and the Multiplication Rule
- **Section 9.3:** Counting Elements of Disjoint Sets: The Addition Rule
- **Section 9.4:** The Pigeonhole Principle
- **Section 9.5:** Counting Subsets of a Set: Combinations
- **Section 9.6:** r-Combinations with Repetition Allowed
- **Section 9.7:** Pascal's Formula and the Binomial Theorem
- **Section 9.8:** Probability Axioms and Expected Value
- **Section 9.9:** Conditional Probability, Bayes' Formula, and Independent Events

**Page 522**

## 9.1 Introduction to Probability

> I claim to be a simple individual liable to err like any other fellow mortal. I own, however, that I have humility enough to confess my errors and to retrace my steps.
> — Mahatma Gandhi, 1869–1948

When you roll a pair of dice, what are the chances of rolling a sum of 7? When you flip a coin ten times, what is the likelihood of getting exactly four heads? If you pick a number at random between 1 and 100, what is the probability that it is divisible by 3?

To answer these questions requires knowledge of probability, the subject to which much of the rest of this chapter is devoted.

### Sample Spaces and Probability Functions

The set of all possible outcomes of an experiment or an observation is called a **sample space**. If you roll a single six-sided die and observe the number showing face up, the sample space is the set {1, 2, 3, 4, 5, 6}. If you pick a ball from a bag containing four blue and three gray balls and observe its color, the sample space is {blue, gray}. If you roll a pair of dice—say, one black and one gray—you can think of the sample space either as the set of all possible sums (which range from 2 through 12) or as the set of all 36 different outcomes for the pair of dice:

```
(1,1) (1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (2,2) (2,3) (2,4) (2,5) (2,6)
(3,1) (3,2) (3,3) (3,4) (3,5) (3,6)
(4,1) (4,2) (4,3) (4,4) (4,5) (4,6)
(5,1) (5,2) (5,3) (5,4) (5,5) (5,6)
(6,1) (6,2) (6,3) (6,4) (6,5) (6,6)
```

where (a,b) indicates that a is the number face up on the black die and b is the number face up on the gray die.

**Page 523**

### Definition

An **event** is a subset of a sample space. If you roll a pair of dice and denote the event "the sum is at least 3" by A, then

```
A = {(1,2), (1,3), (1,4), (1,5), (1,6),
     (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
     (3,1), (3,2), (3,3), (3,4), (3,5), (3,6),
     (4,1), (4,2), (4,3), (4,4), (4,5), (4,6),
     (5,1), (5,2), (5,3), (5,4), (5,5), (5,6),
     (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)}.
```

The event "the sum is 7" is
```
{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}.
```

### Probability in the Equally Likely Case

Given a finite sample space S in which all outcomes are equally likely and an event E in S,

**the probability of E**, denoted **P(E)**, is

```
P(E) = the number of outcomes in E / the number of outcomes in S = N(E)/N(S)
```

Note that because E ⊆ S, 0 ≤ N(E) ≤ N(S), and so
```
0 ≤ P(E) ≤ 1.
```

**Page 524**

### Example 9.1.1 Probabilities for a Pair of Dice

A pair of dice, one black and one gray, are rolled, and the numbers showing face up are observed.

a. What is the probability that the sum is 7?
b. What is the probability that the sum is 10 or 11?
c. What is the probability that the black die shows 3?

**Solution:**

Consider the sample space to be the set of all 36 outcomes for a pair of dice.

a. The event E that the sum is 7:
   E = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}
   N(E) = 6, so P(E) = 6/36 = 1/6

b. The event F that sum is 10:
   {(4,6), (5,5), (6,4)} has 3 outcomes
   The event that sum is 11:
   {(5,6), (6,5)} has 2 outcomes
   Combined: 3 + 2 = 5 outcomes
   P(sum is 10 or 11) = 5/36

c. Event that black die shows 3:
   {(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)}
   P(black die shows 3) = 6/36 = 1/6 ■

**Page 525**

### Example 9.1.2 Probability of Having Two Boys and Two Girls

If a couple has four children, what is the probability that they have two boys and two girls?

**Solution:**

The sample space S is the set of all possible sequences of four births. We can represent each outcome as a sequence of B's (boys) and G's (girls).

The total number of outcomes = 2^4 = 16

The favorable outcomes (2 boys, 2 girls) are:
BBGG, BGBG, BGGB, GBGB, GBBG, GGBB

Number of ways to choose positions for the 2 B's = C(4,2) = 6

P(2 boys and 2 girls) = 6/16 = 3/8 ■

**Page 526**

### Counting the Elements of a List

**Theorem 9.1.1**
1. If m is a positive integer and if objects are placed into m different boxes, then at least one box must contain two or more objects if there are at least m + 1 objects.
2. A list of n distinct elements has n! permutations.
3. The number of subsets of a set with n elements is 2^n.

### Example 9.1.3 The Probability of a Full House

Five cards are dealt from a standard 52-card deck. What is the probability of being dealt a full house (three cards of one denomination and two cards of another)?

**Solution:**

Total number of 5-card hands = C(52,5) = 2,598,960

For a full house:
- Choose denomination for triple: 13 ways
- Choose 3 cards from that denomination: C(4,3) = 4 ways
- Choose denomination for pair: 12 ways
- Choose 2 cards from that denomination: C(4,2) = 6 ways

Total full houses = 13 × 4 × 12 × 6 = 3,744

P(full house) = 3,744/2,598,960 ≈ 0.00144 ■

**Page 527**

### Example 9.1.4 Probability and Divisibility by 3

An integer is chosen at random from the first 100 positive integers. What is the probability that it is divisible by 3?

**Solution:**

The sample space S = {1, 2, 3, ..., 100}, so N(S) = 100.

The event E consists of integers divisible by 3:
E = {3, 6, 9, 12, ..., 99}

To count these: 99 = 3 × 33, so there are 33 multiples of 3.

P(divisible by 3) = 33/100 ■

**Page 528**

### Example 9.1.5 Probability of Winning a Lottery

In many state lottery games, six numbers are randomly chosen from the first 40 positive integers. A player wins the big prize by selecting the same six numbers (in any order). What is the probability of winning the big prize?

**Solution:**

Total ways to choose 6 numbers from 40:
```
C(40, 6) = 40!/(6!(40-6)!) = 40!/(6!34!) = 3,838,380
```

Only 1 way wins the big prize.

P(winning big prize) = 1/3,838,380 ≈ 0.00000026 ■

This is about 1 chance in 4 million!

**Page 541**

## 9.1 Introduction to Probability

### Computing Probabilities Using Counting Techniques

The definitions and formulas from this and the previous two chapters can be used to calculate probabilities. To find the probability that an event occurs, you compute the number of outcomes in the event and divide by the total number of outcomes in the sample space.

### Example 9.1.6 Five-Card Poker Hands

In five-card draw poker, each player is dealt five cards from an ordinary deck of 52 playing cards.

a. How many five-card draw poker hands are there?
b. How many hands contain four aces?
c. What is the probability that a hand contains four aces?
d. What is the probability that a hand is a full house?
e. What is the probability that a hand is a three-of-a-kind?

**Solution:**

a. Each hand is an unordered selection of five cards from 52.
   Number of hands = C(52, 5) = 52!/(5!·47!) = 2,598,960

b. A hand with four aces must contain all four aces plus one other card.
   Choose the aces: C(4, 4) = 1 way
   Choose one other card from the remaining 48: C(48, 1) = 48 ways
   Total hands with four aces = 1 × 48 = 48

c. P(four aces) = 48/2,598,960 = 1/54,145 ≈ 0.0000185

d. A full house consists of three cards of one denomination and two cards of another.
   Choose the denomination for the triple: 13 ways
   Choose 3 cards from that denomination: C(4, 3) = 4 ways
   Choose the denomination for the pair: 12 ways
   Choose 2 cards from that denomination: C(4, 2) = 6 ways
   Total full houses = 13 × 4 × 12 × 6 = 3,744
   P(full house) = 3,744/2,598,960 ≈ 0.00144

e. Three-of-a-kind means exactly three cards of one denomination, and the other two cards have different denominations.
   Choose the denomination for the triple: 13 ways
   Choose 3 cards from that denomination: C(4, 3) = 4 ways
   Choose 2 different denominations for the other cards: C(12, 2) = 66 ways
   Choose 1 card from each of these denominations: 4 × 4 = 16 ways
   Total three-of-a-kinds = 13 × 4 × 66 × 16 = 54,912
   P(three-of-a-kind) = 54,912/2,598,960 ≈ 0.0211 ■

**Page 542**

### The Complement of an Event

The **complement** of an event A in a sample space S, denoted A^c, is the set of all outcomes in S that are not in A. In symbols:

```
A^c = S - A
```

Since A and A^c are disjoint and A ∪ A^c = S:
```
N(A) + N(A^c) = N(S)
```

Therefore:
```
P(A) + P(A^c) = 1
```

Or equivalently:
```
P(A^c) = 1 - P(A)
```

### Example 9.1.7 The Probability of Having at Least One Girl

If a family has four children, what is the probability that at least one child is a girl, assuming that it is equally likely for a child to be a boy or a girl?

**Solution:**

Let E be the event "at least one girl."
E^c is the event "no girls" = "all boys."

The only outcome in E^c is BBBB.
P(E^c) = 1/16

Therefore:
P(E) = 1 - P(E^c) = 1 - 1/16 = 15/16 ■

**Page 543**

### Odds

In addition to probability, another way to measure the likelihood of an event is to compute its **odds**.

**Definition:** If E is an event in a sample space S with P(E) ≠ 0 and P(E) ≠ 1, then:
- The **odds in favor of E** are P(E)/P(E^c)
- The **odds against E** are P(E^c)/P(E)

### Example 9.1.8 Odds in Favor of an Event

Suppose E is the event that a five-card poker hand contains exactly one pair (two cards of one denomination and the other three cards of different denominations).

**Solution:**

To compute the odds in favor of E:
1. Find P(E)
2. Find P(E^c) = 1 - P(E)
3. Calculate P(E)/P(E^c)

Number of hands with exactly one pair:
- Choose the denomination for the pair: 13 ways
- Choose 2 cards from that denomination: C(4, 2) = 6 ways
- Choose 3 different denominations: C(12, 3) = 220 ways
- Choose 1 card from each: 4 × 4 × 4 = 64 ways
- Total = 13 × 6 × 220 × 64 = 1,098,240

P(E) = 1,098,240/2,598,960 ≈ 0.423

Odds in favor = 0.423/0.577 ≈ 0.73 to 1

This is often expressed as 73 to 100, or about 3 to 4. ■

**Page 544**

### Exercise Set 9.1

1. A person selects a card at random from a standard 52-card deck.
   a. What is the probability that it is a king?
   b. What is the probability that it is a face card (jack, queen, or king)?

2. A lottery ticket contains six different numbers from 1 to 40. Six winning numbers are chosen randomly.
   a. What is the probability of matching all six numbers?
   b. What is the probability of matching exactly five numbers?

3. Two dice are rolled. Find the probability that:
   a. The sum is 8
   b. The sum is less than 5
   c. At least one die shows 6

[Additional exercises continue...]

**Page 545**

### Test Yourself

1. A sample space is _____.
2. An event is _____.
3. If all outcomes in a finite sample space S are equally likely and E is an event in S, then P(E) = _____.
4. If A is an event in a sample space S, then the complement of A is _____.
5. If A is an event in a sample space S, then P(A^c) = _____.

Answers:
1. the set of all possible outcomes of an experiment
2. a subset of a sample space
3. N(E)/N(S)
4. the set of all outcomes in S that are not in A
5. 1 - P(A)

---

## 9.2 Possibility Trees and the Multiplication Rule

**Page 546**

> If one can't be happy, one must be amused.
> — Nancy Mitford, 1904–1973

### Teams A and B

Teams A and B are to play each other repeatedly until one wins two games in a row or a total of three games. One way in which this tournament can be played is shown on the next page.

```
A wins → A wins [A wins the tournament]
      → B wins → A wins [A wins the tournament]
                → B wins [B wins the tournament]

B wins → B wins [B wins the tournament]
      → A wins → B wins [B wins the tournament]
                → A wins [A wins the tournament]
```

**Page 547**

### Possibility Trees

A **possibility tree** is a visual tool that:
- Represents all possible outcomes of a sequence of events
- Each branch represents one possible outcome at each stage
- Complete paths from root to leaf represent complete sequences

### The Multiplication Rule

**Theorem 9.2.1 The Multiplication Rule**

If an operation consists of k steps and:
- The first step can be performed in n₁ ways
- The second step can be performed in n₂ ways (regardless of how the first step was performed)
- ...
- The kth step can be performed in nₖ ways (regardless of how the preceding steps were performed)

Then the entire operation can be performed in n₁ · n₂ · ... · nₖ ways.

**Page 548**

### Example 9.2.1 Using the Multiplication Rule

**Number of Two-Letter Words**

How many two-letter "words" (sequences) can be formed from the English alphabet if:
a. Letters can be repeated?
b. Letters cannot be repeated?

**Solution:**

a. With repetition allowed:
   - First position: 26 choices
   - Second position: 26 choices
   - Total: 26 × 26 = 676

b. Without repetition:
   - First position: 26 choices
   - Second position: 25 choices (can't reuse first letter)
   - Total: 26 × 25 = 650 ■

**Page 549**

### Example 9.2.2 Number of PINs

A personal identification number (PIN) is a sequence of any four symbols chosen from the 26 letters in the alphabet and the ten digits, with repetition allowed. How many different PINs are possible?

**Solution:**

- Total symbols available: 26 + 10 = 36
- Each position can use any of 36 symbols
- Number of PINs = 36 × 36 × 36 × 36 = 36⁴ = 1,679,616 ■

**Page 550**

### Example 9.2.3 License Plates

How many different license plates can be made if:
- Each plate contains a sequence of three letters followed by three digits?
- Letters and digits can be repeated?

**Solution:**

- Letters: 26 choices for each of 3 positions = 26³
- Digits: 10 choices for each of 3 positions = 10³
- Total = 26³ × 10³ = 17,576 × 1,000 = 17,576,000 ■

**Page 551**

### Example 9.2.4 Computer Passwords

A computer password must be between 6 and 8 characters long, where each character is an uppercase letter (26 choices) or a digit (10 choices). How many different passwords are possible?

**Solution:**

- Characters per position: 26 + 10 = 36
- 6-character passwords: 36⁶
- 7-character passwords: 36⁷
- 8-character passwords: 36⁸

Total = 36⁶ + 36⁷ + 36⁸
     = 36⁶(1 + 36 + 36²)
     = 36⁶(1 + 36 + 1,296)
     = 36⁶(1,333)
     = 2,176,782,336 × 1,333
     = 2,901,650,853,888 ■

**Page 552**

### Example 9.2.5 Counting Bit Strings

a. How many bit strings of length 8 are there?
b. How many bit strings of length 8 begin with 1?
c. How many bit strings of length 8 begin with 11?
d. How many bit strings of length 8 begin with 11 or end with 00?

**Solution:**

a. Each position: 2 choices (0 or 1)
   Total = 2⁸ = 256

b. First position fixed as 1, remaining 7 positions free
   Total = 1 × 2⁷ = 128

c. First two positions fixed as 11, remaining 6 positions free
   Total = 1 × 1 × 2⁶ = 64

d. Begin with 11: 2⁶ = 64
   End with 00: 2⁶ = 64
   Begin with 11 AND end with 00: 2⁴ = 16
   By inclusion-exclusion: 64 + 64 - 16 = 112 ■

**Page 553**

### Counting with Possibility Trees

When the multiplication rule is difficult to apply directly, possibility trees can help visualize and count outcomes.

### Example 9.2.6 Best Two Out of Three

Teams A and B play until one team wins two games. How many different ways can the tournament be played?

**Solution:**

Using a possibility tree:

```
Start → A wins → A wins [A wins 2-0]
              → B wins → A wins [A wins 2-1]
                      → B wins [B wins 2-1]
     → B wins → B wins [B wins 2-0]
              → A wins → B wins [B wins 2-1]
                      → A wins [A wins 2-1]
```

Total: 6 different ways ■

**Page 554**

### When Multiplication Rule Doesn't Apply Directly

Sometimes the number of ways to perform each step depends on previous steps. In such cases:
1. Draw a possibility tree, or
2. Reorder the steps cleverly

### Example 9.2.7 Officers with Restrictions

Three officers—president, treasurer, secretary—are to be chosen from Ann, Bob, Cyd, Dan, with restrictions:
- Ann cannot be president
- Either Cyd or Dan must be secretary

How many ways can the officers be chosen?

**Solution:**

Reorder the steps:
1. Choose secretary first: 2 ways (Cyd or Dan)
2. Choose president: 2 ways (not Ann, not secretary)
3. Choose treasurer: 2 ways (remaining people)

Total = 2 × 2 × 2 = 8 ways ■

**Page 555**

### Permutations

A **permutation** of a set of objects is an ordering of the objects in a row.

**Theorem 9.2.2**
For any integer n ≥ 1, the number of permutations of a set with n elements is n!

**Proof idea:**
- Position 1: n choices
- Position 2: n-1 choices
- Position 3: n-2 choices
- ...
- Position n: 1 choice

Total = n × (n-1) × (n-2) × ... × 1 = n! ■

### Example 9.2.8 Arranging Books

In how many ways can 6 different books be arranged on a shelf?

**Solution:**
Number of arrangements = 6! = 720 ■

**Page 556**

### Example 9.2.3 The Number of Elements in a Cartesian Product

Suppose A₁, A₂, A₃, and A₄ are sets with n₁, n₂, n₃, and n₄ elements, respectively. Show that the set A₁ × A₂ × A₃ × A₄ has n₁n₂n₃n₄ elements.

**Solution:**

Each element in A₁ × A₂ × A₃ × A₄ is an ordered 4-tuple of the form (a₁, a₂, a₃, a₄), where a₁ ∈ A₁, a₂ ∈ A₂, a₃ ∈ A₃, and a₄ ∈ A₄. Imagine the process of constructing these ordered tuples as a four-step operation:

Step 1: Choose the first element of the 4-tuple.
Step 2: Choose the second element of the 4-tuple.
Step 3: Choose the third element of the 4-tuple.
Step 4: Choose the fourth element of the 4-tuple.

There are n₁ ways to perform step 1, n₂ ways to perform step 2, n₃ ways to perform step 3, and n₄ ways to perform step 4. Hence, by the multiplication rule, there are n₁n₂n₃n₄ ways to perform the entire operation. Therefore, there are n₁n₂n₃n₄ distinct 4-tuples in A₁ × A₂ × A₃ × A₄. ■

### Example 9.2.4 Number of PINs without Repetition

In Example 9.2.2 we formed PINs using four symbols, either letters of the alphabet or digits, and supposing that letters could be repeated. Now suppose that repetition is not allowed.

a. How many different PINs are there?
b. If all PINs are equally likely, what is the probability that a PIN chosen at random contains no repeated symbol?

**Solution:**

a. Again think of forming a PIN as a four-step operation: Choose the first symbol, then the second, then the third, and then the fourth. There are 36 ways to choose the first symbol, 35 ways to choose the second (since the first symbol cannot be used again), 34 ways to choose the third (since the first two symbols cannot be reused), and 33 ways to choose the fourth (since the first three symbols cannot be reused). Thus, the multiplication rule can be applied to conclude that there are 36 · 35· 34· 33 = 1,413,720 different PINs with no repeated symbol.

b. By part (a) there are 1,413,720 PINs with no repeated symbol, and by Example 9.2.2 there are 1,679,616 PINs in all. Thus the probability that a PIN chosen at random contains no repeated symbol is 1,413,720/1,679,616 ≈ 0.8417. In other words, approximately 84% of PINs have no repeated symbol. ■

**Page 557**

### Example 9.2.5 Number of Input/Output Tables for a Circuit with Two Input Signals

Consider the set of all circuits with two input signals P and Q. For each such circuit an input/output table can be constructed, but, as shown in Section 2.4, two such input/output tables may have the same values. How many distinct input/output tables can be constructed for circuits with input/output signals P and Q?

**Solution:**

Fix the order of the input values for P and Q. Then two input/output tables are distinct if their output values differ in at least one row. For example, the input/output tables shown below are distinct, because their output values differ in the first row.

| P | Q | Output |     | P | Q | Output |
|---|---|--------|     |---|---|--------|
| 1 | 1 | 1      |     | 1 | 1 | 0      |
| 1 | 0 | 0      |     | 1 | 0 | 0      |
| 0 | 1 | 1      |     | 0 | 1 | 1      |
| 0 | 0 | 0      |     | 0 | 0 | 0      |

For a fixed ordering of input values, you can obtain a complete input/output table by filling in the entries in the output column. You can think of this as a four-step operation:

Step 1: Fill in the output value for the first row.
Step 2: Fill in the output value for the second row.
Step 3: Fill in the output value for the third row.
Step 4: Fill in the output value for the fourth row.

Each step can be performed in exactly two ways: either a 1 or a 0 can be filled in. Hence, by the multiplication rule, there are

2 · 2 ·2 · 2 = 16

ways to perform the entire operation. It follows that there are 2⁴ = 16 distinct input/output tables for a circuit with two input signals P and Q. This means that such a circuit can function in only 16 distinct ways. ■

**Page 558**

### Example 9.2.6 Counting the Number of Iterations of a Nested Loop

Consider the following nested loop:
```
for i := 1 to 4
    for j := 1 to 3
        [Statements in body of inner loop.
        None contain branching statements
        that lead out of the inner loop.]
    next j
next i
```

How many times will the inner loop be iterated when the algorithm is implemented and run?

**Solution:**

The outer loop is iterated four times, and during each iteration of the outer loop, there are three iterations of the inner loop. Hence by the multiplication rule, the total number of iterations of the inner loop is 4· 3 = 12. This is illustrated by the trace table below.

| i | j |   |   |   | Total |
|---|---|---|---|---|-------|
| 1 | 1 | 2 | 3 |   |   3   |
| 2 | 1 | 2 | 3 |   |   3   |
| 3 | 1 | 2 | 3 |   |   3   |
| 4 | 1 | 2 | 3 |   |   3   |
|   |   |   |   |   |  12   |

■

### When the Multiplication Rule Is Difficult or Impossible to Apply

Consider the following problem:

Three officers—a president, a treasurer, and a secretary—are to be chosen from among four people: Ann, Bob, Cyd, and Dan. Suppose that, for various reasons, Ann cannot be president and either Cyd or Dan must be secretary. How many ways can the officers be chosen?

**Page 559**

### Example 9.2.7 A More Subtle Use of the Multiplication Rule

Reorder the steps for choosing the officers in the previous example so that the total number of ways to choose officers can be computed using the multiplication rule.

**Solution:**

Step 1: Choose the secretary.
Step 2: Choose the president.
Step 3: Choose the treasurer.

There are exactly two ways to perform step 1 (either Cyd or Dan may be chosen), two ways to perform step 2 (neither Ann nor the person chosen in step 1 may be chosen but either of the other two may), and two ways to perform step 3 (either of the two people not chosen as secretary or president may be chosen as treasurer). Thus, by the multiplication rule, the total number of ways to choose officers is 2 · 2 ·2 = 8. ■

### Permutations

A permutation of a set of objects is an ordering of the objects in a row. For example, the set of elements a, b, and c has six permutations.

abc    acb    cba    bac    bca    cab

In general, given a set of n objects, how many permutations does the set have? Imagine forming a permutation as an n-step operation:

Step 1: Choose an element to write first.
Step 2: Choose an element to write second.
...
Step n: Choose an element to write nth.

**Page 560**

Any element of the set can be chosen in step 1, so there are n ways to perform step 1. Any element except that chosen in step 1 can be chosen in step 2, so there are n − 1 ways to perform step 2. In general, the number of ways to perform each successive step is one less than the number of ways to perform the preceding step. At the point when the nth element is chosen, there is only one element left, so there is only one way to perform step n. Hence, by the multiplication rule, there are

n(n − 1)(n − 2) · · · 2 ·1 = n!

ways to perform the entire operation. In other words, there are n! permutations of a set of n elements. This reasoning is summarized in the following theorem. A formal proof uses mathematical induction and is left as an exercise.

**Theorem 9.2.2**
For any integer n with n ≥ 1, the number of permutations of a set with n elements is n!.

### Example 9.2.8 Permutations of the Letters in a Word

a. How many ways can the letters in the word COMPUTER be arranged in a row?
b. How many ways can the letters in the word COMPUTER be arranged if the letters CO must remain next to each other (in order) as a unit?
c. If letters of the word COMPUTER are randomly arranged in a row, what is the probability that the letters CO remain next to each other (in order) as a unit?

**Solution:**

a. All the eight letters in the word COMPUTER are distinct, so the number of ways in which we can arrange the letters equals the number of permutations of a set of eight elements. This equals 8! = 40,320.

b. If the letter group CO is treated as a unit, then there are effectively only seven objects that are to be arranged in a row.

CO    M    P    U    T    E    R

Hence there are as many ways to write the letters as there are permutations of a set of seven elements, namely 7! = 5,040.

c. When the letters are arranged randomly in a row, the total number of arrangements is 40,320 by part (a), and the number of arrangements with the letters CO next to each other (in order) as a unit is 5,040. Thus the probability is

5,040/40,320 = 1/8 = 12.5%. ■

### Example 9.2.9 Permutations of Objects Around a Circle

At a meeting of diplomats, the six participants are to be seated around a circular table. Since the table has no ends to confer particular status, it doesn't matter who sits in which chair. But it does matter how the diplomats are seated relative to each other. In other words, two seatings are considered the same if one is a rotation of the other. How many different ways can the diplomats be seated?

**Page 561**

**Solution:**

Call the diplomats by the letters A, B, C, D, E, and F. Since only relative position matters, you can start with any diplomat (say A), place that diplomat anywhere (say in the top seat of the diagram shown in Figure 9.2.5), and then consider all arrangements of the other diplomats around that one. B through F can be arranged in the seats around diplomat A in all possible orders. So there are 5! = 120 ways to seat the group. ■

### Permutations of Selected Elements

Given the set {a, b, c}, there are six ways to select two letters from the set and write them in order.

ab    ac    ba    bc    ca    cb

Each such ordering of two elements of {a, b, c} is called a 2-permutation of {a, b, c}.

• **Definition**
An r-permutation of a set of n elements is an ordered selection of r elements taken from the set of n elements. The number of r-permutations of a set of n elements is denoted P(n, r).

**Theorem 9.2.3**
If n and r are integers and 1 ≤ r ≤ n, then the number of r-permutations of a set of n elements is given by the formula

P(n, r) = n(n − 1)(n − 2) · · · (n − r + 1)    first version

or, equivalently,

P(n, r) = n!/(n − r)!    second version.

A formal proof of this theorem uses mathematical induction and is based on the multiplication rule. The idea of the proof is the following.

Suppose a set of n elements is given. Formation of an r-permutation can be thought of as an r-step process. Step 1 is to choose the element to be first. Since the set has n elements, there are n ways to perform step 1. Step 2 is to choose the element to be second. Since the element chosen in step 1 is no longer available, there are n − 1 ways to perform step 2. Step 3 is to choose the element to be third. Since neither of the two elements chosen in the first two steps is available, there are n − 2 choices for step 3. This process is repeated r times, as shown on the next page.

**Page 562**

```
Pool of available
elements: x₁, x₂, . . . , xₙ

n choices         Position 1
n - 1 choices     Position 2
n - 2 choices     Position 3
    ⋮                 ⋮
n - (r - 1) choices   Position r
```

The number of ways to perform each successive step is one less than the number of ways to perform the preceding step. Step r is to choose the element to be rth. At the point just before step r is performed, r − 1 elements have already been chosen, and so there are

n − (r − 1) = n − r + 1

left to choose from. Hence there are n − r + 1 ways to perform step r. It follows by the multiplication rule that the number of ways to form an r-permutation is

P(n, r) = n(n − 1)(n − 2) · · · (n − r + 1).

Note that

n(n − 1)(n − 2) · · · (n − r + 1)(n − r)(n − r − 1) · · · 3 · 2· 1 / (n − r)(n − r − 1) · · · 3 · 2· 1 = n!/(n − r)!
= n(n − 1)(n − 2) · · · (n − r + 1).

Thus the formula can be written as

P(n, r) = n!/(n − r)!.

The second version of the formula is easier to remember. When you actually use it, however, first substitute the values of n and r and then immediately cancel the numerical value of (n − r)! from the numerator and denominator. Because factorials become so large so fast, direct use of the second version of the formula without cancellation can overload your calculator's capacity for exact arithmetic even when n and r are quite small. For instance, if n = 15 and r = 2, then

n!/(n − r)! = 15!/13! = 1,307,674,368,000/6,227,020,800.

But if you cancel (n − r)! = 13! from numerator and denominator before multiplying out, you obtain

n!/(n − r)! = 15!/13! = 15· 14· 13!/13! = 15· 14 = 210.

In fact, many scientific calculators allow you to compute P(n, r) simply by entering the values of n and r and pressing a key or making a menu choice. Alternative notations for P(n, r) that you may see in your calculator manual are ₙPᵣ, Pₙ,ᵣ and ⁿPᵣ.

### Example 9.2.10 Evaluating r-Permutations

a. Evaluate P(5, 2).
b. How many 4-permutations are there of a set of seven objects?
c. How many 5-permutations are there of a set of five objects?

**Page 563**

**Solution:**

a. P(5, 2) = 5!/(5 − 2)! = 5 · 4 ·3· 2· 1/3· 2· 1 = 20

b. The number of 4-permutations of a set of seven objects is
   P(7, 4) = 7!/(7 − 4)! = 7 · 6 · 5· 4 ·3· 2· 1/3· 2· 1 = 7 · 6 ·5 · 4 = 840.

c. The number of 5-permutations of a set of five objects is
   P(5, 5) = 5!/(5 − 5)! = 5!/0! = 5!/1 = 5! = 120.

Note that the definition of 0! as 1 makes this calculation come out as it should, for the number of 5-permutations of a set of five objects is certainly equal to the number of permutations of the set. ■

### Example 9.2.11 Permutations of Selected Letters of a Word

a. How many different ways can three of the letters of the word BYTES be chosen and written in a row?
b. How many different ways can this be done if the first letter must be B?

**Solution:**

a. The answer equals the number of 3-permutations of a set of five elements. This equals
   P(5, 3) = 5!/(5 − 3)! = 5 · 4 ·3 · 2· 1/2· 1 = 5 ·4 · 3 = 60.

b. Since the first letter must be B, there are effectively only two letters to be chosen and placed in the other two positions. And since the B is used in the first position, there are four letters available to fill the remaining two positions.

```
Pool of available
letters: Y, T, E, S

B        Position 2    Position 3
Position 1
```

Hence the answer is the number of 2-permutations of a set of four elements, which is
P(4, 2) = 4!/(4 − 2)! = 4 · 3 · 2· 1/2· 1 = 4 ·3 = 12. ■

In many applications of the mathematics of counting, it is necessary to be skillful in working algebraically with quantities of the form P(n, r). The next example shows a kind of problem that gives practice in developing such skill.

### Example 9.2.12 Proving a Property of P(n, r)

Prove that for all integers n ≥ 2,
P(n, 2) + P(n, 1) = n².

**Page 564**

**Solution:**

Suppose n is an integer that is greater than or equal to 2. By Theorem 9.2.3,
P(n, 2) = n!/(n − 2)! = n(n − 1)(n − 2)!/(n − 2)! = n(n − 1)

and
P(n, 1) = n!/(n − 1)! = n · (n − 1)!/(n − 1)! = n.

Hence
P(n, 2) + P(n, 1) = n · (n − 1) + n = n² − n + n = n²,

which is what we needed to show. ■

### Test Yourself

1. The multiplication rule says that if an operation can be performed in k steps and, for each i with 1 ≤ i ≤ k, the ith step can be performed in nᵢ ways (regardless of how previous steps were performed), then the operation as a whole can be performed in _____.

2. A permutation of a set of elements is _____.

3. The number of permutations of a set of n elements equals _____.

4. An r-permutation of a set of n elements is _____.

5. The number of r-permutations of a set of n elements is denoted _____.

6. One formula for the number of r-permutations of a set of n elements is _____ and another formula is _____.

**Page 565**

### Exercise Set 9.2

In 1–4, use the fact that in baseball's World Series, the first team to win four games wins the series.

1. Suppose team A wins the first three games. How many ways can the series be completed? (Draw a tree.)

2. Suppose team A wins the first two games. How many ways can the series be completed? (Draw a tree.)

3. How many ways can a World Series be played if team A wins four games in a row?

4. How many ways can a World Series be played if no team wins two games in a row?

[Additional exercises 5-19 listed...]

**Page 566-567**

[Exercises 20-47 continue with various probability and counting problems]

### Answers for Test Yourself

1. n₁n₂ · · · nₖ ways
2. an ordering of the elements of the set in a row
3. n!
4. an ordered selection of r of the elements of the set
5. P(n, r)
6. n(n − 1)(n − 2) · · · (n − r + 1); n!/(n−r)!

---

## 9.3 Counting Elements of Disjoint Sets: The Addition Rule

**Page 568**

> The whole of science is nothing more than a refinement of everyday thinking.
> — Albert Einstein, 1879–1955

In the last section we discussed counting problems that can be solved using possibility trees. In this section we look at counting problems that can be solved by counting the number of elements in the union of two sets, the difference of two sets, or the intersection of two sets.

The basic rule underlying the calculation of the number of elements in a union or difference or intersection is the addition rule. This rule states that the number of elements in a union of mutually disjoint finite sets equals the sum of the number of elements in each of the component sets.

**Theorem 9.3.1 The Addition Rule**

Suppose a finite set A equals the union of k distinct mutually disjoint subsets A₁, A₂, . . . , Aₖ. Then

N(A) = N(A₁) + N(A₂) + · · · + N(Aₖ).

A formal proof of this theorem uses mathematical induction and is left to the exercises.

### Example 9.3.1 Counting Passwords with Three or Fewer Letters

A computer access password consists of from one to three letters chosen from the 26 in the alphabet with repetitions allowed. How many different passwords are possible?

**Solution:**

The set of all passwords can be partitioned into subsets consisting of those of length 1, those of length 2, and those of length 3 as shown in Figure 9.3.1.

```
Set of All Passwords of Length ≤ 3
    /          |          \
passwords   passwords   passwords
of length 1 of length 2 of length 3
```

By the addition rule, the total number of passwords equals the number of passwords of length 1, plus the number of passwords of length 2, plus the number of passwords of length 3. Now the

number of passwords of length 1 = 26 (because there are 26 letters in the alphabet)

number of passwords of length 2 = 26² (because forming such a word can be thought of as a two-step process in which there are 26 ways to perform each step)

number of passwords of length 3 = 26³ (because forming such a word can be thought of as a three-step process in which there are 26 ways to perform each step).

Hence the total number of passwords = 26 + 26² + 26³ = 18,278. ■

**Page 569**

### Example 9.3.2 Counting the Number of Integers Divisible by 5

How many three-digit integers (integers from 100 to 999 inclusive) are divisible by 5?

**Solution:**

One solution to this problem was discussed in Example 9.1.4. Another approach uses the addition rule. Integers that are divisible by 5 end either in 5 or in 0. Thus the set of all three-digit integers that are divisible by 5 can be split into two mutually disjoint subsets A₁ and A₂ as shown in Figure 9.3.2.

```
Three-Digit Integers That Are Divisible by 5
           /                \
three-digit integers    three-digit integers
that end in 0          that end in 5
      A₁                     A₂

A₁ ∪ A₂ = the set of all three-digit integers that are divisible by 5
A₁ ∩ A₂ = ∅
```

Now there are as many three-digit integers that end in 0 as there are possible choices for the left-most and middle digits (because the right-most digit must be a 0). As illustrated below, there are nine choices for the left-most digit (the digits 1 through 9) and ten choices for the middle digit (the digits 0 through 9). Hence N(A₁) = 9 · 10 = 90.

```
_ _ 0
↑   ↑   ↑
9   10  number ends in 0
choices choices
1,2,3,4,5,6,7,8,9  0,1,2,3,4,5,6,7,8,9
```

Similar reasoning (using 5 instead of 0) shows that N(A₂) = 90 also. So

[the number of three-digit integers that are divisible by 5] = N(A₁) + N(A₂) = 90 + 90 = 180. ■

### The Difference Rule

An important consequence of the addition rule is the fact that if the number of elements in a set A and the number in a subset B of A are both known, then the number of elements that are in A and not in B can be computed.

**Theorem 9.3.2 The Difference Rule**

If A is a finite set and B is a subset of A, then
N(A − B) = N(A) − N(B).

**Page 570**

The difference rule is illustrated in Figure 9.3.3.

```
A (n elements)
    B (k elements)
    A - B (n - k elements)
```

Figure 9.3.3 The Difference Rule

The difference rule holds for the following reason: If B is a subset of A, then the two sets B and A − B have no elements in common and B ∪ (A − B) = A. Hence, by the addition rule,

N(B) + N(A − B) = N(A).

Subtracting N(B) from both sides gives the equation

N(A − B) = N(A) − N(B).

### Example 9.3.3 Counting PINs with Repeated Symbols

The PINs discussed in Examples 9.2.2 and 9.2.4 are made from exactly four symbols chosen from the 26 letters of the alphabet and the ten digits, with repetitions allowed.

a. How many PINs contain repeated symbols?
b. If all PINs are equally likely, what is the probability that a randomly chosen PIN contains a repeated symbol?

**Solution:**

a. According to Example 9.2.2, there are 36⁴ = 1,679,616 PINs when repetition is allowed, and by Example 9.2.4, there are 1,413,720 PINs when repetition is not allowed. Thus, by the difference rule, there are

1,679,616 − 1,413,720 = 265,896

PINs that contain at least one repeated symbol.

b. By Example 9.2.2 there are 1,679,616 PINs in all, and by part (a) 265,896 of these contain at least one repeated symbol. Thus, by the equally likely probability formula, the probability that a randomly chosen PIN contains a repeated symbol is 265,896/1,679,616 ≈ 0.158 = 15.8%. ■

An alternative solution to Example 9.3.3(b) is based on the observation that if S is the set of all PINs and A is the set of all PINs with no repeated symbol, then S − A is the set of all PINs with at least one repeated symbol. It follows that

P(S − A) = N(S − A)/N(S)    by definition of probability in the equally likely case
         = [N(S) − N(A)]/N(S)    by the difference rule
         = N(S)/N(S) − N(A)/N(S)    by the laws of fractions
         = 1 − P(A)    by definition of probability in the equally likely case
         ≈ 1 − 0.842    by Example 9.2.4
         ≈ 0.158 = 15.8%

**Page 571**

This solution illustrates a more general property of probabilities: that the probability of the complement of an event is obtained by subtracting the probability of the event from the number 1. In Section 9.8 we derive this formula from the axioms for probability.

**Formula for the Probability of the Complement of an Event**

If S is a finite sample space and A is an event in S, then
P(Aᶜ) = 1 − P(A).

### Example 9.3.4 Number of Python Identifiers of Eight or Fewer Characters

In the computer language Python, identifiers must start with one of 53 symbols: either one of the 52 letters of the upper- and lower-case Roman alphabet or an underscore (_). The initial character may stand alone, or it may be followed by any number of additional characters chosen from a set of 63 symbols: the 53 symbols allowed as an initial character plus the ten digits. Certain keywords, however, such as and, if, print, and so forth, are set aside and may not be used as identifiers. In one implementation of Python there are 31 such reserved keywords, none of which has more than eight characters. How many Python identifiers are there that are less than or equal to eight characters in length?

**Solution:**

The set of all Python identifiers with eight or fewer characters can be partitioned into eight subsets—identifiers of length 1, identifiers of length 2, and so on—as shown in Figure 9.3.4. The reserved words have various lengths (all less than or equal to 8), so the set of reserved words is shown overlapping the various subsets.

```
Set of Python Identifiers with Eight or Fewer Characters
length length length length length length length length
  1      2      3      4      5      6      7      8
                Reserved words
```

According to the rules for creating Python identifiers, there are

53 potential identifiers of length 1    because there are 53 choices for the first character

53· 63 potential identifiers of length 2    because the first character can be any one of 53 symbols, and the second character can be any one of 63 symbols

53· 63² potential identifiers of length 3    because the first character can be any one of 53 symbols, and each of the next two characters can be any one of 63 symbols

...

53· 63⁷ potential identifiers of length 8    because the first character can be any one of 53 symbols, and each of the next seven characters can be any one of 63 symbols.

**Page 572**

Thus, by the addition rule, the number of potential Python identifiers with eight or fewer characters is

53 + 53· 63 + 53· 63² + 53· 63³ + 53· 63⁴ + 53· 63⁵ + 53· 63⁶ + 53· 63⁷

= 53(63⁸ − 1)/(63 − 1)

= 212,133,167,002,880.

Now 31 of these potential identifiers are reserved, so by the difference rule, the actual number of Python identifiers with eight or fewer characters is

212,133,167,002,880 − 31 = 212,133,167,002,849. ■

### Example 9.3.5 Internet Addresses

In order to communicate effectively, each computer in a network needs a distinguishing name called an address. For the Internet this address is currently a 32-bit number called the Internet Protocol (IP) address (although 128-bit addresses are being phased in to accommodate the growth of the Internet). For technical reasons some computers have more than one address, whereas other sets of computers, which use the Internet only sporadically, may share a pool of addresses that are assigned on a temporary basis. Like telephone numbers, IP addresses are divided into parts: one, the network ID, specifies the local network to which a given computer belongs, and the other, the host ID, specifies the particular computer.

An example of an IP address is 10001100 11000000 00100000 10001000, where the 32 bits have been divided into four groups of 8 for easier reading. To make the reading even easier, IP addresses are normally written as "dotted decimals," in which each group of 8 bits is converted into a decimal number between 0 and 255. For instance, the IP address above converts into 140.192.32.136.

In order to accommodate the various sizes of the local networks connected through the Internet, the network IDs are divided into several classes, the most important of which are called A, B, and C. In every class, a host ID may not consist of either all 0's or all 1's.

Class A network IDs are used for very large local networks. The left-most bit is set to 0, and the left-most 8 bits give the full network ID. The remaining 24 bits are used for individual host IDs. However, neither 00000000 nor 01111111 is allowed as a network ID for a class A IP address.

```
Class A: 0[Network ID - 8 bits][Host ID - 24 bits]
```

Class B network IDs are used for medium to large local networks. The two left-most bits are set to 10, and the left-most 16 bits give the full network ID. The remaining 16 bits are used for individual host IDs.

```
Class B: 10[Network ID - 16 bits][Host ID - 16 bits]
```

Class C network IDs are used for small local networks. The three left-most bits are set to 110, and the left-most 24 bits give the full network ID. The remaining 8 bits are used for individual host IDs.

**Page 573**

```
Class C: 110[Network ID - 24 bits][Host ID - 8 bits]
```

a. Check that the dotted decimal form of 10001100 11000000 00100000 10001000 is 140.192.32.136.
b. How many Class B networks can there be?
c. What is the dotted decimal form of the IP address for a computer in a Class B network?
d. How many host IDs can there be for a Class B network?

**Solution:**

a. 10001100 = 1 · 2⁷ + 1 · 2³ + 1 · 2² = 128 + 8 + 4 = 140
   11000000 = 1· 2⁷ + 1 · 2⁶ = 128 + 64 = 192
   00100000 = 1 · 2⁵ = 32
   10001000 = 1 · 2⁷ + 1 · 2³ = 128 + 8 = 136

b. The network ID for a Class B network consists of 16 bits and begins with 10. Because there are two choices for each of the remaining 14 positions (either 0 or 1), the total number of possible network IDs is 2¹⁴, or 16,384.

c. The network ID part of a Class B IP address goes from 10000000 00000000 to 10111111 11111111.
   As dotted decimals, these numbers range from 128.0 to 191.255 because 10000000₂ = 128₁₀, 00000000₂ = 0₁₀, 10111111₂ = 191₁₀, and 11111111₂ = 255₁₀. Thus the dotted decimal form of the IP address of a computer in a Class B network is w.x.y.z, where 128 ≤ w ≤ 191, 0 ≤ x ≤ 255, 0 ≤ y ≤ 255, and 0 ≤ z ≤ 255. However, y and z are not allowed both to be 0 or both to be 255 because host IDs may not consist of either all 0's or all 1's.

d. For a class B network, 16 bits are used for host IDs. Having two choices (either 0 or 1) for each of 16 positions gives a potential total of 2¹⁶, or 65,536, host IDs. But because two of these are not allowed (all 0's and all 1's), the total number of host IDs is 65,534. ■

### The Inclusion/Exclusion Rule

The addition rule says how many elements are in a union of sets if the sets are mutually disjoint. Now consider the question of how to determine the number of elements in a union of sets when some of the sets overlap. For simplicity, begin by looking at a union of two sets A and B, as shown in Figure 9.3.5.

```
    A       B
  A ∩ B   A ∩ B   A ∩ B
```

Figure 9.3.5

**Page 574**

First observe that the number of elements in A ∪ B varies according to the number of elements the two sets have in common. If A and B have no elements in common, then N(A ∪ B) = N(A) + N(B). If A and B coincide, then N(A ∪ B) = N(A). Thus any general formula for N(A ∪ B) must contain a reference to the number of elements the two sets have in common, N(A ∩ B), as well as to N(A) and N(B).

The simplest way to derive a formula for N(A ∪ B) is to reason as follows: The number N(A) counts the elements that are in A and not in B and also the elements that are in both A and B. Similarly, the number N(B) counts the elements that are in B and not in A and also the elements that are in both A and B. Hence when the two numbers N(A) and N(B) are added, the elements that are in both A and B are counted twice. To get an accurate count of the elements in A ∪ B, it is necessary to subtract the number of elements that are in both A and B. Because these are the elements in A ∩ B,

N(A ∪ B) = N(A) + N(B) − N(A ∩ B).

A similar analysis gives a formula for the number of elements in a union of three sets, as shown in Theorem 9.3.3.

**Theorem 9.3.3 The Inclusion/Exclusion Rule for Two or Three Sets**

If A, B, and C are any finite sets, then

N(A ∪ B) = N(A) + N(B) − N(A ∩ B)

and

N(A ∪ B ∪ C) = N(A) + N(B) + N(C) − N(A ∩ B) − N(A ∩ C) − N(B ∩ C) + N(A ∩ B ∩ C).

It can be shown using mathematical induction (see exercise 48 at the end of this section) that formulas analogous to those of Theorem 9.3.3 hold for unions of any finite number of sets.

### Example 9.3.6 Counting Elements of a General Union

a. How many integers from 1 through 1,000 are multiples of 3 or multiples of 5?
b. How many integers from 1 through 1,000 are neither multiples of 3 nor multiples of 5?

**Solution:**

a. Let A = the set of all integers from 1 through 1,000 that are multiples of 3.
   Let B = the set of all integers from 1 through 1,000 that are multiples of 5.

   Then
   A ∪ B = the set of all integers from 1 through 1,000 that are multiples of 3 or multiples of 5

   and
   A ∩ B = the set of all integers from 1 through 1,000 that are multiples of both 3 and 5
         = the set of all integers from 1 through 1,000 that are multiples of 15.

   [Now calculate N(A), N(B), and N(A ∩ B) and use the inclusion/exclusion rule to solve for N(A ∪ B).]

**Page 575**

Because every third integer from 3 through 999 is a multiple of 3, each can be represented in the form 3k, for some integer k from 1 through 333. Hence there are 333 multiples of 3 from 1 through 1,000, and so N(A) = 333.

```
1  2  3  4  5  6  ...  996  997  998  999
      ↑     ↑          ↑         ↑
     3·1   3·2       3·332      3·333
```

Similarly, each multiple of 5 from 1 through 1,000 has the form 5k, for some integer k from 1 through 200.

```
1 2 3 4 5 6 7 8 9 10 ... 995 996 997 998 999 1,000
        ↑         ↑       ↑                   ↑
       5·1       5·2    5·199               5·200
```

Thus there are 200 multiples of 5 from 1 through 1,000 and N(B) = 200.

Finally, each multiple of 15 from 1 through 1,000 has the form 15k, for some integer k from 1 through 66 (since 990 = 66· 15).

```
1  2 ...  15  ...  30  ...  975  ...  990  ...  999  1,000
          ↑        ↑         ↑         ↑
        15·1     15·2      15·65     15·66
```

Hence there are 66 multiples of 15 from 1 through 1,000, and N(A ∩ B) = 66.

It follows by the inclusion/exclusion rule that

N(A ∪ B) = N(A) + N(B) − N(A ∩ B)
         = 333 + 200 − 66
         = 467.

Thus, 467 integers from 1 through 1,000 are multiples of 3 or multiples of 5.

b. There are 1,000 integers from 1 through 1,000, and by part (a), 467 of these are multiples of 3 or multiples of 5. Thus, by the set difference rule, there are 1,000 − 467 = 533 that are neither multiples of 3 nor multiples of 5. ■

Note that the solution to part (b) of Example 9.3.6 hid a use of De Morgan's law. The number of elements that are neither in A nor in B is N(Aᶜ ∩ Bᶜ), and by De Morgan's law, Aᶜ ∩ Bᶜ = (A ∪ B)ᶜ. So N((A ∪ B)ᶜ) was then calculated using the set difference rule: N((A ∪ B)ᶜ) = N(U) − N(A ∪ B), where the universe U was the set of all integers from 1 through 1,000. Exercises 37–39 at the end of this section explore this technique further.

### Example 9.3.7 Counting the Number of Elements in an Intersection

A professor in a discrete mathematics class passes out a form asking students to check all the mathematics and computer science courses they have recently taken. The finding is that out of a total of 50 students in the class,

30 took precalculus;            16 took both precalculus and Java;
18 took calculus;               8 took both calculus and Java;
26 took Java;                   47 took at least one of the three courses.
9 took both precalculus and calculus;

**Page 576**

Note that when we write "30 students took precalculus," we mean that the total number of students who took precalculus is 30, and we allow for the possibility that some of these students may have taken one or both of the other courses. If we want to say that 30 students took precalculus only (and not either of the other courses), we will say so explicitly.

a. How many students did not take any of the three courses?
b. How many students took all three courses?
c. How many students took precalculus and calculus but not Java? How many students took precalculus but neither calculus nor Java?

**Solution:**

a. By the difference rule, the number of students who did not take any of the three courses equals the number in the class minus the number who took at least one course. Thus the number of students who did not take any of the three courses is 50 − 47 = 3.

b. Let
   P = the set of students who took precalculus
   C = the set of students who took calculus
   J = the set of students who took Java.

   Then, by the inclusion/exclusion rule,

   N(P ∪ C ∪ J) = N(P) + N(C) + N(J) − N(P ∩ C) − N(P ∩ J) − N(C ∩ J) + N(P ∩ C ∩ J)

   Substituting known values, we get

   47 = 30 + 26 + 18 − 9 − 16 − 8 + N(P ∩ C ∩ J).

   Solving for N(P ∩ C ∩ J) gives

   N(P ∩ C ∩ J) = 6.

   Hence there are six students who took all three courses. In general, if you know any seven of the eight terms in the inclusion/exclusion formula for three sets, you can solve for the eighth term.

c. To answer the questions of part (c), look at the diagram in Figure 9.3.6.

```
            P                    J
         11    10
           3  6  8
             2
         7
            C
                3
```

Figure 9.3.6

**Page 577**

Since N(P ∩ C ∩ J) = 6, put the number 6 inside the innermost region. Then work outward to find the numbers of students represented by the other regions of the diagram. For example, since nine students took both precalculus and calculus and six took all three courses, 9 − 6 = 3 students took precalculus and calculus but not Java. Similarly, since 16 students took precalculus and Java and six took all three courses, 16 − 6 = 10 students took precalculus and Java but not calculus. Now the total number of students who took precalculus is 30. Of these 30, three also took calculus but not Java, ten took Java but not calculus, and six took both calculus and Java. That leaves 11 students who took precalculus but neither of the other two courses.

A similar analysis can be used to fill in the numbers for the other regions of the diagram. ■

### Test Yourself

1. The addition rule says that if a finite set A equals the union of k distinct mutually disjoint subsets A₁, A₂, . . . , Aₖ, then _____.

2. The difference rule says that if A is a finite set and B is a subset of A, then _____.

3. If S is a finite sample space and A is an event in S, then the probability of Aᶜ equals _____.

4. The inclusion/exclusion rule for two sets says that if A and B are any finite sets, then _____.

5. The inclusion/exclusion rule for three sets says that if A, B, and C are any finite sets, then _____.

**Page 578-580**

### Exercise Set 9.3

[Various exercises numbered 1-49 with problems about counting, probability, and set theory]

### Answers for Test Yourself

1. the number of elements in A equals N(A₁) + N(A₂) + . . . + N(Aₙ)
2. the number of elements in A − B is the difference between the number of elements in A and the number of elements in B, that is, N(A − B) = N(A) − N(B).
3. 1 − P(A)
4. N(A ∪ B) = N(A) + N(B) − N(A ∩ B)
5. N(A ∪ B ∪ C) = N(A) + N(B) + N(C) − N(A ∩ B) − N(A ∩ C) − N(B ∩ C) + N(A ∩ B ∩ C)

---

## 9.4 The Pigeonhole Principle

**Page 582**

> The shrewd guess, the fertile hypothesis, the courageous leap to a tentative conclusion—these are the most valuable coin of the thinker at work
> — Jerome S. Bruner, 1960

The pigeonhole principle states that if n pigeons fly into m pigeonholes and n > m, then at least one hole must contain two or more pigeons. This principle is illustrated in Figure 9.4.1 for n = 5 and m = 4. Illustration (a) shows the pigeons perched next to their holes, and (b) shows the correspondence from pigeons to pigeonholes. The pigeonhole principle is sometimes called the Dirichlet box principle because it was first stated formally by J. P. G. L. Dirichlet (1805–1859).

```
Pigeons           Pigeonholes
   2                   1
 1   2                 2
   3                   3
 1   3                 4
   4
 4   5
   (a)                (b)
```

Figure 9.4.1

Illustration (b) suggests the following mathematical way to phrase the principle.

**Pigeonhole Principle**

A function from one finite set to a smaller finite set cannot be one-to-one: There must be a least two elements in the domain that have the same image in the co-domain.

Thus an arrow diagram for a function from a finite set to a smaller finite set must have at least two arrows from the domain that point to the same element of the co-domain. In Figure 9.4.1(b), arrows from pigeons 1 and 4 both point to pigeonhole 3.

Since the truth of the pigeonhole principle is easy to accept on an intuitive basis, we move immediately to applications, leaving a formal proof to the end of the section. Applications of the pigeonhole principle range from the totally obvious to the extremely subtle. A representative sample is given in the examples and exercises that follow.

### Example 9.4.1 Applying the Pigeonhole Principle

a. In a group of six people, must there be at least two who were born in the same month? In a group of thirteen people, must there be at least two who were born in the same month? Why?

b. Among the residents of New York City, must there be at least two people with the same number of hairs on their heads? Why?

**Page 583**

**Solution:**

a. A group of six people need not contain two who were born in the same month. For instance, the six people could have birthdays in each of the six months January through June.

   A group of thirteen people, however, must contain at least two who were born in the same month, for there are only twelve months in a year and 13 > 12. To get at the essence of this reasoning, think of the thirteen people as the pigeons and the twelve months of the year as the pigeonholes. Denote the thirteen people by the symbols x₁, x₂, . . . , x₁₃ and define a function B from the set of people to the set of twelve months as shown in the following arrow diagram.

```
13 people (pigeons)        12 months (pigeonholes)
    x₁                           Jan
    x₂         B                 Feb
    ...    B(xᵢ) = birth         ...
    x₁₂    month of xᵢ           Dec
    x₁₃
```

The pigeonhole principle says that no matter what the particular assignment of months to people, there must be at least two arrows pointing to the same month. Thus at least two people must have been born in the same month.

b. The answer is yes. In this example the pigeons are the people of New York City and the pigeonholes are all possible numbers of hairs on any individual's head. Call the population of New York City P. It is known that P is at least 5,000,000. Also the maximum number of hairs on any person's head is known to be no more than 300,000. Define a function H from the set of people in New York City {x₁, x₂, . . . , xₚ} to the set {0, 1, 2, 3, . . . , 300,000}, as shown below.

```
People in New York City          Possible number of hairs on
    (pigeons)                     a person's head (pigeonholes)
    x₁                                    0
    x₂         H                         1
    x₃    H(xᵢ) = the number            2
    ...    of hairs on xᵢ's              ...
    xₚ        head                   300,000
```

Since the number of people in New York City is larger than the number of possible hairs on their heads, the function H is not one-to-one; at least two arrows point to the same number. But that means that at least two people have the same number of hairs on their heads. ■

**Page 584**

### Example 9.4.2 Finding the Number to Pick to Ensure a Result

A drawer contains ten black and ten white socks. You reach in and pull some out without looking at them. What is the least number of socks you must pull out to be sure to get a matched pair? Explain how the answer follows from the pigeonhole principle.

**Solution:**

If you pick just two socks, they may have different colors. But when you pick a third sock, it must be the same color as one of the socks already chosen. Hence the answer is three.

This answer could be phrased more formally as follows: Let the socks pulled out be denoted s₁, s₂, s₃, . . . , sₙ and consider the function C that sends each sock to its color, as shown below.

```
Socks pulled out (pigeons)      Colors (pigeonholes)
    s₁                              white
    s₂         C                    black
    ...    C(sᵢ) = color of sᵢ
    sₙ
```

If n = 2, C could be a one-to-one correspondence (if the two socks pulled out were of different colors). But if n > 2, then the number of elements in the domain of C is larger than the number of elements in the co-domain of C. Thus by the pigeonhole principle, C is not one-to-one: C(sᵢ) = C(sⱼ) for some sᵢ ≠ sⱼ. This means that if at least three socks are pulled out, then at least two of them have the same color. ■

### Example 9.4.3 Selecting a Pair of Integers with a Certain Sum

Let A = {1, 2, 3, 4, 5, 6, 7, 8}.

a. If five integers are selected from A, must at least one pair of the integers have a sum of 9?
b. If four integers are selected from A, must at least one pair of the integers have a sum of 9?

**Solution:**

a. Yes. Partition the set A into the following four disjoint subsets:
   {1, 8},    {2, 7},    {3, 6},    and    {4, 5}

   Observe that each of the integers in A occurs in exactly one of the four subsets and that the sum of the integers in each subset is 9. Thus if five integers from A are chosen, then by the pigeonhole principle, two must be from the same subset. It follows that the sum of these two integers is 9.

   To see precisely how the pigeonhole principle applies, let the pigeons be the five selected integers (call them a₁, a₂, a₃, a₄, and a₅) and let the pigeonholes be the subsets of the partition. The function P from pigeons to pigeonholes is defined by letting P(aᵢ) be the subset that contains aᵢ.

**Page 585**

```
The 5 selected integers        The 4 subsets in the partition of A
    (pigeons)                           (pigeonholes)
    a₁                                    {1, 8}
    a₂         P                         {2, 7}
    a₃    P(aᵢ) = the subset            {3, 6}
    a₄    that contains aᵢ               {4, 5}
    a₅
```

The function P is well defined because for each integer aᵢ in the domain, aᵢ belongs to one of the subsets (since the union of the subsets is A) and aᵢ does not belong to more than one subset (since the subsets are disjoint).

Because there are more pigeons than pigeonholes, at least two pigeons must go to the same hole. Thus two distinct integers are sent to the same set. But that implies that those two integers are the two distinct elements of the set, so their sum is 9. More formally, by the pigeonhole principle, since P is not one-to-one, there are integers aᵢ and aⱼ such that

P(aᵢ) = P(aⱼ) and aᵢ ≠ aⱼ.

But then, by definition of P, aᵢ and aⱼ belong to the same subset. Since the elements in each subset add up to 9, aᵢ + aⱼ = 9.

b. The answer is no. This is a case where the pigeonhole principle does not apply; the number of pigeons is not larger than the number of pigeonholes. For instance, if you select the numbers 1, 2, 3, and 4, then since the largest sum of any two of these numbers is 7, no two of them add up to 9. ■

### Application to Decimal Expansions of Fractions

One important consequence of the pigeonhole principle is the fact that

**the decimal expansion of any rational number either terminates or repeats.**

A terminating decimal is one like 3.625, and a repeating decimal is one like 2.38246̄, where the bar over the digits 246 means that these digits are repeated forever.

Recall that a rational number is one that can be written as a ratio of integers—in other words, as a fraction. Recall also that the decimal expansion of a fraction is obtained by dividing its numerator by its denominator using long division. For example, the decimal expansion of 4/33 is obtained as follows:

```
        .1 2 1 2 1 2 1 2...
    33)4.0 0 0 0 0 0 0 0 0 0 0
       3 3
       ---
       7 0    ← These are the same number.
       6 6
       ---
       4 0
       3 3
       ---
       7 0
       6 6
       ---
       4 ...
```

**Page 586**

Because the number 4 reappears as a remainder in the long-division process, the sequence of quotients and remainders that give the digits of the decimal expansion repeats forever; hence the digits of the decimal expansion repeat forever.

In general, when one integer is divided by another, it is the pigeonhole principle (together with the quotient-remainder theorem) that guarantees that such a repetition of remainders and hence decimal digits must always occur. This is explained in the following example. The analysis in the example uses an obvious generalization of the pigeonhole principle, namely that a function from an infinite set to a finite set cannot be one-to-one.

### Example 9.4.4 The Decimal Expansion of a Fraction

Consider a fraction a/b, where for simplicity a and b are both assumed to be positive. The decimal expansion of a/b is obtained by dividing the a by the b as illustrated here for a = 3 and b = 14.

[Long division calculation shown]

Let r₀ = a and let r₁, r₂, r₃, . . . be the successive remainders obtained in the long division of a by b. By the quotient-remainder theorem, each remainder must be between 0 and b − 1. (In this example, a is 3 and b is 14, and so the remainders are from 0 to 13.) If some remainder rᵢ = 0, then the division terminates and a/b has a terminating decimal expansion. If no rᵢ = 0, then the division process and hence the sequence of remainders continues forever. By the pigeonhole principle, since there are more remainders than

**Page 587**

values that the remainders can take, some remainder value must repeat: rⱼ = rₖ, for some indices j and k with j < k. This is illustrated below for a = 3 and b = 14.

```
Sequence of remainders        Values of remainders when b = 14
    r₀                                   0
    r₁         F                        1
    r₂    F(rᵢ) = value of rᵢ          2
    ...                                 3
    r₇                                  ...
                                        13
```

It follows that the decimal digits obtained from the divisions between rⱼ and rₖ₋₁ repeat forever. In the case of 3/14, the repetition begins with r₇ = 2 = r₁ and the decimal expansion repeats the quotients obtained from the divisions from r₁ through r₆ forever: 3/14 = 0.2̄14285̄7̄. ■

Note that since the decimal expansion of any rational number either terminates or repeats, if a number has a decimal expansion that neither terminates nor repeats, then it cannot be rational. Thus, for example, the following number cannot be rational:

0.01011011101111011111 . . . (where each string of 1's is one longer than the previous string).

### Generalized Pigeonhole Principle

A generalization of the pigeonhole principle states that if n pigeons fly into m pigeonholes and, for some positive integer k, k < n/m, then at least one pigeonhole contains k + 1 or more pigeons. This is illustrated in Figure 9.4.2 for m = 4, n = 9, and k = 2. Since 2 < 9/4 = 2.25, at least one pigeonhole contains three (2 + 1) or more pigeons. (In this example, pigeonhole 3 contains three pigeons.)

```
Pigeons                    Pigeonholes
3    2                        1  →  1
  1    3    8                 2  →  2
    5 6    7                  3  →  3
  2    4                      4  →  4
      9                       5  →  3
  4                          6  →  3
     (a)                     7  →  3
                             8  →  3
                             9  →  4
                                (b)
```

Figure 9.4.2

**Generalized Pigeonhole Principle**

For any function f from a finite set X with n elements to a finite set Y with m elements and for any positive integer k, if k < n/m, then there is some y ∈ Y such that y is the image of at least k + 1 distinct elements of X.

**Page 588**

### Example 9.4.5 Applying the Generalized Pigeonhole Principle

Show how the generalized pigeonhole principle implies that in a group of 85 people, at least 4 must have the same last initial.

**Solution:**

In this example the pigeons are the 85 people and the pigeonholes are the 26 possible last initials of their names. Note that

3 < 85/26 ≈ 3.27.

Consider the function L from people to initials defined by the following arrow diagram.

```
85 people (pigeons)         26 initials (pigeonholes)
    x₁                            A
    x₂         L                  B
    ...    L(xᵢ) = the initial    ...
    x₈₅    of xᵢ's last name      Z
```

Since 3 < 85/26, the generalized pigeonhole principle states that some initial must be the image of at least four (3 + 1) people. Thus at least four people have the same last initial. ■

Consider the following contrapositive form of the generalized pigeonhole principle.

**Generalized Pigeonhole Principle (Contrapositive Form)**

For any function f from a finite set X with n elements to a finite set Y with m elements and for any positive integer k, if for each y ∈ Y, f⁻¹(y) has at most k elements, then X has at most km elements; in other words, n ≤ km.

You may find it natural to use the contrapositive form of the generalized pigeonhole principle in certain situations. For instance, the result of Example 9.4.5 can be explained as follows:

Suppose no 4 people out of the 85 had the same last initial. Then at most 3 would share any particular one. By the generalized pigeonhole principle (contrapositive form), this would imply that the total number of people is at most 3 · 26 = 78. But this contradicts the fact that there are 85 people in all. Hence at least 4 people share a last initial.

### Example 9.4.6 Using the Contrapositive Form of the Generalized Pigeonhole Principle

There are 42 students who are to share 12 computers. Each student uses exactly 1 computer, and no computer is used by more than 6 students. Show that at least 5 computers are used by 3 or more students.

**Page 589**

**Solution:**

a. **Using an Argument by Contradiction:** Suppose not. Suppose that 4 or fewer computers are used by 3 or more students. [A contradiction will be derived.] Then 8 or more computers are used by 2 or fewer students. Divide the set of computers into two subsets: C₁ and C₂. Into C₁ place 8 of the computers used by 2 or fewer students; into C₂ place the computers used by 3 or more students plus any remaining computers (to make a total of 4 computers in C₂). (See Figure 9.4.3.)

```
The Set of 12 Computers
        C₁                           C₂
Each of these computers      Some or all of these computers serve
serves at most 2 students.   3 or more students. Each computer
So the maximum number         serves at most 6 students. So the
served by these computers is  maximum number served by these
2 · 8 = 16.                  computers is 6 · 4 = 24.
```

Figure 9.4.3

Since at most 6 students are served by any one computer, by the contrapositive form of the generalized pigeonhole principle, the computers in set C₂ serve at most 6 ·4 = 24 students. Since at most 2 students are served by any one computer in C₁, by the generalized pigeonhole principle (contrapositive form), the computers in set C₁ serve at most 2· 8 = 16 students. Hence the total number of students served by the computers is 24 + 16 = 40. But this contradicts the fact that each of the 42 students is served by a computer. Therefore, the supposition is false: At least 5 computers are used by 3 or more students.

b. **Using a Direct Argument:** Let k be the number of computers used by 3 or more students. [We must show that k ≥ 5.] Because each computer is used by at most 6 students, these computers are used by at most 6k students (by the contrapositive form of the generalized pigeonhole principle). Each of the remaining 12 − k computers is used by at most 2 students. Hence, taken together, they are used by at most 2(12 − k) = 24 − 2k students (again, by the contrapositive form of the generalized pigeonhole principle). Thus the maximum number of students served by the computers is 6k + (24 − 2k) = 4k + 24. Because 42 students are served by the computers, 4k +24 ≥ 42. Solving for k gives that k ≥ 4.5, and since k is an integer, this implies that k ≥ 5 [as was to be shown]. ■

### Proof of the Pigeonhole Principle

The truth of the pigeonhole principle depends essentially on the sets involved being finite. Recall from Section 7.4 that a set is called finite if, and only if, it is the empty set or there is a one-to-one correspondence from {1, 2, . . . , n} to it, where n is a positive integer. In the first case the number of elements in the set is said to be 0, and in the second case it is said to be n. A set that is not finite is called infinite.

Thus any finite set is either empty or can be written in the form {x₁, x₂, . . . , xₙ} where n is a positive integer.

**Page 590**

**Theorem 9.4.1 The Pigeonhole Principle**

For any function f from a finite set X with n elements to a finite set Y with m elements, if n > m, then f is not one-to-one.

**Proof:**
Suppose f is any function from a finite set X with n elements to a finite set Y with m elements where n > m. Denote the elements of Y by y₁, y₂, . . . , yₘ. Recall that for each yᵢ in Y, the inverse image set f⁻¹(yᵢ) = {x ∈ X | f(x) = yᵢ}. Now consider the collection of all the inverse image sets for all the elements of Y:

f⁻¹(y₁), f⁻¹(y₂), . . . , f⁻¹(yₘ).

By definition of function, each element of X is sent by f to some element of Y. Hence each element of X is in one of the inverse image sets, and so the union of all these sets equals X. But also, by definition of function, no element of X is sent by f to more than one element of Y. Thus each element of X is in only one of the inverse image sets, and so the inverse image sets are mutually disjoint. By the addition rule, therefore,

N(X) = N(f⁻¹(y₁)) + N(f⁻¹(y₂)) + · · · + N(f⁻¹(yₘ)).    9.4.1

Now suppose that f is one-to-one [which is the opposite of what we want to prove]. Then each set f⁻¹(yᵢ) has at most one element, and so

N(f⁻¹(y₁)) + N(f⁻¹(y₂)) + · · · + N(f⁻¹(yₘ)) ≤ 1 + 1 + · · · + 1 = m    9.4.2
                                                     m terms

Putting equations (9.4.1) and (9.4.2) together gives that

n = N(X) ≤ m = N(Y).

This contradicts the fact that n > m, and so the supposition that f is one-to-one must be false. Hence f is not one-to-one [as was to be shown].

An important theorem that follows from the pigeonhole principle states that a function from one finite set to another finite set of the same size is one-to-one if, and only if, it is onto. As shown in Section 7.4, this result does not hold for infinite sets.

**Theorem 9.4.2 One-to-One and Onto for Finite Sets**

Let X and Y be finite sets with the same number of elements and suppose f is a function from X to Y. Then f is one-to-one if, and only if, f is onto.

**Proof:**
Suppose f is a function from X to Y, where X and Y are finite sets each with m elements. Let X = {x₁, x₂, . . . , xₘ} and Y = {y₁, y₂, . . . , yₘ}.

If f is one-to-one, then f is onto: Suppose f is one-to-one. Then f(x₁), f(x₂), . . . , f(xₘ) are all distinct. Consider the set S of all elements of Y that are not the image of any element of X.

[Content continues beyond page 590]