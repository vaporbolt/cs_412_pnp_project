"""
name: Seth Roper and Max Mancini

 """
import random
import time


# Swaps two vertices in the given list and returns the swapped indices
# We don't want to move the source node, so we generate indexes from the second to the second to last item
def swap_vertices(vertex_list, rand_v1, rand_v2):
    temp = vertex_list[rand_v2]
    vertex_list[rand_v2] = vertex_list[rand_v1]
    vertex_list[rand_v1] = temp

    return rand_v1, rand_v2


"""
    This solution to approximating the TSP is a RANDOM solution. On each iteration of the loop
    the program swaps two random vertices and checks if the new cost is lower than the old cost. 
    If the new cost is better than the previous, it accepts the new path, 
    otherwise it attempts to make a positive swap on the current best path again.

"""


def find_optimal_tsp_path(graph, src, max_iter):
    # Create a list of all vertices in the graph, in order initially
    vertex_list = list(graph.keys())
    vertex_list.append(src)

    # Set up initial path and cost variables to reflect the cost of the initial list
    cost = 0
    path = list()
    path.append(src)
    last_vertex = src
    for i in vertex_list:
        if i == src:
            continue
        path.append(i)
        cost += float(graph[i][last_vertex])
        last_vertex = i
    path.append(src)
    cost += float(graph[last_vertex][src])

    current_best_cost = cost
    current_best_path = path

    # Begin approximation
    for _ in range(max_iter):
        # Make a copy of the vertex list and swap two vertices in the copy

        i1 = random.randint(1, len(vertex_list) - 2)
        i2 = random.randint(1, len(vertex_list) - 2)
        while i2 == i1:
            i2 = random.randint(1, len(vertex_list) - 2)

        vertex_list_total = \
            float(graph[vertex_list[i1 - 1]][vertex_list[i1]]) + \
            float(graph[vertex_list[i1]][vertex_list[i1 + 1]]) + \
            float(graph[vertex_list[i2 - 1]][vertex_list[i2]]) + \
            float(graph[vertex_list[i2]][vertex_list[i2 + 1]])

        swap_vertices(vertex_list, i1, i2)

        # Gather total weight of edges connected to swapped vertices in both lists
        new_list_total = \
            float(graph[vertex_list[i1 - 1]][vertex_list[i1]]) + \
            float(graph[vertex_list[i1]][vertex_list[i1 + 1]]) + \
            float(graph[vertex_list[i2 - 1]][vertex_list[i2]]) + \
            float(graph[vertex_list[i2]][vertex_list[i2 + 1]])

        # If the weight of the edges after the swap is smaller, we have made a positive swap
        # Update the best cost and path
        if new_list_total < vertex_list_total:
            current_best_cost -= vertex_list_total
            current_best_cost += new_list_total
            current_best_path = vertex_list
        else:
            swap_vertices(vertex_list, i1, i2)

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
    # Starting point will always be first vertex, iteration count set to 100000
    # by default to balance speed and accuracy
    opt_path, opt_cost = find_optimal_tsp_path(graph, vertices[0], 100000)
    end = time.time()
    print(opt_cost)
    print(*opt_path)
    print(f"TIME: {end - start}s")


if __name__ == "__main__":
    main()
