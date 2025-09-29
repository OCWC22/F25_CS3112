# Section 4.5 Homework Solutions

This document provides step-by-step solutions for the problems in Section 4.5 of the algorithms textbook. I've added more detailed, intuitive explanations to help you understand the reasoning without needing to memorize formulas or have advanced math knowledge. Think of these as puzzle-solving strategies that make sense step by step.

## Understanding the Master Method Intuitively

The "master method" is like a shortcut for solving a specific type of puzzle called "recurrences" (equations that define a problem in terms of smaller versions of itself). Imagine you have a big task that you break down into smaller tasks, plus some extra work.

The general puzzle looks like this: T(n) = a × T(n/b) + f(n)
- **a** is how many smaller versions of the same task you create (like splitting one job into 2 smaller jobs)
- **b** is how much smaller each version is (like each small job is 1/4 the size of the original)
- **f(n)** is the extra work needed to combine the results (like gluing pieces together)

The method has three cases, like different strategies depending on whether the "extra work" (f(n)) is small, medium, or large compared to the work from the smaller tasks:

1. **Case 1:** If the extra work is tiny compared to the smaller tasks, the total time is basically determined by the smaller tasks.
2. **Case 2:** If the extra work is about the same as the smaller tasks, you add a bit more time (like adding an extra layer of work).
3. **Case 3:** If the extra work is huge, that's what dominates the total time.

We'll apply this intuitively to each problem.

## 4.5-1 Master Method Applications

For each recurrence T(n) = 2T(n/4) + f(n), we apply the master method where a=2, b=4, log_b a = log4 2 = 1/2.

### a. T(n) = 2T(n/4) + 1

**Intuitive Explanation:**
- We have a big problem of size n that splits into 2 smaller problems, each of size n/4.
- The extra work to combine them is just 1 unit (very small).
- Since we're creating 2 subproblems and each is 1/4 the size, the "growth rate" is log4 2 = 1/2 (meaning each level reduces size by factor of 4, doubling the work).
- The extra work (1) is much smaller than what the subproblems would cost, so it doesn't affect the total much.
- Result: The time grows like n^{1/2}, because we're essentially doing work proportional to the square root of n.

**Step 1:** Identify parameters: a=2, b=4, f(n)=1  
**Step 2:** Compute log_b a = log4 2 = 1/2  
**Step 3:** Compare f(n)=n^0 with n^{1/2}: n^0 = O(n^{1/2 - ε}) for ε=1/2  
**Step 4:** Since 0 < 1/2, this falls into Case 1  
**Solution:** T(n) = Θ(n^{1/2})

### b. T(n) = 2T(n/4) + √n

**Intuitive Explanation:**
- Big problem splits into 2 smaller ones of size n/4.
- Extra work is √n (square root of n), which grows with n but slowly.
- The subproblems also cost about n^{1/2} each, so the extra work matches the subproblem cost.
- When extra work equals subproblem work, we add one more "layer" of work, so total time is subproblem time times log n.
- Result: Time grows like n^{1/2} times log n.

**Step 1:** Identify parameters: a=2, b=4, f(n)=n^{1/2}  
**Step 2:** Compute log_b a = 1/2  
**Step 3:** Compare f(n)=n^{1/2} with n^{1/2}: f(n) = Θ(n^{1/2})  
**Step 4:** This matches Case 2 with k=0  
**Solution:** T(n) = Θ(n^{1/2} log n)

### c. T(n) = 2T(n/4) + √n lg² n

**Intuitive Explanation:**
- Same split as before: 2 subproblems of size n/4.
- Extra work is √n times (log n)², which is n^{1/2} times a log factor.
- Compared to the subproblem cost of n^{1/2}, this extra work is just a bit more (with two log factors).
- So it's still Case 2, but with k=2, meaning we add three log factors total.
- Result: Time grows like n^{1/2} times log³ n.

**Step 1:** Identify parameters: a=2, b=4, f(n)=n^{1/2} lg² n  
**Step 2:** Compute log_b a = 1/2  
**Step 3:** Compare f(n)=n^{1/2} lg² n with n^{1/2}: f(n) = Θ(n^{1/2} lg² n)  
**Step 4:** This matches Case 2 with k=2  
**Solution:** T(n) = Θ(n^{1/2} lg³ n)

### d. T(n) = 2T(n/4) + n

**Intuitive Explanation:**
- Big problem splits into 2 subproblems of size n/4.
- Extra work is n (linear in n), which is much larger than the subproblem cost of n^{1/2}.
- Since the extra work dominates, the total time should just be the extra work itself.
- We check if this makes sense by seeing if the subproblems don't add much extra cost.
- Result: Time grows like n, matching the extra work.

**Step 1:** Identify parameters: a=2, b=4, f(n)=n  
**Step 2:** Compute log_b a = 1/2  
**Step 3:** Compare f(n)=n^1 with n^{1/2}: 1 > 1/2, so potentially Case 3  
**Step 4:** Check regularity condition: 2f(n/4) ≤ c f(n) for some c<1  
**Step 5:** f(n/4)=n/4, 2(n/4)=n/2 ≤ c n ⇒ c ≥ 1/2  
**Step 6:** Since c=1/2 <1, regularity holds  
**Solution:** T(n) = Θ(n)

### e. T(n) = 2T(n/4) + n²

**Intuitive Explanation:**
- Big problem splits into 2 subproblems of size n/4.
- Extra work is n² (quadratic), which is even larger than the linear case.
- The subproblem cost is n^{1/2}, so n² completely dominates.
- Since the extra work is so huge, the total time is just the extra work.
- Result: Time grows like n².

**Step 1:** Identify parameters: a=2, b=4, f(n)=n²  
**Step 2:** Compute log_b a = 1/2  
**Step 3:** Compare f(n)=n² with n^{1/2}: 2 > 1/2, so potentially Case 3  
**Step 4:** Check regularity condition: 2f(n/4) ≤ c f(n) for some c<1  
**Step 5:** f(n/4)=(n/4)²=n²/16, 2(n²/16)=n²/8 ≤ c n² ⇒ c ≥ 1/8  
**Step 6:** Since c=1/8 <1, regularity holds  
**Solution:** T(n) = Θ(n²)

## 4.5-2 Professor Caesar's Algorithm

**Intuitive Explanation:**
- This is about matrix multiplication algorithms. Strassen's method is a smart way to multiply big matrices faster than the basic method.
- Professor Caesar wants to make an even faster algorithm by dividing matrices into smaller pieces (n/4 size instead of n/2).
- He has 'a' smaller matrix multiplications to do, plus some extra work that's about n².
- To beat Strassen's speed (which grows like n^{2.81}), we need the new algorithm's speed to grow slower than that.
- By calculating, we find that if a ≤ 49, it could potentially be faster.
- So the largest integer a is 49.

**Step 1:** The recurrence is T(n) = a T(n/4) + Θ(n²), where a is the number of subproblems  
**Step 2:** To be faster than Strassen's, we need log₄ a < log₂ 7 ≈ 2.807  
**Step 3:** Calculate 4^{2.807} ≈ 4² × 4^{0.807} ≈ 16 × 3.1 ≈ 49.6  
**Step 4:** Thus, a < 49.6, so largest integer a = 49  

## 4.5-3 Binary Search Recurrence

**Intuitive Explanation:**
- Binary search is like guessing a number by always picking the middle.
- For a list of n items, you check the middle one (constant time), then search half the list.
- So it's 1 subproblem of size n/2, plus constant extra work.
- The subproblem cost is about log n (each step halves the size), and extra work is constant, so it matches Case 2.
- Result: Total time is Θ(log n).

**Step 1:** Identify parameters: a=1, b=2, f(n)=Θ(1)  
**Step 2:** Compute log_b a = log₂ 1 = 0  
**Step 3:** Compare f(n)=Θ(1) with n^0: f(n) = Θ(n^0)  
**Step 4:** This matches Case 2 with k=0  
**Solution:** T(n) = Θ(lg n)

## 4.5-4 Function f(n) = lg n Analysis

**Intuitive Explanation:**
- f(n) = log n grows very slowly - it only increases when n doubles.
- For the regularity check, we see if log(n/2) ≤ c log n. Since log(n/2) = log n - 1, we need 1 ≤ c log n, which for large n means c has to be at least 1.
- So for c < 1, it doesn't hold.
- For the other condition, log n doesn't grow as fast as any n^ε for ε > 0, so it can't satisfy that either.
- This means the master method's Case 3 doesn't apply here.

**Step 1:** Regularity check: f(n/2) ≤ c f(n)  
**Step 2:** lg(n/2) = lg n - 1 ≤ c lg n  
**Step 3:** 1 - 1/lg n ≤ c, for large n, c ≥ 1 - ε, but not for c<1  

**Step 4:** For case 3: f(n) = Ω(n^{0 + ε}) for ε>0  
**Step 5:** lg n = Ω(n^ε) would require lg n ≥ c n^ε for some c, but lg n grows slower than any positive power, so false  

**Conclusion:** Master method cases do not apply directly.
