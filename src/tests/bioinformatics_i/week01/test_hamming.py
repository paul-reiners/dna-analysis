from bioinformatics_i.week01.hamming import hamming_distance, find_approximate_pattern_matches, count


def test_hamming_distance():
    s1 = 'GGGCCGTTGGT'
    s2 = 'GGACCGTTGAC'
    computed_result = hamming_distance(s1, s2)
    expected_result = 3
    assert computed_result == expected_result


def test_find_approximate_pattern_matches():
    pattern = 'ATTCTGGA'
    text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    d = 3
    computed_result = find_approximate_pattern_matches(text, pattern, d)
    expected_result = [6, 7, 26, 27]
    assert computed_result == expected_result


def test_count():
    text = 'AACAAGCTGATAAACATTTAAAGAG'
    pattern = 'AAAAA'
    d = 2
    calculated_result = count(text, pattern, d)
    print(calculated_result)


def test_count_2():
    text = 'TTTAGAGCCTTCAGAGG'
    pattern = 'GAGG'
    d = 2
    calculated_result = count(text, pattern, d)
    expected_result = 4
    assert calculated_result == expected_result
