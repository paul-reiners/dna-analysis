from bioinformatics_ii.week2 import get_eulerian_cycle, get_eulerian_path, string_reconstruction, \
    get_k_universal_circular_string, get_binary_strings


def test_get_eulerian_cycle():
    graph = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
    computed_result = get_eulerian_cycle(graph)
    expected_result = [6, 8, 7, 9, 6, 5, 4, 2, 1, 0, 3, 2]
    n = len(expected_result)
    assert len(computed_result) == n
    found = False
    for i in range(n):
        rotation = expected_result[i:] + expected_result[:i]
        if rotation == computed_result:
            found = True

            break

    assert found


def test_get_eulerian_path():
    graph = {0: [2], 1: [3], 2: [1], 3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
    computed_result = get_eulerian_path(graph)
    expected_result = [6, 7, 8, 9, 6, 3, 0, 2, 1, 3, 4]
    assert computed_result == expected_result


def test_string_reconstruction():
    patterns = ['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC']
    calculated_output = string_reconstruction(patterns)
    expected_result = 'GGCTTACCA'
    assert calculated_output == expected_result


def test_get_k_universal_circular_string():
    k = 4
    computed_result = get_k_universal_circular_string(k)
    n = 16
    assert n == len(computed_result)
    patterns = get_binary_strings(k)
    for pattern in patterns:
        found_pattern = False
        for i in range(n):
            rotation = computed_result[i:] + computed_result[:i]
            if pattern in rotation:
                found_pattern = True

                break
        assert found_pattern
