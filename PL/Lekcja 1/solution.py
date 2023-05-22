# Wczytywanie grafu
n, m = map(int, input().split())
n = n + 1
G = []

for i in range(n):
    G.append([])

for i in range(m):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

# Sortujemy sąsiadów
for i in range(n):
    G[i].sort()

# Wypisujemy sąsiadów każdego wierzchołka
for i in range(1, n):
    if len(G[i]) == 0:
        print("Wiwior sam!")
    else:
        for v in G[i]:
            print(v, end=' ')
        print()

