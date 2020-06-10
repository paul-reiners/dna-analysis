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
