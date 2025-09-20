# 9.5 Counting Subsets of a Set: Combinations

"But 'glory' doesn't mean 'a nice knock-down argument,' " Alice objected. "When I use a word," Humpty Dumpty said, in rather a scornful tone, "it means just what I choose it to mean—neither more nor less." — Lewis Carroll, Through the Looking Glass, 1872

Consider the following question:
Suppose five members of a group of twelve are to be chosen to work as a team on a special project. How many distinct five-person teams can be selected?

This question is answered in Example 9.5.4. It is a special case of the following more general question:
Given a set S with n elements, how many subsets of size r can be chosen from S?

The number of subsets of size r that can be chosen from S equals the number of subsets of size r that S has. Each individual subset of size r is called an r-combination of the set.

## Definition
Let n and r be nonnegative integers with r ≤ n. An r-combination of a set of n elements is a subset of r of the n elements. As indicated in Section 5.1, the symbol
⎛ n ⎞
⎜ r ⎟
⎝   ⎠
which is read "n choose r," denotes the number of subsets of size r (r-combinations) that can be chosen from a set of n elements.

Recall from Section 5.1 that calculators generally use symbols like C(n, r), n C r , Cn,r , or
n
Cr instead of
⎛ n ⎞
⎜ r ⎟
⎝   ⎠.

## Example 9.5.1 3-Combinations
Let S = {Ann, Bob, Cyd, Dan}. Each committee consisting of three of the four people in S is a 3-combination of S.

a. List all such 3-combinations of S.
b. What is
⎛ 4 ⎞
⎜ 3 ⎟?
⎝   ⎠

### Solution
a. Each 3-combination of S is a subset of S of size 3. But each subset of size 3 can be obtained by leaving out one of the elements of S. The 3-combinations are

{Bob, Cyd, Dan}  leave out Ann
{Ann, Cyd, Dan}  leave out Bob
{Ann, Bob, Dan}  leave out Cyd
{Ann, Bob, Cyd}  leave out Dan.

b. Because
⎛ 4 ⎞
⎜ 3 ⎟ is the number of 3-combinations of a set with four elements, by part (a),
⎝   ⎠

⎛ 4 ⎞
⎜ 3 ⎟ = 4.
⎝   ⎠

There are two distinct methods that can be used to select r objects from a set of n elements. In an ordered selection, it is not only what elements are chosen but also the order in which they are chosen that matters. Two ordered selections are said to be the same if the elements chosen are the same and also if the elements are chosen in the same order. An ordered selection of r elements from a set of n elements is an r-permutation of the set.

In an unordered selection, on the other hand, it is only the identity of the chosen elements that matters. Two unordered selections are said to be the same if they consist of the same elements, regardless of the order in which the elements are chosen. An unordered selection of r elements from a set of n elements is the same as a subset of size r or an r-combination of the set.

## Example 9.5.2 Unordered Selections
How many unordered selections of two elements can be made from the set {0, 1, 2, 3}?

### Solution
An unordered selection of two elements from {0, 1, 2, 3} is the same as a 2-combination, or subset of size 2, taken from the set. These can be listed systematically:

{0, 1}, {0, 2}, {0, 3}  subsets containing 0
{1, 2}, {1, 3}          subsets containing 1 but not already listed
{2, 3}                  subsets containing 2 but not already listed.

Since this listing exhausts all possibilities, there are six subsets in all. Thus
⎛ 4 ⎞
⎜ 2 ⎟ = 6, which is the number of unordered selections of two elements from a set of four.
⎝   ⎠

When the values of n and r are small, it is reasonable to calculate values of
⎛ n ⎞
⎜ r ⎟ using the method of complete enumeration (listing all possibilities) illustrated in Examples 9.5.1 and 9.5.2. But when n and r are large, it is not feasible to compute these
⎝   ⎠

numbers by listing and counting all possibilities.

The general values of
⎛ n ⎞
⎜ r ⎟ can be found by a somewhat indirect but simple method. An equation is derived that contains
⎝   ⎠

a formula for
⎛ n ⎞
⎜ r ⎟ as a factor. Then this equation is solved to obtain
⎛ n ⎞
⎜ r ⎟. The method is illustrated by Example 9.5.3.
⎝   ⎠
⎝   ⎠

## Example 9.5.3 Relation between Permutations and Combinations
Write all 2-permutations of the set {0, 1, 2, 3}. Find an equation relating the number of 2-permutations, P(4, 2), and the number of 2-combinations,
⎛ 4 ⎞
⎜ 2 ⎟, and solve this equation for
⎛ 4 ⎞
⎜ 2 ⎟.
⎝   ⎠
⎝   ⎠

### Solution
According to Theorem 9.2.3, the number of 2-permutations of the set {0, 1, 2, 3} is P(4, 2), which equals

4 · 3 · 2· 1   4!
------------- = --- = 12.
(4 − 2)!      2· 1

Now the act of constructing a 2-permutation of {0, 1, 2, 3} can be thought of as a two-step process:

Step 1: Choose a subset of two elements from {0, 1, 2, 3}.
Step 2: Choose an ordering for the two-element subset.

This process can be illustrated by the possibility tree shown in Figure 9.5.1.

Step 1: Write the 2-combinations
of {0, 1, 2, 3}.
{0, 1}

Step 2: Order the 2-combinations
to obtain 2-permutations.
01
10

{0, 2}

02
20

Start

{0, 3}

03

{1, 2}

30
12
21

{1, 3}

13
31

{2, 3}

23
32

Figure 9.5.1 Relation between Permutations and Combinations

The number of ways to perform step 1 is
⎛ 4 ⎞
⎜ 2 ⎟, the same as the number of subsets of size 2 that can be chosen from {0, 1, 2, 3}. The number of ways to perform step 2 is 2!, the
⎝   ⎠

number of ways to order the elements in a subset of size 2. Because the number of ways of performing the whole process is the number of 2-permutations of the set {0, 1, 2, 3}, which equals P(4, 2), it follows from the product rule that

⎛ 4 ⎞
P(4, 2) = ⎜ 2 ⎟ · 2!.
⎝   ⎠

This is an equation that relates P(4, 2) and
⎛ 4 ⎞
⎜ 2 ⎟. Solving the equation for
⎛ 4 ⎞
⎜ 2 ⎟ gives
⎝   ⎠
⎝   ⎠

⎛ 4 ⎞   P(4, 2)    4!
⎜ 2 ⎟ = -------- = --- = 6.
⎝   ⎠     2!       2

Recall that P(4, 2) =
4!
---. Hence, substituting yields
(4 − 2)!

⎛ 4 ⎞   4!      4!
⎜ 2 ⎟ = -------- = --- = 6.
⎝   ⎠   2!(4 − 2)!   2· 2

The reasoning used in Example 9.5.3 applies in the general case as well. To form an r-permutation of a set of n elements, first choose a subset of r of the n elements (there are
⎛ n ⎞
⎜ r ⎟ ways to perform this step), and then choose an ordering for the r elements (there
⎝   ⎠

are r ! ways to perform this step). Thus the number of r-permutations is

⎛ n ⎞
P(n, r) = ⎜ r ⎟ · r !.
⎝   ⎠

Now solve for
⎛ n ⎞
⎜ r ⎟ to obtain the formula
⎝   ⎠

⎛ n ⎞   P(n, r)
⎜ r ⎟ = --------.
⎝   ⎠     r !

n!
Since P(n, r) = ---------, substitution gives
(n−r)!

⎛ n ⎞   n!      n!
⎜ r ⎟ = -------- = ---------.
⎝   ⎠   r!      r !(n − r)!

The result of this discussion is summarized and extended in Theorem 9.5.1.

## Theorem 9.5.1
The number of subsets of size r (or r-combinations) that can be chosen from a set of n elements,
⎛ n ⎞
⎜ r ⎟, is given by the formula
⎝   ⎠

⎛ n ⎞   P(n, r)
⎜ r ⎟ = --------                    first version
⎝   ⎠     r !

or, equivalently,

⎛ n ⎞   n!
⎜ r ⎟ = ---------                    second version
⎝   ⎠   r !(n − r)!

where n and r are nonnegative integers with r ≤ n.

Note that the analysis presented before the theorem proves the theorem in all cases where n and r are positive. If r is zero and n is any nonnegative integer, then
⎛ n ⎞
⎜ 0 ⎟ is the number of subsets of size zero of a set with n elements. But you know from Section 6.2 that there is only one set that does not have any elements. Consequently,
⎝   ⎠

⎛ n ⎞
⎜ 0 ⎟ = 1. Also
n!
----- = 1 since 0! = 1 by definition. (Remember we said that definition would turn out to be convenient!) Hence the formula
⎝   ⎠
0!(n − 0)!

⎛ n ⎞   n!
⎜ 0 ⎟ = ----- holds for all integers n ≥ 0, and so the theorem is true for all nonnegative integers n and r with r ≤ n.
⎝   ⎠
0!(n − 0)!

## Example 9.5.4 Calculating the Number of Teams
Consider again the problem of choosing five members from a group of twelve to work as a team on a special project. How many distinct five-person teams can be chosen?

### Solution
The number of distinct five-person teams is the same as the number of subsets of size 5 (or 5-combinations) that can be chosen from the set of twelve. This number is
⎛ 12 ⎞
⎜  5 ⎟. By Theorem 9.5.1,
⎝    ⎠

⎛ 12 ⎞   12!         12· 11· 10· 9 · 8 · 7!         12· 11· 9 ·8
⎜  5 ⎟ = -------- = ------------------------ = 11· 9 ·8 = 792.
⎝    ⎠   5!(12 − 5)!   (5· 4· 3· 2· 1) · 7!

Thus there are 792 distinct five-person teams.

The formula for the number of r-combinations of a set can be applied in a wide variety of situations. Some of these are illustrated in the following examples.

## Example 9.5.5 Teams That Contain Both or Neither
Suppose two members of the group of twelve insist on working as a pair—any team must contain either both or neither. How many five-person teams can be formed?

### Solution
Call the two members of the group that insist on working as a pair A and B. Then any team formed must contain both A and B or neither A nor B. The set of all possible teams can be partitioned into two subsets as shown in Figure 9.5.2 on the next page.

Because a team that contains both A and B contains exactly three other people from the remaining ten in the group, there are as many such teams as there are subsets of three people that can be chosen from the remaining ten. By Theorem 9.5.1, this number is

⎛ 10 ⎞   10!         10 · 9 · 8 · 7!
⎜  3 ⎟ = -------- = ------------------ = 120.
⎝    ⎠   3! ·7!      3· 2·1·7!

Because a team that contains neither A nor B contains exactly five people from the remaining ten, there are as many such teams as there are subsets of five people that can be chosen from the remaining ten. By Theorem 9.5.1, this number is

⎛ 10 ⎞   10!         10· 9 · 8· 7 · 6· 5!
⎜  5 ⎟ = -------- = ------------------------ = 252.
⎝    ⎠   5! · 5!      5· 4 · 3 · 2· 1·5!

Because the set of teams that contain both A and B is disjoint from the set of teams that contain neither A nor B, by the addition rule,

⎡ number of teams ⎤   ⎡ number of teams ⎤   ⎡ number of teams ⎤
⎣containing both  ⎦ + ⎣containing       ⎦ = ⎣containing both  ⎦
A and B or neither    neither A nor B        A and B
A nor B

= 120 + 252 = 372.

This reasoning is summarized in Figure 9.5.2.

All Possible Five-Person Teams
Containing Both or Neither

teams with
both A and B

teams with
neither A nor B

⎛ 10 ⎞
⎜  3 ⎟ = 120 of these.
⎝    ⎠

⎛ 10 ⎞
⎜  5 ⎟ = 252 of these.
⎝    ⎠

So the total number of teams
that contain either both A and B
or neither A nor B is
120 + 252 = 372.

Figure 9.5.2

## Example 9.5.6 Teams That Do Not Contain Both
Suppose two members of the group don't get along and refuse to work together on a team. How many five-person teams can be formed?

### Solution
Call the two people who refuse to work together C and D. There are two different ways to answer the given question: One uses the addition rule and the other uses the difference rule.

To use the addition rule, partition the set of all teams that don't contain both C and D into three subsets as shown in Figure 9.5.3 on the next page.

Because any team that contains C but not D contains exactly four other people from the remaining ten in the group, by Theorem 9.5.1 the number of such teams is

⎛ 10 ⎞   10!         10 · 9 · 8 · 7 · 6!
⎜  4 ⎟ = -------- = ------------------ = 210.
⎝    ⎠   4!(10 − 4)!   4 · 3 · 2· 1· 6!

Similarly, there are
⎛ 10 ⎞
⎜  4 ⎟ = 210 teams that contain D but not C. Finally, by the same reasoning as in Example 9.5.5, there are 252 teams that contain neither C nor D. Thus, by the addition rule,
⎝    ⎠

*
number of teams that do    +
+
not contain both C and D
= 210 + 210 + 252 = 672.

This reasoning is summarized in Figure 9.5.3.

All Possible Five-Person Teams
That Do Not Contain Both C and D

teams that
contain C
but not D

teams that
contain D
but not C

teams that
contain neither
C nor D

⎛ 10 ⎞
⎜  4 ⎟ = 210 of these.
⎝    ⎠

⎛ 10 ⎞
⎜  4 ⎟ = 210 of these.
⎝    ⎠

⎛ 10 ⎞
⎜  5 ⎟ = 252 of these.
⎝    ⎠

So the total number of teams that
do not contain both C and D is
210 + 210 + 252 = 672.

Figure 9.5.3

The alternative solution by the difference rule is based on the following observation: The set of all five-person teams that don't contain both C and D equals the set difference between the set of all five-person teams and the set of all five-person teams that contain both C and D. By Example 9.5.4, the total number of five-person teams is
⎛ 12 ⎞
⎜  5 ⎟ = 792. Thus, by the difference rule,
⎝    ⎠

*
number of teams that don't    +
+
contain both C and D
= total number of teams of five − number of teams that contain both C and D

⎛ 12 ⎞   ⎛ 10 ⎞
= ⎜  5 ⎟ − ⎜  3 ⎟ = 792 − 120 = 672.
⎝    ⎠   ⎝    ⎠

This reasoning is summarized in Figure 9.5.4.

There are
All Five-Person Teams

teams that do
not contain
both C and D

teams that
contain
both C and D

So there are
792 – 120 = 672 of these.

⎛ 10 ⎞
⎜  3 ⎟ = 120 of these.
⎝    ⎠

⎛ 12 ⎞
⎜  5 ⎟ = 792 of these.
⎝    ⎠

Figure 9.5.4

Before we begin the next example, a remark on the phrases at least and at most is in order:
The phrase "at least n" means "n or more."
The phrase "at most n" means "n or fewer."

For instance, if a set consists of three elements and you are to choose at least two, you will choose two or three; if you are to choose at most two, you will choose none, or one, or two.

## Example 9.5.7 Teams with Members of Two Types
Suppose the group of twelve consists of five men and seven women.
a. How many five-person teams can be chosen that consist of three men and two women?
b. How many five-person teams contain at least one man?
c. How many five-person teams contain at most one man?

### Solution
a. To answer this question, think of forming a team as a two-step process:
Step 1: Choose the men.
Step 2: Choose the women.

⎛ 5 ⎞   ⎛ 7 ⎞
There are ⎜ 3 ⎟ ways to choose the three men out of the five and ⎜ 2 ⎟ ways to choose the two women out of the seven. Hence, by the product rule,
⎝   ⎠   ⎝   ⎠

*
number of teams of five    +
+
that contain three men and two women
⎛ 5 ⎞⎛ 7 ⎞   5! 7!   5· 4· 3!· 7 · 6· 5· 4· 3· 2· 1
= ⎜ 3 ⎟⎜ 2 ⎟ = · · = ----------------------------------
⎝   ⎠⎝   ⎠   3!2! 2!5!      3· 2· 1 · 2· 1 · 2· 1

5 · 4 · 3!· 7 · 6· 5!
= --------------------- = 210.
3! · 2· 4!· 3 ·2

b. This question can also be answered either by the addition rule or by the difference rule. The solution by the difference rule is shorter and is shown first.

Observe that the set of five-person teams containing at least one man equals the set difference between the set of all five-person teams and the set of five-person teams that do not contain any men. See Figure 9.5.5 below.

Now a team with no men consists entirely of five women chosen from the seven women in the group, so there are
⎛ 7 ⎞
⎜ 5 ⎟ = 21 such teams. Also, by Example 9.5.4, the total number of five-person teams is
⎛ 12 ⎞
⎜  5 ⎟ = 792. Hence, by the difference rule,
⎝    ⎠
⎝   ⎠

⎡
⎤ ⎡
⎤ ⎡
⎤
number of teams
total number
number of teams
⎣with at least
⎦ = ⎣of teams
⎦ − ⎣of five that do not⎦
one man
of five
contain any men

⎛ 12 ⎞   ⎛ 7 ⎞
7· 6· 5!
= ⎜  5 ⎟ − ⎜ 5 ⎟ = 792 − -------- = 792 − 21 = 771.
⎝    ⎠   ⎝   ⎠   5! · 2· 1

This reasoning is summarized in Figure 9.5.5.

All Five-Person Teams

teams that
contain at
least one man

teams that
contain no men

So there are
792 – 21 = 771 of these.

⎛ 7 ⎞
⎜ 5 ⎟ = 21 of these.
⎝   ⎠

There are
⎛ 12 ⎞
⎜  5 ⎟ = 792 of these.
⎝    ⎠

Figure 9.5.5

Alternatively, to use the addition rule, observe that the set of teams containing at least one man can be partitioned as shown in Figure 9.5.6. The number of teams in each subset of the partition is calculated using the method illustrated in part (a).

There are
⎛ 5 ⎞⎛ 7 ⎞
⎜ 1 ⎟⎜ 4 ⎟ teams with one man and four women
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 2 ⎟⎜ 3 ⎟ teams with two men and three women
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 3 ⎟⎜ 2 ⎟ teams with three men and two women
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 4 ⎟⎜ 1 ⎟ teams with four men and one woman
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 5 ⎟⎜ 0 ⎟ teams with five men and no women.
⎝   ⎠⎝   ⎠

Hence, by the addition rule,

*
number of teams with
+
at least one man
⎛ 5 ⎞⎛ 7 ⎞   ⎛ 5 ⎞⎛ 7 ⎞   ⎛ 5 ⎞⎛ 7 ⎞   ⎛ 5 ⎞⎛ 7 ⎞   ⎛ 5 ⎞⎛ 7 ⎞
= ⎜ 1 ⎟⎜ 4 ⎟ + ⎜ 2 ⎟⎜ 3 ⎟ + ⎜ 3 ⎟⎜ 2 ⎟ + ⎜ 4 ⎟⎜ 1 ⎟ + ⎜ 5 ⎟⎜ 0 ⎟
⎝   ⎠⎝   ⎠   ⎝   ⎠⎝   ⎠   ⎝   ⎠⎝   ⎠   ⎝   ⎠⎝   ⎠   ⎝   ⎠⎝   ⎠

5! 7!   5! 7!   5! 7!   5! 7!   5! 7!
= · + · + · + · + ·
1!4! 4!3! 2!3! 3!4! 3!2! 2!5! 4!1! 1!6! 5!0! 0!7!

5 · 4 · 3!· 7 · 6· 5 · 4!   5 · 4 · 3!· 7 · 6· 5!
= ----------------------- + ---------------------
4! · 3 · 2· 4!              3! · 2· 4!· 3 ·2

5· 4!· 7 · 6· 5 · 4!   5 · 4!· 7 · 6!   5! · 7!
+ --------------------- + -------------- + --------
2· 3!· 5!· 2            4! · 6!        5! · 7!

= 175 + 350 + 210 + 35 + 1 = 771.

This reasoning is summarized in Figure 9.5.6.

Teams with At Least One Man

teams with
one man

teams with
two men

teams with
three men

teams with
four men

teams with
five men

⎛ 5 ⎞⎛ 7 ⎞
⎜ 1 ⎟⎜ 4 ⎟ = 175
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 2 ⎟⎜ 3 ⎟ = 350
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 3 ⎟⎜ 2 ⎟ = 210
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 4 ⎟⎜ 1 ⎟ = 35
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 5 ⎟⎜ 0 ⎟ = 1
⎝   ⎠⎝   ⎠

So the total number of
teams with at least
one man is
175 + 350 + 210 + 35 + 1 = 771.

Figure 9.5.6

c. As shown in Figure 9.5.7 on the next page, the set of teams containing at most one man can be partitioned into the set that does not contain any men and the set that contains exactly one man. Hence, by the addition rule,

⎡
⎤ ⎡
⎤ ⎡
⎤
number of teams
number of
number of
⎣with at
⎦ = ⎣teams without⎦ + ⎣teams with⎦
most one man
any men
one man

⎛ 5 ⎞⎛ 7 ⎞   ⎛ 5 ⎞⎛ 7 ⎞
= ⎜ 0 ⎟⎜ 5 ⎟ + ⎜ 1 ⎟⎜ 4 ⎟ = 21 + 175 = 196.
⎝   ⎠⎝   ⎠   ⎝   ⎠⎝   ⎠

This reasoning is summarized in Figure 9.5.7.

Teams with At Most One Man

teams without
any men

teams with
one man

⎛ 5 ⎞⎛ 7 ⎞
⎜ 0 ⎟⎜ 5 ⎟ = 21
⎝   ⎠⎝   ⎠

⎛ 5 ⎞⎛ 7 ⎞
⎜ 1 ⎟⎜ 4 ⎟ = 175
⎝   ⎠⎝   ⎠

So the total number of
teams with at most one
man is 21 + 175 = 196.

Figure 9.5.7

## Example 9.5.8 Poker Hand Problems
The game of poker is played with an ordinary deck of cards (see Example 9.1.1). Various five-card holdings are given special names, and certain holdings beat certain other holdings. The named holdings are listed from highest to lowest below.

Royal flush: 10, J, Q, K, A of the same suit
Straight flush: five adjacent denominations of the same suit but not a royal flush—aces can be high or low, so A, 2, 3, 4, 5 of the same suit is a straight flush.
Four of a kind: four cards of one denomination—the fifth card can be any other in the deck
Full house: three cards of one denomination, two cards of another denomination
Flush: five cards of the same suit but not a straight or a royal flush
Straight: five cards of adjacent denominations but not all of the same suit—aces can be high or low
Three of a kind: three cards of the same denomination and two other cards of different denominations
Two pairs: two cards of one denomination, two cards of a second denomination, and a fifth card of a third denomination
One pair: two cards of one denomination and three other cards all of different denominations
No pairs: all cards of different denominations but not a straight or straight flush or flush

a. How many five-card poker hands contain two pairs?
b. If a five-card hand is dealt at random from an ordinary deck of cards, what is the probability that the hand contains two pairs?

### Solution
a. Consider forming a hand with two pairs as a four-step process:
Step 1: Choose the two denominations for the pairs.
Step 2: Choose two cards from the smaller denomination.
Step 3: Choose two cards from the larger denomination.
Step 4: Choose one card from those remaining.

⎛ 13 ⎞
The number of ways to perform step 1 is ⎜  2 ⎟ because there are 13 denominations in all. The number of ways to perform steps 2 and 3 is
⎛ 4 ⎞
⎜ 2 ⎟ because there are four cards of each denomination, one in each suit. The number of ways to perform step 4 is
⎛ 44 ⎞
⎜  1 ⎟ because the fifth card is chosen from the eleven denominations not included in the pair and there are four cards of each denomination. Thus
⎝    ⎠

*
the total number of    +
+
hands with two pairs
⎛ 13 ⎞⎛ 4 ⎞⎛ 4 ⎞⎛ 44 ⎞
= ⎜  2 ⎟⎜ 2 ⎟⎜ 2 ⎟⎜  1 ⎟
⎝    ⎠⎝   ⎠⎝   ⎠⎝    ⎠

13!
4!
4!
44!
= · · ·
2!(13 − 2)! 2!(4 − 2)! 2!(4 − 2)! 1!(44 − 1)!

13· 12· 11! 4 · 3 · 2! 4 ·3 · 2! 44· 43!
= · · ·
(2 · 1) · 11! (2 · 1) · 2! (2 · 1) · 2! 1 · 43!

= 78· 6 · 6· 44 = 123,552.

⎛ 52 ⎞
b. The total number of five-card hands from an ordinary deck of cards is ⎜  5 ⎟ = 2,598,960. Thus if all hands are equally likely, the probability of obtaining a hand with two pairs
⎝    ⎠

123,552
is ---------- = 4.75%.
2,598,960

## Example 9.5.9 Number of Bit Strings with Fixed Number of 1's
How many eight-bit strings have exactly three 1's?

### Solution
To solve this problem, imagine eight empty positions into which the 0's and 1's of the bit string will be placed. In step 1, choose positions for the three 1's, and in step 2, put the 0's into place.

Three 1's and
five 0's to be
put into the
positions

1

2

3

4

5

6

7

8

Once a subset of three positions has been chosen from the eight to contain 1's, then the remaining five positions must all contain 0's (since the string is to have exactly three 1's). It follows that the number of ways to construct an eight-bit string with exactly three 1's is the same as the number of subsets of three positions that can be chosen from the eight into which to place the 1's. By Theorem 9.5.1, this equals

⎛ 8 ⎞   8!         8· 7 ·6· 5!
⎜ 3 ⎟ = -------- = --------------- = 56.
⎝   ⎠   3! ·5!      3 · 2 · 5!

## Example 9.5.10 Permutations of a Set with Repeated Elements
Consider various ways of ordering the letters in the word MISSISSIPPI:
IIMSSPISSIP, ISSSPMIIPIS, PIMISSSSIIP, and so on.

How many distinguishable orderings are there?

### Solution
This example generalizes Example 9.5.9. Imagine placing the 11 letters of MISSISSIPPI one after another into 11 positions.

Letters of
MISSISSIPPI
to be placed
into the
positions

1

2

3

4

5

6

7

8

9

10

11

Because copies of the same letter cannot be distinguished from one another, once the positions for a certain letter are known, then all copies of the letter can go into the positions in any order. It follows that constructing an ordering for the letters can be thought of as a four-step process:
Step 1: Choose a subset of four positions for the S's.
Step 2: Choose a subset of four positions for the I 's.
Step 3: Choose a subset of two positions for the P's.
Step 4: Choose a subset of one position for the M.

⎛ 11 ⎞
Since there are 11 positions in all, there are ⎜  4 ⎟ subsets of four positions for the S's. Once the four S's are in place, there are seven positions that remain empty, so there are
⎝    ⎠

⎛ 7 ⎞
⎜ 4 ⎟ subsets of four positions for the I 's. After the I 's are in place, there are three positions left empty, so there are
⎛ 3 ⎞
⎜ 2 ⎟ subsets of two positions for the P's. That leaves just one position for the M. But
⎛ 1 ⎞
⎜ 1 ⎟ = 1. Hence by the multiplication rule,
⎝   ⎠
⎝   ⎠

*
number of ways to    +
+
position all the letters
⎛ 11 ⎞⎛ 7 ⎞⎛ 3 ⎞⎛ 1 ⎞
= ⎜  4 ⎟⎜ 4 ⎟⎜ 2 ⎟⎜ 1 ⎟
⎝    ⎠⎝   ⎠⎝   ⎠⎝   ⎠

11! 7! 3! 1!
= · · ·
4!7! 4!3! 2!1! 1!0!

11!
= --------- = 34,650.
4! ·4! · 2! ·1!

In exercise 18 at the end of the section, you are asked to show that changing the order in which the letters are placed into the positions does not change the answer to this example.

The same reasoning used in this example can be used to derive the following general theorem.

## Theorem 9.5.2 Permutations with sets of Indistinguishable Objects
Suppose a collection consists of n objects of which
n 1 are of type 1 and are indistinguishable from each other
n 2 are of type 2 and are indistinguishable from each other
..
.
n k are of type k and are indistinguishable from each other,
and suppose that n 1 + n 2 + · · · + n k = n. Then the number of distinguishable permutations of the n objects is

⎛   ⎞⎛       ⎞⎛             ⎞⎛                       ⎞
⎜ n  ⎟⎛ n − n 1 ⎞⎛ n − n 1 − n 2 ⎞⎛ n − n 1 − n 2 − · · · − n k−1 ⎞
⎜  1 ⎟⎜       2 ⎟⎜           3 ⎟⎜                         k ⎟
⎜    ⎟⎜       ⎟⎜           ⎟⎜                         ⎟
⎝    ⎠⎝       ⎠⎝           ⎠⎝                         ⎠

n!
= ----------.
n 1! n 2! n 3! · · · n k !

## Some Advice about Counting
Students learning counting techniques often ask, "How do I know what to multiply and what to add? When do I use the multiplication rule and when do I use the addition rule?" Unfortunately, these questions have no easy answers. You need to imagine, as vividly as possible, the objects you are to count. You might even start to make an actual list of the items you are trying to count to get a sense for how to obtain them in a systematic way. You should then construct a model that would allow you to continue counting the objects one by one if you had enough time. If you can imagine the elements to be counted as being obtained through a multistep process (in which each step is performed in a fixed number of ways regardless of how preceding steps were performed), then you can use the multiplication rule. The total number of elements will be the product of the number of ways to perform each step. If, however, you can imagine the set of elements to be counted as being broken up into disjoint subsets, then you can use the addition rule. The total number of elements in the set will be the sum of the number of elements in each subset.

One of the most common mistakes students make is to count certain possibilities more than once.

## Example 9.5.11 Double Counting
Consider again the problem of Example 9.5.7(b). A group consists of five men and seven women. How many teams of five contain at least one man?

! Caution! Be careful to
avoid counting items
twice when using the
multiplication rule.

### Incorrect Solution
Imagine constructing the team as a two-step process:
Step 1: Choose a subset of one man from the five men.
Step 2: Choose a subset of four others from the remaining eleven people.

⎛ 5 ⎞⎛ 11 ⎞
Hence, by the multiplication rule, there are ⎜ 1 ⎟⎜  4 ⎟ = 1,650 five-person teams that contain at least one man.
⎝   ⎠⎝    ⎠

### Analysis of the Incorrect Solution
The problem with the solution above is that some teams are counted more than once. Suppose the men are Anwar, Ben, Carlos, Dwayne, and Ed and the women are Fumiko, Gail, Hui-Fan, Inez, Jill, Kim, and Laura. According to the method described previously, one possible outcome of the two-step process is as follows:
Outcome of step 1: Anwar
Outcome of step 2: Ben, Gail, Inez, and Jill.
In this case the team would be {Anwar, Ben, Gail, Inez, Jill}. But another possible outcome is
Outcome of step 1: Ben
Outcome of step 2: Anwar, Gail, Inez, and Jill,
which also gives the team {Anwar, Ben, Gail, Inez, Jill}. Thus this one team is given by two different branches of the possibility tree, and so it is counted twice.

The best way to avoid mistakes such as the one just described is to visualize the possibility tree that corresponds to any use of the multiplication rule and the set partition that corresponds to a use of the addition rule. Check how your division into steps works by applying it to some actual data—as was done in the analysis above—and try to pick data that are as typical or generic as possible.

It often helps to ask yourself (1) "Am I counting everything?" and (2) "Am I counting anything twice?" When using the multiplication rule, these questions become (1) "Does every outcome appear as some branch of the tree?" and (2) "Does any outcome appear on more than one branch of the tree?" When using the addition rule, the questions become (1) "Does every outcome appear in some subset of the diagram?" and (2) "Do any two subsets in the diagram share common elements?"

## The Number of Partitions of a Set into r Subsets

Note Stirling numbers
of the first kind are used
in counting
r -permutations with
various properties.

In an ordinary (or singly indexed) sequence, integers n are associated to numbers an . In a doubly indexed sequence, ordered pairs of integers (m, n) are associated to numbers am,n . For example, combinations can be thought of as terms of the doubly indexed sequence defined by Cn,r =
⎛ n ⎞
⎜ r ⎟ for all integers n and r with 0 ≤ r ≤ n.
⎝   ⎠

An important example of a doubly indexed sequence is the sequence of Stirling numbers of the second kind. These numbers, named after the Scottish mathematician James Stirling (1692–1770), arise in a surprisingly large variety of counting problems. They are defined recursively and can be interpreted in terms of partitions of a set.

Observe that if a set of three elements {x1 , x2 , x3 } is partitioned into two subsets, then one of the subsets has one element and the other has two elements. Therefore, there are three ways the set can be partitioned:
{x1 , x2 }{x3 } put x3 by itself
{x1 , x3 }{x2 } put x2 by itself
{x2 , x3 }{x1 } put x1 by itself

In general, let
Sn,r = number of ways a set of size n
can be partitioned into r subsets

Then, by the above, S3,2 = 3. The numbers Sn,r are called Stirling numbers of the second kind.

## Example 9.5.12 Values of Stirling Numbers
Find S4,1 , S4,2 , S4,3 , and S4,4 .

### Solution
Given a set with four elements, denote it by {x1 , x2 , x3 , x4 }. The Stirling number S4,1 = 1 because a set of four elements can be partitioned into one subset in only one way:

{x1 , x2 , x3 , x4 }.

Similarly, S4,4 = 1 because there is only one way to partition a set of four elements into four subsets:
{x1 }{x2 }{x3 }{x4 }.

The number S4,2 = 7. The reason is that any partition of {x1 , x2 , x3 , x4 } into two subsets must consist either of two subsets of size two or of one subset of size three and one subset of size one. The partitions for which both subsets have size two must pair x1 with x2 , with x3 , or with x4 , which give rise to these three partitions:
{x1 , x2 }{x3 , x4 }  x2 paired with x1
{x1 , x3 }{x2 , x4 }  x3 paired with x1
{x1 , x4 }{x2 , x3 }  x4 paired with x1

The partitions for which one subset has size one and the other has size three can have any one of the four elements in the subset of size one, which leads to these four partitions:
{x1 }{x2 , x3 , x4 }  x1 by itself
{x2 }{x1 , x3 , x4 }  x2 by itself
{x3 }{x1 , x2 , x4 }  x3 by itself
{x4 }{x1 , x2 , x3 }  x4 by itself

It follows that the total number of ways that the set {x1 , x2 , x3 , x4 } can be partitioned into two subsets is 3 + 4 = 7.

Finally, S4,3 = 6 because any partition of a set of four elements into three subsets must have two elements in one subset and the other two elements in subsets by themselves. There are
⎛ 4 ⎞
⎜ 2 ⎟ = 6 ways to choose the two elements to put together, which results in the following six possible partitions:
⎝   ⎠

{x1 , x2 }{x3 }{x4 }
{x1 , x3 }{x2 }{x4 }
{x1 , x4 }{x2 }{x3 }

{x2 , x3 }{x1 }{x4 }
{x2 , x4 }{x1 }{x3 }
{x3 , x4 }{x1 }{x2 }

## Example 9.5.13 Finding a Recurrence Relation for Sn,r
Find a recurrence relation relating Sn,r to values of the sequence with lower indices than n and r, and give initial conditions for the recursion.

### Solution
To solve this problem recursively, suppose a procedure has been found to count both the number of ways to partition a set of n − 1 elements into r − 1 subsets and the number of ways to partition a set of n − 1 elements into r subsets. The partitions of a set of n elements {x1 , x2 , . . . , xn } into r subsets can be divided, as shown in Figure 9.5.8 on the next page, into those that contain the set {xn } and those that do not.

To obtain the result shown in Figure 9.5.8 first count the number of partitions of {x1 , x2 , . . . , xn } into r subsets where one of the subsets is {xn }. To do this, imagine taking any one of the Sn−1, r−1 partitions of {x1 , x2 , . . . , xn−1 } into r − 1 subsets and adding the subset {xn } to the partition. For example, if n = 4 and r = 3, you would take one of the three partitions of {x1 , x2 , x3 } into two subsets, namely
{x1 , x2 }{x3 }, {x1 , x3 }{x2 }, or {x2 , x3 }{x1 }, and add {x4 }. The result would be one of the partitions
{x1 , x2 }{x3 }{x4 }, {x1 , x3 }{x3 }{x4 }, or {x2 , x3 }{x1 }{x4 }.

Clearly, any partition of {x1 , x2 , . . . , xn } into r subsets with {xn } as one of the subsets can be obtained in this way. Hence Sn−1, r−1 is the number of partitions of {x1 , x2 , . . . , xn } into r subsets of which one is {xn }.

Next, count the number of partitions of {x1 , x2 , . . . , xn } into r subsets where {xn } is not one of the subsets of the partition. Imagine taking any one of the Sn−1, r partitions of {x1 , x2 , . . . , xn−1 } into r subsets. Now imagine choosing one of the r subsets of the partition and adding in the element xn . The result is a partition of {x1 , x2 , . . . , xn } into r subsets none of which is the singelton subset {xn }. Since the element xn could have been added to any one of the r subsets of the partition, it follows from the multiplication rule that there are r Sn−1, r partitions of this type. For instance, if n = 4 and r = 3, you would take the (unique) partition of {x1 , x2 , x3 } into three subsets, namely {x1 }{x2 }{x3 }, and add x4 to one of these sets. The result would be one of the partitions
{x1 , x4 }{x2 }{x3 }, {x1 }{x2 , x4 }{x3 }, or {x1 }{x2 }{x3 , x4 }.

↑
↑
↑

x4 is added to {x1 }
x4 is added to {x2 }
x4 is added to {x3 }

Clearly, any partition of {x1 , x2 , . . . , xn } into r subsets, none of which is {xn }, can be obtained in the way described above, for when xn is removed from whatever subset contains it in such a partition, the result is a partition of {x1 , x2 , . . . , xn−1 } into r subsets. Hence r Sn−1, r is the number of partitions of {x1 , x2 , . . . , xn } that do not contain {xn }.

Since any partition of {x1 , x2 , . . . , xn } either contains {xn } or does not,
⎡
⎤ ⎡
⎤ ⎡
⎤
the number of partitions of
the number of partitions
⎣ {x1 , x2 , . . . , xn } ⎦ = ⎣ {x1 , x2 , . . . , xn } into r subsets ⎦ + ⎣ {x1 , x2 , . . . , xn } into r subsets ⎦
into r subsets
of which {xn } is one
none of which is {xn }

Thus
Sn,r = Sn−1, r−1 + r Sn−1, r
for all integers n and r with 1 < r < n.

The initial conditions for the recurrence relation are
Sn,1 = 1 and Sn,n = 1 for all integers n ≥ 1

because there is only one way to partition {x1 , x2 , . . . , xn } into one subset, namely
{x1 , x2 , . . . , xn }.
and only one way to partition {x1 , x2 , . . . , xn } into n subsets, namely
{x1 }, {x2 }, . . . , {xn }.

## Test Yourself
1. The number of subsets of size r that can be formed from a set with n elements is denoted _____, which is read as "_____."

2. The number of r -combinations of a set of n elements is _____.

3. Two unordered selections are said to be the same if the elements chosen are the same, regardless of _____.

4. A formula relating
⎛ n ⎞
⎜ r ⎟ and P(n, r ) is _____.
⎝   ⎠

5. The phrase "at least n" means _____, and the phrase "at most n" means _____.

6. Suppose a collection consists of n objects of which, for each i with 1 ≤ i ≤ k, n i are of type i and are indistinguishable from each other. Also suppose that n = n 1 + n 2 + · · · + n k . Then the number of distinct permutations of the n objects is _____.

7. The Stirling number of the second kind, Sn,r , can be interpreted as _____.

8. Because any partition of a set X = {x1 , x2 , . . . , xn } either contains {xn } or does not, the number of partitions of X into r subsets equals _____ plus _____.

## Exercise Set 9.5

1. a. List all 2-combinations for the set {x1 , x2 , x3 }. Deduce the value of
⎛ 3 ⎞
⎜ 2 ⎟.
⎝   ⎠

b. List all unordered selections of four elements from the set {a, b, c, d, e}. Deduce the value of
⎛ 5 ⎞
⎜ 4 ⎟.
⎝   ⎠

2. a. List all 3-combinations for the set {x1 , x2 , x3 , x4 , x5 }. Deduce the value of
⎛ 5 ⎞
⎜ 3 ⎟.
⎝   ⎠

b. List all unordered selections of two elements from the set {x1 , x2 , x3 , x4 , x5 , x6 }. Deduce the value of
⎛ 6 ⎞
⎜ 2 ⎟.
⎝   ⎠

3. Write an equation relating P(7, 2) and
⎛ 7 ⎞
⎜ 2 ⎟.
⎝   ⎠

4. Write an equation relating P(8, 3) and
⎛ 8 ⎞
⎜ 3 ⎟.
⎝   ⎠

5. Use Theorem 9.5.1 to compute each of the following.
a.
⎛ 6 ⎞
⎜ 3 ⎟
⎝   ⎠

b.
⎛ 6 ⎞
⎜ 0 ⎟
⎝   ⎠

c.
⎛ 6 ⎞
⎜ 1 ⎟
⎝   ⎠

d.
⎛ 6 ⎞
⎜ 4 ⎟
⎝   ⎠

e.
⎛ 6 ⎞
⎜ 2 ⎟
⎝   ⎠

f.
⎛ 6 ⎞
⎜ 5 ⎟
⎝   ⎠

g.
⎛ 6 ⎞
⎜ 6 ⎟
⎝   ⎠

6. A student council consists of 15 students.
a. In how many ways can a committee of six be selected from the membership of the council?
b. Two council members have the same major and are not permitted to serve together on a committee. How many ways can a committee of six be selected from the membership of the council?
c. Two council members always insist on serving on committees together. If they can't serve together, they won't serve at all. How many ways can a committee of six be selected from the council membership?
d. Suppose the council contains eight men and seven women.
(i) How many committees of six contain three men and three women?
(ii) How many committees of six contain at least one woman?
e. Suppose the council consists of three freshmen, four sophomores, three juniors, and five seniors. How many committees of eight contain two representatives from each class?

7. A computer programming team has 13 members.
a. How many ways can a group of seven be chosen to work on a project?
b. Suppose seven team members are women and six are men.
(i) How many groups of seven can be chosen that contain four women and three men?
(ii) How many groups of seven can be chosen that contain at least one man?
(iii) How many groups of seven can be chosen that contain at most three women?
c. Suppose two team members refuse to work together on projects. How many groups of seven can be chosen to work on a project?
d. Suppose two team members insist on either working together or not at all on projects. How many groups of seven can be chosen to work on a project?

8. An instructor gives an exam with fourteen questions. Students are allowed to choose any ten to answer.
a. How many different choices of ten questions are there?
b. Suppose six questions require proof and eight do not.
(i) How many groups of ten questions contain four that require proof and six that do not?
(ii) How many groups of ten questions contain at least one that requires proof?
(iii) How many groups of ten questions contain at most three that require proof?
c. Suppose the exam instructions specify that at most one of questions 1 and 2 may be included among the ten. How many different choices of ten questions are there?
d. Suppose the exam instructions specify that either both questions 1 and 2 are to be included among the ten or neither is to be included. How many different choices of ten questions are there?

9. A club is considering changing its bylaws. In an initial straw vote on the issue, 24 of the 40 members of the club favored the change and 16 did not. A committee of six is to be chosen from the 40 club members to devote further study to the issue.
a. How many committees of six can be formed from the club membership?
b. How many of the committees will contain at least three club members who, in the preliminary survey, favored the change in the bylaws?

10. Two new drugs are to be tested using a group of 60 laboratory mice, each tagged with a number for identification purposes. Drug A is to be given to 22 mice, drug B is to be given to another 22 mice, and the remaining 16 mice are to be used as controls. How many ways can the assignment of treatments to mice be made? (A single assignment involves specifying the treatment for each mouse—whether drug A, drug B, or no drug.)

11. Refer to Example 9.5.8. For each poker holding below, (1) find the number of five-card poker hands with that holding; (2) find the probability that a randomly chosen set of five cards has that holding.
a. royal flush
b. straight flush
c. four of a kind
d. full house
e. flush
f. straight
g. three of a kind
h. one pair
i. neither a repeated denomination nor five of the same suit nor five adjacent denominations

12. How many pairs of two distinct integers chosen from the set {1, 2, 3, . . . , 101} have a sum that is even?

13. A coin is tossed ten times. In each case the outcome H (for heads) or T (for tails) is recorded. (One possible outcome of the ten tossings is denoted T H H T T T H T T H .)
a. What is the total number of possible outcomes of the coin-tossing experiment?
b. In how many of the possible outcomes are exactly five heads obtained?
c. In how many of the possible outcomes are at least eight heads obtained?
d. In how many of the possible outcomes is at least one head obtained?
e. In how many of the possible outcomes is at most one head obtained?

14. a. How many 16-bit strings contain exactly seven 1's?
b. How many 16-bit strings contain at least thirteen 1's?
c. How many 16-bit strings contain at least one 1?
d. How many 16-bit strings contain at most one 1?

15. a. How many even integers are in the set {1, 2, 3, . . . , 100}?
b. How many odd integers are in the set {1, 2, 3, . . . , 100}?
c. How many ways can two integers be selected from the set {1, 2, 3, . . . , 100} so that their sum is even?
d. How many ways can two integers be selected from the set {1, 2, 3, . . . , 100} so that their sum is odd?

16. Suppose that three computer boards in a production run of forty are defective. A sample of five is to be selected to be checked for defects.
a. How many different samples can be chosen?
b. How many samples will contain at least one defective board?
c. What is the probability that a randomly chosen sample of five contains at least one defective board?

17. Ten points labeled A, B, C, D, E, F, G, H, I, J are arranged in a plane in such a way that no three lie on the same straight line.
a. How many straight lines are determined by the ten points?
b. How many of these straight lines do not pass through point A?
c. How many triangles have three of the ten points as vertices?
d. How many of these triangles do not have A as a vertex?

18. Suppose that you placed the letters in Example 9.5.10 into positions in the following order: first the M, then the I 's, then the S's, and then the P's. Show that you would obtain the same answer for the number of distinguishable orderings.

19. a. How many distinguishable ways can the letters of the word HULLABALOO be arranged in order?
b. How many distinguishable orderings of the letters of HULLABALOO begin with U and end with L?
c. How many distinguishable orderings of the letters of HULLABALOO contain the two letters HU next to each other in order?

20. a. How many distinguishable ways can the letters of the word MILLIMICRON be arranged in order?
b. How many distinguishable orderings of the letters of MILLIMICRON begin with M and end with N ?
c. How many distinguishable orderings of the letters of MILLIMICRON contain the letters C R next to each other in order and also the letters ON next to each other in order?

21. In Morse code, symbols are represented by variable-length sequences of dots and dashes. (For example, A = · −, 1 = · − − − −, ? = · · − − · · .) How many different symbols can be represented by sequences of seven or fewer dots and dashes?

22. Each symbol in the Braille code is represented by a rectangular arrangement of six dots, each of which may be raised or flat against a smooth background. For instance, when the word Braille is spelled out, it looks like this:

·· ·· ··
·· ·· ··
·· ·· ··
·· ·· ··
·· ·· ··
·· ·· ··

Given that at least one of the six dots must be raised, how many symbols can be represented in the Braille code?

23. On an 8 × 8 chessboard, a rook is allowed to move any number of squares either horizontally or vertically. How many different paths can a rook follow from the bottom-left square of the board to the top-right square of the board if all moves are to the right or upward?

24. The number 42 has the prime factorization 2 · 3 · 7. Thus 42 can be written in four ways as a product of two positive integer factors (without regard to the order of the factors): 1 · 42, 2 · 21, 3 · 14, and 6 · 7. Answer a–d below with out regard to the order of the factors.
a. List the distinct ways the number 210 can be written as a product of two positive integer factors.
b. If n = p1 p2 p3 p4 , where the pi are distinct prime numbers, how many ways can n be written as a product of two positive integer factors?
c. If n = p1 p2 p3 p4 p5 , where the pi are distinct prime numbers, how many ways can n be written as a product of two positive integer factors?
d. If n = p1 p2 · · · pk , where the pi are distinct prime numbers, how many ways can n be written as a product of two positive integer factors?

25. a. How many one-to-one functions are there from a set with three elements to a set with four elements?
b. How many one-to-one functions are there from a set with three elements to a set with two elements?
c. How many one-to-one functions are there from a set with three elements to a set with three elements?
d. How many one-to-one functions are there from a set with three elements to a set with five elements?
e. How many one-to-one functions are there from a set with m elements to a set with n elements, where m ≤ n?

26. a. How many onto functions are there from a set with three elements to a set with two elements?
b. How many onto functions are there from a set with three elements to a set with five elements?
c. How many onto functions are there from a set with three elements to a set with three elements?
d. How many onto functions are there from a set with four elements to a set with two elements?
e. How many onto functions are there from a set with four elements to a set with three elements?
f. Let cm,n be the number of onto functions from a set of m elements to a set of n elements, where m ≥ n ≥ 1. Find a formula relating cm,n to cm−1,n and cm−1,n−1 .

27. Let A be a set with eight elements.
a. How many relations are there on A?
b. How many relations on A are reflexive?
c. How many relations on A are symmetric?
d. How many relations on A are both reflexive and symmetric?

28. A student council consists of three freshmen, four sophomores, four juniors, and five seniors. How many committees of eight members of the council contain at least one member from each class?

29. An alternative way to derive Theorem 9.5.1 uses the following division rule: Let n and k be integers so that k divides n. If a set consisting of n elements is divided into subsets that each contain k elements, then the number of such subsets is n/k. Explain how Theorem 9.5.1 can be derived using the division rule.

30. Find the error in the following reasoning: "Consider forming a poker hand with two pairs as a five-step process.
Step 1: Choose the denomination of one of the pairs.
Step 2: Choose the two cards of that denomination.
Step 3: Choose the denomination of the other of the pairs.
Step 4: Choose the two cards of that second denomination.
Step 5: Choose the fifth card from the remaining denominations.

⎛ 13 ⎞⎛ 4 ⎞
There are ⎜  1 ⎟ ways to perform step 1, ⎜ 2 ⎟ ways to perform step 2,
⎝    ⎠⎝   ⎠

⎛ 12 ⎞⎛ 4 ⎞
⎜  1 ⎟ ways to perform step 3, ⎜ 2 ⎟ ways to perform step 4, and
⎝    ⎠⎝   ⎠

⎛ 44 ⎞
⎜  1 ⎟ ways to perform step 5. Therefore, the total number of five-card poker hands with two pairs is
⎝    ⎠

13 · 6 · 12 · 6 · 44 = 247,104."

31. Let Pn be the number of partitions of a set with n elements. Show that
⎛ n − 1 ⎞          ⎛ n − 1 ⎞                    ⎛ n − 1 ⎞
Pn = ⎜       ⎟ Pn−1 + ⎜       ⎟ Pn−2 + · · · + ⎜         ⎟ P0
⎝   0   ⎠          ⎝   1   ⎠                    ⎝ n − 1 ⎠
for all integers n ≥ 1.

Exercises 32–38 refer to the sequence of Stirling numbers of the second kind.

32. Find S3,4 by exhibiting all the partitions of {x1 , x2 , x3 , x4 , x5 } into four subsets.

33. Use the values computed in Example 9.5.12 and the recurrence relation and initial conditions found in Example 9.5.13 to compute S5,2 .

34. Use the values computed in Example 9.5.12 and the recurrence relation and initial conditions found in Example 9.5.13 to compute S5,3 .

35. Use the results of exercises 32–34 to find the total number of different partitions of a set with five elements.

36. Use mathematical induction and the recurrence relation found in Example 9.5.13 to prove that for all integers n ≥ 2, Sn,2 = 2n−1 − 1.

37. Use mathematical induction and the recurrence relation found in Example 9.5.13 to prove that for all integers n ≥ 2,
n
⎛      ⎞
⎜      ⎟ 3 4−k Sk,2  − Sn+1,3 .
⎝ k=2  ⎠

38. If X is a set with n elements and Y is a set with m elements, express the number of onto functions from X and Y using Stirling numbers of the second kind. Justify your answer.

## Answers for Test Yourself
1.
⎛ n ⎞
⎜ r ⎟; n choose r  2.
⎛ n ⎞
⎜ r ⎟ (Or: n choose r )  3. the order in which they are chosen  4.
⎛ n ⎞   P(n, r )
⎜ r ⎟ = --------  5. n or more; n or fewer  6.
⎛   ⎞⎛       ⎞⎛             ⎞⎛                       ⎞
⎝   ⎠     r!
⎜ n  ⎟⎛ n − n 1 ⎞⎛ n − n 1 − n 2 ⎞⎛ n − n 1 − n 2 − · · · − n k−1 ⎞
⎜  1 ⎟⎜       2 ⎟⎜           3 ⎟⎜                         k ⎟
⎜    ⎟⎜       ⎟⎜           ⎟⎜                         ⎟
⎝    ⎠⎝       ⎠⎝           ⎠⎝                         ⎠
Or : n !n !n !···n !
1 2 3 k
7. the number of ways a set of size n can be partitioned
into r subsets  8. the number of partitions of X into r subsets of which {xn } is one; the number of partitions of X into r subsets, none
of which is {xn }
