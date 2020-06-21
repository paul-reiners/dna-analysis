from bioinformatics_ii.week1 import composition


def test_composition():
    text = 'CAATCCAAC'
    k = 5
    calculated_result = composition(text, k)
    expected_result = ['CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC']
    assert calculated_result == sorted(expected_result)
