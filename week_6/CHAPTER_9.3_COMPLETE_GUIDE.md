# Chapter 9.3 Complete Guide: Counting Elements of Disjoint Sets

**Course:** CS3112 - Introduction to Algorithms (Discrete Math Component)  
**Section:** 9.3 - The Addition Rule and Inclusion/Exclusion  
**Purpose:** Master advanced counting techniques for overlapping sets

---

## 🎯 What Chapter 9.3 Is Really About

### The Big Picture

Chapter 9.3 teaches you **how to count unions** - essential for analyzing algorithms with multiple cases.

**Mental model:** The inclusion/exclusion principle is like **avoiding double-counting**:
- Add individual sets
- Subtract overlaps (counted twice)
- Add back triple overlaps (subtracted too much)
- Continue pattern...

**Why it's important:**
- **Algorithm analysis:** Count cases that satisfy multiple conditions
- **Probability:** Calculate P(A or B)
- **Set operations:** Understand unions and intersections
- **Real-world problems:** Survey data, scheduling conflicts

**Key insight:** When sets overlap, simple addition double-counts! Must subtract intersections.

---

## 📚 Core Theorems

### Theorem 9.3.1: The Addition Rule

**For mutually disjoint sets:**

If A = A₁ ∪ A₂ ∪ ... ∪ Aₖ and the sets are pairwise disjoint, then:
```
N(A) = N(A₁) + N(A₂) + ... + N(Aₖ)
```

**Key requirement:** Sets must be DISJOINT (no overlap)

**Example:**
```
Bit strings of length 1, 2, 3, or 4:
N(total) = N(length 1) + N(length 2) + N(length 3) + N(length 4)
         = 2¹ + 2² + 2³ + 2⁴
         = 2 + 4 + 8 + 16
         = 30
```

---

### Theorem 9.3.2: The Difference Rule

**For subset B ⊆ A:**
```
N(A - B) = N(A) - N(B)
```

**Application to complements:**
```
N(Aᶜ) = N(U) - N(A)
```

where U is the universe

**Example:**
```
Integers from 1 to 1000 that are NOT multiples of 3:
N(not multiples of 3) = 1000 - 333 = 667
```

---

### Theorem 9.3.3: Inclusion/Exclusion Rule

**For two sets:**
```
N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
```

**Why?** When we add N(A) + N(B), elements in A ∩ B are counted TWICE. Subtract once to correct.

**For three sets:**
```
N(A ∪ B ∪ C) = N(A) + N(B) + N(C)
                - N(A ∩ B) - N(A ∩ C) - N(B ∩ C)
                + N(A ∩ B ∩ C)
```

**Pattern:**
1. Add individual sets
2. Subtract pairwise intersections
3. Add triple intersections
4. Subtract quadruple intersections
5. Continue alternating...

---

## 🎓 Detailed Examples

### Example 1: Multiples of 3 or 5

**Problem:** How many integers from 1 to 1000 are multiples of 3 OR multiples of 5?

**Solution:**

**Step 1: Define sets**
```
A = multiples of 3 from 1 to 1000
B = multiples of 5 from 1 to 1000
A ∩ B = multiples of both 3 and 5 = multiples of 15
```

**Step 2: Count each set**
```
N(A): 3, 6, 9, ..., 999 = 3×1, 3×2, ..., 3×333
N(A) = 333

N(B): 5, 10, 15, ..., 1000 = 5×1, 5×2, ..., 5×200
N(B) = 200

N(A ∩ B): 15, 30, 45, ..., 990 = 15×1, 15×2, ..., 15×66
N(A ∩ B) = 66
```

**Step 3: Apply inclusion/exclusion**
```
N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
         = 333 + 200 - 66
         = 467
```

**Answer:** 467 integers are multiples of 3 or 5

---

### Example 2: Neither Multiples

**Problem:** How many integers from 1 to 1000 are NEITHER multiples of 3 NOR multiples of 5?

**Solution:**

**Use complement:**
```
N(neither) = N(Aᶜ ∩ Bᶜ)
           = N((A ∪ B)ᶜ)    [De Morgan's Law]
           = N(U) - N(A ∪ B)  [Difference Rule]
           = 1000 - 467
           = 533
```

**Answer:** 533 integers are neither multiples of 3 nor 5

---

### Example 3: Three-Set Problem

**Problem:** In a class of 50 students:
- 30 took precalculus (P)
- 18 took calculus (C)
- 26 took Java (J)
- 9 took both P and C
- 16 took both P and J
- 8 took both C and J
- 47 took at least one course

**Find:** How many took all three courses?

**Solution:**

**Apply inclusion/exclusion:**
```
N(P ∪ C ∪ J) = N(P) + N(C) + N(J)
               - N(P ∩ C) - N(P ∩ J) - N(C ∩ J)
               + N(P ∩ C ∩ J)

47 = 30 + 18 + 26 - 9 - 16 - 8 + N(P ∩ C ∩ J)
47 = 74 - 33 + N(P ∩ C ∩ J)
47 = 41 + N(P ∩ C ∩ J)
N(P ∩ C ∩ J) = 6
```

**Answer:** 6 students took all three courses

---

## 💡 Venn Diagram Technique

### For Three Sets

**Given data, fill in diagram from inside out:**

```
        P           J
    ┌─────────────────┐
    │   a   │ d │  b  │
    │       └───┘     │
    │   e  │ f │  g  │
    └──────┴───┴─────┘
         │  c  │
         └─────┘
           C
```

**Regions:**
- f = P ∩ C ∩ J (all three)
- d = P ∩ J but not C
- e = P ∩ C but not J
- c = C ∩ J but not P
- a = P only
- b = J only
- g = C only

**Fill in order:**
1. Start with f (center)
2. Work outward to d, e, c
3. Calculate a, b, g from totals

---

## 🔑 Key Formulas

### Counting Multiples

**Multiples of d from 1 to n:**
```
Count = ⌊n/d⌋
```

**Example:**
```
Multiples of 7 from 1 to 1000:
⌊1000/7⌋ = ⌊142.857...⌋ = 142
```

---

### Repeated Digits

**Integers with NO repeated digits:**
```
Two-digit: 9 × 9 = 81
  (first digit: 1-9, second: 0-9 except first)

Three-digit: 9 × 9 × 8 = 648
  (first: 1-9, second: 0-9 except first, third: 0-9 except first two)
```

**Integers with AT LEAST ONE repeated digit:**
```
Total - (no repeated) = with repeated

Two-digit: 90 - 81 = 9
Three-digit: 900 - 648 = 252
```

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Disjoint Sets (Addition Rule)

**Given:** Multiple non-overlapping cases
**Task:** Count total

**Steps:**
1. Verify sets are disjoint
2. Count each set separately
3. Add all counts

---

### Framework 2: Overlapping Sets (Inclusion/Exclusion)

**Given:** Sets that may overlap
**Task:** Count union

**Steps:**
1. Define sets clearly
2. Count individual sets
3. Count intersections
4. Apply inclusion/exclusion formula
5. Calculate result

---

### Framework 3: Complement Counting

**Given:** Hard to count directly
**Task:** Count by complement

**Steps:**
1. Define universe U
2. Count complement
3. Subtract from universe
4. N(A) = N(U) - N(Aᶜ)

---

### Framework 4: Venn Diagram

**Given:** Three-set problem with various intersections
**Task:** Find specific region

**Steps:**
1. Draw Venn diagram
2. Fill in center first (all three)
3. Work outward to pairwise intersections
4. Calculate individual-only regions
5. Extract answer

---

## ⚠️ Common Mistakes

### Mistake 1: Adding When Sets Overlap
```
✗ N(A ∪ B) = N(A) + N(B) when A and B overlap
✓ N(A ∪ B) = N(A) + N(B) - N(A ∩ B)
```

### Mistake 2: Wrong Intersection for LCM
```
✗ Multiples of 3 AND 5 = multiples of 8
✓ Multiples of 3 AND 5 = multiples of 15 (LCM)
```

### Mistake 3: Forgetting De Morgan's Law
```
✗ N(neither A nor B) = N(U) - N(A) - N(B)
✓ N(neither A nor B) = N(U) - N(A ∪ B)
```

### Mistake 4: Wrong Sign in Inclusion/Exclusion
```
✗ N(A ∪ B ∪ C) = N(A) + N(B) + N(C) - ... - N(A ∩ B ∩ C)
✓ N(A ∪ B ∪ C) = N(A) + N(B) + N(C) - ... + N(A ∩ B ∩ C)
```

### Mistake 5: Not Counting from Inside Out
```
✗ Fill Venn diagram randomly
✓ Start with center (all three), work outward
```

---

## 🚀 Exam Strategy

### For Addition Rule
- [ ] Verify sets are disjoint
- [ ] Count each set
- [ ] Add totals
- [ ] Verify no overlap

### For Inclusion/Exclusion
- [ ] Define sets clearly
- [ ] Count all individual sets
- [ ] Count all intersections
- [ ] Apply formula carefully
- [ ] Check signs (alternating)

### For Complement
- [ ] Define universe
- [ ] Count complement
- [ ] Subtract from universe
- [ ] Verify answer reasonable

### For Venn Diagrams
- [ ] Draw diagram
- [ ] Fill center first
- [ ] Work outward systematically
- [ ] Verify all regions sum correctly

### Time Management
- Addition rule: 3-5 min
- Two-set inclusion/exclusion: 5-8 min
- Three-set problems: 10-15 min
- Venn diagrams: 8-12 min

---

**You're ready to master counting unions! 🎉**

---

**End of Guide**
