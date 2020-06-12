

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


def main():
    file1 = open('../data/chapter02/Salmonella_enterica.txt', 'r')
    lines = file1.readlines()
    genome = ''.join(map(lambda s: s.strip(), lines[1:]))
    calculated_output = get_minimum_skew_positions(genome)
    print(' '.join(map(lambda n: str(n), calculated_output)))
    L = 1000
    start = calculated_output[0]
    text = genome[start: start + L]
    k = 9
    d = 1
    candidates = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
    print(' '.join(candidates))


if __name__ == "__main__":
    main()
