from bioinformatics_ii.week2 import get_eulerian_cycle
from collections import deque


def test_get_eulerian_cycle():
    graph = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
    computed_result = get_eulerian_cycle(graph)
    expected_result = deque([6, 8, 7, 9, 6, 5, 4, 2, 1, 0, 3, 2])
    n = len(expected_result)
    assert len(computed_result) == n
    rotations = [expected_result.rotate(i) for i in range(n)]
    assert computed_result in rotations
