from week03.week03 import get_profile_most_probable_k_mer


def test_get_profile_most_probable_k_mer():
    text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    k = 5
    profile = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],
               'C': [0.4, 0.3, 0.1, 0.5, 0.1],
               'G': [0.3, 0.3, 0.5, 0.2, 0.4],
               'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
    computed_result = get_profile_most_probable_k_mer(text, k, profile)
    expected_result = 'CCGAG'
    assert computed_result == expected_result
