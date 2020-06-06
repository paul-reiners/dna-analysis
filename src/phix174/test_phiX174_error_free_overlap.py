from phix174.phiX174_error_free_overlap import pattern_count, frequent_words


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


def test_frequent_words():
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    computed_output = frequent_words(text, k)
    expected_output = ['CATG', 'GCAT']
    assert sorted(computed_output) == sorted(expected_output)


def test_frequent_words_2():
    file1 = open('../../data/chapter01/dataset_2_10.txt', 'r')
    lines = file1.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    computed_output = frequent_words(text, k)
    expected_output = ['GCACGGTATTGC', 'TTGCACGGTATT']
    assert sorted(computed_output) == sorted(expected_output)
