from itertools import product

from bioinformatics_ii.week1 import composition, path_to_genome, overlap_graph, \
    construct_de_bruijn_graph, construct_de_bruijn_graph_from_k_mers
from bioinformatics_ii.week2 import get_k_universal_circular_string, get_binary_strings


def test_composition():
    text = 'CAATCCAAC'
    k = 5
    calculated_result = composition(text, k)
    expected_result = ['CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC']
    assert calculated_result == sorted(expected_result)


def test_string_spelled_genome_path():
    patterns = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']
    calculated_result = path_to_genome(patterns)
    expected_result = 'ACCGAAGCT'
    assert calculated_result == expected_result


def test_overlap_graph():
    patterns = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'GGCAC']
    calculated_output = overlap_graph(patterns)
    expected_output = {'CATGC': ['ATGCG'], 'GCATG': ['CATGC'], 'GGCAT': ['GCATG'], 'AGGCA': ['GGCAC', 'GGCAT']}
    for key, value in calculated_output.items():
        if key in expected_output:
            assert (sorted(value) == sorted(expected_output[key]))
        else:
            assert len(value) == 0
    for key, value in expected_output.items():
        assert sorted(calculated_output[key]) == sorted(value)


def test_construct_3_universal_string():
    k = 3
    result = get_k_universal_circular_string(k)
    n = 8
    assert n == len(result)
    patterns = get_binary_strings(k)
    for pattern in patterns:
        found_pattern = False
        for i in range(n):
            rotation = result[i:] + result[:i]
            if pattern in rotation:
                found_pattern = True

                break
        assert found_pattern


def test_construct_4_universal_string():
    k = 4
    result = get_k_universal_circular_string(k)
    n = 16
    assert n == len(result)
    patterns = get_binary_strings(k)
    for pattern in patterns:
        found_pattern = False
        for i in range(n):
            rotation = result[i:] + result[:i]
            if pattern in rotation:
                found_pattern = True

                break
        assert found_pattern


def test_construct_de_bruijn_graph():
    k = 4
    text = 'AAGATTCTCTAAGA'
    computed_result = construct_de_bruijn_graph(k, text)
    expected_result = {'AAG': ['AGA', 'AGA'], 'AGA': ['GAT'], 'ATT': ['TTC'], 'CTA': ['TAA'], 'CTC': ['TCT'],
                       'GAT': ['ATT'], 'TAA': ['AAG'], 'TCT': ['CTA', 'CTC'], 'TTC': ['TCT']}
    for key, value in computed_result.items():
        assert (sorted(value) == sorted(expected_result[key]))
    for key, value in expected_result.items():
        assert sorted(computed_result[key]) == sorted(value)


def test_construct_de_bruijn_graph_from_k_mers():
    patterns = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
    computed_result = construct_de_bruijn_graph_from_k_mers(patterns)
    expected_result = {'AGG': ['GGG'], 'CAG': ['AGG', 'AGG'], 'GAG': ['AGG'], 'GGA': ['GAG'], 'GGG': ['GGA', 'GGG']}
    for key, value in computed_result.items():
        assert (sorted(value) == sorted(expected_result[key]))
    for key, value in expected_result.items():
        assert sorted(computed_result[key]) == sorted(value)
