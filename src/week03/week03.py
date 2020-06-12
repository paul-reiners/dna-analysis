from chapter01.regulatory_motifs import pr


def get_profile_most_probable_k_mer(text, k, profile):
    largest_prob = -1.0
    best = None
    for start in range(len(text) - k + 1):
        k_mer = text[start:start + k]
        prob = pr(k_mer, profile)
        if prob > largest_prob:
            best = k_mer
            largest_prob = prob

    return best
