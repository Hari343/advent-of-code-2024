import re
import operator


mul = operator.mul  # define the mul function given in the input string

def find_sum(string: str) -> None:
    val = sum(eval(s) for s in re.compile(r"mul\(\d{1,3},\d{1,3}\)").findall(string))
    print(val)


def find_sum_conditional(string: str) -> None:
    dont_initial_index = re.compile(r"don't\(\)").search(string).start()
    do_ranges = [range(dont_initial_index)]
    for match in re.compile(r"do\(\).*?don't\(\)", flags=re.DOTALL).finditer(string):
        do_ranges.append(range(match.start(), match.end()))

    total = 0
    for match in re.compile(r"mul\(\d{1,3},\d{1,3}\)").finditer(string):
        if any(match.start() in do_range for do_range in do_ranges):
            total += eval(match.group())

    print(total)


def main():
    with open("input.txt") as f:
        string = "".join(f.readlines())

    find_sum(string) # part 1
    find_sum_conditional(string) # part 2


if __name__ == "__main__":
    main()