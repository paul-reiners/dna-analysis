nucleotide_mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def get_reverse_complement(pattern):
    complement_chars = [nucleotide_mapping[c] for c in pattern]
    complement = ''.join([str(elem) for elem in complement_chars])
    reverse_complement = complement[::-1]

    return reverse_complement


def get_pattern_matches(pattern, genome):
    pattern_matches = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            pattern_matches.append(i)

    return pattern_matches
