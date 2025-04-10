
def find_antinodes(graph: list[str]) -> None:
    antennas = {}

    for x in range(len(graph)):
        for y in range(len(graph[0])):
            c = graph[x][y]
            if c.isalnum():
                if c in antennas:
                    antennas[c].append((x, y))
                else:
                    antennas[c] = [(x, y)]

    anti_nodes = set()
    for locations in antennas.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                loc_i, loc_j = locations[i], locations[j]
                dx, dy = loc_j[0] - loc_i[0], loc_j[1] - loc_i[1]
                an_j = (loc_j[0] - 2 * dx, loc_j[1] - 2 * dy)
                an_i = (loc_i[0] + 2 * dx, loc_i[1] + 2 * dy)

                for node in an_i, an_j:
                    if -1 < node[0] < len(graph) and -1 < node[1] < len(graph[0]):
                        anti_nodes.add(node)
    print(len(anti_nodes))


def find_antinodes2(graph: list[str]) -> None:
    antennas = {}

    for x in range(len(graph)):
        for y in range(len(graph[0])):
            c = graph[x][y]
            if c.isalnum():
                if c in antennas:
                    antennas[c].append((x, y))
                else:
                    antennas[c] = [(x, y)]

    anti_nodes = set()
    for locations in antennas.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                loc_i, loc_j = locations[i], locations[j]
                dx, dy = loc_j[0] - loc_i[0], loc_j[1] - loc_i[1]

                anti_nodes.add(loc_j)

                for direction in (-1, 1):
                    mul = 1
                    while 1:
                        anti_node = loc_j[0] - mul * dx * direction, loc_j[1] - mul * dy * direction

                        if (-1 >= anti_node[0] or anti_node[0] >= len(graph) or -1 >= anti_node[1] or
                                anti_node[1] >= len(graph[0])):
                            break

                        anti_nodes.add(anti_node)
                        mul += 1
    print(len(anti_nodes))

    mark_anti_node_on_graph(graph, anti_nodes)


def mark_anti_node_on_graph(graph: list[str], anti_nodes: set) -> None:
    graph = [list(string) for string in graph]

    for x, y in anti_nodes:
        graph[x][y] = "*"

    graph = ["".join(line) for line in graph]

    with open("output.txt", "w") as f:
        for line in graph:
            f.write(line + "\n")


def main():
    with open("input.txt") as f:
        graph = [line.strip() for line in f.readlines()]

    find_antinodes(graph)
    find_antinodes2(graph)


if __name__ == "__main__":
    main()
