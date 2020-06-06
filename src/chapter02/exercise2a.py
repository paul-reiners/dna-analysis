from chapter02.neighbors import neighbors
from section01.hamming import approximate_pattern_count


def motif_enumeration(dna, k, d):
    patterns = set()
    for i in range(len(dna[0]) - k + 1):
        k_mer = dna[0][i:i + k]
        for neighbor in neighbors(k_mer, d):
            if all(map(lambda s: approximate_pattern_count(s, neighbor, d) > 0, dna)):
                patterns.add(neighbor)

    return patterns
