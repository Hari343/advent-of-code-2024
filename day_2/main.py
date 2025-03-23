from itertools import pairwise
from collections import deque


def main():
    with open("input.txt") as f:
        records = [tuple(int(c) for c in line.strip().split(" ")) for line in f.readlines()]

    find_safe_records(records)  # part 1
    find_safe_records_with_dampener(records)  # part 2


def find_safe_records(records: list):
    safe_records = len(records)

    for record in records:
        sign = record[1] - record[0]
        for x, y in pairwise(record):
            delta = y - x
            if delta < 0 < sign or sign < 0 < delta or not 0 < abs(delta) < 4:
                safe_records -= 1
                break

    print(safe_records)


def find_safe_records_with_dampener(records: list):
    total = 0
    for record in records:
        omissions, dec = 0, None
        stack = deque()

        for num in record:
            if not stack:
                stack.append(num)
                continue

            if stack[-1] == num or not (0 < abs(stack[-1] - num) < 4):
                omissions += 1
                continue

            if dec is None:
                dec = stack[-1] > num
                stack.append(num)
                continue

            if (dec and stack[-1] < num) or (not dec and stack[-1] > num):
                omissions += 1
                continue

            stack.append(num)

        if omissions < 2:
            total += 1
            continue

        stack.clear()
        omissions_rev, dec = 0, None

        for num in record[::-1]:
            if not stack:
                stack.append(num)
                continue

            if stack[-1] == num  or not (0 < abs(stack[-1] - num) < 4):
                omissions_rev += 1
                continue

            if dec is None:
                dec = stack[-1] > num
                stack.append(num)
                continue

            if (dec and stack[-1] < num) or (not dec and stack[-1] > num):
                omissions_rev += 1
                continue

            stack.append(num)

        if omissions_rev < 2:
            total += 1

    print(total)


if __name__ == "__main__":
    main()

