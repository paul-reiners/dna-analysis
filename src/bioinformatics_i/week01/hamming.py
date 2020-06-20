# coding=utf-8
def hamming_distance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1

    return dist


def find_approximate_pattern_matches(text, pattern, d):
    pattern_matches = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            pattern_matches.append(i)

    return pattern_matches


def count(text, pattern, d):
    return len(find_approximate_pattern_matches(text, pattern, d))


def approximate_pattern_count(text, pattern, d):
    c = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern2 = text[i:i + len(pattern)]
        if hamming_distance(pattern, pattern2) <= d:
            c += 1
    return c
