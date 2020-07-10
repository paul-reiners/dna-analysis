import random


def get_random_cycle(graph):
    random_cycle = []
    nodes = list(graph.keys())
    node = random.choice(nodes)
    while node not in random_cycle:
        random_cycle.append(node)
        nodes = graph[node]
        node = random.choice(nodes)
    return random_cycle[random_cycle.index(node):]

def get_all_edges(graph):
    return [[i, j] for i in graph.keys() for j in graph[i]]


def get_unexplored_edges(unexplored_edges, cycle):
    pass


def get_new_start(cycle, unexplored_edges):
    pass


def get_eulerian_cycle(graph):
    unexplored_edges = get_all_edges(graph)
    cycle = get_random_cycle(graph)
    unexplored_edges = get_unexplored_edges(unexplored_edges, cycle)
    while len(unexplored_edges > 0):
        new_start = get_new_start(cycle, unexplored_edges)
        next_cycle = get_random_cycle(graph, cycle, unexplored_edges)
        cycle = next_cycle
        unexplored_edges = get_unexplored_edges(unexplored_edges, cycle)

    return cycle
