from itertools import permutations


def composition(text, k):
    return sorted([text[start: start + k] for start in range(len(text) - k + 1)])


def path_to_genome(patterns):
    return patterns[0] + ''.join([patterns[i][-1] for i in range(1, len(patterns))])


def overlap(str1, str2):
    return str1[1:] == str2[:-1]


def overlap_graph(patterns):
    graph = {pattern: [] for pattern in patterns}
    for combo in permutations(patterns, 2):
        if overlap(combo[0], combo[1]):
            graph[combo[0]].append(combo[1])

    return graph


def construct_de_bruijn_graph(k, text):
    graph = {}
    for i in range(len(text) - k + 1):
        key = text[i:i + k - 1]
        if key not in graph:
            graph[key] = []
        graph[key].append(text[i + 1: i + k])

    return graph


def construct_de_bruijn_graph_from_k_mers(patterns):
    graph = {}
    for pattern in patterns:
        prefix = pattern[: -1]
        if prefix not in graph:
            graph[prefix] = []
        suffix = pattern[1:]
        graph[prefix].append(suffix)

    return graph
