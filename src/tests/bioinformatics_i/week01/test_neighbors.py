from bioinformatics_i.week01.neighbors import neighbors


def test_neighbors():
    pattern = 'ACG'
    d = 1
    computed_output = neighbors(pattern, d)
    expected_output = ['CCG', 'TCG', 'GCG', 'AAG', 'ATG', 'AGG', 'ACA', 'ACC', 'ACT', 'ACG']
    assert sorted(computed_output) == sorted(expected_output)
