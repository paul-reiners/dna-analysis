import random


def get_random_cycle(graph):
    random_cycle = []
    nodes = list(graph.keys())
    node = random.choice(nodes)
    while node not in random_cycle:
        random_cycle.append(node)
        nodes = graph[node]
        unseen_nodes = [n for n in nodes if n not in random_cycle[1:] or n == random_cycle[0]]
        node = random.choice(unseen_nodes)
    return random_cycle

def get_all_edges(graph):
    return [[i, j] for i in graph.keys() for j in graph[i]]


def get_unexplored_edges(unexplored_edges, cycle):
    n = len(cycle)
    for i in range(n):
        unexplored_edges.remove([cycle[i], cycle[(i + 1) % n]])
    return unexplored_edges


def get_new_start(cycle, unexplored_edges):
    new_starts = [edge for edge in unexplored_edges if edge[0] in cycle]

    return new_starts[0]


def get_eulerian_cycle(graph):
    unexplored_edges = get_all_edges(graph)
    cycle = get_random_cycle(graph)
    unexplored_edges = get_unexplored_edges(unexplored_edges, cycle)
    while len(unexplored_edges) > 0:
        new_start = get_new_start(cycle, unexplored_edges)
        next_cycle = get_random_cycle(graph, cycle, unexplored_edges)
        cycle = next_cycle
        unexplored_edges = get_unexplored_edges(unexplored_edges, cycle)

    return cycle
