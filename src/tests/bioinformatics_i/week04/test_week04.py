import random

from bioinformatics_i.week04.week04 import monte_carlo_randomized_motif_search, motifs, get_most_likely_motif, \
    gibbs_sampler_with_restarts


def test_monte_carlo_randomized_motif_search():
    random.seed(30)
    dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
           'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    k = 8
    t = 5
    computed_result = monte_carlo_randomized_motif_search(dna, k, t)
    expected_result = ['AACGGCCA', 'AAGTGCCA', 'TAGTACCG', 'AAGTTTCA', 'ACGTGCAA']
    assert computed_result == expected_result


def test_get_most_likely_motif():
    profile = {'A': [4 / 5, 0, 0, 1 / 5],
               'C': [0, 3 / 5, 1 / 5, 0],
               'G': [1 / 5, 1 / 5, 4 / 5, 0],
               'T': [0, 1 / 5, 0, 4 / 5]}
    dna = ['ttaccttaac',
           'gatgtctgtc',
           'acggcgttag',
           'ccctaacgag']
    computed_result = get_most_likely_motif(profile, dna[0])
    expected_result = "acct"
    assert computed_result == expected_result


def test_motifs():
    profile = {'A': [4 / 5, 0, 0, 1 / 5],
               'C': [0, 3 / 5, 1 / 5, 0],
               'G': [1 / 5, 1 / 5, 4 / 5, 0],
               'T': [0, 1 / 5, 0, 4 / 5]}
    dna = ['ttaccttaac',
           'gatgtctgtc',
           'acggcgttag',
           'ccctaacgag',
           'cgtcagaggt']
    computed_result = motifs(profile, dna)
    expected_result = ["acct",
                       "atgt",
                       "gcgt",
                       "acga",
                       "aggt"]
    assert computed_result == expected_result


def test_gibbs_sampler():
    random.seed(30)
    dna = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
           'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    k = 8
    t = 5
    n = 100
    computed_results = gibbs_sampler_with_restarts(dna, k, t, n)
    expected_results = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
    assert computed_results == expected_results
