from bioinformatics_i.week03.week03 import get_profile_most_probable_k_mer, greedy_motif_search, \
    distance_between_pattern_and_strings


def test_get_profile_most_probable_k_mer():
    text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    k = 5
    profile = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],
               'C': [0.4, 0.3, 0.1, 0.5, 0.1],
               'G': [0.3, 0.3, 0.5, 0.2, 0.4],
               'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
    computed_result = get_profile_most_probable_k_mer(text, k, profile)
    expected_result = 'CCGAG'
    assert computed_result == expected_result


def test_greedy_motif_search():
    dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    k = 3
    t = 5
    calculated_result = greedy_motif_search(dna, k, t)
    expected_result = ['TTC', 'ATC', 'TTC', 'ATC', 'TTC']
    assert calculated_result == expected_result


def test_distance_between_pattern_and_strings():
    pattern = 'AAA'
    dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
    computed_result = distance_between_pattern_and_strings(pattern, dna)
    expected_result = 5
    assert computed_result == expected_result
