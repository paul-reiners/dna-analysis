from regulatory_motifs import d, motif_d


def test_d():
    pattern = 'GATTCTCA'
    string = 'GCAAAGACGCTGACCAA'
    distance = d(pattern, string)
    assert distance == 3


def test_motif_d():
    pattern = 'AAA'
    dna = {'TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT'}
    distance = motif_d(pattern, dna)
    assert distance == 5
