import random
import copy
from itertools import product

from bioinformatics_ii.week1 import path_to_genome, construct_de_bruijn_graph_from_k_mers


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


def add_edge(graph, new_edge):
    source = new_edge[0]
    if source not in graph:
        graph[source] = []
    graph[source].append(new_edge[1])

    return graph


def remove_edge(eulerian_cycle, edge):
    idx = eulerian_cycle.index(edge[1])
    new_path = eulerian_cycle[idx:] + eulerian_cycle[:idx]

    return new_path


def get_eulerian_path(graph):
    all_edges = get_all_edges(graph)
    degree_counts = {}
    for edge in all_edges:
        source = edge[0]
        if source not in degree_counts:
            degree_counts[source] = [0, 0]
        degree_counts[source] = [degree_counts[source][0] + 1, degree_counts[source][1]]
        destination = edge[1]
        if destination not in degree_counts:
            degree_counts[destination] = [0, 0]
        degree_counts[destination] = [degree_counts[destination][0], degree_counts[destination][1] + 1]
    new_source = None
    new_destination = None
    for node in degree_counts:
        degree_node_counts = degree_counts[node]
        if degree_node_counts[0] == degree_node_counts[1] - 1:
            new_source = node
        elif degree_node_counts[1] == degree_node_counts[0] - 1:
            new_destination = node
    new_edge = [new_source, new_destination]
    expanded_graph = add_edge(copy.deepcopy(graph), new_edge)
    eulerian_cycle = get_eulerian_cycle(expanded_graph)
    eulerian_path = remove_edge(eulerian_cycle, new_edge)

    return eulerian_path


def string_reconstruction(patterns):
    d_b = construct_de_bruijn_graph_from_k_mers(patterns)
    path = get_eulerian_path(d_b)
    text = path_to_genome(path)

    return text


def get_k_universal_circular_string(k):
    patterns = get_binary_strings(k)
    d_b = construct_de_bruijn_graph_from_k_mers(patterns)
    cycle = get_eulerian_cycle(d_b)
    k_universal_circular_string = ''.join([cycle[i][-1] for i in range(len(cycle))])

    return k_universal_circular_string


def get_binary_strings(k):
    patterns = [''.join(t) for t in list(product('01', repeat=k))]
    return patterns


def generate_k_d_mer_composition(text, k, d):
    k_d_mer_len = 2 * k + d
    n = len(text)
    composition = []
    for i in range(n - k_d_mer_len + 1):
        k_d_mer = [text[i:i + k], text[i + k + d:i + k_d_mer_len]]
        composition.append(k_d_mer)
    composition.sort()

    return composition


def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = [p[0] for p in gapped_patterns]
    second_patterns = [p[1] for p in gapped_patterns]
    prefix_string = path_to_genome(first_patterns)
    suffix_string = path_to_genome(second_patterns)
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            return "there is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-(k + d):]
