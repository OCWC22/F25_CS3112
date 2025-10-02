# Chapter 9.1 Complete Guide: Introduction to Probability

**Course:** CS3112 - Introduction to Algorithms (Discrete Math Component)  
**Section:** 9.1 - Introduction to Probability  
**Purpose:** Master basic probability concepts for algorithm analysis

---

## 🎯 What Chapter 9.1 Is Really About

### The Big Picture

Chapter 9.1 teaches you **basic probability** - the foundation for analyzing randomized algorithms and average-case performance.

**Mental model:** Probability is like **predicting outcomes**:
- Sample space = all possible outcomes
- Event = subset of outcomes we care about
- Probability = fraction of favorable outcomes

**Why it's important:**
- **Average-case analysis:** Understand expected algorithm performance
- **Randomized algorithms:** Analyze algorithms that use randomness
- **Counting:** Connect to combinatorics
- **Real-world applications:** Model uncertainty

**Key insight:** You can predict long-term behavior even when individual outcomes are random!

---

## 📚 Core Definitions

### Sample Space

**Definition:** The set of all possible outcomes of a random process or experiment

**Examples:**
```
Tossing one coin: S = {H, T}
Tossing two coins: S = {HH, HT, TH, TT}
Rolling one die: S = {1, 2, 3, 4, 5, 6}
Picking a card: S = {all 52 cards}
```

**Key properties:**
- Contains ALL possible outcomes
- Outcomes are mutually exclusive
- Exactly one outcome occurs

---

### Event

**Definition:** A subset of a sample space

**Examples:**
```
Two coins, event "exactly 1 head": E = {HT, TH}
One die, event "even number": E = {2, 4, 6}
Card deck, event "black face card": E = {J♣, Q♣, K♣, J♠, Q♠, K♠}
```

**Special events:**
- Empty event: ∅ (impossible event)
- Entire sample space: S (certain event)

---

### Probability (Equally Likely Formula)

**Definition:** If all outcomes are equally likely:

```
P(E) = N(E) / N(S) = (number of outcomes in E) / (total number of outcomes)
```

**Where:**
- N(E) = number of elements in event E
- N(S) = number of elements in sample space S

**Properties:**
- 0 ≤ P(E) ≤ 1 (probability is between 0 and 1)
- P(∅) = 0 (impossible event)
- P(S) = 1 (certain event)

---

## 🎓 Fundamental Examples

### Example 1: Two Coins

**Experiment:** Toss two coins (A and B)

**Sample space:**
```
S = {HH, HT, TH, TT}
N(S) = 4
```

**Events:**
```
E₁ = "2 heads" = {HH}
P(E₁) = 1/4 = 25%

E₂ = "1 head" = {HT, TH}
P(E₂) = 2/4 = 50%

E₃ = "0 heads" = {TT}
P(E₃) = 1/4 = 25%
```

**Key insight:** Getting 1 head is TWICE as likely as 2 heads or 0 heads!

---

### Example 2: Two Dice

**Experiment:** Roll blue die and gray die

**Sample space:**
```
S = {11, 12, 13, ..., 66}
N(S) = 36 (6 × 6)
```

**Event: Sum equals 6**
```
E = {15, 24, 33, 42, 51}
N(E) = 5
P(E) = 5/36 ≈ 13.9%
```

**Event: Both dice same**
```
E = {11, 22, 33, 44, 55, 66}
N(E) = 6
P(E) = 6/36 = 1/6 ≈ 16.7%
```

---

### Example 3: Deck of Cards

**Sample space:** 52 cards
- 4 suits: ♠, ♥, ♦, ♣
- 13 denominations per suit: 2-10, J, Q, K, A
- Red cards: ♥, ♦ (26 cards)
- Black cards: ♠, ♣ (26 cards)
- Face cards: J, Q, K (12 cards)

**Event: Black face card**
```
E = {J♣, Q♣, K♣, J♠, Q♠, K♠}
N(E) = 6
P(E) = 6/52 = 3/26 ≈ 11.5%
```

**Event: Red non-face card**
```
E = {2♥, 3♥, ..., 10♥, A♥, 2♦, 3♦, ..., 10♦, A♦}
N(E) = 10 + 10 = 20
P(E) = 20/52 = 5/13 ≈ 38.5%
```

---

## 🔑 Counting Elements in Lists

### Theorem 9.1.1: Number of Elements

**If m ≤ n, the number of integers from m to n inclusive is:**
```
n - m + 1
```

**Examples:**
```
From 5 to 12: 12 - 5 + 1 = 8 integers
From 1 to 100: 100 - 1 + 1 = 100 integers
From 100 to 999: 999 - 100 + 1 = 900 integers
```

**Why +1?** Both endpoints are included!

---

### Application: Three-Digit Integers Divisible by 5

**Question:** How many three-digit integers (100-999) are divisible by 5?

**Solution:**
```
Three-digit multiples of 5: 100, 105, 110, ..., 995

Rewrite as: 5×20, 5×21, 5×22, ..., 5×199

Count multiples: from 20 to 199
Number: 199 - 20 + 1 = 180
```

**Probability:**
```
Total three-digit integers: 999 - 100 + 1 = 900
Divisible by 5: 180
P(divisible by 5) = 180/900 = 1/5 = 20%
```

---

## 💡 Array Probability Problems

### Array Structure

**Given:** A[1], A[2], ..., A[n]

**Total elements:** n

**Subarray A[m] to A[k]:**
- Number of elements: k - m + 1
- Probability of random element in subarray: (k - m + 1) / n

---

### Example: Even Subscripts

**Question:** Probability that random element has even subscript?

**Case 1: n is even**
```
Even subscripts: 2, 4, 6, ..., n
Number: n/2
Probability: (n/2) / n = 1/2
```

**Case 2: n is odd**
```
Even subscripts: 2, 4, 6, ..., n-1
Number: (n-1)/2
Probability: (n-1)/2 / n = (n-1)/(2n)

As n → ∞, this approaches 1/2
```

**Using floor notation:** ⌊n/2⌋ / n

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Basic Probability

**Given:** Random experiment
**Task:** Find probability of event

**Steps:**
1. Define sample space S
2. Count N(S)
3. Define event E
4. Count N(E)
5. Calculate P(E) = N(E) / N(S)

---

### Framework 2: Counting List Elements

**Given:** Range from m to n
**Task:** Count elements

**Steps:**
1. Verify m ≤ n
2. Apply formula: n - m + 1
3. Verify with small example if unsure

---

### Framework 3: Array Probability

**Given:** Array A[1..n] and subarray
**Task:** Find probability

**Steps:**
1. Count elements in subarray (use n - m + 1)
2. Total elements: n
3. Probability: (subarray size) / n

---

### Framework 4: Multiples in Range

**Given:** Range and divisor d
**Task:** Count multiples of d

**Steps:**
1. Find first multiple: ⌈m/d⌉ × d
2. Find last multiple: ⌊n/d⌋ × d
3. Rewrite as d×k₁ to d×k₂
4. Count: k₂ - k₁ + 1

---

## 📊 Common Probability Patterns

### Coin Tosses

**One coin:**
```
S = {H, T}
P(H) = P(T) = 1/2
```

**Two coins:**
```
S = {HH, HT, TH, TT}
P(2 heads) = 1/4
P(1 head) = 2/4 = 1/2
P(0 heads) = 1/4
```

**Three coins:**
```
S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}
N(S) = 8
P(3 heads) = 1/8
P(2 heads) = 3/8
P(1 head) = 3/8
P(0 heads) = 1/8
```

**Pattern:** n coins → 2ⁿ outcomes

---

### Dice Rolls

**One die:**
```
S = {1, 2, 3, 4, 5, 6}
N(S) = 6
P(any specific number) = 1/6
```

**Two dice:**
```
N(S) = 36 (6 × 6)
P(sum = 7) = 6/36 = 1/6 (outcomes: 16, 25, 34, 43, 52, 61)
P(sum = 2) = 1/36 (outcome: 11)
P(sum = 12) = 1/36 (outcome: 66)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Count Formula
```
✗ From m to n: n - m elements
✓ From m to n: n - m + 1 elements
```

### Mistake 2: Assuming Equal Likelihood
```
✗ "Two coins: 0, 1, or 2 heads each with P = 1/3"
✓ P(0 heads) = 1/4, P(1 head) = 1/2, P(2 heads) = 1/4
```

### Mistake 3: Forgetting Outcomes
```
✗ Two coins: {HH, HT, TT} (forgetting TH)
✓ Two coins: {HH, HT, TH, TT}
```

### Mistake 4: Wrong Subarray Count
```
✗ A[1] to A[n/2]: n/2 - 1 elements
✓ A[1] to A[n/2]: ⌊n/2⌋ elements (using floor)
```

### Mistake 5: Not Simplifying Fractions
```
✗ P(E) = 6/52
✓ P(E) = 3/26 (simplified)
```

---

## 🚀 Exam Strategy

### For Basic Probability
- [ ] List sample space completely
- [ ] Define event as set
- [ ] Count carefully
- [ ] Simplify fraction

### For Counting Problems
- [ ] Apply n - m + 1 formula
- [ ] Verify with small example
- [ ] Check endpoints included

### For Array Problems
- [ ] Use floor/ceiling correctly
- [ ] Handle even/odd cases
- [ ] Apply counting formula

### For Multiples
- [ ] Find first and last multiple
- [ ] Convert to counting problem
- [ ] Apply formula

### Time Management
- Basic probability: 3-5 min
- Counting: 2-3 min
- Array probability: 5-8 min
- Multiples: 5-8 min

---

**You're ready to master probability basics! 🎉**

---

**End of Guide**
