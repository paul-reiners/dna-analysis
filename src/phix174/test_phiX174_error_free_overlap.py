from phix174.phiX174_error_free_overlap import pattern_count


def test_pattern_count():
    assert pattern_count('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT') == 3


def test_pattern_count_2():
    assert pattern_count('GCGCG', 'GCG') == 2


def test_neighbors_3():
    file1 = open('../../data/chapter01/dataset_2_7.txt', 'r')
    lines = file1.readlines()
    text = lines[0].strip()
    pattern = lines[1].strip()
    computed_output = pattern_count(text, pattern)
    assert computed_output == 24
