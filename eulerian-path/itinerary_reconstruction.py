"""
Itinerary Reconstruction via Eulerian Path (Hierholzer's algorithm)

Given a shuffled list of used flight tickets, reconstruct the travel route
that uses every ticket exactly once.

Reference:
    Hierholzer, C. (1873). Mathematische Annalen 6:30-32.
"""


def build_graph(tickets):
    """
    Build a directed adjacency list from a ticket list.

    Args:
        tickets: list of [departure, arrival] pairs
    Returns:
        dict mapping airport -> list of destination airports

    Learning note:
        Each ticket is an EDGE, not a node. Duplicate tickets must produce
        duplicate entries in the destination list -- collapsing them would
        silently delete edges from the graph.
    """
    a = {}
    for i in tickets:
        if i[0] not in a:
            a[i[0]] = [i[-1]]
        else:
            a[i[0]].append(i[-1])
    return a


def find_start(graph):
    """
    Find the starting airport of the Eulerian path.

    Returns:
        the node with out_degree - in_degree == 1, or the lexicographically
        smallest node if every node is balanced (Eulerian circuit).

    Learning note:
        A node in the middle of a path must depart once for every arrival,
        so out == in. Only the start (+1) and the end (-1) break this.

        Bug fixed here: in-degree was originally counted with
        `if graph[j] == [i]`, which is only true when j has exactly one
        outgoing edge. Nodes with multiple destinations were skipped
        entirely. `.count()` is required rather than `in`, because `in`
        is boolean and cannot see duplicate tickets.
    """
    num = {}
    for i in graph:
        out_degree = len(graph[i])
        in_degree = 0
        for j in graph:
            in_degree += graph[j].count(i)
        result = out_degree - in_degree
        num[i] = result
    for k in num:
        if num[k] == 1:
            return k
    return sorted(num)[0]


def find_route(graph):
    """
    Hierholzer traversal. Return the full itinerary as a list of airports.

    Learning note:
        stack[-1] (not stack[0]) is inspected because the structure must be
        LIFO. The most recent branch is explored to exhaustion first, and
        popping returns control to exactly the junction it descended from.
        Backtracking is therefore implicit -- the stack itself encodes the
        junction history, so no explicit "go back" logic is written.

        A node is appended to `circuit` only once it has no outgoing edges
        left, so the first node appended is near the END of the route.
        `circuit` records the order in which nodes became stuck, not the
        order in which they are visited. Hence the final reverse().

        graph.get(current, []) is required because terminal airports appear
        as edge targets but never as dictionary keys.

    TODO:
        pop() takes the last element, so the lexicographically smallest
        route is not guaranteed when multiple valid routes exist.
    """
    start = find_start(graph)
    stack = [start]
    circuit = []

    while len(stack) > 0:
        current = stack[-1]
        if len(graph.get(current, [])) > 0:
            next_node = graph[current].pop()
            stack.append(next_node)
        else:
            circuit.append(stack.pop())
    circuit.reverse()
    return circuit


def verify_route(route, tickets):
    """
    Return True if the route uses every ticket exactly once.

    Learning note:
        The tickets actually consumed by a route are its adjacent pairs:
        route[i] -> route[i+1]. Comparing sorted() lists is a multiset
        comparison, which is what is needed here since the input order is
        arbitrary. Python compares nested lists element-wise, so no
        conversion to tuples is necessary.

        Note that find_route() destroys the graph by popping edges, so
        verification must be done against the original ticket list.
    """
    a = []
    for i in range(0, len(tickets)):
        a.append([route[i], route[i + 1]])
    return sorted(a) == sorted(tickets)


tickets = [["ICN", "NRT"], ["NRT", "SFO"], ["SFO", "ICN"], ["ICN", "JFK"], ["JFK", "LHR"]]
graph = build_graph(tickets)
route = find_route(graph)
print(route)
print(verify_route(route, tickets))

circuit_tickets = [["ATL", "BOS"], ["BOS", "CDG"], ["CDG", "ATL"]]
circuit_graph = build_graph(circuit_tickets)
circuit_route = find_route(circuit_graph)
print(circuit_route)
print(verify_route(circuit_route, circuit_tickets))

duplicate_tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
duplicate_graph = build_graph(duplicate_tickets)
duplicate_route = find_route(duplicate_graph)
print(duplicate_route)
print(verify_route(duplicate_route, duplicate_tickets))
