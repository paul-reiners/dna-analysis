import random

from week04.week04 import monte_carlo_randomized_motif_search, get_most_likely_motif


def test_monte_carlo_randomized_motif_search():
    dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
           'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    k = 8
    t = 5
    computed_result = monte_carlo_randomized_motif_search(dna, k, t)
    expected_result = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
    assert computed_result == expected_result


def test_monte_carlo_randomized_motif_search_2():
    random.seed(0)
    file1 = open('../../../data/week04/dataset_161_5.txt', 'r')
    lines = file1.readlines()
    k, t = [int(s) for s in lines[0].strip().split()]
    dna = list(map(lambda line: line.strip(), lines[1:]))
    calculated_result = monte_carlo_randomized_motif_search(dna, k, t)
    with open('OUTPUTFILENAME.txt', 'w') as f:
        print('\r\n'.join(calculated_result), file=f, flush=True)


def test_get_most_likely_motif():
    profile = {'A': [4/5,   0,   0, 1/5],
               'C': [  0, 3/5, 1/5,   0],
               'G': [1/5, 1/5, 4/5,   0],
               'T': [  0, 1/5,   0, 4/5]}
    dna = ['ttaccttaac',
           'gatgtctgtc',
           'acggcgttag',
           'ccctaacgag']
    computed_result = get_most_likely_motif(profile, dna[0])
    expected_result = "acct"
    assert computed_result == expected_result
