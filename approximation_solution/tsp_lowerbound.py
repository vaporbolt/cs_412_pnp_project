import random


def find_lower_bound(graph):
    key = {}
    parent = {}
    mst = {}
    graph_keys = list(graph.keys())
    removed_vertex = graph_keys.pop(0)

    for x in graph_keys:
        key[x] = float("inf")
        parent[x] = None
        mst[x] = False

    key[graph_keys[0]] = 0

    for _ in range(len(graph)):
        u = ""
        minimum = float("inf")
        for v in graph_keys:
            if float(key[v]) < float(minimum) and mst[v] is False:
                minimum = key[v]
                u = v
        mst[u] = True

        for v in graph_keys:
            if u == v or u == "":
                continue
            if 0 < float(graph[u][v]) < float(key[v]) and mst[v] is False:
                key[v] = graph[u][v]
                parent[v] = u

    bound = 0
    for i in graph_keys:
        bound += float(key[i])

    shortest_edge_one = float("inf")
    for v in graph[removed_vertex]:
        weight = float(graph[removed_vertex][v])
        if weight < shortest_edge_one:
            shortest_edge_one = weight
    bound += shortest_edge_one

    shortest_edge_two = float("inf")
    for v in graph[removed_vertex]:
        weight = float(graph[removed_vertex][v])
        if weight < shortest_edge_two and weight != shortest_edge_one:
            shortest_edge_two = weight
    bound += shortest_edge_two

    return bound


def lower_bound_sum(graph):
    keys = list(graph.keys())
    total = 0
    for key in keys:
        sum = 0
        shortest_edge_one = float("inf")
        for v in graph[key]:
            weight = float(graph[key][v])
            if weight < shortest_edge_one:
                shortest_edge_one = weight
        sum += shortest_edge_one

        shortest_edge_two = float("inf")
        for v in graph[key]:
            weight = float(graph[key][v])
            if weight < shortest_edge_two and weight != shortest_edge_one:
                shortest_edge_two = weight
        sum += shortest_edge_two

        sum /= 2
        total += sum
    return total


def main():
    # get input.
    num_things = input().split(" ")
    num_vertices = int(num_things[0])
    num_edges = int(num_things[1])
    graph = {}
    for i in range(num_edges):
        edge_info = input().split(" ")
        if graph.get(edge_info[0]) is None:
            graph[edge_info[0]] = {}
        if graph.get(edge_info[1]) is None:
            graph[edge_info[1]] = {}
        graph[edge_info[0]][edge_info[1]] = edge_info[2]
        graph[edge_info[1]][edge_info[0]] = edge_info[2]
    res = lower_bound_sum(graph)
    res2 = find_lower_bound(graph)
    print(f"Sum method: {res}\tMST method: {res2}")


if __name__ == "__main__":
    main()