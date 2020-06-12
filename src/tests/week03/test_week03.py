from week03.week03 import get_profile_most_probable_k_mer, greedy_motif_search


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


def test_get_profile_most_probable_k_mer_2():
    file1 = open('../../../data/week03/dataset_159_3.txt', 'r')
    lines = file1.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    profile = {'A': list(map(lambda s: float(s), lines[2].strip().split())),
               'C': list(map(lambda s: float(s), lines[3].strip().split())),
               'G': list(map(lambda s: float(s), lines[4].strip().split())),
               'T': list(map(lambda s: float(s), lines[5].strip().split()))}
    calculated_output = get_profile_most_probable_k_mer(text, k, profile)
    print(calculated_output)


def test_greedy_motif_search():
    dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
    k = 3
    t = 5
    calculated_result = greedy_motif_search(dna, k, t)
    expected_result = ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
    assert calculated_result == expected_result
