# Chapter 9.2 Exercises: Complete Solutions with Frameworks

**Section:** 9.2 - Possibility Trees and the Multiplication Rule  
**Focus:** Counting techniques and permutations

---

## 🎯 Problem Recognition Framework

| Problem Type | Keywords | What It's Really Asking | How to Solve |
|--------------|----------|------------------------|--------------|
| **Multiplication Rule** | "how many ways", "distinct" | Count sequential choices | Multiply choices per step |
| **Possibility Tree** | "draw tree", "show outcomes" | Visualize all paths | Draw branches, count leaves |
| **Permutations** | "arrange", "order matters" | Count orderings | Use n! or P(n,r) |
| **Loop Iterations** | "how many times", "nested loop" | Count executions | Multiply loop ranges |
| **Constrained Counting** | "must begin with", "must end with" | Count with restrictions | Fix constrained positions first |

---

## Exercise 8: Computer System Choices

### Problem Statement
A person buying a personal computer system is offered a choice of three models of the basic unit, two models of keyboard, and two models of printer. How many distinct systems can be purchased?

---

### What This Problem Is Asking

**Task:** Count combinations of components
**Method:** Multiplication rule
**Goal:** Total distinct systems

---

### Solution

**Step 1: Identify steps**
```
Step 1: Choose basic unit
Step 2: Choose keyboard
Step 3: Choose printer
```

**Step 2: Count choices per step**
```
Basic unit: 3 choices
Keyboard: 2 choices
Printer: 2 choices
```

**Step 3: Apply multiplication rule**
```
Total systems = 3 × 2 × 2 = 12
```

**Answer:** 12 distinct systems

---

## Exercise 9: Travel Routes

### Problem Statement
Suppose there are three roads from city A to city B and five roads from city B to city C.

a. How many ways is it possible to travel from city A to C via city B?
b. How many different round-trip routes are there from A to B to C to B and back to A?
c. How many different routes are there from A to B to C to B and back to A in which no road is traversed twice?

---

### Solution

**Part (a): A to C via B**

**Steps:**
```
Step 1: A to B (3 roads)
Step 2: B to C (5 roads)

Total: 3 × 5 = 15 routes
```

---

**Part (b): Round-trip (roads can be reused)**

**Steps:**
```
Step 1: A to B (3 roads)
Step 2: B to C (5 roads)
Step 3: C to B (5 roads)
Step 4: B to A (3 roads)

Total: 3 × 5 × 5 × 3 = 225 round-trips
```

---

**Part (c): Round-trip (no road used twice)**

**Steps:**
```
Step 1: A to B (3 roads)
Step 2: B to C (5 roads)
Step 3: C to B (4 roads - can't use same road as step 2)
Step 4: B to A (2 roads - can't use same road as step 1)

Total: 3 × 5 × 4 × 2 = 120 round-trips
```

---

## Exercise 11: Bit Strings

### Problem Statement
a. A bit string is a finite sequence of 0's and 1's. How many bit strings have length 8?
b. How many bit strings of length 8 begin with three 0's?
c. How many bit strings of length 8 begin and end with a 1?

---

### Solution

**Part (a): All 8-bit strings**

**Each position:** 2 choices (0 or 1)
```
Position 1: 2 choices
Position 2: 2 choices
...
Position 8: 2 choices

Total: 2⁸ = 256 bit strings
```

---

**Part (b): Begin with 000**

**Fixed:** First 3 positions are 000
**Free:** Last 5 positions
```
Positions 1-3: 1 way (must be 000)
Positions 4-8: 2⁵ = 32 ways

Total: 1 × 32 = 32 bit strings
```

---

**Part (c): Begin and end with 1**

**Fixed:** First and last positions are 1
**Free:** Middle 6 positions
```
Position 1: 1 way (must be 1)
Positions 2-7: 2⁶ = 64 ways
Position 8: 1 way (must be 1)

Total: 1 × 64 × 1 = 64 bit strings
```

---

## Exercise 13: Four Coin Tosses

### Problem Statement
A coin is tossed four times. Each time the result H or T is recorded.

a. How many distinct outcomes are possible?
b. What is the probability that exactly two heads occur?
c. What is the probability that exactly one head occurs?

---

### Solution

**Part (a): Total outcomes**

**Each toss:** 2 outcomes (H or T)
```
Toss 1: 2 choices
Toss 2: 2 choices
Toss 3: 2 choices
Toss 4: 2 choices

Total: 2⁴ = 16 outcomes
```

---

**Part (b): Exactly 2 heads**

**Event:** Choose which 2 positions have heads

**Outcomes:**
```
HHTT, HTHT, HTTH, THHT, THTH, TTHH
```

**Count:** 6 outcomes

**Probability:**
```
P(exactly 2 heads) = 6/16 = 3/8 = 37.5%
```

---

**Part (c): Exactly 1 head**

**Event:** Choose which 1 position has head

**Outcomes:**
```
HTTT, THTT, TTHT, TTTH
```

**Count:** 4 outcomes

**Probability:**
```
P(exactly 1 head) = 4/16 = 1/4 = 25%
```

---

## Exercise 16: Two-Digit Integers

### Problem Statement
a. How many integers are there from 10 through 99?
b. How many odd integers are there from 10 through 99?
c. How many integers from 10 through 99 have distinct digits?
d. How many odd integers from 10 through 99 have distinct digits?
e. What is the probability that a randomly chosen two-digit integer has distinct digits? has distinct digits and is odd?

---

### Solution

**Part (a): Total two-digit integers**
```
From 10 to 99: 99 - 10 + 1 = 90 integers
```

---

**Part (b): Odd two-digit integers**

**Method 1: Count directly**
```
Odd integers: 11, 13, 15, ..., 99
First: 11 = 2×5 + 1
Last: 99 = 2×49 + 1
Count: 49 - 5 + 1 = 45
```

**Method 2: Multiplication rule**
```
Tens digit: 1-9 (9 choices)
Units digit: 1, 3, 5, 7, 9 (5 choices)
Total: 9 × 5 = 45
```

---

**Part (c): Distinct digits**

**Constraint:** Tens digit ≠ units digit
```
Tens digit: 1-9 (9 choices, can't be 0)
Units digit: 0-9 except tens digit (9 choices)

Total: 9 × 9 = 81 integers
```

---

**Part (d): Distinct digits AND odd**

**Constraints:** Distinct digits, units digit odd
```
Units digit: 1, 3, 5, 7, 9 (5 choices)
Tens digit: 1-9 except units digit (8 choices)

Total: 5 × 8 = 40 integers
```

**Alternative ordering:**
```
Tens digit: 1-9 (9 choices)
Units digit: odd, ≠ tens digit (5 or 4 choices depending on tens)

If tens is odd: 4 choices for units
If tens is even: 5 choices for units

Count: 5×4 + 4×5 = 20 + 20 = 40 ✓
```

---

**Part (e): Probabilities**

**Distinct digits:**
```
P = 81/90 = 9/10 = 90%
```

**Distinct digits AND odd:**
```
P = 40/90 = 4/9 ≈ 44.4%
```

---

## Exercise 24-28: Loop Iteration Counting

### Exercise 24
```
for i = 1 to 30
    for j = 1 to 15
        [body]
```

**Solution:**
```
Outer: 30 iterations
Inner: 15 iterations
Total: 30 × 15 = 450 iterations
```

---

### Exercise 25
```
for j = 1 to m
    for k = 1 to n
        [body]
```

**Solution:**
```
Outer: m iterations
Inner: n iterations
Total: m × n iterations
```

---

### Exercise 26
```
for i = 1 to m
    for j = 1 to n
        for k = 1 to p
            [body]
```

**Solution:**
```
Outer: m iterations
Middle: n iterations
Inner: p iterations
Total: m × n × p iterations
```

---

### Exercise 27
```
for i = 5 to 50
    for j = 10 to 20
        [body]
```

**Solution:**
```
Outer: 50 - 5 + 1 = 46 iterations
Inner: 20 - 10 + 1 = 11 iterations
Total: 46 × 11 = 506 iterations
```

---

### Exercise 28
```
for i = a to b
    for j = c to d
        [body]
        
(Assume a ≤ b and c ≤ d)
```

**Solution:**
```
Outer: b - a + 1 iterations
Inner: d - c + 1 iterations
Total: (b - a + 1) × (d - c + 1) iterations
```

---

## Exercise 32: ALGORITHM Permutations

### Problem Statement
a. How many ways can the letters of the word ALGORITHM be arranged in a row?
b. How many ways if A and L must remain together (in order) as a unit?
c. How many ways if the letters GOR must remain together (in order) as a unit?

---

### Solution

**Part (a): All arrangements**

**ALGORITHM has 9 distinct letters**
```
Number of arrangements: 9! = 362,880
```

---

**Part (b): AL as unit**

**Treat AL as single object**
```
Objects to arrange: [AL], G, O, R, I, T, H, M (8 objects)
Number of arrangements: 8! = 40,320
```

---

**Part (c): GOR as unit**

**Treat GOR as single object**
```
Objects to arrange: [GOR], A, L, I, T, H, M (7 objects)
Number of arrangements: 7! = 5,040
```

---

## Exercise 37: Evaluate P(n, r)

### Problem Statement
Evaluate:
a. P(6, 4)
b. P(6, 6)
c. P(6, 3)
d. P(6, 1)

---

### Solution

**Part (a): P(6, 4)**
```
P(6, 4) = 6! / (6-4)!
        = 6! / 2!
        = (6 × 5 × 4 × 3 × 2 × 1) / (2 × 1)
        = 6 × 5 × 4 × 3
        = 360
```

---

**Part (b): P(6, 6)**
```
P(6, 6) = 6! / (6-6)!
        = 6! / 0!
        = 6! / 1
        = 720
```

---

**Part (c): P(6, 3)**
```
P(6, 3) = 6! / (6-3)!
        = 6! / 3!
        = 6 × 5 × 4
        = 120
```

---

**Part (d): P(6, 1)**
```
P(6, 1) = 6! / (6-1)!
        = 6! / 5!
        = 6
```

---

## Exercise 39: ALGORITHM r-Permutations

### Problem Statement
a. How many ways can three of the letters of ALGORITHM be selected and written in a row?
b. How many ways can six of the letters be selected and written in a row?
c. How many ways can six letters be selected and written in a row if the first letter must be A?
d. How many ways can six letters be selected and written in a row if the first two letters must be OR?

---

### Solution

**Part (a): 3-permutation**

**ALGORITHM has 9 distinct letters**
```
P(9, 3) = 9! / (9-3)!
        = 9! / 6!
        = 9 × 8 × 7
        = 504
```

---

**Part (b): 6-permutation**
```
P(9, 6) = 9! / (9-6)!
        = 9! / 3!
        = 9 × 8 × 7 × 6 × 5 × 4
        = 60,480
```

---

**Part (c): First letter must be A**

**Fixed:** Position 1 is A
**Free:** Choose 5 from remaining 8 letters
```
Position 1: 1 way (must be A)
Positions 2-6: P(8, 5) ways

P(8, 5) = 8! / 3!
        = 8 × 7 × 6 × 5 × 4
        = 6,720

Total: 1 × 6,720 = 6,720
```

---

**Part (d): First two letters must be OR**

**Fixed:** Positions 1-2 are OR
**Free:** Choose 4 from remaining 7 letters
```
Positions 1-2: 1 way (must be OR)
Positions 3-6: P(7, 4) ways

P(7, 4) = 7! / 3!
        = 7 × 6 × 5 × 4
        = 840

Total: 1 × 840 = 840
```

---

## Exercise 40: Prove P(n+1, 3) = n³ - n

### Problem Statement
Prove that for all integers n ≥ 2, P(n+1, 3) = n³ - n.

---

### Solution

**Step 1: Expand P(n+1, 3)**
```
P(n+1, 3) = (n+1)! / ((n+1)-3)!
          = (n+1)! / (n-2)!
          = (n+1) × n × (n-1) × (n-2)! / (n-2)!
          = (n+1) × n × (n-1)
```

**Step 2: Expand the product**
```
(n+1) × n × (n-1) = n(n+1)(n-1)
                  = n[(n+1)(n-1)]
                  = n[n² - 1]
                  = n³ - n ✓
```

**Conclusion:** P(n+1, 3) = n³ - n for all n ≥ 2 ✓

---

## Exercise 43: Prove P(n, n) = P(n, n-1)

### Problem Statement
Prove that for all integers n ≥ 2, P(n, n) = P(n, n-1).

---

### Solution

**Step 1: Expand P(n, n)**
```
P(n, n) = n! / (n-n)!
        = n! / 0!
        = n! / 1
        = n!
```

**Step 2: Expand P(n, n-1)**
```
P(n, n-1) = n! / (n-(n-1))!
          = n! / 1!
          = n! / 1
          = n!
```

**Step 3: Compare**
```
P(n, n) = n!
P(n, n-1) = n!

Therefore: P(n, n) = P(n, n-1) ✓
```

**Intuition:** Arranging all n elements = arranging first n-1 elements (last one has no choice)

---

## 📋 Quick Reference: Selected Exercises

### Exercise 8: Computer System
```
3 units × 2 keyboards × 2 printers = 12 systems
```

### Exercise 9: Travel Routes
```
(a) A→B→C: 3 × 5 = 15
(b) Round-trip (reuse): 3 × 5 × 5 × 3 = 225
(c) Round-trip (no reuse): 3 × 5 × 4 × 2 = 120
```

### Exercise 11: Bit Strings
```
(a) 8-bit: 2⁸ = 256
(b) Begin 000: 2⁵ = 32
(c) Begin and end with 1: 2⁶ = 64
```

### Exercise 13: Four Coins
```
(a) Total: 2⁴ = 16
(b) P(2 heads) = 6/16 = 3/8
(c) P(1 head) = 4/16 = 1/4
```

### Exercise 16: Two-Digit Integers
```
(a) Total: 90
(b) Odd: 45
(c) Distinct: 81
(d) Distinct and odd: 40
(e) P(distinct) = 9/10, P(distinct & odd) = 4/9
```

### Exercise 24-28: Loop Iterations
```
24: 30 × 15 = 450
25: m × n
26: m × n × p
27: 46 × 11 = 506
28: (b-a+1) × (d-c+1)
```

### Exercise 32: ALGORITHM
```
(a) 9! = 362,880
(b) AL as unit: 8! = 40,320
(c) GOR as unit: 7! = 5,040
```

### Exercise 37: Evaluate P(n, r)
```
(a) P(6,4) = 360
(b) P(6,6) = 720
(c) P(6,3) = 120
(d) P(6,1) = 6
```

### Exercise 39: ALGORITHM r-Perms
```
(a) P(9,3) = 504
(b) P(9,6) = 60,480
(c) First A: 6,720
(d) First OR: 840
```

### Exercise 40: Prove Identity
```
P(n+1, 3) = (n+1)×n×(n-1) = n³ - n ✓
```

### Exercise 43: Prove Identity
```
P(n, n) = n! = P(n, n-1) ✓
```

---

## 🔑 Key Formulas

### Multiplication Rule
```
n₁ × n₂ × ... × nₖ
```

### Permutations
```
n! = n × (n-1) × (n-2) × ... × 1
```

### r-Permutations
```
P(n, r) = n! / (n-r)!
        = n × (n-1) × ... × (n-r+1)
```

### Loop Iterations
```
Single: n iterations
Nested: m × n iterations
Triple: m × n × p iterations
```

---

## ⚠️ Common Mistakes

### Mistake 1: Adding Instead of Multiplying
```
✗ 3 + 5 = 8 routes
✓ 3 × 5 = 15 routes
```

### Mistake 2: Not Canceling
```
✗ P(15, 2) = 15!/13! = (compute huge numbers)
✓ P(15, 2) = 15 × 14 = 210
```

### Mistake 3: Wrong Constraint Handling
```
✗ Begin with 000: 2⁸ = 256
✓ Begin with 000: 2⁵ = 32 (only 5 free positions)
```

### Mistake 4: Dependent Choices
```
✗ Distinct digits: 10 × 10 = 100
✓ Distinct digits: 9 × 9 = 81 (second depends on first)
```

### Mistake 5: Wrong Loop Count
```
✗ for i = 5 to 50: 50 - 5 = 45
✓ for i = 5 to 50: 50 - 5 + 1 = 46
```

---

## 🚀 Exam Strategy

### For Multiplication Rule
- [ ] Identify all steps
- [ ] Count choices per step
- [ ] Verify independence
- [ ] Multiply

### For Permutations
- [ ] Check if all n or just r
- [ ] Apply n! or P(n,r)
- [ ] Cancel before computing
- [ ] Verify answer reasonable

### For Constraints
- [ ] Fix constrained positions first
- [ ] Count remaining choices
- [ ] Apply multiplication rule
- [ ] Verify with small example

### For Loops
- [ ] Count each loop range (n-m+1)
- [ ] Multiply all ranges
- [ ] Verify independence

### Time Management
- Multiplication rule: 3-5 min
- Permutations: 3-5 min
- Constrained: 5-8 min
- Loops: 2-3 min
- Proofs: 10-15 min

---

**You're ready to master counting! 🎉**

---

**End of Guide**
