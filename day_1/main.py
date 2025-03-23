from collections import Counter


def main():
    left, right = [], []
    with open("input.txt") as f:
        for line in f.readlines():
            numbers = line.strip().split("   ")
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))

    # part 1
    diff_sum = sum(abs(y - x) for x, y in zip(sorted(left), sorted(right)))
    print(diff_sum)

    # part 2
    counter = Counter(right)
    score = 0
    for num in left:
        score += num * counter[num]
    print(score)


if __name__ == "__main__":
    main()
