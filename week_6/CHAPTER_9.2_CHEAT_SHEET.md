# Chapter 9.2 Quick Reference: Multiplication Rule & Permutations

**One-page cheat sheet for midterm**

---

## 🎯 The Multiplication Rule

### Formula
```
If operation has k steps:
- Step 1: n₁ ways
- Step 2: n₂ ways
- ...
- Step k: nₖ ways

Total: n₁ × n₂ × ... × nₖ ways
```

### Key Requirement
```
Choices at each step must be INDEPENDENT
```

---

## 🔑 Permutations

### Full Permutations
```
n! = n × (n-1) × (n-2) × ... × 1

Examples:
3! = 6
4! = 24
5! = 120
0! = 1 (by definition)
```

### r-Permutations
```
P(n, r) = n! / (n-r)!
        = n × (n-1) × ... × (n-r+1)

Examples:
P(5, 2) = 5 × 4 = 20
P(7, 4) = 7 × 6 × 5 × 4 = 840
P(n, n) = n!
```

---

## 📊 Common Applications

### Bit Strings
```
n-bit string: 2ⁿ possibilities
Begin with k fixed bits: 2^(n-k)
Begin and end fixed: 2^(n-2)
```

### License Plates
```
4 letters + 3 digits: 26⁴ × 10³
Distinct letters: 26 × 25 × 24 × 23 × 10³
```

### Nested Loops
```
for i = 1 to m
    for j = 1 to n
        [body]
        
Iterations: m × n
```

---

## 💡 Quick Calculations

### Factorials
```
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5,040
8! = 40,320
```

### Powers of 2
```
2¹ = 2
2² = 4
2³ = 8
2⁴ = 16
2⁵ = 32
2⁶ = 64
2⁷ = 128
2⁸ = 256
```

### Common P(n, r)
```
P(5, 2) = 20
P(6, 3) = 120
P(7, 4) = 840
P(n, 1) = n
P(n, 2) = n(n-1)
```

---

## 🧮 Problem Patterns

### Pattern 1: Sequential Choices
```
Choose A (n ways), then B (m ways)
Total: n × m
```

### Pattern 2: Constrained Position
```
Fix constrained position first
Count remaining choices
Multiply
```

### Pattern 3: Units/Groups
```
Treat group as single object
Reduce n by (group size - 1)
Calculate permutations
```

### Pattern 4: Distinct Elements
```
First choice: n options
Second choice: n-1 options (can't repeat)
Apply P(n, r)
```

---

## 📋 Exercise Quick Reference

### Ex 8: Computer System
```
3 × 2 × 2 = 12 systems
```

### Ex 9: Routes
```
(a) A→C: 3 × 5 = 15
(b) Round-trip: 3 × 5 × 5 × 3 = 225
(c) No repeat: 3 × 5 × 4 × 2 = 120
```

### Ex 11: Bit Strings
```
(a) 8-bit: 2⁸ = 256
(b) Begin 000: 2⁵ = 32
(c) Begin/end 1: 2⁶ = 64
```

### Ex 13: Four Coins
```
(a) Total: 2⁴ = 16
(b) P(2 heads) = 6/16 = 3/8
(c) P(1 head) = 4/16 = 1/4
```

### Ex 16: Two-Digit
```
(a) Total: 90
(b) Odd: 45
(c) Distinct: 81
(d) Distinct & odd: 40
```

### Ex 24-28: Loops
```
24: 30 × 15 = 450
25: m × n
26: m × n × p
27: 46 × 11 = 506
28: (b-a+1)(d-c+1)
```

### Ex 32: ALGORITHM
```
(a) 9! = 362,880
(b) AL unit: 8! = 40,320
(c) GOR unit: 7! = 5,040
```

### Ex 37: P(6, r)
```
P(6,4) = 360
P(6,6) = 720
P(6,3) = 120
P(6,1) = 6
```

### Ex 39: ALGORITHM r-Perms
```
(a) P(9,3) = 504
(b) P(9,6) = 60,480
(c) First A: 6,720
(d) First OR: 840
```

---

## ⚠️ Common Pitfalls

### Multiplication Rule
- ❌ Adding instead of multiplying
- ❌ Not checking independence
- ❌ Wrong step count

### Permutations
- ❌ Not canceling factorials
- ❌ Computing huge numbers
- ❌ Forgetting 0! = 1

### Constraints
- ❌ Not fixing constrained positions first
- ❌ Double-counting
- ❌ Wrong remaining choices

### Loops
- ❌ Forgetting +1 in range count
- ❌ Wrong iteration count
- ❌ Not multiplying nested loops

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **3 choices, then 5 choices. Total?**
   - 15

2. **8-bit string, how many?**
   - 256

3. **P(5, 2) = ?**
   - 20

4. **5! = ?**
   - 120

5. **Nested loops m×n iterations?**
   - Yes

---

## 🚀 Exam Checklist

### Before Solving
- [ ] Identify problem type
- [ ] Check if multiplication rule applies
- [ ] Verify independence

### While Solving
- [ ] Count systematically
- [ ] Fix constraints first
- [ ] Cancel before computing
- [ ] Verify reasonableness

### For Permutations
- [ ] Identify n and r
- [ ] Use P(n,r) = n!/(n-r)!
- [ ] Cancel (n-r)! immediately
- [ ] Compute remaining factors

---

**You got this! 🎉**

---

**End of Cheat Sheet**
