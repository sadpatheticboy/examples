def histogram(text):
    histogram = {}
    for char in text:
        if char not in [' ', '\n']:
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1

    sorted_histogram = sorted(histogram.items(), key=lambda x: ord(x[0]))
    max_count = max([count for _, count in sorted_histogram])

    for i in range(max_count, 0, -1):
        line = ''
        for char, count in sorted_histogram:
            line += '#' * (count >= i) + ' ' * (count < i)
        print(line)

    bottom_line = ''
    for char, _ in sorted_histogram:
        bottom_line += char + ' '
    print(bottom_line)


s = input()
histogram(s)
