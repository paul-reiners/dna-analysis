from bioinformatics_i.week01.hamming import approximate_pattern_count
from bioinformatics_i.week01.neighbors import neighbors


def motif_enumeration(dna, k, d):
    patterns = set()
    for dna_str in dna:
        for i in range(len(dna_str) - k + 1):
            k_mer = dna_str[i:i + k]
            for neighbor in neighbors(k_mer, d):
                if all(map(lambda s: approximate_pattern_count(s, neighbor, d) > 0, dna)):
                    patterns.add(neighbor)

    return patterns
