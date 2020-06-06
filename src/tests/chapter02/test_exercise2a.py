from chapter02.exercise2a import motif_enumeration


def test_motif_enumeration():
    k = 3
    d = 1
    dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
    computed_result = motif_enumeration(dna, k, d)
    expected_output = {"ATA", "ATT", "GTT", "TTT"}

    assert computed_result == expected_output


def test_motif_enumeration_2():
    file1 = open('../../data/chapter02/dataset_156_8.txt', 'r')
    lines = file1.readlines()
    line1 = lines[0].strip().split()
    k = int(line1[0])
    d = int(line1[1])
    dna = list(map(lambda s: s.strip(), lines[1:]))
    calculated_output = motif_enumeration(dna, k, d)
    print(' '.join(sorted(calculated_output)))
