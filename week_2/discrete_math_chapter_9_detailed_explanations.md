# Discrete Mathematics Chapter 9 - Detailed Example Explanations

This document provides detailed explanations for every example from Chapter 9 of Discrete Mathematics with Applications, following the same format as the detailed explanation for examples in Chapter 5 and Chapter 8.

## Chapter 9.1 Examples

### Example 9.1.1 Probabilities for a Deck of Cards

An ordinary deck of cards contains 52 cards divided into four suits. The red suits are diamonds (♦) and hearts (♥) and the black suits are clubs (♣) and spades (♠). Each suit contains 13 cards of the following denominations: 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king), and A (ace). The cards J, Q, and K are called face cards.

Mathematician Persi Diaconis, working with David Aldous in 1986 and Dave Bayer in 1992, showed that seven shuffles are needed to "thoroughly mix up" the cards in an ordinary deck. In 2000 mathematician Nick Trefethen, working with his father, Lloyd Trefethen, a mechanical engineer, used a somewhat different definition of "thoroughly mix up" to show that six shuffles will nearly always suffice.

Imagine that the cards in a deck have become—by some method—so thoroughly mixed up that if you spread them out face down and pick one at random, you are as likely to get any one card as any other.

a. What is the sample space of outcomes?
b. What is the event that the chosen card is a black face card?
c. What is the probability that the chosen card is a black face card?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For a standard deck of 52 playing cards, determine the sample space, identify the event of drawing a black face card, and calculate its probability.

**Step-by-Step Reasoning:**

1. **Understanding the Sample Space:**
   - A sample space is the set of all possible outcomes of a random process or experiment.
   - For this experiment, we are picking one card at random from a standard deck of 52 cards.
   - Since the cards are thoroughly mixed and we pick one at random, each card is equally likely to be selected.
   - Therefore, the sample space S consists of all 52 cards in the deck.

2. **Defining the Event:**
   - An event is a subset of the sample space.
   - We need to find the event that the chosen card is a black face card.
   - Face cards are Jacks (J), Queens (Q), and Kings (K).
   - Black suits are clubs (♣) and spades (♠).
   - So the black face cards are: J♣, Q♣, K♣, J♠, Q♠, K♠.

3. **Calculating the Probability:**
   - The equally likely probability formula states that if S is a finite sample space with all outcomes equally likely and E is an event in S, then P(E) = N(E)/N(S).
   - Here, N(E) = 6 (the number of black face cards).
   - N(S) = 52 (total number of cards in the deck).
   - Therefore, P(E) = 6/52 ≈ 11.5%.

**Common Mistakes to Avoid:**
- Confusing face cards with all cards of denomination 10 or higher (face cards are only J, Q, K).
- Forgetting that there are 4 suits, each with 3 face cards, so 12 face cards total, but we only want the black ones.
- Not understanding that the cards are equally likely to be chosen.

**Key Insights:**
- This example introduces the fundamental concepts of probability: sample space, events, and the equally likely probability formula.
- It shows how to systematically count elements in a set to calculate probabilities.
- The calculation 6/52 simplifies to 3/26, which is the exact probability.

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

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For two six-sided dice (one blue, one gray), represent the sample space using compact notation and find the probability that the sum of the numbers showing is 6.

**Step-by-Step Reasoning:**

1. **Understanding the Sample Space:**
   - Each die has 6 faces, numbered 1 through 6.
   - Since the dice are distinguishable (blue and gray), we need to consider ordered pairs.
   - The blue die can show any number from 1-6, and the gray die can show any number from 1-6 independently.
   - Using compact notation, we represent (blue, gray) as a two-digit number where the first digit is blue and second is gray.
   - So S = {11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66}.

2. **Defining the Event:**
   - The event E is that the sum of the numbers showing is 6.
   - We need to find all outcomes where blue + gray = 6.
   - This gives us: (1,5), (2,4), (3,3), (4,2), (5,1).
   - In compact notation: 15, 24, 33, 42, 51.

3. **Calculating the Probability:**
   - N(E) = 5 (the five outcomes listed above).
   - N(S) = 36 (6 × 6 = 36 possible outcomes).
   - Therefore, P(E) = 5/36.

**Common Mistakes to Avoid:**
- Forgetting that dice are distinguishable (blue vs gray matters).
- Using unordered pairs instead of ordered pairs.
- Not listing all combinations that sum to 6 systematically.
- Confusing this with unordered dice (which would have only 21 possible outcomes).

**Key Insights:**
- This example demonstrates how to handle distinguishable objects in probability.
- It shows the importance of systematic counting when outcomes are equally likely.
- The compact notation makes it easier to list and count outcomes.

### Example 9.1.3 The Monty Hall Problem

There are three doors on the set for a game show. Let's call them A, B, and C. If you pick the right door you win the prize. You pick door A. The host of the show, Monty Hall, then opens one of the other doors and reveals that there is no prize behind it. Keeping the remaining two doors closed, he asks you whether you want to switch your choice to the other closed door or stay with your original choice of door A. What should you do if you want to maximize your chance of winning the prize: stay with door A or switch—or would the likelihood of winning be the same either way?

```
Case 1     Case 2     Case 3
   B           C           B
   C           B           C
   B           C           B
```

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: In the Monty Hall problem with three doors (A, B, C), after choosing door A and having one wrong door opened, determine whether to switch doors to maximize the probability of winning.

**Step-by-Step Reasoning:**

1. **Understanding the Initial Situation:**
   - There are three doors, one with a prize behind it.
   - You choose door A (without loss of generality).
   - The prize is equally likely to be behind any door initially, so P(prize behind A) = P(prize behind B) = P(prize behind C) = 1/3.

2. **The Host's Action:**
   - The host knows where the prize is and always opens a door that has no prize behind it.
   - The host cannot open door A (your choice).
   - So the host opens either door B or door C, whichever doesn't have the prize.

3. **Analyzing the Three Cases:**
   - **Case 1:** Prize is behind A. Host can open either B or C. You win by staying with A.
   - **Case 2:** Prize is behind B. Host must open C. You win by switching to B.
   - **Case 3:** Prize is behind C. Host must open B. You win by switching to C.

4. **Calculating Probabilities:**
   - Each case has probability 1/3 initially.
   - In Case 1 (probability 1/3): You win by staying.
   - In Cases 2 and 3 (probability 2/3 total): You win by switching.
   - Therefore, switching gives you a 2/3 probability of winning, staying gives 1/3.

**Common Mistakes to Avoid:**
- Thinking that after one door is opened, the remaining two doors each have 1/2 probability.
- Forgetting that the host's action provides information about where the prize is not located.
- Assuming the host chooses randomly which door to open.

**Key Insights:**
- This is a classic example of conditional probability and Bayesian reasoning.
- The host's action reveals information that changes the probabilities.
- Many people find the correct answer counterintuitive, which is why this problem became famous.

### Example 9.1.4 Counting the Elements of a Sublist

a. How many three-digit integers (integers from 100 to 999 inclusive) are divisible by 5?
b. What is the probability that a randomly chosen three-digit integer is divisible by 5?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of three-digit integers divisible by 5 and find the probability of selecting one at random.

**Step-by-Step Reasoning:**

1. **Finding the First and Last Three-Digit Multiples of 5:**
   - The smallest three-digit integer is 100.
   - 100 divided by 5 is 20, so 5 × 20 = 100.
   - The largest three-digit integer is 999.
   - 999 divided by 5 is 199.8, so the largest multiple is 5 × 199 = 995.

2. **Using Theorem 9.1.1:**
   - Theorem 9.1.1 states that if m ≤ n, then there are n - m + 1 integers from m to n inclusive.
   - Here, m = 100, n = 995.
   - So the number of three-digit multiples of 5 is 995 - 100 + 1 = 896.

3. **Alternative Approach (as shown in the example):**
   - Three-digit integers divisible by 5 end in 0 or 5.
   - First digit: 1-9 (9 choices)
   - Second digit: 0-9 (10 choices)
   - Third digit: 0 or 5 (2 choices)
   - Total: 9 × 10 × 2 = 180.

4. **Calculating Probability:**
   - Total three-digit integers: 999 - 100 + 1 = 900.
   - Number divisible by 5: 180.
   - Probability: 180/900 = 1/5.

**Common Mistakes to Avoid:**
- Forgetting that 100 is included (it is a three-digit multiple of 5).
- Not realizing that 995 is the largest three-digit multiple of 5 less than 1000.
- Using 999 - 100 = 899 instead of 899 + 1 = 900.

**Key Insights:**
- This example shows two different methods to count the same set: using the formula for counting elements in a list, and using systematic multiplication.
- It demonstrates how to find the first and last elements in a sequence of numbers with a common property.
- The probability calculation follows directly from the counting.

### Example 9.1.5 Application: Counting Elements of a One-Dimensional Array

Analysis of many computer algorithms requires skill at counting the elements of a one-dimensional array. Let A[1], A[2], . . . , A[n] be a one-dimensional array, where n is a positive integer.

a. Suppose the array is cut at a middle value A[m] so that two subarrays are formed:
   (1) A[1], A[2], . . . , A[m] and
   (2) A[m + 1], A[m + 2], . . . , A[n].

   How many elements does each subarray have?
b. What is the probability that a randomly chosen element of the array has an even subscript
   (i) if n is even?
   (ii) if n is odd?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For an array A[1] to A[n], determine the sizes of subarrays when cut at A[m] and find the probability of selecting an element with an even subscript.

**Step-by-Step Reasoning:**

1. **Counting Elements in Subarrays:**
   - First subarray: A[1] to A[m]
   - This is the list of integers from 1 to m inclusive.
   - By Theorem 9.1.1: m - 1 + 1 = m elements.

   - Second subarray: A[m+1] to A[n]
   - This is the list of integers from m+1 to n inclusive.
   - By Theorem 9.1.1: n - (m+1) + 1 = n - m elements.

2. **Probability for Even n:**
   - Elements with even subscripts: 2, 4, 6, ..., n
   - This is an arithmetic sequence with first term 2, common difference 2.
   - The number of terms is n/2.
   - Total elements: n
   - Probability: (n/2)/n = 1/2.

3. **Probability for Odd n:**
   - Elements with even subscripts: 2, 4, 6, ..., n-1
   - Number of terms: (n-1)/2
   - Total elements: n
   - Probability: ((n-1)/2)/n = (n-1)/(2n)

**Common Mistakes to Avoid:**
- Forgetting that A[m] is the last element of the first subarray, not the first of the second.
- Using floor division incorrectly when counting even indices.
- Not considering that when n is odd, the largest even subscript is n-1.

**Key Insights:**
- This example shows how to apply the counting formula to array indices.
- It demonstrates that when n is even, exactly half the elements have even subscripts.
- When n is odd, slightly fewer than half have even subscripts.
- The floor function ⌊n/2⌋ gives the correct count for even subscripts.

## Chapter 9.2 Examples

### Example 9.2.1 Possibilities for Tournament Play

Teams A and B are to play each other repeatedly until one wins two games in a row or a total of three games. One way in which this tournament can be played is for A to win the first game, B to win the second, and A to win the third and fourth games. Denote this by writing A–B–A–A.

a. How many ways can the tournament be played?
b. Assuming that all the ways of playing the tournament are equally likely, what is the probability that five games are needed to determine the tournament winner?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of possible sequences of games between teams A and B until one wins two in a row or three games total, and find the probability of needing five games.

**Step-by-Step Reasoning:**

1. **Understanding the Tournament Rules:**
   - Games continue until one team wins two consecutive games OR a total of three games are played.
   - The tournament ends when either condition is met.
   - We need to count all possible sequences of A wins and B wins.

2. **Using a Possibility Tree:**
   - The tree starts at the beginning.
   - At each step, we branch on who wins the next game.
   - We stop when we reach a winning condition.

3. **Listing All Possible Sequences:**
   - Game 1: A wins (A), B wins (B)
   - From A: Game 2 A wins (AA - A wins), B wins (AB - continue)
   - From AA: A already won two in a row.
   - From AB: Game 3 A wins (ABA - A wins), B wins (ABB - B wins)
   - From B: Game 2 A wins (BA - continue), B wins (BB - B wins)
   - From BA: Game 3 A wins (BAA - A wins), B wins (BAB - B wins)
   - From BB: B already won two in a row.

4. **Counting the Sequences:**
   - AA, BB (2 games)
   - ABA, ABB, BAA, BAB (3 games)
   - ABAA, ABAB, BABA, BABB (4 games)
   - ABAAB, ABAAB, BABAA, BABAB (5 games)
   - Total: 2 + 4 + 4 + 4 = 14? Wait, let me count properly...

Actually, looking at the tree diagram in the book:
- The tree shows 10 paths total.
- The sequences are: AA, BB, ABA, ABB, BAA, BAB, ABAA, ABAB, BABA, BABB.

5. **Probability of 5 Games:**
   - Sequences requiring 5 games: ABABA, ABABB, BABAA, BABAB.
   - There are 4 such sequences.
   - Total sequences: 10.
   - Probability: 4/10 = 2/5 = 40%.

**Common Mistakes to Avoid:**
- Forgetting that the tournament can end early if someone wins two in a row.
- Not considering all possible sequences systematically.
- Missing some of the longer sequences.

**Key Insights:**
- Possibility trees are essential for counting sequences with stopping conditions.
- This example shows how to handle tournaments with multiple winning conditions.
- The tree structure makes it easy to see all possibilities and count them.

### Example 9.2.2 Number of Personal Identification Numbers (PINs)

A typical PIN (personal identification number) is a sequence of any four symbols chosen from the 26 letters in the alphabet and the ten digits, with repetition allowed. How many different PINs are possible?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of possible 4-symbol PINs where each symbol can be any letter A-Z or digit 0-9.

**Step-by-Step Reasoning:**

1. **Understanding the Symbol Set:**
   - Letters: A-Z (26 choices)
   - Digits: 0-9 (10 choices)
   - Total symbols: 26 + 10 = 36 choices per position.

2. **Using the Multiplication Rule:**
   - Step 1: Choose first symbol (36 choices)
   - Step 2: Choose second symbol (36 choices)
   - Step 3: Choose third symbol (36 choices)
   - Step 4: Choose fourth symbol (36 choices)
   - Total: 36 × 36 × 36 × 36 = 36⁴

3. **Calculating 36⁴:**
   - 36² = 1,296
   - 36⁴ = 1,296² = 1,679,616

**Common Mistakes to Avoid:**
- Forgetting that letters can be uppercase or lowercase (this example uses uppercase).
- Not including all 10 digits (0-9).
- Forgetting that repetition is allowed.

**Key Insights:**
- This is a basic application of the multiplication rule.
- PINs are essentially strings of length 4 over an alphabet of 36 symbols.
- The calculation shows there are over 1.6 million possible PINs.

### Example 9.2.3 The Number of Elements in a Cartesian Product

Suppose A₁, A₂, A₃, and A₄ are sets with n₁, n₂, n₃, and n₄ elements, respectively. Show that the set A₁ × A₂ × A₃ × A₄ has n₁n₂n₃n₄ elements.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Prove that the Cartesian product of four finite sets has size equal to the product of the sizes of the individual sets.

**Step-by-Step Reasoning:**

1. **Understanding Cartesian Product:**
   - A₁ × A₂ × A₃ × A₄ = {(a₁, a₂, a₃, a₄) | a₁ ∈ A₁, a₂ ∈ A₂, a₃ ∈ A₃, a₄ ∈ A₄}

2. **Using the Multiplication Rule:**
   - Step 1: Choose a₁ from A₁ (n₁ choices)
   - Step 2: Choose a₂ from A₂ (n₂ choices)
   - Step 3: Choose a₃ from A₃ (n₃ choices)
   - Step 4: Choose a₄ from A₄ (n₄ choices)
   - Total: n₁ × n₂ × n₃ × n₄

**Common Mistakes to Avoid:**
- Confusing Cartesian product with union or intersection.
- Thinking the size is the sum rather than the product.

**Key Insights:**
- This generalizes the multiplication rule to multiple sets.
- Cartesian products are fundamental in combinatorics and set theory.
- The proof by multiplication rule is straightforward and elegant.

### Example 9.2.4 Number of PINs without Repetition

In Example 9.2.2 we formed PINs using four symbols, either letters of the alphabet or digits, and supposing that letters could be repeated. Now suppose that repetition is not allowed.

a. How many different PINs are there?
b. If all PINs are equally likely, what is the probability that a PIN chosen at random contains no repeated symbol?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of 4-symbol PINs with no repeated symbols and find the probability of selecting such a PIN at random.

**Step-by-Step Reasoning:**

1. **Counting PINs without Repetition:**
   - Step 1: Choose first symbol (36 choices)
   - Step 2: Choose second symbol (35 choices, since no repetition)
   - Step 3: Choose third symbol (34 choices)
   - Step 4: Choose fourth symbol (33 choices)
   - Total: 36 × 35 × 34 × 33

2. **Calculating the Product:**
   - 36 × 35 = 1,260
   - 1,260 × 34 = 42,840
   - 42,840 × 33 = 1,413,720

3. **Probability Calculation:**
   - Total PINs (with repetition): 36⁴ = 1,679,616
   - PINs without repetition: 1,413,720
   - Probability: 1,413,720 / 1,679,616 ≈ 0.8417

**Common Mistakes to Avoid:**
- Using the wrong number of choices at each step.
- Forgetting that the probability is the ratio of the two counts.

**Key Insights:**
- This shows how repetition constraints reduce the number of possibilities.
- The probability is quite high (about 84%), which might be surprising.
- This is an application of the difference between permutations and combinations with repetition.

### Example 9.2.5 Number of Input/Output Tables for a Circuit with Two Input Signals

Consider the set of all circuits with two input signals P and Q. For each such circuit an input/output table can be constructed, but, as shown in Section 2.4, two such input/output tables may have the same values. How many distinct input/output tables can be constructed for circuits with input/output signals P and Q?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of distinct Boolean functions of two variables.

**Step-by-Step Reasoning:**

1. **Understanding Input/Output Tables:**
   - Two input signals: P and Q, each can be 0 or 1.
   - Four possible input combinations: (0,0), (0,1), (1,0), (1,1)
   - For each combination, the output can be 0 or 1.

2. **Using the Multiplication Rule:**
   - Step 1: Choose output for (0,0) (2 choices)
   - Step 2: Choose output for (0,1) (2 choices)
   - Step 3: Choose output for (1,0) (2 choices)
   - Step 4: Choose output for (1,1) (2 choices)
   - Total: 2 × 2 × 2 × 2 = 16

**Common Mistakes to Avoid:**
- Forgetting that each of the four input combinations can have independent outputs.
- Thinking there are fewer possibilities due to some constraint.

**Key Insights:**
- There are exactly 16 possible Boolean functions of two variables.
- This corresponds to the number of bit strings of length 4.
- Each function can be represented by a 4-bit truth table.

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
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of iterations of the inner loop in a nested loop structure.

**Step-by-Step Reasoning:**

1. **Analyzing the Loop Structure:**
   - Outer loop: i goes from 1 to 4 (4 iterations)
   - For each i, inner loop: j goes from 1 to 3 (3 iterations)

2. **Using the Multiplication Rule:**
   - The inner loop runs 3 times for each of the 4 outer loop iterations.
   - Total iterations: 4 × 3 = 12

3. **Trace Table Verification:**
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

**Common Mistakes to Avoid:**
- Forgetting that the inner loop runs to completion for each outer iteration.
- Not counting the iterations systematically.

**Key Insights:**
- Nested loops multiply the number of iterations.
- This is a simple application of the multiplication rule to algorithm analysis.
- The trace table provides a clear way to verify the count.

### Example 9.2.7 A More Subtle Use of the Multiplication Rule

Reorder the steps for choosing the officers in the previous example so that the total number of ways to choose officers can be computed using the multiplication rule.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Reorder the steps in the officer selection problem to apply the multiplication rule directly.

**Step-by-Step Reasoning:**

1. **Original Problem Context:**
   - From the previous example: 4 people (Ann, Bob, Cyd, Dan)
   - Choose president, treasurer, secretary
   - Constraints: Ann cannot be president, either Cyd or Dan must be secretary

2. **New Order of Steps:**
   - Step 1: Choose secretary (2 choices: Cyd or Dan)
   - Step 2: Choose president (2 choices: neither Ann nor the secretary)
   - Step 3: Choose treasurer (2 choices: the remaining two people)

3. **Applying Multiplication Rule:**
   - The number of choices at each step is constant regardless of previous choices.
   - Total: 2 × 2 × 2 = 8

**Common Mistakes to Avoid:**
- Not reordering the steps properly to make the choices independent.
- Forgetting the constraints when counting choices at each step.

**Key Insights:**
- Sometimes you need to reorder steps to apply the multiplication rule.
- The key is to make each step have a constant number of choices.
- This technique is useful when dependencies exist between choices.

### Example 9.2.8 Permutations of the Letters in a Word

a. How many ways can the letters in the word COMPUTER be arranged in a row?
b. How many ways can the letters in the word COMPUTER be arranged in a row if the letters CO must remain next to each other (in order) as a unit?
c. If letters of the word COMPUTER are randomly arranged in a row, what is the probability that the letters CO remain next to each other (in order) as a unit?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count permutations of the letters in "COMPUTER" with and without constraints, and find the probability of the constrained arrangement.

**Step-by-Step Reasoning:**

1. **Total Permutations (no constraints):**
   - 8 distinct letters.
   - Number of permutations: 8! = 40,320.

2. **Permutations with CO together:**
   - Treat "CO" as a single unit.
   - Now we have 7 units: (CO), M, P, U, T, E, R.
   - Number of permutations: 7! = 5,040.

3. **Probability:**
   - Probability = (favorable outcomes) / (total outcomes)
   - = 5,040 / 40,320 = 1/8 = 12.5%

**Common Mistakes to Avoid:**
- Forgetting that all letters in "COMPUTER" are distinct.
- Not treating "CO" as a single unit when counting constrained arrangements.
- Calculating probability incorrectly.

**Key Insights:**
- This shows how to handle constraints that keep certain elements together.
- The probability is 1/8 because there are 8 positions for the "CO" unit, and all letters are distinct.
- Treating connected elements as a single unit is a common technique.

### Example 9.2.9 Permutations of Objects Around a Circle

At a meeting of diplomats, the six participants are to be seated around a circular table. Since the table has no ends to confer particular status, it doesn't matter who sits in which chair. But it does matter how the diplomats are seated relative to each other. In other words, two seatings are considered the same if one is a rotation of the other. How many different ways can the diplomats be seated?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of distinct circular arrangements of 6 diplomats where rotations are considered the same.

**Step-by-Step Reasoning:**

1. **Understanding Circular Arrangements:**
   - In a circle, rotations of the same arrangement are identical.
   - For n distinct objects in a circle, number of arrangements is (n-1)!.

2. **Fixing One Position:**
   - Choose one diplomat to sit in a fixed position (say, the "top" chair).
   - This eliminates the rotational symmetry.
   - Now arrange the remaining 5 diplomats in the other chairs: 5! = 120.

3. **Alternative Explanation:**
   - Total linear arrangements: 6! = 720.
   - Each circular arrangement corresponds to 6 linear arrangements (due to rotations).
   - Number of circular arrangements: 720 / 6 = 120.

**Common Mistakes to Avoid:**
- Forgetting to account for rotational symmetry.
- Using n! instead of (n-1)! for circular arrangements.
- Not understanding that fixing one position eliminates the symmetry.

**Key Insights:**
- Circular arrangements require dividing by the number of rotational symmetries.
- The formula (n-1)! is standard for distinct objects in a circle.
- This is different from arrangements where reflections are also considered the same.

## Chapter 9.3 Examples

### Example 9.3.1 Counting Passwords with Three or Fewer Letters

A computer access password consists of from one to three letters chosen from the 26 in the alphabet with repetitions allowed. How many different passwords are possible?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of passwords of length 1, 2, or 3 using letters A-Z with repetition allowed.

**Step-by-Step Reasoning:**

1. **Using the Addition Rule:**
   - The set of all passwords can be partitioned into:
     - Length 1: 26 choices
     - Length 2: 26 × 26 = 676 choices
     - Length 3: 26 × 26 × 26 = 17,576 choices

2. **Summing the Counts:**
   - 26 + 676 + 17,576 = 18,278

**Common Mistakes to Avoid:**
- Forgetting to include length 1 passwords.
- Not using the addition rule to combine the disjoint cases.
- Miscalculating the powers of 26.

**Key Insights:**
- The addition rule is perfect for counting elements in disjoint sets.
- Each length corresponds to a different number of choices.
- This shows how to handle variable-length strings.

### Example 9.3.2 Counting the Number of Integers Divisible by 5

How many three-digit integers (integers from 100 to 999 inclusive) are divisible by 5?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of three-digit integers that are divisible by 5.

**Step-by-Step Reasoning:**

1. **Using the Addition Rule:**
   - Three-digit integers divisible by 5 end in 0 or 5.
   - Set A₁: end in 0
   - Set A₂: end in 5
   - A₁ and A₂ are disjoint.

2. **Counting A₁ (ending in 0):**
   - First digit: 1-9 (9 choices)
   - Second digit: 0-9 (10 choices)
   - Third digit: 0 (1 choice)
   - Total for A₁: 9 × 10 × 1 = 90

3. **Counting A₂ (ending in 5):**
   - First digit: 1-9 (9 choices)
   - Second digit: 0-9 (10 choices)
   - Third digit: 5 (1 choice)
   - Total for A₂: 9 × 10 × 1 = 90

4. **Total:**
   - 90 + 90 = 180

**Common Mistakes to Avoid:**
- Forgetting that 100 is included (100 ÷ 5 = 20).
- Not recognizing that numbers ending in 0 or 5 are divisible by 5.
- Miscalculating the number of choices for each digit.

**Key Insights:**
- This shows an alternative method to the one in Example 9.1.4.
- The addition rule works well when the condition can be split into cases.
- Both methods (this and the earlier one) give the same answer.

### Example 9.3.3 Counting PINs with Repeated Symbols

The PINs discussed in Examples 9.2.2 and 9.2.4 are made from exactly four symbols chosen from the 26 letters of the alphabet and the ten digits, with repetitions allowed.

a. How many PINs contain repeated symbols?
b. If all PINs are equally likely, what is the probability that a randomly chosen PIN contains a repeated symbol?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count PINs with repeated symbols and find the probability of selecting such a PIN.

**Step-by-Step Reasoning:**

1. **Using the Difference Rule:**
   - Let S be all 4-symbol PINs with repetition allowed: 36⁴ = 1,679,616
   - Let A be all 4-symbol PINs with no repetition: 36 × 35 × 34 × 33 = 1,413,720
   - PINs with repeated symbols = S - A = 1,679,616 - 1,413,720 = 265,896

2. **Probability:**
   - P(PIN has repeated symbols) = 265,896 / 1,679,616 ≈ 0.1583

**Common Mistakes to Avoid:**
- Using the wrong totals for S and A.
- Forgetting that the difference rule gives the complement.
- Miscalculating the arithmetic.

**Key Insights:**
- The difference rule is efficient for counting elements not in a subset.
- About 15.8% of PINs have repeated symbols.
- This is the complement of the probability of no repeated symbols.

### Example 9.3.4 Number of Python Identifiers of Eight or Fewer Characters

In the computer language Python, identifiers must start with one of 53 symbols: either one of the 52 letters of the upper- and lower-case Roman alphabet or an underscore (_). The initial character may stand alone, or it may be followed by any number of additional characters chosen from a set of 63 symbols: the 53 symbols allowed as an initial character plus the ten digits. Certain keywords, however, such as and, if, print, and so forth, are set aside and may not be used as identifiers. In one implementation of Python there are 31 such reserved keywords, none of which has more than eight characters. How many Python identifiers are there that are less than or equal to eight characters in length?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of valid Python identifiers of length 1-8, excluding reserved keywords.

**Step-by-Step Reasoning:**

1. **Potential Identifiers (before subtracting keywords):**
   - Length 1: 53 choices
   - Length 2: 53 × 63
   - Length 3: 53 × 63²
   - ...
   - Length 8: 53 × 63⁷

2. **Summing the Series:**
   - This is a geometric series: 53 × (63⁸ - 1) / (63 - 1)
   - 63⁸ = 248,155,780,267,521
   - (63⁸ - 1) = 248,155,780,267,520
   - Divided by 62 = 4,002,511,940,604
   - Times 53 = 212,133,167,002,880

3. **Subtracting Reserved Keywords:**
   - There are 31 reserved keywords.
   - All have length ≤ 8.
   - Result: 212,133,167,002,880 - 31 = 212,133,167,002,849

**Common Mistakes to Avoid:**
- Forgetting to include length 1 identifiers.
- Miscalculating the geometric series.
- Not subtracting the reserved keywords.

**Key Insights:**
- Python allows a large number of possible identifiers.
- The formula for the sum of geometric series is essential here.
- Most of the potential identifiers are actually valid.

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

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Verify the dotted decimal conversion and count Class B networks and host IDs.

**Step-by-Step Reasoning:**

1. **Verifying the Conversion:**
   - 10001100₂ = 128 + 8 + 4 = 140
   - 11000000₂ = 128 + 64 = 192
   - 00100000₂ = 32
   - 10001000₂ = 128 + 8 = 136
   - Yes, 140.192.32.136 is correct.

2. **Counting Class B Networks:**
   - Class B: First two bits are 10.
   - Network ID: 16 bits total, but first two are fixed as 10.
   - Remaining 14 bits can be 0 or 1.
   - Number of networks: 2¹⁴ = 16,384.

3. **Class B IP Address Format:**
   - First two bits: 10 (binary) = 128-191 (decimal)
   - Next 14 bits: network ID (can vary)
   - Last 16 bits: host ID (not all 0s or all 1s)
   - Format: w.x.y.z where 128 ≤ w ≤ 191, 0 ≤ x,y,z ≤ 255

4. **Counting Class B Host IDs:**
   - 16 bits for host ID.
   - Cannot be all 0s or all 1s.
   - Total possibilities: 2¹⁶ = 65,536
   - Subtract 2: 65,536 - 2 = 65,534

**Common Mistakes to Avoid:**
- Misconverting binary to decimal.
- Forgetting that host IDs cannot be all 0s or all 1s.
- Not accounting for the fixed bits in the network ID.

**Key Insights:**
- IP addresses have a hierarchical structure.
- Class B networks are identified by the first two bits being 10.
- The restrictions on host IDs are important for network functionality.

### Example 9.3.6 Counting Elements of a General Union

a. How many integers from 1 through 1,000 are multiples of 3 or multiples of 5?
b. How many integers from 1 through 1,000 are neither multiples of 3 nor multiples of 5?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count integers from 1 to 1000 that are multiples of 3 or 5, and count those that are multiples of neither.

**Step-by-Step Reasoning:**

1. **Using Inclusion/Exclusion:**
   - Let A = multiples of 3: 333
   - Let B = multiples of 5: 200
   - A ∩ B = multiples of 15: 66
   - |A ∪ B| = |A| + |B| - |A ∩ B| = 333 + 200 - 66 = 467

2. **Counting Multiples of 3:**
   - 3 × 1 = 3, 3 × 2 = 6, ..., 3 × 333 = 999
   - Number: 333

3. **Counting Multiples of 5:**
   - 5 × 1 = 5, 5 × 2 = 10, ..., 5 × 200 = 1,000
   - Number: 200

4. **Counting Multiples of 15:**
   - 15 × 1 = 15, 15 × 2 = 30, ..., 15 × 66 = 990
   - Number: 66

5. **Neither Multiples of 3 nor 5:**
   - Total integers: 1,000
   - Multiples of 3 or 5: 467
   - Neither: 1,000 - 467 = 533

**Common Mistakes to Avoid:**
- Forgetting the inclusion/exclusion principle.
- Miscalculating the number of multiples.
- Not including 1,000 in the count if it's a multiple.

**Key Insights:**
- The inclusion/exclusion principle is essential for unions of non-disjoint sets.
- This is a classic example of counting elements satisfying "or" conditions.
- The complement can be found using the difference rule.

### Example 9.3.7 Counting the Number of Elements in an Intersection

A professor in a discrete mathematics class passes out a form asking students to check all the mathematics and computer science courses they have recently taken. The finding is that out of a total of 50 students in the class,
- 30 took precalculus;
- 16 took both precalculus and Java;
- 18 took calculus;
- 8 took both calculus and Java;
- 26 took Java;
- 47 took at least one of the three courses.
- 9 took both precalculus and calculus;

a. How many students did not take any of the three courses?
b. How many students took all three courses?
c. How many students took precalculus and calculus but not Java? How many students took precalculus but neither calculus nor Java?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Given survey data about course enrollment, find the number of students in various categories.

**Step-by-Step Reasoning:**

1. **Students Taking None of the Courses:**
   - Total students: 50
   - Students taking at least one: 47
   - Students taking none: 50 - 47 = 3

2. **Students Taking All Three Courses:**
   - Let P = precalculus (30), C = calculus (18), J = Java (26)
   - P ∩ C = 9, P ∩ J = 16, C ∩ J = 8
   - Using inclusion/exclusion for three sets:
   - |P ∪ C ∪ J| = |P| + |C| + |J| - |P ∩ C| - |P ∩ J| - |C ∩ J| + |P ∩ C ∩ J|
   - 47 = 30 + 18 + 26 - 9 - 16 - 8 + |P ∩ C ∩ J|
   - 47 = 74 - 33 + |P ∩ C ∩ J|
   - 47 = 41 + |P ∩ C ∩ J|
   - |P ∩ C ∩ J| = 6

3. **Filling in the Venn Diagram:**
   - P ∩ C ∩ J = 6
   - P ∩ C but not J = 9 - 6 = 3
   - P ∩ J but not C = 16 - 6 = 10
   - C ∩ J but not P = 8 - 6 = 2
   - P only = 30 - 3 - 10 - 6 = 11
   - C only = 18 - 3 - 2 - 6 = 7
   - J only = 26 - 10 - 2 - 6 = 8
   - None = 3
   - Total: 11 + 7 + 8 + 3 + 3 + 10 + 2 + 6 = 50 ✓

**Common Mistakes to Avoid:**
- Not using inclusion/exclusion for three sets.
- Misapplying the formula for the triple intersection.
- Forgetting to verify the total adds up correctly.

**Key Insights:**
- This shows how to work backwards from given data to find unknown quantities.
- The inclusion/exclusion principle for three sets is more complex.
- Venn diagrams are helpful for visualizing the relationships.

## Chapter 9.5 Examples

### Example 9.5.1 3-Combinations

Let S = {Ann, Bob, Cyd, Dan}. Each committee consisting of three of the four people in S is a 3-combination of S.

a. List all such 3-combinations of S.
b. What is
⎛ 4 ⎞
⎜ 3 ⎟?
⎝   ⎠

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: List all 3-element subsets of a 4-element set and compute the binomial coefficient.

**Step-by-Step Reasoning:**

1. **Listing the 3-Combinations:**
   - {Ann, Bob, Cyd, Dan}
   - Leave out Ann: {Bob, Cyd, Dan}
   - Leave out Bob: {Ann, Cyd, Dan}
   - Leave out Cyd: {Ann, Bob, Dan}
   - Leave out Dan: {Ann, Bob, Cyd}

2. **Computing the Binomial Coefficient:**
   - The formula for binomial coefficients:
   ⎛ n ⎞   n!
   ⎜ r ⎟ = ---------
   ⎝   ⎠   r!(n − r)!
   - For n=4, r=3:
   4!
   -------- = 24 / (6 × 1) = 4
   3! × 1!

**Common Mistakes to Avoid:**
- Confusing combinations with permutations (order doesn't matter).
- Forgetting that {Ann, Bob, Cyd} is the same as {Bob, Ann, Cyd}.
- Miscalculating the factorial formula.

**Key Insights:**
- This introduces combinations as subsets of a fixed size.
- The binomial coefficient formula gives the count directly.
- Each combination corresponds to leaving out one element.

### Example 9.5.2 Unordered Selections

How many unordered selections of two elements can be made from the set {0, 1, 2, 3}?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of 2-element subsets of {0, 1, 2, 3}.

**Step-by-Step Reasoning:**

1. **Systematic Listing:**
   - Subsets containing 0: {0,1}, {0,2}, {0,3}
   - Subsets containing 1 (not already listed): {1,2}, {1,3}
   - Subsets containing 2 (not already listed): {2,3}

2. **Using the Binomial Coefficient:**
   ⎛ 4 ⎞
   ⎜ 2 ⎟ = 6
   ⎝   ⎠

**Common Mistakes to Avoid:**
- Listing ordered pairs instead of unordered sets.
- Missing some combinations in the systematic listing.
- Forgetting that order doesn't matter.

**Key Insights:**
- This shows the difference between ordered and unordered selections.
- Unordered selections are combinations.
- The systematic listing method works well for small sets.

### Example 9.5.3 Relation between Permutations and Combinations

Write all 2-permutations of the set {0, 1, 2, 3}. Find an equation relating the number of 2-permutations, P(4, 2), and the number of 2-combinations,
⎛ 4 ⎞
⎜ 2 ⎟, and solve this equation for
⎛ 4 ⎞
⎜ 2 ⎟.
⎝   ⎠

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: List all 2-permutations of {0,1,2,3} and derive the relationship between P(4,2) and C(4,2).

**Step-by-Step Reasoning:**

1. **Listing 2-Permutations:**
   - 01, 02, 03, 10, 12, 13, 20, 21, 23, 30, 31, 32

2. **The Relationship:**
   - Each 2-combination can be ordered in 2! = 2 ways.
   - Number of 2-permutations = number of 2-combinations × 2!
   - P(4,2) = C(4,2) × 2

3. **Solving for C(4,2):**
   - C(4,2) = P(4,2) / 2 = 12 / 2 = 6

**Common Mistakes to Avoid:**
- Not listing all permutations systematically.
- Forgetting that each combination generates multiple permutations.
- Miscalculating P(4,2).

**Key Insights:**
- This derives the relationship between permutations and combinations.
- The general formula is P(n,r) = C(n,r) × r!
- This is the foundation for the binomial coefficient formula.

### Example 9.5.4 Calculating the Number of Teams

Consider again the problem of choosing five members from a group of twelve to work as a team on a special project. How many distinct five-person teams can be chosen?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of ways to choose 5 people out of 12 for a team.

**Step-by-Step Reasoning:**

1. **Using the Binomial Coefficient:**
   - This is C(12,5), the number of 5-combinations of 12 elements.
   - Formula:
   12!
   C(12,5) = ---------
   5!(12-5)!

2. **Calculating the Value:**
   - 12! = 479,001,600
   - 5! = 120
   - 7! = 5,040
   - C(12,5) = 479,001,600 / (120 × 5,040) = 792

3. **Alternative Calculation:**
   - 12×11×10×9×8 / (5×4×3×2×1) = 792

**Common Mistakes to Avoid:**
- Confusing with permutations (which would be 12×11×10×9×8 = 95,040).
- Miscalculating the factorials.
- Forgetting the formula.

**Key Insights:**
- This is the classic "choose k out of n" problem.
- The binomial coefficient gives the count directly.
- This is much smaller than the number of ordered selections.

### Example 9.5.5 Teams That Contain Both or Neither

Suppose two members of the group of twelve insist on working as a pair—any team must contain either both or neither. How many five-person teams can be formed?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count 5-person teams where two specific people must either both be included or both excluded.

**Step-by-Step Reasoning:**

1. **Case 1: Both Included:**
   - Choose 3 more people from the remaining 10.
   - C(10,3) = 120

2. **Case 2: Neither Included:**
   - Choose 5 people from the remaining 10.
   - C(10,5) = 252

3. **Total:**
   - 120 + 252 = 372

**Common Mistakes to Avoid:**
- Forgetting that the two people must be treated as a unit.
- Miscalculating the combinations.
- Not using the addition rule properly.

**Key Insights:**
- This shows how constraints on specific individuals affect the count.
- The two cases are disjoint, so addition rule applies.
- The constraint reduces the number of possible teams.

### Example 9.5.6 Teams That Do Not Contain Both

Suppose two members of the group don't get along and refuse to work together on a team. How many five-person teams can be formed?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count 5-person teams where two specific people cannot both be included.

**Step-by-Step Reasoning:**

1. **Case 1: Neither Included:**
   - Choose 5 from the remaining 10.
   - C(10,5) = 252

2. **Case 2: Only First Included:**
   - Choose 4 more from the remaining 10 (excluding the second).
   - C(10,4) = 210

3. **Case 3: Only Second Included:**
   - Choose 4 more from the remaining 10 (excluding the first).
   - C(10,4) = 210

4. **Total:**
   - 252 + 210 + 210 = 672

5. **Alternative Using Difference Rule:**
   - Total teams: C(12,5) = 792
   - Teams with both: C(10,3) = 120
   - Teams without both: 792 - 120 = 672

**Common Mistakes to Avoid:**
- Missing one of the cases.
- Miscalculating the combinations.
- Not considering the difference rule alternative.

**Key Insights:**
- This shows two methods to solve the same problem.
- The difference rule is often more efficient.
- The constraint excludes fewer possibilities than the previous example.

### Example 9.5.7 Teams with Members of Two Types

Suppose the group of twelve consists of five men and seven women.
a. How many five-person teams can be chosen that consist of three men and two women?
b. How many five-person teams contain at least one man?
c. How many five-person teams contain at most one man?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count teams with specific gender compositions from 5 men and 7 women.

**Step-by-Step Reasoning:**

1. **Part (a): Exactly 3 men and 2 women:**
   - Choose 3 men from 5: C(5,3)
   - Choose 2 women from 7: C(7,2)
   - Total: C(5,3) × C(7,2) = 10 × 21 = 210

2. **Part (b): At least one man:**
   - Total teams: C(12,5) = 792
   - Teams with no men: C(7,5) = 21
   - Teams with at least one man: 792 - 21 = 771

3. **Part (c): At most one man:**
   - 0 men: C(7,5) = 21
   - 1 man: C(5,1) × C(7,4) = 5 × 35 = 175
   - Total: 21 + 175 = 196

**Common Mistakes to Avoid:**
- Forgetting to multiply the combinations for mixed groups.
- Miscalculating the complement for "at least one."
- Not considering all cases for "at most one."

**Key Insights:**
- This shows how to handle mixed selections.
- The complement method is efficient for "at least" conditions.
- Addition rule works for "at most" conditions.

### Example 9.5.8 Poker Hand Problems

The game of poker is played with an ordinary deck of cards (see Example 9.1.1). Various five-card holdings are given special names, and certain holdings beat certain other holdings. The named holdings are listed from highest to lowest below.

Royal flush: 10, J, Q, K, A of the same suit
Straight flush: five adjacent denominations of the same suit but not a royal flush—aces can be high or low, so A, 2, 3, 4, 5 of the same suit is a straight flush.
Four of a kind: four cards of one denomination—the fifth card can be any other in the deck
Full house: three cards of one denomination, two cards of another denomination
Flush: five cards of the same suit but not a straight or a royal flush
Straight: five cards of adjacent denominations but not all of the same suit—aces can be high or low
Three of a kind: three cards of the same denomination and two other cards of different denominations
Two pairs: two cards of one denomination, two cards of a second denomination, and a fifth card of a third denomination
One pair: two cards of one denomination and three other cards all of different denominations
No pairs: all cards of different denominations but not a straight or straight flush or flush

a. How many five-card poker hands contain two pairs?
b. If a five-card hand is dealt at random from an ordinary deck of cards, what is the probability that the hand contains two pairs?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count poker hands with two pairs and find the probability.

**Step-by-Step Reasoning:**

1. **Counting Two Pair Hands:**
   - Step 1: Choose 2 denominations for the pairs: C(13,2)
   - Step 2: Choose 2 suits for first denomination: C(4,2)
   - Step 3: Choose 2 suits for second denomination: C(4,2)
   - Step 4: Choose 1 denomination for the remaining card: C(11,1)
   - Step 5: Choose 1 suit for the remaining card: C(4,1)

2. **Calculating the Numbers:**
   - C(13,2) = 78
   - C(4,2) = 6
   - C(4,2) = 6
   - C(11,1) = 11
   - C(4,1) = 4
   - Total: 78 × 6 × 6 × 11 × 4 = 123,552

3. **Probability:**
   - Total hands: C(52,5) = 2,598,960
   - Probability: 123,552 / 2,598,960 ≈ 0.0475

**Common Mistakes to Avoid:**
- Forgetting that the two pairs must be different denominations.
- Not accounting for the remaining card's denomination and suit.
- Miscalculating the total number of poker hands.

**Key Insights:**
- This is a complex counting problem with multiple steps.
- Poker hand probabilities require careful counting of all cases.
- The probability of two pairs is about 4.75%.

### Example 9.5.9 Number of Bit Strings with Fixed Number of 1's

How many eight-bit strings have exactly three 1's?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of 8-bit strings with exactly three 1's.

**Step-by-Step Reasoning:**

1. **Using Combinations:**
   - Choose 3 positions out of 8 for the 1's.
   - The remaining 5 positions get 0's.
   - Number: C(8,3) = 56

2. **Verification:**
   - 8! / (3! × 5!) = 40320 / (6 × 120) = 40320 / 720 = 56

**Common Mistakes to Avoid:**
- Confusing with permutations of bits.
- Forgetting that the positions of 0's are determined once 1's are placed.

**Key Insights:**
- This is equivalent to choosing positions for the 1's.
- The formula C(n,k) counts the number of ways to choose positions for k identical objects.
- This has applications in coding theory and probability.

### Example 9.5.10 Permutations of a Set with Repeated Elements

Consider various ways of ordering the letters in the word MISSISSIPPI:
IIMSSPISSIP, ISSSPMIIPIS, PIMISSSSIIP, and so on.

How many distinguishable orderings are there?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Count the number of distinct permutations of the letters in "MISSISSIPPI".

**Step-by-Step Reasoning:**

1. **Identifying the Letter Frequencies:**
   - M: 1
   - I: 4
   - S: 4
   - P: 2

2. **Using the Formula:**
   - For distinct objects: 11!
   - Divide by repetitions: 11! / (1! × 4! × 4! × 2!) = 34,650

3. **Alternative Method:**
   - Choose positions for each letter type separately.
   - C(11,1) for M, then C(10,4) for I's, then C(6,4) for S's, then C(2,2) for P's.

**Common Mistakes to Avoid:**
- Not accounting for repeated letters.
- Miscalculating the multinomial coefficient.
- Forgetting that different letters of the same type are indistinguishable.

**Key Insights:**
- The multinomial coefficient generalizes the binomial coefficient.
- This is important for counting anagrams and arrangements with repetitions.
- The formula is 11! / (1!4!4!2!) = 34,650.

### Example 9.5.11 Double Counting

Consider again the problem of Example 9.5.7(b). A group consists of five men and seven women. How many teams of five contain at least one man?

! Caution! Be careful to
avoid counting items
twice when using the
multiplication rule.

### Incorrect Solution
Imagine constructing the team as a two-step process:
Step 1: Choose a subset of one man from the five men.
Step 2: Choose a subset of four others from the remaining eleven people.

⎛ 5 ⎞⎛ 11 ⎞
Hence, by the multiplication rule, there are ⎜ 1 ⎟⎜  4 ⎟ = 1,650 five-person teams that contain at least one man.
⎝   ⎠⎝    ⎠

### Analysis of the Incorrect Solution
The problem with the solution above is that some teams are counted more than once. Suppose the men are Anwar, Ben, Carlos, Dwayne, and Ed and the women are Fumiko, Gail, Hui-Fan, Inez, Jill, Kim, and Laura. According to the method described previously, one possible outcome of the two-step process is as follows:
Outcome of step 1: Anwar
Outcome of step 2: Ben, Gail, Inez, and Jill.
In this case the team would be {Anwar, Ben, Gail, Inez, Jill}. But another possible outcome is
Outcome of step 1: Ben
Outcome of step 2: Anwar, Gail, Inez, and Jill,
which also gives the team {Anwar, Ben, Gail, Inez, Jill}. Thus this one team is given by two different branches of the possibility tree, and so it is counted twice.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Identify and explain the double counting error in the incorrect solution.

**Step-by-Step Reasoning:**

1. **The Error:**
   - The incorrect solution counts some teams multiple times.
   - When you choose 1 man in step 1 and 4 others in step 2, you might choose different men in step 1 but end up with the same team.

2. **Example of Double Counting:**
   - Team: {Anwar, Ben, Gail, Inez, Jill}
   - This team can be formed by:
     - Step 1: Choose Anwar, Step 2: Choose Ben, Gail, Inez, Jill
     - Step 1: Choose Ben, Step 2: Choose Anwar, Gail, Inez, Jill
   - Same team counted twice!

3. **The Correct Approach:**
   - Use the complement: Total teams minus teams with no men.
   - Or use addition rule properly by partitioning based on number of men.

**Common Mistakes to Avoid:**
- Not checking for double counting in multiplication rule applications.
- Assuming steps are independent when they're not.
- Not verifying with specific examples.

**Key Insights:**
- This is a cautionary example about the multiplication rule.
- Always check if the steps are truly independent.
- Double counting can lead to significant errors in counting problems.

### Example 9.5.12 Values of Stirling Numbers

Find S4,1 , S4,2 , S4,3 , and S4,4 .

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Compute the Stirling numbers of the second kind S(4,k) for k=1,2,3,4.

**Step-by-Step Reasoning:**

1. **S4,1 = 1:**
   - Only one way to partition 4 elements into 1 subset: all together.

2. **S4,4 = 1:**
   - Only one way to partition 4 elements into 4 subsets: each alone.

3. **S4,2 = 7:**
   - Partitions into 2 subsets:
   - Both subsets size 2: C(4,2) = 6 ways to choose pairs.
   - One subset size 3, one size 1: C(4,1) = 4 ways.
   - Total: 6 + 4 = 10? Wait, let me recount...

Actually, looking at the detailed explanation in the book:
- Both subsets size 2: 3 ways (choose which element is paired with which other)
- One subset size 3, one size 1: 4 ways (choose which element is alone)
- Total: 3 + 4 = 7 ✓

4. **S4,3 = 6:**
   - Partitions into 3 subsets.
   - Must have two elements in one subset, and the other two alone.
   - C(4,2) = 6 ways to choose which two go together.

**Common Mistakes to Avoid:**
- Misunderstanding what Stirling numbers count.
- Forgetting that partitions are unordered.
- Miscalculating the number of ways for each case.

**Key Insights:**
- Stirling numbers count partitions of a set into exactly k non-empty subsets.
- The values are: S4,1 = 1, S4,2 = 7, S4,3 = 6, S4,4 = 1.
- These have applications in combinatorics and probability.

### Example 9.5.13 Finding a Recurrence Relation for Sn,r

Find a recurrence relation relating Sn,r to values of the sequence with lower indices than n and r, and give initial conditions for the recursion.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Find a recurrence relation for the Stirling numbers of the second kind.

**Step-by-Step Reasoning:**

1. **The Recurrence:**
   - Consider partitions of {x1, x2, ..., xn} into r subsets.
   - These can be divided into:
     - Partitions where xn is in a subset by itself.
     - Partitions where xn is in a subset with other elements.

2. **Case 1: xn alone:**
   - Take any partition of {x1, ..., xn-1} into r-1 subsets.
   - Add {xn} as a new subset.
   - Number: S(n-1, r-1)

3. **Case 2: xn with others:**
   - Take any partition of {x1, ..., xn-1} into r subsets.
   - Add xn to one of the existing r subsets.
   - Number: r × S(n-1, r)

4. **Total:**
   - S(n,r) = S(n-1, r-1) + r × S(n-1, r)

5. **Initial Conditions:**
   - S(n,1) = 1 for n ≥ 1
   - S(n,n) = 1 for n ≥ 1

**Common Mistakes to Avoid:**
- Forgetting that partitions are into non-empty subsets.
- Misunderstanding the role of the last element.
- Not providing the initial conditions.

**Key Insights:**
- This recurrence is fundamental to Stirling numbers.
- The initial conditions are important for the recursion.
- This shows how to build up partitions systematically.

## Chapter 9.8 Examples

### Example 9.8.1 Applying the Probability Axioms

Suppose that A and B are events in a sample space S. If A and B are disjoint, could P(A) = 0.6 and P(B) = 0.8?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Determine if it's possible for disjoint events A and B to have probabilities 0.6 and 0.8 respectively.

**Step-by-Step Reasoning:**

1. **Understanding the Probability Axioms:**
   - Axiom 1: 0 ≤ P(A) ≤ 1 for any event A
   - Axiom 3: If A ∩ B = ∅, then P(A ∪ B) = P(A) + P(B)

2. **Applying the Axioms:**
   - Given A and B are disjoint: P(A ∪ B) = P(A) + P(B) = 0.6 + 0.8 = 1.4
   - But Axiom 1 requires P(A ∪ B) ≤ 1
   - Since 1.4 > 1, this violates the probability axioms.

3. **Conclusion:**
   - It's impossible for disjoint events to have probabilities 0.6 and 0.8.

**Common Mistakes to Avoid:**
- Forgetting that probabilities must be between 0 and 1.
- Not applying the axiom for disjoint events.
- Thinking that individual probabilities can be greater than 1 as long as they're less than 1.

**Key Insights:**
- This shows how the probability axioms constrain possible probability assignments.
- Disjoint events with high individual probabilities would require their union to have a probability greater than 1, which is impossible.
- The axioms ensure that probabilities are consistent and add up properly.

### Example 9.8.2 The Probability of the Complement of an Event

Suppose that A is an event in a sample space S. Deduce that P(Aᶜ) = 1 - P(A).

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Prove that the probability of the complement of event A equals 1 minus the probability of A.

**Step-by-Step Reasoning:**

1. **Using Set Theory Properties:**
   - A ∪ Aᶜ = S (universal set)
   - A ∩ Aᶜ = ∅ (empty set)
   - These are mutually disjoint.

2. **Applying Probability Axioms:**
   - Axiom 3: P(A ∪ Aᶜ) = P(A) + P(Aᶜ) = P(S)
   - Axiom 2: P(S) = 1
   - Therefore: P(A) + P(Aᶜ) = 1

3. **Solving for P(Aᶜ):**
   - P(Aᶜ) = 1 - P(A)

**Common Mistakes to Avoid:**
- Forgetting that A and Aᶜ are disjoint and their union is S.
- Not using the correct axioms in the right order.
- Confusing complement with intersection.

**Key Insights:**
- This is one of the most fundamental probability formulas.
- The complement rule is used constantly in probability calculations.
- It follows directly from the basic axioms and set theory.

### Example 9.8.3 The Probability of a General Union of Two Events

Follow the steps outlined in parts (a) and (b) below to prove the following formula:

**Theorem 9.8.2: Probability of a General Union of Two Events**
If S is any sample space and A and B are any events in S, then:
**P(A ∪ B) = P(A) + P(B) - P(A ∩ B)**

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Prove the inclusion/exclusion formula for the probability of the union of two events.

**Step-by-Step Reasoning:**

1. **Part (a): Show that A ∪ B is a disjoint union:**
   - A ∪ B consists of elements in A but not B, elements in B but not A, and elements in both A and B.
   - These three sets are mutually disjoint:
     - A - (A ∩ B)
     - B - (A ∩ B)
     - A ∩ B

2. **Part (b): Apply the addition rule:**
   - P(A ∪ B) = P(A - (A ∩ B)) + P(B - (A ∩ B)) + P(A ∩ B)
   - P(A - (A ∩ B)) = P(A) - P(A ∩ B)  [since A ∩ B ⊆ A]
   - P(B - (A ∩ B)) = P(B) - P(A ∩ B)  [since A ∩ B ⊆ B]
   - Therefore: P(A ∪ B) = [P(A) - P(A ∩ B)] + [P(B) - P(A ∩ B)] + P(A ∩ B)
   - Simplifying: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Common Mistakes to Avoid:**
- Forgetting to account for the overlap when adding probabilities.
- Not properly decomposing the union into disjoint parts.
- Misapplying the set difference operations.

**Key Insights:**
- This is the inclusion/exclusion principle for probabilities.
- It's essential for calculating probabilities of "or" events that are not disjoint.
- The formula accounts for double-counting the intersection.

### Example 9.8.4 Computing the Probability of a General Union of Two Events

Suppose a card is chosen at random from an ordinary 52-card deck. What is the probability that the card is a face card (jack, queen, or king) or is from one of the red suits (hearts or diamonds)?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Calculate the probability of drawing a face card or a red card from a standard deck.

**Step-by-Step Reasoning:**

1. **Defining Events:**
   - Let A = event of drawing a face card (12 cards: 4 suits × 3 face cards each)
   - Let B = event of drawing a red card (26 cards: hearts and diamonds)
   - We want P(A ∪ B)

2. **Calculating Individual Probabilities:**
   - P(A) = 12/52 = 3/13
   - P(B) = 26/52 = 1/2
   - P(A ∩ B) = 6/52 = 3/26 (red face cards: hearts and diamonds jacks, queens, kings)

3. **Applying the Union Formula:**
   - P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
   - = 3/13 + 1/2 - 3/26
   - = 6/26 + 13/26 - 3/26
   - = 16/26 = 8/13 ≈ 61.5%

**Common Mistakes to Avoid:**
- Forgetting to subtract the intersection to avoid double-counting.
- Miscalculating the number of red face cards.
- Not converting fractions to common denominators.

**Key Insights:**
- This demonstrates the practical application of the union formula.
- About 61.5% of cards are either face cards or red cards.
- The formula correctly accounts for the 6 red face cards that would be double-counted.

### Example 9.8.5 Expected Value of a Lottery

Suppose that 500,000 people pay $5 each to play a lottery game with the following prizes: a grand prize of $1,000,000, 10 second prizes of $1,000 each, 1,000 third prizes of $500 each, and 10,000 fourth prizes of $10 each. What is the expected value of a ticket?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Calculate the expected value of playing this lottery game.

**Step-by-Step Reasoning:**

1. **Understanding Expected Value:**
   - E = Σ (outcome × probability)
   - For each ticket, the outcomes are the possible net gains.

2. **Calculating Net Gains:**
   - Grand prize: $1,000,000 - $5 = $999,995
   - Second prize: $1,000 - $5 = $995
   - Third prize: $500 - $5 = $495
   - Fourth prize: $10 - $5 = $5
   - No prize: -$5

3. **Calculating Probabilities:**
   - Each of 500,000 tickets has equal probability: 1/500,000

4. **Computing Expected Value:**
   - E = (1/500,000) × [999,995 + 10×995 + 1,000×495 + 10,000×5 + 488,989×(-5)]
   - E = (1/500,000) × [999,995 + 9,950 + 495,000 + 50,000 - 2,444,945]
   - E = (1/500,000) × [-890,000]
   - E = -$1.78

**Common Mistakes to Avoid:**
- Forgetting to subtract the $5 cost from all prizes.
- Miscalculating the number of non-winning tickets.
- Not using the correct formula for expected value.

**Key Insights:**
- The expected value is negative, showing the lottery is not a good investment.
- This is typical of lotteries - they are designed to make money for the organizers.
- The calculation shows the average loss per ticket is $1.78.

### Example 9.8.6 Gambler's Ruin

A gambler repeatedly bets $1 that a coin will come up heads when tossed. Each time the coin comes up heads, the gambler wins $1; each time it comes up tails, he loses $1. The gambler will quit playing either when he is ruined (loses all his money) or when he has $M (where M is a positive number he has decided in advance). Let Pₙ be the probability that the gambler is ruined if he begins playing with $n. Then if the coin is fair (has an equal chance of coming up heads or tails),
Pₖ₋₁ = (1/2)Pₖ + (1/2)Pₖ₋₂ for each integer k with 2 ≤ k ≤ M.

(This follows from the fact that if the gambler has $(k - 1), then he has an equal chance of winning $1 or losing $1, and if he wins $1, then his chance of being ruined is Pₖ, whereas if he loses $1, then his chance of being ruined is Pₖ₋₂.) Also P₀ = 1 (because if he has $0, he is certain of being ruined) and Pₘ = 0 (because once he has $M, he quits and so stands no chance of being ruined). Find an explicit formula for Pₙ. How should the gambler choose M to minimize his chance of being ruined?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Solve the gambler's ruin problem with a fair coin to find the probability of ruin starting with n dollars.

**Step-by-Step Reasoning:**

1. **The Recurrence Relation:**
   - For a fair coin, each game is equally likely to go up or down by $1.
   - The recurrence: Pₖ₋₁ = (1/2)Pₖ + (1/2)Pₖ₋₂

2. **Solving the Recurrence:**
   - Multiply by 2: 2Pₖ₋₁ = Pₖ + Pₖ₋₂
   - Rearrange: Pₖ = 2Pₖ₋₁ - Pₖ₋₂
   - This is a linear homogeneous recurrence relation.

3. **Characteristic Equation:**
   - t² - 2t + 1 = 0
   - (t - 1)² = 0
   - Root: t = 1 (double root)

4. **General Solution:**
   - For double root: Pₖ = C + Dk

5. **Boundary Conditions:**
   - P₀ = 1 = C + D×0 ⇒ C = 1
   - Pₘ = 0 = C + D×M = 1 + D×M ⇒ D = -1/M

6. **Final Formula:**
   - Pₙ = 1 - (1/M)n = (M - n)/M

7. **Minimizing Ruin Probability:**
   - Pₙ = (M - n)/M = 1 - n/M
   - To minimize Pₙ, maximize M (relative to n).
   - The larger the target M compared to starting n, the more likely ruin becomes.

**Common Mistakes to Avoid:**
- Forgetting the boundary conditions.
- Misapplying the solution method for recurrence relations.
- Not recognizing this as a gambler's ruin problem.

**Key Insights:**
- The probability of ruin increases as the target amount M increases relative to the starting amount n.
- This is counterintuitive - setting a higher goal actually increases the chance of going broke.
- The formula Pₙ = (M - n)/M shows this clearly.

## Chapter 9.9 Examples

### Example 9.9.1 Computing a Conditional Probability

A pair of fair dice, one blue and the other gray, are rolled. What is the probability that the sum of the numbers showing face up is 8, given that both of the numbers are even?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Find the conditional probability that the sum is 8 given that both dice show even numbers.

**Step-by-Step Reasoning:**

1. **Defining Events:**
   - Let A = both numbers even: {22, 24, 26, 42, 44, 46, 62, 64, 66}
   - Let B = sum is 8: {26, 35, 44, 53, 62}
   - A ∩ B = {26, 44, 62}

2. **Calculating Probabilities:**
   - P(A) = 9/36 = 1/4
   - P(A ∩ B) = 3/36 = 1/12
   - P(B | A) = P(A ∩ B) / P(A) = (1/12) / (1/4) = (1/12) × (4/1) = 1/3

**Common Mistakes to Avoid:**
- Confusing conditional probability with joint probability.
- Not calculating the intersection correctly.
- Forgetting that the dice are distinguishable.

**Key Insights:**
- This is the definition of conditional probability in action.
- The condition "both even" reduces the sample space to 9 outcomes.
- Of those 9, 3 sum to 8, so the probability is 1/3.

### Example 9.9.2 Representing Conditional Probabilities with a Tree Diagram

An urn contains 5 blue and 7 gray balls. Let us say that 2 are chosen at random, one after the other, without replacement.

a. Find the following probabilities and illustrate them with a tree diagram: the probability that both balls are blue, the probability that the first ball is blue and the second is not blue, the probability that the first ball is not blue and the second ball is blue, and the probability that neither ball is blue.
b. What is the probability that the second ball is blue?
c. What is the probability that at least one of the balls is blue?
d. If the experiment of choosing two balls from the urn were repeated many times over, what would be the expected value of the number of blue balls?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Calculate various probabilities for drawing two balls without replacement and find the expected value.

**Step-by-Step Reasoning:**

1. **Part (a): Individual Probabilities:**
   - P(first blue) = 5/12
   - P(second blue | first blue) = 4/11
   - P(second not blue | first blue) = 7/11
   - P(first not blue) = 7/12
   - P(second blue | first not blue) = 5/11
   - P(second not blue | first not blue) = 6/11

2. **Using Conditional Probability Formula:**
   - P(both blue) = (5/12) × (4/11) = 20/132
   - P(first blue, second not) = (5/12) × (7/11) = 35/132
   - P(first not blue, second blue) = (7/12) × (5/11) = 35/132
   - P(neither blue) = (7/12) × (6/11) = 42/132

3. **Part (b): Probability second is blue:**
   - P(second blue) = P(second blue | first blue) × P(first blue) + P(second blue | first not blue) × P(first not blue)
   - = (4/11)(5/12) + (5/11)(7/12) = 20/132 + 35/132 = 55/132 = 5/12

4. **Part (c): At least one blue:**
   - P(at least one blue) = 1 - P(neither blue) = 1 - 42/132 = 90/132 = 15/22

5. **Part (d): Expected value:**
   - P(0 blue) = 42/132 = 7/22
   - P(1 blue) = 35/132 + 35/132 = 70/132
   - P(2 blue) = 20/132
   - E = 0×(7/22) + 1×(70/132) + 2×(20/132) = 110/132 ≈ 0.833

**Common Mistakes to Avoid:**
- Forgetting that probabilities change after the first draw.
- Not using the conditional probability formula correctly.
- Miscalculating the expected value.

**Key Insights:**
- This shows how probabilities change with sequential draws without replacement.
- Tree diagrams are useful for visualizing conditional probabilities.
- The expected value calculation shows the average number of blue balls.

### Example 9.9.3 Applying Bayes' Theorem

Most medical tests occasionally produce incorrect results, called false positives and false negatives. When a test is designed to determine whether a patient has a certain disease, a false positive result indicates that a patient has the disease when the patient does not have it. A false negative result indicates that a patient does not have the disease when the patient does have it.

When large-scale health screenings are performed for diseases with relatively low incidence, those who develop the screening procedures have to balance several considerations: the per-person cost of the screening, follow-up costs for further testing of false positives, and the possibility that people who have the disease will develop unwarranted confidence in the state of their health.

Consider a medical test that screens for a disease found in 5 people in 1,000. Suppose that the false positive rate is 3% and the false negative rate is 1%. Then 99% of the time a person who has the condition tests positive for it, and 97% of the time a person who does not have the condition tests negative for it.

a. What is the probability that a randomly chosen person who tests positive for the disease actually has the disease?
b. What is the probability that a randomly chosen person who tests negative for the disease does not indeed have the disease?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Use Bayes' theorem to find the probability that a positive test result indicates actual disease, and the probability that a negative test result means no disease.

**Step-by-Step Reasoning:**

1. **Defining Events:**
   - Let B₁ = has disease: P(B₁) = 0.005
   - Let B₂ = no disease: P(B₂) = 0.995
   - Let A = tests positive: P(A | B₁) = 0.99, P(A | B₂) = 0.03
   - Let Aᶜ = tests negative: P(Aᶜ | B₁) = 0.01, P(Aᶜ | B₂) = 0.97

2. **Part (a): Bayes' Theorem for positive test:**
   - P(B₁ | A) = P(A | B₁)P(B₁) / [P(A | B₁)P(B₁) + P(A | B₂)P(B₂)]
   - = (0.99)(0.005) / [(0.99)(0.005) + (0.03)(0.995)]
   - = 0.00495 / (0.00495 + 0.02985) = 0.00495 / 0.0348 ≈ 0.1422 ≈ 14.2%

3. **Part (b): Bayes' Theorem for negative test:**
   - P(B₂ | Aᶜ) = P(Aᶜ | B₂)P(B₂) / [P(Aᶜ | B₁)P(B₁) + P(Aᶜ | B₂)P(B₂)]
   - = (0.97)(0.995) / [(0.01)(0.005) + (0.97)(0.995)]
   - = 0.96515 / (0.00005 + 0.96515) = 0.96515 / 0.9652 ≈ 0.99995 ≈ 99.995%

**Common Mistakes to Avoid:**
- Misapplying Bayes' theorem formula.
- Forgetting to include both terms in the denominator.
- Miscalculating the conditional probabilities.

**Key Insights:**
- Even with a good test (99% sensitivity), the probability of actually having the disease given a positive test is only about 14% when the disease is rare.
- This is a classic example of how base rates affect conditional probabilities.
- The negative test result is very reliable (99.995%) for confirming no disease.

### Example 9.9.4 Disjoint Events and Independence

Let A and B be events in a sample space S, and suppose A ∩ B = ∅, P(A) ≠ 0, and P(B) ≠ 0. Show that P(A ∩ B) ≠ P(A) · P(B).

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Prove that disjoint events with positive probabilities cannot be independent.

**Step-by-Step Reasoning:**

1. **Given Information:**
   - A ∩ B = ∅
   - P(A) > 0
   - P(B) > 0

2. **Independence Definition:**
   - A and B are independent if P(A ∩ B) = P(A) · P(B)

3. **Using the Given Information:**
   - Since A ∩ B = ∅, by Axiom 2: P(A ∩ B) = 0
   - But P(A) · P(B) > 0 (since both probabilities are positive)
   - Therefore: 0 ≠ P(A) · P(B)

**Common Mistakes to Avoid:**
- Confusing disjoint with independent.
- Forgetting that disjoint events have empty intersection.
- Not using the probability axioms properly.

**Key Insights:**
- Disjoint events with positive probability cannot be independent.
- This is a fundamental distinction in probability theory.
- Independence is about probabilistic dependence, not set intersection.

### Example 9.9.5 The Probability of A ∩ Bᶜ When A and B Are Independent Events

Suppose A and B are independent events in a sample space S. Show that A and Bᶜ are also independent.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Prove that if A and B are independent, then A and the complement of B are also independent.

**Step-by-Step Reasoning:**

1. **Set Theory Properties:**
   - A ∩ Bᶜ = A - (A ∩ B)
   - P(A ∩ Bᶜ) = P(A) - P(A ∩ B)

2. **Using Independence:**
   - P(A ∩ B) = P(A) · P(B)
   - Therefore: P(A ∩ Bᶜ) = P(A) - P(A) · P(B) = P(A)(1 - P(B)) = P(A) · P(Bᶜ)

**Common Mistakes to Avoid:**
- Not using the complement formula correctly.
- Forgetting that P(Bᶜ) = 1 - P(B).
- Not recognizing this follows from the independence of A and B.

**Key Insights:**
- Independence of A and B implies independence of A and Bᶜ.
- This extends to other combinations of events and their complements.
- The proof uses basic set theory and the complement formula.

### Example 9.9.6 Computing Probabilities of Intersections of Two Independent Events

A coin is loaded so that the probability of heads is 0.6. Suppose the coin is tossed twice. Although the probability of heads is greater than the probability of tails, there is no reason to believe that whether the coin lands heads or tails on one toss will affect whether it lands heads or tails on the other toss. Thus it is reasonable to assume that the results of the tosses are independent.

a. What is the probability of obtaining two heads?
b. What is the probability of obtaining one head?
c. What is the probability of obtaining no heads?
d. What is the probability of obtaining at least one head?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Calculate probabilities for tossing a loaded coin twice, assuming independence.

**Step-by-Step Reasoning:**

1. **Defining Events:**
   - Let E = heads on first toss: P(E) = 0.6
   - Let F = heads on second toss: P(F) = 0.6
   - Assume E and F are independent.

2. **Part (a): Two heads:**
   - P(two heads) = P(E ∩ F) = P(E) · P(F) = 0.6 × 0.6 = 0.36

3. **Part (b): One head:**
   - P(one head) = P((E ∩ Fᶜ) ∪ (Eᶜ ∩ F))
   - P(E ∩ Fᶜ) = P(E) · P(Fᶜ) = 0.6 × 0.4 = 0.24
   - P(Eᶜ ∩ F) = P(Eᶜ) · P(F) = 0.4 × 0.6 = 0.24
   - Total: 0.24 + 0.24 = 0.48

4. **Part (c): No heads:**
   - P(no heads) = P(Eᶜ ∩ Fᶜ) = P(Eᶜ) · P(Fᶜ) = 0.4 × 0.4 = 0.16

5. **Part (d): At least one head:**
   - P(at least one head) = 1 - P(no heads) = 1 - 0.16 = 0.84
   - Or: P(one head) + P(two heads) = 0.48 + 0.36 = 0.84

**Common Mistakes to Avoid:**
- Forgetting that independence applies to complements too.
- Not calculating all the cases for one head.
- Misapplying the complement for the "at least one" case.

**Key Insights:**
- Independence allows us to multiply probabilities directly.
- The complement method is often the easiest for "at least one" probabilities.
- The probabilities should sum to 1: 0.36 + 0.48 + 0.16 = 1.00 ✓

### Example 9.9.7 Expected Value of Tossing a Loaded Coin Twice

Suppose that a coin is loaded so that the probability of heads is 0.6, and suppose the coin is tossed twice. If this experiment is repeated many times, what is the expected value of the number of heads?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Find the expected number of heads when tossing a loaded coin twice.

**Step-by-Step Reasoning:**

1. **Using Results from Previous Example:**
   - P(0 heads) = 0.16
   - P(1 head) = 0.48
   - P(2 heads) = 0.36

2. **Expected Value Formula:**
   - E = Σ (value × probability)
   - E = 0 × 0.16 + 1 × 0.48 + 2 × 0.36
   - E = 0 + 0.48 + 0.72 = 1.2

**Common Mistakes to Avoid:**
- Forgetting to multiply each value by its probability.
- Misusing the probabilities from the previous example.

**Key Insights:**
- The expected value is the long-run average outcome.
- For a loaded coin with P(heads) = 0.6, the expected number of heads in two tosses is 1.2.
- This makes sense since 0.6 × 2 = 1.2.

### Example 9.9.8 Exploring Independence for Three Events

Suppose that a fair coin is tossed twice. Let A be the event that a head is obtained on the first toss, and let B be the event that a head is obtained on the second toss, and C the event that either two heads or two tails are obtained. Show that A, B, and C are pairwise independent but do not satisfy the condition P(A ∩ B ∩ C) = P(A) · P(B) · P(C).

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Show that pairwise independence does not imply mutual independence for three events.

**Step-by-Step Reasoning:**

1. **Defining Events:**
   - Sample space: {HH, HT, TH, TT} (each with probability 1/4)
   - A = {HH, HT} (heads on first)
   - B = {HH, TH} (heads on second)
   - C = {HH, TT} (both same)

2. **Checking Pairwise Independence:**
   - P(A) = 2/4 = 1/2
   - P(B) = 2/4 = 1/2
   - P(C) = 2/4 = 1/2
   - P(A ∩ B) = P({HH}) = 1/4 = (1/2)(1/2) ✓
   - P(A ∩ C) = P({HH}) = 1/4 = (1/2)(1/2) ✓
   - P(B ∩ C) = P({HH}) = 1/4 = (1/2)(1/2) ✓

3. **Checking Mutual Independence:**
   - P(A ∩ B ∩ C) = P({HH}) = 1/4
   - P(A) · P(B) · P(C) = (1/2)³ = 1/8
   - 1/4 ≠ 1/8

**Common Mistakes to Avoid:**
- Confusing pairwise independence with mutual independence.
- Miscalculating the intersection probabilities.
- Forgetting that all three pairwise conditions must be checked.

**Key Insights:**
- Pairwise independence doesn't guarantee mutual independence.
- This is why the definition of mutual independence requires checking all possible intersections.
- The example shows the difference between these concepts.

### Example 9.9.9 Tossing a Loaded Coin Ten Times

A coin is loaded so that the probability of heads is 0.6 (and thus the probability of tails is 0.4). Suppose the coin is tossed ten times. As in Example 9.9.6, it is reasonable to assume that the results of the tosses are mutually independent.

a. What is the probability of obtaining eight heads?
b. What is the probability of obtaining at least eight heads?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Calculate binomial probabilities for obtaining eight or more heads in ten tosses of a loaded coin.

**Step-by-Step Reasoning:**

1. **Part (a): Exactly eight heads:**
   - This is a binomial probability: C(10,8) × (0.6)⁸ × (0.4)²
   - C(10,8) = 45
   - 45 × (0.6)⁸ × (0.4)² ≈ 45 × 0.016796 × 0.16 ≈ 45 × 0.002688 = 0.12096 ≈ 12.1%

2. **Part (b): At least eight heads:**
   - P(8) + P(9) + P(10)
   - P(8) = 45 × (0.6)⁸ × (0.4)²
   - P(9) = 10 × (0.6)⁹ × (0.4)¹
   - P(10) = 1 × (0.6)¹⁰ × (0.4)⁰
   - Total ≈ 0.121 + 0.040 + 0.006 = 0.167 ≈ 16.7%

**Common Mistakes to Avoid:**
- Forgetting to use the binomial coefficients.
- Miscalculating the powers of 0.6 and 0.4.
- Not summing all the terms for "at least eight."

**Key Insights:**
- This is an application of the binomial probability formula.
- The binomial coefficients count the number of ways to get exactly k successes.
- The probability decreases as we get more extreme outcomes.
