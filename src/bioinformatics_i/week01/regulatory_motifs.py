import itertools
import math
from itertools import product

from bioinformatics_i.week01.hamming import hamming_distance


def d(pattern, string):
    shortest = -1
    pattern_length = len(pattern)
    for start_index in range(len(string) - pattern_length + 1):
        sub_string = string[start_index:start_index + pattern_length]
        distance = hamming_distance(pattern, sub_string)
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


def pr(pattern, prfl):
    prob = 1.0
    for i in range(len(pattern)):
        nucleotide = pattern[i]
        prob *= prfl[nucleotide][i]

    return prob


def compute_entropy(probs):
    eps = 0.01
    entropy = 0.0
    for prob in probs:
        if prob >= eps:
            entropy += -1 * prob * math.log(prob, 2)

    return entropy


def score(motifs):
    p = profile(motifs)
    n = len(p['A'])
    entropies = [0.0] * n
    for i in range(n):
        col = [p[nucleotide][i] for nucleotide in 'ACGT']
        entropies[i] = compute_entropy(col)

    return sum(entropies)


def count(motifs):
    row_count = len(motifs)
    col_count = len(motifs[0])
    counts = {'A': [0] * col_count, 'C': [0] * col_count, 'G': [0] * col_count, 'T': [0] * col_count}
    for col in range(col_count):
        for row in range(row_count):
            nucleotide = motifs[row][col].upper()
            counts[nucleotide][col] += 1

    return counts


def count_with_pseudocounts(motifs):
    row_count = len(motifs)
    col_count = len(motifs[0])
    counts = {'A': [1] * col_count, 'C': [1] * col_count, 'G': [1] * col_count, 'T': [1] * col_count}
    for col in range(col_count):
        for row in range(row_count):
            nucleotide = motifs[row][col].upper()
            counts[nucleotide][col] += 1

    return counts


def profile(motifs):
    n = len(motifs)
    profile_dict = {}
    counts = count(motifs)
    for nucleotide in counts:
        profile_dict[nucleotide] = list(map(lambda k: k / n, counts[nucleotide]))

    return profile_dict


def profile_with_pseudocounts(motifs):
    n = len(motifs)
    profile_dict = {}
    counts = count_with_pseudocounts(motifs)
    for nucleotide in counts:
        profile_dict[nucleotide] = list(map(lambda k: k / (n + len(motifs[0])), counts[nucleotide]))

    return profile_dict
