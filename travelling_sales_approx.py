"""
name: Seth Roper and Max Mancini

 """
import random
import time


def swap_vertices(vertex_list):
    rand_v1 = random.randint(0, len(vertex_list) - 1)
    rand_v2 = random.randint(0, len(vertex_list) - 1)
    while rand_v2 == rand_v1:
        rand_v2 = random.randint(0, len(vertex_list) - 1)
    temp = vertex_list[rand_v2]
    vertex_list[rand_v2] = vertex_list[rand_v1]
    vertex_list[rand_v1] = temp


"""
    This solution to approximating the TSP is a RANDOM solution. It starts from a random 
    permutation of the vertices in the graph and on each iteration of the loop
    the program swaps two random vertices and recomputes the cost. This could lead to a decrease or increase
    in the total cost. This also means that if one iteration results in a lower cost, the next could result in a
    higher one. It is completely random.

"""


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
            cost += float(graph[i][last_vertex])
            last_vertex = i
        path.append(src)
        cost += float(graph[last_vertex][src])
        if cost < current_best_cost:
            current_best_cost = cost
            current_best_path = path

        # Swap two random vertices
        swap_vertices(vertex_list)

    return current_best_path, current_best_cost


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
    vertices = list(graph.keys())
    start = time.time()
    opt_path, opt_cost = find_optimal_tsp_path(graph, vertices[0], num_edges)
    end = time.time()
    print(opt_path)
    print(opt_cost)
    print(f"TIME: {end - start}s")


if __name__ == "__main__":
    main()
