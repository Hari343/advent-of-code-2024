
def find_hiking_paths(graph: list[list]) -> None:
    zeros = []
    for x, row in enumerate(graph):
        for y, val in enumerate(row):
            if val == 0:
                zeros.append((x, y))

    def find_path(start_pos: tuple) -> tuple:
        nonlocal graph, nines, rating
        x, y = start_pos
        val = graph[x][y]
        next_val = val + 1

        path_found = False
        for _x, _y in ((x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)):
            if _x < 0 or _x >= len(graph) or _y < 0 or _y >= len(graph[0]):
                continue
            if graph[_x][_y] == next_val:
                path_found = True
                if next_val != 9:
                    find_path((_x, _y))
                else:
                    nines.add((_x, _y))
                    rating += 1

        if not path_found:
            return -1, -1

    total, total_rating = 0, 0
    for zero in zeros:
        nines, rating = set(), 0
        find_path(zero)
        total += len(nines)
        total_rating += rating

    print(total, total_rating)


def main():
    with open("input.txt") as f:
        graph = [[int(c) for c in line.strip()] for line in f.readlines()]

    find_hiking_paths(graph)


if __name__ == "__main__":
    main()
