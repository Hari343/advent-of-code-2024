from itertools import product


def map_guard_path(graph: list[str]):
    # find curr location
    curr_loc = None
    for x, y in product(range(len(graph)), range(len(graph[0]))):
        if graph[x][y] == "^":
            curr_loc = x, y
            break

    dir_to_next_map = {
        0: lambda x, y: (x - 1, y),
        90: lambda x, y: (x, y + 1),
        180: lambda x, y: (x + 1, y),
        270: lambda x, y: (x, y - 1)
    }

    seen, curr_dir = set(), 0
    while -1 < curr_loc[0] < len(graph) and -1 < curr_loc[1] < len(graph[0]):
        seen.add(curr_loc)

        next_loc = dir_to_next_map[curr_dir](*curr_loc)
        while ((-1 < next_loc[0] < len(graph)) and (-1 < next_loc[1] < len(graph[0])) and
               graph[next_loc[0]][next_loc[1]] == "#"):
            curr_dir += 90
            curr_dir = 0 if curr_dir == 360 else curr_dir
            next_loc = dir_to_next_map[curr_dir](*curr_loc)

        curr_loc = next_loc

    print(len(seen))


def main():
    with open("input.txt") as f:
        graph = [line.strip() for line in f.readlines()]

    map_guard_path(graph) # part 1


if __name__ == "__main__":
    main()