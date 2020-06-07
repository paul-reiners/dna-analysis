from chapter01.chapter01 import pattern_to_number, number_to_pattern


def test_pattern_to_number():
    assert pattern_to_number('GT') == 11


def test_pattern_to_number_2():
    actual_result = pattern_to_number('ATGCAA')
    expected_result = 912
    assert actual_result == expected_result


def test_number_to_pattern():
    assert number_to_pattern(11, 2) == 'GT'


def test_number_to_pattern_2():
    actual_result = number_to_pattern(5437, 7)
    expected_result = 'CCCATTC'
    assert actual_result == expected_result
