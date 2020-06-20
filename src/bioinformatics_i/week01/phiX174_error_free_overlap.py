# coding=utf-8
# Uses python3

import sys


def longest_overlap(s, t):
    n = len(s)
    m = len(t)
    max_possible = min(n, m)
    max_found = max_possible
    while max_found >= 0:
        current_suffix = s[n - max_found:]
        if s[n - max_found:] == t[:max_found]:
            return current_suffix
        max_found -= 1
    return ""


def overlap(patterns, k):
    g = {}
    for pattern1 in patterns:
        g[pattern1] = []
        for pattern2 in patterns:
            if pattern1 == pattern2:
                continue
            # We form a vertex for each k-mer in Patterns and connect k-mers Pattern and Pattern’ by a directed edge
            # from Pattern to Pattern’ if SUFFIX(Pattern)=PREFIX(Pattern’).
            if suffix(pattern1, k) == prefix(pattern2, k):
                g[pattern1].append(pattern2)

    return g


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1

    return count


def frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_so_far = max_map(freq_map)
    for pattern in freq_map.keys():
        if freq_map[pattern] == max_so_far:
            frequent_patterns.append(pattern)

    return frequent_patterns


def max_map(freq_map):
    return max(freq_map.values())


def construct_hamiltonian_path(graph):
    # Then construct a Hamiltonian path in this graph in a greedy fashion: for each read select an out-going edge of
    # maximum weight.
    trimmed_graph = {}
    for v1 in graph.keys():
        edges = graph[v1]
        max_overlap = 0
        for edge in edges:
            w = len(edge[1])
            if w > max_overlap:
                max_overlap = w
        for e in edges:
            if len(e[1]) == max_overlap:
                trimmed_graph[v1] = e

                break
    # Then read a string spelled by this path.
    cur_symbol = trimmed_graph.keys()[0]
    path = cur_symbol
    for i in range(len(trimmed_graph) - 1):
        next_v_w = trimmed_graph[cur_symbol]
        next_symbol = next_v_w[0]
        ovrlp = next_v_w[1]
        path = path + next_symbol[len(ovrlp):]
        cur_symbol = next_symbol

    return path


def get_assembled_genome(genome_reads):
    overlap_graph = get_overlap_graph(genome_reads)
    hamiltonian_path = construct_hamiltonian_path(overlap_graph)

    return hamiltonian_path


def get_overlap_graph(genome_reads):
    # Construct an overlap graph: two reads are joined by a directed edge of weight equal to the length of the maximum
    # overlap of these two reads.
    reads_set = set(genome_reads)
    graph = {}
    for read1 in reads_set:
        for read2 in reads_set:
            if read1 != read2:
                ovrlp = longest_overlap(read1, read2)
                new_v = [read2, ovrlp]
                if read1 not in graph.keys():
                    graph[read1] = []
                graph[read1].append(new_v)

    return graph


def suffix(pattern, k):
    """we define SUFFIX(Pattern) as the last (k-1)-mers in a k-mer Pattern"""
    return pattern[-(k - 1):]


def prefix(pattern, k):
    """we define PREFIX(Pattern) as the first (k-1)-mers in a k-mer Pattern"""
    return pattern[k - 1:]


def frequency_table(text, k):
    freq_map = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i: i + k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    return freq_map


if __name__ == '__main__':
    algorithm_input = sys.stdin.read()
    reads = algorithm_input.split()
    assembled_genome = get_assembled_genome(reads)

    print(assembled_genome)
