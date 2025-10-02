# Chapter 9.1 Exercises: Complete Solutions with Frameworks

**Section:** 9.1 - Introduction to Probability  
**Focus:** Sample spaces, events, and probability calculations

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **List Sample Space** | "list outcomes", "sample space" | Enumerate all possibilities | Systematic listing |
| **Define Event** | "write event as set" | Identify favorable outcomes | List outcomes in event |
| **Calculate Probability** | "find probability", "what is P" | Apply formula | P(E) = N(E)/N(S) |
| **Count List Elements** | "how many integers from m to n" | Apply counting formula | n - m + 1 |
| **Array Probability** | "array element", "subscript" | Count subarray elements | Use floor/ceiling |
| **Multiples in Range** | "divisible by", "multiples of" | Count arithmetic sequence | Find first/last, count |

---

## Exercise 2: Two Quarters Probabilities

### Problem Statement
In the example of tossing two quarters, what is the probability that:
a. At least one head is obtained?
b. Coin A is a head?
c. Coins A and B are either both heads or both tails?

---

### What This Problem Is Asking

**Context:** Two distinguishable coins (A and B)
**Sample space:** {HH, HT, TH, TT}
**Task:** Calculate three different probabilities

---

### Solution

**Sample space:** S = {HH, HT, TH, TT}, N(S) = 4

---

**Part (a): At least one head**

**Event:** E = outcomes with 1 or more heads
```
E = {HH, HT, TH}
N(E) = 3
```

**Probability:**
```
P(E) = N(E)/N(S) = 3/4 = 75%
```

**Alternative (complement):**
```
P(at least 1 head) = 1 - P(no heads)
                   = 1 - P({TT})
                   = 1 - 1/4
                   = 3/4
```

---

**Part (b): Coin A is heads**

**Event:** E = outcomes where A shows heads
```
E = {HH, HT}
N(E) = 2
```

**Probability:**
```
P(E) = N(E)/N(S) = 2/4 = 1/2 = 50%
```

---

**Part (c): Both same (both heads or both tails)**

**Event:** E = outcomes where A and B match
```
E = {HH, TT}
N(E) = 2
```

**Probability:**
```
P(E) = N(E)/N(S) = 2/4 = 1/2 = 50%
```

---

## Exercise 3: Red Non-Face Card

### Problem Statement
The event that the chosen card is red and is not a face card.

**Context:** Standard 52-card deck

---

### Solution

**Red suits:** ♥ (hearts) and ♦ (diamonds)

**Non-face cards:** 2, 3, 4, 5, 6, 7, 8, 9, 10, A (10 per suit)

**Event:**
```
E = {2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, A♥,
     2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, A♦}
N(E) = 20
```

**Probability:**
```
P(E) = 20/52 = 5/13 ≈ 38.5%
```

---

## Exercise 7: Dice Sum Equals 8

### Problem Statement
The event that the sum of the numbers showing face up is 8.

---

### Solution

**Sample space:** N(S) = 36

**Event: Sum = 8**
```
Find all (blue, gray) pairs that sum to 8:
2 + 6 = 8 → (2, 6)
3 + 5 = 8 → (3, 5)
4 + 4 = 8 → (4, 4)
5 + 3 = 8 → (5, 3)
6 + 2 = 8 → (6, 2)

E = {26, 35, 44, 53, 62}
N(E) = 5
```

**Probability:**
```
P(E) = 5/36 ≈ 13.9%
```

---

## Exercise 11: Three Coin Tosses

### Problem Statement
A coin is tossed three times. Let HHT indicate heads on first two tosses and tails on third, etc.

a. List the eight elements in the sample space.
b. Find probability of:
   (i) Exactly one head
   (ii) At least two heads
   (iii) No heads

---

### Solution

**Part (a): Sample Space**
```
S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}
N(S) = 8 = 2³
```

---

**Part (b)(i): Exactly one head**

**Event:**
```
E = {HTT, THT, TTH}
N(E) = 3
```

**Probability:**
```
P(E) = 3/8 = 37.5%
```

---

**Part (b)(ii): At least two heads**

**Event:** 2 or 3 heads
```
E = {HHH, HHT, HTH, THH}
N(E) = 4
```

**Probability:**
```
P(E) = 4/8 = 1/2 = 50%
```

---

**Part (b)(iii): No heads**

**Event:**
```
E = {TTT}
N(E) = 1
```

**Probability:**
```
P(E) = 1/8 = 12.5%
```

---

## Exercise 21: Two-Digit Multiples

### Problem Statement
a. How many positive two-digit integers are multiples of 3?
b. What is the probability that a randomly chosen positive two-digit integer is a multiple of 3?
c. What is the probability that a randomly chosen positive two-digit integer is a multiple of 4?

---

### Solution

**Part (a): Count multiples of 3**

**Two-digit integers:** 10 to 99

**Multiples of 3:** 12, 15, 18, ..., 99

**Rewrite as:** 3×4, 3×5, 3×6, ..., 3×33

**Count:**
```
From 4 to 33: 33 - 4 + 1 = 30 multiples
```

**Answer:** 30 two-digit multiples of 3

---

**Part (b): Probability of multiple of 3**

**Total two-digit integers:**
```
From 10 to 99: 99 - 10 + 1 = 90 integers
```

**Multiples of 3:** 30 (from part a)

**Probability:**
```
P(multiple of 3) = 30/90 = 1/3 ≈ 33.3%
```

---

**Part (c): Probability of multiple of 4**

**Multiples of 4:** 12, 16, 20, ..., 96

**Rewrite as:** 4×3, 4×4, 4×5, ..., 4×24

**Count:**
```
From 3 to 24: 24 - 3 + 1 = 22 multiples
```

**Probability:**
```
P(multiple of 4) = 22/90 = 11/45 ≈ 24.4%
```

---

## Exercise 23: Array Subarrays

### Problem Statement
Suppose A[1], A[2], ..., A[n] is a one-dimensional array and n ≥ 50.

a. How many elements are in the array?
b. How many elements are in the subarray A[4], A[5], ..., A[39]?
c. If 3 ≤ m ≤ n, what is the probability that a randomly chosen array element is in the subarray A[3], A[4], ..., A[m]?
d. What is the probability that a randomly chosen array element is in the subarray A[⌊n/2⌋], A[⌊n/2⌋+1], ..., A[n] if n = 39?

---

### Solution

**Part (a): Total elements**
```
Array: A[1] to A[n]
Number: n - 1 + 1 = n elements
```

---

**Part (b): Subarray A[4] to A[39]**
```
From 4 to 39: 39 - 4 + 1 = 36 elements
```

---

**Part (c): Subarray A[3] to A[m]**

**Count:**
```
From 3 to m: m - 3 + 1 elements
```

**Probability:**
```
P = (m - 3 + 1) / n = (m - 2) / n
```

---

**Part (d): Subarray A[⌊n/2⌋] to A[n] with n = 39**

**Calculate ⌊39/2⌋:**
```
⌊39/2⌋ = ⌊19.5⌋ = 19
```

**Subarray:** A[19] to A[39]

**Count:**
```
From 19 to 39: 39 - 19 + 1 = 21 elements
```

**Probability:**
```
P = 21/39 = 7/13 ≈ 53.8%
```

---

## Exercise 24: First Half of Array

### Problem Statement
Consider the subarray A[1], A[2], ..., A[⌊n/2⌋].

a. How many elements are in the subarray (i) if n is even? (ii) if n is odd?
b. What is the probability that a randomly chosen array element is in the subarray (i) if n is even? (ii) if n is odd?

---

### Solution

**Part (a): Count elements**

**(i) n is even:**
```
⌊n/2⌋ = n/2
Subarray: A[1] to A[n/2]
Count: n/2 - 1 + 1 = n/2 elements
```

**(ii) n is odd:**
```
⌊n/2⌋ = (n-1)/2
Subarray: A[1] to A[(n-1)/2]
Count: (n-1)/2 - 1 + 1 = (n-1)/2 elements
```

---

**Part (b): Probability**

**(i) n is even:**
```
P = (n/2) / n = 1/2 = 50%
```

**(ii) n is odd:**
```
P = [(n-1)/2] / n = (n-1)/(2n)

Example: n=39
P = 38/78 = 19/39 ≈ 48.7%
```

---

## Exercise 28: Consecutive Integers

### Problem Statement
If the largest of 56 consecutive integers is 279, what is the smallest?

---

### Solution

**Given:**
- 56 consecutive integers
- Largest = 279

**Let smallest = m**

**Then:** Integers are m, m+1, m+2, ..., 279

**Count:** 279 - m + 1 = 56

**Solve:**
```
279 - m + 1 = 56
280 - m = 56
m = 280 - 56
m = 224
```

**Answer:** The smallest is 224

**Verification:**
```
From 224 to 279: 279 - 224 + 1 = 56 ✓
```

---

## Exercise 30: Even Integers Between 1 and 1001

### Problem Statement
How many even integers are between 1 and 1,001?

---

### Solution

**Even integers:** 2, 4, 6, 8, ..., 1000

**Note:** 1 is odd, 1001 is odd, so range is 2 to 1000

**Rewrite as:** 2×1, 2×2, 2×3, ..., 2×500

**Count:**
```
From 1 to 500: 500 - 1 + 1 = 500 multiples
```

**Answer:** 500 even integers

**Alternative method:**
```
Even integers from 2 to 1000
First: 2
Last: 1000
Difference: 1000 - 2 = 998
Step: 2
Count: 998/2 + 1 = 500
```

---

## 📋 Quick Reference: Selected Exercises

### Exercise 2: Two Quarters
```
(a) P(at least 1 head) = 3/4
(b) P(coin A is head) = 1/2
(c) P(both same) = 1/2
```

### Exercise 3: Red Non-Face Card
```
E = {2-10, A of ♥ and ♦}
N(E) = 20
P(E) = 20/52 = 5/13
```

### Exercise 7: Dice Sum = 8
```
E = {26, 35, 44, 53, 62}
N(E) = 5
P(E) = 5/36
```

### Exercise 11: Three Coins
```
(i) P(exactly 1 head) = 3/8
(ii) P(at least 2 heads) = 4/8 = 1/2
(iii) P(no heads) = 1/8
```

### Exercise 21: Two-Digit Multiples
```
(a) Multiples of 3: 30
(b) P(multiple of 3) = 30/90 = 1/3
(c) P(multiple of 4) = 22/90 = 11/45
```

### Exercise 23: Array Subarrays
```
(a) n elements
(b) 36 elements (from 4 to 39)
(c) P = (m-2)/n
(d) P = 21/39 = 7/13
```

### Exercise 24: First Half
```
(a)(i) n/2 elements (n even)
(a)(ii) (n-1)/2 elements (n odd)
(b)(i) P = 1/2 (n even)
(b)(ii) P = (n-1)/(2n) (n odd)
```

### Exercise 28: Consecutive Integers
```
Largest: 279
Count: 56
Smallest: 279 - 56 + 1 = 224
```

### Exercise 30: Even Integers
```
From 2 to 1000
Count: 500
```

---

## 🔑 Key Formulas

### Counting Formula
```
Integers from m to n: n - m + 1
```

### Probability Formula
```
P(E) = N(E) / N(S)
```

### Complement Rule
```
P(not E) = 1 - P(E)
```

### Array Subarray
```
A[m] to A[k]: k - m + 1 elements
```

### Multiples of d in [m, n]
```
First: ⌈m/d⌉ × d
Last: ⌊n/d⌋ × d
Count: ⌊n/d⌋ - ⌈m/d⌉ + 1
```

---

## ⚠️ Common Mistakes

### Mistake 1: Forgetting +1
```
✗ From 5 to 12: 12 - 5 = 7
✓ From 5 to 12: 12 - 5 + 1 = 8
```

### Mistake 2: Not Distinguishing Coins
```
✗ Two coins: {HH, HT, TT} (3 outcomes)
✓ Two coins: {HH, HT, TH, TT} (4 outcomes)
```

### Mistake 3: Wrong Event Definition
```
✗ "At least 1 head" = {HH, HT}
✓ "At least 1 head" = {HH, HT, TH}
```

### Mistake 4: Not Simplifying
```
✗ P = 20/52
✓ P = 5/13
```

### Mistake 5: Wrong Array Count
```
✗ A[1] to A[n/2]: n/2 - 1 elements
✓ A[1] to A[n/2]: ⌊n/2⌋ elements
```

---

## 🚀 Exam Strategy

### For Sample Spaces
- [ ] List systematically
- [ ] Check completeness
- [ ] Verify equally likely
- [ ] Count carefully

### For Events
- [ ] Write as set
- [ ] List all outcomes
- [ ] Count N(E)
- [ ] Verify against sample space

### For Probabilities
- [ ] Apply P(E) = N(E)/N(S)
- [ ] Simplify fraction
- [ ] Convert to percentage if asked
- [ ] Check 0 ≤ P ≤ 1

### For Counting
- [ ] Apply n - m + 1
- [ ] Handle floor/ceiling
- [ ] Verify with small example
- [ ] Check endpoints

### Time Management
- Sample space: 2-3 min
- Event definition: 2-3 min
- Probability: 2-3 min
- Counting: 3-5 min
- Array problems: 5-8 min

---

**You're ready to master probability! 🎉**

---

**End of Guide**
