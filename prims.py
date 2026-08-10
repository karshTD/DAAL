def prim(G, start):
    key = {}
    parent = {}
    inmst = {}
    
    for v in G:
        key[v] = float('inf')
        parent[v] = None
        inmst[v] = False
    
    key[start] = 0
    
    for _ in range(len(G)):
        u = None
        min_key = float('inf')
        for v in G:
            if not inmst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        
        inmst[u] = True
        
        for v in G[u]:
            if not inmst[v] and G[u][v] < key[v]:
                key[v] = G[u][v]
                parent[v] = u
    
    return parent


G = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

parent = prim(G, 'A')

print("MST edges:")
for v in parent:
    if parent[v] != None:
        print(v, "-", parent[v], "weight:", G[v][parent[v]])
