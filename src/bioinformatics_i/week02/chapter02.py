from itertools import product

from bioinformatics_i.week01.hamming import count
from bioinformatics_i.week01.pattern import get_reverse_complement


def get_all_k_mers(k):
    return product('ACGT', repeat=k)


def frequent_words_with_mismatches(text, k, d):
    k_mers = get_all_k_mers(k)
    k_mer_to_freq = {}
    max_count = -1
    for k_mer in k_mers:
        k_mer_str = ''.join(k_mer)
        n = count(text, k_mer_str, d)
        if n > max_count:
            max_count = n
        k_mer_to_freq[k_mer_str] = n
    frequent_words = []
    for k in k_mer_to_freq:
        n = k_mer_to_freq[k]
        if n == max_count:
            frequent_words.append(k)

    return frequent_words


def frequent_words_with_mismatches_and_reverse_complements(text, k, d):
    k_mers = get_all_k_mers(k)
    k_mer_to_freq = {}
    max_count = -1
    for k_mer in k_mers:
        k_mer_str = ''.join(k_mer)
        reverse_complement = get_reverse_complement(k_mer_str)
        n = count(text, k_mer_str, d) + count(text, reverse_complement, d)
        if n > max_count:
            max_count = n
        k_mer_to_freq[k_mer_str] = n
    frequent_words = []
    for k in k_mer_to_freq:
        n = k_mer_to_freq[k]
        if n == max_count:
            frequent_words.append(k)

    return frequent_words


def get_skew(genome):
    n = len(genome)
    skew = [0] * (n + 1)
    for i in range(n):
        nucleotide = genome[i]
        prev = skew[i]
        next_skew = prev
        if nucleotide == 'G':
            next_skew += 1
        elif nucleotide == 'C':
            next_skew -= 1
        skew[i + 1] = next_skew

    return skew


def get_minimum_skew_positions(genome):
    skew = get_skew(genome)
    min_skew = min(skew)
    min_skew_pos = list(filter(lambda i: skew[i] == min_skew, range(len(skew))))

    return min_skew_pos


def get_maximum_skew_positions(genome):
    skew = get_skew(genome)
    max_skew = max(skew)
    max_skew_pos = list(filter(lambda i: skew[i] == max_skew, range(len(skew))))

    return max_skew_pos
