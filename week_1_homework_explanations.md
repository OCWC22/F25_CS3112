# CS3112 Homework Solutions - Weeks 1-2
## Detailed Explanations for Understanding

This document provides step-by-step explanations for all homework problems, breaking down complex mathematical concepts into understandable parts for learners at all levels.

---

## Chapter 5.1: Sequences and Summations

### Example 5.1.1: Finding Terms of Sequences Given by Explicit Formulas

**Problem Statement:** Define sequences a₁, a₂, a₃, . . . and b₂, b₃, b₄, . . . by the following explicit formulas:
- aₖ = k/(k+1) for all integers k ≥ 1
- bᵢ = (i-1)/i for all integers i ≥ 2
Compute the first five terms of both sequences.

**Formal Restatement:** Compute the first five terms of sequences aₖ and bᵢ defined by the given explicit formulas.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Compute the first five terms of sequences a sub k and b sub i defined by the given explicit formulas."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Compute":** This means to calculate or figure out the values.
  - **"the first five terms":** We need to find the first five values in each sequence.
  - **"of sequences a sub k and b sub i":** We're dealing with two different sequences, one starting with subscript 1 and one starting with subscript 2.
  -**"defined by the given explicit formulas":** Each sequence has a formula that tells us how to calculate each term based on its position number.
- **Putting it all together in plain English:** This is asking us to calculate the first five numbers in each of two sequences using the formulas provided.
- **Why do we use this fancy notation?** It gives us precise formulas to work with so we can systematically calculate each term.
- **Assumptions and considerations:** We need to understand what explicit formulas are and how to substitute values into them. The thought process is: For each position k or i, plug the number into the formula and calculate the result.

**Step-by-Step Solution:**

For sequence aₖ = k/(k+1):
- When k = 1: a₁ = 1/(1+1) = 1/2
- When k = 2: a₂ = 2/(2+1) = 2/3
- When k = 3: a₃ = 3/(3+1) = 3/4
- When k = 4: a₄ = 4/(4+1) = 4/5
- When k = 5: a₅ = 5/(5+1) = 5/6

For sequence bᵢ = (i-1)/i:
- When i = 2: b₂ = (2-1)/2 = 1/2
- When i = 3: b₃ = (3-1)/3 = 2/3
- When i = 4: b₄ = (4-1)/4 = 3/4
- When i = 5: b₅ = (5-1)/5 = 4/5
- When i = 6: b₆ = (6-1)/6 = 5/6

**Final Answer:**
- First five terms of aₖ: 1/2, 2/3, 3/4, 4/5, 5/6
- First five terms of bᵢ: 1/2, 2/3, 3/4, 4/5, 5/6

---

## Chapter 5.1: Homework Problems

### Problem 1: Write the first four terms of the sequences defined in 1-6.

#### Problem 1a: aₖ = 10 + k, for all integers k ≥ 1

**Formal Restatement:** Compute the first four terms of the sequence aₖ where each term is 10 plus its position number.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"aₖ = 10 + k":** The k-th term of the sequence equals 10 plus k
- **"for all integers k ≥ 1":** We start counting from position 1
- **"first four terms":** We need to calculate terms for positions 1, 2, 3, and 4

**Step-by-Step Solution:**
- When k = 1: a₁ = 10 + 1 = 11
- When k = 2: a₂ = 10 + 2 = 12
- When k = 3: a₃ = 10 + 3 = 13
- When k = 4: a₄ = 10 + 4 = 14

**Final Answer:** The first four terms are: 11, 12, 13, 14.

#### Problem 1b: bⱼ = (5-j)/(5+j), for all integers j ≥ 1

**Formal Restatement:** Compute the first four terms of the sequence bⱼ where each term is (5 minus j) divided by (5 plus j).

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"bⱼ = (5-j)/(5+j)":** The j-th term is a fraction where the numerator is 5-j and the denominator is 5+j
- **"for all integers j ≥ 1":** We start counting from position 1
- **"first four terms":** We need to calculate terms for positions 1, 2, 3, and 4

**Step-by-Step Solution:**
- When j = 1: b₁ = (5-1)/(5+1) = 4/6 = 2/3
- When j = 2: b₂ = (5-2)/(5+2) = 3/7
- When j = 3: b₃ = (5-3)/(5+3) = 2/8 = 1/4
- When j = 4: b₄ = (5-4)/(5+4) = 1/9

**Final Answer:** The first four terms are: 2/3, 3/7, 1/4, 1/9.

#### Problem 1c: cᵢ = (-1)ⁱ/(3·i), for all integers i ≥ 1

**Formal Restatement:** Compute the first four terms of the sequence cᵢ where each term is (-1) raised to the i-th power, divided by (3 times i).

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"cᵢ = (-1)ⁱ/(3·i)":** The i-th term alternates in sign (due to (-1)ⁱ) and gets smaller as i increases
- **"(-1)ⁱ":** This means the sign alternates: positive for even i, negative for odd i
- **"for all integers i ≥ 1":** We start counting from position 1
- **"first four terms":** We need to calculate terms for positions 1, 2, 3, and 4

**Step-by-Step Solution:**
- When i = 1: c₁ = (-1)¹/(3·1) = -1/3
- When i = 2: c₂ = (-1)²/(3·2) = 1/6
- When i = 3: c₃ = (-1)³/(3·3) = -1/9
- When i = 4: c₄ = (-1)⁴/(3·4) = 1/12

**Final Answer:** The first four terms are: -1/3, 1/6, -1/9, 1/12.

---

## Chapter 5.2: Mathematical Induction

### Example 5.2.1: Proving a Property Using Mathematical Induction

**Problem Statement:** Use mathematical induction to show that any amount of money of at least 14¢ can be made up using 3¢ and 8¢ coins.

**Formal Restatement:** Prove that for all integers n ≥ 14, there exist non-negative integers a and b such that n = 3a + 8b.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Use mathematical induction":** We need to use a specific proof technique that works like climbing a ladder
- **"any amount of money of at least 14¢":** We're focusing on amounts starting from 14 cents and going up
- **"can be made up using 3¢ and 8¢ coins":** We need to show how to combine these coin values to make each amount
- **"for all integers n ≥ 14":** This is our domain - we need to prove it for every integer from 14 upwards

**Step-by-Step Solution:**

**Step 1: Understand what mathematical induction is**
Mathematical induction is a proof technique that works like this:
1. **Base Case:** Show the statement is true for the first value (in this case, n = 14)
2. **Inductive Step:** Show that IF the statement is true for some value k, THEN it must also be true for k+1
3. **Conclusion:** Since we can start at the base and keep going one step at a time, the statement must be true for all values

**Step 2: Set up the proof formally**
Let P(n) be the statement: "n cents can be made using 3¢ and 8¢ coins."

We need to prove P(n) is true for all integers n ≥ 14.

**Step 3: Base Case (n = 14)**
We must show that 14¢ can be made using 3¢ and 8¢ coins.

**How to think about this:**
We need to find non-negative integers a and b such that 14 = 3a + 8b.

Let's try different values:
- If b = 0: 14 = 3a + 0, so a = 14/3 ≈ 4.67 (not an integer)
- If b = 1: 14 = 3a + 8, so 3a = 6, so a = 2 ✓

Therefore: 14 = 3(2) + 8(1) = 6 + 8 = 14

**Step 4: Inductive Step**
We must show that for any integer k ≥ 14, IF k cents can be made using 3¢ and 8¢ coins, THEN k+1 cents can also be made.

**How to think about this:**
We're assuming that k cents can be made (this is our "inductive hypothesis"), and we need to show how to make k+1 cents.

There are two cases based on how the k cents are made:

**Case 1: The combination for k cents includes at least one 8¢ coin**
- If we have at least one 8¢ coin in the combination for k cents
- We can replace one 8¢ coin with three 3¢ coins
- This changes the total by: -8 + 3(3) = -8 + 9 = +1 cent
- So if k cents can be made with at least one 8¢ coin, then k+1 cents can be made

**Case 2: The combination for k cents uses no 8¢ coins**
- If k cents are made only with 3¢ coins, then k = 3m for some integer m
- Since k ≥ 14, we must have 3m ≥ 14, so m ≥ 5 (because 3×4 = 12 < 14)
- This means we have at least five 3¢ coins
- We can replace five 3¢ coins with two 8¢ coins
- This changes the total by: -5(3) + 2(8) = -15 + 16 = +1 cent
- So if k cents can be made with only 3¢ coins, then k+1 cents can be made

**Step 5: Conclusion**
Since we've shown:
1. **Base Case:** 14¢ can be made (with two 3¢ coins and one 8¢ coin)
2. **Inductive Step:** For any k ≥ 14, if k¢ can be made, then k+1¢ can be made

By the principle of mathematical induction, any amount of money of at least 14¢ can be made using 3¢ and 8¢ coins.

---

## Chapter 5.2: Homework Problems

### Problem 1: Use mathematical induction to show that any amount of money of at least 14¢ can be made up using 3¢ and 8¢ coins.

**Formal Restatement:** Prove that for all integers n ≥ 14, there exist non-negative integers a and b such that n = 3a + 8b.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Use mathematical induction":** We need to use a proof technique that works like climbing a ladder
- **"any amount of money of at least 14¢":** We're focusing on amounts starting from 14 cents and going up
- **"can be made up using 3¢ and 8¢ coins":** We need to show how to combine these coin values to make each amount
- **"for all integers n ≥ 14":** This is our domain - we need to prove it for every integer from 14 upwards

**Step-by-Step Solution:**

Let P(n) be the statement: "n cents can be made using 3¢ and 8¢ coins."

**Step 1: Base Case (n = 14)**
We must show that P(14) is true.
14¢ can be made with two 3¢ coins and one 8¢ coin: 2 × 3 + 1 × 8 = 6 + 8 = 14.
Thus, the basis step is true.

**Step 2: Inductive Step**
1. **Inductive Hypothesis:** Suppose that for some integer k ≥ 14, P(k) is true. That is, k cents can be made using 3¢ and 8¢ coins.

2. **Goal:** We must show that P(k+1) is true. That is, k+1 cents can be made using 3¢ and 8¢ coins.

3. **Proof:**
   Starting with the k cents from the inductive hypothesis, we consider two cases for how the k cents are formed:

   *   **Case 1: The combination for k cents includes at least one 8¢ coin**
       To make k+1 cents, we can replace one 8¢ coin with three 3¢ coins. This changes the total value by: -8 + 3 × 3 = -8 + 9 = +1 cent.
       So, if k cents can be made with at least one 8¢ coin, k+1 cents can also be made.

   *   **Case 2: The combination for k cents uses no 8¢ coins**
       In this case, the k cents must be made up entirely of 3¢ coins. So, k = 3m for some integer m.
       Since we know k ≥ 14, it must be that 3m ≥ 14, which means m ≥ 14/3, so m must be at least 5.
       This means there are at least five 3¢ coins in the combination for k.
       To make k+1 cents, we can replace five 3¢ coins (15¢) with two 8¢ coins (16¢). This changes the total value by: -5 × 3 + 2 × 8 = -15 + 16 = +1 cent.
       So, if k cents can be made with only 3¢ coins, k+1 cents can also be made.

Since both possible cases lead to the conclusion that k+1 cents can be formed, the inductive step is true.

**Step 3: Conclusion**
Because the basis step and the inductive step have been proved, by the principle of mathematical induction, the statement is true for all integers n ≥ 14.

---

## Chapter 5.6: Recursively Defined Sequences

### Example 5.6.1: Finding Terms of Recursively Defined Sequences

**Problem Statement:** Find the first four terms of each of the recursively defined sequences in 1-8.

**Formal Restatement:** For each recursively defined sequence, compute the first four terms by applying the recurrence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Recursively defined sequences":** These are sequences where each term is defined based on previous terms
- **"Find the first four terms":** We need to calculate the values for positions 1, 2, 3, and 4
- **"Apply the recurrence relation":** We use the given formula that relates each term to previous terms

**Step-by-Step Solution for Problem 1:**

**Problem 1a: aₖ = 2aₖ₋₁ + k, for all integers k ≥ 2, a₁ = 1**

**How to understand this recurrence:**
- **"aₖ = 2aₖ₋₁ + k":** Each term is twice the previous term plus the position number
- **"for all integers k ≥ 2":** This rule applies starting from the second term
- **"a₁ = 1":** This is our starting value (the base case)

**Step-by-Step Calculation:**
- a₁ = 1 (given)
- a₂ = 2 × a₁ + 2 = 2 × 1 + 2 = 2 + 2 = 4
- a₃ = 2 × a₂ + 3 = 2 × 4 + 3 = 8 + 3 = 11
- a₄ = 2 × a₃ + 4 = 2 × 11 + 4 = 22 + 4 = 26

**Final Answer:** The first four terms are: 1, 4, 11, 26.

**Problem 1c: cₖ = k(cₖ₋₁)², for all integers k ≥ 1, c₀ = 1**

**How to understand this recurrence:**
- **"cₖ = k(cₖ₋₁)²":** Each term is the position number times the square of the previous term
- **"for all integers k ≥ 1":** This rule applies starting from the first term
- **"c₀ = 1":** This is our starting value (the base case)

**Step-by-Step Calculation:**
- c₀ = 1 (given)
- c₁ = 1 × (c₀)² = 1 × (1)² = 1 × 1 = 1
- c₂ = 2 × (c₁)² = 2 × (1)² = 2 × 1 = 2
- c₃ = 3 × (c₂)² = 3 × (2)² = 3 × 4 = 12

**Final Answer:** The first four terms are: 1, 1, 2, 12.

**Problem 1e: sₖ = sₖ₋₁ + 2sₖ₋₂, for all integers k ≥ 2, s₀ = 1, s₁ = 1**

**How to understand this recurrence:**
- **"sₖ = sₖ₋₁ + 2sₖ₋₂":** Each term is the previous term plus twice the term before that
- **"for all integers k ≥ 2":** This rule applies starting from the third term
- **"s₀ = 1, s₁ = 1":** These are our starting values (the base cases)

**Step-by-Step Calculation:**
- s₀ = 1 (given)
- s₁ = 1 (given)
- s₂ = s₁ + 2 × s₀ = 1 + 2 × 1 = 1 + 2 = 3
- s₃ = s₂ + 2 × s₁ = 3 + 2 × 1 = 3 + 2 = 5

**Final Answer:** The first four terms are: 1, 1, 3, 5.

---

## Chapter 5.6: Tower of Hanoi Problems

### Problem 17: Tower of Hanoi with Adjacency Requirement

**Problem Statement:** Let aₙ be the minimum number of moves to transfer n disks from pole A to C, where moves are restricted to adjacent poles (A to B, B to C, etc.).

**Formal Restatement:** Find a recurrence relation for the minimum number of moves aₙ to transfer n disks from A to C with the adjacency restriction.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Tower of Hanoi":** This is a classic puzzle with disks of different sizes on three poles
- **"adjacency requirement":** Normally you can move any disk from any pole to any other, but now you can only move to adjacent poles
- **"minimum number of moves":** We want the most efficient way to solve this restricted version
- **"recurrence relation":** We need a formula that relates aₙ to previous terms aₙ₋₁, aₙ₋₂, etc.

**Step-by-Step Solution:**

**Part a: Find a₁ and a₂**

**For a₁ (1 disk):**
- Move disk 1 from A to B (1 move)
- Move disk 1 from B to C (1 move)
- Total: a₁ = 2

**For a₂ (2 disks):**
The strategy is:
1. Move disk 1 from A to B to C (2 moves)
2. Move disk 2 from A to B (1 move)
3. Move disk 1 from C to B (1 move)
4. Move disk 2 from B to C (1 move)
5. Move disk 1 from A to B to C (2 moves)
Wait, this doesn't work because disk 1 is on B at the end, not A.

Let me try a better strategy:
1. Move the top n-1 disks from A to C using aₙ₋₁ moves
2. Move the largest disk from A to B (1 move)
3. Move the n-1 disks from C back to A using aₙ₋₁ moves
4. Move the largest disk from B to C (1 move)
5. Move the n-1 disks from A to C using aₙ₋₁ moves

Total moves: aₙ = aₙ₋₁ + 1 + aₙ₋₁ + 1 + aₙ₋₁ = 3aₙ₋₁ + 2

Using a₁ = 2, we get a₂ = 3(2) + 2 = 8

**Part c: Find a recurrence relation**

The strategy above gives us the recurrence relation:
aₙ = 3aₙ₋₁ + 2 for n ≥ 2, with a₁ = 2

**Why this works:**
1. To move n disks from A to C with adjacent moves only:
   - First, we must move the top n-1 disks from A to C (this takes aₙ₋₁ moves)
   - Then move the largest disk from A to B (1 move)
   - Then move the n-1 disks from C back to A (this takes aₙ₋₁ moves)
   - Then move the largest disk from B to C (1 move)
   - Finally, move the n-1 disks from A to C (this takes aₙ₋₁ moves)

**Final Answer:**
- a. a₁ = 2, a₂ = 8
- c. aₙ = 3aₙ₋₁ + 2 for n ≥ 2, with a₁ = 2

---

## Chapter 5.7: Solving Recurrence Relations

### Example 5.7.1: Solving Linear Recurrence Relations

**Problem Statement:** Use iteration to guess an explicit formula for the sequence defined by aₖ = aₖ₋₁ - 1, for all integers k ≥ 1, a₀ = 2.

**Formal Restatement:** Find a closed-form formula for the recurrence relation aₖ = aₖ₋₁ - 1 with initial condition a₀ = 2.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Use iteration":** We need to repeatedly apply the recurrence relation to see if a pattern emerges
- **"guess an explicit formula":** We want a direct formula for aₙ that doesn't reference previous terms
- **"recurrence relation":** This defines each term based on the previous term
- **"closed-form formula":** A formula that lets you compute any term directly without referring to previous terms

**Step-by-Step Solution:**

**Step 1: Write out the first few terms**
- a₀ = 2 (given)
- a₁ = a₀ - 1 = 2 - 1 = 1
- a₂ = a₁ - 1 = 1 - 1 = 0
- a₃ = a₂ - 1 = 0 - 1 = -1

**Step 2: Look for a pattern**
Looking at these terms: 2, 1, 0, -1, ...
It appears that each term is 2 minus its position number.

**Step 3: Guess the formula**
Based on the pattern, I guess: aₙ = 2 - n

**Step 4: Verify the formula**
Let's check if this formula satisfies the recurrence relation:
- Left side: aₖ = 2 - k
- Right side: aₖ₋₁ - 1 = (2 - (k-1)) - 1 = (2 - k + 1) - 1 = (3 - k) - 1 = 2 - k

Since both sides equal 2 - k, the formula satisfies the recurrence relation.

**Step 5: Check the initial condition**
For n = 0: a₀ = 2 - 0 = 2, which matches the given initial condition.

**Final Answer:** The explicit formula is aₙ = 2 - n for n ≥ 0.

---

## Chapter 5.7: Homework Problems

### Problem 3: Use iteration to guess an explicit formula

**Problem 3a: aₖ = aₖ₋₁ - 1, for all integers k ≥ 1, a₀ = 2**

**Formal Restatement:** Find a closed-form formula for the recurrence relation aₖ = aₖ₋₁ - 1 with initial condition a₀ = 2.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Use iteration":** We need to repeatedly apply the recurrence relation to see if a pattern emerges
- **"guess an explicit formula":** We want a direct formula for aₙ that doesn't reference previous terms
- **"aₖ = aₖ₋₁ - 1":** Each term is the previous term minus 1
- **"a₀ = 2":** This is our starting value

**Step-by-Step Solution:**

**Step 1: Write out the first few terms by iteration**
- a₀ = 2
- a₁ = a₀ - 1 = 2 - 1 = 1
- a₂ = a₁ - 1 = (2 - 1) - 1 = 2 - 2
- a₃ = a₂ - 1 = (2 - 2) - 1 = 2 - 3

**Step 2: Observe the pattern**
Looking at the pattern: 2, 2-1, 2-2, 2-3, ...
It appears that the k-th term is 2 minus k.

**Step 3: Guess the formula**
Based on the pattern, I guess: aₙ = 2 - n, for n ≥ 0.

**Final Answer:** The explicit formula is aₙ = 2 - n for n ≥ 0.

**Problem 3c: cₖ = 3cₖ₋₁ + 1, for all integers k ≥ 1, c₀ = 1**

**Formal Restatement:** Find a closed-form formula for the recurrence relation cₖ = 3cₖ₋₁ + 1 with initial condition c₀ = 1.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"cₖ = 3cₖ₋₁ + 1":** Each term is 3 times the previous term plus 1
- **"c₀ = 1":** This is our starting value
- This looks like a geometric sequence with an additional constant term

**Step-by-Step Solution:**

**Step 1: Write out the first few terms by iteration**
- c₀ = 1
- c₁ = 3c₀ + 1 = 3(1) + 1 = 4
- c₂ = 3c₁ + 1 = 3(4) + 1 = 13
- c₃ = 3c₂ + 1 = 3(13) + 1 = 40

**Step 2: Expand the terms to see the pattern**
- c₀ = 1
- c₁ = 3(1) + 1
- c₂ = 3(3(1) + 1) + 1 = 3²(1) + 3 + 1
- c₃ = 3(3²(1) + 3 + 1) + 1 = 3³(1) + 3² + 3 + 1

**Step 3: Recognize the pattern**
The k-th term appears to be: cₖ = 3ᵏ + 3ᵏ⁻¹ + ... + 3 + 1

**Step 4: Apply the geometric series sum formula**
This is a geometric series with first term 1 and common ratio 3.
The sum of 1 + 3 + 3² + ... + 3ᵏ = (3ᵏ⁺¹ - 1)/(3 - 1) = (3ᵏ⁺¹ - 1)/2

**Step 5: Write the formula**
cₖ = (3ᵏ⁺¹ - 1)/2

**Step 6: Verify with initial terms**
- For k = 0: (3¹ - 1)/2 = (3 - 1)/2 = 1 ✓
- For k = 1: (3² - 1)/2 = (9 - 1)/2 = 4 ✓
- For k = 2: (3³ - 1)/2 = (27 - 1)/2 = 13 ✓

**Final Answer:** The explicit formula is cₙ = (3ⁿ⁺¹ - 1)/2 for n ≥ 0.

---

## Chapter 5.7: Compound Interest Problem

### Problem 23: Compound Interest Calculation

**Problem Statement:** A country's population is 50 million and grows at 3% per year. What will it be in 25 years?

**Formal Restatement:** Given an initial population of 50,000,000 with a 3% annual growth rate, calculate the population after 25 years.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Compound interest":** This is about exponential growth where each year's growth is based on the previous year's total
- **"Population is 50 million":** This is our starting amount or principal
- **"Grows at 3% per year":** Each year, the population increases by 3% of its current value
- **"What will it be in 25 years":** We need to find the population after 25 years of growth

**Step-by-Step Solution:**

**Step 1: Set up the recurrence relation**
The population after n years, Pₙ, follows the recurrence:
Pₙ = Pₙ₋₁ + 0.03 × Pₙ₋₁ = 1.03 × Pₙ₋₁

With initial condition: P₀ = 50,000,000

**Step 2: Recognize this as a geometric sequence**
This is a geometric sequence with:
- First term (when n = 0): a = 50,000,000
- Common ratio: r = 1.03

**Step 3: Use the formula for geometric sequences**
The explicit formula is: Pₙ = P₀ × rⁿ

For our case: Pₙ = 50,000,000 × (1.03)ⁿ

**Step 4: Calculate for n = 25**
P₂₅ = 50,000,000 × (1.03)²⁵

**Step 5: Compute the numerical value**
(1.03)²⁵ ≈ 2.093778
P₂₅ ≈ 50,000,000 × 2.093778 ≈ 104,688,900

**Step 6: Round appropriately**
Since we're talking about population, we should round to the nearest whole number.
P₂₅ ≈ 104,688,900 people

**Final Answer:** The population will be approximately 104.7 million in 25 years.

---

## Chapter 5.7: Verification by Induction

### Problem 29: Verify the formula for Exercise 5

**Problem Statement:** Verify the formula for Exercise 5 using mathematical induction.

**Formal Restatement:** Prove that the explicit formula cₙ = (3ⁿ⁺¹ - 1)/2 satisfies the recurrence relation cₖ = 3cₖ₋₁ + 1 with c₀ = 1.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **"Verify the formula":** We need to prove that our guessed formula is correct
- **"using mathematical induction":** We'll use the standard induction proof technique
- **"satisfies the recurrence relation":** We need to show that when we plug our formula into the recurrence, both sides are equal

**Step-by-Step Solution:**

**Formula to verify:** cₙ = (3ⁿ⁺¹ - 1)/2
**Recurrence relation:** cₖ = 3cₖ₋₁ + 1
**Initial condition:** c₀ = 1

**Step 1: Basis Step (n = 0)**
We need to show that the formula gives the correct value for n = 0.

**Left side:** c₀ = 1 (given)
**Right side:** (3⁰⁺¹ - 1)/2 = (3¹ - 1)/2 = (3 - 1)/2 = 2/2 = 1

Since both sides equal 1, the basis step holds.

**Step 2: Inductive Step**
We need to show that if the formula holds for some integer k ≥ 0, then it also holds for k+1.

**Inductive Hypothesis:** Assume that cₖ = (3ᵏ⁺¹ - 1)/2 is true.

**Goal:** Show that cₖ₊₁ = (3^(k+2) - 1)/2 is true.

**Proof:**
From the recurrence relation: cₖ₊₁ = 3cₖ + 1

Substitute the inductive hypothesis:
cₖ₊₁ = 3 × [(3ᵏ⁺¹ - 1)/2] + 1
      = (3 × (3ᵏ⁺¹ - 1))/2 + 1
      = (3ᵏ⁺² - 3)/2 + 1
      = (3ᵏ⁺² - 3)/2 + 2/2
      = (3ᵏ⁺² - 3 + 2)/2
      = (3ᵏ⁺² - 1)/2
      = (3^(k+2) - 1)/2

This matches our goal formula for cₖ₊₁.

**Step 3: Conclusion**
Since the basis step holds and the inductive step is valid, by the principle of mathematical induction, the formula cₙ = (3ⁿ⁺¹ - 1)/2 is correct for all integers n ≥ 0.

**Final Answer:** The formula cₙ = (3ⁿ⁺¹ - 1)/2 has been verified by mathematical induction.