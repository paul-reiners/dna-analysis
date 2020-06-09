import math

symbol_to_number_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
number_to_symbol_map = {v: k for k, v in symbol_to_number_map.items()}


def last_symbol(pattern):
    return pattern[-1]


def prefix(pattern):
    return pattern[:-1]


def symbol_to_number(symbol):
    return symbol_to_number_map[symbol]


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = last_symbol(pattern)
    prfx = prefix(pattern)

    return 4 * pattern_to_number(prfx) + symbol_to_number(symbol)


def number_to_symbol(number):
    return number_to_symbol_map[number]


def quotient(dividend, divisor):
    return dividend // divisor


def remainder(dividend, divisor):
    return dividend % divisor


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    prefix_index = quotient(index, 4)
    r = remainder(index, 4)
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)

    return prefix_pattern + symbol


def computing_frequencies(text, k):
    frequency_array = [0] * int(math.pow(4, k))
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1

    return frequency_array


def faster_frequent_words(text, k):
    frequent_patterns = set()
    frequency_array = computing_frequencies(text, k)
    max_count = max(frequency_array)
    for i in range(int(math.pow(4, k))):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)

    return frequent_patterns


def finding_frequent_words_by_sorting(text, k):
    frequent_patterns = set()
    n = len(text) - k + 1
    index = [0] * n
    count = [0] * n
    for i in range(n):
        pattern = text(i, k)
        index[i] = pattern_to_number(pattern)
        count[i] = 1
    sorted_index = sorted(index)
    for i in range(1, n):
        if sorted_index[i] == sorted_index[i - 1]:
            count[i] = count[i - 1] + 1
    max_count = max(count)
    for i in range(n):
        if count[i] == max_count:
            pattern = number_to_pattern(sorted_index[i], k)
            frequent_patterns.add(pattern)

    return frequent_patterns


def clump_finding(genome, k, L, t):
    frequent_patterns = set()
    n = int(math.pow(4, k))
    clump = [0] * n
    for i in range(len(genome) - L + 1):
        text = genome[i : i + L]
        frequency_array = computing_frequencies(text, k)
        for index in range(n):
            if frequency_array[index] >= t:
                clump[index] = 1
    for i in range(n):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)

    return frequent_patterns


def better_clump_finding(genome, k, t, L):
    frequent_patterns = set()
    n = int(math.pow(4, k))
    clump = [0] * n
    text = genome[0:L]
    frequency_array = computing_frequencies(text, k)
    for i in range(n):
        if frequency_array[i] >= t:
            clump[i] = 1
    for i in range(1, len(genome) - L + 1):
        first_pattern = genome[i - 1 : i - 1 + k]
        index = pattern_to_number(first_pattern)
        frequency_array[index] = frequency_array[index] - 1
        last_pattern = genome[i + L - k : i + L]
        index = pattern_to_number(last_pattern)
        frequency_array[index] = frequency_array[index] + 1
        if frequency_array[index] >= t:
            clump[index] = 1
    for i in range(n):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)

    return frequent_patterns
