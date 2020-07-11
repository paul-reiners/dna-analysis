from bioinformatics_i.week02.skew import get_minimum_skew_positions


def test_get_minimum_skew_positions():
    genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    computed_value = get_minimum_skew_positions(genome)
    expected_value = [11, 24]
    assert computed_value == expected_value
