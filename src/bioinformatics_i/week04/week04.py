import random

from week01.hamming import hamming_distance
from week01.regulatory_motifs import profile_with_pseudocounts, get_consensus_strings


def monte_carlo_randomized_motif_search(dna, k, t):
    best_score = -1
    best_motifs = None
    for i in range(1000):
        next_motifs = randomized_motif_search(dna, k, t)
        if best_score == -1 or get_score(next_motifs) < best_score:
            best_motifs = next_motifs[:]
            best_score = get_score(next_motifs)

    return best_motifs


def get_score(current_motifs):
    next_profile = profile_with_pseudocounts(current_motifs)
    consensus_string = list(get_consensus_strings(next_profile))[0]
    current_score = 0
    t = len(current_motifs)
    for i in range(t):
        current_score += hamming_distance(current_motifs[i], consensus_string)
    return current_score


def randomized_motif_search(dna, k, t):
    current_motifs = select_random_k_mers(dna, k, t)
    best_motifs = current_motifs[:]
    best_score = -1
    while True:
        next_profile = profile_with_pseudocounts(current_motifs)
        current_motifs = motifs(next_profile, dna)
        current_score = get_current_score(current_motifs, t)
        if best_score == -1 or current_score < best_score:
            best_motifs = current_motifs[:]
            best_score = current_score
        else:
            return best_motifs


def gibbs_sampler(dna, k, t, n):
    current_motifs = select_random_k_mers(dna, k, t)
    best_motifs = current_motifs[:]
    best_score = -1
    for j in range(n):
        i = random.randrange(t)
        next_profile = profile_with_pseudocounts([x for ii, x in enumerate(current_motifs) if ii != i])
        current_motifs[i] = profile_randomly_generated_k_mer_in_sequence(next_profile, k, dna[i])
        current_score = get_current_score(current_motifs, t)
        if best_score == -1 or current_score < best_score:
            best_motifs = current_motifs[:]
            best_score = current_score

    return best_motifs


def gibbs_sampler_with_restarts(dna, k, t, n):
    best_score = None
    best_motifs = None
    for i in range(20):
        current_motifs = gibbs_sampler(dna, k, t, n)
        current_score = get_current_score(current_motifs, t)
        if best_score is None or current_score < best_score:
            best_motifs = current_motifs[:]
            best_score = current_score

    return best_motifs


def get_current_score(current_motifs, t):
    next_profile = profile_with_pseudocounts(current_motifs)
    consensus_string = list(get_consensus_strings(next_profile))[0]
    current_score = 0
    for i in range(t):
        current_score += hamming_distance(current_motifs[i], consensus_string)
    return current_score


def profile_randomly_generated_k_mer_in_sequence(profile, k, dna_row):
    n = len(dna_row)
    probs = []
    for start in range(n - k + 1):
        prob = 1.0
        i = 0
        for nucleotide in dna_row[start: start + k]:
            prob *= profile[nucleotide.upper()][i]
            i += 1
        probs.append(prob)
    p = random.random() * sum(probs)
    cum_prob = 0.0
    for start in range(n - k + 1):
        cum_prob += probs[start]
        if cum_prob >= p:
            return dna_row[start:start + k]
    return dna_row[n - k + 1:]


def select_random_k_mers(dna, k, t):
    current_motifs = [''] * t
    for i in range(t):
        start = random.randrange(len(dna[0]) - k + 1)
        current_motifs[i] = dna[i][start: start + k]
    return current_motifs


def get_most_likely_motif(profile, dna_row):
    k = len(profile['A'])
    best_prob = -1.0
    best_start = 0
    n = len(dna_row)
    for start in range(n - k + 1):
        prob = 1.0
        i = 0
        for nucleotide in dna_row[start: start + k]:
            prob *= profile[nucleotide.upper()][i]
            i += 1
        if prob > best_prob:
            best_prob = prob
            best_start = start

    return dna_row[best_start: best_start + k]


def motifs(profile, dna):
    return [get_most_likely_motif(profile, dna[i]) for i in range(len(dna))]
