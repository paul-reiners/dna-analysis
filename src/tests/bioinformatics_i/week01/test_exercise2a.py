from bioinformatics_i.week01.exercise2a import motif_enumeration


def test_motif_enumeration():
    k = 3
    d = 1
    dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
    computed_result = motif_enumeration(dna, k, d)
    expected_output = {"ATA", "ATT", "GTT", "TTT"}

    assert computed_result == expected_output
