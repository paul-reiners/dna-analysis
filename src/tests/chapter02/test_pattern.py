from chapter02.pattern import get_reverse_complement


def test_get_reverse_complement():
    pattern = 'AAAACCCGGT'
    computed_output = get_reverse_complement(pattern)
    expected_output = 'ACCGGGTTTT'
    assert computed_output == expected_output
