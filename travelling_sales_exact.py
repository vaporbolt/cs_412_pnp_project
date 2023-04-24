"""
name: Seth Roper and Max Mancini

 """
import itertools


def find_optimal_tsp_path(graph, src):
    current_best_path = None
    current_best_cost = float('inf')
    graph_copy = graph.copy()
    graph_copy.pop(src)
    for v_perm in itertools.permutations(graph_copy):
        v_perm = list(v_perm)
        cost = 0
        for i in range(len(v_perm)):
            if i == 0:
                continue
            cost += graph[v_perm[i]][v_perm[i - 1]]

        # add cost to go back to src
        cost += graph[src][v_perm[len(v_perm) - 1]]
        if cost < current_best_cost:
            current_best_cost = cost
            current_best_path = v_perm
    current_best_path.append(src)
    current_best_path.insert(0, src)
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
    opt_path, opt_cost = find_optimal_tsp_path(graph, 0)
    print(opt_path)
    print(opt_cost)


if __name__ == "__main__":
    main()
