# Chapter 9.1 Quick Reference: Introduction to Probability

**One-page cheat sheet for midterm**

---

## 🎯 Core Definitions

### Sample Space
```
S = set of all possible outcomes
```

### Event
```
E = subset of sample space
```

### Probability (Equally Likely)
```
P(E) = N(E) / N(S)
     = (# outcomes in E) / (# outcomes in S)
```

---

## 🔑 Key Formulas

### Counting List Elements
```
Integers from m to n: n - m + 1
```

### Probability Properties
```
0 ≤ P(E) ≤ 1
P(∅) = 0 (impossible)
P(S) = 1 (certain)
P(not E) = 1 - P(E)
```

### Array Subarray
```
A[m] to A[k]: k - m + 1 elements
Probability: (k - m + 1) / n
```

---

## 📊 Common Experiments

### Coins
```
1 coin: S = {H, T}, N(S) = 2
2 coins: S = {HH, HT, TH, TT}, N(S) = 4
3 coins: N(S) = 8
n coins: N(S) = 2ⁿ
```

### Dice
```
1 die: S = {1, 2, 3, 4, 5, 6}, N(S) = 6
2 dice: N(S) = 36
```

### Cards
```
Deck: 52 cards
Suits: 4 (♠, ♥, ♦, ♣)
Per suit: 13 cards
Face cards: 12 (J, Q, K in each suit)
```

---

## 💡 Quick Calculations

### Two Coins
```
P(2 heads) = 1/4
P(1 head) = 2/4 = 1/2
P(0 heads) = 1/4
P(at least 1 head) = 3/4
```

### Two Dice
```
P(sum = 7) = 6/36 = 1/6
P(sum = 2) = 1/36
P(sum = 12) = 1/36
P(both same) = 6/36 = 1/6
```

### Three Coins
```
P(3 heads) = 1/8
P(2 heads) = 3/8
P(1 head) = 3/8
P(0 heads) = 1/8
```

---

## 🧮 Counting Techniques

### Multiples of d in [m, n]
```
First multiple: ⌈m/d⌉ × d
Last multiple: ⌊n/d⌋ × d
Count: ⌊n/d⌋ - ⌈m/d⌉ + 1
```

### Even Numbers in [m, n]
```
If m and n both odd: (n-m)/2
If m even, n odd: (n-m+1)/2
Use: ⌊n/2⌋ - ⌊(m-1)/2⌋
```

### Array Elements
```
A[1] to A[n]: n elements
A[1] to A[⌊n/2⌋]: ⌊n/2⌋ elements
A[m] to A[n]: n - m + 1 elements
```

---

## 📋 Exercise Quick Reference

### Two Quarters (Ex 2)
```
(a) P(≥1 head) = 3/4
(b) P(A is head) = 1/2
(c) P(both same) = 1/2
```

### Cards (Ex 3-6)
```
Red non-face: 20/52 = 5/13
Black even: 20/52 = 5/13
Denomination ≥10: 20/52 = 5/13
Denomination ≤4: 16/52 = 4/13
```

### Dice (Ex 7-10)
```
Sum = 8: 5/36
Both same: 6/36 = 1/6
Sum ≤ 6: 15/36 = 5/12
Sum ≥ 9: 10/36 = 5/18
```

### Three Coins (Ex 11)
```
Exactly 1 head: 3/8
At least 2 heads: 4/8 = 1/2
No heads: 1/8
```

### Multiples (Ex 21)
```
Two-digit multiples of 3: 30
P(multiple of 3) = 30/90 = 1/3
P(multiple of 4) = 22/90 = 11/45
```

### Arrays (Ex 23-25)
```
A[4] to A[39]: 36 elements
A[3] to A[m]: (m-2) elements
First half: ⌊n/2⌋ elements
Second half: ⌈n/2⌉ elements
```

### Consecutive (Ex 28-29)
```
56 integers, largest 279
Smallest: 279 - 56 + 1 = 224
```

---

## ⚠️ Common Pitfalls

### Counting
- ❌ Forgetting +1 in n - m + 1
- ❌ Not distinguishing objects (coins A and B)
- ❌ Wrong floor/ceiling handling

### Probability
- ❌ Assuming equal likelihood without justification
- ❌ Not simplifying fractions
- ❌ Probability > 1 or < 0

### Arrays
- ❌ Off-by-one errors
- ❌ Not handling even/odd cases
- ❌ Wrong subarray bounds

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **From 10 to 99, how many integers?**
   - 90

2. **P(1 head in 2 coins)?**
   - 1/2

3. **Two dice, P(sum = 7)?**
   - 1/6

4. **Three coins, P(at least 2 heads)?**
   - 1/2

5. **A[1] to A[n/2], how many if n even?**
   - n/2

---

## 🚀 Exam Checklist

### Before Solving
- [ ] Identify sample space
- [ ] Verify equally likely
- [ ] Define event clearly

### While Solving
- [ ] Count systematically
- [ ] Apply correct formula
- [ ] Simplify answer
- [ ] Check reasonableness

### For Counting
- [ ] Use n - m + 1
- [ ] Include both endpoints
- [ ] Handle floor/ceiling
- [ ] Verify with example

---

**You got this! 🎉**

---

**End of Cheat Sheet**
