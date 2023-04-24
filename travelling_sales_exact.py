"""
name: Seth Roper and Max Mancini

 """
import itertools


def find_optimal_tsp_path(graph):
    current_best_path = None
    current_best_cost = float('inf')
    for v_perm in itertools.product(graph, repeat= len(graph)):
        cost = 0
        for i in range(len(v_perm)):
            # first vertex's cost is weight of edge between v[n -1]
            if i == 0:
                cost += graph[v_perm[i]][v_perm[len(v_perm) - 1]]
            else:
                cost += graph[v_perm[i]][v_perm][i - 1]
        if cost < current_best_cost:
            current_best_cost = cost
            current_best_path = v_perm

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

    opt_path, opt_cost = find_optimal_tsp_path(graph)
    print(opt_path)


if __name__ == "__main__":
    main()
