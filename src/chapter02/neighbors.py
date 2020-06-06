# coding=utf-8
from phix174.phiX174_error_free_overlap import suffix
from section01.hamming import hamming_distance

nucleotides = {'A', 'C', 'G', 'T'}


def immediate_neighbors(pattern):
    neighborhood = {pattern}
    for i in range(len(pattern)):
        symbol = pattern[i]
        for x in nucleotides:
            if x == symbol:
                continue
            neighbor = pattern[:i] + x + pattern[i + 1:]
            neighborhood.add(neighbor)
    return neighborhood


def first_symbol(pattern):
    return pattern[0]


def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return nucleotides
    neighborhood = set()
    k = len(pattern)
    suffix_neighbors = neighbors(suffix(pattern, k), d)
    for text in suffix_neighbors:
        if hamming_distance(suffix(pattern, k), text) < d:
            for x in nucleotides:
                neighborhood.add(x + text)
        else:
            neighborhood.add(first_symbol(pattern) + text)
    return neighborhood
