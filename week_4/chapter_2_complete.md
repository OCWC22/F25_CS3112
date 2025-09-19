# Chapter 2: Getting Started (Pages 44-78)

## Page 44

# 2 Getting Started

This chapter will familiarize you with the framework we'll use throughout the book to think about the design and analysis of algorithms. It is self-contained, but it does include several references to material that will be introduced in Chapters 3 and 4. (It also contains several summations, which Appendix A shows how to solve.)

We'll begin by examining the insertion sort algorithm to solve the sorting problem introduced in Chapter 1. We'll specify algorithms using a pseudocode that should be understandable to you if you have done computer programming. We'll see why insertion sort correctly sorts and analyze its running time. The analysis introduces a notation that describes how running time increases with the number of items to be sorted. Following a discussion of insertion sort, we'll use a method called divide-and-conquer to develop a sorting algorithm called merge sort. We'll end with an analysis of merge sort's running time.

## 2.1 Insertion sort

Our first algorithm, insertion sort, solves the sorting problem introduced in Chapter 1:

**Input:** A sequence of n numbers ⟨a₁, a₂, …, aₙ⟩.

**Output:** A permutation (reordering) ⟨a'₁, a'₂, …, a'ₙ⟩ of the input sequence such that a'₁ ≤ a'₂ ≤ … ≤ a'ₙ.

## Page 45

The numbers to be sorted are also known as the keys. Although the problem is conceptually about sorting a sequence, the input comes in the form of an array with n elements. When we want to sort numbers, it's often because they are the keys associated with other data, which we call satellite data. Together, a key and satellite data form a record. For example, consider a spreadsheet containing student records with many associated pieces of data such as age, grade-point average, and number of courses taken. Any one of these quantities could be a key, but when the spreadsheet sorts, it moves the associated record (the satellite data) with the key. When describing a sorting algorithm, we focus on the keys, but it is important to remember that there usually is associated satellite data.

In this book, we'll typically describe algorithms as procedures written in a pseudocode that is similar in many respects to C, C++, Java, Python,¹ or JavaScript. (Apologies if we've omitted your favorite programming language. We can't list them all.) If you have been introduced to any of these languages, you should have little trouble understanding algorithms "coded" in pseudocode. What separates pseudocode from real code is that in pseudocode, we employ whatever expressive method is most clear and concise to specify a given algorithm. Sometimes the clearest method is English, so do not be surprised if you come across an English phrase or sentence embedded within a section that looks more like real code. Another difference between pseudocode and real code is that pseudocode often ignores aspects of software engineering—such as data abstraction, modularity, and error handling—in order to convey the essence of the algorithm more concisely.

We start with insertion sort, which is an efficient algorithm for sorting a small number of elements. Insertion sort works the way you might sort a hand of playing cards. Start with an empty left hand and the cards in a pile on the table. Pick up the first card in the pile and hold it with your left hand. Then, with your right hand, remove one card at a time from the pile, and insert it into the correct position in your left hand. As Figure 2.1 illustrates, you find the correct position for a card by comparing it with each of the cards already in your left hand,

## Page 46

starting at the right and moving left. As soon as you see a card in your left hand whose value is less than or equal to the card you're holding in your right hand, insert the card that you're holding in your right hand just to the right of this card in your left hand. If all the cards in your left hand have values greater than the card in your right hand, then place this card as the leftmost card in your left hand. At all times, the cards held in your left hand are sorted, and these cards were originally the top cards of the pile on the table.

The pseudocode for insertion sort is given as the procedure INSERTION-SORT on the facing page. It takes two parameters: an array A containing the values to be sorted and the number n of values to sort. The values occupy positions A[1] through A[n] of the array, which we denote by A[1 : n]. When the INSERTION-SORT procedure is finished, array A[1 : n] contains the original values, but in sorted order.

**Figure 2.1** Sorting a hand of cards using insertion sort.

```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1 : i – 1].
4      j = i – 1
5      while j > 0 and A[j] > key
```

## Page 47

```
6          A[j + 1] = A[j]
7          j = j – 1
8      A[j + 1] = key
```

### Loop invariants and the correctness of insertion sort

Figure 2.2 shows how this algorithm works for an array A that starts out with the sequence ⟨5, 2, 4, 6, 1, 3⟩. The index i indicates the "current card" being inserted into the hand. At the beginning of each iteration of the for loop, which is indexed by i, the subarray (a contiguous portion of the array) consisting of elements A[1 : i – 1] (that is, A[1] through A[i – 1]) constitutes the currently sorted hand, and the remaining subarray A[i + 1 : n] (elements A[i + 1] through A[n]) corresponds to the pile of cards still on the table. In fact, elements A[1 : i – 1] are the elements originally in positions 1 through i – 1, but now in sorted order. We state these properties of A[1 : i – 1] formally as a loop invariant:

**Figure 2.2** The operation of INSERTION-SORT(A, n), where A initially contains the sequence ⟨5, 2, 4, 6, 1, 3⟩ and n = 6. Array indices appear above the rectangles, and values stored in the array positions appear within the rectangles. (a)–(e) The iterations of the for loop of lines 1–8. In each iteration, the blue rectangle holds the key taken from A[i], which is compared with the values in tan rectangles to its left in the test of line 5. Orange arrows show array values moved one position to the right in line 6, and blue arrows indicate where the key moves to in line 8. (f) The final sorted array.

> At the start of each iteration of the for loop of lines 1–8, the subarray A[1 : i – 1] consists of the elements originally in A[1 : i – 1], but in sorted order.

Loop invariants help us understand why an algorithm is correct. When you're using a loop invariant, you need to show three things:

## Page 48

**Initialization:** It is true prior to the first iteration of the loop.

**Maintenance:** If it is true before an iteration of the loop, it remains true before the next iteration.

**Termination:** The loop terminates, and when it terminates, the invariant—usually along with the reason that the loop terminated—gives us a useful property that helps show that the algorithm is correct.

When the first two properties hold, the loop invariant is true prior to every iteration of the loop. (Of course, you are free to use established facts other than the loop invariant itself to prove that the loop invariant remains true before each iteration.) A loop-invariant proof is a form of mathematical induction, where to prove that a property holds, you prove a base case and an inductive step. Here, showing that the invariant holds before the first iteration corresponds to the base case, and showing that the invariant holds from iteration to iteration corresponds to the inductive step.

The third property is perhaps the most important one, since you are using the loop invariant to show correctness. Typically, you use the loop invariant along with the condition that caused the loop to terminate. Mathematical induction typically applies the inductive step infinitely, but in a loop invariant the "induction" stops when the loop terminates.

Let's see how these properties hold for insertion sort.

**Initialization:** We start by showing that the loop invariant holds before the first loop iteration, when i = 2.² The subarray A[1 : i – 1] consists of just the single element A[1], which is in fact the original element in A[1]. Moreover, this subarray is sorted (after all, how could a subarray with just one value not be sorted?), which shows that the loop invariant holds prior to the first iteration of the loop.

**Maintenance:** Next, we tackle the second property: showing that each iteration maintains the loop invariant. Informally, the body of the for loop works by moving the values in A[i – 1], A[i – 2], A[i – 3], and so on by one position to the right until it finds the proper position for A[i] (lines 4–7), at which point it inserts the value of A[i] (line 8). The subarray A[1 : i] then consists of the elements originally in A[1 : i], but

## Page 49

in sorted order. Incrementing i (increasing its value by 1) for the next iteration of the for loop then preserves the loop invariant.

A more formal treatment of the second property would require us to state and show a loop invariant for the while loop of lines 5–7. Let's not get bogged down in such formalism just yet. Instead, we'll rely on our informal analysis to show that the second property holds for the outer loop.

**Termination:** Finally, we examine loop termination. The loop variable i starts at 2 and increases by 1 in each iteration. Once i's value exceeds n in line 1, the loop terminates. That is, the loop terminates once i equals n + 1. Substituting n + 1 for i in the wording of the loop invariant yields that the subarray A[1 : n] consists of the elements originally in A[1 : n], but in sorted order. Hence, the algorithm is correct.

This method of loop invariants is used to show correctness in various places throughout this book.

### Pseudocode conventions

We use the following conventions in our pseudocode.

• **Indentation** indicates block structure. For example, the body of the for loop that begins on line 1 consists of lines 2–8, and the body of the while loop that begins on line 5 contains lines 6–7 but not line 8. Our indentation style applies to if-else statements³ as well. Using indentation instead of textual indicators of block structure, such as begin and end statements or curly braces, reduces clutter while preserving, or even enhancing, clarity.⁴

• The looping constructs **while**, **for**, and **repeat-until** and the **if-else** conditional construct have interpretations similar to those in C, C++, Java, Python, and JavaScript.⁵ In this book, the loop counter retains its value after the loop is exited, unlike some situations that arise in C++ and Java. Thus, immediately after a for loop, the loop counter's value is the value that first exceeded

## Page 50

the for loop bound.⁶ We used this property in our correctness argument for insertion sort. The for loop header in line 1 is **for i = 2 to n**, and so when this loop terminates, i equals n + 1. We use the keyword **to** when a for loop increments its loop counter in each iteration, and we use the keyword **downto** when a for loop decrements its loop counter (reduces its value by 1 in each iteration). When the loop counter changes by an amount greater than 1, the amount of change follows the optional keyword **by**.

• The symbol "**//**" indicates that the remainder of the line is a comment.

• **Variables** (such as i, j, and key) are local to the given procedure. We won't use global variables without explicit indication.

• We access **array elements** by specifying the array name followed by the index in square brackets. For example, A[i] indicates the ith element of the array A.

• Although many programming languages enforce 0-origin indexing for arrays (0 is the smallest valid index), we choose whichever indexing scheme is clearest for human readers to understand. Because people usually start counting at 1, not 0, most—but not all—of the arrays in this book use 1-origin indexing. To be clear about whether a particular algorithm assumes 0-origin or 1-origin indexing, we'll specify the bounds of the arrays explicitly. If you are implementing an algorithm that we specify using 1-origin indexing, but you're writing in a programming language that enforces 0-origin indexing (such as C, C++, Java, Python, or JavaScript), then give yourself credit for being able to adjust. You can either always subtract 1 from each index or allocate each array with one extra position and just ignore position 0.

• The notation "**:**" denotes a subarray. Thus, A[i : j] indicates the subarray of A consisting of the elements A[i], A[i + 1], …, A[j].⁷ We also use this notation to indicate the bounds of an array, as we did earlier when discussing the array A[1 : n].

## Page 51

• We typically organize compound data into **objects**, which are composed of **attributes**. We access a particular attribute using the syntax found in many object-oriented programming languages: the object name, followed by a dot, followed by the attribute name. For example, if an object x has attribute f, we denote this attribute by x.f.

• We treat a variable representing an array or object as a **pointer** (known as a reference in some programming languages) to the data representing the array or object. For all attributes f of an object x, setting y = x causes y.f to equal x.f. Moreover, if we now set x.f = 3, then afterward not only does x.f equal 3, but y.f equals 3 as well. In other words, x and y point to the same object after the assignment y = x. This way of treating arrays and objects is consistent with most contemporary programming languages.

• Our attribute notation can "cascade." For example, suppose that the attribute f is itself a pointer to some type of object that has an attribute g. Then the notation x.f.g is implicitly parenthesized as (x.f).g. In other words, if we had assigned y = x.f, then x.f.g is the same as y.g.

• Sometimes a pointer refers to no object at all. In this case, we give it the special value **NIL**.

• We pass parameters to a procedure **by value**: the called procedure receives its own copy of the parameters, and if it assigns a value to a parameter, the change is not seen by the calling procedure. When objects are passed, the pointer to the data representing the object is copied, but the object's attributes are not. For example, if x is a parameter of a called procedure, the assignment x = y within the called procedure is not visible to the calling procedure. The assignment x.f = 3, however, is visible if the calling procedure has a pointer to the same object as x. Similarly, arrays are passed by pointer, so that a pointer to the array is passed, rather than the entire array, and changes to individual array elements are visible to the calling procedure. Again, most contemporary programming languages work this way.

## Page 52

• A **return** statement immediately transfers control back to the point of call in the calling procedure. Most return statements also take a value to pass back to the caller. Our pseudocode differs from many programming languages in that we allow multiple values to be returned in a single return statement without having to create objects to package them together.⁸

• The boolean operators "**and**" and "**or**" are short circuiting. That is, evaluate the expression "x and y" by first evaluating x. If x evaluates to FALSE, then the entire expression cannot evaluate to TRUE, and therefore y is not evaluated. If, on the other hand, x evaluates to TRUE, y must be evaluated to determine the value of the entire expression. Similarly, in the expression "x or y" the expression y is evaluated only if x evaluates to FALSE. Short-circuiting operators allow us to write boolean expressions such as "x ≠ NIL and x.f = y" without worrying about what happens upon evaluating x.f when x is NIL.

• The keyword **error** indicates that an error occurred because conditions were wrong for the procedure to have been called, and the procedure immediately terminates. The calling procedure is responsible for handling the error, and so we do not specify what action to take.

### Exercises

**2.1-1**

Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on an array initially containing the sequence ⟨31, 41, 59, 26, 41, 58⟩.

**2.1-2**

Consider the procedure SUM-ARRAY on the facing page. It computes the sum of the n numbers in array A[1 : n]. State a loop invariant for this procedure, and use its initialization, maintenance, and termination properties to show that the SUM-ARRAY procedure returns the sum of the numbers in A[1 : n].

## Page 53

```
SUM-ARRAY(A, n)
1  sum = 0
2  for i = 1 to n
3      sum = sum + A[i]
4  return sum
```

**2.1-3**

Rewrite the INSERTION-SORT procedure to sort into monotonically decreasing instead of monotonically increasing order.

**2.1-4**

Consider the searching problem:

**Input:** A sequence of n numbers ⟨a₁, a₂, …, aₙ⟩ stored in array A[1 : n] and a value x.

**Output:** An index i such that x equals A[i] or the special value NIL if x does not appear in A.

Write pseudocode for **linear search**, which scans through the array from beginning to end, looking for x. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

**2.1-5**

Consider the problem of adding two n-bit binary integers a and b, stored in two n-element arrays A[0 : n – 1] and B[0 : n – 1], where each element is either 0 or 1, a = ∑ᵢ₌₀ⁿ⁻¹ A[i]·2ⁱ, and b = ∑ᵢ₌₀ⁿ⁻¹ B[i]·2ⁱ. The sum c = a + b of the two integers should be stored in binary form in an (n + 1)-element array C[0 : n], where c = ∑ᵢ₌₀ⁿ C[i]·2ⁱ. Write a procedure ADD-BINARY-INTEGERS that takes as input arrays A and B, along with the length n, and returns array C holding the sum.

## 2.2 Analyzing algorithms

## Page 54

Analyzing an algorithm has come to mean predicting the resources that the algorithm requires. You might consider resources such as memory, communication bandwidth, or energy consumption. Most often, however, you'll want to measure computational time. If you analyze several candidate algorithms for a problem, you can identify the most efficient one. There might be more than just one viable candidate, but you can often rule out several inferior algorithms in the process.

Before you can analyze an algorithm, you need a model of the technology that it runs on, including the resources of that technology and a way to express their costs. Most of this book assumes a generic one-processor, **random-access machine (RAM)** model of computation as the implementation technology, with the understanding that algorithms are implemented as computer programs. In the RAM model, instructions execute one after another, with no concurrent operations.

The RAM model assumes that each instruction takes the same amount of time as any other instruction and that each data access—using the value of a variable or storing into a variable—takes the same amount of time as any other data access. In other words, in the RAM model each instruction or data access takes a constant amount of time—even indexing into an array.⁹

Strictly speaking, we should precisely define the instructions of the RAM model and their costs. To do so, however, would be tedious and yield little insight into algorithm design and analysis. Yet we must be careful not to abuse the RAM model. For example, what if a RAM had an instruction that sorts? Then you could sort in just one step. Such a RAM would be unrealistic, since such instructions do not appear in real computers. Our guide, therefore, is how real computers are designed.

The RAM model contains instructions commonly found in real computers: arithmetic (such as add, subtract, multiply, divide, remainder, floor, ceiling), data movement (load, store, copy), and control (conditional and unconditional branch, subroutine call and return).

The data types in the RAM model are integer, floating point (for storing real-number approximations), and character. Real computers do not usually have a separate data type for the boolean values TRUE and

## Page 55

FALSE. Instead, they often test whether an integer value is 0 (FALSE) or nonzero (TRUE), as in C. Although we typically do not concern ourselves with precision for floating-point values in this book (many numbers cannot be represented exactly in floating point), precision is crucial for most applications. We also assume that each word of data has a limit on the number of bits. For example, when working with inputs of size n, we typically assume that integers are represented by c log₂ n bits for some constant c ≥ 1. We require c ≥ 1 so that each word can hold the value of n, enabling us to index the individual input elements, and we restrict c to be a constant so that the word size does not grow arbitrarily. (If the word size could grow arbitrarily, we could store huge amounts of data in one word and operate on it all in constant time—an unrealistic scenario.)

Real computers contain instructions not listed above, and such instructions represent a gray area in the RAM model. For example, is exponentiation a constant-time instruction? In the general case, no: to compute xⁿ when x and n are general integers typically takes time logarithmic in n (see equation (31.34) on page 934), and you must worry about whether the result fits into a computer word. If n is an exact power of 2, however, exponentiation can usually be viewed as a constant-time operation. Many computers have a "shift left" instruction, which in constant time shifts the bits of an integer by n positions to the left. In most computers, shifting the bits of an integer by 1 position to the left is equivalent to multiplying by 2, so that shifting the bits by n positions to the left is equivalent to multiplying by 2ⁿ. Therefore, such computers can compute 2ⁿ in 1 constant-time instruction by shifting the integer 1 by n positions to the left, as long as n is no more than the number of bits in a computer word. We'll try to avoid such gray areas in the RAM model and treat computing 2ⁿ and multiplying by 2ⁿ as constant-time operations when the result is small enough to fit in a computer word.

The RAM model does not account for the memory hierarchy that is common in contemporary computers. It models neither caches nor virtual memory. Several other computational models attempt to

## Page 56

account for memory-hierarchy effects, which are sometimes significant in real programs on real machines. Section 11.5 and a handful of problems in this book examine memory-hierarchy effects, but for the most part, the analyses in this book do not consider them. Models that include the memory hierarchy are quite a bit more complex than the RAM model, and so they can be difficult to work with. Moreover, RAM-model analyses are usually excellent predictors of performance on actual machines.

Although it is often straightforward to analyze an algorithm in the RAM model, sometimes it can be quite a challenge. You might need to employ mathematical tools such as combinatorics, probability theory, algebraic dexterity, and the ability to identify the most significant terms in a formula. Because an algorithm might behave differently for each possible input, we need a means for summarizing that behavior in simple, easily understood formulas.

### Analysis of insertion sort

How long does the INSERTION-SORT procedure take? One way to tell would be for you to run it on your computer and time how long it takes to run. Of course, you'd first have to implement it in a real programming language, since you cannot run our pseudocode directly. What would such a timing test tell you? You would find out how long insertion sort takes to run on your particular computer, on that particular input, under the particular implementation that you created, with the particular compiler or interpreter that you ran, with the particular libraries that you linked in, and with the particular background tasks that were running on your computer concurrently with your timing test (such as checking for incoming information over a network). If you run insertion sort again on your computer with the same input, you might even get a different timing result. From running just one implementation of insertion sort on just one computer and on just one input, what would you be able to determine about insertion sort's running time if you were to give it a different input, if you were to run it on a different computer, or if you were to implement it in a different

## Page 57

programming language? Not much. We need a way to predict, given a new input, how long insertion sort will take.

Instead of timing a run, or even several runs, of insertion sort, we can determine how long it takes by analyzing the algorithm itself. We'll examine how many times it executes each line of pseudocode and how long each line of pseudocode takes to run. We'll first come up with a precise but complicated formula for the running time. Then, we'll distill the important part of the formula using a convenient notation that can help us compare the running times of different algorithms for the same problem.

How do we analyze insertion sort? First, let's acknowledge that the running time depends on the input. You shouldn't be terribly surprised that sorting a thousand numbers takes longer than sorting three numbers. Moreover, insertion sort can take different amounts of time to sort two input arrays of the same size, depending on how nearly sorted they already are. Even though the running time can depend on many features of the input, we'll focus on the one that has been shown to have the greatest effect, namely the size of the input, and describe the running time of a program as a function of the size of its input. To do so, we need to define the terms "running time" and "input size" more carefully. We also need to be clear about whether we are discussing the running time for an input that elicits the worst-case behavior, the best-case behavior, or some other case.

The best notion for **input size** depends on the problem being studied. For many problems, such as sorting or computing discrete Fourier transforms, the most natural measure is the number of items in the input—for example, the number n of items being sorted. For many other problems, such as multiplying two integers, the best measure of input size is the total number of bits needed to represent the input in ordinary binary notation. Sometimes it is more appropriate to describe the size of the input with more than just one number. For example, if the input to an algorithm is a graph, we usually characterize the input size by both the number of vertices and the number of edges in the graph. We'll indicate which input size measure is being used with each problem we study.

## Page 58

The **running time** of an algorithm on a particular input is the number of instructions and data accesses executed. How we account for these costs should be independent of any particular computer, but within the framework of the RAM model. For the moment, let us adopt the following view. A constant amount of time is required to execute each line of our pseudocode. One line might take more or less time than another line, but we'll assume that each execution of the kth line takes cₖ time, where cₖ is a constant. This viewpoint is in keeping with the RAM model, and it also reflects how the pseudocode would be implemented on most actual computers.¹⁰

Let's analyze the INSERTION-SORT procedure. As promised, we'll start by devising a precise formula that uses the input size and all the statement costs cₖ. This formula turns out to be messy, however. We'll then switch to a simpler notation that is more concise and easier to use. This simpler notation makes clear how to compare the running times of algorithms, especially as the size of the input increases.

To analyze the INSERTION-SORT procedure, let's view it on the following page with the time cost of each statement and the number of times each statement is executed. For each i = 2, 3, …, n, let tᵢ denote the number of times the while loop test in line 5 is executed for that value of i. When a for or while loop exits in the usual way—because the test in the loop header comes up FALSE—the test is executed one time more than the loop body. Because comments are not executable statements, assume that they take no time.

The running time of the algorithm is the sum of running times for each statement executed. A statement that takes cₖ steps to execute and executes m times contributes cₖm to the total running time.¹¹ We usually denote the running time of an algorithm on an input of size n by T(n). To compute T(n), the running time of INSERTION-SORT on an input of n values, we sum the products of the cost and times columns, obtaining

```
INSERTION-SORT(A, n)                              cost    times
```

## Page 59

```
1  for i = 2 to n                                 c₁      n
2      key = A[i]                                 c₂      n - 1
3      // Insert A[i] into the sorted             0       n - 1
       // subarray A[1 : i - 1].
4      j = i - 1                                  c₄      n - 1
5      while j > 0 and A[j] > key                 c₅      ∑ᵢ₌₂ⁿ tᵢ
6          A[j + 1] = A[j]                        c₆      ∑ᵢ₌₂ⁿ(tᵢ - 1)
7          j = j - 1                              c₇      ∑ᵢ₌₂ⁿ(tᵢ - 1)
8      A[j + 1] = key                             c₈      n - 1
```

T(n) = c₁n + c₂(n - 1) + c₄(n - 1) + c₅∑ᵢ₌₂ⁿ tᵢ + c₆∑ᵢ₌₂ⁿ(tᵢ - 1) + c₇∑ᵢ₌₂ⁿ(tᵢ - 1) + c₈(n - 1).

Even for inputs of a given size, an algorithm's running time may depend on which input of that size is given. For example, in INSERTION-SORT, the best case occurs when the array is already sorted. In this case, each time that line 5 executes, the value of key—the value originally in A[i]—is already greater than or equal to all values in A[1 : i - 1], so that the while loop of lines 5–7 always exits upon the first test in line 5. Therefore, we have that tᵢ = 1 for i = 2, 3, …, n, and the best-case running time is given by

T(n) = c₁n + c₂(n - 1) + c₄(n - 1) + c₅(n - 1) + c₈(n - 1)
     = (c₁ + c₂ + c₄ + c₅ + c₈)n - (c₂ + c₄ + c₅ + c₈).     (2.1)

We can express this running time as an + b for constants a and b that depend on the statement costs cₖ (where a = c₁ + c₂ + c₄ + c₅ + c₈ and b = -(c₂ + c₄ + c₅ + c₈)). The running time is thus a linear function of n.

The worst case arises when the array is in reverse sorted order—that is, it starts out in decreasing order. The procedure must compare each element A[i] with each element in the entire sorted subarray A[1 : i - 1], and so tᵢ = i for i = 2, 3, …, n. (The procedure finds that A[j] > key

## Page 60

every time in line 5, and the while loop exits only when j reaches 0.) Noting that

∑ᵢ₌₂ⁿ i = n(n + 1)/2 - 1

and

∑ᵢ₌₂ⁿ(i - 1) = n(n - 1)/2,

we find that in the worst case, the running time of INSERTION-SORT is

T(n) = c₁n + c₂(n - 1) + c₄(n - 1) + c₅(n(n + 1)/2 - 1) + c₆(n(n - 1)/2) + c₇(n(n - 1)/2) + c₈(n - 1)
     = (c₅/2 + c₆/2 + c₇/2)n² + (c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈)n - (c₂ + c₄ + c₅ + c₈).     (2.2)

We can express this worst-case running time as an² + bn + c for constants a, b, and c that again depend on the statement costs cₖ (now, a = c₅/2 + c₆/2 + c₇/2, b = c₁ + c₂ + c₄ + c₅/2 - c₆/2 - c₇/2 + c₈, and c = -(c₂ + c₄ + c₅ + c₈)). The running time is thus a quadratic function of n.

Typically, as in insertion sort, the running time of an algorithm is fixed for a given input, although we'll also see some interesting "randomized" algorithms whose behavior can vary even for a fixed input.

### Worst-case and average-case analysis

## Page 61

Our analysis of insertion sort looked at both the best case, in which the input array was already sorted, and the worst case, in which the input array was reverse sorted. For the remainder of this book, though, we'll usually (but not always) concentrate on finding only the **worst-case running time**, that is, the longest running time for any input of size n. Why? Here are three reasons:

• The worst-case running time of an algorithm gives an upper bound on the running time for any input. If you know it, then you have a guarantee that the algorithm never takes any longer. You need not make some educated guess about the running time and hope that it never gets much worse. This feature is especially important for real-time computing, in which operations must complete by a deadline.

• For some algorithms, the worst case occurs fairly often. For example, in searching a database for a particular piece of information, the searching algorithm's worst case often occurs when the information is not present in the database. In some applications, searches for absent information may be frequent.

• The "average case" is often roughly as bad as the worst case. Suppose that you run insertion sort on an array of n randomly chosen numbers. How long does it take to determine where in subarray A[1 : i - 1] to insert element A[i]? On average, half the elements in A[1 : i - 1] are less than A[i], and half the elements are greater. On average, therefore, A[i] is compared with just half of the subarray A[1 : i - 1], and so tᵢ is about i/2. The resulting average-case running time turns out to be a quadratic function of the input size, just like the worst-case running time.

In some particular cases, we'll be interested in the **average-case** running time of an algorithm. We'll see the technique of probabilistic analysis applied to various algorithms throughout this book. The scope of average-case analysis is limited, because it may not be apparent what constitutes an "average" input for a particular problem. Often, we'll assume that all inputs of a given size are equally likely. In practice, this assumption may be violated, but we can sometimes use a randomized

## Page 62

algorithm, which makes random choices, to allow a probabilistic analysis and yield an **expected running time**. We explore randomized algorithms more in Chapter 5 and in several other subsequent chapters.

### Order of growth

In order to ease our analysis of the INSERTION-SORT procedure, we used some simplifying abstractions. First, we ignored the actual cost of each statement, using the constants cₖ to represent these costs. Still, the best-case and worst-case running times in equations (2.1) and (2.2) are rather unwieldy. The constants in these expressions give us more detail than we really need. That's why we also expressed the best-case running time as an + b for constants a and b that depend on the statement costs cₖ and why we expressed the worst-case running time as an² + bn + c for constants a, b, and c that depend on the statement costs. We thus ignored not only the actual statement costs, but also the abstract costs cₖ.

Let's now make one more simplifying abstraction: it is the **rate of growth**, or **order of growth**, of the running time that really interests us. We therefore consider only the leading term of a formula (e.g., an²), since the lower-order terms are relatively insignificant for large values of n. We also ignore the leading term's constant coefficient, since constant factors are less significant than the rate of growth in determining computational efficiency for large inputs. For insertion sort's worst-case running time, when we ignore the lower-order terms and the leading term's constant coefficient, only the factor of n² from the leading term remains. That factor, n², is by far the most important part of the running time. For example, suppose that an algorithm implemented on a particular machine takes n²/100 + 100n + 17 microseconds on an input of size n. Although the coefficients of 1/100 for the n² term and 100 for the n term differ by four orders of magnitude, the n²/100 term dominates the 100n term once n exceeds 10,000. Although 10,000 might seem large, it is smaller than the population of an average town. Many real-world problems have much larger input sizes.

## Page 63

To highlight the order of growth of the running time, we have a special notation that uses the Greek letter Θ (theta). We write that insertion sort has a worst-case running time of Θ(n²) (pronounced "theta of n-squared" or just "theta n-squared"). We also write that insertion sort has a best-case running time of Θ(n) ("theta of n" or "theta n"). For now, think of Θ-notation as saying "roughly proportional when n is large," so that Θ(n²) means "roughly proportional to n² when n is large" and Θ(n) means "roughly proportional to n when n is large." We'll use Θ-notation informally in this chapter and define it precisely in Chapter 3.

We usually consider one algorithm to be more efficient than another if its worst-case running time has a lower order of growth. Due to constant factors and lower-order terms, an algorithm whose running time has a higher order of growth might take less time for small inputs than an algorithm whose running time has a lower order of growth. But on large enough inputs, an algorithm whose worst-case running time is Θ(n²), for example, takes less time in the worst case than an algorithm whose worst-case running time is Θ(n³). Regardless of the constants hidden by the Θ-notation, there is always some number, say n₀, such that for all input sizes n ≥ n₀, the Θ(n²) algorithm beats the Θ(n³) algorithm in the worst case.

### Exercises

**2.2-1**

Express the function n³/1000 + 100n² - 100n + 3 in terms of Θ-notation.

**2.2-2**

Consider sorting n numbers stored in array A[1 : n] by first finding the smallest element of A[1 : n] and exchanging it with the element in A[1]. Then find the smallest element of A[2 : n], and exchange it with A[2]. Then find the smallest element of A[3 : n], and exchange it with A[3]. Continue in this manner for the first n - 1 elements of A. Write

## Page 64

pseudocode for this algorithm, which is known as **selection sort**. What loop invariant does this algorithm maintain? Why does it need to run for only the first n - 1 elements, rather than for all n elements? Give the worst-case running time of selection sort in Θ-notation. Is the best-case running time any better?

**2.2-3**

Consider linear search again (see Exercise 2.1-4). How many elements of the input array need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? Using Θ-notation, give the average-case and worst-case running times of linear search. Justify your answers.

**2.2-4**

How can you modify any sorting algorithm to have a good best-case running time?

## 2.3 Designing algorithms

You can choose from a wide range of algorithm design techniques. Insertion sort uses the incremental method: for each element A[i], insert it into its proper place in the subarray A[1 : i], having already sorted the subarray A[1 : i – 1].

This section examines another design method, known as "divide-and-conquer," which we explore in more detail in Chapter 4. We'll use divide-and-conquer to design a sorting algorithm whose worst-case running time is much less than that of insertion sort. One advantage of using an algorithm that follows the divide-and-conquer method is that analyzing its running time is often straightforward, using techniques that we'll explore in Chapter 4.

[Section 2.3 content continues through Page 78 as in chapter_2_section_2_3_complete.md]

## Problems

### 2-1 Insertion sort on small arrays in merge sort

Although merge sort runs in Θ(n lg n) worst-case time and insertion sort runs in Θ(n²) worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which n/k sublists of length k are sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

a. Show that insertion sort can sort the n/k sublists, each of length k, in Θ(nk) worst-case time.

b. Show how to merge the sublists in Θ(n lg(n/k)) worst-case time.

c. Given that the modified algorithm runs in Θ(nk + n lg(n/k)) worst-case time, what is the largest value of k as a function of n for which the modified algorithm has the same running time as standard merge sort, in terms of Θ-notation?

d. How should you choose k in practice?

### 2-2 Correctness of bubblesort

Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order. The procedure BUBBLESORT sorts array A[1 : n].

```
BUBBLESORT(A, n)
1  for i = 1 to n – 1
2      for j = n downto i + 1
3          if A[j] < A[j – 1]
4              exchange A[j] with A[j – 1]
```

a. Let A′ denote the array A after BUBBLESORT(A, n) is executed. To prove that A′[1] ≤ A′[2] ≤ … ≤ A′[n], (2.5) in order to show that BUBBLESORT actually sorts, what else do you need to prove?

The next two parts prove inequality (2.5).

b. State precisely a loop invariant for the for loop in lines 2–4, and prove that this loop invariant holds. Your proof should use the structure of the loop-invariant proof presented in this chapter.

c. Using the termination condition of the loop invariant proved in part (b), state a loop invariant for the for loop in lines 1–4 that allows you to prove inequality (2.5). Your proof should use the structure of the loop-invariant proof presented in this chapter.

d. What is the worst-case running time of BUBBLESORT? How does it compare with the running time of INSERTION-SORT?

### 2-3 Correctness of Horner's rule

You are given the coefficients a₀, a₁, a₂, …, aₙ of a polynomial

P(x) = ∑ᵢ₌₀ⁿ aᵢxⁱ = a₀ + x(a₁ + x(a₂ + … + x(aₙ₋₁ + xaₙ)…))

and you want to evaluate this polynomial for a given value of x. Horner's rule says to evaluate the polynomial according to this parenthesization:

P(x) = a₀ + x(a₁ + x(a₂ + … + x(aₙ₋₁ + xaₙ)…)).

The procedure HORNER implements Horner's rule to evaluate P(x), given the coefficients a₀, a₁, a₂, …, aₙ in an array A[0 : n] and the value of x.

```
HORNER(A, n, x)
1  p = 0
2  for i = n downto 0
3      p = A[i] + x · p
4  return p
```

a. In terms of Θ-notation, what is the running time of this procedure?

b. Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare with HORNER?

c. Consider the following loop invariant for the procedure HORNER:

At the start of each iteration of the for loop of lines 2–3,
p = ∑ₖ₌₀ⁿ⁻⁽ⁱ⁺¹⁾ aₙ₋ₖxᵏ.

Interpret a summation with no terms as equaling 0. Following the structure of the loop-invariant proof presented in this chapter, use this loop invariant to show that, at termination, p = P(x).

### 2-4 Inversions

Let A[1 : n] be an array of n distinct numbers. If i < j and A[i] > A[j], then the pair (i, j) is called an **inversion** of A.

a. List the five inversions of the array ⟨2, 3, 8, 6, 1⟩.

b. What array with elements from the set {1, 2, …, n} has the most inversions? How many does it have?

c. What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer.

d. Give an algorithm that determines the number of inversions in any permutation on n elements in Θ(n lg n) worst-case time. (Hint: Modify merge sort.)

## 2.3 Designing algorithms (Section Summary)

### 2.3.2 Analyzing divide-and-conquer algorithms

The merge sort algorithm follows the divide-and-conquer paradigm. Its recurrence for the worst-case running time T(n) is:

**T(n) = 2T(n/2) + Θ(n)**

This recurrence comes from:
- **Divide:** D(n) = Θ(1) (computing the middle takes constant time)
- **Conquer:** 2T(n/2) (recursively solving two subproblems of size n/2)
- **Combine:** C(n) = Θ(n) (merging n elements)

The solution to this recurrence is **T(n) = Θ(n lg n)**, which represents a significant improvement over insertion sort's Θ(n²) worst-case time.

For the general divide-and-conquer recurrence:

**T(n) = aT(n/b) + f(n)**

where:
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = time to divide and combine

## Chapter notes

In 1968, Knuth published the first of three volumes with the general title *The Art of Computer Programming* [259, 260, 261]. The first volume ushered in the modern study of computer algorithms with a focus on the analysis of running time. The full series remains an engaging and worthwhile reference for many of the topics presented here. According to Knuth, the word "algorithm" is derived from the name "al-Khowârizmî," a ninth-century Persian mathematician.

Aho, Hopcroft, and Ullman [5] advocated the asymptotic analysis of algorithms—using notations that Chapter 3 introduces, including Θ-notation—as a means of comparing relative performance. They also popularized the use of recurrence relations to describe the running times of recursive algorithms.

Knuth [261] provides an encyclopedic treatment of many sorting algorithms. His comparison of sorting algorithms (page 381) includes exact step-counting analyses, like the one we performed here for insertion sort. Knuth's discussion of insertion sort encompasses several variations of the algorithm. The most important of these is Shell's sort, introduced by D. L. Shell, which uses insertion sort on periodic subarrays of the input to produce a faster sorting algorithm.

Merge sort is also described by Knuth. He mentions that a mechanical collator capable of merging two decks of punched cards in a single pass was invented in 1938. J. von Neumann, one of the pioneers of computer science, apparently wrote a program for merge sort on the EDVAC computer in 1945.

The early history of proving programs correct is described by Gries [200], who credits P. Naur with the first article in this field. Gries attributes loop invariants to R. W. Floyd. The textbook by Mitchell [329] is a good reference on how to prove programs correct.

---

## Footnotes

¹ If you're familiar with only Python, you can think of arrays as similar to Python lists.

² When the loop is a for loop, the loop-invariant check just prior to the first iteration occurs immediately after the initial assignment to the loop-counter variable and just before the first test in the loop header. In the case of INSERTION-SORT, this time is after assigning 2 to the variable i but before the first test of whether i ≤ n.

³ In an if-else statement, we indent else at the same level as its matching if. The first executable line of an else clause appears on the same line as the keyword else. For multiway tests, we use elseif for tests after the first one. When it is the first line in an else clause, an if statement appears on the line following else so that you do not misconstrue it as elseif.

⁴ Each pseudocode procedure in this book appears on one page so that you do not need to discern levels of indentation in pseudocode that is split across pages.

⁵ Most block-structured languages have equivalent constructs, though the exact syntax may differ. Python lacks repeat-until loops, and its for loops operate differently from the for loops in this book. Think of the pseudocode line "for i = 1 to n" as equivalent to "for i in range(1, n+1)" in Python.

⁶ In Python, the loop counter retains its value after the loop is exited, but the value it retains is the value it had during the final iteration of the for loop, rather than the value that exceeded the loop bound. That is because a Python for loop iterates through a list, which may contain nonnumeric values.

⁷ If you're used to programming in Python, bear in mind that in this book, the subarray A[i : j] includes the element A[j]. In Python, the last element of A[i : j] is A[j - 1]. Python allows negative indices, which count from the back end of the list. This book does not use negative array indices.

⁸ Python's tuple notation allows return statements to return multiple values without creating objects from a programmer-defined class.

⁹ We assume that each element of a given array occupies the same number of bytes and that the elements of a given array are stored in contiguous memory locations...

¹⁰ There are some subtleties here. Computational steps that we specify in English are often variants of a procedure that requires more than just a constant amount of time...

¹¹ This characteristic does not necessarily hold for a resource such as memory. A statement that references m words of memory and is executed n times does not necessarily reference mn distinct words of memory.

[Additional footnotes for Section 2.3 as previously included...]