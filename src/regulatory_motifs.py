from itertools import product


def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i:i + 1] != str2[i:i + 1]:
            distance += 1

    return distance


def d(pattern, string):
    shortest = -1
    pattern_length = len(pattern)
    for start_index in range(len(string) - pattern_length):
        distance = hamming_distance(pattern, string[start_index:start_index + pattern_length])
        if shortest == -1 or distance < shortest:
            shortest = distance

    return shortest


def motif_d(pattern, motifs):
    total = 0
    for motif in motifs:
        total += d(pattern, motif)
    return total


def get_median_strings(k, motifs):
    k_mers = product('ACGT', repeat=k)
    shortest = -1
    for k_mer in k_mers:
        k_mer_str = ''.join(k_mer)
        dist = motif_d(k_mer_str, motifs)
        if shortest == -1 or dist < shortest:
            shortest = dist
    median_strings = []
    k_mers = product('ACGT', repeat=k)
    for k_mer in k_mers:
        k_mer_str = ''.join(k_mer)
        if motif_d(k_mer_str, motifs) == shortest:
            median_strings.append(k_mer_str)

    return median_strings
