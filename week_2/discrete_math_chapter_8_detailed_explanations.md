# Discrete Mathematics Chapter 8 - Detailed Example Explanations

This document provides detailed explanations for every example from Chapter 8 of Discrete Mathematics with Applications, following the same format as the detailed explanation for examples in Chapter 5.

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

Formal Restatement: For the relation L defined by x L y ⇔ x < y for real numbers x and y, determine if the given pairs satisfy the relation and describe its graph.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation L defined by x L y if and only if x is less than y for real numbers x and y, determine if the given pairs satisfy the relation and describe its graph."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation L defined by":** We're talking about a specific relationship called L.
  - **"x L y if and only if x is less than y":** The relation holds when the first number is smaller than the second number.
  - **"for real numbers x and y":** x and y can be any real numbers (positive, negative, decimals, etc.).
  - **"determine if the given pairs satisfy the relation":** We need to check if each pair makes the "less than" condition true.
  - **"and describe its graph":** We need to visualize this relation as points on a coordinate plane.
- **Putting it all together in plain English:** This is asking us to check whether specific pairs of numbers satisfy the "less than" relationship, and to describe what this relationship looks like when plotted on a graph.
- **Why do we use this fancy notation?** It gives us a precise mathematical way to express the "less than" relationship and allows us to ask questions about specific pairs of numbers.
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

Formal Restatement: For the relation E defined by m E n if and only if m − n is even, determine if the given pairs satisfy the relation, list integers related to 1, and prove the property for odd integers.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation E defined by m E n if and only if m minus n is even, determine if the given pairs satisfy the relation, list integers related to one, and prove the property for odd integers."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation E defined by":** We're dealing with a relationship called E.
  - **"m E n if and only if m minus n is even":** The relation holds when the difference between the two numbers is an even number.
  - **"determine if the given pairs satisfy the relation":** Check if each pair makes the difference even.
  - **"list integers related to one":** Find some numbers that when subtracted from 1 give an even result.
  - **"prove the property for odd integers":** Show that for any odd number n, n minus 1 is even.
- **Putting it all together in plain English:** This is asking us to check whether specific pairs of integers have an even difference, find numbers related to 1 through this relation, and prove that all odd numbers are related to 1.
- **Why do we use this fancy notation?** It gives us a precise way to express the relationship based on even differences and allows us to investigate properties of integers.
- **Assumptions and considerations:** We need to understand what "even" means (divisible by 2) and how to compute differences. The thought process is: For each pair, calculate the difference and check if it's divisible by 2.
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

Formal Restatement: For the relation S defined by A S B if and only if set A has at least as many elements as set B, determine if the given pairs of subsets satisfy the relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation S defined by A S B if and only if set A has at least as many elements as set B, determine if the given pairs of subsets satisfy the relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation S defined by":** We're working with a relationship called S.
  - **"A S B if and only if set A has at least as many elements as set B":** The relation holds when the first set has the same number or more elements than the second set.
  - **"determine if the given pairs of subsets satisfy the relation":** Check if each pair of sets satisfies the "at least as many elements" condition.
- **Putting it all together in plain English:** This is asking us to compare the sizes of different sets and see if the first set in each pair has at least as many elements as the second set.
- **Why do we use this fancy notation?** It gives us a precise way to compare the sizes of sets and allows us to investigate relationships between different subsets.
- **Assumptions and considerations:** We need to understand how to count elements in sets and compare quantities. The thought process is: Count the elements in each set and compare the counts.
- **How it works:** This gives us the formal criteria to use when comparing the sizes of sets in this relation.

### Example 8.1.4: The Inverse of a Finite Relation
Let A = {2, 3, 4} and B = {2, 6, 8} and let R be the "divides" relation from A to B: For all (x, y) ∈ A × B,
```
x R y ⇔ x | y ⇔ x divides y.
```

a. State explicitly which ordered pairs are in R and R⁻¹, and draw arrow diagrams for R and R⁻¹.
b. Describe R⁻¹ in words.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For the divides relation R from A to B, find all ordered pairs in R and its inverse R⁻¹, draw arrow diagrams, and describe R⁻¹ in words.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the divides relation R from A to B, find all ordered pairs in R and its inverse R inverse, draw arrow diagrams, and describe R inverse in words."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the divides relation R from A to B":** We're working with a relationship R that connects elements from set A to set B.
  - **"find all ordered pairs in R and its inverse R inverse":** We need to list all pairs that satisfy the divides condition and then find the "reverse" pairs.
  - **"draw arrow diagrams":** Create visual representations showing the connections.
  - **"describe R inverse in words":** Explain what the inverse relation means in plain language.
- **Putting it all together in plain English:** This is asking us to find all pairs where one number divides another, then find the reverse relationship, draw pictures of both relationships, and explain the reverse relationship in words.
- **Why do we use this fancy notation?** It gives us a precise way to express divisibility relationships and their reverses, allowing us to investigate the inverse relationship.
- **Assumptions and considerations:** We need to understand what "divides" means and how to find inverse relations. The thought process is: Check each possible pair for divisibility, then swap the order for the inverse.
- **How it works:** This gives us the formal approach to working with divisibility relations and their inverses.

### Example 8.1.5: The Inverse of an Infinite Relation
Define a relation R from R to R as follows: For all (x, y) ∈ R × R,
```
x R y ⇔ y = 2|x|.
```

Draw the graphs of R and R⁻¹ in the Cartesian plane. Is R⁻¹ a function?

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For the relation R defined by y = 2 times the absolute value of x, draw the graphs of R and its inverse R⁻¹, and determine if R⁻¹ is a function.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R defined by y equals two times the absolute value of x, draw the graphs of R and its inverse R inverse, and determine if R inverse is a function."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R defined by":** We're dealing with a relationship R between x and y values.
  - **"y equals two times the absolute value of x":** For each x, y is twice the distance of x from zero.
  - **"draw the graphs of R and its inverse":** Create visual plots of both the original and reversed relationships.
  - **"determine if R inverse is a function":** Check if the reversed relationship qualifies as a function.
- **Putting it all together in plain English:** This is asking us to plot a mathematical relationship and its reverse, then determine if the reverse relationship meets the criteria for being a function.
- **Why do we use this fancy notation?** It gives us a precise way to express the absolute value relationship and allows us to investigate its inverse.
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

Formal Restatement: For the relation R defined by 2 divides (x − y), draw the directed graph showing all connections between elements of set A.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R defined by two divides the difference of x and y, draw the directed graph showing all connections between elements of set A."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R defined by":** We're working with a relationship R between numbers in set A.
  - **"two divides the difference of x and y":** The relationship holds when 2 evenly divides the difference between the two numbers.
  - **"draw the directed graph":** Create a visual diagram showing arrows between connected numbers.
  - **"showing all connections between elements of set A":** Show all pairs where this divisibility condition holds.
- **Putting it all together in plain English:** This is asking us to create a visual diagram showing which numbers in the set are connected by the "divisible by 2 difference" relationship, with arrows indicating the direction.
- **Why do we use this fancy notation?** It gives us a precise way to express the divisibility relationship and allows us to visualize the connections.
- **Assumptions and considerations:** We need to understand divisibility and how to check differences. The thought process is: Check every pair of numbers to see if their difference is divisible by 2, then draw arrows accordingly.
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

Formal Restatement: Understand how a quaternary relation represents hospital patient data in a database and how SQL queries extract specific information from this data.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Understand how a quaternary relation represents hospital patient data in a database and how SQL queries extract specific information from this data."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Understand how a quaternary relation represents":** We're learning how a 4-part relationship stores information.
  - **"hospital patient data in a database":** This is about storing patient information in a computer system.
  - **"how SQL queries extract specific information":** We're learning how to ask questions of this database.
  - **"from this data":** How to get answers from the stored information.
- **Putting it all together in plain English:** This is explaining how hospitals store patient information in computer databases using mathematical relations, and how we can ask specific questions to get particular pieces of information from that data.
- **Why do we use this fancy notation?** It gives us a precise mathematical way to model database relationships and allows us to understand how real-world data systems work.
- **Assumptions and considerations:** We need to understand how databases store and retrieve information. The thought process is: Each row represents a complete patient record, and we can filter and select specific parts of that information.
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

Formal Restatement: For the given relations R, S, and T on set A, determine whether each relation is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the given relations R, S, and T on set A, determine whether each relation is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the given relations R, S, and T":** We're examining three different relationships on the same set.
  - **"on set A":** All relationships are between elements of the same set A.
  - **"determine whether each relation is":** We need to check each relationship for three specific properties.
  - **"reflexive, symmetric, and transitive":** These are mathematical properties that relationships can have.
- **Putting it all together in plain English:** This is asking us to analyze three different relationships between numbers in a set to see if they have specific mathematical properties like being true for elements with themselves, working both ways, and following chain relationships.
- **Why do we use this fancy notation?** It gives us a precise way to define and analyze relationships between elements, which is fundamental to understanding how connections work in mathematics.
- **Assumptions and considerations:** We need to understand the definitions of reflexive, symmetric, and transitive properties. The thought process is: Check each property systematically for each relation.
- **How it works:** This gives us the formal approach to analyzing the properties of mathematical relations.

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

Formal Restatement: For the equality relation R defined by x R y if and only if x equals y, determine if R is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the equality relation R defined by x R y if and only if x equals y, determine if R is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the equality relation R":** We're talking about the "equals" relationship.
  - **"defined by x R y if and only if x equals y":** The relation holds when two numbers are the same.
  - **"determine if R is reflexive, symmetric, and transitive":** Check if equality has these three properties.
- **Putting it all together in plain English:** This is asking us to check if the basic "equals" relationship has three fundamental mathematical properties.
- **Why do we use this fancy notation?** It gives us a precise way to analyze the most basic mathematical relationship - equality - to understand its fundamental properties.
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

Formal Restatement: For the less-than relation R defined by x R y if and only if x is less than y, determine if R is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the less-than relation R defined by x R y if and only if x is less than y, determine if R is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the less-than relation R":** We're talking about the "is less than" relationship.
  - **"defined by x R y if and only if x is less than y":** The relation holds when the first number is smaller than the second.
  - **"determine if R is reflexive, symmetric, and transitive":** Check if "less than" has these three properties.
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

Formal Restatement: For the congruence modulo 3 relation T defined by m T n if and only if 3 divides (m − n), determine if T is reflexive, symmetric, and transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the congruence modulo three relation T defined by m T n if and only if three divides the difference of m and n, determine if T is reflexive, symmetric, and transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the congruence modulo three relation T":** We're talking about a relationship based on divisibility by 3.
  - **"defined by m T n if and only if three divides the difference":** The relation holds when the difference between numbers is divisible by 3.
  - **"determine if T is reflexive, symmetric, and transitive":** Check if this divisibility relationship has the three properties.
- **Putting it all together in plain English:** This is asking us to check if the relationship "differs by a multiple of 3" has the three fundamental mathematical properties.
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

Formal Restatement: For the relation R with ordered pairs (0,1), (1,2), (2,3), find the transitive closure R^t that contains R and is transitive.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R with ordered pairs zero to one, one to two, two to three, find the transitive closure R to the power t that contains R and is transitive."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R with ordered pairs":** We're working with a relationship that has specific connections.
  - **"find the transitive closure":** We need to find the smallest extension of this relation that includes all indirect connections.
  - **"that contains R and is transitive":** The new relation must include all the original connections and follow the transitive property.
- **Putting it all together in plain English:** This is asking us to extend a chain of connections (0→1→2→3) to include all the indirect connections (0→2, 0→3, 1→3) so that the relationship follows the transitive property.
- **Why do we use this fancy notation?** It gives us a precise way to express the concept of "reachable through a chain of connections" and allows us to work with indirect relationships.
- **Assumptions and considerations:** We need to understand transitivity and how to find all indirect connections. The thought process is: Start with the given connections, then add all connections that follow from chains of existing connections.
- **How it works:** This gives us the formal approach to finding the transitive closure of a relation.

## Chapter 8.3 Examples

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

Formal Restatement: For the relation R defined by 4 divides (x squared minus y squared), determine if R is reflexive, symmetric, transitive, and thus an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R defined by four divides the difference of x squared and y squared, determine if R is reflexive, symmetric, transitive, and thus an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R defined by":** We're working with a relationship based on a mathematical condition.
  - **"four divides the difference of x squared and y squared":** The relation holds when 4 evenly divides the difference of squares.
  - **"determine if R is reflexive, symmetric, transitive":** Check if this relationship has the three fundamental properties.
  - **"and thus an equivalence relation":** If it has all three properties, it's a special type of relation called equivalence.
- **Putting it all together in plain English:** This is asking us to check if a relationship based on "difference of squares divisible by 4" has the three fundamental mathematical properties that make it an equivalence relation.
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

Formal Restatement: For the relation R defined by x R y if and only if x and y are in the same subset of the partition, determine if R is reflexive, symmetric, transitive, and thus an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R defined by x R y if and only if x and y are in the same subset of the partition, determine if R is reflexive, symmetric, transitive, and thus an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R defined by":** We're working with a relationship based on set membership.
  - **"x R y if and only if x and y are in the same subset":** The relation holds when two elements are grouped together in the partition.
  - **"of the partition":** The partition is a way of dividing the set into non-overlapping groups.
  - **"determine if R is reflexive, symmetric, transitive":** Check if this grouping relationship has the three properties.
- **Putting it all together in plain English:** This is asking us to check if the relationship "belongs to the same group in a partition" has the three fundamental mathematical properties that make it an equivalence relation.
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

Formal Restatement: For the congruence modulo 3 relation T, identify the equivalence classes and verify they form a partition of the integers.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the congruence modulo three relation T, identify the equivalence classes and verify they form a partition of the integers."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the congruence modulo three relation T":** We're working with the "differs by multiple of 3" relationship.
  - **"identify the equivalence classes":** Find the groups of numbers that are all related to each other.
  - **"verify they form a partition":** Check that these groups cover all integers without overlap.
  - **"of the integers":** We're working with all whole numbers.
- **Putting it all together in plain English:** This is asking us to find the groups of integers where each number in a group differs from others by multiples of 3, and verify that all integers are in exactly one such group.
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

Formal Restatement: For the congruence modulo n relation, verify it's an equivalence relation and describe its equivalence classes and the quotient set.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the congruence modulo n relation, verify it's an equivalence relation and describe its equivalence classes and the quotient set."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the congruence modulo n relation":** We're working with the "differs by multiple of n" relationship.
  - **"verify it's an equivalence relation":** Confirm it has the three required properties.
  - **"describe its equivalence classes":** Explain the groups of numbers that are all related.
  - **"and the quotient set":** Describe the set of these groups.
- **Putting it all together in plain English:** This is asking us to understand how dividing by n creates n different groups of integers, where each group contains numbers that leave the same remainder when divided by n.
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

Formal Restatement: Understand how rational numbers can be constructed as equivalence classes of ordered pairs of integers using the relation (a,b) ∼ (c,d) if and only if a d equals b c.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: Understand how rational numbers can be constructed as equivalence classes of ordered pairs of integers using the relation a comma b tilde c comma d if and only if a d equals b c."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"Understand how rational numbers can be constructed":** We're learning how to build fractions mathematically.
  - **"as equivalence classes of ordered pairs of integers":** Each rational number is represented by a group of equivalent pairs.
  - **"using the relation a comma b tilde c comma d":** Two pairs are equivalent if their cross products are equal.
  - **"if and only if a d equals b c":** The mathematical condition for two fractions to be equal.
- **Putting it all together in plain English:** This is explaining how we can think of rational numbers as groups of equivalent fractions, where (2,3) and (4,6) represent the same rational number because 2×6 = 3×4.
- **Why do we use this fancy notation?** It gives us a precise way to define rational numbers without assuming we already know what they are, building them up from integers.
- **Assumptions and considerations:** We need to understand that equivalent fractions represent the same number. The thought process is: Different ways of writing the same fraction are equivalent.
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

Formal Restatement: For the relation R on functions defined by f R g if and only if f minus g is a constant function, verify this is an equivalence relation and understand its meaning.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R on functions defined by f R g if and only if f minus g is a constant function, verify this is an equivalence relation and understand its meaning."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R on functions":** We're working with a relationship between functions.
  - **"defined by f R g if and only if f minus g is a constant function":** Two functions are related if their difference is always the same value.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
  - **"and understand its meaning":** Understand what this relationship means for functions.
- **Putting it all together in plain English:** This is asking us to understand that functions are equivalent if they differ by a constant amount everywhere, and to verify this is a valid equivalence relation.
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

Formal Restatement: For the relation R on triangles defined by triangle ABC R triangle DEF if and only if they are congruent, verify this is an equivalence relation and understand the equivalence classes.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R on triangles defined by triangle ABC R triangle DEF if and only if they are congruent, verify this is an equivalence relation and understand the equivalence classes."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R on triangles":** We're working with a relationship between geometric shapes.
  - **"defined by triangle ABC R triangle DEF":** The relationship holds between two triangles.
  - **"if and only if they are congruent":** When the triangles have the same size and shape.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
  - **"understand the equivalence classes":** Understand the groups of congruent triangles.
- **Putting it all together in plain English:** This is asking us to understand that triangles with the same size and shape are equivalent, and that this forms a valid mathematical equivalence relationship.
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

Formal Restatement: For the relation on vectors defined by v ∼ w if and only if v minus w is in subspace W, verify this is an equivalence relation and understand the quotient space.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation on vectors defined by v tilde w if and only if v minus w is in subspace W, verify this is an equivalence relation and understand the quotient space."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation on vectors":** We're working with a relationship between vectors.
  - **"defined by v tilde w if and only if v minus w is in subspace W":** Two vectors are related if their difference is in a special subset W.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
  - **"understand the quotient space":** Understand the resulting mathematical structure.
- **Putting it all together in plain English:** This is asking us to understand how vectors can be grouped based on their relationship to a subspace, creating a quotient space that captures the essential structure of the vector space modulo the subspace.
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

Formal Restatement: For the relation on binary relations defined by R1 R R2 if and only if they have the same reflexive closure, verify this is an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation on binary relations defined by R1 R R2 if and only if they have the same reflexive closure, verify this is an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation on binary relations":** We're working with relationships between relationships.
  - **"defined by R1 R R2 if and only if they have the same reflexive closure":** Two relations are equivalent if they become the same when we add all necessary self-connections.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
- **Putting it all together in plain English:** This is asking us to understand that binary relations can be grouped based on what they become when we make them reflexive, and that this grouping satisfies the equivalence relation properties.
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

Formal Restatement: For the relation R on logical formulas defined by φ R ψ if and only if φ if and only if ψ is always true, verify this is an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R on logical formulas defined by phi R psi if and only if phi if and only if psi is always true, verify this is an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R on logical formulas":** We're working with a relationship between logical statements.
  - **"defined by phi R psi if and only if phi if and only if psi is always true":** Two formulas are related if they have the same truth value in all situations.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
- **Putting it all together in plain English:** This is asking us to understand that logical formulas can be grouped by whether they always have the same truth values, and that this grouping satisfies the equivalence relation properties.
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

Formal Restatement: For the relation R on continuous functions defined by f R g if and only if f of zero equals g of zero and f of one equals g of one, verify this is an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R on continuous functions defined by f R g if and only if f of zero equals g of zero and f of one equals g of one, verify this is an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R on continuous functions":** We're working with a relationship between functions.
  - **"defined by f R g if and only if f of zero equals g of zero and f of one equals g of one":** Two functions are related if they have the same values at the start and end of the interval.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
- **Putting it all together in plain English:** This is asking us to understand that continuous functions can be grouped based on their values at the endpoints [0,1], and that this grouping satisfies the equivalence relation properties.
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

Formal Restatement: For the relation R on pairs of integers defined by (a,b) R (c,d) if and only if a/b equals c/d, verify this is an equivalence relation and understand it represents rational numbers.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the relation R on pairs of integers defined by a comma b R c comma d if and only if a divided by b equals c divided by d, verify this is an equivalence relation and understand it represents rational numbers."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the relation R on pairs of integers":** We're working with relationships between pairs of numbers.
  - **"defined by a comma b R c comma d if and only if a divided by b equals c divided by d":** Two pairs are related if they represent the same fraction.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
  - **"understand it represents rational numbers":** Understand that each equivalence class is a rational number.
- **Putting it all together in plain English:** This is asking us to understand that different ways of writing the same fraction (like 2/3, 4/6, 6/9) are all equivalent and represent the same rational number.
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

Formal Restatement: For the congruence modulo n relation on integers, understand the quotient set Z/nZ and its properties.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the congruence modulo n relation on integers, understand the quotient set Z divided by n Z and its properties."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the congruence modulo n relation on integers":** We're working with the "differs by multiple of n" relationship.
  - **"understand the quotient set":** Understand the set of equivalence classes.
  - **"Z divided by n Z":** The mathematical notation for the set of residue classes.
  - **"and its properties":** Understand what special properties this set has.
- **Putting it all together in plain English:** This is asking us to understand the mathematical structure that results from grouping integers by their remainders when divided by n, and that this structure has special algebraic properties.
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

Formal Restatement: For the similarity relation on matrices defined by A R B if and only if there exists invertible P such that B equals P inverse A P, verify this is an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the similarity relation on matrices defined by A R B if and only if there exists invertible P such that B equals P inverse A P, verify this is an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the similarity relation on matrices":** We're working with a relationship between square matrices.
  - **"defined by A R B if and only if there exists invertible P":** Two matrices are related if one can be obtained from the other by conjugation with an invertible matrix.
  - **"such that B equals P inverse A P":** The mathematical condition for matrix similarity.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
- **Putting it all together in plain English:** This is asking us to understand that matrices can be grouped by whether they represent the same linear transformation in different bases, and that this grouping satisfies the equivalence relation properties.
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

Formal Restatement: For the path-connected relation on a topological space X defined by x R y if and only if there exists a path connecting them, verify this is an equivalence relation.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the path-connected relation on a topological space X defined by x R y if and only if there exists a path connecting them, verify this is an equivalence relation."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the path-connected relation on a topological space X":** We're working with a relationship between points in a space.
  - **"defined by x R y if and only if there exists a path connecting them":** Two points are related if you can draw a continuous path between them.
  - **"verify this is an equivalence relation":** Confirm it has the three required properties.
- **Putting it all together in plain English:** This is asking us to understand that points in a space can be grouped by whether you can connect them with a path, and that this grouping satisfies the equivalence relation properties.
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

Formal Restatement: For the congruence modulo n relation, understand the canonical projection map π that sends each integer to its equivalence class.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the congruence modulo n relation, understand the canonical projection map pi that sends each integer to its equivalence class."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the congruence modulo n relation":** We're working with the "differs by multiple of n" relationship.
  - **"understand the canonical projection map pi":** Understand the function that assigns each number to its group.
  - **"that sends each integer to its equivalence class":** The function maps numbers to their remainder groups.
- **Putting it all together in plain English:** This is asking us to understand the function that takes any integer and tells us which remainder group it belongs to when divided by n.
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

Formal Restatement: For the absolute value function f(x) = |x|, understand the induced equivalence relation and its equivalence classes.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the absolute value function f of x equals absolute value of x, understand the induced equivalence relation and its equivalence classes."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the absolute value function f of x":** We're working with the function that gives the distance from zero.
  - **"understand the induced equivalence relation":** Understand the relationship it creates between numbers.
  - **"and its equivalence classes":** Understand the groups of numbers it creates.
- **Putting it all together in plain English:** This is asking us to understand that the absolute value function groups numbers by their distance from zero, so positive and negative numbers with the same distance are in the same group.
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

Formal Restatement: For the equivalence relation on real numbers defined by x R y if and only if x squared equals y squared, understand how this relates to the squaring function and the resulting quotient set.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the equivalence relation on real numbers defined by x R y if and only if x squared equals y squared, understand how this relates to the squaring function and the resulting quotient set."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the equivalence relation on real numbers":** We're working with a relationship between real numbers.
  - **"defined by x R y if and only if x squared equals y squared":** Two numbers are related if they have the same square.
  - **"understand how this relates to the squaring function":** Understand the connection to the function that squares numbers.
  - **"and the resulting quotient set":** Understand the set of equivalence classes.
- **Putting it all together in plain English:** This is asking us to understand that the squaring function naturally groups numbers that have the same square, creating equivalence classes that correspond to the non-negative real numbers.
- **Why do we use this fancy notation?** It gives us a precise way to express the relationship between equivalence relations and the functions that induce them.
- **Assumptions and considerations:** We need to understand the squaring function. The thought process is: The equivalence classes are indexed by the non-negative real numbers.
- **How it works:** This gives us the formal approach to understanding how functions induce equivalence relations.

### Example 8.3.19: The Modulo Function
Let R be congruence modulo m on Z, and let S be congruence modulo n on Z. The function f: Z → Z defined by f(k) = k is compatible with R and S if and only if m | n. In this case, the induced function f̃: Z/mZ → Z/nZ is given by f̃([k]_m) = [k]_n.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For congruence relations modulo m and n, understand when the identity function is compatible and how it induces a function between quotient sets.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For congruence relations modulo m and n, understand when the identity function is compatible and how it induces a function between quotient sets."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For congruence relations modulo m and n":** We're working with two modular arithmetic systems.
  - **"understand when the identity function is compatible":** Understand when the function that does nothing special works with both systems.
  - **"how it induces a function between quotient sets":** Understand how it creates a function between the two sets of remainder classes.
- **Putting it all together in plain English:** This is asking us to understand when the identity function respects both modular structures and how it naturally creates a function between the two modular arithmetic systems.
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

Formal Restatement: For the squaring function on integers, understand its compatibility with congruence modulo 4 and modulo 2, and the induced function between quotient sets.

**How to Read This Out Loud and What It Means (Step-by-Step Explanation):**
- **Start by saying the words:** "Formal Restatement: For the squaring function on integers, understand its compatibility with congruence modulo four and modulo two, and the induced function between quotient sets."
- **Breaking it down slowly, without assuming any math knowledge:**
  - **"For the squaring function on integers":** We're working with the function that squares numbers.
  - **"understand its compatibility with congruence modulo four and modulo two":** Understand when squaring preserves these modular relationships.
  - **"and the induced function between quotient sets":** Understand how squaring creates a function between the modular arithmetic systems.
- **Putting it all together in plain English:** This is asking us to understand how the squaring function behaves with respect to different modular arithmetic systems and how it naturally creates a function between them.
- **Why do we use this fancy notation?** It gives us a precise way to express how functions interact with equivalence relations.
- **Assumptions and considerations:** We need to understand modular arithmetic and polynomial functions. The thought process is: Squaring preserves certain modular congruences and induces functions between quotient sets.
- **How it works:** This gives us the formal approach to understanding how algebraic functions interact with modular arithmetic.
