# CS3112 Homework Solutions: Sections 2.1 & 2.2
## Introduction to Algorithms - Insertion Sort & Algorithm Analysis

**Student Guide**: These solutions are designed for complete understanding from ground zero. Every step is explained with the "what" and "why" so you can solve similar problems independently on exams.

---

## 📚 SECTION 2.1: Insertion Sort

### **Background Concepts You Need to Know**

Before solving these problems, let's establish the foundational concepts:

#### **What is Insertion Sort?**
- **Analogy**: Think of sorting a hand of playing cards
- You pick up cards one at a time from a pile
- Each new card is inserted into its correct position among the cards already in your hand
- The cards in your hand are always sorted

#### **How Does Insertion Sort Work?**
```
Initial Array: [5, 2, 4, 6, 1, 3]

Step 1: Start with first element (5) - already "sorted"
        [5 | 2, 4, 6, 1, 3]
        
Step 2: Take 2, insert it before 5
        [2, 5 | 4, 6, 1, 3]
        
Step 3: Take 4, insert it between 2 and 5
        [2, 4, 5 | 6, 1, 3]
        
Step 4: Take 6, it's already in correct position
        [2, 4, 5, 6 | 1, 3]
        
Step 5: Take 1, insert it at the beginning
        [1, 2, 4, 5, 6 | 3]
        
Step 6: Take 3, insert it between 2 and 4
        [1, 2, 3, 4, 5, 6]
```

#### **The Pseudocode (from textbook)**
```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i – 1]
4      j = i – 1
5      while j > 0 and A[j] > key
6          A[j + 1] = A[j]
7          j = j – 1
8      A[j + 1] = key
```

#### **What is a Loop Invariant?**
A **loop invariant** is a property that:
1. Is true before the loop starts (**Initialization**)
2. Remains true before each iteration (**Maintenance**)
3. Helps prove correctness when the loop ends (**Termination**)

**Why do we care?** Loop invariants are mathematical proofs that our algorithm works correctly.

---

## 📝 PROBLEM 2.1-2

### **Problem Statement**
Consider the procedure SUM-ARRAY. It computes the sum of the n numbers in array A[1 : n]. State a loop invariant for this procedure, and use its initialization, maintenance, and termination properties to show that the SUM-ARRAY procedure returns the sum of the numbers in A[1 : n].

```
SUM-ARRAY(A, n)
1  sum = 0
2  for i = 1 to n
3      sum = sum + A[i]
4  return sum
```

---

### **SOLUTION 2.1-2**

#### **Step 1: Understand What the Algorithm Does**

**What is this algorithm?**
- It adds up all numbers in an array
- Example: If A = [3, 7, 2, 5], then SUM-ARRAY returns 3 + 7 + 2 + 5 = 17

**How does it work?**
- Start with sum = 0
- Go through each element one by one (i = 1, 2, 3, ..., n)
- Add each element to the running total
- Return the final sum

---

#### **Step 2: State the Loop Invariant**

**Loop Invariant for SUM-ARRAY:**

> **At the start of each iteration of the for loop (line 2), the variable `sum` equals the sum of the elements A[1 : i - 1].**

**What does this mean in plain English?**
- Before we process element A[i], the variable `sum` already contains the sum of all elements we've seen so far (from A[1] to A[i-1])

**Example walkthrough:**
```
Array A = [3, 7, 2, 5], n = 4

Before iteration 1 (i = 1):
    sum = 0 = sum of A[1:0] (empty, so sum is 0) ✓

Before iteration 2 (i = 2):
    sum = 3 = sum of A[1:1] = A[1] = 3 ✓

Before iteration 3 (i = 3):
    sum = 10 = sum of A[1:2] = A[1] + A[2] = 3 + 7 = 10 ✓

Before iteration 4 (i = 4):
    sum = 12 = sum of A[1:3] = A[1] + A[2] + A[3] = 3 + 7 + 2 = 12 ✓
```

---

#### **Step 3: Prove Initialization**

**Initialization: The loop invariant is true before the first iteration.**

**What we need to show:**
- Before the loop starts (when i = 1), sum equals the sum of A[1 : 0]

**Proof:**
1. Before the loop starts, line 1 sets `sum = 0`
2. The loop starts with `i = 1`
3. At this point, we need to check: does `sum` equal the sum of A[1 : i - 1] = A[1 : 0]?
4. A[1 : 0] is an **empty subarray** (no elements)
5. The sum of an empty array is **0** (by definition)
6. Since `sum = 0` and the sum of A[1 : 0] = 0, the invariant holds! ✓

**Why this matters:** We've proven the starting condition is correct.

---

#### **Step 4: Prove Maintenance**

**Maintenance: If the invariant is true before an iteration, it remains true before the next iteration.**

**What we need to show:**
- Assume the invariant is true at the start of iteration i (sum = sum of A[1 : i - 1])
- After executing the loop body, show it's true for iteration i + 1

**Proof:**
1. **Assumption**: At the start of iteration i, `sum` equals the sum of A[1 : i - 1]
2. **What happens in the loop body** (line 3):
   - We execute: `sum = sum + A[i]`
   - This adds A[i] to the current sum
3. **After line 3**:
   - `sum` now equals (sum of A[1 : i - 1]) + A[i]
   - Which equals the sum of A[1 : i]
4. **Loop increments i**:
   - i becomes i + 1
5. **Before the next iteration** (i + 1):
   - `sum` equals the sum of A[1 : i]
   - Which is the same as A[1 : (i + 1) - 1]
   - The invariant holds for the next iteration! ✓

**Example:**
```
Iteration i = 2, A = [3, 7, 2, 5]

Before iteration 2:
    sum = 3 (sum of A[1:1])
    
During iteration 2:
    sum = sum + A[2] = 3 + 7 = 10
    
After iteration 2 (before iteration 3):
    sum = 10 (sum of A[1:2]) ✓
```

**Why this matters:** We've proven that each step maintains correctness.

---

#### **Step 5: Prove Termination**

**Termination: When the loop terminates, the invariant gives us the desired result.**

**What we need to show:**
- When the loop ends, the algorithm returns the correct answer

**Proof:**
1. **When does the loop terminate?**
   - The loop runs while i ≤ n
   - It terminates when i = n + 1
   
2. **What is the invariant at termination?**
   - At the start of iteration i = n + 1, the invariant says:
   - `sum` equals the sum of A[1 : (n + 1) - 1] = A[1 : n]
   
3. **But wait!** When i = n + 1, the loop condition (i ≤ n) is false, so we don't enter the loop
   - This means we're at the point RIGHT AFTER the last iteration (i = n)
   - After iteration i = n completes, `sum` contains the sum of A[1 : n]
   
4. **Line 4 returns sum**:
   - We return the sum of A[1 : n]
   - This is exactly what we wanted! ✓

**Why this matters:** We've proven the algorithm returns the correct final answer.

---

#### **Step 6: Complete Proof Summary**

**We have proven:**
1. ✓ **Initialization**: The invariant is true before the loop starts
2. ✓ **Maintenance**: Each iteration preserves the invariant
3. ✓ **Termination**: When the loop ends, we have the correct result

**Therefore:** SUM-ARRAY correctly computes the sum of all elements in A[1 : n].

---

### **Key Takeaways for Problem 2.1-2**

**For your exam, remember:**
1. **Loop invariant structure**: "At the start of iteration i, [property] holds"
2. **Initialization**: Check the invariant before the first iteration (often with empty arrays or i = 1)
3. **Maintenance**: Show that one iteration preserves the invariant for the next
4. **Termination**: Use the loop exit condition + invariant to prove correctness

**Common mistakes to avoid:**
- ❌ Stating the invariant incorrectly (be precise about "before" vs "after" iteration)
- ❌ Forgetting to handle the empty array case in initialization
- ❌ Not connecting the termination condition to the final result

---

## 📝 PROBLEM 2.1-3

### **Problem Statement**
Rewrite the INSERTION-SORT procedure to sort into monotonically decreasing instead of monotonically increasing order.

---

### **SOLUTION 2.1-3**

#### **Step 1: Understand the Original Algorithm**

**Original INSERTION-SORT (increasing order):**
```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i – 1]
4      j = i – 1
5      while j > 0 and A[j] > key
6          A[j + 1] = A[j]
7          j = j – 1
8      A[j + 1] = key
```

**What does "monotonically increasing" mean?**
- Each element is ≤ the next element
- Example: [1, 2, 4, 5, 6] or [1, 1, 3, 5, 5]

**What does "monotonically decreasing" mean?**
- Each element is ≥ the next element
- Example: [6, 5, 4, 2, 1] or [5, 5, 3, 1, 1]

---

#### **Step 2: Identify What Needs to Change**

**Key insight:** The only difference is the comparison direction!

**In increasing order:**
- Line 5: `while j > 0 and A[j] > key`
- We move elements RIGHT if they are GREATER than the key
- This puts smaller elements on the left

**For decreasing order:**
- We need to move elements RIGHT if they are SMALLER than the key
- This will put larger elements on the left

**What changes:** Only the comparison operator in line 5!

---

#### **Step 3: Write the Modified Algorithm**

**INSERTION-SORT-DECREASING(A, n):**
```
INSERTION-SORT-DECREASING(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i – 1]
4      j = i – 1
5      while j > 0 and A[j] < key          // CHANGED: > to <
6          A[j + 1] = A[j]
7          j = j – 1
8      A[j + 1] = key
```

**The ONLY change:** Line 5 now says `A[j] < key` instead of `A[j] > key`

---

#### **Step 4: Trace Through an Example**

**Example: Sort [5, 2, 4, 6, 1, 3] in decreasing order**

**Initial array:** [5, 2, 4, 6, 1, 3]

**Iteration 1 (i = 2, key = 2):**
```
Current state: [5 | 2, 4, 6, 1, 3]
key = 2
j = 1

Check: A[1] = 5 < 2? NO (5 is not less than 2)
No movement needed
Result: [5, 2 | 4, 6, 1, 3]
```

**Iteration 2 (i = 3, key = 4):**
```
Current state: [5, 2 | 4, 6, 1, 3]
key = 4
j = 2

Check: A[2] = 2 < 4? YES → move 2 right
Array: [5, _, 2, 6, 1, 3]
j = 1

Check: A[1] = 5 < 4? NO
Insert key at position 2
Result: [5, 4, 2 | 6, 1, 3]
```

**Iteration 3 (i = 4, key = 6):**
```
Current state: [5, 4, 2 | 6, 1, 3]
key = 6
j = 3

Check: A[3] = 2 < 6? YES → move 2 right
Array: [5, 4, _, 2, 1, 3]
j = 2

Check: A[2] = 4 < 6? YES → move 4 right
Array: [5, _, 4, 2, 1, 3]
j = 1

Check: A[1] = 5 < 6? YES → move 5 right
Array: [_, 5, 4, 2, 1, 3]
j = 0

j = 0, exit loop
Insert key at position 1
Result: [6, 5, 4, 2 | 1, 3]
```

**Iteration 4 (i = 5, key = 1):**
```
Current state: [6, 5, 4, 2 | 1, 3]
key = 1
j = 4

Check: A[4] = 2 < 1? NO
No movement needed
Result: [6, 5, 4, 2, 1 | 3]
```

**Iteration 5 (i = 6, key = 3):**
```
Current state: [6, 5, 4, 2, 1 | 3]
key = 3
j = 5

Check: A[5] = 1 < 3? YES → move 1 right
Array: [6, 5, 4, 2, _, 1]
j = 4

Check: A[4] = 2 < 3? YES → move 2 right
Array: [6, 5, 4, _, 2, 1]
j = 3

Check: A[3] = 4 < 3? NO
Insert key at position 4
Result: [6, 5, 4, 3, 2, 1]
```

**Final sorted array (decreasing order):** [6, 5, 4, 3, 2, 1] ✓

---

#### **Step 5: Verify the Loop Invariant**

**Loop Invariant for Decreasing Sort:**
> At the start of each iteration of the for loop, the subarray A[1 : i - 1] consists of the elements originally in A[1 : i - 1], but in **sorted decreasing order**.

**Why does this work?**
1. **Initialization**: Before i = 2, A[1 : 1] has one element (already sorted)
2. **Maintenance**: Each iteration inserts A[i] into the correct position to maintain decreasing order
3. **Termination**: When i = n + 1, A[1 : n] is sorted in decreasing order

---

### **Key Takeaways for Problem 2.1-3**

**For your exam, remember:**
1. **Increasing to decreasing**: Change `>` to `<` in the comparison
2. **Decreasing to increasing**: Change `<` to `>` in the comparison
3. **Why it works**: The comparison determines which elements move right
4. **Only one line changes**: Line 5 in the while loop condition

**Common mistakes to avoid:**
- ❌ Changing multiple lines (only the comparison changes!)
- ❌ Changing the loop direction (for i = n downto 2) - this is unnecessary
- ❌ Changing the array indexing

---

## 📝 PROBLEM 2.1-4

### **Problem Statement**
Consider the **searching problem**:

**Input:** A sequence of n numbers ⟨a₁, a₂, ..., aₙ⟩ stored in array A[1 : n] and a value x.

**Output:** An index i such that x equals A[i] or the special value NIL if x does not appear in A.

Write pseudocode for **linear search**, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

---

### **SOLUTION 2.1-4**

#### **Step 1: Understand the Problem**

**What is linear search?**
- Search through an array one element at a time
- Start at the beginning, check each element
- If we find the target value x, return its index
- If we reach the end without finding x, return NIL

**Example:**
```
Array A = [3, 7, 2, 5, 9]
Search for x = 5

Check A[1] = 3: 3 ≠ 5, continue
Check A[2] = 7: 7 ≠ 5, continue
Check A[3] = 2: 2 ≠ 5, continue
Check A[4] = 5: 5 = 5, FOUND! Return 4
```

**Example (not found):**
```
Array A = [3, 7, 2, 5, 9]
Search for x = 10

Check A[1] = 3: 3 ≠ 10, continue
Check A[2] = 7: 7 ≠ 10, continue
Check A[3] = 2: 2 ≠ 10, continue
Check A[4] = 5: 5 ≠ 10, continue
Check A[5] = 9: 9 ≠ 10, continue
Reached end, return NIL
```

---

#### **Step 2: Write the Pseudocode**

**LINEAR-SEARCH(A, n, x):**
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

**How it works:**
- **Line 1**: Loop through each index from 1 to n
- **Line 2**: Check if current element equals x
- **Line 3**: If found, immediately return the index
- **Line 4**: If loop completes without finding x, return NIL

---

#### **Step 3: State the Loop Invariant**

**Loop Invariant for LINEAR-SEARCH:**

> **At the start of each iteration of the for loop (line 1), the value x does not appear in the subarray A[1 : i - 1].**

**What does this mean in plain English?**
- Before we check element A[i], we've already verified that x is NOT in any of the elements we've checked so far (A[1] through A[i-1])

**Example walkthrough:**
```
Array A = [3, 7, 2, 5, 9], x = 5

Before iteration 1 (i = 1):
    A[1:0] is empty, x is not in empty array ✓

Before iteration 2 (i = 2):
    A[1:1] = [3], and 5 ≠ 3, so x is not in A[1:1] ✓

Before iteration 3 (i = 3):
    A[1:2] = [3, 7], and 5 ≠ 3 and 5 ≠ 7, so x is not in A[1:2] ✓

Before iteration 4 (i = 4):
    A[1:3] = [3, 7, 2], and 5 is not in this subarray ✓

At iteration 4:
    A[4] = 5 = x, FOUND! Return 4
```

---

#### **Step 4: Prove Initialization**

**Initialization: The loop invariant is true before the first iteration.**

**What we need to show:**
- Before the loop starts (when i = 1), x does not appear in A[1 : 0]

**Proof:**
1. Before the loop starts, i = 1
2. The invariant states: x does not appear in A[1 : i - 1] = A[1 : 0]
3. A[1 : 0] is an **empty subarray** (contains no elements)
4. By definition, x cannot appear in an empty array
5. Therefore, the invariant is trivially true! ✓

**Why this matters:** The starting condition is logically sound.

---

#### **Step 5: Prove Maintenance**

**Maintenance: If the invariant is true before an iteration, it remains true before the next iteration.**

**What we need to show:**
- Assume x is not in A[1 : i - 1] at the start of iteration i
- Show that x is not in A[1 : i] before iteration i + 1

**Proof:**
1. **Assumption**: At the start of iteration i, x does not appear in A[1 : i - 1]

2. **What happens in the loop body**:
   - Line 2 checks if A[i] == x
   
3. **Case 1: A[i] == x (we found it!)**
   - Line 3 executes: `return i`
   - The function terminates immediately
   - We don't need to maintain the invariant because the loop ends
   
4. **Case 2: A[i] ≠ x (not found yet)**
   - We don't return, so we continue to the next iteration
   - Since A[i] ≠ x, and x was not in A[1 : i - 1], we know:
   - x is not in A[1 : i] (which is A[1 : i - 1] plus A[i])
   
5. **Loop increments i**:
   - i becomes i + 1
   
6. **Before the next iteration** (i + 1):
   - x does not appear in A[1 : i]
   - Which is the same as A[1 : (i + 1) - 1]
   - The invariant holds for the next iteration! ✓

**Example:**
```
Iteration i = 2, A = [3, 7, 2, 5], x = 5

Before iteration 2:
    x not in A[1:1] = [3] ✓
    
During iteration 2:
    Check A[2] = 7 ≠ 5, continue
    
After iteration 2 (before iteration 3):
    x not in A[1:2] = [3, 7] ✓
```

**Why this matters:** Each iteration correctly extends our search.

---

#### **Step 6: Prove Termination**

**Termination: When the loop terminates, the invariant gives us the desired result.**

**There are TWO ways the algorithm can terminate:**

**Termination Case 1: Early return (line 3)**
- **When**: We find A[i] == x during some iteration
- **What happens**: We immediately return i
- **Why it's correct**: We found x at index i, which is exactly what we want! ✓

**Termination Case 2: Loop completes (line 4)**
- **When**: The loop runs through all iterations (i = 1, 2, ..., n) without returning
- **What the invariant tells us**:
  - After the last iteration (i = n), the invariant says:
  - x does not appear in A[1 : n]
  - This means x is not in the entire array!
- **What happens**: Line 4 executes: `return NIL`
- **Why it's correct**: x is not in the array, so returning NIL is correct! ✓

**Why this matters:** Both termination paths produce correct results.

---

#### **Step 7: Complete Proof Summary**

**We have proven:**
1. ✓ **Initialization**: The invariant is true before the loop starts (empty array case)
2. ✓ **Maintenance**: Each iteration preserves the invariant (we verify x is not in checked elements)
3. ✓ **Termination**: Both termination cases produce correct results:
   - Found: return the index where x appears
   - Not found: return NIL after checking all elements

**Therefore:** LINEAR-SEARCH correctly finds x in A or returns NIL if x is not present.

---

#### **Step 8: Alternative Implementation (More Explicit)**

Some textbooks prefer a more explicit version that uses a flag:

**LINEAR-SEARCH-VERBOSE(A, n, x):**
```
LINEAR-SEARCH-VERBOSE(A, n, x)
1  i = 1
2  while i ≤ n and A[i] ≠ x
3      i = i + 1
4  if i ≤ n
5      return i
6  else
7      return NIL
```

**Loop Invariant for this version:**
> At the start of each iteration of the while loop, x does not appear in A[1 : i - 1].

**Both versions are correct!** The first is more concise, the second is more explicit.

---

### **Key Takeaways for Problem 2.1-4**

**For your exam, remember:**
1. **Linear search structure**: Loop through array, check each element, return when found
2. **Loop invariant**: "x is not in the elements we've checked so far"
3. **Two termination cases**: Found (return index) or not found (return NIL)
4. **Early return**: It's okay for the loop to terminate early (line 3)

**Common mistakes to avoid:**
- ❌ Forgetting to handle the "not found" case (must return NIL)
- ❌ Incorrect loop invariant (must be about elements NOT checked yet)
- ❌ Not proving both termination cases
- ❌ Off-by-one errors in array indexing

**Exam strategy:**
- Always state your loop invariant clearly
- Prove all three properties (initialization, maintenance, termination)
- Handle both success and failure cases
- Use concrete examples to verify your logic

---

## 📚 SECTION 2.2: Analyzing Algorithms

### **Background Concepts You Need to Know**

Before solving Section 2.2 problems, let's establish the foundational concepts:

#### **What is Algorithm Analysis?**
Algorithm analysis is about understanding:
1. **How much time** an algorithm takes (time complexity)
2. **How much memory** an algorithm uses (space complexity)
3. **How performance scales** as input size grows

#### **Why Do We Analyze Algorithms?**
- To compare different algorithms
- To predict performance on large inputs
- To identify bottlenecks
- To make informed design decisions

#### **Key Concepts in Algorithm Analysis**

**1. Input Size (n)**
- The number of items to process
- For sorting: n = number of elements in array
- For searching: n = length of array

**2. Running Time**
- Number of primitive operations executed
- We count: comparisons, assignments, arithmetic operations
- We ignore: constant factors (for now)

**3. Best Case, Worst Case, Average Case**
- **Best case**: Minimum time (most favorable input)
- **Worst case**: Maximum time (least favorable input)
- **Average case**: Expected time (typical input)

**4. Asymptotic Notation**
- **Big-O (O)**: Upper bound (worst case)
- **Big-Omega (Ω)**: Lower bound (best case)
- **Big-Theta (Θ)**: Tight bound (both upper and lower)

---

### **Analyzing INSERTION-SORT**

Let's analyze the insertion sort algorithm step by step:

```
INSERTION-SORT(A, n)
1  for i = 2 to n                    // Runs n-1 times
2      key = A[i]                    // Runs n-1 times
3      // Insert A[i] into sorted subarray A[1 : i – 1]
4      j = i – 1                     // Runs n-1 times
5      while j > 0 and A[j] > key    // Varies: 0 to i-1 times
6          A[j + 1] = A[j]           // Varies: 0 to i-1 times
7          j = j – 1                 // Varies: 0 to i-1 times
8      A[j + 1] = key                // Runs n-1 times
```

**Counting Operations:**

Let tᵢ = number of times the while loop (line 5) executes for iteration i

**Total operations:**
- Lines 1-4, 8: Execute (n-1) times each
- Lines 5-7: Execute Σ(i=2 to n) tᵢ times

**Best Case (already sorted array):**
- The while loop never executes (tᵢ = 0 for all i)
- Total operations: c₁(n-1) + c₂(n-1) + ... = Θ(n)
- **Linear time**: O(n)

**Worst Case (reverse sorted array):**
- The while loop executes i-1 times for each i
- Total operations: Σ(i=2 to n) (i-1) = 1 + 2 + 3 + ... + (n-1) = n(n-1)/2
- **Quadratic time**: O(n²)

**Average Case:**
- On average, the while loop executes (i-1)/2 times
- Total operations: Θ(n²)

---

## 📝 PROBLEM 2.2-2

### **Problem Statement**
Consider sorting n numbers stored in array A[1 : n] by first finding the smallest element of A[1 : n] and exchanging it with the element in A[1]. Then find the smallest element of A[2 : n], and exchange it with A[2]. Then find the smallest element of A[3 : n], and exchange it with A[3]. Continue in this manner for the first n - 1 elements of A. Write pseudocode for this algorithm, which is known as **selection sort**. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the worst-case running time of selection sort in Θ-notation. Is the best-case running time better than the worst-case running time?

---

### **SOLUTION 2.2-2**

#### **Step 1: Understand Selection Sort**

**What is selection sort?**
- Find the minimum element in the unsorted portion
- Swap it with the first element of the unsorted portion
- Move the boundary between sorted and unsorted portions

**Visual example:**
```
Initial: [5, 2, 4, 6, 1, 3]

Pass 1: Find min in [5, 2, 4, 6, 1, 3] → 1
        Swap 1 with 5
        [1 | 2, 4, 6, 5, 3]

Pass 2: Find min in [2, 4, 6, 5, 3] → 2
        Already in place
        [1, 2 | 4, 6, 5, 3]

Pass 3: Find min in [4, 6, 5, 3] → 3
        Swap 3 with 4
        [1, 2, 3 | 6, 5, 4]

Pass 4: Find min in [6, 5, 4] → 4
        Swap 4 with 6
        [1, 2, 3, 4 | 5, 6]

Pass 5: Find min in [5, 6] → 5
        Already in place
        [1, 2, 3, 4, 5 | 6]

Final: [1, 2, 3, 4, 5, 6]
```

---

#### **Step 2: Write the Pseudocode**

**SELECTION-SORT(A, n):**
```
SELECTION-SORT(A, n)
1  for i = 1 to n - 1
2      // Find the minimum element in A[i : n]
3      min_index = i
4      for j = i + 1 to n
5          if A[j] < A[min_index]
6              min_index = j
7      // Swap A[i] with A[min_index]
8      temp = A[i]
9      A[i] = A[min_index]
10     A[min_index] = temp
```

**Explanation of each part:**

**Lines 1**: Outer loop runs n-1 times
- **Why n-1?** After placing n-1 elements, the last element is automatically in place

**Lines 3-6**: Find minimum in unsorted portion
- **Line 3**: Assume current position has minimum
- **Lines 4-6**: Check all remaining elements
- **Line 5-6**: Update min_index if we find a smaller element

**Lines 8-10**: Swap minimum with current position
- **Standard swap using temporary variable**
- Puts the minimum element in its final sorted position

---

#### **Step 3: State and Prove the Loop Invariant**

**Loop Invariant for SELECTION-SORT:**

> **At the start of each iteration of the for loop (line 1), the subarray A[1 : i - 1] contains the (i - 1) smallest elements of A[1 : n] in sorted order.**

**What does this mean?**
- Elements A[1] through A[i-1] are:
  1. The smallest elements from the original array
  2. In sorted order
  3. In their final positions (won't move again)

---

**Proof of Initialization:**

**Before the first iteration (i = 1):**
- The subarray A[1 : 0] is empty
- An empty array trivially contains 0 smallest elements in sorted order ✓

---

**Proof of Maintenance:**

**Assume the invariant holds at the start of iteration i:**
- A[1 : i-1] contains the (i-1) smallest elements in sorted order

**What happens during iteration i:**
1. Lines 3-6 find the minimum element in A[i : n]
2. This minimum is the ith smallest element overall (why?)
   - A[1 : i-1] already has the (i-1) smallest elements
   - The minimum of the remaining elements is the next smallest
3. Lines 8-10 swap this minimum into position i
4. Now A[1 : i] contains the i smallest elements in sorted order

**After iteration i (before iteration i+1):**
- A[1 : i] contains the i smallest elements in sorted order
- The invariant holds for the next iteration! ✓

---

**Proof of Termination:**

**When does the loop terminate?**
- After iteration i = n - 1

**What does the invariant tell us?**
- A[1 : n-1] contains the (n-1) smallest elements in sorted order

**What about A[n]?**
- If the (n-1) smallest elements are in A[1 : n-1]
- Then A[n] must contain the largest element
- The entire array A[1 : n] is sorted! ✓

---

#### **Step 4: Why Only n-1 Iterations?**

**Question:** Why does selection sort need to run for only the first n - 1 elements, rather than for all n elements?

**Answer:**

**Logical reasoning:**
1. After n-1 iterations, we've placed the (n-1) smallest elements in positions 1 through n-1
2. There's only one element left: A[n]
3. This last element must be the largest element (by process of elimination)
4. It's already in the correct position!
5. No need to "find the minimum" of a single element

**Example:**
```
Array: [5, 2, 4, 6, 1, 3]

After 5 passes (n-1 = 5):
[1, 2, 3, 4, 5 | 6]

The last element (6) is automatically in the correct position!
```

**Mathematical proof:**
- If A[1 : n-1] contains the (n-1) smallest elements
- Then A[n] contains the largest element
- Since A[1 : n-1] is sorted and A[n] ≥ all elements in A[1 : n-1]
- The entire array is sorted

---

#### **Step 5: Analyze Worst-Case Running Time**

**Counting operations:**

**Outer loop (line 1):** Runs n-1 times

**Inner loop (lines 4-6):** 
- Iteration i = 1: Runs n-1 times
- Iteration i = 2: Runs n-2 times
- Iteration i = 3: Runs n-3 times
- ...
- Iteration i = n-1: Runs 1 time

**Total inner loop iterations:**
```
(n-1) + (n-2) + (n-3) + ... + 2 + 1
= Σ(k=1 to n-1) k
= (n-1)(n) / 2
= (n² - n) / 2
```

**Swap operations (lines 8-10):** Runs n-1 times (constant time each)

**Total operations:**
```
T(n) = c₁(n-1) + c₂[(n-1)(n)/2] + c₃(n-1)
     = c₂(n²/2) - c₂(n/2) + (c₁ + c₃)(n-1)
     = O(n²)
```

**Worst-case running time: Θ(n²)**

**Why Θ (theta) notation?**
- The dominant term is n²/2
- We drop constants and lower-order terms
- The algorithm is bounded both above and below by n²

---

#### **Step 6: Best-Case vs Worst-Case Analysis**

**Question:** Is the best-case running time better than the worst-case running time?

**Answer: NO, the best-case is the same as the worst-case!**

**Why?**

**Key observation:** Selection sort ALWAYS performs the same number of comparisons, regardless of the input!

**Best case (already sorted):**
```
Array: [1, 2, 3, 4, 5, 6]

Pass 1: Compare 6 elements to find min → 5 comparisons
Pass 2: Compare 5 elements to find min → 4 comparisons
Pass 3: Compare 4 elements to find min → 3 comparisons
Pass 4: Compare 3 elements to find min → 2 comparisons
Pass 5: Compare 2 elements to find min → 1 comparison

Total: 5 + 4 + 3 + 2 + 1 = 15 comparisons
```

**Worst case (reverse sorted):**
```
Array: [6, 5, 4, 3, 2, 1]

Pass 1: Compare 6 elements to find min → 5 comparisons
Pass 2: Compare 5 elements to find min → 4 comparisons
Pass 3: Compare 4 elements to find min → 3 comparisons
Pass 4: Compare 3 elements to find min → 2 comparisons
Pass 5: Compare 2 elements to find min → 1 comparison

Total: 5 + 4 + 3 + 2 + 1 = 15 comparisons
```

**Same number of comparisons!**

**Why is this different from insertion sort?**
- **Insertion sort**: Best case O(n), worst case O(n²)
  - Best case: Already sorted, inner loop never executes
  - Worst case: Reverse sorted, inner loop always executes fully
  
- **Selection sort**: Best case O(n²), worst case O(n²)
  - Always scans the entire unsorted portion to find minimum
  - Number of comparisons is independent of input order

**Running time for selection sort:**
- **Best case**: Θ(n²)
- **Worst case**: Θ(n²)
- **Average case**: Θ(n²)

**Note on swaps:**
- Selection sort performs at most n-1 swaps (one per iteration)
- Insertion sort can perform up to O(n²) swaps in worst case
- This makes selection sort useful when swaps are expensive

---

### **Key Takeaways for Problem 2.2-2**

**For your exam, remember:**

1. **Selection sort algorithm:**
   - Find minimum in unsorted portion
   - Swap with first unsorted element
   - Repeat n-1 times

2. **Loop invariant:**
   - A[1 : i-1] contains the (i-1) smallest elements in sorted order

3. **Why n-1 iterations:**
   - After placing n-1 elements, the last is automatically correct

4. **Running time:**
   - Always Θ(n²), regardless of input
   - Best case = Worst case = Average case

5. **Comparison with insertion sort:**
   - Selection sort: Always Θ(n²)
   - Insertion sort: Best O(n), worst O(n²)
   - Selection sort: Fewer swaps
   - Insertion sort: Fewer comparisons on nearly-sorted data

**Common mistakes to avoid:**
- ❌ Thinking selection sort has a better best case (it doesn't!)
- ❌ Running the loop n times instead of n-1
- ❌ Incorrect loop invariant (must specify "smallest elements")
- ❌ Not explaining why the last element is automatically sorted

---

## 📝 PROBLEM 2.2-3

### **Problem Statement**
Consider linear search again (see Exercise 2.1-4). How many elements of the input array need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? Using Θ-notation, give the average-case and worst-case running times of linear search. Justify your answers.

---

### **SOLUTION 2.2-3**

#### **Step 1: Recall Linear Search**

**LINEAR-SEARCH(A, n, x):**
```
LINEAR-SEARCH(A, n, x)
1  for i = 1 to n
2      if A[i] == x
3          return i
4  return NIL
```

**What does this algorithm do?**
- Checks each element sequentially from left to right
- Returns immediately when x is found
- Returns NIL if x is not in the array

---

#### **Step 2: Worst-Case Analysis**

**Question:** How many elements need to be checked in the worst case?

**Answer: n elements (all of them)**

**When does the worst case occur?**

**Case 1: Element is not in the array**
```
Array: [3, 7, 2, 5, 9]
Search for x = 10

Check A[1] = 3 ≠ 10
Check A[2] = 7 ≠ 10
Check A[3] = 2 ≠ 10
Check A[4] = 5 ≠ 10
Check A[5] = 9 ≠ 10
Return NIL

Comparisons: 5 = n
```

**Case 2: Element is at the last position**
```
Array: [3, 7, 2, 5, 9]
Search for x = 9

Check A[1] = 3 ≠ 9
Check A[2] = 7 ≠ 9
Check A[3] = 2 ≠ 9
Check A[4] = 5 ≠ 9
Check A[5] = 9 = 9, FOUND!
Return 5

Comparisons: 5 = n
```

**Worst-case running time:**
- **Number of comparisons**: n
- **Running time**: Θ(n)

**Why Θ(n)?**
- We perform exactly n comparisons
- Each comparison takes constant time
- Total time is proportional to n

---

#### **Step 3: Average-Case Analysis**

**Question:** How many elements need to be checked on average?

**Assumptions:**
1. The element x is in the array
2. x is equally likely to be at any position (uniform distribution)
3. Probability x is at position i: P(x at position i) = 1/n

---

**Calculating the average:**

**If x is at position 1:** 1 comparison
**If x is at position 2:** 2 comparisons
**If x is at position 3:** 3 comparisons
...
**If x is at position n:** n comparisons

**Expected number of comparisons:**
```
E[comparisons] = Σ(i=1 to n) [i × P(x at position i)]
               = Σ(i=1 to n) [i × (1/n)]
               = (1/n) × Σ(i=1 to n) i
               = (1/n) × [n(n+1)/2]
               = (n+1)/2
```

**Average-case: (n+1)/2 comparisons**

**Intuitive explanation:**
- On average, we find the element halfway through the array
- Half of n is n/2, but we need to account for the +1
- More precisely: (n+1)/2

**Examples:**
```
n = 10: Average = (10+1)/2 = 5.5 comparisons
n = 100: Average = (100+1)/2 = 50.5 comparisons
n = 1000: Average = (1000+1)/2 = 500.5 comparisons
```

---

#### **Step 4: Average-Case Running Time in Θ-Notation**

**Average number of comparisons:** (n+1)/2

**Simplifying for Θ-notation:**
```
(n+1)/2 = n/2 + 1/2
        = (1/2)n + (1/2)
```

**In Θ-notation:**
- Drop constant factors: (1/2)n → n
- Drop lower-order terms: +1/2 → ignore
- **Average-case running time: Θ(n)**

**Why is it still Θ(n)?**
- The dominant term is n
- Constants don't matter in asymptotic analysis
- (n+1)/2 grows linearly with n

---

#### **Step 5: What if x is NOT in the array?**

**Extended average-case analysis:**

If we consider the possibility that x might not be in the array:

**Assumptions:**
- Probability x is in array: p
- Probability x is not in array: (1 - p)
- If x is in array, it's equally likely at any position

**Expected comparisons:**
```
E[comparisons] = p × [(n+1)/2] + (1-p) × n
               = p(n+1)/2 + n - pn
               = pn/2 + p/2 + n - pn
               = n - pn/2 + p/2
               = n(1 - p/2) + p/2
```

**Special cases:**
- **p = 1** (x always in array): E = (n+1)/2
- **p = 0** (x never in array): E = n
- **p = 0.5** (50% chance): E = 3n/4 + 1/4

**In all cases, the running time is still Θ(n)**

---

#### **Step 6: Summary Table**

| Case | Comparisons | Running Time | When it Occurs |
|------|-------------|--------------|----------------|
| **Best Case** | 1 | Θ(1) | Element at position 1 |
| **Average Case** | (n+1)/2 | Θ(n) | Element equally likely anywhere |
| **Worst Case** | n | Θ(n) | Element at end or not present |

---

#### **Step 7: Detailed Justification**

**Why is the average case (n+1)/2?**

**Proof by example (n = 5):**
```
Array: [a, b, c, d, e]

Scenario 1: x = a (position 1)
    Comparisons: 1
    Probability: 1/5

Scenario 2: x = b (position 2)
    Comparisons: 2
    Probability: 1/5

Scenario 3: x = c (position 3)
    Comparisons: 3
    Probability: 1/5

Scenario 4: x = d (position 4)
    Comparisons: 4
    Probability: 1/5

Scenario 5: x = e (position 5)
    Comparisons: 5
    Probability: 1/5

Expected value:
E = (1)(1/5) + (2)(1/5) + (3)(1/5) + (4)(1/5) + (5)(1/5)
  = (1 + 2 + 3 + 4 + 5) / 5
  = 15 / 5
  = 3

Using formula: (n+1)/2 = (5+1)/2 = 3 ✓
```

**Why is the worst case n?**

**Two scenarios:**
1. **Element not in array**: Must check all n elements to confirm absence
2. **Element at last position**: Must check all n elements before finding it

**Both scenarios require n comparisons, so worst case is n.**

---

#### **Step 8: Asymptotic Analysis**

**Why do we use Θ-notation?**

**Θ-notation provides a tight bound:**
- **Upper bound (O)**: Linear search is at most O(n)
- **Lower bound (Ω)**: Linear search is at least Ω(n) in worst case
- **Tight bound (Θ)**: Linear search is exactly Θ(n)

**Average case: Θ(n)**
- (n+1)/2 is proportional to n
- As n grows large, (n+1)/2 ≈ n/2
- Constant factors (1/2) are ignored in Θ-notation

**Worst case: Θ(n)**
- Exactly n comparisons
- Linear relationship with input size

**Mathematical justification:**
```
For average case:
    (n+1)/2 ≤ c₁ × n  for all n ≥ n₀  (upper bound)
    (n+1)/2 ≥ c₂ × n  for all n ≥ n₀  (lower bound)

Choose c₁ = 1, c₂ = 1/4, n₀ = 1:
    (n+1)/2 ≤ n  ✓  (always true for n ≥ 1)
    (n+1)/2 ≥ n/4  ✓  (true for n ≥ 1)

Therefore: (n+1)/2 = Θ(n)
```

---

### **Key Takeaways for Problem 2.2-3**

**For your exam, remember:**

1. **Average case calculation:**
   - Sum of all possible positions: 1 + 2 + 3 + ... + n = n(n+1)/2
   - Divide by n: (n+1)/2
   - Simplifies to Θ(n)

2. **Worst case:**
   - Element at end or not present
   - Requires n comparisons
   - Running time: Θ(n)

3. **Why both are Θ(n):**
   - Average: (n+1)/2 ≈ n/2 (constant factor ignored)
   - Worst: n
   - Both grow linearly with n

4. **Key formula:**
   - Sum of first n integers: n(n+1)/2
   - Average position: (n+1)/2

**Common mistakes to avoid:**
- ❌ Saying average case is n/2 (it's (n+1)/2)
- ❌ Forgetting to divide by n when calculating expected value
- ❌ Thinking average case is different asymptotic class than worst case
- ❌ Not justifying why Θ(n) is appropriate

**Exam strategy:**
- Show your work: write out the expected value calculation
- Explain the scenarios (element at each position)
- Justify the Θ-notation with asymptotic reasoning
- Give concrete examples for small n

---

## 📝 PROBLEM 2.2-4

### **Problem Statement**
How can you modify any sorting algorithm to have a good best-case running time?

---

### **SOLUTION 2.2-4**

#### **Step 1: Understand the Question**

**What is "good best-case running time"?**
- For sorting, the best possible best-case is **Θ(n)** (linear time)
- This occurs when the input is already sorted
- We want to detect this and avoid unnecessary work

**Current best-case times:**
- **Insertion sort**: Θ(n) - already good!
- **Selection sort**: Θ(n²) - not good
- **Merge sort**: Θ(n log n) - could be better

**Goal:** Modify any algorithm to achieve Θ(n) best-case

---

#### **Step 2: The Key Insight**

**Strategy: Pre-check if the array is already sorted**

**If sorted:**
- Return immediately (no sorting needed)
- Cost: Θ(n) to check

**If not sorted:**
- Run the original sorting algorithm
- Cost: Original algorithm's time complexity

**Result:**
- Best case: Θ(n) (when already sorted)
- Worst case: Θ(n) + original worst case ≈ original worst case

---

#### **Step 3: Write the Modified Algorithm**

**MODIFIED-SORT(A, n):**
```
MODIFIED-SORT(A, n)
1  // Pre-check: Is the array already sorted?
2  for i = 1 to n - 1
3      if A[i] > A[i + 1]
4          // Array is not sorted, use original algorithm
5          ORIGINAL-SORT(A, n)
6          return
7  // If we reach here, array is already sorted
8  return
```

**Explanation:**

**Lines 2-3**: Check if array is sorted
- Compare each adjacent pair
- If any pair is out of order, array is not sorted

**Lines 4-6**: Array not sorted
- Call the original sorting algorithm
- Return the sorted array

**Lines 7-8**: Array already sorted
- No sorting needed, return immediately

---

#### **Step 4: Analyze the Running Time**

**Best case (array already sorted):**
```
Array: [1, 2, 3, 4, 5, 6]

Check A[1] ≤ A[2]: 1 ≤ 2 ✓
Check A[2] ≤ A[3]: 2 ≤ 3 ✓
Check A[3] ≤ A[4]: 3 ≤ 4 ✓
Check A[4] ≤ A[5]: 4 ≤ 5 ✓
Check A[5] ≤ A[6]: 5 ≤ 6 ✓

All checks pass, return immediately
Comparisons: n - 1 = Θ(n)
```

**Best-case running time: Θ(n)** ✓

---

**Worst case (array not sorted):**
```
Array: [6, 5, 4, 3, 2, 1]

Check A[1] ≤ A[2]: 6 ≤ 5? NO
Array is not sorted, call ORIGINAL-SORT

Time: Θ(n) for check + T_original(n) for sorting
    = Θ(n) + T_original(n)
    = T_original(n)  (dominated by sorting time)
```

**Worst-case running time: Same as original algorithm**

---

#### **Step 5: Apply to Specific Algorithms**

**Example 1: Modified Selection Sort**

**Original selection sort:**
- Best case: Θ(n²)
- Worst case: Θ(n²)

**Modified selection sort:**
```
MODIFIED-SELECTION-SORT(A, n)
1  for i = 1 to n - 1
2      if A[i] > A[i + 1]
3          SELECTION-SORT(A, n)
4          return
5  return
```

**Modified selection sort:**
- Best case: Θ(n) ✓ (improved!)
- Worst case: Θ(n²) (same as before)

---

**Example 2: Modified Merge Sort**

**Original merge sort:**
- Best case: Θ(n log n)
- Worst case: Θ(n log n)

**Modified merge sort:**
```
MODIFIED-MERGE-SORT(A, n)
1  for i = 1 to n - 1
2      if A[i] > A[i + 1]
3          MERGE-SORT(A, n)
4          return
5  return
```

**Modified merge sort:**
- Best case: Θ(n) ✓ (improved!)
- Worst case: Θ(n log n) (same as before)

---

#### **Step 6: Alternative Approaches**

**Approach 2: Check during the algorithm**

Instead of pre-checking, integrate the check into the algorithm itself.

**Example: Modified Insertion Sort**

**Observation:** Insertion sort already has Θ(n) best case!
- When array is sorted, the while loop never executes
- Only the outer loop runs: n-1 iterations
- Each iteration does constant work
- Total: Θ(n)

**No modification needed for insertion sort!**

---

**Approach 3: Adaptive sorting**

Some algorithms naturally adapt to partially sorted input:

**Timsort (used in Python):**
- Detects sorted runs
- Merges them efficiently
- Best case: Θ(n) on sorted input
- Worst case: Θ(n log n)

**Smoothsort:**
- Adaptive heap sort variant
- Best case: Θ(n) on sorted input
- Worst case: Θ(n log n)

---

#### **Step 7: Trade-offs and Considerations**

**Advantages of pre-checking:**
1. ✓ Simple to implement
2. ✓ Works with any sorting algorithm
3. ✓ Guarantees Θ(n) best case
4. ✓ No change to worst-case complexity

**Disadvantages:**
1. ✗ Adds overhead to every call (even when not needed)
2. ✗ Doesn't help with partially sorted arrays
3. ✗ Two passes through the data in worst case

**When is this useful?**
- When you expect many already-sorted inputs
- When the original algorithm has poor best-case (like selection sort)
- When the check cost is negligible compared to sorting

**When is this NOT useful?**
- When inputs are rarely sorted
- When the original algorithm already has good best-case (like insertion sort)
- When the overhead of checking is significant

---

#### **Step 8: Formal Analysis**

**Let T_original(n) be the running time of the original algorithm.**

**Modified algorithm running time:**
```
T_modified(n) = {
    Θ(n)                     if array is sorted (best case)
    Θ(n) + T_original(n)     if array is not sorted (worst case)
}
```

**Simplification:**
- Best case: Θ(n)
- Worst case: Θ(n) + T_original(n) = T_original(n)
  - Because T_original(n) dominates Θ(n) for large n
  - For example: Θ(n) + Θ(n²) = Θ(n²)

**Asymptotic improvement:**
- Best case: Always improved to Θ(n)
- Worst case: Unchanged (asymptotically)

---

### **Key Takeaways for Problem 2.2-4**

**For your exam, remember:**

1. **Simple modification:**
   - Pre-check if array is sorted
   - If yes, return immediately (Θ(n))
   - If no, run original algorithm

2. **Best-case improvement:**
   - Any algorithm can achieve Θ(n) best case
   - Cost: One linear scan through the array

3. **Worst-case preservation:**
   - Worst case remains the same (asymptotically)
   - Small constant overhead added

4. **When to use:**
   - When sorted inputs are common
   - When original best case is poor
   - When check cost is acceptable

**Common mistakes to avoid:**
- ❌ Thinking this improves worst-case time
- ❌ Not considering the overhead cost
- ❌ Applying to algorithms that already have good best case
- ❌ Not explaining why Θ(n) is the best possible for sorting

**Exam strategy:**
- Clearly state the modification (pre-check)
- Analyze both best and worst cases
- Explain the trade-offs
- Give a concrete example

**Additional insight:**
- Θ(n) is the best possible best-case for comparison-based sorting
- Why? Must at least look at every element once to verify it's sorted
- This modification achieves the theoretical optimum for best case

---

## 🎯 SUMMARY AND EXAM PREPARATION

### **Section 2.1 Summary: Insertion Sort**

**Key Concepts:**
1. **Insertion sort algorithm**: Insert each element into its correct position in the sorted portion
2. **Loop invariants**: Properties that help prove correctness
3. **Three properties**: Initialization, Maintenance, Termination
4. **Pseudocode conventions**: Understand array indexing, loops, and notation

**Problems Covered:**
- **2.1-2**: Loop invariant for SUM-ARRAY
- **2.1-3**: Modify insertion sort for decreasing order
- **2.1-4**: Linear search with loop invariant proof

---

### **Section 2.2 Summary: Analyzing Algorithms**

**Key Concepts:**
1. **Running time analysis**: Count operations, identify dominant terms
2. **Best, worst, average cases**: Different scenarios, different times
3. **Asymptotic notation**: Θ, O, Ω for describing growth rates
4. **Algorithm comparison**: Trade-offs between different approaches

**Problems Covered:**
- **2.2-2**: Selection sort algorithm and analysis
- **2.2-3**: Average-case analysis of linear search
- **2.2-4**: Improving best-case running time

---

### **Quick Reference: Algorithm Comparison**

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable? |
|-----------|-----------|--------------|------------|-------|---------|
| **Insertion Sort** | Θ(n) | Θ(n²) | Θ(n²) | Θ(1) | Yes |
| **Selection Sort** | Θ(n²) | Θ(n²) | Θ(n²) | Θ(1) | No |
| **Linear Search** | Θ(1) | Θ(n) | Θ(n) | Θ(1) | N/A |

---

### **Exam Strategies**

**For loop invariant problems:**
1. State the invariant clearly and precisely
2. Prove initialization (often with empty arrays)
3. Prove maintenance (show one iteration preserves it)
4. Prove termination (connect to final result)
5. Use concrete examples to verify

**For algorithm design problems:**
1. Write clear pseudocode with comments
2. Explain the logic in plain English
3. Trace through a concrete example
4. Analyze the running time
5. Consider edge cases

**For analysis problems:**
1. Count operations systematically
2. Identify best, worst, and average cases
3. Use summation formulas (Σ k = n(n+1)/2)
4. Simplify to asymptotic notation
5. Justify your reasoning

---

### **Common Formulas to Memorize**

**Summations:**
```
Σ(k=1 to n) k = n(n+1)/2 = Θ(n²)

Σ(k=1 to n) k² = n(n+1)(2n+1)/6 = Θ(n³)

Σ(k=0 to n) 2^k = 2^(n+1) - 1 = Θ(2^n)
```

**Average position in array:**
```
(n+1)/2
```

**Number of comparisons in nested loops:**
```
Outer loop: n iterations
Inner loop: varies from 1 to n
Total: n(n+1)/2 = Θ(n²)
```

---

### **Final Checklist**

Before your exam, make sure you can:

- [ ] Write insertion sort pseudocode from memory
- [ ] Explain what a loop invariant is and why it's useful
- [ ] Prove correctness using initialization, maintenance, termination
- [ ] Modify insertion sort for decreasing order
- [ ] Write linear search pseudocode
- [ ] Calculate average-case running time
- [ ] Explain the difference between best, worst, and average cases
- [ ] Use Θ-notation correctly
- [ ] Analyze nested loops
- [ ] Compare different sorting algorithms

---

## 📚 ADDITIONAL RESOURCES

**For deeper understanding:**
1. Practice tracing algorithms by hand on small examples
2. Implement the algorithms in your favorite programming language
3. Time them on different input sizes to verify the analysis
4. Try modifying the algorithms in different ways
5. Prove correctness for your modifications

**Common pitfalls to avoid:**
- Off-by-one errors in array indexing
- Incorrect loop bounds
- Forgetting to handle empty arrays
- Mixing up best and worst cases
- Dropping important terms in analysis

---

**Good luck on your exam! Remember:**
- Understand the "why" behind each step
- Use concrete examples to verify your logic
- Show your work clearly
- Explain your reasoning
- Double-check edge cases

**You've got this! 🚀**

---

## 📝 CHANGELOG

**File**: `HW_ANSWERS_2.1_and_2.2.md`
**Created**: 2025-09-30
**Purpose**: Comprehensive homework solutions for CS3112 Sections 2.1 and 2.2

**Problems Solved:**
- Section 2.1: Problems 2, 3, 4
- Section 2.2: Problems 2, 3, 4

**Key Features:**
- Step-by-step explanations from ground zero
- Detailed loop invariant proofs
- Running time analysis with justification
- Concrete examples for every concept
- Exam preparation strategies
- Quick reference tables

**Target Audience:**
- Students learning algorithms for the first time
- Anyone preparing for midterm/final exams
- Professionals reviewing fundamental algorithms

---

*End of Document*
