def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i:i + 1] != str2[i:i + 1]:
            distance += 1

    return distance


def d(pattern, string):
    shortest = -1
    pattern_length = len(pattern)
    for start_index in range(len(string) - pattern_length):
        distance = hamming_distance(pattern, string[start_index:start_index + pattern_length])
        if shortest == -1 or distance < shortest:
            shortest = distance

    return shortest
