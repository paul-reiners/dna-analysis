from week02.chapter02 import frequent_words_with_mismatches, frequent_words_with_mismatches_and_reverse_complements


def test_frequent_words_with_mismatches():
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    computed_result = frequent_words_with_mismatches(text, k, d)
    expected_result = ['GATG', 'ATGC', 'ATGT']
    assert sorted(computed_result) == sorted(expected_result)


def test_frequent_words_with_mismatches_2():
    file1 = open('../../../data/week02/dataset_9_7.txt', 'r')
    lines = file1.readlines()
    text = lines[0].strip()
    k_and_d = lines[1].strip().split()
    k = int(k_and_d[0])
    d = int(k_and_d[1])
    calculated_output = frequent_words_with_mismatches(text, k, d)
    print(' '.join(map(lambda n: str(n), calculated_output)))


def test_frequent_words_with_mismatches_and_reverse_complements():
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    computed_result = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
    expected_result = ['ATGT', 'ACAT']
    assert sorted(computed_result) == sorted(expected_result)


def test_frequent_words_with_mismatches_and_reverse_complements_2():
    file1 = open('../../../data/week02/dataset_9_8.txt', 'r')
    lines = file1.readlines()
    text = lines[0].strip()
    k_and_d = lines[1].strip().split()
    k = int(k_and_d[0])
    d = int(k_and_d[1])
    calculated_output = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
    print(' '.join(map(lambda n: str(n), calculated_output)))
