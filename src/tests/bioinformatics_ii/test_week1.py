from itertools import product

from bioinformatics_ii.week1 import composition, path_to_genome, overlap_graph, construct_k_universal_string


def test_composition():
    text = 'CAATCCAAC'
    k = 5
    calculated_result = composition(text, k)
    expected_result = ['CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC']
    assert calculated_result == sorted(expected_result)


def test_composition_2():
    file1 = open('../../../data/bioinformatics_ii/week1/dataset_197_3.txt', 'r')
    lines = file1.readlines()
    k = int(lines[0].strip())
    text = lines[1].strip()
    calculated_result = composition(text, k)
    print('\n'.join(calculated_result))
    with open('../../../data/bioinformatics_ii/week1/dataset_197_3-OUTPUT.txt', 'w') as f:
        print('\r\n'.join(calculated_result), file=f, flush=True)


def test_string_spelled_genome_path():
    patterns = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']
    calculated_result = path_to_genome(patterns)
    expected_result = 'ACCGAAGCT'
    assert calculated_result == expected_result


def test_path_to_genome():
    file1 = open('../../../data/bioinformatics_ii/week1/dataset_198_3.txt', 'r')
    lines = file1.readlines()
    patterns = [line.strip() for line in lines]
    calculated_result = path_to_genome(patterns)
    print(calculated_result)


def test_overlap_graph():
    patterns = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC']
    calculated_output = overlap_graph(patterns)
    expected_output = {'CATGC': ['ATGCG'], 'GCATG': ['CATGC'], 'GGCAT': ['GCATG'], 'AGGCA': ['GGCAC', 'GGCAT']}
    for key, value in calculated_output.items():
        if key in expected_output:
            assert(sorted(value) == sorted(expected_output[key]))
        else:
            assert len(value) == 0
    for key, value in expected_output.items():
        assert sorted(calculated_output[key]) == sorted(value)


def test_overlap_graph_2():
    file1 = open('../../../data/bioinformatics_ii/week1/dataset_198_10.txt', 'r')
    lines = file1.readlines()
    patterns = [line.strip() for line in lines]
    calculated_result = overlap_graph(patterns)
    out_f = open('../../../data/bioinformatics_ii/week1/dataset_198_10_output.txt', 'w')
    for key, value in calculated_result.items():
        if len(value) > 0:
            output_line = "%s->%s" % (key, ",".join(value))
            out_f.write(output_line)
            out_f.write("\n")


def test_construct_3_universal_string():
    result = construct_k_universal_string(3)
    all_3_mers = [''.join(p) for p in product('01', repeat=3)]
    for three_mer in all_3_mers:
        assert result.count(three_mer) == 1
