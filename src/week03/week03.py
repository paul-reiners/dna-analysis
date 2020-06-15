from chapter01.regulatory_motifs import pr, score, profile_with_pseudocounts


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


def greedy_motif_search(dna, k, t):
    best_motifs = [s[:k] for s in dna]
    motifs = [''] * t
    for start in range(len(dna[0]) - k + 1):
        motif = dna[0][start:start + k]
        motifs[0] = motif
        for i in range(1, t):
            next_profile = profile_with_pseudocounts(motifs[:i])
            motifs[i] = get_profile_most_probable_k_mer(dna[i], k, next_profile)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]

    return best_motifs
