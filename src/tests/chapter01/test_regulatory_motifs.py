from chapter01.regulatory_motifs import d, motif_d, get_median_strings, pr, compute_entropy, get_consensus_strings, \
    count, score, profile


def test_d():
    pattern = 'GATTCTCA'
    string = 'GCAAAGACGCTGACCAA'
    distance = d(pattern, string)
    assert distance == 3


def test_motif_d():
    pattern = 'AAA'
    dna = {'TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT'}
    distance = motif_d(pattern, dna)
    assert distance == 5


def test_get_median_strings():
    motifs = {'AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTTCGGGACAG'}
    computed_median_strings = set(get_median_strings(3, motifs))
    expected_median_strings = {'GAC'}
    assert computed_median_strings == expected_median_strings


def test_get_median_strings_2():
    motifs = {'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
              'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
              'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'}
    computed_median_strings = set(get_median_strings(7, motifs))
    expected_median_strings = {'AATCCTA', 'GAACCAC', 'GTAGGAA'}
    assert computed_median_strings == expected_median_strings


def test_pr():
    profile = {
        'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
        'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
        'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
        'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
    }
    result = pr('CAGTGA', profile)
    print(result)


def test_pr_2():
    profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.0],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
    }
    result = pr('TCGTGGATTTCC', profile)
    assert abs(result - 0.0) < 0.01


def test_compute_entropy():
    epsilon = 0.01
    probs1 = [0.2, 0.6, 0.0, 0.2]
    entropy1 = compute_entropy(probs1)
    assert abs(entropy1 - 1.371) < epsilon

    probs2 = [0.0, 0.6, 0.0, 0.4]
    entropy2 = compute_entropy(probs2)
    assert abs(entropy2 - 0.971) < epsilon

    probs3 = [0.0, 0.0, 0.9, 0.1]
    entropy3 = compute_entropy(probs3)
    assert abs(entropy3 - 0.467) < epsilon


def test_get_consensus_strings():
    probs = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
             'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
             'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
             'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
    computed_consensus_strings = set(get_consensus_strings(probs))
    expected_consensus_strings = {'AAGCGA', 'ACGCGA', 'AGGCGA', 'AAGTGA', 'ACGTGA', 'AGGTGA', 'AAGCTA', 'ACGCTA',
                                  'AGGCTA', 'AAGTTA', 'ACGTTA', 'AGGTTA'}

    assert computed_consensus_strings == expected_consensus_strings


def test_get_consensus_strings_2():
    probs = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
             'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
             'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
             'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
    computed_consensus_strings = set(get_consensus_strings(probs))
    expected_consensus_strings = \
        {'AGGCGA', 'AAGCGA', 'ACGTTA', 'AGGTTA', 'ACGCGA', 'AAGCTA', 'ACGTGA', 'AGGCTA', 'AAGTTA', 'ACGCTA', 'AGGTGA',
         'AAGTGA'}
    assert computed_consensus_strings == expected_consensus_strings


def test_count():
    motifs = [['T', 'C', 'G', 'G', 'G', 'G', 'g', 'T', 'T', 'T', 't', 't'],
              ['c', 'C', 'G', 'G', 't', 'G', 'A', 'c', 'T', 'T', 'a', 'C'],
              ['a', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'T', 't', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 't', 't'],
              ['a', 'a', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'a', 't'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'C', 't'],
              ['T', 'a', 'G', 'G', 'G', 'G', 'A', 'a', 'c', 'T', 'a', 'C'],
              ['T', 'C', 'G', 'G', 'G', 't', 'A', 'T', 'a', 'a', 'C', 'C']]
    computed_result = count(motifs)
    expected_result = {'A': [2, 2,  0,  0, 0, 0, 9, 1, 1, 1, 3, 0],
                       'C': [1, 6,  0,  0, 0, 0, 0, 4, 1, 2, 4, 6],
                       'G': [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0],
                       'T': [7, 2,  0,  0, 1, 1, 0, 5, 8, 7, 3, 4]}
    for nucleotide in 'ACGT':
        assert computed_result[nucleotide] == expected_result[nucleotide]


def test_profile():
    motifs = [['T', 'C', 'G', 'G', 'G', 'G', 'g', 'T', 'T', 'T', 't', 't'],
              ['c', 'C', 'G', 'G', 't', 'G', 'A', 'c', 'T', 'T', 'a', 'C'],
              ['a', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'T', 't', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 't', 't'],
              ['a', 'a', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'a', 't'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'C', 't'],
              ['T', 'a', 'G', 'G', 'G', 'G', 'A', 'a', 'c', 'T', 'a', 'C'],
              ['T', 'C', 'G', 'G', 'G', 't', 'A', 'T', 'a', 'a', 'C', 'C']]
    computed_result = profile(motifs)
    expected_result = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
                       'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
                       'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
                       'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
    for nucleotide in 'ACGT':
        assert computed_result[nucleotide] == expected_result[nucleotide]


def test_score():
    motifs = [['T', 'C', 'G', 'G', 'G', 'G', 'g', 'T', 'T', 'T', 't', 't'],
              ['c', 'C', 'G', 'G', 't', 'G', 'A', 'c', 'T', 'T', 'a', 'C'],
              ['a', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'T', 't', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 't', 't'],
              ['a', 'a', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 't', 'G', 'G', 'G', 'G', 'A', 'c', 'T', 'T', 'C', 'C'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'a', 't'],
              ['T', 'C', 'G', 'G', 'G', 'G', 'A', 'T', 'T', 'c', 'C', 't'],
              ['T', 'a', 'G', 'G', 'G', 'G', 'A', 'a', 'c', 'T', 'a', 'C'],
              ['T', 'C', 'G', 'G', 'G', 't', 'A', 'T', 'a', 'a', 'C', 'C']]
    computed_result = score(motifs)
    expected_result = 9.916290005356972
    assert abs(computed_result - expected_result) < 0.1


def test_get_median_strings_3():
    file1 = open('../../../data/chapter01/dataset_158_9.txt', 'r')
    lines = file1.readlines()
    k = int(lines[0].strip())
    motifs = list(map(lambda s: s.strip(), lines[1:]))
    computed_output = get_median_strings(k, motifs)
    print(' '.join(map(lambda s: str(s), computed_output)))
