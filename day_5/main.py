from functools import cmp_to_key


def find_ordered_updates(rules: list, updates: list):
    rules.sort(key=lambda x: x[0])
    total, unordered_updates = 0, []
    for update in updates:
        max_val = max(update)
        val_to_index, next_update = {num: i for i, num in enumerate(update)}, False
        for rule in rules:
            if rule[0] > max_val:
                break

            if rule[0] not in val_to_index or rule[1] not in val_to_index:
                continue

            if not val_to_index[rule[0]] < val_to_index[rule[1]]:
                unordered_updates.append(update)
                next_update = True
                break
        if next_update:
            continue

        total += update[len(update) // 2]

    print(total)

    fix_unordered_updates(rules, unordered_updates) # part 2


def fix_unordered_updates(rules: list ,unordered_updates: list):
    rule_set = set(rules)
    def compare(x: int, y: int) -> int:
        if (x, y) in rule_set:
            res = -1
        elif (y, x) in rule_set:
            res = 1
        else:
            res = 0

        return res

    total = 0
    for update in unordered_updates:
        update.sort(key=cmp_to_key(compare))
        total += update[len(update) // 2]

    print(total)


def main():
    with open("input.txt") as f:
        rules, updates = [], []
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            if "|" in line:
                nums = line.split("|")
                rules.append((int(nums[0]), int(nums[1])))
            else:
                update = []
                for num in line.split(","):
                    update.append(int(num.strip()))
                updates.append(update)

    find_ordered_updates(rules, updates) # part 1 and part 2


if __name__ == "__main__":
    main()