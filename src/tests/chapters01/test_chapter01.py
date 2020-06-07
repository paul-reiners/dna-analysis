from chapter01.chapter01 import pattern_to_number, number_to_pattern


def test_pattern_to_number():
    assert pattern_to_number('GT') == 11


def test_number_to_pattern():
    assert number_to_pattern(11, 2) == 'GT'
