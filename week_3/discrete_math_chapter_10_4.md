# Chapter 10.4: Isomorphisms of Graphs

## Introduction

*Thinking is a momentary dismissal of irrelevancies.*
— R. Buckminster Fuller, 1969

Recall from Example 10.1.3 that the two drawings shown in Figure 10.4.1 both represent the same graph: Their vertex and edge sets are identical, and their edge-endpoint functions are the same. Call this graph G.

```
v1 ---e1--- v2
|      e5    |
e4            e2
|      e3    |
v4 ---e5--- v3
```

Now consider the graph G' represented in Figure 10.4.2.

```
v1 ---e1--- v2
|      e3    |
e4            e2
|      e5    |
v4 ---e6--- v5
```

Observe that G' is a different graph from G (for instance, in G the endpoints of e₁ are v₁ and v₂, whereas in G' the endpoints of e₁ are v₁ and v₃). Yet G' is certainly very similar to G. In fact, if the vertices and edges of G' are relabeled by the functions shown in Figure 10.4.3, then G' becomes the same as G.

**Figure 10.4.3: Relabeling Functions**
```
Vertices of G    Vertices of G'    Edges of G    Edges of G'
v1               v1               e1            e1
v2               v2               e2            e2
v3               v3               e3            e3
v4               v4               e4            e4
v5               v5               e5            e5
```

Note that these relabeling functions are one-to-one and onto.

Two graphs that are the same except for the labeling of their vertices and edges are called isomorphic. The word isomorphism comes from the Greek, meaning "same form." Isomorphic graphs are those that have essentially the same form.

## Definition of Graph Isomorphism

**Definition 10.4.1: Graph Isomorphism**
Let G and G' be graphs with vertex sets V(G) and V(G') and edge sets E(G) and E(G'), respectively. G is isomorphic to G' if, and only if, there exist one-to-one correspondences g: V(G) → V(G') and h: E(G) → E(G') that preserve the edge-endpoint functions of G and G' in the sense that for all v ∈ V(G) and e ∈ E(G),
**v is an endpoint of e ⇔ g(v) is an endpoint of h(e).**

In words, G is isomorphic to G' if, and only if, the vertices and edges of G and G' can be matched up by one-to-one, onto functions such that the edges between corresponding vertices correspond to each other.

It is common in mathematics to identify objects that are isomorphic. For instance, if we are given a graph G with five vertices such that each pair of vertices is connected by an edge, then we may identify G with K₅, saying that G is K₅ rather than that G is isomorphic to K₅.

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
To solve this problem, you must find functions g: V(G) → V(G') and h: E(G) → E(G') such that for all v ∈ V(G) and e ∈ E(G), v is an endpoint of e if, and only if, g(v) is an endpoint of h(e). Setting up such functions is partly a matter of trial and error and partly a matter of deduction. For instance, since e₂ and e₃ are parallel (have the same endpoints), h(e₂) and h(e₃) must be parallel also. So h(e₂) = f₁ and h(e₃) = f₂ or h(e₂) = f₂ and h(e₃) = f₁. Also, the endpoints of e₂ and e₃ must correspond to the endpoints of f₁ and f₂, and so g(v₃) = w₁ and g(v₄) = w₅ or g(v₃) = w₅ and g(v₄) = w₁.

Similarly, since v₁ is the endpoint of four distinct edges (e₁, e₇, e₅, and e₄), g(v₁) must also be the endpoint of four distinct edges (because every edge incident on g(v₁) is the image under h of an edge incident on v₁ and h is one-to-one and onto). But the only vertex in G' that has four edges coming out of it is w₂, and so g(v₁) = w₂.

Now if g(v₃) = w₁, then since v₁ and v₃ are endpoints of e₁ in G, g(v₁) = w₂ and g(v₃) = w₁ must be endpoints of h(e₁) in G'. This implies that h(e₁) = f₃.

By continuing in this way, possibly making some arbitrary choices as you go, you eventually can find functions g and h to define the isomorphism between G and G'. One pair of functions (there are several) is the following:

```
V(G)    g    V(G')    E(G)    h    E(G')
v1  →   w1        e1  →   f1
v2  →   w2        e2  →   f2
v3  →   w3        e3  →   f3
v4  →   w4        e4  →   f4
v5  →   w5        e5  →   f5
                 e6  →   f6
                 e7  →   f7
```

## Graph Isomorphism as an Equivalence Relation

It is not hard to show that graph isomorphism is an equivalence relation on a set of graphs; in other words, it is reflexive, symmetric, and transitive.

**Theorem 10.4.1: Graph Isomorphism is an Equivalence Relation**
Let S be a set of graphs and let R be the relation of graph isomorphism on S. Then R is an equivalence relation on S.

**Proof:**
- **R is reflexive:** Given any graph G in S, define a graph isomorphism from G to G by using the identity functions on the set of vertices and on the set of edges of G.
- **R is symmetric:** Given any graphs G and G' in S such that G is isomorphic to G', we must show that G' is isomorphic to G. But this is true because if g and h are vertex and edge correspondences from G to G' that preserve the edge-endpoint functions, then g⁻¹ and h⁻¹ are vertex and edge correspondences from G' to G that preserve the edge-endpoint functions.
- **R is transitive:** Given any graphs G, G', and G'' in S such that G is isomorphic to G' and G' is isomorphic to G'', we must show that G is isomorphic to G''. But this follows from the fact that if g₁ and h₁ are vertex and edge correspondences from G to G' that preserve the edge-endpoint functions of G and G' and g₂ and h₂ are vertex and edge correspondences from G' to G'' that preserve the edge-endpoint functions of G' and G'', then g₂ ∘ g₁ and h₂ ∘ h₁ are vertex and edge correspondences from G to G'' that preserve the edge-endpoint functions of G and G''.

**Note:** As a consequence of the symmetry property, you can simply say "G and G' are isomorphic" instead of "G is isomorphic to G'" or "G' is isomorphic to G."

### Example 10.4.2: Finding Representatives of Isomorphism Classes
Find all nonisomorphic graphs that have two vertices and two edges. In other words, find a collection of representative graphs with two vertices and two edges such that every such graph is isomorphic to one in the collection.

**Solution:**
There are four nonisomorphic graphs that have two vertices and two edges. These can be drawn without vertex and edge labels because any two labelings give isomorphic graphs.

```
(a)     (b)     (c)     (d)
o-------o       o       o       o
|       |       |       |
o-------o       o---o   o   o
```

To see that these four drawings show all the nonisomorphic graphs that have two vertices and two edges, first note whether one of the edges joins the two vertices or not. If it does, there are two possibilities: The other edge can also join the two vertices (as in (a)) or it can be a loop incident on one of them (as in (b)—it makes no difference which vertex is chosen to have the loop because interchanging the two vertex labels gives isomorphic graphs). If neither edge joins the two vertices, then both edges are loops. In this case, there are only two possibilities: Either both loops are incident on the same vertex (as in (c)) or the two loops are incident on separate vertices (as in (d)). There are no other possibilities for placing the edges, so the listing is complete.

## Isomorphic Invariants

Now consider the question, "Is there a general method to figure out whether graphs G and G' are isomorphic?" In other words, is there some algorithm that will accept graphs G and G' as input and produce a statement as to whether they are isomorphic? In fact, there is such an algorithm. It consists of generating all one-to-one, onto functions from the set of vertices of G to the set of vertices of G' and from the set of edges of G to the set of edges of G' and checking each pair to determine whether it preserves the edge-endpoint functions of G and G'.

The problem with this algorithm is that it takes an unreasonably long time to perform, even on a high-speed computer. If G and G' each have n vertices and m edges, the number of one-to-one correspondences from vertices to vertices is n! and the number of one-to-one correspondences from edges to edges is m!, so the total number of pairs of functions to check is n! · m!. For instance, if m = n = 20, there would be 20! · 20! ≈ 5.9 × 10³⁶ pairs to check. Assuming that each check takes just 1 nanosecond, the total time would be approximately 1.9 × 10²⁰ years!

Unfortunately, there is no more efficient general method known for checking whether two graphs are isomorphic. However, there are some simple tests that can be used to show that certain pairs of graphs are not isomorphic. For instance, if two graphs are isomorphic, then they have the same number of vertices (because there is a one-to-one correspondence from the vertex set of one graph to the vertex set of the other). It follows that if you are given two graphs, one with 16 vertices and the other with 17, you can immediately conclude that the two are not isomorphic.

More generally, a property that is preserved by graph isomorphism is called an isomorphic invariant. For instance, "having 16 vertices" is an isomorphic invariant: If one graph has 16 vertices, then so does any graph that is isomorphic to it.

**Definition: Isomorphic Invariant**
A property P is called an invariant for graph isomorphism if, and only if, given any graphs G and G', if G has property P and G' is isomorphic to G, then G' has property P.

**Theorem 10.4.2: Isomorphic Invariants**
Each of the following properties is an invariant for graph isomorphism, where n, m, and k are all nonnegative integers:
1. has n vertices
2. has m edges
3. has a vertex of degree k
4. has m vertices of degree k
5. has a circuit of length k
6. has a simple circuit of length k
7. has m simple circuits of length k
8. is connected
9. has an Euler circuit
10. has a Hamiltonian circuit

### Example 10.4.3: Showing That Two Graphs Are Not Isomorphic
Show that the following pairs of graphs are not isomorphic by finding an isomorphic invariant that they do not share.

**Pair (a):**
```
G (9 edges)    G' (8 edges)
o---o---o---o   o---o---o
|   |   |   |   |   |   |
o---o---o---o   o---o---o
```

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
a. G has nine edges; G' has only eight.
b. H has a vertex of degree 4; H' does not.

### Example 10.4.4: Proof of Theorem 10.4.2, Part (3)
Prove that if G is a graph that has a vertex of degree k and G' is isomorphic to G, then G' has a vertex of degree k.

**Proof:**
Suppose G and G' are isomorphic graphs and G has a vertex v of degree k, where k is a nonnegative integer. [We must show that G' has a vertex of degree k.] Since G and G' are isomorphic, there are one-to-one, onto functions g and h from the vertices of G to the vertices of G' and from the edges of G to the edges of G' that preserve the edge-endpoint functions in the sense that for all edges e and all vertices u of G, u is an endpoint of e if, and only if, g(u) is an endpoint of h(e).

Let e₁, e₂, ..., eₘ be the m distinct edges that are incident on a vertex v in G, where m is a nonnegative integer. Then h(e₁), h(e₂), ..., h(eₘ) are m distinct edges that are incident on g(v) in G'. [The reason why h(e₁), h(e₂), ..., h(eₘ) are distinct is that h is one-to-one and e₁, e₂, ..., eₘ are distinct. And the reason why h(e₁), h(e₂), ..., h(eₘ) are incident on g(v) is that g and h preserve the edge-endpoint functions of G and G' and e₁, e₂, ..., eₘ are incident on v.]

Also, there are no edges incident on g(v) other than the ones that are images under g of edges incident on v [because g is onto and g and h preserve the edge-endpoint functions of G and G']. Thus the number of edges incident on v equals the number of edges incident on g(v).

Finally, an edge e is a loop at v if, and only if, h(e) is a loop at g(v), so the number of loops incident on v equals the number of loops incident on g(v). [For since g and h preserve the edge-endpoint functions of G and G', a vertex w is an endpoint of e in G if, and only if, g(w) is an endpoint of h(e) in G'. It follows that v is the only endpoint of e in G if, and only if, g(v) is the only endpoint of h(e) in G'.]

Now the degree of v, which is k, equals the number of edges incident on v plus the number of edges incident on v that are loops (since each loop contributes 2 to the degree of v). But we have already shown that the number of edges incident on v equals the number of edges incident on g(v) and that the number of loops incident on v equals the number of loops incident on g(v). Hence g(v) also has degree k.

## Graph Isomorphism for Simple Graphs

When graphs G and G' are both simple, the definition of G being isomorphic to G' can be written without referring to the correspondence between the edges of G and the edges of G'.

**Definition 10.4.2: Isomorphism of Simple Graphs**
If G and G' are simple graphs, then G is isomorphic to G' if, and only if, there exists a one-to-one correspondence g from the vertex set V(G) of G to the vertex set V(G') of G' that preserves the edge-endpoint functions of G and G' in the sense that for all vertices u and v of G,
**{u, v} is an edge in G ⇔ {g(u), g(v)} is an edge in G'.**

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
Yes. Define g: V(G) → V(G') by the arrow diagram shown below.

```
V(G)    g    V(G')
a    →   w
b    →   x
c    →   y
d    →   z
e    →   u
f    →   v
g    →   t
```

Then g is one-to-one and onto by inspection. The fact that g preserves the edge-endpoint functions of G and G' is shown by the following table:

```
Edges of G    Edges of G'
{a, b}       {y, w} = {g(a), g(b)}
{a, c}       {y, x} = {g(a), g(c)}
{a, d}       {y, z} = {g(a), g(d)}
{c, d}       {x, z} = {g(c), g(d)}
{b, e}       {x, u} = {g(b), g(e)}
{c, f}       {y, v} = {g(c), g(f)}
{d, g}       {z, t} = {g(d), g(g)}
{e, f}       {u, v} = {g(e), g(f)}
{f, g}       {v, t} = {g(f), g(g)}
```

## Exercise Set 10.4

For each pair of graphs G and G' in 1–5, determine whether G and G' are isomorphic. If they are, give functions g: V(G) → V(G') and h: E(G) → E(G') that define the isomorphism. If they are not, give an invariant for graph isomorphism that they do not share.

[Note: The exercise problems from the textbook are included here but not fully worked out due to space constraints.]

## Test Yourself

1. If G and G' are graphs, then G is isomorphic to G' if, and only if, there exist a one-to-one correspondence g from the vertex set of G to the vertex set of G' and a one-to-one correspondence h from the edge set of G to the edge set of G' such that for all vertices v and edges e in G, v is an endpoint of e if, and only if, _____.

2. A property P is an invariant for graph isomorphism if, and only if, given any graphs G and G', if G has property P and G' is isomorphic to G then _____.

3. Some invariants for graph isomorphisms are _____, _____, _____, _____, _____, _____, _____, _____, _____, and _____.

**Answers:**
1. g(v) is an endpoint of h(e)
2. G' has property P
3. has n vertices; has m edges; has a vertex of degree k; has m vertices of degree k; has a circuit of length k; has a simple circuit of length k; has m simple circuits of length k; is connected; has an Euler circuit; has a Hamiltonian circuit