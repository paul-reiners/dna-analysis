from itertools import product

from chapter01.hamming import count
from chapter01.pattern import get_reverse_complement


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
            frequenwt_words.append(k)

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
