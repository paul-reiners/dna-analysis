import itertools
import math
from itertools import product


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


def get_consensus_strings(profile_matrix):
    n = len(profile_matrix['A'])
    epsilon = 0.01
    consensus_choices = []
    for i in range(n):
        max_prob = max(profile_matrix['A'][i], profile_matrix['C'][i], profile_matrix['T'][i], profile_matrix['G'][i])
        position_consensus = ''
        nucleotides = 'ACTG'
        for nucleotide in nucleotides:
            if abs(profile_matrix[nucleotide][i] - max_prob) < epsilon:
                position_consensus += nucleotide
        consensus_choices.append(position_consensus)
    prod = itertools.product(*consensus_choices)

    return map(lambda lst: ''.join(lst), prod)


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


def pr(pattern, profile):
    prob = 1.0
    for i in range(len(pattern)):
        nucleotide = pattern[i]
        prob *= profile[nucleotide][i]

    return prob


def compute_entropy(probs):
    eps = 0.01
    entropy = 0.0
    for prob in probs:
        if prob >= eps:
            entropy += -1 * prob * math.log(prob, 2)

    return entropy
