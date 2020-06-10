from chapter01.hamming import hamming_distance, find_approximate_pattern_matches


def test_hamming_distance():
    s1 = 'GGGCCGTTGGT'
    s2 = 'GGACCGTTGAC'
    computed_result = hamming_distance(s1, s2)
    expected_result = 3
    assert computed_result == expected_result


def test_hamming_distance_2():
    file1 = open('../../../data/chapter01/dataset_9_3.txt', 'r')
    lines = file1.readlines()
    s1 = lines[0].strip()
    s2 = lines[1].strip()
    calculated_output = hamming_distance(s1, s2)
    print(calculated_output)


def test_find_approximate_pattern_matches():
    pattern = 'ATTCTGGA'
    text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    d = 3
    computed_result = find_approximate_pattern_matches(pattern, text, d)
    expected_result = [6, 7, 26, 27]
    assert computed_result == expected_result


def test_find_approximate_pattern_matche_2():
    file1 = open('../../../data/chapter01/dataset_9_4.txt', 'r')
    lines = file1.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = int(lines[2].strip())
    calculated_output = find_approximate_pattern_matches(pattern, text, d)
    print(' '.join(map(lambda n: str(n), calculated_output)))
