# Chapter 4.4 Quick Reference: Recursion-Tree Method

**One-page cheat sheet for midterm**

---

## 🎯 The Five-Step Process

### 1. Draw the tree
```
Root = original problem
Children = recursive calls
Continue to base case
```

### 2. Calculate cost per level
```
Level i: a^i nodes × f(n/b^i) each
```

### 3. Find height
```
Divide by b: log_b n
Subtract 1: n
```

### 4. Sum all levels
```
Identify pattern (geometric series)
Determine which dominates
```

### 5. Verify with substitution
```
Use guess in induction proof
```

---

## 🔑 Three Key Patterns

### Pattern 1: Root Dominates (r < 1)

**When:** Cost decreases geometrically

**Example:** T(n) = T(n/2) + n³
```
Costs: n³, n³/8, n³/64, ...
Ratio: 1/8 < 1
Result: Θ(n³)
```

**Recognition:** Single call OR large f(n)

---

### Pattern 2: All Levels Equal (r = 1)

**When:** Cost constant per level

**Example:** T(n) = 2T(n/2) + n
```
Costs: n, n, n, ...
All levels: n
Height: lg n
Result: Θ(n lg n)
```

**Recognition:** a = b^k where f(n) = Θ(n^k)

---

### Pattern 3: Leaves Dominate (r > 1)

**When:** Cost increases geometrically

**Example:** T(n) = 4T(n/2) + n
```
Costs: n, 2n, 4n, 8n, ...
Ratio: 2 > 1
Leaves: n²
Result: Θ(n²)
```

**Recognition:** a > b^k where f(n) = Θ(n^k)

---

## 📊 Quick Pattern Matcher

### For T(n) = aT(n/b) + n^k

**Calculate:** r = a/b^k

| Ratio | Dominates | Result |
|-------|-----------|--------|
| r < 1 | Root | Θ(n^k) |
| r = 1 | All equal | Θ(n^k lg n) |
| r > 1 | Leaves | Θ(n^(log_b a)) |

---

## 🧮 Essential Formulas

### Geometric Series
```
Σ(i=0 to k) r^i = (r^(k+1) - 1)/(r - 1)

r < 1: Sum ≈ 1/(1-r) (converges)
r = 1: Sum = k+1
r > 1: Sum ≈ r^k/(r-1) (last term dominates)
```

### Logarithms
```
lg(n/2) = lg n - 1
log_b n = lg n / lg b
b^(log_b n) = n
a^(log_b n) = n^(log_b a)
```

### Tree Properties
```
Height (divide by b): log_b n
Height (subtract 1): n
Nodes at level i: a^i
Total leaves: a^(height)
```

---

## 📋 Exercise Quick Reference

### 4.4-1(a): T(n) = T(n/2) + n³
```
Pattern: Root dominates (r = 1/8)
Guess: O(n³)
Verify: c ≥ 8/7
```

### 4.4-1(b): T(n) = 4T(n/3) + n
```
Pattern: Leaves dominate (r = 4/3)
Guess: O(n^(log₃ 4)) ≈ O(n^1.262)
Verify: Need cn^α - dn
```

### 4.4-1(c): T(n) = 4T(n/2) + n
```
Pattern: Leaves dominate (r = 2)
Sum: 2n² - n
Guess: O(n²)
Verify: Need cn² - dn
```

### 4.4-1(d): T(n) = 3T(n-1) + 1
```
Pattern: Exponential
Sum: (3^n - 1)/2
Guess: O(3^n)
Verify: Need c·3^n - d
```

### 4.4-2: L(n) = L(n/3) + L(2n/3) + 1
```
Prove: L(n) ≥ cn
Key: n/3 + 2n/3 = n
Result: Θ(n)
```

### 4.4-3: T(n) = T(n/3) + T(2n/3) + cn
```
Cost per level: cn
Height: Θ(lg n)
Result: Θ(n lg n)
```

### 4.4-4: T(n) = T(αn) + T((1-α)n) + Θ(n)
```
Cost per level: cn
Height: Θ(lg n) (any α)
Result: Θ(n lg n)
```

---

## 💡 Quick Decision Guide

### Step 1: Identify Type
```
T(n/b): Divide-and-conquer
T(n-1): Linear decrease
```

### Step 2: Calculate Ratio
```
For T(n) = aT(n/b) + n^k:
r = a/b^k
```

### Step 3: Determine Domination
```
r < 1: Root → Θ(n^k)
r = 1: Equal → Θ(n^k lg n)
r > 1: Leaves → Θ(n^(log_b a))
```

### Step 4: Verify
```
Use substitution method
May need lower-order terms
```

---

## ⚠️ Common Pitfalls

### Drawing
- ❌ Wrong number of nodes per level
- ❌ Wrong cost per node
- ❌ Forgetting to label costs

### Analyzing
- ❌ Not identifying pattern
- ❌ Wrong geometric series formula
- ❌ Forgetting leaves

### Verifying
- ❌ Not using substitution
- ❌ Not modifying failed guess
- ❌ Skipping base case

---

## 💪 Quick Self-Test

### Can you answer in 30 seconds?

1. **T(n) = 2T(n/2) + n → ?**
   - Θ(n lg n)

2. **T(n) = T(n/2) + n² → ?**
   - Θ(n²)

3. **T(n) = 4T(n/2) + n → ?**
   - Θ(n²)

4. **When do leaves dominate?**
   - When r = a/b^k > 1

5. **Height for T(n/3)?**
   - log₃ n

---

## 🎓 Key Takeaways

### The Power of Visualization
```
Tree shows WHERE cost comes from
Pattern shows WHICH level dominates
Sum gives TOTAL cost
```

### Three Scenarios
```
Decreasing: Root wins
Constant: All equal
Increasing: Leaves win
```

### Always Verify
```
Tree gives intuition
Substitution gives proof
Both together = complete solution
```

---

## 🚀 Exam Checklist

### Before Drawing
- [ ] Identify a and b
- [ ] Identify f(n)
- [ ] Predict pattern

### While Drawing
- [ ] Label all costs
- [ ] Show first 3-4 levels
- [ ] Calculate pattern
- [ ] Find height

### After Drawing
- [ ] Sum levels
- [ ] Make guess
- [ ] Verify with substitution
- [ ] State conclusion

---

**You got this! 🎉**

---

**End of Cheat Sheet**
