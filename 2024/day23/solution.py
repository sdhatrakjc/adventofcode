from collections import defaultdict

connections = open('./day23/input.txt').read().strip().split('\n')

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

networks  = []
for node in graph:
    neighbors = graph[node]
    for n1 in neighbors:
        for n2 in neighbors:
            if n1 != n2 and n2 in graph[n1]:
                network = tuple(sorted([node, n1, n2]))
                if network not in networks:
                    networks.append(network)

filtered_networks = [network for network in networks if any(computer.startswith('t') for computer in network)]
print(len(filtered_networks))


def bron_kerbosch(r, p, x, graph, cliques):
    if not p and not x:
        cliques.append(r)
        return

    for node in list(p):
        bron_kerbosch(r | {node}, p & graph[node], x & graph[node], graph, cliques)
        p.remove(node)
        x.add(node)

cliques = []
bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
largest_clique = max(cliques, key=len)
# print(largest_clique)

password = ",".join(sorted(largest_clique))
print(password)
