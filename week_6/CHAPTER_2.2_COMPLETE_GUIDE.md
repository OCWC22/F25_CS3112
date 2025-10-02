# Chapter 2.2 Complete Guide: Analyzing Algorithms

**Course:** CS3112 - Introduction to Algorithms  
**Section:** 2.2 - Analyzing Algorithms  
**Purpose:** Master algorithm analysis and the RAM model

---

## 🎯 What Chapter 2.2 Is Really About

### The Big Picture

Chapter 2.2 teaches you **how to analyze algorithms** - predicting how long they take without running them.

**Mental model:** Algorithm analysis is like **predicting a car's fuel efficiency**:
- Don't need to drive it to know
- Count operations (like counting engine cycles)
- Express as function of input size
- Compare different algorithms

**Why it's important:**
- **Prediction:** Know performance before implementing
- **Comparison:** Choose best algorithm for the job
- **Understanding:** See where time is spent
- **Foundation:** All algorithm analysis uses these techniques

**Key insight:** You can predict performance mathematically, without running code!

---

## 📚 The RAM Model

### What Is the RAM Model?

**RAM = Random Access Machine**

**Key assumptions:**
1. **Sequential execution:** One instruction at a time
2. **Constant-time operations:** Each instruction takes same time
3. **Constant-time memory access:** Array indexing is O(1)
4. **Simple instructions:** Arithmetic, data movement, control

**What it includes:**
- Arithmetic: +, -, ×, ÷, mod, floor, ceiling
- Data movement: load, store, copy
- Control: if-else, loops, function calls

**What it excludes:**
- Parallel operations
- Memory hierarchy (caches)
- Complex instructions (like "sort")

---

### Why Use RAM Model?

**Advantages:**
- Simple and clean
- Machine-independent
- Good predictor of real performance
- Easy to analyze

**Limitations:**
- Ignores cache effects
- Ignores memory hierarchy
- Assumes all operations equal
- Oversimplifies modern CPUs

**But:** Good enough for algorithm comparison!

---

## 🎓 Analyzing Insertion Sort

### The Detailed Analysis

**Pseudocode with costs:**

```
INSERTION-SORT(A, n)                    cost    times
1  for i = 2 to n                       c₁      n
2      key = A[i]                       c₂      n-1
3      // Insert A[i] into sorted...    0       n-1
4      j = i - 1                        c₄      n-1
5      while j > 0 and A[j] > key       c₅      Σᵢ₌₂ⁿ tᵢ
6          A[j+1] = A[j]                c₆      Σᵢ₌₂ⁿ (tᵢ-1)
7          j = j - 1                    c₇      Σᵢ₌₂ⁿ (tᵢ-1)
8      A[j+1] = key                     c₈      n-1
```

**Where:**
- cₖ = cost of line k
- tᵢ = number of times while loop test executes for iteration i

---

### Total Running Time

**Formula:**
```
T(n) = c₁n + c₂(n-1) + c₄(n-1) + c₅Σtᵢ + c₆Σ(tᵢ-1) + c₇Σ(tᵢ-1) + c₈(n-1)
```

**This depends on tᵢ, which varies by input!**

---

### Best Case Analysis

**When:** Array already sorted

**What happens:**
- Each time line 5 executes, A[j] ≤ key immediately
- While loop exits after first test
- tᵢ = 1 for all i

**Running time:**
```
T(n) = c₁n + c₂(n-1) + c₄(n-1) + c₅(n-1) + c₈(n-1)
     = (c₁ + c₂ + c₄ + c₅ + c₈)n - (c₂ + c₄ + c₅ + c₈)
     = an + b
```

**This is a linear function!**

**Best case: T(n) = Θ(n)**

---

### Worst Case Analysis

**When:** Array in reverse sorted order

**What happens:**
- Each time line 5 executes, must check all of A[1 : i-1]
- While loop runs i times (including final test)
- tᵢ = i for all i

**Calculate sums:**
```
Σᵢ₌₂ⁿ tᵢ = Σᵢ₌₂ⁿ i = (Σᵢ₌₁ⁿ i) - 1 = n(n+1)/2 - 1

Σᵢ₌₂ⁿ (tᵢ-1) = Σᵢ₌₂ⁿ (i-1) = Σᵢ₌₁ⁿ⁻¹ i = n(n-1)/2
```

**Running time:**
```
T(n) = c₁n + c₂(n-1) + c₄(n-1) + c₅(n(n+1)/2 - 1) 
     + c₆(n(n-1)/2) + c₇(n(n-1)/2) + c₈(n-1)
     
     = (c₅/2 + c₆/2 + c₇/2)n² 
     + (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)n 
     - (c₂ + c₄ + c₅ + c₈)
     
     = an² + bn + c
```

**This is a quadratic function!**

**Worst case: T(n) = Θ(n²)**

---

### Average Case Analysis

**When:** Random order

**What happens:**
- On average, A[i] compares with half of A[1 : i-1]
- tᵢ ≈ i/2 on average

**Running time:**
```
T(n) ≈ an² + bn + c (with smaller constants than worst case)
```

**Average case: T(n) = Θ(n²)**

**Key insight:** Average is roughly as bad as worst case (same asymptotic growth)!

---

## 📊 Why Focus on Worst Case?

### Three Reasons

**1. Upper Bound Guarantee**
- Worst case gives maximum time
- Algorithm never takes longer
- Essential for real-time systems

**2. Worst Case Often Common**
- Example: Searching for absent element
- Database queries often search for non-existent data
- Worst case isn't rare!

**3. Average ≈ Worst**
- For many algorithms, average case has same asymptotic growth
- Example: Insertion sort is Θ(n²) in both
- Worst case analysis often sufficient

---

## 🔑 From Detailed to Asymptotic

### The Simplification Process

**Step 1: Detailed formula**
```
T(n) = an² + bn + c
```

**Step 2: Identify dominant term**
```
For large n: n² >> n >> 1
Dominant term: an²
```

**Step 3: Drop constants and lower-order terms**
```
T(n) = Θ(n²)
```

**Why this works:**
- For large n, lower-order terms negligible
- Constants depend on machine, not algorithm
- Asymptotic notation captures growth rate

---

### Example: Simplify n³/1000 + 100n² - 100n + 3

**Step 1: Identify terms**
```
n³/1000  - cubic term
100n²    - quadratic term
-100n    - linear term
3        - constant term
```

**Step 2: Find dominant term**
```
For large n: n³ >> n² >> n >> 1
Dominant: n³/1000
```

**Step 3: Drop constants**
```
n³/1000 → n³
```

**Answer: Θ(n³)**

**Why?**
- As n → ∞, n³/1000 dominates
- Constant 1/1000 doesn't affect growth rate
- Other terms become negligible

---

## 💡 Selection Sort Example

### The Algorithm

**Idea:**
1. Find minimum element in A[1 : n]
2. Swap with A[1]
3. Find minimum in A[2 : n]
4. Swap with A[2]
5. Continue for n-1 elements

**Why n-1?** Last element automatically in place!

---

### Pseudocode

```
SELECTION-SORT(A, n)
1  for i = 1 to n - 1
2      min_index = i
3      for j = i + 1 to n
4          if A[j] < A[min_index]
5              min_index = j
6      swap A[i] with A[min_index]
```

---

### Loop Invariant

**Invariant:**
> At the start of each iteration of the for loop (line 1), the subarray A[1 : i-1] contains the i-1 smallest elements of the original array in sorted order.

**Key difference from insertion sort:**
- Insertion sort: A[1:i-1] contains ORIGINAL elements from those positions
- Selection sort: A[1:i-1] contains SMALLEST elements from entire array

---

### Running Time Analysis

**Outer loop:** n-1 iterations

**Inner loop (for each i):**
- Runs from i+1 to n
- Number of iterations: n - i
- Total: Σᵢ₌₁ⁿ⁻¹ (n-i) = (n-1) + (n-2) + ... + 1 = n(n-1)/2

**Total comparisons:**
```
Σᵢ₌₁ⁿ⁻¹ (n-i) = n(n-1)/2 = Θ(n²)
```

**Key insight:** ALWAYS makes n(n-1)/2 comparisons!

**Best case: Θ(n²)**
**Worst case: Θ(n²)**
**Average case: Θ(n²)**

**All cases are the same!** Selection sort always scans entire unsorted portion.

---

## 🎯 Linear Search Analysis

### The Algorithm

```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

---

### Best Case

**When:** x is first element (A[1])

**Time:** Θ(1) - constant time, one comparison

---

### Worst Case

**When:** x is not in array OR x is last element

**Time:** Θ(n) - must check all n elements

---

### Average Case

**Assumption:** x is equally likely to be any element

**Analysis:**
- Probability x is at position i: 1/n
- If at position i, need i comparisons
- Expected comparisons: (1/n)(1 + 2 + 3 + ... + n) = (1/n) × n(n+1)/2 = (n+1)/2

**Average case: Θ(n)**

**Key insight:** Average case is about half of worst case, but same asymptotic growth!

---

## 📋 Analysis Framework

### Framework for Any Algorithm

**Step 1: Identify input size**
- Usually n (number of elements)
- Sometimes multiple parameters

**Step 2: Count operations**
- How many times does each line execute?
- Consider loops carefully

**Step 3: Sum costs**
- Total = Σ (cost × times)

**Step 4: Identify dominant term**
- What grows fastest?

**Step 5: Express in Θ-notation**
- Drop constants and lower-order terms

---

### Framework for Loop Analysis

**Single loop:**
```
for i = 1 to n
    // constant work
    
Time: Θ(n)
```

**Nested loops:**
```
for i = 1 to n
    for j = 1 to n
        // constant work
        
Time: Θ(n²)
```

**Dependent nested loops:**
```
for i = 1 to n
    for j = i to n
        // constant work
        
Time: Σᵢ₌₁ⁿ (n-i+1) = n + (n-1) + ... + 1 = n(n+1)/2 = Θ(n²)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Counting Loop Iterations Wrong
```
✗ for i = 1 to n → n-1 iterations
✓ for i = 1 to n → n iterations
```

### Mistake 2: Forgetting Loop Test
```
✗ while loop runs k times → k operations
✓ while loop runs k times → k+1 tests (final test fails)
```

### Mistake 3: Wrong Summation
```
✗ Σᵢ₌₁ⁿ i = n²
✓ Σᵢ₌₁ⁿ i = n(n+1)/2
```

### Mistake 4: Not Dropping Constants
```
✗ T(n) = Θ(5n²)
✓ T(n) = Θ(n²)
```

### Mistake 5: Including Lower-Order Terms
```
✗ T(n) = Θ(n² + n)
✓ T(n) = Θ(n²)
```

---

## 🧮 Essential Summation Formulas

### Arithmetic Series
```
Σᵢ₌₁ⁿ i = 1 + 2 + 3 + ... + n = n(n+1)/2 ≈ n²/2

Σᵢ₌₁ⁿ i² = 1² + 2² + ... + n² = n(n+1)(2n+1)/6 ≈ n³/3
```

### Geometric Series
```
Σᵢ₌₀ⁿ 2ⁱ = 1 + 2 + 4 + ... + 2ⁿ = 2ⁿ⁺¹ - 1

Σᵢ₌₀^∞ rⁱ = 1/(1-r) for |r| < 1
```

### Logarithmic
```
Σᵢ₌₁ⁿ 1/i = ln n + O(1) (harmonic series)
```

---

## 🎯 Problem-Solving Frameworks

### Framework 1: Express in Θ-Notation

**Given:** Polynomial function
**Task:** Simplify to Θ-notation

**Steps:**
1. Identify all terms
2. Find highest-degree term
3. Drop constant coefficient
4. Express as Θ(dominant term)

**Example:** n³/1000 + 100n² - 100n + 3
- Highest degree: n³
- Answer: Θ(n³)

---

### Framework 2: Design and Analyze Algorithm

**Given:** Problem description
**Task:** Write pseudocode and analyze

**Steps:**
1. Design algorithm
2. Write pseudocode
3. State loop invariant
4. Count operations
5. Express running time
6. Determine best/worst/average cases

---

### Framework 3: Compare Algorithms

**Given:** Multiple algorithms for same problem
**Task:** Determine which is better

**Steps:**
1. Analyze each algorithm
2. Express in Θ-notation
3. Compare growth rates
4. Consider best/worst/average cases
5. Choose based on requirements

---

## 🚀 Exam Strategy

### For Θ-Notation Problems
- [ ] Identify dominant term
- [ ] Drop constants
- [ ] Drop lower-order terms
- [ ] Express clearly

### For Algorithm Design
- [ ] Write clear pseudocode
- [ ] State loop invariant
- [ ] Count operations
- [ ] Analyze all cases

### For Analysis Problems
- [ ] Count loop iterations
- [ ] Handle nested loops
- [ ] Sum correctly
- [ ] Simplify to Θ-notation

### Time Management
- Θ-notation: 2-3 min
- Algorithm design: 10-15 min
- Full analysis: 15-20 min

---

**You're ready to master algorithm analysis! 🎉**

---

**End of Guide**
