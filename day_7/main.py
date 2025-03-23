def process_eqns(eqns: list) -> None:

    def solve(target: int, index: int, curr_val: int = 0):
        nonlocal sequence
        if index == len(sequence):
            if target == curr_val:
                return True
            else:
                return False

        if curr_val > target:
            return False

        return (solve(target, index + 1, curr_val + sequence[index]) or
                solve(target, index + 1, curr_val * sequence[index] if index else sequence[index]))

    total = 0
    for eqn in eqns:
        sequence = eqn[1]
        if solve(eqn[0], 0):
            total += eqn[0]

    print(total)


def process_eqns_with_concatenation(eqns: list) -> None:

    def solve(target: int, index: int, curr_val: int = 0):
        nonlocal sequence
        if index == len(sequence):
            if target == curr_val:
                return True
            else:
                return False

        if curr_val > target:
            return False

        return (solve(target, index + 1, curr_val + sequence[index]) or
                solve(target, index + 1, curr_val * sequence[index] if index else sequence[index]) or
                solve(target, index + 1, int(str(curr_val) + str(sequence[index]))))

    total = 0
    for eqn in eqns:
        sequence = eqn[1]
        if solve(eqn[0], 0):
            total += eqn[0]

    print(total)


def main():
    with open("input.txt") as f:
        eqns = []
        for line in f.readlines():
            line = line.strip()
            line_components = line.split(":")
            eqns.append((int(line_components[0]), [int(x.strip())
                                                   for x in line_components[1].split(" ") if x.strip() != "" ]))

    process_eqns(eqns) # part 1
    process_eqns_with_concatenation(eqns) # part 2


if __name__ == "__main__":
    main()


