# Chapter 9.2 Complete Guide: Possibility Trees and the Multiplication Rule

**Course:** CS3112 - Introduction to Algorithms (Discrete Math Component)  
**Section:** 9.2 - Possibility Trees and the Multiplication Rule  
**Purpose:** Master counting techniques for algorithm analysis

---

## 🎯 What Chapter 9.2 Is Really About

### The Big Picture

Chapter 9.2 teaches you **systematic counting** - the foundation for analyzing algorithms with multiple choices.

**Mental model:** The multiplication rule is like **counting paths through decisions**:
- Each decision has multiple choices
- Total outcomes = multiply choices at each step
- Possibility trees visualize all paths

**Why it's important:**
- **Algorithm analysis:** Count loop iterations, function calls
- **Nested loops:** Understand why they're expensive
- **Permutations:** Analyze ordering problems
- **Combinatorics:** Foundation for advanced counting

**Key insight:** When making sequential choices, MULTIPLY the number of options!

---

## 📚 The Multiplication Rule

### Theorem 9.2.1: The Multiplication Rule

**If an operation consists of k steps:**
- Step 1 can be performed in n₁ ways
- Step 2 can be performed in n₂ ways
- ...
- Step k can be performed in nₖ ways

**Then the entire operation can be performed in:**
```
n₁ × n₂ × n₃ × ... × nₖ ways
```

**Key requirement:** Number of ways to perform each step is independent of previous choices

---

### Simple Examples

**Example 1: Computer System**
```
Choose: Basic unit (3 models) + Keyboard (2 models) + Printer (2 models)

Step 1: Choose unit (3 ways)
Step 2: Choose keyboard (2 ways)
Step 3: Choose printer (2 ways)

Total: 3 × 2 × 2 = 12 different systems
```

**Example 2: Travel Routes**
```
City A → City B: 3 roads
City B → City C: 5 roads

Total routes A to C via B: 3 × 5 = 15 routes
```

**Example 3: Bit Strings**
```
8-bit string: each position is 0 or 1

Position 1: 2 choices
Position 2: 2 choices
...
Position 8: 2 choices

Total: 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2⁸ = 256 bit strings
```

---

## 🎓 Possibility Trees

### What Is a Possibility Tree?

**Definition:** A tree diagram showing all possible outcomes of a multi-step process

**Structure:**
- Root = starting point
- Branches = choices at each step
- Leaves = final outcomes

**How to count:** Count the leaves!

---

### Example: Two Coin Tosses

```
                Start
               /     \
              H       T      (First toss)
             / \     / \
            H   T   H   T    (Second toss)
            |   |   |   |
           HH  HT  TH  TT    (Outcomes)
```

**Count:** 4 leaves = 4 outcomes

**Using multiplication rule:** 2 × 2 = 4 ✓

---

### Example: Three Roads, Two Choices

```
                Start
            /    |    \
           R1   R2    R3     (Choose road A→B)
          / \   / \   / \
         C1 C2 C1 C2 C1 C2   (Choose road B→C)
```

**Count:** 6 leaves = 6 routes

**Using multiplication rule:** 3 × 2 = 6 ✓

---

## 🔑 Permutations

### Definition

**Permutation:** An ordered arrangement of elements

**Notation:** n! (n factorial)
```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

**Examples:**
```
3! = 3 × 2 × 1 = 6
4! = 4 × 3 × 2 × 1 = 24
5! = 5 × 4 × 3 × 2 × 1 = 120
0! = 1 (by definition)
```

---

### Theorem 9.2.2: Number of Permutations

**The number of permutations of n elements is n!**

**Why?**
```
Position 1: n choices
Position 2: n-1 choices (one used)
Position 3: n-2 choices (two used)
...
Position n: 1 choice (all others used)

Total: n × (n-1) × (n-2) × ... × 1 = n!
```

**Example:** Arrange letters in COMPUTER
```
8 distinct letters
Number of arrangements: 8! = 40,320
```

---

## 💡 r-Permutations

### Definition

**r-permutation:** Ordered selection of r elements from n elements

**Notation:** P(n, r) or ₙPᵣ

**Formula (two versions):**
```
P(n, r) = n(n-1)(n-2)...(n-r+1)  [first version - r factors]

P(n, r) = n! / (n-r)!             [second version - easier to remember]
```

---

### Why the Formula Works

**Selecting r elements in order:**
```
Position 1: n choices
Position 2: n-1 choices
Position 3: n-2 choices
...
Position r: n-r+1 choices

Total: n × (n-1) × (n-2) × ... × (n-r+1) = P(n, r)
```

**Why n!/(n-r)!?**
```
n! = n × (n-1) × ... × (n-r+1) × (n-r) × ... × 1
                  ↑ r factors ↑    ↑ (n-r)! ↑

Divide by (n-r)! to get just the first r factors!
```

---

### Examples

**P(5, 2):**
```
Method 1: 5 × 4 = 20
Method 2: 5! / 3! = 120 / 6 = 20 ✓
```

**P(7, 4):**
```
Method 1: 7 × 6 × 5 × 4 = 840
Method 2: 7! / 3! = 5040 / 6 = 840 ✓
```

**P(5, 5):**
```
Method 1: 5 × 4 × 3 × 2 × 1 = 120
Method 2: 5! / 0! = 120 / 1 = 120 ✓
```

**Note:** P(n, n) = n! (all permutations)

---

## 📊 Application to Nested Loops

### Counting Loop Iterations

**Single loop:**
```
for i = 1 to n
    [body]
    
Iterations: n
```

**Nested loops (independent):**
```
for i = 1 to m
    for j = 1 to n
        [body]
        
Iterations: m × n
```

**Triple nested:**
```
for i = 1 to m
    for j = 1 to n
        for k = 1 to p
            [body]
            
Iterations: m × n × p
```

---

### Example: Specific Ranges

**Problem:** Count iterations
```
for i = 5 to 50
    for j = 10 to 20
        [body]
```

**Solution:**
```
Outer loop: 50 - 5 + 1 = 46 iterations
Inner loop: 20 - 10 + 1 = 11 iterations
Total: 46 × 11 = 506 iterations
```

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Apply Multiplication Rule

**Given:** Multi-step process
**Task:** Count total outcomes

**Steps:**
1. Identify number of steps
2. Count choices for each step
3. Verify independence
4. Multiply all counts

---

### Framework 2: Draw Possibility Tree

**Given:** Sequential choices
**Task:** Visualize all outcomes

**Steps:**
1. Draw root
2. Branch for each choice at step 1
3. From each branch, branch again for step 2
4. Continue for all steps
5. Count leaves

---

### Framework 3: Calculate Permutations

**Given:** n objects, arrange all
**Task:** Count arrangements

**Steps:**
1. Verify all objects distinct
2. Apply n!
3. Calculate result

---

### Framework 4: Calculate r-Permutations

**Given:** n objects, select and arrange r
**Task:** Count ordered selections

**Steps:**
1. Identify n and r
2. Apply P(n, r) = n!/(n-r)!
3. Cancel (n-r)! before computing
4. Calculate result

---

## ⚠️ Common Mistakes

### Mistake 1: Adding Instead of Multiplying
```
✗ 3 units + 2 keyboards + 2 printers = 7
✓ 3 × 2 × 2 = 12
```

### Mistake 2: Not Canceling Factorials
```
✗ P(15, 2) = 15! / 13! = (huge number) / (huge number)
✓ P(15, 2) = 15 × 14 = 210 (cancel first!)
```

### Mistake 3: Wrong Loop Count
```
✗ for i = 1 to n: n-1 iterations
✓ for i = 1 to n: n iterations
```

### Mistake 4: Dependent Steps
```
✗ Using multiplication rule when choices depend on previous
✓ Verify independence before multiplying
```

### Mistake 5: Confusing P(n,r) with nʳ
```
✗ P(5, 2) = 5² = 25 (with replacement)
✓ P(5, 2) = 5 × 4 = 20 (without replacement)
```

---

## 🚀 Exam Strategy

### For Multiplication Rule
- [ ] Identify all steps
- [ ] Count choices per step
- [ ] Verify independence
- [ ] Multiply

### For Possibility Trees
- [ ] Draw systematically
- [ ] Label all branches
- [ ] Count leaves
- [ ] Verify with multiplication rule

### For Permutations
- [ ] Identify n (total objects)
- [ ] Identify r (objects to arrange)
- [ ] Apply correct formula
- [ ] Cancel before computing

### For Loop Counting
- [ ] Count outer loop iterations
- [ ] Count inner loop iterations
- [ ] Multiply
- [ ] Use n - m + 1 for ranges

### Time Management
- Multiplication rule: 3-5 min
- Possibility tree: 5-10 min
- Permutations: 3-5 min
- Loop counting: 3-5 min

---

**You're ready to master counting! 🎉**

---

**End of Guide**
