from collections import defaultdict


def count_paths(start, target):
    # paths[n] = количество программ, приводящих к n, не проходя через target раньше
    current = defaultdict(int)
    current[start] = 1
    total = 0

    for _ in range(200):
        next_level = defaultdict(int)
        for num, ways in current.items():
            for cmd in ['A', 'B']:
                if cmd == 'A':
                    res = num - 2
                    if res < 0:
                        continue
                else:
                    tens, ones = num // 10, num % 10
                    if ones < tens:
                        res = ones * 10 + tens
                    else:
                        continue

                if res == target:
                    total += ways
                else:
                    next_level[res] += ways

        current = next_level
        if not current:
            break

    return total


print(count_paths(57, 13))