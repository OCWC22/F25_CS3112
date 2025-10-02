# Chapter 9.3 Quick Reference: Addition Rule & Inclusion/Exclusion

**One-page cheat sheet for midterm**

---

## 🎯 Core Formulas

### Addition Rule (Disjoint Sets)
```
If A₁, A₂, ..., Aₖ are pairwise disjoint:
N(A₁ ∪ A₂ ∪ ... ∪ Aₖ) = N(A₁) + N(A₂) + ... + N(Aₖ)
```

### Difference Rule
```
N(A - B) = N(A) - N(B)  [if B ⊆ A]
N(Aᶜ) = N(U) - N(A)
```

### Inclusion/Exclusion (Two Sets)
```
N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
```

### Inclusion/Exclusion (Three Sets)
```
N(A ∪ B ∪ C) = N(A) + N(B) + N(C)
                - N(A ∩ B) - N(A ∩ C) - N(B ∩ C)
                + N(A ∩ B ∩ C)
```

---

## 🔑 Key Patterns

### Pattern: Add, Subtract, Add
```
2 sets: + + -
3 sets: + + + - - - +
4 sets: + + + + - - - - - - + + + + -
```

### Counting Multiples
```
Multiples of d from 1 to n: ⌊n/d⌋

Multiples of BOTH d₁ and d₂: ⌊n/lcm(d₁,d₂)⌋
```

### Complement Technique
```
N(at least one) = N(U) - N(none)
N(neither A nor B) = N(U) - N(A ∪ B)
```

---

## 💡 Quick Examples

### Multiples of 3 or 5 (1 to 1000)
```
A = multiples of 3: 333
B = multiples of 5: 200
A ∩ B = multiples of 15: 66

N(A ∪ B) = 333 + 200 - 66 = 467
```

### Neither 3 nor 5
```
N(neither) = 1000 - 467 = 533
```

### Repeated Digits
```
Two-digit (10-99):
Total: 90
No repeat: 9 × 9 = 81
At least one repeat: 90 - 81 = 9
```

---

## 📊 Venn Diagram Technique

### Three Sets - Fill Order
```
1. Center (A ∩ B ∩ C)
2. Pairwise only:
   - A ∩ B but not C
   - A ∩ C but not B
   - B ∩ C but not A
3. Individual only:
   - A only
   - B only
   - C only
```

### Example Layout
```
     A           B
  ┌──────────────┐
  │ a  │ d │  b  │
  │    └───┘    │
  │ e  │ f │  g │
  └────┴───┴────┘
      │ c │
      └───┘
        C

f = all three
d, e, c = pairwise
a, b, g = individual
```

---

## 🧮 Common Calculations

### LCM for Intersections
```
Multiples of 3 AND 5: lcm(3,5) = 15
Multiples of 4 AND 6: lcm(4,6) = 12
Multiples of 6 AND 9: lcm(6,9) = 18
```

### Counting Formulas
```
⌊1000/3⌋ = 333
⌊1000/5⌋ = 200
⌊1000/15⌋ = 66
⌊1000/7⌋ = 142
```

---

## 📋 Exercise Quick Reference

### Ex 23: Multiples of 4 or 7
```
A = mult of 4: 250
B = mult of 7: 142
A ∩ B = mult of 28: 35
N(A ∪ B) = 250 + 142 - 35 = 357
```

### Ex 3: No Repeated Digits (1-999)
```
1-digit: 9
2-digit: 9 × 9 = 81
3-digit: 9 × 9 × 8 = 648
Total: 9 + 81 + 648 = 738
At least one repeat: 999 - 738 = 261
```

### Ex 16: Seven-Digit Phone
```
Total: 10⁷ = 10,000,000
No repeat: P(10,7) = 10×9×8×7×6×5×4 = 604,800
At least one repeat: 10,000,000 - 604,800 = 9,395,200
```

---

## ⚠️ Common Pitfalls

### Inclusion/Exclusion
- ❌ Adding when sets overlap
- ❌ Wrong LCM for intersection
- ❌ Wrong sign pattern
- ❌ Forgetting triple intersection

### Complement
- ❌ Not using De Morgan's Law
- ❌ Subtracting individual sets instead of union
- ❌ Wrong universe size

### Venn Diagrams
- ❌ Not filling from center outward
- ❌ Regions don't sum to total
- ❌ Negative region values

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **N(A ∪ B) if N(A)=50, N(B)=30, N(A∩B)=10?**
   - 70

2. **Multiples of 6 from 1 to 100?**
   - 16

3. **Neither A nor B formula?**
   - N(U) - N(A ∪ B)

4. **Three-set formula sign pattern?**
   - + + + - - - +

5. **LCM(4, 6)?**
   - 12

---

## 🚀 Exam Checklist

### Before Solving
- [ ] Identify if sets are disjoint
- [ ] Define all sets clearly
- [ ] Determine which formula applies

### While Solving
- [ ] Count each set carefully
- [ ] Find correct LCM for intersections
- [ ] Apply formula with correct signs
- [ ] Verify answer reasonable

### For Three Sets
- [ ] Use Venn diagram if helpful
- [ ] Fill from center outward
- [ ] Check all regions sum correctly
- [ ] Extract requested information

---

**You got this! 🎉**

---

**End of Cheat Sheet**
