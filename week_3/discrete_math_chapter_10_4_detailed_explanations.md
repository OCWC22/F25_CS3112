# Discrete Mathematics Chapter 10.4 - Detailed Example Explanations

This document provides detailed explanations for every example from Chapter 10.4 of Discrete Mathematics with Applications, following the same format as the detailed explanation for examples in previous chapters.

## Chapter 10.4 Examples

### Example 10.4.1: Showing That Two Graphs Are Isomorphic
Show that the following two graphs are isomorphic.

**Graph G:**
```
    e1     e7
v1 ------ v3
|  \    / |
|   e5   |
|  /    \ |
v2 ------ v4
    e6    e2
    |     |
    e3    e4
    |     |
    v5    (isolated)
```

**Graph G':**
```
    f1     f7
w1 ------ w3
|  \    / |
|   f5   |
|  /    \ |
w2 ------ w4
    f6    f2
    |     |
    f3    f4
    |     |
    w5    (isolated)
```

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: We need to find one-to-one correspondences g: V(G) → V(G') and h: E(G) → E(G') such that for all v ∈ V(G) and e ∈ E(G), v is an endpoint of e if, and only if, g(v) is an endpoint of h(e).

**Step-by-Step Reasoning:**

1. **Identify structural similarities:** Both graphs have 5 vertices and 7 edges. Both have one isolated vertex (v5 in G, w5 in G').

2. **Analyze vertex degrees:** Look at the degrees of vertices to find corresponding vertices:
   - v1 is connected to 4 edges (e1, e5, e7, e4)
   - v2 is connected to 3 edges (e1, e5, e6)
   - v3 is connected to 4 edges (e1, e7, e2, e6)
   - v4 is connected to 3 edges (e2, e6, e3, e4)
   - v5 is isolated (degree 0)

3. **Find the highest degree vertex:** v1 and v3 both have degree 4, so they must correspond to w2 and w4, which have degree 4. The other vertices have degree 3 or 0.

4. **Look for parallel edges:** e2 and e3 both connect the same vertices (v3 and v4), so they are parallel edges. Their images under h must also be parallel edges.

5. **Match vertices systematically:** Start by mapping v1 to w2 (both degree 4). Then look at neighbors of v1: v2, v3, v4. These must map to neighbors of w2: w1, w3, w4.

6. **Continue the mapping:** The solution provides one possible mapping that works.

**Common Mistakes to Avoid:**
- Don't just try to match vertices randomly - look for structural patterns
- Don't forget to check that both vertices AND edges correspond properly
- Don't assume there's only one possible mapping

**Key Insights:**
- Graph isomorphism requires both vertices and edges to correspond
- Look for unique structural features like degree patterns, isolated vertices, or parallel edges
- The mapping must preserve all adjacencies

### Example 10.4.2: Finding Representatives of Isomorphism Classes
Find all nonisomorphic graphs that have two vertices and two edges. In other words, find a collection of representative graphs with two vertices and two edges such that every such graph is isomorphic to one in the collection.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: We need to find all distinct (up to isomorphism) simple graphs with exactly 2 vertices and exactly 2 edges.

**Step-by-Step Reasoning:**

1. **Consider all possible edge configurations:** With 2 vertices and 2 edges, the edges can be placed in several ways:
   - Both edges between the same two vertices (multiedge)
   - One edge between vertices, one loop
   - Two loops on the same vertex
   - Two loops on different vertices

2. **Case 1 - Both edges between vertices:** This creates a graph with two vertices connected by two parallel edges.

3. **Case 2 - One edge between vertices, one loop:** This can be on either vertex (these are isomorphic).

4. **Case 3 - Both edges are loops on same vertex:** This creates one vertex with two loops and one isolated vertex.

5. **Case 4 - Both edges are loops on different vertices:** This creates two vertices each with one loop.

**Common Mistakes to Avoid:**
- Forgetting that multiedges are allowed in general graphs
- Not considering that loops on different vertices create different structures
- Thinking there are only 3 possibilities instead of 4

**Key Insights:**
- There are exactly 4 nonisomorphic graphs with 2 vertices and 2 edges
- Each configuration represents a distinct isomorphism class
- The systematic enumeration considers all possible ways to place the edges

### Example 10.4.3: Showing That Two Graphs Are Not Isomorphic
Show that the following pairs of graphs are not isomorphic by finding an isomorphic invariant that they do not share.

**Pair (a):**
```
G (9 edges)    G' (8 edges)
o---o---o---o   o---o---o
|   |   |   |   |   |   |
o---o---o---o   o---o---o
```

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: For pair (a), show that G and G' are not isomorphic because G has 9 edges while G' has only 8 edges.

**Step-by-Step Reasoning:**

1. **Count the edges in G:** The left graph has 9 edges clearly labeled.

2. **Count the edges in G':** The right graph has only 8 edges.

3. **Apply the invariant:** Number of edges is an isomorphic invariant. If two graphs are isomorphic, they must have the same number of edges.

4. **Conclusion:** Since 9 ≠ 8, the graphs cannot be isomorphic.

**Common Mistakes to Avoid:**
- Not counting edges carefully
- Forgetting that number of edges is a basic invariant
- Trying to use more complex invariants when simple ones suffice

**Key Insights:**
- Basic counting invariants like number of vertices and edges are often the quickest way to show graphs are not isomorphic
- Always check these simple invariants first before looking for more complex ones

**Pair (b):**
```
G (has vertex of degree 4)    G' (no vertex of degree 4)
    o                           o
  / | \                       / | \
o   o   o                   o   o   o
  \ | /                       \ | /
    o                           o
```

**Solution:**
Formal Restatement: For pair (b), show that G and G' are not isomorphic because G has a vertex of degree 4 while G' does not.

**Step-by-Step Reasoning:**

1. **Analyze degrees in G:** The left graph has a central vertex connected to 4 others, so degree 4.

2. **Analyze degrees in G':** The right graph has vertices with degrees at most 3 (the top and bottom vertices have degree 3, others have degree 2).

3. **Apply the invariant:** Having a vertex of degree 4 is an isomorphic invariant.

4. **Conclusion:** Since G has this property but G' does not, they cannot be isomorphic.

**Key Insights:**
- Degree sequences are important isomorphic invariants
- The presence or absence of vertices with specific degrees can distinguish graphs

### Example 10.4.4: Proof of Theorem 10.4.2, Part (3)
Prove that if G is a graph that has a vertex of degree k and G' is isomorphic to G, then G' has a vertex of degree k.

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: If G and G' are isomorphic graphs and G has a vertex v of degree k, then G' has a vertex of degree k.

**Step-by-Step Reasoning:**

1. **Set up the isomorphism:** Since G ≅ G', there exist bijections g: V(G) → V(G') and h: E(G) → E(G') that preserve adjacency.

2. **Consider edges incident to v:** Let e₁, e₂, ..., eₘ be all edges incident to v.

3. **Map to G':** The images h(e₁), h(e₂), ..., h(eₘ) are edges incident to g(v) in G'.

4. **Show no other edges:** There are no other edges incident to g(v) because the isomorphism is bijective and preserves adjacency.

5. **Handle loops:** Show that loops are preserved under the isomorphism.

6. **Conclude degrees are equal:** The degree of g(v) equals the degree of v, which is k.

**Common Mistakes to Avoid:**
- Forgetting to handle loops separately
- Not clearly explaining why h is bijective
- Not showing that adjacency is preserved in both directions

**Key Insights:**
- Isomorphisms preserve all structural properties, including degrees
- The proof technique of following elements through the isomorphism mapping is fundamental
- Loops require special consideration because they contribute 2 to vertex degree

### Example 10.4.5: Isomorphism of Simple Graphs
Are the two graphs shown below isomorphic? If so, define an isomorphism.

**Graph G:**
```
    a
  / | \
 b--c--d
 |  |  |
 e--f--g
```

**Graph G':**
```
    w
  / | \
 x--y--z
 |  |  |
 u--v--t
```

**Solution:**
Begin by asking yourself, "Where am I starting from?" and "What do I need to show?" To help answer these questions, introduce variables to represent the quantities in the statement to be proved.

Formal Restatement: Determine if G and G' are isomorphic simple graphs, and if so, provide a bijection g: V(G) → V(G') such that {u, v} is an edge in G if and only if {g(u), g(v)} is an edge in G'.

**Step-by-Step Reasoning:**

1. **Check basic invariants:** Both graphs have 7 vertices and 9 edges, so this check passes.

2. **Analyze degree sequences:** Both graphs have:
   - 1 vertex of degree 3 (the top vertex)
   - 2 vertices of degree 3 (the middle level)
   - 2 vertices of degree 2 (the bottom level)
   - 2 vertices of degree 2 (the bottom level)

3. **Find the degree 3 vertex:** In both graphs, there's a unique vertex of degree 3 (a and w).

4. **Map systematically:** Start with a → w, then map neighbors based on the structure.

5. **Verify all adjacencies:** The table in the solution shows that all edge pairs are preserved.

**Common Mistakes to Avoid:**
- Not checking that all adjacencies are preserved
- Not verifying the mapping is bijective
- Forgetting to check that the edge sets correspond properly

**Key Insights:**
- For simple graphs, we only need to define the vertex mapping - the edge correspondence follows automatically
- The structure is like two triangles sharing a vertex, creating a diamond shape
- The systematic mapping preserves all adjacencies as shown in the table
