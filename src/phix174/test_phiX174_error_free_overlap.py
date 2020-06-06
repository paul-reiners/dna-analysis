from phix174.phiX174_error_free_overlap import pattern_count


def test_pattern_count():
    assert pattern_count('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT') == 3


def test_pattern_count_2():
    assert pattern_count('GCGCG', 'GCG') == 2
