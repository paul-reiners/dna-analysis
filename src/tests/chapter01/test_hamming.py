from chapter01.hamming import hamming_distance


def test_hamming_distance():
    s1 = 'GGGCCGTTGGT'
    s2 = 'GGACCGTTGAC'
    computed_result = hamming_distance(s1, s2)
    expected_result = 3
    assert computed_result == expected_result
