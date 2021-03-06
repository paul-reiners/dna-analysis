from bioinformatics_i.week01.chapter01 import pattern_to_number, number_to_pattern, computing_frequencies, \
    better_clump_finding


def test_pattern_to_number():
    assert pattern_to_number('GT') == 11


def test_pattern_to_number_2():
    actual_result = pattern_to_number('ATGCAA')
    expected_result = 912
    assert actual_result == expected_result


def test_pattern_to_number_3():
    actual_result = pattern_to_number('AGT')
    expected_result = 11
    assert actual_result == expected_result


def test_number_to_pattern():
    assert number_to_pattern(11, 2) == 'GT'


def test_number_to_pattern_2():
    actual_result = number_to_pattern(5437, 7)
    expected_result = 'CCCATTC'
    assert actual_result == expected_result


def test_number_to_pattern_3():
    actual_result = number_to_pattern(5437, 8)
    expected_result = 'ACCCATTC'
    assert actual_result == expected_result


def test_number_to_pattern_4():
    actual_result = number_to_pattern(45, 4)
    expected_result = 'AGTC'
    assert actual_result == expected_result


def test_number_to_pattern_5():
    actual_result = number_to_pattern(5765, 11)
    expected_result = 'AAAACCGGACC'
    assert actual_result == expected_result


def test_computing_frequencies():
    text = 'ACGCGGCTCTGAAA'
    k = 2
    computed_result = computing_frequencies(text, k)
    expected_output = [2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0]
    assert computed_result == expected_output


def test_better_clump_finding():
    genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    k = 5
    l = 50
    t = 4
    calculated_output = better_clump_finding(genome, k, t, l)
    expected_output = {'CGACA', 'GAAGA'}
    assert expected_output == calculated_output
