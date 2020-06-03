from regulatory_motifs import d


def test_d():
    pattern = 'GATTCTCA'
    string = 'GCAAAGACGCTGACCAA'
    distance = d(pattern, string)
    assert distance == 3
