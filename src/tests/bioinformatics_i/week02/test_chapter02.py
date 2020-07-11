from bioinformatics_i.week02.chapter02 import frequent_words_with_mismatches, \
    frequent_words_with_mismatches_and_reverse_complements


def test_frequent_words_with_mismatches():
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    computed_result = frequent_words_with_mismatches(text, k, d)
    expected_result = ['GATG', 'ATGC', 'ATGT']
    assert sorted(computed_result) == sorted(expected_result)


def test_frequent_words_with_mismatches_and_reverse_complements():
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    computed_result = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
    expected_result = ['ATGT', 'ACAT']
    assert sorted(computed_result) == sorted(expected_result)
