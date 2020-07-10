import random


def get_all_edges(graph):
    return [[i, j] for i in graph.keys() for j in graph[i]]


def get_unexplored_edges(unexplored_edges, cycle):
    n = len(cycle)
    for i in range(n):
        unexplored_edges.remove([cycle[i], cycle[(i + 1) % n]])
    return unexplored_edges


def get_next_cycle(unexplored_edges):
    next_cycle = []
    nodes = [e[0] for e in unexplored_edges]
    node = random.choice(nodes)
    while node not in next_cycle:
        next_cycle.append(node)
        nodes = [e[1] for e in unexplored_edges if e[0] == next_cycle[-1]]
        node = random.choice(nodes)
    start = next_cycle.index(node)
    return next_cycle[start:]


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def rotate(cycle, common_node):
    idx = cycle.index(common_node)

    return cycle[idx:] + cycle[:idx]


def splice_all_cycles(cycles):
    n = len(cycles)
    while n > 1:
        trim_cycles(cycles, n)
        n = len(cycles)

    return cycles[0]


def trim_cycles(cycles, n):
    for i in range(n):
        cycle1 = cycles[i]
        for j in range(i + 1, n):
            cycle2 = cycles[j]
            intersect = intersection(cycle1, cycle2)
            if len(intersect) > 0:
                common_node = intersect[0]
                rotated_cycle1 = rotate(cycle1, common_node)
                pos = cycle2.index(common_node)
                spliced_cycle = cycle2[:pos] + rotated_cycle1[:] + cycle2[pos:]
                cycles.append(spliced_cycle)
                cycles.remove(cycle1)
                cycles.remove(cycle2)

                return cycles


def get_eulerian_cycle(graph):
    unexplored_edges = get_all_edges(graph)
    cycles = []
    while len(unexplored_edges) > 0:
        next_cycle = get_next_cycle(unexplored_edges)
        cycles.append(next_cycle)
        unexplored_edges = get_unexplored_edges(unexplored_edges, next_cycle)
    eulerian_cycle = splice_all_cycles(cycles)

    return eulerian_cycle
