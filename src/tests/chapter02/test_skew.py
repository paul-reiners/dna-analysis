from chapter02.skew import get_minimum_skew_positions


def test_get_minimum_skew_positions():
    genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    computed_value = get_minimum_skew_positions(genome)
    expected_value = [11, 24]
    assert computed_value == expected_value


def test_get_minimum_skew_positions_2():
    file1 = open('../../../data/chapter02/dataset_7_6.txt', 'r')
    lines = file1.readlines()
    genome = lines[0].strip()
    calculated_output = get_minimum_skew_positions(genome)
    print(' '.join(map(lambda n: str(n), calculated_output)))
