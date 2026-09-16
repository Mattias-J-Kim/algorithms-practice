# algorithms-practice

Dynamic programming and algorithm practice, separate from biology-specific work.

Python and Java, standard library only. No external dependencies.

## Purpose

Algorithms are implemented from scratch rather than looked up, so that the
recurrence or data structure is understood before it gets applied to real
problems. Where an algorithm here later turns out to be useful biologically, the
application lives in
[bioinformatics-from-scratch](https://github.com/Mattias-J-Kim/bioinformatics-from-scratch)
and this repository keeps the general form.

Each file carries its own learning notes: the recurrence, and the bugs that came
up while deriving it.

## dynamic_programming/

Grouped by table structure rather than by problem name, since the point of
working through them in this order was to see the same shapes recur.

**1D table**

- `house_robber.py` — max non-adjacent sum
- `longest_increasing_subsequence.py` — `dp[i]` indexed by *ending element*, not by prefix length

**2D grid**

- `unique_paths.py` — path counting on a lattice

**2D string comparison** — all four share one table shape, differing only in the recurrence

- `edit_distance.py` — Levenshtein distance
- `longest_common_subsequence.py` — non-contiguous match
- `longest_common_substring.py` — contiguous match; requires tracking a running maximum rather than reading the final cell
- `longest_palindromic_subsequence.py` — reduces to LCS of a string against its own reverse

## eulerian-path/

- `itinerary_reconstruction.py` — Eulerian path via Hierholzer's algorithm.
  Reconstructs a travel route from a shuffled ticket list: build an adjacency
  list, locate the start node by degree difference, traverse with an explicit
  stack, then reverse.

  This is the same pattern as the De Bruijn genome assembler in
  `bioinformatics-from-scratch`, deliberately re-applied to a non-biological
  input (airport codes rather than k-mers) to check that the algorithm had been
  understood rather than memorized.

## recursion/

Java, from a university Data Structures lab. Unlike the rest of this
repository, the problem specifications here came from the course rather than
from the Socratic sessions described under Method.

- `Power.java` — x^n by repeated squaring; O(log n) calls instead of O(n)
- `BinarySum.java` — array sum by halving the range; work stays O(n) but recursion depth drops to O(log n)
- `LinearFib.java` — Fibonacci returning the pair (F(n), F(n-1)), turning the exponential two-call recursion into a single call per step

## Usage

Each script is standalone. Inputs are assigned as plain variables at the bottom
of the file rather than passed as arguments — edit those assignments and run:

```
python <script_name>.py
```

Java files (Java 11+) run directly from source:

```
java <ClassName>.java
```

## Method

## Method

Claude (AI assistant) was used in a Socratic mode: it set the specifications
and test cases, and when I was stuck it asked targeted questions or explained
concepts instead of giving code.

- **Code:** all implementation code was written by me.
- **Documentation:** the explanatory text (header comments and this README)
  was drafted with Claude and reviewed by me.
- **Exception, `recursion/`:** specifications came from a university Data
  Structures course. Claude was used afterwards to document the code and to
  reformat it (English strings, naming, indentation) without changing the
  logic; I reviewed both the documentation and the reformatted code.
