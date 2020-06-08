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
