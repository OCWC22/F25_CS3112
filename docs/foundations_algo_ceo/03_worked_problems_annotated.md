# 03 Worked Problem Set (Annotated)

Each solution highlights:
- Key idea(s)
- Algorithm/pseudocode
- Correctness sketch citing discrete math concepts (e.g., invariants, induction, equivalence)
- Exact/asymptotic complexity with equations
- Business note (where appropriate)
- Citations to repository sections

---

## 1) Two Sum (LeetCode 1)

**Problem:** Given an integer array `nums` and an integer `target`, return indices i≠j such that `nums[i] + nums[j] = target`. Assume exactly one solution; do not reuse the same element twice.

**Key Idea:** Use a hash map to store value→index while scanning once; for each x check if (target−x) was seen.

**Algorithm (One-pass Hash Table):**
```
map = empty hash table
for i from 0 to n-1:
    x = nums[i]
    y = target - x
    if y in map: return (map[y], i)
    map[x] = i
```

**Correctness Sketch:**
- We maintain the invariant: after processing index i−1, map contains each value nums[k] for k ∈ [0..i−1] mapped to its index.
- When we see x=nums[i], if y=target−x exists in map, then there is k<i s.t. nums[k]=y; hence nums[k]+nums[i]=target, satisfying the requirement.
- Since exactly one solution exists, the algorithm returns that pair when the second of the two indices is encountered.
Discrete math concepts: **Function definition and mapping** (Epp 7.1), **Pigeonhole intuition** for collisions (Epp 7.2.8) though proper hashing ensures average O(1) expected lookup.
Citations: (week_2/discrete_math_chapter_7_complete.md#definition-function), (week_2/discrete_math_chapter_7_complete.md#example-728-the-pigeonhole-principle).

**Complexity:**
- Time: Expected Θ(n), with O(1) average hash operations; worst-case Θ(n²) if all items collide (adversarial hashing).
- Space: O(n) for the map.
Equations: One pass over n elements ⇒ ∑_{i=1}^{n} O(1) = O(n).

**Business Note:** Hash-based designs give excellent average performance but pay attention to worst-case risks (e.g., adversarial inputs). Mitigate using robust hashing, load-factor management, or using trees for buckets.

---

## 2) Valid Parentheses (LeetCode 20)

**Problem:** Given a string s containing '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Valid means: open brackets must be closed by the same type, and in the correct order.

**Key Idea:** Use a stack; push opening. On closing, check match with top. Final stack must be empty.

**Algorithm:**
```
stack = empty
for ch in s:
    if ch in {'(', '{', '['}:
        push ch
    else:
        if stack empty: return false
        top = pop stack
        if not matches(top, ch): return false
return stack empty
```

**Correctness Sketch:**
- **Invariant:** After processing prefix s[1..i], the stack contains (from bottom to top) the unmatched opening brackets in the order they were seen; top is the most recent unmatched opener.
- For an opening bracket, pushing preserves the invariant.
- For a closing bracket, matching and popping ensures that the closest unmatched opener is matched (LIFO), preserving "properly nested" structure.
- **Termination:** At the end, the string is valid iff the stack is empty (all openers have been matched).
Discrete math concepts: **Induction on string length** (Epp 5.2), **invariants** for iterative correctness, **well-formedness via parenthesis grammar**.
Citations: (week_1/discrete_math_chapter_5_complete.md#52-mathematical-induction-i), (week_4/chapter_2_complete.md#21-insertion-sort) for invariant method.

**Complexity:**
- Time: Θ(n).
- Space: O(n) in worst case for stack of all openers.
Equation: Single scan ⇒ ∑ O(1) operations per symbol.

---

## 3) Merge Two Sorted Lists (LeetCode 21)

**Problem:** Given heads of two sorted linked lists l1 and l2, merge them into a single sorted list and return its head.

**Key Idea:** Use two pointers; repeatedly choose the smaller head to append to a new list; advance one pointer; continue until one list empties; then append the remaining list.

**Algorithm (Iterative):**
```
dummy = new node
tail = dummy
p = l1; q = l2
while p and q:
    if p.val <= q.val:
        tail.next = p; p = p.next
    else:
        tail.next = q; q = q.next
    tail = tail.next
if p: tail.next = p
else: tail.next = q
return dummy.next
```

**Correctness Sketch:**
- **Invariant:** At the start of each loop, the list starting at dummy.next contains exactly the smallest elements among those already consumed from p and q, in sorted order; tail points to its last node; p and q point to the next unmerged nodes.
- Each iteration links the smaller of p.val and q.val to the result, preserving sorted order (since both input lists are sorted and we always take the smallest next element).
- **Termination:** When one list is exhausted, appending the remainder keeps the overall list sorted (the remainder is already sorted and all its elements are ≥ the last added node).
Discrete math concepts: **Induction on the number of selected nodes**, **invariants**, and **total order** preservation.
Citations: (week_1/discrete_math_chapter_5_complete.md#52-mathematical-induction-i), (week_4/chapter_2_complete.md#21-insertion-sort).

**Complexity:**
- Time: Θ(n+m), scanning each list once.
- Space: O(1) additional (beyond the nodes themselves) in the iterative approach.
Equation: The while-loop performs at most (n+m) iterations, each O(1).

---

## 4) Number of Islands (LeetCode 200) — Sketch

**Problem:** Given a 2D grid of '1's (land) and '0's (water), count the number of islands (connected components) using 4-directional adjacency.

**Key Idea:** View grid as an undirected graph; use DFS/BFS to mark all vertices reachable from any unvisited '1'; count connected components.

**Algorithm Outline:**
- For each cell (i,j): if grid[i][j]=='1' and unvisited, increment count and DFS/BFS to mark all reachable '1' cells.

**Correctness:** Connected component detection via reachability; **equivalence relation** of "is in the same island" partitions land cells into disjoint sets; counting is counting the partitions.
Citations: Equivalence relations and partitions (week_2/discrete_math_chapter_8_complete_full.md#definition-4), transitive closure notion (reachability) (…#the-transitive-closure-of-a-relation).

**Complexity:** Θ(R·C), proportional to total cells; BFS/DFS each cell/edge once.

---

## 5) Subsets / Power Set (LeetCode 78) — Sketch

**Problem:** Given distinct integers, return all possible subsets.

**Key Idea:** Use backtracking or bitmasking; the count is \(2^n\).

**Correctness:** Each element either appears or not ⇒ 2 choices per element; by **multiplication rule**, total = \(2 \cdot 2 \cdots 2 = 2^n\).
Citations: (week_2/discrete_math_chapter_9_1_9_2_9_3.md#theorem-921-the-multiplication-rule), combinations (week_2/discrete_math_chapter_9_5.md).

**Complexity:** O(n·2^n) to output all subsets.

---

## 6) Climbing Stairs (LeetCode 70) — Sketch

**Problem:** Ways to climb n stairs taking 1 or 2 steps.

**Key Idea:** Recurrence \(F(n)=F(n-1)+F(n-2)\) with bases \(F(0)=1, F(1)=1\) ⇒ Fibonacci numbers.

**Correctness:** At step n, last move was 1-step (ways F(n−1)) or 2-step (ways F(n−2)); mutually exclusive and exhaustive; add counts (**addition rule**).
Citations: (week_1/discrete_math_chapter_5_complete.md#example-566-the-fibonacci-numbers), (week_2/discrete_math_chapter_9_1_9_2_9_3.md#theorem-931-the-addition-rule).

**Complexity:** DP Θ(n) time, Θ(1) space (rolling vars).

---

## Notes on Proofs/Equations Used
- **Invariant proofs** (Valid Parentheses, Merge Two Lists) rely on Epp/CLRS templates.
- **Summations** appear in Insertion Sort analysis; **recurrences** in Climbing Stairs.
- **Counting** uses multiplication and addition rules; **equivalence relations** motivate components.

---