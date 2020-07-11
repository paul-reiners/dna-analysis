from bioinformatics_ii.week2 import get_eulerian_cycle, get_eulerian_path


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


def test_get_eulerian_cycle_2():
    file1 = open('../../../data/bioinformatics_ii/week1/dataset_203_2.txt', 'r')
    lines = file1.readlines()
    lines = [line.strip() for line in lines]
    graph = {}
    for line in lines:
        key_and_value = line.split("->")
        key = int(key_and_value[0])
        value_strs = key_and_value[1].split(',')
        values = [int(s) for s in value_strs]
        graph[key] = values
    calculated_result = get_eulerian_cycle(graph)
    out_f = open('../../../data/bioinformatics_ii/week1/dataset_203_2_output.txt', 'w')
    calculated_result.append(calculated_result[0])
    output_line = '->'.join([str(n) for n in calculated_result])
    out_f.write(output_line)
    out_f.write("\n")


def test_get_eulerian_path():
    graph = {0: [2], 1: [3], 2: [1],  3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
    computed_result = get_eulerian_path(graph)
    expected_result = [6, 7, 8, 9, 6, 3, 0, 2, 1, 3, 4]
    assert computed_result == expected_result
