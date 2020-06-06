from chapter02.pattern import get_reverse_complement, get_pattern_matches


def test_get_reverse_complement():
    pattern = 'AAAACCCGGT'
    computed_output = get_reverse_complement(pattern)
    expected_output = 'ACCGGGTTTT'
    assert computed_output == expected_output


def test_get_reverse_complement_2():
    file1 = open('../../../data/chapter01/dataset_3_2.txt', 'r')
    lines = file1.readlines()
    pattern = lines[0].strip()
    computed_output = get_reverse_complement(pattern)
    print(computed_output)


def test_get_pattern_matches():
    pattern = 'ATAT'
    genome = 'GATATATGCATATACTT'
    computed_output = get_pattern_matches(pattern, genome)
    expected_output = [1, 3, 9]
    assert computed_output == expected_output
