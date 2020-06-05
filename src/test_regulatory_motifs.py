import math

from regulatory_motifs import d, motif_d, get_median_strings, pr, compute_entropy, get_consensus_strings


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
    motifs = {'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
              'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
              'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'}
    median_strings = get_median_strings(7, motifs)
    print(median_strings)


def test_pr():
    profile = {
        'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
        'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
        'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
        'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
    }
    result = pr('CAGTGA', profile)
    print(result)


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
