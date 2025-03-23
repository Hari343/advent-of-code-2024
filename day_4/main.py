from itertools import product


def find_total_occurrences(lines: list[str]) -> None:
    # first row search
    row_count = sum(line.count("XMAS") + line.count("SAMX") for line in lines)
    # column count
    column_lines = ["".join(line[i] for line in lines) for i in range(len(lines))]
    column_count = sum(line.count("XMAS") + line.count("SAMX") for line in column_lines)
    # lr count
    lr_lines = []
    for i in range(2 * len(lines)):
        line = []
        for j in range(len(lines)):
            m = i - j
            if m < 0:
                continue
            if m < len(lines):
                line.append(lines[j][m])
        lr_lines.append("".join(line))

    lr_count = sum(line.count("XMAS") + line.count("SAMX") for line in lr_lines)

    # rl count
    rl_lines = []
    for i in range(2 * len(lines)):
        line = []
        for j in range(len(lines)):
            m = len(lines) - (i - j) + 1
            if m < 0:
                continue

            if m < len(lines):
                line.append(lines[j][m])
        rl_lines.append("".join(line))

    rl_count = sum(line.count("XMAS") + line.count("SAMX") for line in rl_lines)

    total_count = row_count + column_count + lr_count + rl_count
    print(total_count)


def find_x_mas(lines: list[str]) -> None:
    count = 0
    for i, j in product(range(len(lines)), repeat=2):
        c = lines[i][j]
        if c != "A":
            continue

        if i in {0, len(lines) - 1} or j in {0, len(lines) - 1}:
            continue

        x_lines = ("".join((lines[i - 1][j - 1], c, lines[i + 1][j + 1])),
                   "".join((lines[i - 1][j + 1], c, lines[i + 1][j - 1])))
        valid = True
        for line in x_lines:
            if line not in {"SAM", "MAS"}:
                valid = False
                break

        if valid:
            count += 1
    print(count)


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    find_total_occurrences(lines) # part 1
    find_x_mas(lines) # part 2


if __name__ == "__main__":
    main()