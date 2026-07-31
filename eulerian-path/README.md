# Eulerian Paths: One Algorithm, Two Domains

An exercise in verifying that an algorithm was understood rather than memorized,
by implementing it twice in unrelated problem domains.

- **Problem 1 — De Bruijn genome assembly.** Implemented in a separate repository:
  [`bioinformatics-from-scratch/de-bruijn-assembly`](https://github.com/Mattias-J-Kim/bioinformatics-from-scratch)
- **Problem 2 — Itinerary reconstruction.** `itinerary_reconstruction.py`, this directory.

The second problem was chosen specifically because it shares no vocabulary with
the first. The input is a list of airport code pairs rather than overlapping
substrings, and the output is a list rather than a concatenated string.
Everything between those two ends is identical.

---

## Background

Both problems reduce to finding an **Eulerian path**: a walk through a directed
graph using every edge exactly once.

- **Hierholzer's algorithm** (Hierholzer, C. 1873. *Mathematische Annalen* 6:30–32)
  constructs such a path in linear time.
- Its application to sequence assembly follows Compeau, P., Pevzner, P. & Tesler, G.
  (2011). "How to apply de Bruijn graphs to genome assembly." *Nature Biotechnology*
  29:987–991 — the structural basis of assemblers such as Velvet and SPAdes.

---

## The Shared Pattern

```
1. Raw data          →  adjacency list (dict of lists)
2. Degree analysis   →  identify the start node
3. Stack traversal   →  Hierholzer; append on exhaustion, reverse at the end
4. Reconstruction    →  traversal order → final answer
5. Verification      →  compare against the input as a multiset
```

| Step | Assembly | Itinerary |
|---|---|---|
| Edge | a k-mer | a ticket |
| Node | a (k−1)-mer | an airport |
| Reconstruction | overlap-collapse into a string | the node list itself |
| Verification | re-decompose into k-mers | extract adjacent pairs |

Steps 2 and 3 are byte-for-byte the same in both implementations. Recognizing
that a k-mer prefix and an airport code are the same object as far as the
algorithm is concerned was the intended outcome.

---

## Problem 2 — Itinerary Reconstruction

Given a shuffled list of used flight tickets, reconstruct the route that uses
every ticket exactly once.

```python
tickets = [["ICN","NRT"], ["NRT","SFO"], ["SFO","ICN"],
           ["ICN","JFK"], ["JFK","LHR"]]

# → ["ICN", "NRT", "SFO", "ICN", "JFK", "LHR"]
```

| Function | Responsibility |
|---|---|
| `build_graph(tickets)` | ticket list → adjacency list |
| `find_start(graph)` | degree analysis; lexicographic fallback for circuits |
| `find_route(graph)` | Hierholzer traversal |
| `verify_route(route, tickets)` | adjacent-pair extraction, multiset comparison |

**Test cases covered**

| Case | Purpose |
|---|---|
| Eulerian path | one node with `out − in == 1` |
| Eulerian circuit | all balanced; exercises the lexicographic fallback |
| Duplicate tickets | exercises occurrence counting rather than membership |
| Dead-end first | greedy first choice strands edges; exercises stack backtracking |

---

## Concepts Worked Through

Recorded because the reasoning, not the code, was the point of the exercise.
These are the questions I actually had to resolve.

### Why does `out_degree − in_degree == 1` identify the start?

Any node interior to a path must depart once for every arrival, so `out == in`.
Only two nodes can break this symmetry: the start, whose first departure has no
preceding arrival (`+1`), and the end, whose final arrival has no following
departure (`−1`).

If no node breaks symmetry, the graph holds an Eulerian *circuit* rather than a
path — start and end coincide and any node is a valid entry point. The
itinerary problem specifies the lexicographically smallest node in that case,
which is a tie-breaking rule from the problem statement, not a property of the
algorithm.

### Why inspect `stack[-1]` rather than `stack[0]`?

The stack must be LIFO by necessity, not convention. Reading the top means the
most recently entered branch is fully explored before anything else; when it
dead-ends, popping returns control to *exactly* the branch point it descended
from. Backtracking is therefore implicit — the stack encodes the junction
history, so no explicit "return to previous junction" logic is written. It is a
recursive call stack made explicit.

Reading `stack[0]` treats the structure as a queue and destroys this property:
intermediate nodes sit unexamined in the middle of the structure with no
guarantee of when or in what order they resolve.

### What happens at a branch point?

Nothing special, which is the point. Taking one outgoing edge does not discard
the others — the branch node stays on the stack and its unused edges stay in the
adjacency list. After the chosen branch dead-ends and unwinds, the node is
re-examined and its remaining edges consumed. Where an Eulerian path is
guaranteed to exist, *any* choice order eventually consumes every edge; only the
traversal order differs.

### Why must the result be reversed?

Nodes are appended only once they have no outgoing edges left, so the first node
appended lies near the *end* of the route. The output records the order in which
nodes became stuck, not the order they are visited.

In the test case above, the first greedy step `ICN → JFK → LHR` strands three
unused tickets. `LHR` and `JFK` are appended first, the stack unwinds to `ICN`,
the remaining `ICN → NRT` edge is consumed, and the final reversal yields the
correct route. A naive greedy walk that emits nodes as it visits them fails here.

---

## Debugging Log

**Counting in-degrees with an equality test.**

```python
if graph[j] == [i]:      # wrong
    in_degree += 1
```

True only when node `j` has exactly one outgoing edge pointing to `i`. Any node
with two or more destinations was silently skipped. The first test case passed
anyway, because every contributing node there happened to have exactly one
outgoing edge — the code was accidentally correct, not correct. Exposing it
required constructing an input that violated that accidental assumption.

Membership (`i in graph[j]`) fixes multi-destination nodes but still fails on
duplicate edges, since membership is boolean. Counting occurrences is required:

```python
in_degree += graph[j].count(i)     # correct
```

This also eliminates the surrounding `if`, since `count` returns 0 when absent.

**Worth noting:** the assembler, written first, counted in-degrees correctly with
a nested scan over all destination lists. The bug above was introduced when the
same subproblem was re-solved from memory a day later in a different domain. The
concept was understood; the reimplementation was not checked against the case
that made it necessary. Recorded here because that failure mode is more
instructive than the fix.

**Other recurring patterns caught during these two problems:**

- indexing dictionaries and `.keys()` / `.values()` views with integers instead
  of iterating them directly
- `=+1` typed in place of `+=1`
- substring matching (`in`) where equality (`==`) was intended
- shallow copy where a deep copy of a nested structure was required — traversal
  consumes edges, so a shallow copy empties the caller's graph and makes
  post-hoc verification impossible
- `KeyError` on terminal nodes, which appear as edge targets but never as
  dictionary keys; handled with `graph.get(node, [])`

---

## Open Items

- `find_route` consumes edges with `list.pop()`, taking the last element, so the
  lexicographically smallest route is not guaranteed when several valid routes
  exist. Producing it requires ordering each adjacency list before traversal.
  Not yet implemented.
- `find_start` assumes an Eulerian path exists and does not reject inputs where
  two or more nodes satisfy `out − in == 1`. Validation is currently delegated to
  `verify_route`, which returns `False` for such inputs. The assembler
  implementation raises explicitly instead; the two should be made consistent.
- In-degree computation is O(V·E) in both implementations. Accumulating degrees
  in a single pass over the edge list would reduce this.

---

## Note on Method

These problems were worked through with an AI assistant (Claude) used in a
Socratic mode: the assistant set the specifications and test cases, and when I
was stuck responded with targeted questions and conceptual explanations rather
than code.

All implementation code in this repository was written by me. Where the assistant
identified a defect, it described the failing condition and why it failed; the
correction was then made by me. The conceptual sections above reflect
explanations I requested and then restated in my own terms, and the questions
listed under "Concepts Worked Through" are the questions I actually asked.

This is stated explicitly because the value of this repository is the reasoning
trail, and a reasoning trail is only meaningful if its provenance is accurate.
