import random

def parse_graph(edges):
    graph = {}
    animal_map = {"cat": 1, "hippo": 2, "fox": 3, "rabbit": 4, "crocodile": 5, "pig": 6}
    
    for edge in edges:
        nodes = edge.split(',')
        u, v = nodes[0], nodes[1]
        u_num = animal_map[u]
        v_num = animal_map[v]
        
        if u_num not in graph:
            graph[u_num] = []
        if v_num not in graph:
            graph[v_num] = []
        
        graph[u_num].append(v_num)
        graph[v_num].append(u_num)
    
    return graph

def find_eulerian_cycles(graph, num_cycles=50):
    def is_eulerian(graph):
        for node in graph:
            if len(graph[node]) % 2 != 0:
                return False
        return True

    def eulerian_cycle_random(graph):
        start = random.choice(list(graph.keys()))
        stack = [start]
        path = []

        while stack:
            u = stack[-1]
            if graph[u]:
                v = random.choice(graph[u])
                graph[u].remove(v)
                graph[v].remove(u)
                stack.append(v)
            else:
                path.append(stack.pop())
        return path[::-1]

    if not is_eulerian(graph):
        return []

    all_cycles = set()
    original_graph = {node: list(neighbors) for node, neighbors in graph.items()}
    animal_map = {1: "cat", 2: "hippo", 3: "fox", 4: "rabbit", 5: "crocodile", 6: "pig"}
    
    while len(all_cycles) < num_cycles:
        graph_copy = {node: list(neighbors) for node, neighbors in original_graph.items()}
        cycle = eulerian_cycle_random(graph_copy)
        cycle_str = ",".join(map(lambda x: animal_map[x], cycle))
        all_cycles.add(cycle_str)

    return list(all_cycles)

def format_cycles(cycles):
    return "\n".join(cycles)

edges = [
    "cat,hippo,(cat->hippo)", "hippo,cat,(hippo->cat)", "cat,fox,(cat->fox)", "fox,cat,(fox->cat)",
    "cat,rabbit,(cat->rabbit)", "rabbit,cat,(rabbit->cat)", "cat,crocodile,(cat->crocodile)", "crocodile,cat,(crocodile->cat)",
    "cat,pig,(cat->pig)", "pig,cat,(pig->cat)", "hippo,fox,(hippo->fox)", "fox,hippo,(fox->hippo)",
    "hippo,rabbit,(hippo->rabbit)", "rabbit,hippo,(rabbit->hippo)", "hippo,crocodile,(hippo->crocodile)", "crocodile,hippo,(crocodile->hippo)",
    "hippo,pig,(hippo->pig)", "pig,hippo,(pig->hippo)", "fox,rabbit,(fox->rabbit)", "rabbit,fox,(rabbit->fox)",
    "fox,crocodile,(fox->crocodile)", "crocodile,fox,(crocodile->fox)", "fox,pig,(fox->pig)", "pig,fox,(pig->fox)",
    "rabbit,crocodile,(rabbit->crocodile)", "crocodile,rabbit,(crocodile->rabbit)", "rabbit,pig,(rabbit->pig)", "pig,rabbit,(pig->rabbit)",
    "crocodile,pig,(crocodile->pig)", "pig,crocodile,(pig->crocodile)"
]

graph = parse_graph(edges)
cycles = find_eulerian_cycles(graph, num_cycles=50)
formatted_cycles = format_cycles(cycles)

print(formatted_cycles)
