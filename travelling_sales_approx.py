"""
name: Seth Roper and Max Mancini


4 6
0 1 20
0 2 42
0 3 35
1 3 34
2 3 12
1 2 30

 """
import itertools
import random


def find_optimal_tsp_path(graph, src, max_iter):
    current_best_path = None
    current_best_cost = float('inf')
    graph_copy = graph.copy()
    graph_copy.pop(src)
    vertex_list = list(graph_copy.keys())
    random.shuffle(vertex_list)

    for _ in range(max_iter):
        cost = 0
        path = list()
        path.append(src)
        last_vertex = src
        for i in vertex_list:
            path.append(i)
            cost += graph[i][last_vertex]
            last_vertex = i
        path.append(src)
        cost += graph[last_vertex][src]
        if cost < current_best_cost:
            current_best_cost = cost
            current_best_path = path

        # Swap two random vertices
        rand_v1 = random.randint(0, len(vertex_list)-1)
        rand_v2 = random.randint(0, len(vertex_list)-1)
        while rand_v2 == rand_v1:
            rand_v2 = random.randint(0, len(vertex_list)-1)
        temp = vertex_list[rand_v2]
        vertex_list[rand_v2] = vertex_list[rand_v1]
        vertex_list[rand_v1] = temp

    return current_best_path, current_best_cost


def main():
    # get input.
    num_things = input().split(" ")
    num_vertices = int(num_things[0])
    num_edges = int(num_things[1])
    graph = {}
    for i in range(num_vertices):
        graph[i] = {}
    for i in range(num_edges):
        edge_info = list(map(lambda x: int(x), input().split(" ")))
        graph[edge_info[0]][edge_info[1]] = edge_info[2]
        graph[edge_info[1]][edge_info[0]] = edge_info[2]
    opt_path, opt_cost = find_optimal_tsp_path(graph, 0, 50)
    print(opt_path)
    print(opt_cost)


if __name__ == "__main__":
    main()
