from itertools import permutations


def composition(text, k):
    return sorted([text[start : start + k] for start in range(len(text) - k + 1)])


def path_to_genome(patterns):
    return patterns[0] + ''.join([patterns[i][-1] for i in range(1, len(patterns))])


def overlap(str1, str2):
    return str1[1:] == str2[:-1]
