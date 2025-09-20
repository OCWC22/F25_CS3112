# Discrete Mathematics Chapter 8 - Detailed Example Explanations

This document provides detailed explanations for every example from Chapter 8 of Discrete Mathematics with Applications, following the same format as the detailed explanation for examples in Chapter 4.

## Chapter 8.1 Examples

### Example 8.1.1: The Less-than Relation for Real Numbers
Define a relation L from R to R as follows: For all real numbers x and y,
```
x L y ⇔ x < y.
```

a. Is 57 L 53?
b. Is (−17) L (−14)?
c. Is 143 L 143?
d. Is (−35) L 1?
e. Draw the graph of L as a subset of the Cartesian plane R × R

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation L from ℝ to ℝ where for all real numbers x and y, x L y ⇔ x < y. Then determine if 57 L 53, (−17) L (−14), 143 L 143, (−35) L 1, and describe the graph of L in ℝ × ℝ.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation L from real numbers to real numbers where for all real numbers x and y, x L y if and only if x is less than y. Then determine if fifty-seven L fifty-three, negative seventeen L negative fourteen, one hundred forty-three L one hundred forty-three, negative thirty-five L one, and describe the graph of L in real numbers cross real numbers."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation L":** We're creating a specific relationship or connection called L.
  - **"from ℝ to ℝ":** "ℝ" is the symbol for the set of all real numbers (like ..., -2, -1, 0, 1, 2, 3.14, etc.). This means the relation connects real numbers to real numbers.
  - **"where for all real numbers x and y":** This means we're talking about any possible real numbers, and we're calling them x and y for convenience.
  - **"," (comma):** Just a separator, like a pause in speech.
  - **"x L y":** This is the notation for the relation - we read it as "x L y" or "x is L-related to y."
  - **"⇔":** This symbol means "if and only if" or "is equivalent to." It's like saying "means exactly the same as."
  - **"x < y":** This means "x is less than y" - x is smaller than y.
  - **"Then determine if":** Now we need to check whether each specific pair satisfies this relation.
  - **"57 L 53":** Is 57 less than 53? (No, 57 is greater than 53)
  - **"(−17) L (−14)":** Is negative 17 less than negative 14? (Yes, because -17 is to the left of -14 on the number line)
  - **"143 L 143":** Is 143 less than 143? (No, they're equal)
  - **"(−35) L 1":** Is negative 35 less than 1? (Yes, -35 is much smaller than 1)
  - **"and describe the graph of L":** We need to visualize this relation as points on a coordinate plane.
  - **"in ℝ × ℝ":** "×" means "cross" or "Cartesian product" - it's the set of all ordered pairs (x, y) where both are real numbers.
- **Putting it all together in plain English:** This is defining a relationship where one number is less than another, then asking us to check specific examples and describe what this relationship looks like when plotted on a graph.
- **Why do we use this fancy notation?** It gives us a precise mathematical way to express the "less than" relationship and allows us to ask questions about specific pairs of numbers and visualize the relationship.
- **Assumptions and considerations:** We need to understand what "less than" means for different types of numbers (positive, negative, equal numbers). The thought process is: Compare the first number to the second in each pair and see if the first is smaller.
- **How it works:** This gives us the formal criteria to use when evaluating whether pairs of numbers are related by the less-than relation.

### Example 8.1.2: The Congruence Modulo 2 Relation
Define a relation E from Z to Z as follows: For all (m, n) ∈ Z × Z,
```
m E n ⇔ m − n is even.
```

a. Is 4 E 0? Is 2 E 6? Is 3 E (−3)? Is 5 E 2?
b. List five integers that are related by E to 1.
c. Prove that if n is any odd integer, then n E 1.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation E from ℤ to ℤ where for all integers m and n, m E n ⇔ m − n is even. Then determine if 4 E 0, 2 E 6, 3 E (−3), 5 E 2; list five integers related to 1 by E; and prove that for any odd integer n, n E 1.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation E from integers to integers where for all integers m and n, m E n if and only if m minus n is even. Then determine if four E zero, two E six, three E negative three, five E two; list five integers related to one by E; and prove that for any odd integer n, n E one."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation E":** We're creating a specific relationship called E.
  - **"from ℤ to ℤ":** "ℤ" is the symbol for the set of all integers (..., -3, -2, -1, 0, 1, 2, 3, ...). This means the relation connects integers to integers.
  - **"where for all integers m and n":** We're talking about any possible integers, calling them m and n.
  - **"," (comma):** Just a separator.
  - **"m E n":** The notation for the relation - "m is E-related to n."
  - **"⇔":** "if and only if" or "means exactly the same as."
  - **"m − n is even":** "m minus n" means subtract n from m. "is even" means the result is divisible by 2 (like 2, 4, 6, 8, etc., or -2, -4, -6, etc.).
  - **"Then determine if":** Check whether each pair satisfies this condition.
  - **"4 E 0":** Is 4 - 0 = 4 even? (Yes, 4 is even)
  - **"2 E 6":** Is 2 - 6 = -4 even? (Yes, -4 is even)
  - **"3 E (−3)":** Is 3 - (-3) = 6 even? (Yes, 6 is even)
  - **"5 E 2":** Is 5 - 2 = 3 even? (No, 3 is odd)
  - **"list five integers related to 1 by E":** Find five numbers k such that k - 1 is even.
  - **"prove that for any odd integer n":** Show that if n is odd (not divisible by 2), then...
  - **"n E 1":** ...n - 1 is even.
- **Putting it all together in plain English:** This defines a relationship where two integers differ by an even number, then asks us to check specific examples, find numbers related to 1, and prove a property about odd integers.
- **Why do we use this fancy notation?** It gives us a precise way to express relationships based on even differences between integers.
- **Assumptions and considerations:** We need to understand even/odd numbers and subtraction. The thought process is: For each pair, calculate the difference and check if it's even.
- **How it works:** This gives us the formal definition to use when working with this relation on integers.

### Example 8.1.3: A Relation on a Power Set
Let X = {a, b, c}. Then P(X) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}. Define a relation S from P(X) to Z as follows: For all sets A and B in P(X) (i.e., for all subsets A and B of X),
```
A S B ⇔ A has at least as many elements as B.
```

a. Is {a, b} S {b, c}?
b. Is {a} S ∅?
c. Is {b, c} S {a, b, c}?
d. Is {c} S {a}?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let X = {a, b, c} and P(X) be its power set. Define a relation S from P(X) to ℤ where for all subsets A and B of X, A S B ⇔ A has at least as many elements as B. Then determine if {a, b} S {b, c}, {a} S ∅, {b, c} S {a, b, c}, {c} S {a}.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let X equals the set containing a, b, c and P of X be its power set. Define a relation S from P of X to integers where for all subsets A and B of X, A S B if and only if A has at least as many elements as B. Then determine if the set containing a and b S the set containing b and c, the set containing a S the empty set, the set containing b and c S the set containing a, b, and c, the set containing c S the set containing a."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let X = {a, b, c}":** We're defining a set X that contains three elements: a, b, and c.
  - **"P(X)":** This means "power set of X" - the set of all possible subsets of X.
  - **"be its power set":** P(X) contains all subsets: empty set, singletons, pairs, and the full set.
  - **"Define a relation S":** We're creating a relationship called S.
  - **"from P(X) to ℤ":** The relation connects subsets of X to integers.
  - **"where for all subsets A and B of X":** A and B are any subsets of X.
  - **"A S B":** The notation for the relation.
  - **"⇔":** "if and only if."
  - **"A has at least as many elements as B":** Set A has the same number or more elements than set B.
  - **"Then determine if":** Check each pair of sets.
  - **"{a, b} S {b, c}":** Does the set with a,b have at least as many elements as the set with b,c? (Both have 2 elements, so yes)
  - **"{a} S ∅":** Does the set with a have at least as many elements as the empty set? (1 ≥ 0, so yes)
  - **"{b, c} S {a, b, c}":** Does the set with b,c have at least as many elements as the set with a,b,c? (2 < 3, so no)
  - **"{c} S {a}":** Does the set with c have at least as many elements as the set with a? (Both have 1 element, so yes)
- **Putting it all together in plain English:** This defines a relationship that compares the sizes of subsets, then asks us to check specific examples of set pairs.
- **Why do we use this fancy notation?** It gives us a precise way to compare the sizes of sets within the power set.
- **Assumptions and considerations:** We need to understand sets, subsets, and counting elements. The thought process is: Count elements in each set and compare.
- **How it works:** This gives us the formal criteria for comparing set sizes.

### Example 8.1.4: The Inverse of a Finite Relation
Let A = {2, 3, 4} and B = {2, 6, 8} and let R be the "divides" relation from A to B: For all (x, y) ∈ A × B,
```
x R y ⇔ x | y ⇔ x divides y.
```

a. State explicitly which ordered pairs are in R and R⁻¹, and draw arrow diagrams for R and R⁻¹.
b. Describe R⁻¹ in words.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {2, 3, 4} and B = {2, 6, 8}. Define the divides relation R from A to B where for all x in A and y in B, x R y ⇔ x divides y. Then state the ordered pairs in R and its inverse R^{-1}, draw arrow diagrams for both, and describe R^{-1} in words.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing two, three, four and B equals the set containing two, six, eight. Define the divides relation R from A to B where for all x in A and y in B, x R y if and only if x divides y. Then state the ordered pairs in R and its inverse R to the power of negative one, draw arrow diagrams for both, and describe R to the power of negative one in words."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {2, 3, 4}":** We're defining set A with three elements.
  - **"B = {2, 6, 8}":** We're defining set B with three elements.
  - **"Define the divides relation R":** We're creating a relationship based on divisibility.
  - **"from A to B":** The relation connects elements of A to elements of B.
  - **"where for all x in A and y in B":** x is from A, y is from B.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"x divides y":** x is a divisor of y (y is divisible by x).
  - **"Then state the ordered pairs in R":** List all pairs (x, y) where x divides y.
  - **"and its inverse R^{-1}":** The "reverse" relation where we swap the order.
  - **"draw arrow diagrams":** Create visual representations showing connections.
  - **"and describe R^{-1} in words":** Explain the inverse relation in plain language.
- **Putting it all together in plain English:** This defines a divisibility relationship between two sets, asks us to find all such pairs and their reverses, draw pictures, and explain the reverse relationship.
- **Why do we use this fancy notation?** It gives us a precise way to express divisibility and work with inverse relations.
- **Assumptions and considerations:** We need to understand divisibility and inverse relations. The thought process is: Check each possible pair for divisibility, then reverse the pairs.
- **How it works:** This gives us the formal approach to working with divisibility relations and their inverses.

### Example 8.1.5: The Inverse of an Infinite Relation
Define a relation R from R to R as follows: For all (x, y) ∈ R × R,
```
x R y ⇔ y = 2|x|.
```

Draw the graphs of R and R⁻¹ in the Cartesian plane. Is R⁻¹ a function?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation R from ℝ to ℝ where for all real numbers x and y, x R y ⇔ y = 2 times the absolute value of x. Then draw the graphs of R and its inverse R^{-1} in the Cartesian plane and determine if R^{-1} is a function.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation R from real numbers to real numbers where for all real numbers x and y, x R y if and only if y equals two times the absolute value of x. Then draw the graphs of R and its inverse R to the power of negative one in the Cartesian plane and determine if R to the power of negative one is a function."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation R":** We're creating a relationship called R.
  - **"from ℝ to ℝ":** Between real numbers.
  - **"where for all real numbers x and y":** Any real numbers.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"y = 2 times the absolute value of x":** y equals twice the distance of x from zero.
  - **"Then draw the graphs":** Create visual plots.
  - **"of R and its inverse R^{-1}":** Plot both the original and reversed relationships.
  - **"in the Cartesian plane":** On the coordinate plane (x-y graph).
  - **"and determine if R^{-1} is a function":** Check if the reverse relation qualifies as a function.
- **Putting it all together in plain English:** This defines a relationship based on absolute value and asks us to plot it and its reverse, then determine if the reverse is a function.
- **Why do we use this fancy notation?** It gives us a precise way to express absolute value relationships and investigate their inverses.
- **Assumptions and considerations:** We need to understand absolute values, functions, and inverse relations. The thought process is: Understand the original relationship, then swap x and y to find the inverse.
- **How it works:** This gives us the formal approach to working with absolute value relations and their inverses.

### Example 8.1.6: Directed Graph of a Relation
Let A = {3, 4, 5, 6, 7, 8} and define a relation R on A as follows: For all x, y ∈ A,
```
x R y ⇔ 2 | (x − y).
```

Draw the directed graph of R.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {3, 4, 5, 6, 7, 8}. Define a relation R on A where for all x, y in A, x R y ⇔ 2 divides (x − y). Then draw the directed graph of R.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing three, four, five, six, seven, eight. Define a relation R on A where for all x, y in A, x R y if and only if two divides the quantity x minus y. Then draw the directed graph of R."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {3, 4, 5, 6, 7, 8}":** We're defining a set A with six consecutive integers.
  - **"Define a relation R on A":** We're creating a relationship within this set.
  - **"where for all x, y in A":** x and y are elements of this set.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"2 divides (x − y)":** 2 is a divisor of (x minus y).
  - **"Then draw the directed graph of R":** Create a visual diagram with arrows showing the connections.
- **Putting it all together in plain English:** This defines a relationship based on divisibility by 2 within a set of numbers, then asks us to create a visual diagram showing all the connections.
- **Why do we use this fancy notation?** It gives us a precise way to express divisibility relationships and visualize them as a graph.
- **Assumptions and considerations:** We need to understand divisibility and directed graphs. The thought process is: Check every pair of numbers to see if their difference is divisible by 2, then draw arrows accordingly.
- **How it works:** This gives us the formal approach to creating directed graphs for divisibility relations.

### Example 8.1.7: A Simple Database
The following is a radically simplified version of a database that might be used in a hospital. Let A₁ be a set of positive integers, A₂ a set of alphabetic character strings, A₃ a set of numeric character strings, and A₄ a set of alphabetic character strings. Define a quaternary relation R on A₁ × A₂ × A₃ × A₄ as follows:
```
(a₁, a₂, a₃, a₄) ∈ R ⇔ a patient with patient ID number a₁, named a₂, was admitted on date a₃, with primary diagnosis a₄.
```

At a particular hospital, this relation might contain the following 4-tuples:
- (011985, John Schmidt, 020710, asthma)
- (574329, Tak Kurosawa, 0114910, pneumonia)
- (466581, Mary Lazars, 0103910, appendicitis)
- (008352, Joan Kaplan, 112409, gastritis)
- (011985, John Schmidt, 021710, pneumonia)
- (244388, Sarah Wu, 010310, broken leg)
- (778400, Jamal Baskers, 122709, appendicitis)

In discussions of relational databases, the tuples are normally thought of as being written in tables. Each row of the table corresponds to one tuple, and the header for each column gives the descriptive attribute for the elements in the column.

Operations within a database allow the data to be manipulated in many different ways. For example, in the database language SQL, if the above database is denoted S, the result of the query:
```
SELECT Patient−ID#, Name FROM S WHERE Admission−Date = 010310
```

would be a list of the ID numbers and names of all patients admitted on 01-03-10:
- 466581, Mary Lazars
- 244388, Sarah Wu

This is obtained by taking the intersection of the set A₁ × A₂ × {010310} × A₄ with the database and then projecting onto the first two coordinates. Similarly, SELECT can be used to obtain a list of all admission dates of a given patient. For John Schmidt this list is 02-07-10 and 02-17-10.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Understand how a quaternary relation R on A₁ × A₂ × A₃ × A₄ represents hospital patient data where (a₁, a₂, a₃, a₄) ∈ R means patient with ID a₁ named a₂ admitted on date a₃ with diagnosis a₄, and understand how SQL queries extract information from this relational database.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Understand how a quaternary relation R on A one cross A two cross A three cross A four represents hospital patient data where a one, a two, a three, a four in R means patient with ID a one named a two admitted on date a three with diagnosis a four, and understand how SQL queries extract information from this relational database."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Understand how a quaternary relation R":** We're learning about a 4-part relationship.
  - **"on A₁ × A₂ × A₃ × A₄":** "×" means "cross" or "Cartesian product" - combining four sets.
  - **"represents hospital patient data":** This is about storing patient information in a database.
  - **"where (a₁, a₂, a₃, a₄) ∈ R":** The notation for a record in the database.
  - **"means patient with ID a₁ named a₂":** Each component represents a piece of information.
  - **"admitted on date a₃ with diagnosis a₄":** The complete patient record.
  - **"and understand how SQL queries":** Learn about asking questions of the database.
  - **"extract information from this relational database":** How to get specific data out.
- **Putting it all together in plain English:** This is explaining how hospitals store patient information using mathematical relations and how we can ask specific questions to get particular information from that data.
- **Why do we use this fancy notation?** It gives us a precise mathematical way to model database relationships and understand how real-world data systems work.
- **Assumptions and considerations:** We need to understand databases and data retrieval. The thought process is: Each row is a complete patient record, and we can filter and select specific information.
- **How it works:** This gives us the formal mathematical foundation for understanding relational databases.

## Chapter 8.2 Examples

### Example 8.2.1: Properties of Relations on Finite Sets
Let A = {0, 1, 2, 3} and define relations R, S, and T on A as follows:
```
R = {(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)},
S = {(0, 0), (0, 2), (0, 3), (2, 3)},
T = {(0, 1), (2, 3)}.
```

a. Is R reflexive? symmetric? transitive?
b. Is S reflexive? symmetric? transitive?
c. Is T reflexive? symmetric? transitive?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {0, 1, 2, 3}. Define relations R, S, T on A. Determine if R is reflexive, symmetric, and transitive; if S is reflexive, symmetric, and transitive; and if T is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing zero, one, two, three. Define relations R, S, T on A. Determine if R is reflexive, symmetric, and transitive; if S is reflexive, symmetric, and transitive; and if T is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {0, 1, 2, 3}":** We're defining a set with four elements.
  - **"Define relations R, S, T on A":** We're creating three different relationships on this set.
  - **"Determine if R is reflexive, symmetric, and transitive":** Check if R has these three properties.
  - **"reflexive":** Every element is related to itself.
  - **"symmetric":** If x is related to y, then y is related to x.
  - **"transitive":** If x is related to y and y to z, then x is related to z.
  - **"S is reflexive, symmetric, and transitive":** Same checks for S.
  - **"T is reflexive, symmetric, and transitive":** Same checks for T.
- **Putting it all together in plain English:** This is asking us to check three different relationships for three specific mathematical properties.
- **Why do we use this fancy notation?** It gives us a precise way to analyze the fundamental properties of relationships between elements.
- **Assumptions and considerations:** We need to understand the definitions of reflexive, symmetric, and transitive. The thought process is: Check each property systematically for each relation.
- **How it works:** This gives us the formal approach to analyzing relation properties.

### Example 8.2.2: Properties of Equality
Define a relation R on R (the set of all real numbers) as follows: For all real numbers x and y,
```
x R y ⇔ x = y.
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation R on ℝ where for all real numbers x and y, x R y ⇔ x = y. Then determine if R is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation R on real numbers where for all real numbers x and y, x R y if and only if x equals y. Then determine if R is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation R on ℝ":** We're creating a relationship called R between real numbers.
  - **"where for all real numbers x and y":** Any real numbers.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"x = y":** x equals y (they're the same number).
  - **"Then determine if R is reflexive, symmetric, and transitive":** Check if equality has these three properties.
- **Putting it all together in plain English:** This is asking us to check if the basic "equals" relationship has the three fundamental mathematical properties.
- **Why do we use this fancy notation?** It gives us a precise way to analyze the most basic mathematical relationship - equality.
- **Assumptions and considerations:** We need to understand that equality means two things are identical. The thought process is: Check if equal things are equal to themselves, if equality works both ways, and if chains of equality work.
- **How it works:** This gives us the formal approach to analyzing the equality relation.

### Example 8.2.3: Properties of "Less Than"
Define a relation R on R (the set of all real numbers) as follows: For all x, y ∈ R,
```
x R y ⇔ x < y.
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation R on ℝ where for all real numbers x and y, x R y ⇔ x < y. Then determine if R is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation R on real numbers where for all real numbers x and y, x R y if and only if x is less than y. Then determine if R is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation R on ℝ":** We're creating a relationship called R between real numbers.
  - **"where for all real numbers x and y":** Any real numbers.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"x < y":** x is less than y.
  - **"Then determine if R is reflexive, symmetric, and transitive":** Check if "less than" has these three properties.
- **Putting it all together in plain English:** This is asking us to check if the "less than" relationship has the three fundamental mathematical properties.
- **Why do we use this fancy notation?** It gives us a precise way to analyze ordering relationships and understand why they don't have all the same properties as equality.
- **Assumptions and considerations:** We need to understand strict inequality. The thought process is: Check if numbers are less than themselves, if "less than" works both ways, and if chains of inequalities work.
- **How it works:** This gives us the formal approach to analyzing ordering relations.

### Example 8.2.4: Properties of Congruence Modulo 3
Define a relation T on Z (the set of all integers) as follows: For all integers m and n,
```
m T n ⇔ 3 | (m − n).
```

This relation is called congruence modulo 3.

a. Is T reflexive?
b. Is T symmetric?
c. Is T transitive?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Define a relation T on ℤ where for all integers m and n, m T n ⇔ 3 divides (m − n). This is called congruence modulo 3. Then determine if T is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Define a relation T on integers where for all integers m and n, m T n if and only if three divides m minus n. This is called congruence modulo three. Then determine if T is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Define a relation T on ℤ":** We're creating a relationship called T between integers.
  - **"where for all integers m and n":** Any integers.
  - **"m T n":** The relation notation.
  - **"⇔":** "if and only if."
  - **"3 divides (m − n)":** 3 is a divisor of (m minus n).
  - **"This is called congruence modulo 3":** This is the name for this type of relationship.
  - **"Then determine if T is reflexive, symmetric, and transitive":** Check if this divisibility relationship has the three properties.
- **Putting it all together in plain English:** This defines a relationship based on divisibility by 3 and asks us to check if it has the three fundamental mathematical properties.
- **Why do we use this fancy notation?** It gives us a precise way to express modular arithmetic relationships and understand their properties.
- **Assumptions and considerations:** We need to understand divisibility by 3. The thought process is: Check if numbers are congruent to themselves modulo 3, if the relationship works both ways, and if chains of congruences work.
- **How it works:** This gives us the formal approach to analyzing congruence relations.

### Example 8.2.5: Transitive Closure of a Relation
Let A = {0, 1, 2, 3} and consider the relation R defined on A as follows:
```
R = {(0, 1), (1, 2), (2, 3)}.
```

Find the transitive closure of R.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {0, 1, 2, 3}. Consider the relation R on A defined by R = {(0, 1), (1, 2), (2, 3)}. Then find the transitive closure of R.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing zero, one, two, three. Consider the relation R on A defined by R equals the set containing the ordered pairs zero one, one two, two three. Then find the transitive closure of R."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {0, 1, 2, 3}":** We're defining a set with four elements.
  - **"Consider the relation R on A":** We're looking at a relationship within this set.
  - **"defined by R = {(0, 1), (1, 2), (2, 3)}":** The relation contains three ordered pairs: 0→1, 1→2, 2→3.
  - **"Then find the transitive closure of R":** Find the smallest extension that includes all indirect connections.
- **Putting it all together in plain English:** This is asking us to extend a chain of connections (0→1→2→3) to include all the indirect connections (0→2, 0→3, 1→3).
- **Why do we use this fancy notation?** It gives us a precise way to express the concept of "reachable through a chain of connections."
- **Assumptions and considerations:** We need to understand transitivity and indirect connections. The thought process is: Start with given connections, add all connections that follow from chains of existing connections.
- **How it works:** This gives us the formal approach to finding the transitive closure of a relation.

### Example 8.2.5: Transitive Closure of a Relation
Let A = {0, 1, 2, 3} and consider the relation R defined on A as follows:
```
R = {(0, 1), (1, 2), (2, 3)}.
```

Find the transitive closure of R.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {0, 1, 2, 3}. Consider the relation R on A defined by R = {(0, 1), (1, 2), (2, 3)}. Then find the transitive closure of R.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing zero, one, two, three. Consider the relation R on A defined by R equals the set containing the ordered pairs zero one, one two, two three. Then find the transitive closure of R."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {0, 1, 2, 3}":** We're defining a set with four elements.
  - **"Consider the relation R on A":** We're looking at a relationship within this set.
  - **"defined by R = {(0, 1), (1, 2), (2, 3)}":** The relation contains three ordered pairs: 0→1, 1→2, 2→3.
  - **"Then find the transitive closure of R":** Find the smallest extension that includes all indirect connections.
- **Putting it all together in plain English:** This is asking us to extend a chain of connections (0→1→2→3) to include all the indirect connections (0→2, 0→3, 1→3).
- **Why do we use this fancy notation?** It gives us a precise way to express the concept of "reachable through a chain of connections."
- **Assumptions and considerations:** We need to understand transitivity and indirect connections. The thought process is: Start with given connections, add all connections that follow from chains of existing connections.
- **How it works:** This gives us the formal approach to finding the transitive closure of a relation.

### Example 8.3.1: An Equivalence Relation on a Finite Set
Let A = {0, 1, 2, 3, 4} and define a relation R on A as follows:
```
For all x, y ∈ A, x R y ⇔ 4 | (x² - y²).
```

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?
d. Is R an equivalence relation?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {0, 1, 2, 3, 4}. Define a relation R on A where for all x, y in A, x R y ⇔ 4 divides (x squared minus y squared). Then determine if R is reflexive, symmetric, transitive, and thus an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing zero, one, two, three, four. Define a relation R on A where for all x, y in A, x R y if and only if four divides the quantity x squared minus y squared. Then determine if R is reflexive, symmetric, transitive, and thus an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {0, 1, 2, 3, 4}":** We're defining a set with five elements.
  - **"Define a relation R on A":** We're creating a relationship within this set.
  - **"where for all x, y in A":** x and y are elements of this set.
  - **"x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"4 divides (x² - y²)":** 4 is a divisor of (x squared minus y squared).
  - **"Then determine if R is reflexive, symmetric, transitive":** Check if this relationship has the three properties.
  - **"and thus an equivalence relation":** If it has all three properties, it's an equivalence relation.
- **Putting it all together in plain English:** This defines a relationship based on divisibility of differences of squares and asks us to check if it has the three fundamental properties that make it an equivalence relation.
- **Why do we use this fancy notation?** It gives us a precise way to express relationships between numbers based on divisibility of differences of squares.
- **Assumptions and considerations:** We need to understand the difference of squares formula and divisibility. The thought process is: Factor the difference of squares and check if 4 divides it.
- **How it works:** This gives us the formal approach to analyzing equivalence relations defined by divisibility conditions.

### Example 8.3.2: The Relation Induced by a Partition
Let A = {0, 1, 2, 3, 4, 5} and consider the partition P = {{0, 3, 4}, {1, 2}, {5}} of A. Define a relation R on A as follows:

For all x, y ∈ A, x R y if and only if x and y are in the same element of P.

a. Is R reflexive?
b. Is R symmetric?
c. Is R transitive?
d. Is R an equivalence relation?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let A = {0, 1, 2, 3, 4, 5} and consider the partition P = {{0, 3, 4}, {1, 2}, {5}} of A. Define a relation R on A where for all x, y in A, x R y if and only if x and y are in the same element of P. Then determine if R is reflexive, symmetric, transitive, and thus an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let A equals the set containing zero, one, two, three, four, five and consider the partition P equals the set of sets zero three four, one two, five of A. Define a relation R on A where for all x, y in A, x R y if and only if x and y are in the same element of P. Then determine if R is reflexive, symmetric, transitive, and thus an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let A = {0, 1, 2, 3, 4, 5}":** We're defining a set with six elements.
  - **"consider the partition P":** We're looking at a way of dividing this set into groups.
  - **"{{0, 3, 4}, {1, 2}, {5}}":** The groups are: {0,3,4}, {1,2}, and {5} alone.
  - **"of A":** This partition divides the set A.
  - **"Define a relation R on A":** We're creating a relationship based on these groups.
  - **"where for all x, y in A":** x and y are elements of A.
  - **"x R y if and only if x and y are in the same element of P":** x is related to y if they're in the same group.
  - **"Then determine if R is reflexive, symmetric, transitive":** Check if this grouping relationship has the three properties.
  - **"and thus an equivalence relation":** If it has all three, it's an equivalence relation.
- **Putting it all together in plain English:** This defines a relationship where elements are related if they're in the same partition group, and asks us to check if this has the three fundamental properties of an equivalence relation.
- **Why do we use this fancy notation?** It gives us a precise way to express relationships between elements based on how they're grouped in a partition.
- **Assumptions and considerations:** We need to understand partitions and set membership. The thought process is: Elements are related if they're in the same group, and we need to check if this satisfies the equivalence properties.
- **How it works:** This gives us the formal approach to understanding how partitions induce equivalence relations.

### Example 8.3.3: Equivalence Classes of the Congruence Modulo 3 Relation
Consider the congruence modulo 3 relation T on Z defined by:
```
m T n ⇔ 3 | (m - n)
```

The equivalence classes are:
- [0] = {..., -6, -3, 0, 3, 6, ...}
- [1] = {..., -5, -2, 1, 4, 7, ...}
- [2] = {..., -4, -1, 2, 5, 8, ...}

These three equivalence classes form a partition of Z.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the congruence modulo 3 relation T on ℤ defined by m T n ⇔ 3 divides (m − n). The equivalence classes are [0] equals the set of dots dots dots negative six negative three zero three six dots dots dots, [1] equals the set of dots dots dots negative five negative two one four seven dots dots dots, [2] equals the set of dots dots dots negative four negative one two five eight dots dots dots. These three equivalence classes form a partition of ℤ.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the congruence modulo three relation T on integers defined by m T n if and only if three divides m minus n. The equivalence classes are bracket zero equals the set of dots dots dots negative six negative three zero three six dots dots dots, bracket one equals the set of dots dots dots negative five negative two one four seven dots dots dots, bracket two equals the set of dots dots dots negative four negative one two five eight dots dots dots. These three equivalence classes form a partition of integers."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the congruence modulo 3 relation T":** We're looking at the "differs by multiple of 3" relationship.
  - **"on ℤ":** On the integers.
  - **"defined by m T n":** The relation notation.
  - **"⇔":** "if and only if."
  - **"3 divides (m − n)":** 3 is a divisor of (m minus n).
  - **"The equivalence classes are":** The groups of numbers that are all related to each other.
  - **"[0] = {..., -6, -3, 0, 3, 6, ...}":** The group containing multiples of 3.
  - **"[1] = {..., -5, -2, 1, 4, 7, ...}":** The group containing numbers that leave remainder 1 when divided by 3.
  - **"[2] = {..., -4, -1, 2, 5, 8, ...}":** The group containing numbers that leave remainder 2 when divided by 3.
  - **"These three equivalence classes form a partition of ℤ":** These groups cover all integers without overlap.
- **Putting it all together in plain English:** This shows the three groups of integers where each number in a group differs from others by multiples of 3, and together they cover all integers exactly once.
- **Why do we use this fancy notation?** It gives us a precise way to express the grouping of integers by remainders when divided by 3.
- **Assumptions and considerations:** We need to understand remainders when dividing by 3. The thought process is: Numbers with the same remainder when divided by 3 are in the same class.
- **How it works:** This gives us the formal approach to understanding equivalence classes in modular arithmetic.

### Example 8.3.4: The Equivalence Relation of Congruence Modulo n
For any integer n ≥ 2, the relation of congruence modulo n is defined as:
```
a ≡ b (mod n) ⇔ n | (a - b)
```

This relation is an equivalence relation on Z, and the equivalence classes are:
```
[r] = {..., r - 2n, r - n, r, r + n, r + 2n, ...}
```
where r ∈ {0, 1, 2, ..., n-1}.

The set of equivalence classes is denoted Z_n and has n elements:
```
Z_n = {[0], [1], [2], ..., [n-1]}
```

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For any integer n greater than or equal to 2, the relation of congruence modulo n is defined as a congruent to b modulo n if and only if n divides a minus b. This relation is an equivalence relation on ℤ, and the equivalence classes are bracket r equals the set of dots dots dots r minus two n, r minus n, r, r plus n, r plus two n dots dots dots where r is in the set zero one two dots dots dots n minus one. The set of equivalence classes is denoted ℤ sub n and has n elements ℤ sub n equals bracket zero bracket one bracket two dots dots dots bracket n minus one.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For any integer n greater than or equal to two, the relation of congruence modulo n is defined as a congruent to b modulo n if and only if n divides a minus b. This relation is an equivalence relation on integers, and the equivalence classes are bracket r equals the set of dots dots dots r minus two n, r minus n, r, r plus n, r plus two n dots dots dots where r is in the set zero one two dots dots dots n minus one. The set of equivalence classes is denoted integers sub n and has n elements integers sub n equals bracket zero bracket one bracket two dots dots dots bracket n minus one."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For any integer n ≥ 2":** For any integer n that is 2 or bigger.
  - **"the relation of congruence modulo n":** The relationship "differs by multiple of n."
  - **"is defined as a ≡ b (mod n)":** The notation for congruence.
  - **"⇔":** "if and only if."
  - **"n | (a - b)":** n divides (a minus b).
  - **"This relation is an equivalence relation on ℤ":** This relationship has the three required properties on integers.
  - **"the equivalence classes are [r]":** The groups are labeled by r.
  - **"{..., r - 2n, r - n, r, r + n, r + 2n, ...}":** The arithmetic sequence centered at r.
  - **"where r ∈ {0, 1, 2, ..., n-1}":** r ranges from 0 to n-1.
  - **"The set of equivalence classes is denoted ℤ_n":** We call this set ℤ_n.
  - **"and has n elements":** There are exactly n groups.
  - **"ℤ_n = {[0], [1], [2], ..., [n-1]}":** The n different groups.
- **Putting it all together in plain English:** This is the general definition of modular arithmetic, showing how dividing by n creates n different groups of integers, where each group contains numbers that leave the same remainder when divided by n.
- **Why do we use this fancy notation?** It gives us a precise way to express modular arithmetic, which is fundamental to many areas of mathematics and computer science.
- **Assumptions and considerations:** We need to understand remainders when dividing by n. The thought process is: Numbers with the same remainder when divided by n are congruent modulo n.
- **How it works:** This gives us the formal approach to understanding modular arithmetic and quotient sets.

### Example 8.3.5: Rational Numbers as Equivalence Classes
The set of rational numbers Q can be defined as equivalence classes of ordered pairs of integers. Define a relation ∼ on Z × (Z - {0}) as follows:
```
(a, b) ∼ (c, d) ⇔ ad = bc
```

This is an equivalence relation, and the equivalence class of (a, b) is:
```
[(a, b)] = {(c, d) ∈ Z × (Z - {0}) | ad = bc}
```

The rational number a/b is defined as the equivalence class [(a, b)].

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: The set of rational numbers ℚ can be defined as equivalence classes of ordered pairs of integers. Define a relation tilde on ℤ cross the set of integers minus zero as follows a comma b tilde c comma d if and only if a d equals b c. This is an equivalence relation, and the equivalence class of a comma b is bracket a comma b equals the set of c comma d in ℤ cross the set of integers minus zero such that a d equals b c. The rational number a over b is defined as the equivalence class bracket a comma b.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: The set of rational numbers Q can be defined as equivalence classes of ordered pairs of integers. Define a relation tilde on integers cross integers minus zero as follows a comma b tilde c comma d if and only if a d equals b c. This is an equivalence relation, and the equivalence class of a comma b is bracket a comma b equals the set of c comma d in integers cross integers minus zero such that a d equals b c. The rational number a over b is defined as the equivalence class bracket a comma b."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"The set of rational numbers ℚ":** We're talking about fractions like 1/2, 3/4, etc.
  - **"can be defined as equivalence classes":** We can think of them as groups of equivalent pairs.
  - **"of ordered pairs of integers":** Each fraction is represented by a pair (numerator, denominator).
  - **"Define a relation ∼":** We're creating a relationship between these pairs.
  - **"on ℤ × (ℤ - {0})":** Between pairs where the second number isn't zero.
  - **"as follows: (a, b) ∼ (c, d)":** The relation notation.
  - **"⇔":** "if and only if."
  - **"ad = bc":** The cross multiplication condition for equivalent fractions.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"the equivalence class of (a, b) is [(a, b)]":** The group containing all equivalent pairs.
  - **"The rational number a/b":** The fraction itself.
  - **"is defined as the equivalence class [(a, b)]":** Each fraction is the group of all equivalent ways to write it.
- **Putting it all together in plain English:** This is explaining how we can build rational numbers from integer pairs, where (2,3) and (4,6) represent the same rational number because 2×6 = 3×4.
- **Why do we use this fancy notation?** It gives us a precise way to define rational numbers without assuming we already know what they are, building them up from integers.
- **Assumptions and considerations:** We need to understand equivalent fractions. The thought process is: Different ways of writing the same fraction are equivalent.
- **How it works:** This gives us the formal mathematical foundation for rational numbers.


### Example 8.3.6: Equivalence Classes of Functions
Let F be the set of all functions from R to R. Define a relation R on F as follows:
```
f R g ⇔ f - g is a constant function
```

This is an equivalence relation where:
- f R f because f - f = 0 is constant
- If f R g, then f - g = c (constant), so g - f = -c is constant, hence g R f
- If f R g and g R h, then f - g = c₁ and g - h = c₂, so f - h = (f - g) + (g - h) = c₁ + c₂ is constant, hence f R h

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let F be the set of all functions from ℝ to ℝ. Define a relation R on F where f R g ⇔ f minus g is a constant function. This is an equivalence relation where f R f because f minus f equals zero is constant; if f R g, then f minus g equals c constant, so g minus f equals negative c is constant, hence g R f; if f R g and g R h, then f minus g equals c sub one and g minus h equals c sub two, so f minus h equals f minus g plus g minus h equals c sub one plus c sub two is constant, hence f R h.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let F be the set of all functions from real numbers to real numbers. Define a relation R on F where f R g if and only if f minus g is a constant function. This is an equivalence relation where f R f because f minus f equals zero is constant; if f R g, then f minus g equals c constant, so g minus f equals negative c is constant, hence g R f; if f R g and g R h, then f minus g equals c sub one and g minus h equals c sub two, so f minus h equals f minus g plus g minus h equals c sub one plus c sub two is constant, hence f R h."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let F be the set of all functions from ℝ to ℝ":** We're working with all possible functions that take real numbers and give real numbers.
  - **"Define a relation R on F":** We're creating a relationship between functions.
  - **"where f R g":** The relation notation.
  - **"⇔":** "if and only if."
  - **"f - g is a constant function":** The difference between the two functions is always the same value.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"where f R f because f - f = 0 is constant":** Every function is related to itself because f - f = 0, which is constant.
  - **"if f R g, then f - g = c (constant)":** If f is related to g, their difference is constant.
  - **"so g - f = -c is constant":** Then the reverse difference is also constant.
  - **"hence g R f":** So the relation works both ways.
  - **"if f R g and g R h":** If f is related to g and g is related to h.
  - **"then f - g = c₁ and g - h = c₂":** Their differences are constants.
  - **"so f - h = (f - g) + (g - h) = c₁ + c₂ is constant":** The combined difference is also constant.
  - **"hence f R h":** So the relation follows through chains.
- **Putting it all together in plain English:** This defines a relationship where functions are equivalent if they differ by a constant amount everywhere, and shows this satisfies the three equivalence relation properties.
- **Why do we use this fancy notation?** It gives us a precise way to express when two functions are essentially the same except for a vertical shift.
- **Assumptions and considerations:** We need to understand function operations and constant functions. The thought process is: Functions that differ by a constant are in the same equivalence class.
- **How it works:** This gives us the formal approach to classifying functions by their vertical separation.

### Example 8.3.7: Equivalence Classes in Geometry
Consider the set of all triangles in the plane. Define a relation R as follows:
```
△ABC R △DEF ⇔ △ABC is congruent to △DEF
```

This is an equivalence relation where triangles are equivalent if they have the same size and shape. The equivalence classes consist of all triangles that are congruent to each other.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the set of all triangles in the plane. Define a relation R where triangle ABC R triangle DEF if and only if triangle ABC is congruent to triangle DEF. This is an equivalence relation where triangles are equivalent if they have the same size and shape. The equivalence classes consist of all triangles that are congruent to each other.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the set of all triangles in the plane. Define a relation R where triangle ABC R triangle DEF if and only if triangle ABC is congruent to triangle DEF. This is an equivalence relation where triangles are equivalent if they have the same size and shape. The equivalence classes consist of all triangles that are congruent to each other."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the set of all triangles in the plane":** We're working with all possible triangles that can be drawn.
  - **"Define a relation R":** We're creating a relationship between triangles.
  - **"where △ABC R △DEF":** The notation for triangles being related.
  - **"⇔":** "if and only if."
  - **"△ABC is congruent to △DEF":** The triangles have the same size and shape.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"where triangles are equivalent if they have the same size and shape":** The meaning of the relation.
  - **"The equivalence classes consist of":** The groups contain.
  - **"all triangles that are congruent to each other":** All triangles that are the same in size and shape.
- **Putting it all together in plain English:** This defines a relationship where triangles with the same size and shape are equivalent, and shows this forms a valid equivalence relation.
- **Why do we use this fancy notation?** It gives us a precise way to classify geometric shapes by their essential properties.
- **Assumptions and considerations:** We need to understand triangle congruence. The thought process is: Triangles that can be matched exactly by size and shape are in the same class.
- **How it works:** This gives us the formal approach to classifying geometric objects by their congruence.

### Example 8.3.8: Equivalence Classes in Linear Algebra
Let V be a vector space and W a subspace of V. Define a relation ∼ on V as follows:
```
v ∼ w ⇔ v - w ∈ W
```

This is an equivalence relation, and the equivalence classes are the cosets of W in V. The set of equivalence classes forms the quotient space V/W.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let V be a vector space and W a subspace of V. Define a relation tilde on V where v tilde w if and only if v minus w is in W. This is an equivalence relation, and the equivalence classes are the cosets of W in V. The set of equivalence classes forms the quotient space V slash W.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let V be a vector space and W a subspace of V. Define a relation tilde on V where v tilde w if and only if v minus w is in W. This is an equivalence relation, and the equivalence classes are the cosets of W in V. The set of equivalence classes forms the quotient space V slash W."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let V be a vector space":** We're working with a mathematical space of vectors.
  - **"W a subspace of V":** W is a smaller space inside V.
  - **"Define a relation ∼ on V":** We're creating a relationship between vectors in V.
  - **"where v ∼ w":** The relation notation.
  - **"⇔":** "if and only if."
  - **"v - w ∈ W":** The difference between the vectors is in the subspace W.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"the equivalence classes are the cosets of W in V":** The groups are the cosets.
  - **"The set of equivalence classes forms the quotient space V/W":** The resulting structure is the quotient space.
- **Putting it all together in plain English:** This defines a relationship where vectors are equivalent if their difference is in a subspace, creating the mathematical structure of a quotient space.
- **Why do we use this fancy notation?** It gives us a precise way to express the concept of quotient spaces in linear algebra.
- **Assumptions and considerations:** We need to understand vector spaces and subspaces. The thought process is: Vectors that differ by an element of W are in the same coset.
- **How it works:** This gives us the formal approach to understanding quotient spaces in linear algebra.

### Example 8.3.9: Equivalence Classes of Binary Relations
Consider the set of all binary relations on a set A. Define a relation R as follows:
```
R₁ R R₂ ⇔ R₁ and R₂ have the same reflexive closure
```

This is an equivalence relation where two relations are equivalent if adding all necessary self-loops results in the same relation.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the set of all binary relations on a set A. Define a relation R where R sub one R R sub two if and only if R sub one and R sub two have the same reflexive closure. This is an equivalence relation where two relations are equivalent if adding all necessary self-loops results in the same relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the set of all binary relations on a set A. Define a relation R where R sub one R R sub two if and only if R sub one and R sub two have the same reflexive closure. This is an equivalence relation where two relations are equivalent if adding all necessary self-loops results in the same relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the set of all binary relations on a set A":** We're working with all possible relationships on a set.
  - **"Define a relation R":** We're creating a relationship between these relations.
  - **"where R₁ R R₂":** The notation for relations being related.
  - **"⇔":** "if and only if."
  - **"R₁ and R₂ have the same reflexive closure":** They become the same when we add all necessary self-connections.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"where two relations are equivalent":** The meaning of the relation.
  - **"if adding all necessary self-loops results in the same relation":** When we make them reflexive in the same way.
- **Putting it all together in plain English:** This defines a relationship between binary relations based on what they become when we add self-loops to make them reflexive.
- **Why do we use this fancy notation?** It gives us a precise way to classify binary relations by their "reflexive completion."
- **Assumptions and considerations:** We need to understand reflexive closures of relations. The thought process is: Relations that require the same self-loops to become reflexive are in the same class.
- **How it works:** This gives us the formal approach to classifying relations by their reflexive properties.

### Example 8.3.10: Equivalence Classes in Logic
Consider the set of all propositional formulas. Define a relation R as follows:
```
φ R ψ ⇔ φ ↔ ψ is a tautology
```

This is an equivalence relation where two formulas are equivalent if they are logically equivalent. The equivalence classes consist of all formulas that are logically equivalent to each other.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the set of all propositional formulas. Define a relation R where phi R psi if and only if phi if and only if psi is a tautology. This is an equivalence relation where two formulas are equivalent if they are logically equivalent. The equivalence classes consist of all formulas that are logically equivalent to each other.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the set of all propositional formulas. Define a relation R where phi R psi if and only if phi if and only if psi is a tautology. This is an equivalence relation where two formulas are equivalent if they are logically equivalent. The equivalence classes consist of all formulas that are logically equivalent to each other."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the set of all propositional formulas":** We're working with logical statements.
  - **"Define a relation R":** We're creating a relationship between formulas.
  - **"where φ R ψ":** The relation notation.
  - **"⇔":** "if and only if."
  - **"φ ↔ ψ is a tautology":** The statement "φ if and only if ψ" is always true.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"where two formulas are equivalent":** The meaning of the relation.
  - **"if they are logically equivalent":** They have the same truth values in all situations.
  - **"The equivalence classes consist of":** The groups contain.
  - **"all formulas that are logically equivalent to each other":** All formulas that always have the same truth values.
- **Putting it all together in plain English:** This defines a relationship where logical formulas are equivalent if they always have the same truth values, and shows this forms a valid equivalence relation.
- **Why do we use this fancy notation?** It gives us a precise way to express logical equivalence between formulas.
- **Assumptions and considerations:** We need to understand logical equivalence and tautologies. The thought process is: Formulas that are always true or false together are in the same class.
- **How it works:** This gives us the formal approach to classifying logical formulas by their truth values.

### Example 8.3.11: Equivalence Classes in Topology
Consider the set of all continuous functions from [0,1] to R. Define a relation R as follows:
```
f R g ⇔ f(0) = g(0) and f(1) = g(1)
```

This is an equivalence relation where two functions are equivalent if they agree at the endpoints of the interval. The equivalence classes consist of all functions with the same boundary values.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the set of all continuous functions from the interval zero one to ℝ. Define a relation R where f R g if and only if f of zero equals g of zero and f of one equals g of one. This is an equivalence relation where two functions are equivalent if they agree at the endpoints of the interval. The equivalence classes consist of all functions with the same boundary values.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the set of all continuous functions from the interval zero one to real numbers. Define a relation R where f R g if and only if f of zero equals g of zero and f of one equals g of one. This is an equivalence relation where two functions are equivalent if they agree at the endpoints of the interval. The equivalence classes consist of all functions with the same boundary values."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the set of all continuous functions":** We're working with functions that are smooth (no jumps).
  - **"from [0,1] to ℝ":** From the interval from 0 to 1 to real numbers.
  - **"Define a relation R":** We're creating a relationship between these functions.
  - **"where f R g":** The relation notation.
  - **"⇔":** "if and only if."
  - **"f(0) = g(0) and f(1) = g(1)":** The functions have the same values at 0 and at 1.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"where two functions are equivalent":** The meaning of the relation.
  - **"if they agree at the endpoints":** They have the same boundary values.
  - **"The equivalence classes consist of":** The groups contain.
  - **"all functions with the same boundary values":** All functions that start and end at the same points.
- **Putting it all together in plain English:** This defines a relationship where continuous functions are equivalent if they have the same values at the start and end of the interval [0,1].
- **Why do we use this fancy notation?** It gives us a precise way to classify functions by their boundary behavior.
- **Assumptions and considerations:** We need to understand continuous functions and function evaluation. The thought process is: Functions with the same boundary values are in the same class.
- **How it works:** This gives us the formal approach to classifying functions by their endpoint values.

### Example 8.3.12: Equivalence Classes in Number Theory
Consider the set Z × Z⁺ (where Z⁺ is the set of positive integers). Define a relation R as follows:
```
(a, b) R (c, d) ⇔ a/b = c/d in the real numbers
```

This is an equivalence relation, and the equivalence classes correspond to rational numbers. This is essentially the same construction as in Example 8.3.5, but phrased differently.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the set ℤ cross ℤ positive where ℤ positive is the set of positive integers. Define a relation R where a comma b R c comma d if and only if a divided by b equals c divided by d in the real numbers. This is an equivalence relation, and the equivalence classes correspond to rational numbers. This is essentially the same construction as in Example eight point three point five, but phrased differently.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the set integers cross positive integers where positive integers is the set of positive integers. Define a relation R where a comma b R c comma d if and only if a divided by b equals c divided by d in the real numbers. This is an equivalence relation, and the equivalence classes correspond to rational numbers. This is essentially the same construction as in Example eight point three point five, but phrased differently."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the set ℤ × ℤ⁺":** We're working with pairs of integers where the second is positive.
  - **"where ℤ⁺ is the set of positive integers":** Positive integers are 1, 2, 3, 4, etc.
  - **"Define a relation R":** We're creating a relationship between these pairs.
  - **"where (a, b) R (c, d)":** The relation notation.
  - **"⇔":** "if and only if."
  - **"a/b = c/d in the real numbers":** The fractions are equal.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"the equivalence classes correspond to rational numbers":** Each group represents a rational number.
  - **"This is essentially the same construction":** It's the same idea.
  - **"as in Example 8.3.5, but phrased differently":** Just presented differently.
- **Putting it all together in plain English:** This is another way to think about rational numbers as groups of equivalent fractions, just like in the earlier example.
- **Why do we use this fancy notation?** It gives us a precise way to construct rational numbers from integer pairs.
- **Assumptions and considerations:** We need to understand equivalent fractions. The thought process is: Pairs that represent the same number are in the same class.
- **How it works:** This gives us the formal mathematical foundation for rational numbers.

### Example 8.3.13: The Quotient Set of Congruence Modulo n
For the equivalence relation of congruence modulo n on Z, the quotient set is:
```
Z/nZ = {[0], [1], [2], ..., [n-1]}
```

This set has exactly n elements, and it forms a ring under appropriate operations.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For the equivalence relation of congruence modulo n on ℤ, the quotient set is integers divided by n integers equals bracket zero bracket one bracket two dots dots dots bracket n minus one. This set has exactly n elements, and it forms a ring under appropriate operations.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the equivalence relation of congruence modulo n on integers, the quotient set is integers divided by n integers equals bracket zero bracket one bracket two dots dots dots bracket n minus one. This set has exactly n elements, and it forms a ring under appropriate operations."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the equivalence relation of congruence modulo n":** For the "differs by multiple of n" relationship.
  - **"on ℤ":** On the integers.
  - **"the quotient set is":** The set of equivalence classes is.
  - **"ℤ/nℤ":** The mathematical notation for this set.
  - **"equals {[0], [1], [2], ..., [n-1]}":** The n different groups.
  - **"This set has exactly n elements":** There are exactly n groups.
  - **"and it forms a ring":** It has algebraic structure.
  - **"under appropriate operations":** With the right mathematical operations.
- **Putting it all together in plain English:** This describes the mathematical structure that results from grouping integers by their remainders when divided by n.
- **Why do we use this fancy notation?** It gives us a precise way to express the set of all possible remainders when dividing by n, which is fundamental to modular arithmetic.
- **Assumptions and considerations:** We need to understand remainders and modular arithmetic. The thought process is: Each possible remainder when divided by n gives a different equivalence class.
- **How it works:** This gives us the formal approach to understanding modular arithmetic systems.

### Example 8.3.14: The Quotient Set of Similarity Matrices
Consider the relation of similarity on n × n matrices:
```
A R B ⇔ there exists an invertible matrix P such that B = P⁻¹AP
```

This is an equivalence relation, and the equivalence classes consist of all matrices that are similar to each other. The quotient set consists of these similarity classes.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the relation of similarity on n by n matrices A R B if and only if there exists an invertible matrix P such that B equals P inverse A P. This is an equivalence relation, and the equivalence classes consist of all matrices that are similar to each other. The quotient set consists of these similarity classes.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the relation of similarity on n by n matrices A R B if and only if there exists an invertible matrix P such that B equals P inverse A P. This is an equivalence relation, and the equivalence classes consist of all matrices that are similar to each other. The quotient set consists of these similarity classes."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the relation of similarity":** We're working with a relationship called similarity.
  - **"on n × n matrices":** Between square matrices of size n.
  - **"A R B":** The relation notation.
  - **"⇔":** "if and only if."
  - **"there exists an invertible matrix P":** There is a special matrix P that can be inverted.
  - **"such that B = P⁻¹AP":** The mathematical condition for similarity.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"the equivalence classes consist of":** The groups contain.
  - **"all matrices that are similar to each other":** All matrices that represent the same linear transformation in different bases.
  - **"The quotient set consists of":** The set of these groups.
  - **"these similarity classes":** These groups of similar matrices.
- **Putting it all together in plain English:** This defines a relationship where matrices are equivalent if they represent the same linear transformation in different coordinate systems.
- **Why do we use this fancy notation?** It gives us a precise way to express when two matrices represent the same linear transformation up to change of basis.
- **Assumptions and considerations:** We need to understand matrix similarity and change of basis. The thought process is: Matrices that represent the same transformation in different coordinates are in the same class.
- **How it works:** This gives us the formal approach to classifying matrices by their similarity.

### Example 8.3.15: The Quotient Set of Connected Components
Consider the relation on a topological space X defined by:
```
x R y ⇔ there exists a path connecting x and y
```

This is an equivalence relation, and the equivalence classes are the connected components of X. The quotient set X/R is the set of all connected components.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Consider the relation on a topological space X defined by x R y if and only if there exists a path connecting x and y. This is an equivalence relation, and the equivalence classes are the connected components of X. The quotient set X slash R is the set of all connected components.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Consider the relation on a topological space X defined by x R y if and only if there exists a path connecting x and y. This is an equivalence relation, and the equivalence classes are the connected components of X. The quotient set X slash R is the set of all connected components."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Consider the relation on a topological space X":** We're working with a mathematical space.
  - **"defined by x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"there exists a path connecting x and y":** There is a continuous path between the points.
  - **"This is an equivalence relation":** This relationship has the three required properties.
  - **"the equivalence classes are the connected components":** The groups are the connected pieces.
  - **"of X":** Of the space.
  - **"The quotient set X/R":** The set of these components.
  - **"is the set of all connected components":** All the connected pieces of the space.
- **Putting it all together in plain English:** This defines a relationship where points are equivalent if you can draw a continuous path between them, creating the connected components of a space.
- **Why do we use this fancy notation?** It gives us a precise way to express the concept of connected components in topology.
- **Assumptions and considerations:** We need to understand paths and connectivity. The thought process is: Points that can be connected by a path are in the same component.
- **How it works:** This gives us the formal approach to understanding connected components in topological spaces.

### Example 8.3.16: The Canonical Projection for Congruence Modulo n
For the equivalence relation of congruence modulo n on Z, the canonical projection π: Z → Z/nZ is given by:
```
π(k) = [k] = k mod n
```

This is essentially the modulo function.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For the equivalence relation of congruence modulo n on ℤ, the canonical projection pi from ℤ to integers sub n integers is given by pi of k equals bracket k equals k mod n. This is essentially the modulo function.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the equivalence relation of congruence modulo n on integers, the canonical projection pi from integers to integers sub n integers is given by pi of k equals bracket k equals k mod n. This is essentially the modulo function."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the equivalence relation of congruence modulo n":** For the "differs by multiple of n" relationship.
  - **"on ℤ":** On the integers.
  - **"the canonical projection π":** The standard function that assigns each number to its group.
  - **"from ℤ to ℤ/nℤ":** From integers to the modular arithmetic system.
  - **"is given by π(k)":** The function definition.
  - **"equals [k]":** The equivalence class of k.
  - **"equals k mod n":** The remainder when k is divided by n.
  - **"This is essentially the modulo function":** It's the remainder function.
- **Putting it all together in plain English:** This describes the function that takes any integer and tells us which remainder group it belongs to when divided by n.
- **Why do we use this fancy notation?** It gives us a precise way to express the function that computes remainders and assigns numbers to their modular classes.
- **Assumptions and considerations:** We need to understand the modulo operation. The thought process is: The canonical projection is essentially the remainder function.
- **How it works:** This gives us the formal approach to understanding the canonical projection in quotient sets.

### Example 8.3.17: Equivalence Relation Induced by the Absolute Value
Let f: R → R be defined by f(x) = |x|. The equivalence relation R_f is:
```
x R_f y ⇔ |x| = |y|
```

The equivalence classes are [r] = {r, -r} for each r ≥ 0, with [0] = {0}.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let f from ℝ to ℝ be defined by f of x equals the absolute value of x. The equivalence relation R sub f is x R sub f y if and only if the absolute value of x equals the absolute value of y. The equivalence classes are bracket r equals the set containing r and negative r for each r greater than or equal to zero, with bracket zero equals the set containing zero.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let f from real numbers to real numbers be defined by f of x equals the absolute value of x. The equivalence relation R sub f is x R sub f y if and only if the absolute value of x equals the absolute value of y. The equivalence classes are bracket r equals the set containing r and negative r for each r greater than or equal to zero, with bracket zero equals the set containing zero."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let f: ℝ → ℝ":** We're defining a function from real numbers to real numbers.
  - **"be defined by f(x) = |x|":** The function gives the distance from zero.
  - **"The equivalence relation R_f":** The relationship induced by this function.
  - **"is x R_f y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"|x| = |y|":** The absolute values are equal (same distance from zero).
  - **"The equivalence classes are [r]":** The groups are labeled by r.
  - **"equals {r, -r}":** Each group contains a number and its negative.
  - **"for each r ≥ 0":** For non-negative numbers.
  - **"with [0] = {0}":** Zero is in its own group.
- **Putting it all together in plain English:** This shows that the absolute value function groups numbers by their distance from zero, so positive and negative numbers with the same distance are in the same group.
- **Why do we use this fancy notation?** It gives us a precise way to express how functions induce equivalence relations on their domains.
- **Assumptions and considerations:** We need to understand absolute values. The thought process is: Numbers with the same absolute value are in the same class.
- **How it works:** This gives us the formal approach to understanding equivalence relations induced by functions.

### Example 8.3.18: Constructing Functions from Equivalence Relations
Let R be the equivalence relation on R defined by:
```
x R y ⇔ x² = y²
```

This is the equivalence relation induced by f(x) = x². The quotient set R/R can be identified with [0, ∞), and the canonical projection π: R → [0, ∞) is given by π(x) = x².

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let R be the equivalence relation on ℝ defined by x R y if and only if x squared equals y squared. This is the equivalence relation induced by f of x equals x squared. The quotient set R slash R can be identified with the interval from zero to infinity, and the canonical projection pi from ℝ to the interval from zero to infinity is given by pi of x equals x squared.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let R be the equivalence relation on real numbers defined by x R y if and only if x squared equals y squared. This is the equivalence relation induced by f of x equals x squared. The quotient set R slash R can be identified with the interval from zero to infinity, and the canonical projection pi from real numbers to the interval from zero to infinity is given by pi of x equals x squared."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let R be the equivalence relation on ℝ":** We're defining a relationship between real numbers.
  - **"defined by x R y":** The relation notation.
  - **"⇔":** "if and only if."
  - **"x² = y²":** The squares are equal.
  - **"This is the equivalence relation induced by f(x) = x²":** This relationship comes from the squaring function.
  - **"The quotient set ℝ/ℝ":** The set of equivalence classes.
  - **"can be identified with [0, ∞)":** It corresponds to non-negative real numbers.
  - **"the canonical projection π: ℝ → [0, ∞)":** The function that assigns each number to its group.
  - **"is given by π(x) = x²":** The function gives the square.
- **Putting it all together in plain English:** This shows that the squaring function naturally groups numbers that have the same square, creating equivalence classes that correspond to the non-negative real numbers.
- **Why do we use this fancy notation?** It gives us a precise way to express the relationship between equivalence relations and the functions that induce them.
- **Assumptions and considerations:** We need to understand the squaring function. The thought process is: The equivalence classes are indexed by the non-negative real numbers.
- **How it works:** This gives us the formal approach to understanding how functions induce equivalence relations.

### Example 8.3.19: The Modulo Function
Let R be congruence modulo m on Z, and let S be congruence modulo n on Z. The function f: Z → Z defined by f(k) = k is compatible with R and S if and only if m | n. In this case, the induced function f̃: Z/mZ → Z/nZ is given by f̃([k]_m) = [k]_n.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let R be congruence modulo m on ℤ, and let S be congruence modulo n on ℤ. The function f from ℤ to ℤ defined by f of k equals k is compatible with R and S if and only if m divides n. In this case, the induced function f tilde from integers sub m integers to integers sub n integers is given by f tilde of bracket k bracket sub m equals bracket k bracket sub n.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let R be congruence modulo m on integers, and let S be congruence modulo n on integers. The function f from integers to integers defined by f of k equals k is compatible with R and S if and only if m divides n. In this case, the induced function f tilde from integers sub m integers to integers sub n integers is given by f tilde of bracket k bracket sub m equals bracket k bracket sub n."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let R be congruence modulo m on ℤ":** First modular relationship.
  - **"S be congruence modulo n on ℤ":** Second modular relationship.
  - **"The function f: ℤ → ℤ":** The function that does nothing special.
  - **"defined by f(k) = k":** It's the identity function.
  - **"is compatible with R and S":** It respects both modular structures.
  - **"if and only if m | n":** When m divides n.
  - **"In this case":** When the condition holds.
  - **"the induced function f̃":** The function it creates.
  - **"from ℤ/mℤ to ℤ/nℤ":** Between the two modular systems.
  - **"is given by f̃([k]_m) = [k]_n":** How it maps the classes.
- **Putting it all together in plain English:** This describes when the identity function respects both modular structures and how it naturally creates a function between the two modular arithmetic systems.
- **Why do we use this fancy notation?** It gives us a precise way to express the compatibility of functions with respect to equivalence relations.
- **Assumptions and considerations:** We need to understand modular arithmetic and function compatibility. The thought process is: The identity function preserves modular congruences when one modulus divides the other.
- **How it works:** This gives us the formal approach to understanding compatible functions between quotient sets.

### Example 8.3.20: The Square Function on Integers Modulo n
Let R be congruence modulo 4 on Z, and let S be congruence modulo 2 on Z. The function f: Z → Z defined by f(k) = k² is compatible with R and S because:
```
If k ≡ l (mod 4), then k² ≡ l² (mod 2)
```

The induced function f̃: Z/4Z → Z/2Z is given by f̃([k]_4) = [k²]_2.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Let R be congruence modulo four on ℤ, and let S be congruence modulo two on ℤ. The function f from ℤ to ℤ defined by f of k equals k squared is compatible with R and S because if k congruent to l modulo four, then k squared congruent to l squared modulo two. The induced function f tilde from integers sub four integers to integers sub two integers is given by f tilde of bracket k bracket sub four equals bracket k squared bracket sub two.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Let R be congruence modulo four on integers, and let S be congruence modulo two on integers. The function f from integers to integers defined by f of k equals k squared is compatible with R and S because if k congruent to l modulo four, then k squared congruent to l squared modulo two. The induced function f tilde from integers sub four integers to integers sub two integers is given by f tilde of bracket k bracket sub four equals bracket k squared bracket sub two."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Let R be congruence modulo 4 on ℤ":** The "differs by multiple of 4" relationship.
  - **"S be congruence modulo 2 on ℤ":** The "differs by multiple of 2" relationship.
  - **"The function f: ℤ → ℤ":** The squaring function.
  - **"defined by f(k) = k²":** Squares each number.
  - **"is compatible with R and S":** Respects both modular structures.
  - **"because if k ≡ l (mod 4)":** If numbers differ by multiple of 4.
  - **"then k² ≡ l² (mod 2)":** Then their squares differ by multiple of 2.
  - **"The induced function f̃":** The function it creates.
  - **"from ℤ/4ℤ to ℤ/2ℤ":** Between the two modular systems.
  - **"is given by f̃([k]_4) = [k²]_2":** Maps classes to the class of the square.
- **Putting it all together in plain English:** This describes how the squaring function behaves with respect to different modular arithmetic systems and how it naturally creates a function between them.
- **Why do we use this fancy notation?** It gives us a precise way to express how functions interact with equivalence relations.
- **Assumptions and considerations:** We need to understand modular arithmetic and polynomial functions. The thought process is: Squaring preserves certain modular congruences and induces functions between quotient sets.
- **How it works:** This gives us the formal approach to understanding how algebraic functions interact with modular arithmetic.
