from week02.neighbors import neighbors


def test_neighbors():
    pattern = 'ACG'
    d = 1
    computed_output = neighbors(pattern, d)
    expected_output = ['CCG', 'TCG', 'GCG', 'AAG', 'ATG', 'AGG', 'ACA', 'ACC', 'ACT', 'ACG']
    assert sorted(computed_output) == sorted(expected_output)


def test_neighbors_2():
    file1 = open('../../data/chapter02/dataset_3014_4.txt', 'r')
    lines = file1.readlines()
    pattern = lines[0].strip()
    d = int(lines[1])
    computed_output = neighbors(pattern, d)
    print(' '.join(sorted(computed_output)))
