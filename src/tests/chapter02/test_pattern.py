from chapter02.pattern import get_reverse_complement


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
