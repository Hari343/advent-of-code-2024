def rearrange_files(file_str: str) -> None:
    disk = []
    file_id = 0

    for i, c in enumerate(file_str):
        val = int(c)
        if i % 2 != 0:
            for j in range(val):
                disk.append(-1)
        else:
            for j in range(val):
                disk.append(file_id)
            file_id += 1

    write, read = 0, len(disk) - 1
    while write < len(disk) and read >= write:
        if disk[write] != -1:
            write += 1
            continue

        while disk[read] == -1:
            read -= 1

        if read < write:
            break

        disk[write], disk[read] = disk[read], -1
        read -= 1
        write += 1

    print(sum(i * x for i, x in enumerate(disk) if x != -1))


def rearrange_without_fragmentation(file_str: str) -> None:
    disk = []
    free_space_locations, file_id_locations = {}, {}
    file_id_to_size = {}
    file_id = 0
    for i, c in enumerate(file_str):
        val = int(c)
        if i % 2 != 0:
            if val > 0:
                free_space_locations[len(disk)] = val
            for j in range(val):
                disk.append(-1)
        else:
            file_id_to_size[file_id] = val
            file_id_locations[file_id] = len(disk)
            for j in range(val):
                disk.append(file_id)
            file_id += 1

    for file_id in list(file_id_to_size.keys())[::-1]:
        size = file_id_to_size[file_id]
        for free_space_loc in sorted(free_space_locations):
            if free_space_locations[free_space_loc] >= size and free_space_loc < file_id_locations[file_id]:
                for j in range(free_space_loc, free_space_loc + size):
                    disk[j] = file_id

                if disk[j + 1] == -1:
                    free_space_locations[j + 1] = free_space_locations[free_space_loc] - size

                del free_space_locations[free_space_loc]

                file_id_loc = file_id_locations[file_id]
                for j in range(file_id_loc, file_id_loc + size):
                    disk[j] = -1

                break

    checksum = 0
    for i, x in enumerate(disk):
        if x != -1:
            checksum += i * x

    print(checksum)


def main():
    with open("input.txt") as f:
        file_str = f.readline()

    rearrange_files(file_str)
    rearrange_without_fragmentation(file_str)


if __name__ == "__main__":
    main()
