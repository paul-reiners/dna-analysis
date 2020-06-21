def composition(text, k):
    return sorted([text[start : start + k] for start in range(len(text) - k + 1)])
