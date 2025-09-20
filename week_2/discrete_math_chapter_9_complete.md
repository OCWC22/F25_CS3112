# Chapter 9: Counting and Probability (Complete)

**Pages 545-563**

---

## -- Page 545 --

9.1

Introduction 517

## 9.1 Introduction

Imagine tossing two coins and observing whether 0, 1, or 2 heads are obtained. It would be natural to guess that each of these events occurs about one-third of the time, but in fact this is not the case. Table 9.1.1 below shows actual data obtained from tossing two quarters 50 times.

### Table 9.1.1 Experimental Data Obtained from Tossing Two Quarters 50 Times

| Event | Tally | Frequency (Number of times the event occurred) | Relative Frequency (Fraction of times the event occurred) |
|-------|-------|---------------------------------------------|------------------------------------------------------|
| 2 heads obtained | \|\|\|\| \|\|\|\| | | 11 | 22% |
| 1 head obtained | \|\|\|\| \|\|\|\| \|\|\|\| \|\|\|\| \|\| | 27 | 54% |
| 0 heads obtained | \|\|\|\| \|\|\|\| \|\| | 12 | 24% |

As you can see, the relative frequency of obtaining exactly 1 head was roughly twice as great as that of obtaining either 2 heads or 0 heads. It turns out that the mathematical theory of probability can be used to predict that a result like this will almost always occur.

To see how, call the two coins A and B, and suppose that each is perfectly balanced. Then each has an equal chance of coming up heads or tails, and when the two are tossed together, the four outcomes pictured in Figure 9.1.2 are all equally likely.

```
A   B           A   B           A   B           A   B
```

Figure 9.1.2 shows that there is a 1 in 4 chance of obtaining two heads and a 1 in 4 chance of obtaining no heads. The chance of obtaining one head, however, is 2 in 4 because either A could come up heads and B tails or B could come up heads and A tails. So if you repeatedly toss two balanced coins and record the number of heads, you should expect relative frequencies similar to those shown in Table 9.1.1.

To formalize this analysis and extend it to more complex situations, we introduce the notions of random process, sample space, event and probability. To say that a process is random means that when it takes place, one outcome from some set of outcomes is sure to occur, but it is impossible to predict with certainty which outcome that will be.

For instance, if an ordinary person performs the experiment of tossing an ordinary coin into the air and allowing it to fall flat on the ground, it can be predicted with certainty that the coin will land either heads up or tails up (so the set of outcomes can be denoted {heads, tails}), but it is not known for sure whether heads or tails will occur. We restricted this experiment to ordinary people because a skilled magician can toss a coin in a way that appears random but is not, and a physicist equipped with first-rate measuring devices may be able to analyze all the forces on the coin and correctly predict its landing position.

Just a few of many examples of random processes or experiments are choosing winners in state lotteries, selecting respondents in public opinion polls, and choosing subjects to receive treatments or serve as controls in medical experiments. The set of outcomes that can result from a random process or experiment is called a sample space.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 546 --

518 Chapter 9 Counting and Probability

• Definition

A sample space is the set of all possible outcomes of a random process or experiment.
An event is a subset of a sample space.

In case an experiment has finitely many outcomes and all outcomes are equally likely to occur, the probability of an event (set of outcomes) is just the ratio of the number of outcomes in the event to the total number of outcomes. Strictly speaking, this result can be deduced from a set of axioms for probability formulated in 1933 by the Russian mathematician A. N. Kolmogorov. In Section 9.8 we discuss the axioms and show how to derive their consequences formally. At present, we take a naïve approach to probability and simply state the result as a principle.

### Equally Likely Probability Formula

If S is a finite sample space in which all outcomes are equally likely and E is an event in S, then the probability of E, denoted P(E), is

```
P(E) = the number of outcomes in E
        --------------------------
        the total number of outcomes in S
```

• Notation

For any finite set A, N(A) denotes the number of elements in A.

With this notation, the equally likely probability formula becomes

```
P(E) = N(E)
        ----
        N(S)
```

### Example 9.1.1 Probabilities for a Deck of Cards

An ordinary deck of cards contains 52 cards divided into four suits. The red suits are diamonds (♦) and hearts (♥) and the black suits are clubs (♣) and spades (♠). Each suit contains 13 cards of the following denominations: 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king), and A (ace). The cards J, Q, and K are called face cards.

Mathematician Persi Diaconis, working with David Aldous in 1986 and Dave Bayer in 1992, showed that seven shuffles are needed to "thoroughly mix up" the cards in an ordinary deck. In 2000 mathematician Nick Trefethen, working with his father, Lloyd Trefethen, a mechanical engineer, used a somewhat different definition of "thoroughly mix up" to show that six shuffles will nearly always suffice.

Imagine that the cards in a deck have become—by some method—so thoroughly mixed up that if you spread them out face down and pick one at random, you are as likely to get any one card as any other.

a. What is the sample space of outcomes?
b. What is the event that the chosen card is a black face card?
c. What is the probability that the chosen card is a black face card?

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 547 --

9.1

Introduction 519

**Solution**

a. The outcomes in the sample space S are the 52 cards in the deck.

b. Let E be the event that a black face card is chosen. The outcomes in E are the jack, queen, and king of clubs and the jack, queen, and king of spades. Symbolically,
E = {J♣, Q♣, K♣, J♠, Q♠, K♠}.

c. By part (b), N(E) = 6, and according to the description of the situation, all 52 outcomes in the sample space are equally likely. Therefore, by the equally likely probability formula, the probability that the chosen card is a black face card is

```
P(E) = N(E)/N(S) = 6/52 ≈ 11.5%
```

### Example 9.1.2 Rolling a Pair of Dice

A die is one of a pair of dice. It is a cube with six sides, each containing from one to six dots, called pips. Suppose a blue die and a gray die are rolled together, and the numbers of dots that occur face up on each are recorded. The possible outcomes can be listed as follows, where in each case the die on the left is blue and the one on the right is gray.

A more compact notation identifies, say,
```
 with the notation 11,
 with 12,
 with 13,
 and so forth.
```

a. Use the compact notation to write the sample space S of possible outcomes.
b. Use set notation to write the event E that the numbers showing face up have a sum of 6 and find the probability of this event.

**Solution**

a. S = {11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66}.

b. E = {15, 24, 33, 42, 51}.
The probability that the sum of the numbers is 6 = P(E) = N(E)/N(S) = 5/36.

The next example is called the Monty Hall problem after the host of an old game show, "Let's Make A Deal." When it was originally publicized in a newspaper column and on a radio show, it created tremendous controversy. Many highly educated people, even some with Ph.D.'s, submitted incorrect solutions or argued vociferously against the correct solution. Before you read the answer, think about what your own response to the situation would be.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 548 --

520 Chapter 9 Counting and Probability

### Example 9.1.3 The Monty Hall Problem

There are three doors on the set for a game show. Let's call them A, B, and C. If you pick the right door you win the prize. You pick door A. The host of the show, Monty Hall, then opens one of the other doors and reveals that there is no prize behind it. Keeping the remaining two doors closed, he asks you whether you want to switch your choice to the other closed door or stay with your original choice of door A. What should you do if you want to maximize your chance of winning the prize: stay with door A or switch—or would the likelihood of winning be the same either way?

```
Case 1     Case 2     Case 3
   B           C           B
   C           B           C
   B           C           B
```

**Solution**

At the point just before the host opens one of the closed doors, there is no information about the location of the prize. Thus there are three equally likely possibilities for what lies behind the doors: (Case 1) the prize is behind A (i.e., it is not behind either B or C), (Case 2) the prize is behind B; (Case 3) the prize is behind C.

Since there is no prize behind the door the host opens, in Case 1 the host could open either door and you would win by staying with your original choice: door A. In Case 2 the host must open door C, and so you would win by switching to door B. In Case 3 the host must open door B, and so you would win by switching to door C. Thus, in two of the three equally likely cases, you would win by switching from A to the other closed door. In only one of the three equally likely cases would you win by staying with your original choice. Therefore, you should switch.

A reality note: The analysis used for this solution applies only if the host always opens one of the closed doors and offers the contestant the choice of staying with the original choice or switching. In the original show, Monty Hall made this offer only occasionally—most often when he knew the contestant had already chosen the correct door.

Many of the fundamental principles of probability were formulated in the mid-1600s in an exchange of letters between Pierre de Fermat and Blaise Pascal in response to questions posed by a French nobleman interested in games of chance. In 1812, Pierre-Simon Laplace published the first general mathematical treatise on the subject and extended the range of applications to a variety of scientific and practical problems.

---

## Counting the Elements of a List

Some counting problems are as simple as counting the elements of a list. For instance, how many integers are there from 5 through 12? To answer this question, imagine going along the list of integers from 5 to 12, counting each in turn.

```
list:   5   6   7   8   9  10  11  12
count: (1) (2) (3) (4) (5) (6) (7) (8)
```

So the answer is 8.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 549 --

9.1

Introduction 521

More generally, if m and n are integers and m ≤ n, how many integers are there from m through n? To answer this question, note that n = m + (n - m), where n - m ≥ 0 [since n ≥ m]. Note also that the element m + 0 is the first element of the list, the element m + 1 is the second element, the element m + 2 is the third, and so forth. In general, the element m + i is the (i + 1)st element of the list.

```
list:   m(= m + 0)  m + 1  m + 2  ...  n (= m + (n - m))
count:    (1)        (2)     (3)    ...    (n - m) + 1
```

And so the number of elements in the list is n - m + 1.

This general result is important enough to be restated as a theorem, the formal proof of which uses mathematical induction. (See exercise 28 at the end of this section.) The heart of the proof is the observation that if the list m, m + 1, . . . , k has k - m + 1 numbers, then the list m, m + 1, . . . , k, k + 1 has (k - m + 1) + 1 = (k + 1) - m + 1 numbers.

### Theorem 9.1.1 The Number of Elements in a List

If m and n are integers and m ≤ n, then there are n - m + 1 integers from m to n inclusive.

### Example 9.1.4 Counting the Elements of a Sublist

a. How many three-digit integers (integers from 100 to 999 inclusive) are divisible by 5?
b. What is the probability that a randomly chosen three-digit integer is divisible by 5?

**Solution**

a. Imagine writing the three-digit integers in a row, noting those that are multiples of 5 and drawing arrows between each such integer and its corresponding multiple of 5.

```
100 101 102 103 104 105 106 107 108 109 110 · · · 994 995 996 997 998 999
 (      (      (      (                     (
 5·20   5·21   5·22   5·23                  5·199
```

From the sketch it is clear that there are as many three-digit integers that are multiples of 5 as there are integers from 20 to 199 inclusive. By Theorem 9.1.1, there are 199 - 20 + 1, or 180, such integers. Hence there are 180 three-digit integers that are divisible by 5.

b. By Theorem 9.1.1 the total number of integers from 100 through 999 is 999 - 100 + 1 = 900. By part (a), 180 of these are divisible by 5. Hence the probability that a randomly chosen three-digit integer is divisible by 5 is 180/900 = 1/5.

### Example 9.1.5 Application: Counting Elements of a One-Dimensional Array

Analysis of many computer algorithms requires skill at counting the elements of a one-dimensional array. Let A[1], A[2], . . . , A[n] be a one-dimensional array, where n is a positive integer.

a. Suppose the array is cut at a middle value A[m] so that two subarrays are formed:
   (1) A[1], A[2], . . . , A[m] and
   (2) A[m + 1], A[m + 2], . . . , A[n].

   How many elements does each subarray have?
b. What is the probability that a randomly chosen element of the array has an even subscript
   (i) if n is even?
   (ii) if n is odd?

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 550 --

522 Chapter 9 Counting and Probability

**Solution**

a. Array (1) has the same number of elements as the list of integers from 1 through m. So by Theorem 9.1.1, it has m, or m - 1 + 1, elements. Array (2) has the same number of elements as the list of integers from m + 1 through n. So by Theorem 9.1.1, it has n - m, or n - (m + 1) + 1, elements.

b. (i) If n is even, each even subscript starting with 2 and ending with n can be matched up with an integer from 1 to n/2.

```
 1   2   3   4   5   6   7   8   9  10 · · ·  n
(   (   (   (   (   (   (   (   (   (
2·1 2·1 2·2 2·2 2·3 2·3 2·4 2·4 2·5 2·5 · · · 2·n/2
```

So there are n/2 array elements with even subscripts. Since the entire array has n elements, the probability that a randomly chosen element has an even subscript is (n/2)/n = 1/2.

(ii) If n is odd, then the greatest even subscript of the array is n - 1. So there are as many even subscripts between 1 and n as there are from 2 through n - 1. Then the reasoning of (i) can be used to conclude that there are (n - 1)/2 array elements with even subscripts.

```
 1   2   3   4   5   6 ··· n-1   n
(   (   (   (   (   (     (
2·1 2·1 2·2 2·2 2·3 2·3 ··· 2·(n-1)/2
```

Since the entire array has n elements, the probability that a randomly chosen element has an even subscript is [(n - 1)/2]/n = (n - 1)/(2n). Observe that as n gets larger and larger, this probability gets closer and closer to 1/2.

Note that the answers to (i) and (ii) can be combined using the floor notation. By Theorem 4.5.2, the number of array elements with even subscripts is ⌊n/2⌋, so the probability that a randomly chosen element has an even subscript is ⌊n/2⌋/n.

---

## Test Yourself

Answers to Test Yourself questions are located at the end of each section.

1. A sample space of a random process or experiment is _____.
2. An event in a sample space is _____.
3. To compute the probability of an event using the equally likely probability formula, you take the ratio of the _____ to the _____.
4. If m ≤ n, the number of integers from m to n inclusive is _____.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 551 --

9.1

Introduction 523

## Exercise Set 9.1*

1. Toss two coins 30 times and make a table showing the relative frequencies of 0, 1, and 2 heads. How do your values compare with those shown in Table 9.1.1?

2. In the example of tossing two quarters, what is the probability that at least one head is obtained? that coin A is a head? that coins A and B are either both heads or both tails?

In 3–6 use the sample space given in Example 9.1.1. Write each event as a set, and compute its probability.

3. The event that the chosen card is red and is not a face card.
4. The event that the chosen card is black and has an even number on it.
5. The event that the denomination of the chosen card is at least 10 (counting aces high).
6. The event that the denomination of the chosen card is at most 4 (counting aces high).

In 7–10, use the sample space given in Example 9.1.2. Write each of the following events as a set and compute its probability.

7. The event that the sum of the numbers showing face up is 8.
8. The event that the numbers showing face up are the same.
9. The event that the sum of the numbers showing face up is at most 6.
10. The event that the sum of the numbers showing face up is at least 9.

11. Suppose that a coin is tossed three times and the side showing face up on each toss is noted. Suppose also that on each toss heads and tails are equally likely. Let HHT indicate the outcome heads on the first two tosses and tails on the third, THT the outcome tails on the first and third tosses and heads on the second, and so forth.

a. List the eight elements in the sample space whose outcomes are all the possible head–tail sequences obtained in the three tosses.
b. Write each of the following events as a set and find its probability:
   (i) The event that exactly one toss results in a head.
   (ii) The event that at least two tosses result in a head.
   (iii) The event that no head is obtained.

12. Suppose that each child born is equally likely to be a boy or a girl. Consider a family with exactly three children. Let BBG indicate that the first two children born are boys and the third child is a girl, let GBG indicate that the first and third children born are girls and the second is a boy, and so forth.

a. List the eight elements in the sample space whose outcomes are all possible genders of the three children.
b. Write each of the following events as a set and find its probability:
   (i) The event that exactly one child is a girl.
   (ii) The event that at least two children are girls.
   (iii) The event that no child is a girl.

13. Suppose that on a true/false exam you have no idea at all about the answers to three questions. You choose answers randomly and therefore have a 50–50 chance of being correct on any one question. Let CCW indicate that you were correct on the first two questions and wrong on the third, let WCW indicate that you were wrong on the first and third questions and correct on the second, and so forth.

a. List the elements in the sample space whose outcomes are all possible sequences of correct and incorrect responses on your part.
b. Write each of the following events as a set and find its probability:
   (i) The event that exactly one answer is correct.
   (ii) The event that at least two answers are correct.
   (iii) The event that no answer is correct.

14. Three people have been exposed to a certain illness. Once exposed, a person has a 50–50 chance of actually becoming ill.

a. What is the probability that exactly one of the people becomes ill?
b. What is the probability that at least two of the people become ill?
c. What is the probability that none of the three people becomes ill?

15. When discussing counting and probability, we often consider situations that may appear frivolous or of little practical value, such as tossing coins, choosing cards, or rolling dice. The reason is that these relatively simple examples serve as models for a wide variety of more complex situations in the real world. In light of this remark, comment on the relationship between your answer to exercise 11 and your answers to exercises 12–14.

16. Two faces of a six-sided die are painted red, two are painted blue, and two are painted yellow. The die is rolled three times, and the colors that appear face up on the first, second, and third rolls are recorded.

a. Let BBR denote the outcome where the color appearing face up on the first and second rolls is blue and the color appearing face up on the third roll is red. Because there are as many faces of one color as of any other, the outcomes of this experiment are equally likely. List all 27 possible outcomes.
b. Consider the event that all three rolls produce different colors. One outcome in this event is RBY and another RYB. List all outcomes in the event. What is the probability of the event?

*For exercises with blue numbers or letters, solutions are given in Appendix B. The symbol H indicates that only a hint or a partial solution is given. The symbol ✶ signals that an exercise is more challenging than usual.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 552 --

524 Chapter 9 Counting and Probability

c. Consider the event that two of the colors that appear face up are the same. One outcome in this event is RRB and another is RBR. List all outcomes in the event. What is the probability of the event?

17. Consider the situation described in exercise 16.

a. Find the probability of the event that exactly one of the colors that appears face up is red.
b. Find the probability of the event that at least one of the colors that appears face up is red.

18. An urn contains two blue balls (denoted B1 and B2) and one white ball (denoted W). One ball is drawn, its color is recorded, and it is replaced in the urn. Then another ball is drawn, and its color is recorded.

a. Let B1W denote the outcome that the first ball drawn is B1 and the second ball drawn is W. Because the first ball is replaced before the second ball is drawn, the outcomes of the experiment are equally likely. List all nine possible outcomes of the experiment.
b. Consider the event that the two balls that are drawn are both blue. List all outcomes in the event. What is the probability of the event?
c. Consider the event that the two balls that are drawn are of different colors. List all outcomes in the event. What is the probability of the event?

19. An urn contains two blue balls (denoted B1 and B2) and three white balls (denoted W1, W2, and W3). One ball is drawn, its color is recorded, and it is replaced in the urn. Then another ball is drawn and its color is recorded.

a. Let B1W2 denote the outcome that the first ball drawn is B1 and the second ball drawn is W2. Because the first ball is replaced before the second ball is drawn, the outcomes of the experiment are equally likely. List all 25 possible outcomes of the experiment.
b. Consider the event that the first ball that is drawn is blue. List all outcomes in the event. What is the probability of the event?
c. Consider the event that only white balls are drawn. List all outcomes in the event. What is the probability of the event?

20. Refer to Example 9.1.3. Suppose you are appearing on a game show with a prize behind one of five closed doors: A, B, C, D, and E. If you pick the right door, you win the prize. You pick door A. The game show host then opens one of the other doors and reveals that there is no prize behind it. Then the host gives you the option of staying with your original choice of door A or switching to one of the other doors that is still closed.

a. If you stick with your original choice, what is the probability that you will win the prize?
b. If you switch to another door, what is the probability that you will win the prize?

21. a. How many positive two-digit integers are multiples of 3?
b. What is the probability that a randomly chosen positive two-digit integer is a multiple of 3?
c. What is the probability that a randomly chosen positive two-digit integer is a multiple of 4?

22. a. How many positive three-digit integers are multiples of 6?
b. What is the probability that a randomly chosen positive three-digit integer is a multiple of 6?
c. What is the probability that a randomly chosen positive three-digit integer is a multiple of 7?

23. Suppose A[1], A[2], A[3], . . . , A[n] is a one-dimensional array and n ≥ 50.

a. How many elements are in the array?
b. How many elements are in the subarray A[4], A[5], . . . , A[39]?
c. If 3 ≤ m ≤ n, what is the probability that a randomly chosen array element is in the subarray A[3], A[4], . . . , A[m]?
d. What is the probability that a randomly chosen array element is in the subarray shown below if n = 39?
   A[⌊n/2⌋], A[⌊n/2⌋ + 1], . . . , A[n]

24. Suppose A[1], A[2], . . . , A[n] is a one-dimensional array and n ≥ 2. Consider the subarray A[1], A[2], . . . , A[⌊n/2⌋].

a. How many elements are in the subarray (i) if n is even? and (ii) if n is odd?
b. What is the probability that a randomly chosen array element is in the subarray (i) if n is even? and (ii) if n is odd?

25. Suppose A[1], A[2], . . . , A[n] is a one-dimensional array and n ≥ 2. Consider the subarray A[⌊n/2⌋], A[⌊n/2⌋ + 1], . . . , A[n].

a. How many elements are in the subarray (i) if n is even? and (ii) if n is odd?
b. What is the probability that a randomly chosen array element is in the subarray (i) if n is even? and (ii) if n is odd?

26. What is the 27th element in the one-dimensional array A[42], A[43], . . . , A[100]?

27. What is the 62nd element in the one-dimensional array B[29], B[30], . . . , B[100]?

28. If the largest of 56 consecutive integers is 279, what is the smallest?

29. If the largest of 87 consecutive integers is 326, what is the smallest?

30. How many even integers are between 1 and 1,001?

31. How many integers that are multiples of 3 are between 1 and 1,001?

32. A certain non-leap year has 365 days, and January 1 occurs on a Monday.

a. How many Sundays are in the year?
b. How many Mondays are in the year?

✶ 33. Prove Theorem 9.1.1. (Let m be any integer and prove the theorem by mathematical induction on n.)

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 553 --

9.2

Possibility Trees and the Multiplication Rule

525

## Answers for Test Yourself

1. the set of all outcomes of the random process or experiment
2. a subset of the sample space
3. number of outcomes in the event; total number of outcomes
4. n - m + 1

---

## 9.2 Possibility Trees and the Multiplication Rule

Don't believe anything unless you have thought it through for yourself.
— Anna Pell Wheeler, 1883–1966

A tree structure is a useful tool for keeping systematic track of all possibilities in situations in which events happen in order. The following example shows how to use such a structure to count the number of different outcomes of a tournament.

### Example 9.2.1 Possibilities for Tournament Play

Teams A and B are to play each other repeatedly until one wins two games in a row or a total of three games. One way in which this tournament can be played is for A to win the first game, B to win the second, and A to win the third and fourth games. Denote this by writing A–B–A–A.

a. How many ways can the tournament be played?
b. Assuming that all the ways of playing the tournament are equally likely, what is the probability that five games are needed to determine the tournament winner?

**Solution**

a. The possible ways for the tournament to be played are represented by the distinct paths from "root" (the start) to "leaf" (a terminal point) in the tree shown sideways in Figure 9.2.1. The label on each branching point indicates the winner of the game. The notations in parentheses indicate the winner of the tournament.

```
Winner of game 1
Start
A (A wins)
Winner of game 2
A (A wins)
Winner of game 3
A (A wins)
Winner of game 4
A (A wins)
B (B wins)
B (B wins)
B (B wins)
B (B wins)
```

Figure 9.2.1 The Outcomes of a Tournament

The fact that there are ten paths from the root of the tree to its leaves shows that there are ten possible ways for the tournament to be played. They are (moving from the top down): A–A, A–B–A–A, A–B–A–B–A, A–B–A–B–B, A–B–B, B–A–A, B–A–B–A–A, B–A–B–A–B, B–A–B–B, and B–B. In five cases A wins, and in the other five B wins. The least number of games that must be played to determine a winner is two, and the most that will need to be played is five.

---

## -- Page 554 --

526 Chapter 9 Counting and Probability

b. Since all the possible ways of playing the tournament listed in part (a) are assumed to be equally likely, and the listing shows that five games are needed in four different cases (A–B–A–B–A, A–B–A–B–B, B–A–B–A–B, and B–A–B–A–A), the probability that five games are needed is 4/10 = 2/5 = 40%.

The Multiplication Rule
Consider the following example. Suppose a computer installation has four input/output units (A, B, C, and D) and three central processing units (X, Y, and Z). Any input/output unit can be paired with any central processing unit. How many ways are there to pair an input/output unit with a central processing unit?

To answer this question, imagine the pairing of the two types of units as a two-step operation:
Step 1: Choose the input/output unit.
Step 2: Choose the central processing unit.

The possible outcomes of this operation are illustrated in the possibility tree of Figure 9.2.2.

```
Step 1: Choose the        Step 2: Choose the
input/output unit.        central processing unit.
                          X
                        A   Y
                          Z
                          X
                        B   Y
                          Z
Start                    X
                        C   Y
                          Z
                          X
                        D   Y
                          Z
```

Figure 9.2.2 Pairing Objects Using a Possibility Tree

The topmost path from "root" to "leaf" indicates that input/output unit A is to be paired with central processing unit X. The next lower branch indicates that input/output unit A is to be paired with central processing unit Y. And so forth.

Thus the total number of ways to pair the two types of units is the same as the number of branches of the tree, which is
3 + 3 + 3 + 3 = 4 · 3 = 12.

The idea behind this example can be used to prove the following rule. A formal proof uses mathematical induction and is left to the exercises.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 555 --

9.2

Possibility Trees and the Multiplication Rule

527

### Theorem 9.2.1 The Multiplication Rule

If an operation consists of k steps and
- the first step can be performed in n₁ ways,
- the second step can be performed in n₂ ways [regardless of how the first step was performed],
- ...
- the kth step can be performed in nₖ ways [regardless of how the preceding steps were performed],

then the entire operation can be performed in n₁n₂ · · · nₖ ways.

To apply the multiplication rule, think of the objects you are trying to count as the output of a multistep operation. The possible ways to perform a step may depend on how preceding steps were performed, but the number of ways to perform each step must be constant regardless of the action taken in prior steps.

### Example 9.2.2 Number of Personal Identification Numbers (PINs)

A typical PIN (personal identification number) is a sequence of any four symbols chosen from the 26 letters in the alphabet and the ten digits, with repetition allowed. How many different PINs are possible?

**Solution**

Typical PINs are CARE, 3387, B32B, and so forth. You can think of forming a PIN as a four-step operation to fill in each of the four symbols in sequence.

```
                          36
                         ch
                          oic
                        1   es
                           36
                           ch
                       3  oic
                         s
                          36
                         ch
                       2 oice
                          s
                          36
                       4  cho
                         ice
                          s

Pool of available
symbols: A, B, C, D, E, F, G,
H, I, J, K, L, M, N, O, P, Q, R,
S, T, U, V, W, X, Y, Z,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

Step 1: Choose the first symbol.
Step 2: Choose the second symbol.
Step 3: Choose the third symbol.
Step 4: Choose the fourth symbol.
```

There is a fixed number of ways to perform each step, namely 36, regardless of how preceding steps were performed. And so, by the multiplication rule, there are
36·36·36·36 = 36⁴ = 1,679,616 PINs in all.

Another way to look at the PINs of Example 9.2.2 is as ordered 4-tuples. For example, you can think of the PIN M2ZM as the ordered 4-tuple (M, 2, Z, M). Therefore, the total number of PINs is the same as the total number of ordered 4-tuples whose elements are either letters of the alphabet or digits. One of the most important uses of the multiplication rule is to derive a general formula for the number of elements in any Cartesian product of a finite number of finite sets. In Example 9.2.3, this is done for a Cartesian product of four sets.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 556 --

528 Chapter 9 Counting and Probability

### Example 9.2.3 The Number of Elements in a Cartesian Product

Suppose A₁, A₂, A₃, and A₄ are sets with n₁, n₂, n₃, and n₄ elements, respectively. Show that the set A₁ × A₂ × A₃ × A₄ has n₁n₂n₃n₄ elements.

**Solution**

Each element in A₁ × A₂ × A₃ × A₄ is an ordered 4-tuple of the form (a₁, a₂, a₃, a₄), where a₁ ∈ A₁, a₂ ∈ A₂, a₃ ∈ A₃, and a₄ ∈ A₄. Imagine the process of constructing these ordered tuples as a four-step operation:

Step 1: Choose the first element of the 4-tuple.
Step 2: Choose the second element of the 4-tuple.
Step 3: Choose the third element of the 4-tuple.
Step 4: Choose the fourth element of the 4-tuple.

There are n₁ ways to perform step 1, n₂ ways to perform step 2, n₃ ways to perform step 3, and n₄ ways to perform step 4. Hence, by the multiplication rule, there are n₁n₂n₃n₄ ways to perform the entire operation. Therefore, there are n₁n₂n₃n₄ distinct 4-tuples in A₁ × A₂ × A₃ × A₄.

### Example 9.2.4 Number of PINs without Repetition

In Example 9.2.2 we formed PINs using four symbols, either letters of the alphabet or digits, and supposing that letters could be repeated. Now suppose that repetition is not allowed.

a. How many different PINs are there?
b. If all PINs are equally likely, what is the probability that a PIN chosen at random contains no repeated symbol?

**Solution**
a. Again think of forming a PIN as a four-step operation: Choose the first symbol, then the second, then the third, and then the fourth. There are 36 ways to choose the first symbol, 35 ways to choose the second (since the first symbol cannot be used again), 34 ways to choose the third (since the first two symbols cannot be reused), and 33 ways to choose the fourth (since the first three symbols cannot be reused). Thus, the multiplication rule can be applied to conclude that there are 36·35·34·33 = 1,413,720 different PINs with no repeated symbol.

b. By part (a) there are 1,413,720 PINs with no repeated symbol, and by Example 9.2.2 there are 1,679,616 PINs in all. Thus the probability that a PIN chosen at random contains no repeated symbol is 1,413,720/1,679,616 ≈ .8417. In other words, approximately 84% of PINs have no repeated symbol.

Any circuit with two input signals P and Q has an input/output table consisting of four rows corresponding to the four possible assignments of values to P and Q: 11, 10, 01, and 00. The next example shows that there are only 16 distinct ways in which such a circuit can function.

### Example 9.2.5 Number of Input/Output Tables for a Circuit with Two Input Signals

Consider the set of all circuits with two input signals P and Q. For each such circuit an input/output table can be constructed, but, as shown in Section 2.4, two such input/output tables may have the same values. How many distinct input/output tables can be constructed for circuits with input/output signals P and Q?

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 557 --

9.2

Possibility Trees and the Multiplication Rule

529

**Solution**

Fix the order of the input values for P and Q. Then two input/output tables are distinct if their output values differ in at least one row. For example, the input/output tables shown below are distinct, because their output values differ in the first row.

```
P   Q   Output          P   Q   Output
1   1      1            1   1      0
1   0      0            1   0      0
0   1      1            0   1      1
0   0      0            0   0      0
```

For a fixed ordering of input values, you can obtain a complete input/output table by filling in the entries in the output column. You can think of this as a four-step operation:

Step 1: Fill in the output value for the first row.
Step 2: Fill in the output value for the second row.
Step 3: Fill in the output value for the third row.
Step 4: Fill in the output value for the fourth row.

Each step can be performed in exactly two ways: either a 1 or a 0 can be filled in. Hence, by the multiplication rule, there are
2·2·2·2 = 16
ways to perform the entire operation. It follows that there are 2⁴ = 16 distinct input/output tables for a circuit with two input signals P and Q. This means that such a circuit can function in only 16 distinct ways.

Recall from Section 5.9 that if S is a nonempty, finite set of characters, then a string over S is a finite sequence of elements of S. The number of characters in a string is called the length of the string. The null string over S is the "string" with no characters. It is usually denoted ε and is said to have length 0.

Observe that in Examples 9.2.2 and 9.2.4, the set of all PINs of length 4 is the same as the set of all strings of length 4 over the set
S = {x | x is a letter of the alphabet or x is a digit}.

Also observe that another way to think of Example 9.2.5 is to realize that there are as many input/output tables for a circuit with two input signals as there are bit strings of length 4 (written vertically) that can be used to fill in the output values. As another example, here is a listing of all bit strings of length 3:
000, 001, 010, 100, 011, 101, 110, 111.

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

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 558 --

530 Chapter 9 Counting and Probability

**Solution**

The outer loop is iterated four times, and during each iteration of the outer loop, there are three iterations of the inner loop. Hence by the multiplication rule, the total number of iterations of the inner loop is 4·3 = 12. This is illustrated by the trace table below.

```
i   j
1   1 →
    2
    3 →
2   1 →
    2
    3 →
3   1 →
    2
    3 →
4   1 →
    2
    3 →
        = 12
```

### When the Multiplication Rule Is Difficult or Impossible to Apply

Consider the following problem:
Three officers—a president, a treasurer, and a secretary—are to be chosen from among four people: Ann, Bob, Cyd, and Dan. Suppose that, for various reasons, Ann cannot be president and either Cyd or Dan must be secretary. How many ways can the officers be chosen?

It is natural to try to solve this problem using the multiplication rule. A person might answer as follows:
There are three choices for president (all except Ann), three choices for treasurer (all except the one chosen as president), and two choices for secretary (Cyd or Dan). Therefore, by the multiplication rule, there are 3·3·2 = 18 choices in all.

Unfortunately, this analysis is incorrect. The number of ways to choose the secretary varies depending on who is chosen for president and treasurer. For instance, if Bob is chosen for president and Ann for treasurer, then there are two choices for secretary: Cyd and Dan. But if Bob is chosen for president and Cyd for treasurer, then there is just one choice for secretary: Dan. The clearest way to see all the possible choices is to construct the possibility tree, as is shown in Figure 9.2.3.

```
Step 1: Choose    Step 2: Choose    Step 3: Choose
the president.     the treasurer.     the secretary.
                   Cyd
                 Ann   Dan
                   Bob
                   Cyd
                 Bob   Dan
                   Dan
Start
                   Cyd
                 Dan   Ann
                   Bob
                   Cyd
                 Ann   Dan
                   Bob
                   Dan
```

From the tree it is easy to see that there are only eight ways to choose a president, treasurer, and secretary so as to satisfy the given conditions.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 559 --

9.2

Possibility Trees and the Multiplication Rule

531

Another way to solve this problem is somewhat surprising. It turns out that the steps can be reordered in a slightly different way so that the number of ways to perform each step is constant regardless of the way previous steps were performed.

### Example 9.2.7 A More Subtle Use of the Multiplication Rule

Reorder the steps for choosing the officers in the previous example so that the total number of ways to choose officers can be computed using the multiplication rule.

**Solution**
Step 1: Choose the secretary.
Step 2: Choose the president.
Step 3: Choose the treasurer.

There are exactly two ways to perform step 1 (either Cyd or Dan may be chosen), two ways to perform step 2 (neither Ann nor the person chosen in step 1 may be chosen but either of the other two may), and two ways to perform step 3 (either of the two people not chosen as secretary or president may be chosen as treasurer). Thus, by the multiplication rule, the total number of ways to choose officers is 2·2·2 = 8. A possibility tree illustrating this sequence of choices is shown in Figure 9.2.4. Note how balanced this tree is compared with the one in Figure 9.2.3.

```
Step 1: Choose    Step 2: Choose    Step 3: Choose
the secretary.     the president.     the treasurer.
                   Ann
                 Bob     Cyd
                   Dan
                 Dan     Ann
                   Bob
Start
                   Ann
                 Cyd     Bob
                   Dan
                 Cyd     Ann
                   Bob
```

### Permutations

A permutation of a set of objects is an ordering of the objects in a row. For example, the set of elements a, b, and c has six permutations.
abc, acb, cba, bac, bca, cab

In general, given a set of n objects, how many permutations does the set have? Imagine forming a permutation as an n-step operation:

Step 1: Choose an element to write first.
Step 2: Choose an element to write second.
...
Step n: Choose an element to write nth.

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 560 --

532 Chapter 9 Counting and Probability

Any element of the set can be chosen in step 1, so there are n ways to perform step 1. Any element except that chosen in step 1 can be chosen in step 2, so there are n - 1 ways to perform step 2. In general, the number of ways to perform each successive step is one less than the number of ways to perform the preceding step. At the point when the nth element is chosen, there is only one element left, so there is only one way to perform step n. Hence, by the multiplication rule, there are
n(n - 1)(n - 2) · · · 2·1 = n!
ways to perform the entire operation. In other words, there are n! permutations of a set of n elements. This reasoning is summarized in the following theorem. A formal proof uses mathematical induction and is left as an exercise.

### Theorem 9.2.2

For any integer n with n ≥ 1, the number of permutations of a set with n elements is n!.

### Example 9.2.8 Permutations of the Letters in a Word

a. How many ways can the letters in the word COMPUTER be arranged in a row?
b. How many ways can the letters in the word COMPUTER be arranged if the letters CO must remain next to each other (in order) as a unit?
c. If letters of the word COMPUTER are randomly arranged in a row, what is the probability that the letters CO remain next to each other (in order) as a unit?

**Solution**
a. All the eight letters in the word COMPUTER are distinct, so the number of ways in which we can arrange the letters equals the number of permutations of a set of eight elements. This equals 8! = 40,320.

b. If the letter group CO is treated as a unit, then there are effectively only seven objects that are to be arranged in a row.

```
CO   M   P   U   T   E   R
```

Hence there are as many ways to write the letters as there are permutations of a set of seven elements, namely 7! = 5,040.

c. When the letters are arranged randomly in a row, the total number of arrangements is 40,320 by part (a), and the number of arrangements with the letters CO next to each other (in order) as a unit is 5,040. Thus the probability is 5,040/40,320 = 1/8 = 12.5%.

### Example 9.2.9 Permutations of Objects Around a Circle

At a meeting of diplomats, the six participants are to be seated around a circular table. Since the table has no ends to confer particular status, it doesn't matter who sits in which chair. But it does matter how the diplomats are seated relative to each other. In other words, two seatings are considered the same if one is a rotation of the other. How many different ways can the diplomats be seated?

Copyright 2010 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

---

## -- Page 561 --

9.2

Possibility Trees and the Multiplication Rule

533

**Solution**

Call the diplomats by the letters A, B, C, D, E, and F. Since only relative position matters, you can start with any diplomat (say A), place that diplomat anywhere (say in the top seat of the diagram shown in Figure 9.2.5), and then consider all arrangements of the other diplomats around that one. B through F can be arranged in the seats around diplomat A in all possible orders. So there are 5! = 120 ways to seat the group.

```
        A
    Five other
    diplomats
    to be seated:
    B, C, D, E, F
```

### Permutations of Selected Elements

Given the set {a, b, c}, there are six ways to select two letters from the set and write them in order.
ab, ac, ba, bc, ca, cb

Each such ordering of two elements of {a, b, c} is called a 2-permutation of {a, b, c}.

### Definition

An r-permutation of a set of n elements is an ordered selection of r elements taken from the set of n elements. The number of r-permutations of a set of n elements is denoted P(n, r).

### Theorem 9.2.3

If n and r are integers and 1 ≤ r ≤ n, then the number of r-permutations of a set of n elements is given by the formula

P(n, r) = n(n - 1)(n - 2) · · · (n - r + 1)    [first version]

or, equivalently,

P(n, r) = n!/(n - r)!    [second version].

---

## 9.3 Counting Elements of Disjoint Sets: The Addition Rule

**Pages 568-582**

The whole of science is nothing more than a refinement of everyday thinking.
— Albert Einstein, 1879–1955

In the last section we discussed counting problems that can be solved using possibility trees. In this section we look at counting problems that can be solved by counting the number of elements in the union of two sets, the difference of two sets, or the intersection of two sets.

The basic rule underlying the calculation of the number of elements in a union or difference or intersection is the addition rule. This rule states that the number of elements in a union of mutually disjoint finite sets equals the sum of the number of elements in each of the component sets.

### Theorem 9.3.1 The Addition Rule

Suppose a finite set A equals the union of k distinct mutually disjoint subsets A₁, A₂, ..., Aₖ. Then
N(A) = N(A₁) + N(A₂) + · · · + N(Aₖ).

A formal proof of this theorem uses mathematical induction and is left to the exercises.

### Example 9.3.1 Counting Passwords with Three or Fewer Letters

A computer access password consists of from one to three letters chosen from the 26 in the alphabet with repetitions allowed. How many different passwords are possible?

**Solution**

The set of all passwords can be partitioned into subsets consisting of those of length 1, those of length 2, and those of length 3 as shown in Figure 9.3.1.

```
Set of All Passwords of Length ≤ 3

passwords
of length 1

passwords
of length 2

passwords
of length 3
```

By the addition rule, the total number of passwords equals the number of passwords of length 1, plus the number of passwords of length 2, plus the number of passwords of length 3. Now the
- number of passwords of length 1 = 26 because there are 26 letters in the alphabet
- number of passwords of length 2 = 26² because forming such a word can be thought of as a two-step process in which there are 26 ways to perform each step
- number of passwords of length 3 = 26³ because forming such a word can be thought of as a three-step process in which there are 26 ways to perform each step.

Hence the total number of passwords = 26 + 26² + 26³ = 18,278.

### Example 9.3.2 Counting the Number of Integers Divisible by 5

How many three-digit integers (integers from 100 to 999 inclusive) are divisible by 5?

**Solution**

One solution to this problem was discussed in Example 9.1.4. Another approach uses the addition rule. Integers that are divisible by 5 end either in 5 or in 0. Thus the set of all three-digit integers that are divisible by 5 can be split into two mutually disjoint subsets A₁ and A₂ as shown in Figure 9.3.2.

```
Three-Digit Integers That Are Divisible by 5

three-digit integers
that end in 0

three-digit integers
that end in 5

A₁
A₂

A₁ ∪ A₂ = the set of all three-digit integers
that are divisible by 5
A₁ ∩ A₂ = ∅
```

Now there are as many three-digit integers that end in 0 as there are possible choices for the left-most and middle digits (because the right-most digit must be a 0). As illustrated below, there are nine choices for the left-most digit (the digits 1 through 9) and ten choices for the middle digit (the digits 0 through 9). Hence N(A₁) = 9 · 10 = 90.

```
↑
9 choices
1, 2, 3, 4, 5, 6, 7, 8, 9

↑
10 choices
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

↑
number ends in 0
```

Similar reasoning (using 5 instead of 0) shows that N(A₂) = 90 also. So
```
the number of
[three-digit integers] = N(A₁) + N(A₂) = 90 + 90 = 180.
that are divisible by 5
```

---

## The Difference Rule

An important consequence of the addition rule is the fact that if the number of elements in a set A and the number in a subset B of A are both known, then the number of elements that are in A and not in B can be computed.

### Theorem 9.3.2 The Difference Rule

If A is a finite set and B is a subset of A, then
N(A - B) = N(A) - N(B).

The difference rule is illustrated in Figure 9.3.3.

```
A (n elements)

B (k elements)

A – B (n – k elements)
```

The difference rule holds for the following reason: If B is a subset of A, then the two sets B and A - B have no elements in common and B ∪ (A - B) = A. Hence, by the addition rule,
N(B) + N(A - B) = N(A).
Subtracting N(B) from both sides gives the equation
N(A - B) = N(A) - N(B).

### Example 9.3.3 Counting PINs with Repeated Symbols

The PINs discussed in Examples 9.2.2 and 9.2.4 are made from exactly four symbols chosen from the 26 letters of the alphabet and the ten digits, with repetitions allowed.

a. How many PINs contain repeated symbols?
b. If all PINs are equally likely, what is the probability that a randomly chosen PIN contains a repeated symbol?

**Solution**

a. According to Example 9.2.2, there are 36⁴ = 1,679,616 PINs when repetition is allowed, and by Example 9.2.4, there are 1,413,720 PINs when repetition is not allowed. Thus, by the difference rule, there are
1,679,616 - 1,413,720 = 265,896
PINs that contain at least one repeated symbol.

b. By Example 9.2.2 there are 1,679,616 PINs in all, and by part (a) 265,896 of these contain at least one repeated symbol. Thus, by the equally likely probability formula,
the probability that a randomly chosen PIN contains a repeated symbol is 265,896/1,679,616 ≈ 0.158 = 15.8%.

An alternative solution to Example 9.3.3(b) is based on the observation that if S is the set of all PINs and A is the set of all PINs with no repeated symbol, then S - A is the set of all PINs with at least one repeated symbol. It follows that
P(S - A) = N(S - A)/N(S) by definition of probability in the equally likely case
= [N(S) - N(A)]/N(S) by the difference rule
= N(S)/N(S) - N(A)/N(S) by the laws of fractions
= 1 - P(A) by definition of probability in the equally likely case
≈ 1 - 0.842 by Example 9.2.4
≈ 0.158 = 15.8%

This solution illustrates a more general property of probabilities: that the probability of the complement of an event is obtained by subtracting the probability of the event from the number 1. In Section 9.8 we derive this formula from the axioms for probability.

### Formula for the Probability of the Complement of an Event

If S is a finite sample space and A is an event in S, then
P(Aᶜ) = 1 - P(A).

### Example 9.3.4 Number of Python Identifiers of Eight or Fewer Characters

In the computer language Python, identifiers must start with one of 53 symbols: either one of the 52 letters of the upper- and lower-case Roman alphabet or an underscore (_). The initial character may stand alone, or it may be followed by any number of additional characters chosen from a set of 63 symbols: the 53 symbols allowed as an initial character plus the ten digits. Certain keywords, however, such as and, if, print, and so forth, are set aside and may not be used as identifiers. In one implementation of Python there are 31 such reserved keywords, none of which has more than eight characters. How many Python identifiers are there that are less than or equal to eight characters in length?

**Solution**

The set of all Python identifiers with eight or fewer characters can be partitioned into eight subsets—identifiers of length 1, identifiers of length 2, and so on—as shown in Figure 9.3.4. The reserved words have various lengths (all less than or equal to 8), so the set of reserved words is shown overlapping the various subsets.

```
Set of Python Identifiers with Eight or Fewer Characters
length
1

length
2

length
3

length
4

length
5

length
6

length
7

length
8

Reserved words
```

According to the rules for creating Python identifiers, there are
- 53 potential identifiers of length 1 because there are 53 choices for the first character
- 53·63 potential identifiers of length 2 because the first character can be any one of 53 symbols, and the second character can be any one of 63 symbols
- 53·63² potential identifiers of length 3 because the first character can be any one of 53 symbols, and each of the next two characters can be any one of 63 symbols
- ...
- 53·63⁷ potential identifiers of length 8 because the first character can be any one of 53 symbols, and each of the next seven characters can be any one of 63 symbols.

Thus, by the addition rule, the number of potential Python identifiers with eight or fewer characters is
53 + 53·63 + 53·63² + 53·63³ + 53·63⁴ + 53·63⁵ + 53·63⁶ + 53·63⁷
= 53[(63⁸ - 1)/(63 - 1)] = 212,133,167,002,880.

Now 31 of these potential identifiers are reserved, so by the difference rule, the actual number of Python identifiers with eight or fewer characters is
212,133,167,002,880 - 31 = 212,133,167,002,849.

### Example 9.3.5 Internet Addresses

In order to communicate effectively, each computer in a network needs a distinguishing name called an address. For the Internet this address is currently a 32-bit number called the Internet Protocol (IP) address (although 128-bit addresses are being phased in to accommodate the growth of the Internet). For technical reasons some computers have more than one address, whereas other sets of computers, which use the Internet only sporadically, may share a pool of addresses that are assigned on a temporary basis. Like telephone numbers, IP addresses are divided into parts: one, the network ID, specifies the local network to which a given computer belongs, and the other, the host ID, specifies the particular computer.

An example of an IP address is 10001100 11000000 00100000 10001000, where the 32 bits have been divided into four groups of 8 for easier reading. To make the reading even easier, IP addresses are normally written as "dotted decimals," in which each group of 8 bits is converted into a decimal number between 0 and 255. For instance, the IP address above converts into 140.192.32.136.

In order to accommodate the various sizes of the local networks connected through the Internet, the network IDs are divided into several classes, the most important of which are called A, B, and C. In every class, a host ID may not consist of either all 0's or all 1's.

Class A network IDs are used for very large local networks. The left-most bit is set to 0, and the left-most 8 bits give the full network ID. The remaining 24 bits are used for individual host IDs. However, neither 00000000 nor 01111111 is allowed as a network ID for a class A IP address.

```
Network ID       Host ID
Class A: 0
```

Class B network IDs are used for medium to large local networks. The two left-most bits are set to 10, and the left-most 16 bits give the full network ID. The remaining 16 bits are used for individual host IDs.

```
Network ID          Host ID
Class B: 1 0
```

Class C network IDs are used for small local networks. The three left-most bits are set to 110, and the left-most 24 bits give the full network ID. The remaining 8 bits are used for individual host IDs.

```
Network ID               Host ID
Class C: 1 1 0
```

a. Check that the dotted decimal form of 10001100 11000000 00100000 10001000 is 140.192.32.136.
b. How many Class B networks can there be?
c. What is the dotted decimal form of the IP address for a computer in a Class B network?
d. How many host IDs can there be for a Class B network?

**Solution**

a. 10001100 = 1·2⁷ + 1·2³ + 1·2² = 128 + 8 + 4 = 140
   11000000 = 1·2⁷ + 1·2⁶ = 128 + 64 = 192
   00100000 = 1·2⁵ = 32
   10001000 = 1·2⁷ + 1·2³ = 128 + 8 = 136

b. The network ID for a Class B network consists of 16 bits and begins with 10. Because there are two choices for each of the remaining 14 positions (either 0 or 1), the total number of possible network IDs is 2¹⁴, or 16,384.

c. The network ID part of a Class B IP address goes from
   10000000 00000000 to 10111111 11111111.
   As dotted decimals, these numbers range from 128.0 to 191.255 because 10000000₂ = 128₁₀, 00000000₂ = 0₁₀, 10111111₂ = 191₁₀, and 11111111₂ = 255₁₀. Thus the dotted decimal form of the IP address of a computer in a Class B network is w.x.y.z, where 128 ≤ w ≤ 191, 0 ≤ x ≤ 255, 0 ≤ y ≤ 255, and 0 ≤ z ≤ 255. However, y and z are not allowed both to be 0 or both to be 255 because host IDs may not consist of either all 0's or all 1's.

d. For a class B network, 16 bits are used for host IDs. Having two choices (either 0 or 1) for each of 16 positions gives a potential total of 2¹⁶, or 65,536, host IDs. But because two of these are not allowed (all 0's and all 1's), the total number of host IDs is 65,534.

---

## The Inclusion/Exclusion Rule

The addition rule says how many elements are in a union of sets if the sets are mutually disjoint. Now consider the question of how to determine the number of elements in a union of sets when some of the sets overlap. For simplicity, begin by looking at a union of two sets A and B, as shown in Figure 9.3.5.

```
A       B        A       B        A       B
```

First observe that the number of elements in A ∪ B varies according to the number of elements the two sets have in common. If A and B have no elements in common, then N(A ∪ B) = N(A) + N(B). If A and B coincide, then N(A ∪ B) = N(A). Thus any general formula for N(A ∪ B) must contain a reference to the number of elements the two sets have in common, N(A ∩ B), as well as to N(A) and N(B).

The simplest way to derive a formula for N(A ∪ B) is to reason as follows: The number N(A) counts the elements that are in A and not in B and also the elements that are in both A and B. Similarly, the number N(B) counts the elements that are in B and not in A and also the elements that are in both A and B. Hence when the two numbers N(A) and N(B) are added, the elements that are in both A and B are counted twice. To get an accurate count of the elements in A ∪ B, it is necessary to subtract the number of elements that are in both A and B. Because these are the elements in A ∩ B,
N(A ∪ B) = N(A) + N(B) - N(A ∩ B).

A similar analysis gives a formula for the number of elements in a union of three sets, as shown in Theorem 9.3.3.

### Theorem 9.3.3 The Inclusion/Exclusion Rule for Two or Three Sets

If A, B, and C are any finite sets, then
N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
and
N(A ∪ B ∪ C) = N(A) + N(B) + N(C) - N(A ∩ B) - N(A ∩ C) - N(B ∩ C) + N(A ∩ B ∩ C).

It can be shown using mathematical induction (see exercise 48 at the end of this section) that formulas analogous to those of Theorem 9.3.3 hold for unions of any finite number of sets.

### Example 9.3.6 Counting Elements of a General Union

a. How many integers from 1 through 1,000 are multiples of 3 or multiples of 5?
b. How many integers from 1 through 1,000 are neither multiples of 3 nor multiples of 5?

**Solution**

a. Let A = the set of all integers from 1 through 1,000 that are multiples of 3.
   Let B = the set of all integers from 1 through 1,000 that are multiples of 5.
   Then
   A ∪ B = the set of all integers from 1 through 1,000 that are multiples of 3 or multiples of 5
   and
   A ∩ B = the set of all integers from 1 through 1,000 that are multiples of both 3 and 5
          = the set of all integers from 1 through 1,000 that are multiples of 15.

   [Now calculate N(A), N(B), and N(A ∩ B) and use the inclusion/exclusion rule to solve for N(A ∪ B).]

   Because every third integer from 3 through 999 is a multiple of 3, each can be represented in the form 3k, for some integer k from 1 through 333. Hence there are 333 multiples of 3 from 1 through 1,000, and so N(A) = 333.

```
1   2   3   4   5   6   ...   996   997   998   999
        ↑   ↑         ↑           ↑
      3·1  3·2       3·332      3·333
```

   Similarly, each multiple of 5 from 1 through 1,000 has the form 5k, for some integer k from 1 through 200.

```
1   2   3   4   5   6   7   8   9   10   ...   995   996   997   998   999   1,000
        ↑   ↑         ↑           ↑
      5·1  5·2       5·199      5·200
```

   Thus there are 200 multiples of 5 from 1 through 1,000 and N(B) = 200.

   Finally, each multiple of 15 from 1 through 1,000 has the form 15k, for some integer k from 1 through 66 (since 990 = 66·15).

```
1   2   ...   15   ...   30   ...   975   ...   990   ...   999   1,000
              ↑          ↑          ↑           ↑
            15·1      15·2      15·65      15·66
```

   Hence there are 66 multiples of 15 from 1 through 1,000, and N(A ∩ B) = 66.

   It follows by the inclusion/exclusion rule that
   N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
             = 333 + 200 - 66
             = 467.
   Thus, 467 integers from 1 through 1,000 are multiples of 3 or multiples of 5.

b. There are 1,000 integers from 1 through 1,000, and by part (a), 467 of these are multiples of 3 or multiples of 5. Thus, by the set difference rule, there are 1,000 - 467 = 533 that are neither multiples of 3 nor multiples of 5.

Note that the solution to part (b) of Example 9.3.6 hid a use of De Morgan's law. The number of elements that are neither in A nor in B is N(Aᶜ ∩ Bᶜ), and by De Morgan's law, Aᶜ ∩ Bᶜ = (A ∪ B)ᶜ. So N((A ∪ B)ᶜ) was then calculated using the set difference rule: N((A ∪ B)ᶜ) = N(U) - N(A ∪ B), where the universe U was the set of all integers from 1 through 1,000. Exercises 37-39 at the end of this section explore this technique further.

### Example 9.3.7 Counting the Number of Elements in an Intersection

A professor in a discrete mathematics class passes out a form asking students to check all the mathematics and computer science courses they have recently taken. The finding is that out of a total of 50 students in the class,
- 30 took precalculus;
- 16 took both precalculus and Java;
- 18 took calculus;
- 8 took both calculus and Java;
- 26 took Java;
- 47 took at least one of the three courses.
- 9 took both precalculus and calculus;

Note that when we write "30 students took precalculus," we mean that the total number of students who took precalculus is 30, and we allow for the possibility that some of these students may have taken one or both of the other courses. If we want to say that 30 students took precalculus only (and not either of the other courses), we will say so explicitly.

a. How many students did not take any of the three courses?
b. How many students took all three courses?
c. How many students took precalculus and calculus but not Java? How many students took precalculus but neither calculus nor Java?

**Solution**

a. By the difference rule, the number of students who did not take any of the three courses equals the number in the class minus the number who took at least one course. Thus the number of students who did not take any of the three courses is 50 - 47 = 3.

b. Let P = the set of students who took precalculus
   C = the set of students who took calculus
   J = the set of students who took Java.

   Then, by the inclusion/exclusion rule,
   N(P ∪ C ∪ J) = N(P) + N(C) + N(J) - N(P ∩ C) - N(P ∩ J) - N(C ∩ J) + N(P ∩ C ∩ J)

   Substituting known values, we get
   47 = 30 + 26 + 18 - 9 - 16 - 8 + N(P ∩ C ∩ J).

   Solving for N(P ∩ C ∩ J) gives
   N(P ∩ C ∩ J) = 6.

   Hence there are six students who took all three courses. In general, if you know any seven of the eight terms in the inclusion/exclusion formula for three sets, you can solve for the eighth term.

c. To answer the questions of part (c), look at the diagram in Figure 9.3.6.

```
The number of
students who
took all three
courses
The number of
students who
took both
precalcules and
calcules
but not Java

P

J
11
10
3
6
8
2
7
C
3
```

Since N(P ∩ C ∩ J) = 6, put the number 6 inside the innermost region. Then work outward to find the numbers of students represented by the other regions of the diagram. For example, since nine students took both precalculus and calculus and six took all three courses, 9 - 6 = 3 students took precalculus and calculus but not Java.

Similarly, since 16 students took precalculus and Java and six took all three courses, 16 - 6 = 10 students took precalculus and Java but not calculus.

Now the total number of students who took precalculus is 30. Of these 30, three also took calculus but not Java, ten took Java but not calculus, and six took both calculus and Java. That leaves 11 students who took precalculus but neither of the other two courses.

A similar analysis can be used to fill in the numbers for the other regions of the diagram.

---

## Test Yourself

1. The addition rule says that if a finite set A equals the union of k distinct mutually disjoint subsets A₁, A₂, ..., Aₖ, then _____.
2. The difference rule says that if A is a finite set and B is a subset of A, then _____.
3. If S is a finite sample space and A is an event in S, then the probability of Aᶜ equals _____.
4. The inclusion/exclusion rule for two sets says that if A and B are any finite sets, then _____.
5. The inclusion/exclusion rule for three sets says that if A, B, and C are any finite sets, then _____.

---

## Exercise Set 9.3

1. a. How many bit strings consist of from one through four digits? (Strings of different lengths are considered distinct. Thus 10 and 0010 are distinct strings.)
   b. How many bit strings consist of from five through eight digits?

2. a. How many strings of hexadecimal digits consist of from one through three digits? (Recall that hexadecimal numbers are constructed using the 16 digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.)
   b. How many strings of hexadecimal digits consist of from two through five digits?

3. a. How many integers from 1 through 999 do not have any repeated digits?
   b. How many integers from 1 through 999 have at least one repeated digit?
   c. What is the probability that an integer chosen at random from 1 through 999 has at least one repeated digit?

4. How many arrangements in a row of no more than three letters can be formed using the letters of the word NETWORK (with no repetitions allowed)?

5. a. How many five-digit integers (integers from 10,000 through 99,999) are divisible by 5?
   b. What is the probability that a five-digit integer chosen at random is divisible by 5?

6. In a certain state, license plates consist of from zero to three letters followed by from zero to four digits, with the provision, however, that a blank plate is not allowed.
   a. How many different license plates can the state produce?
   b. Suppose 85 letter combinations are not allowed because of their potential for giving offense. How many different license plates can the state produce?

7. In another state, all license plates consist of from four to six symbols chosen from the 26 letters of the alphabet together with the ten digits 0-9.
   a. How many license plates are possible if repetition of symbols is allowed?
   b. How many license plates do not contain any repeated symbol?
   c. How many license plates have at least one repeated symbol?
   d. What is the probability that a license plate chosen at random has a repeated symbol?

8. At a certain company, passwords must be from 3-5 symbols long and composed of the 26 letters of the alphabet, the ten digits 0-9, and the 14 symbols !,@,#,$,%,^,&,*,(,),-,+,{, and }.
   a. How many passwords are possible if repetition of symbols is allowed?
   b. How many passwords contain no repeated symbols?
   c. How many passwords have at least one repeated symbol?
   d. What is the probability that a password chosen at random has a repeated symbol?

9. a. Consider the following algorithm segment:
   ```
   for i := 1 to 4
     for j := 1 to i
       [Statements in body of inner loop.
        None contain branching statements
        that lead outside the loop.]
     next j
   next i
   ```
   How many times will the inner loop be iterated when the algorithm is implemented and run?

   b. Let n be a positive integer, and consider the following algorithm segment:
   ```
   for i := 1 to n
     for j := 1 to i
       [Statements in body of inner loop.
        None contain branching statements
        that lead outside the loop.]
     next j
   next i
   ```
   How many times will the inner loop be iterated when the algorithm is implemented and run?
is implemented and run?

10. A calculator has an eight-digit display and a decimal point that is located at the extreme right of the number displayed, at the extreme left, or between any pair of digits. The calculator can also display a minus sign at the extreme left of the number. How many distinct numbers can the calculator display? (Note that certain numbers are equal, such as 1.9, 1.90, and 01.900, and should, therefore, not be counted twice.)

11. a. How many ways can the letters of the word QUICK be arranged in a row?
    b. How many ways can the letters of the word QUICK be arranged in a row if the Q and the U must remain next to each other in the order QU?
    c. How many ways can the letters of the word QUICK be arranged in a row if the letters QU must remain together but may be in either the order QU or the order UQ?

12. a. How many ways can the letters of the word THEORY be arranged in a row?
    b. How many ways can the letters of the word THEORY be arranged in a row if T and H must remain next to each other as either TH or HT?

13. A group of eight people are attending the movies together.
    a. Two of the eight insist on sitting side-by-side. In how many ways can the eight be seated together in a row?
    b. Two of the people do not like each other and do not want to sit side-by-side. Now how many ways can the eight be seated together in a row?

14. An early compiler recognized variable names according to the following rules: Numeric variable names had to begin with a letter, and then the letter could be followed by another letter or a digit or by nothing at all. String variable names had to begin with the symbol $ followed by a letter, which could then be followed by another letter or a digit or by nothing at all. How many distinct variable names were recognized by this compiler?

15. Identifiers in a certain database language must begin with a letter, and then the letter may be followed by other characters, which can be letters, digits, or underscores (_). However, 82 keywords (all consisting of 15 or fewer characters) are reserved and cannot be used as identifiers. How many identifiers with 30 or fewer characters are possible? (Write the answer using summation notation and evaluate it using a formula from Section 5.2.)

16. a. If any seven digits could be used to form a telephone number, how many seven-digit telephone numbers would not have any repeated digits?
    b. How many seven-digit telephone numbers would have at least one repeated digit?
    c. What is the probability that a randomly chosen seven-digit telephone number would have at least one repeated digit?

17. a. How many strings of four hexadecimal digits do not have any repeated digits?
    b. How many strings of four hexadecimal digits have at least one repeated digit?
    c. What is the probability that a randomly chosen string of four hexadecimal digits has at least one repeated digit?

18. Just as the difference rule gives rise to a formula for the probability of the complement of an event, so the addition and inclusion/exclusion rules give rise to formulas for the probability of the union of mutually disjoint events and for a general union of (not necessarily mutually exclusive) events.
    a. Prove that for mutually disjoint events A and B, P(A ∪ B) = P(A) + P(B).
    b. Prove that for any events A and B, P(A ∪ B) = P(A) + P(B) - P(A ∩ B).

19. A combination lock requires three selections of numbers, each from 1 through 39. Suppose the lock is constructed in such a way that no number can be used twice in a row but the same number may occur both first and third. For example, 20 13 20 would be acceptable, but 20 20 13 would not. How many different combinations are possible?

20. a. How many integers from 1 through 100,000 contain the digit 6 exactly once?
    b. How many integers from 1 through 100,000 contain the digit 6 at least once?
    c. If an integer is chosen at random from 1 through 100,000, what is the probability that it contains two or more occurrences of the digit 6?

21. Six new employees, two of whom are married to each other, are to be assigned six desks that are lined up in a row. If the assignment of employees to desks is made randomly, what is the probability that the married couple will have nonadjacent desks? (Hint: First find the probability that the couple will have adjacent desks, and then subtract this number from 1.)

22. Consider strings of length n over the set {a, b, c, d}.
   a. How many such strings contain at least one pair of adjacent characters that are the same?
   b. If a string of length ten over {a, b, c, d} is chosen at random, what is the probability that it contains at least one pair of adjacent characters that are the same?

23. a. How many integers from 1 through 1,000 are multiples of 4 or multiples of 7?
   b. Suppose an integer from 1 through 1,000 is chosen at random. Use the result of part (a) to find the probability that the integer is a multiple of 4 or a multiple of 7.
   c. How many integers from 1 through 1,000 are neither multiples of 4 nor multiples of 7?

24. a. How many integers from 1 through 1,000 are multiples of 2 or multiples of 9?
   b. Suppose an integer from 1 through 1,000 is chosen at random. Use the result of part (a) to find the probability that the integer is a multiple of 2 or a multiple of 9.
   c. How many integers from 1 through 1,000 are neither multiples of 2 nor multiples of 9?

25. Counting Strings:
   a. Make a list of all bit strings of lengths zero, one, two, three, and four that do not contain the bit pattern 111.
   b. For each integer n ≥ 0, let dn = the number of bit strings of length n that do not contain the bit pattern 111. Find d0, d1, d2, d3, and d4.
   c. Find a recurrence relation for d0, d1, d2, . . .
   d. Use the results of parts (b) and (c) to find the number of bit strings of length five that do not contain the pattern 111.

26. Counting Strings: Consider the set of all strings of a's, b's, and c's.
   a. Make a list of all of these strings of lengths zero, one, two, and three that do not contain the pattern aa.
   b. For each integer n ≥ 0, let sn = the number of strings of a's, b's, and c's of length n that do not contain the pattern aa. Find s0, s1, s2, and s3.
   c. Find a recurrence relation for s0, s1, s2, . . .
   d. Use the results of parts (b) and (c) to find the number of strings of a's, b's, and c's of length four that do not contain the pattern aa.
   e. Use the technique described in Section 5.8 to find an explicit formula for s0, s1, s2, . . .

27. For each integer n ≥ 0, let ak be the number of bit strings of length n that do not contain the pattern 101.
   a. Show that ak = ak-1 + ak-3 + ak-4 + · · · + a0 + 2, for all integers k ≥ 3.
   b. Use the result of part (a) to show that if k ≥ 3, then ak = 2ak-1 - ak-2 + ak-3.

28. For each integer n ≥ 2 let an be the number of permutations of {1, 2, 3, . . . , n} in which no number is more than one place removed from its "natural" position. Thus a1 = 1 since the one permutation of {1}, namely 1, does not move 1 from its natural position. Also a2 = 2 since neither of the two permutations of {1,2}, namely 12 and 21, moves either number more than one place from its natural position.
   a. Find a3.
   b. Find a recurrence relation for a1, a2, a3, . . .

29. Refer to Example 9.3.5.
   a. Write the following IP address in dotted decimal form: 11001010 00111000 01101011 11101110
   b. How many Class A networks can there be?
   c. What is the dotted decimal form of the IP address for a computer in a Class A network?
   d. How many host IDs can there be for a Class A network?
   e. How many Class C networks can there be?
   f. What is the dotted decimal form of the IP address for a computer in a Class C network?
   g. How many host IDs can there be for a Class C network?
   h. How can you tell, by looking at the first of the four numbers in the dotted decimal form of an IP address, what kind of network the address is from? Explain.
   i. An IP address is 140.192.32.136. What class of network does it come from?
   j. An IP address is 202.56.107.238. What class of network does it come from?

30. A row in a classroom has n seats. Let sn be the number of ways nonempty sets of students can sit in the row so that no student is seated directly adjacent to any other student. (For instance, a row of three seats could contain a single student in any of the seats or a pair of students in the two outer seats. Thus s3 = 4.) Find a recurrence relation for s1, s2, s3, . . .

31. Assume that birthdays are equally likely to occur in any one of the 12 months of the year.
   a. Given a group of four people, A, B, C, and D, what is the total number of ways in which birth months could be associated with A, B, C, and D? (For instance, A and B might have been born in May, C in September, and D in February. As another example, A might have been born in January, B in June, C in March, and D in October.)
   b. How many ways could birth months be associated with A, B, C, and D so that no two people would share the same birth month?
   c. How many ways could birth months be associated with A, B, C, and D so that at least two people would share the same birth month?
   d. What is the probability that at least two people out of A, B, C, and D share the same birth month?
   e. How large must n be so that in any group of n people, the probability that two or more share the same birth month is at least 50%?

32. Assuming that all years have 365 days and all birthdays occur with equal probability, how large must n be so that in any randomly chosen group of n people, the probability that two or more have the same birthday is at least 1/2? (This is called the birthday problem. Many people find the answer surprising.)

33. A college conducted a survey to explore the academic interests and achievements of its students. It asked students to place checks beside the numbers of all the statements that were true of them. Statement #1 was "I was on the honor roll last term," statement #2 was "I belong to an academic club, such as the math club or the Spanish club," and statement #3 was "I am majoring in at least two subjects." Out of a sample of 100 students, 28 checked #1, 26 checked #2, and 14 checked #3, 8 checked both #1 and #2, 4 checked both #1 and #3, 3 checked both #2 and #3, and 2 checked all three statements.
   a. How many students checked at least one of the statements?
   b. How many students checked none of the statements?
   c. Let H be the set of students who checked #1, C the set of students who checked #2, and D the set of students who checked #3. Fill in the numbers for all eight regions of the diagram below.
   d. How many students checked #1 and #2 but not #3?
   e. How many students checked #2 and #3 but not #1?
   f. How many students checked #2 but neither of the other two?

34. A study was done to determine the efficacy of three different drugs—A, B, and C—in relieving headache pain. Over the period covered by the study, 50 subjects were given the chance to use all three drugs. The following results were obtained:
   - 21 reported relief from drug A.
   - 21 reported relief from drug B.
   - 31 reported relief from drug C.
   - 9 reported relief from both drugs A and B.
   - 14 reported relief from both drugs A and C.
   - 15 reported relief from both drugs B and C.
   - 41 reported relief from at least one of the drugs.
   Note that some of the 21 subjects who reported relief from drug A may also have reported relief from drugs B or C. A similar occurrence may be true for the other data.
   a. How many people got relief from none of the drugs?
   b. How many people got relief from all three drugs?
   c. Let A be the set of all subjects who got relief from drug A, B the set of all subjects who got relief from drug B, and C the set of all subjects who got relief from drug C. Fill in the numbers for all eight regions of the diagram below.
   d. How many subjects got relief from A only?

35. An interesting use of the inclusion/exclusion rule is to check survey numbers for consistency. For example, suppose a public opinion polltaker reports that out of a national sample of 1,200 adults, 675 are married, 682 are from 20 to 30 years old, 684 are female, 195 are married and are from 20 to 30 years old, 467 are married females, 318 are females from 20 to 30 years old, and 165 are married females from 20 to 30 years old. Are the polltaker's figures consistent? Could they have occurred as a result of an actual sample survey?

36. Fill in the reasons for each step below. If A and B are sets in a finite universe U, then
   N(A ∩ B) = N(U) - N((A ∩ B)^c)
   = N(U) - N(A^c ∪ B^c)
   = N(U) - (N(A^c) + N(B^c) - N(A^c ∩ B^c))

37. How many positive integers less than 1,000 have no common factors with 1,000?

38. How many permutations of abcde are there in which the first character is a, b, or c and the last character is c, d, or e?

39. How many integers from 1 through 999,999 contain each of the digits 1, 2, and 3 at least once? (Hint: For each i = 1, 2, and 3, let Ai be the set of all integers from 1 through 999,999 that do not contain the digit i.)

40. Use the inclusion/exclusion principle to prove the following: If n = pq, where p and q are distinct prime numbers, then φ(n) = (p-1)(q-1).

41. Use the inclusion/exclusion principle to prove the following: If n = pqr, where p, q, and r are distinct prime numbers, then φ(n) = (p-1)(q-1)(r-1).

42. A gambler decides to play successive games of blackjack until he loses three times in a row. (Thus the gambler could play five games by losing the first, winning the second, and losing the final three or by winning the first two and losing the final three. These possibilities can be symbolized as LWLLL and WWLLL.) Let gn be the number of ways the gambler can play n games.
   a. Find g3, g4, and g5.
   b. Find g6.
   c. Find a recurrence relation for g3, g4, g5, . . .

43. A derangement of the set {1, 2, . . . , n} is a permutation that moves every element of the set away from its "natural" position. Thus 21 is a derangement of {1, 2}, and 231 and 312 are derangements of {1, 2, 3}. For each positive integer n, let dn be the number of derangements of the set {1, 2, . . . , n}.
   a. Find d1, d2, and d3.
   b. Find d4.
   c. Find a recurrence relation for d1, d2, d3, . . .

44. Note that a product x1x2x3 may be parenthesized in two different ways: (x1x2)x3 and x1(x2x3). Similarly, there are several different ways to parenthesize x1x2x3x4. Two such ways are (x1x2)(x3x4) and x1((x2x3)x4). Let Pn be the number of different ways to parenthesize the product x1x2 . . . xn. Show that if P1 = 1, then
   Pn = ∑_{k=1}^{n-1} Pk Pn-k for all integers n ≥ 2.
   (It turns out that the sequence P1, P2, P3, . . . is the same as the sequence of Catalan numbers: Pn = Cn-1 for all integers n ≥ 1. See Example 5.6.4.)

45. Use mathematical induction to prove Theorem 9.3.1.

46. Prove the inclusion/exclusion rule for two sets A and B by showing that A ∪ B can be partitioned into A ∩ B, A - (A ∩ B), and B - (A ∩ B), and then using the addition and difference rules.

47. Prove the inclusion/exclusion rule for three sets.

48. Use mathematical induction to prove the general inclusion/exclusion rule:
   If A1, A2, . . . , An are finite sets, then
   N(A1 ∪ A2 ∪ · · · ∪ An) = ∑_{1≤i≤n} N(Ai) - ∑_{1≤i<j≤n} N(Ai ∩ Aj) + ∑_{1≤i<j<k≤n} N(Ai ∩ Aj ∩ Ak) - · · · + (-1)^{n+1} N(A1 ∩ A2 ∩ · · · ∩ An).

49. A circular disk is cut into n distinct sectors, each shaped like a piece of pie and all meeting at the center point of the disk. Each sector is to be painted red, green, yellow, or blue in such a way that no two adjacent sectors are painted the same color. Let Sn be the number of ways to paint the disk.
   a. Find a recurrence relation for Sk in terms of Sk-1 and Sk-2 for each integer k ≥ 4.
   b. Find an explicit formula for Sn for n ≥ 2.
