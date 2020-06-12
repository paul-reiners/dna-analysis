


def main():
    file1 = open('../data/chapter02/Salmonella_enterica.txt', 'r')
    lines = file1.readlines()
    genome = ''.join(map(lambda s: s.strip(), lines[1:]))
    from chapter02.skew import get_minimum_skew_positions
    calculated_output = get_minimum_skew_positions(genome)
    print(' '.join(map(lambda n: str(n), calculated_output)))


if __name__ == "__main__":
    main()
