graph = {}  # Empty dict banaya, yeh banega adjacency list

n = int(input("Enter number of edges: "))  # user se number of edges liya

print("Enter edges in format: from to weight")
for _ in range(n):
    u, v, w = input().split()   # edge line ko 3 parts mein tod diya: from, to, weight
    w = int(w)                  # weight string tha, int mein convert kiya

    # Agar u ya v graph mein nahi hain, to unke liye empty list banao
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    # Directed graph: u se v ek edge hai with weight w
    graph[u].append((v, w))

    # Undirected banana ho to ye bhi likh sakta hai:
    # graph[v].append((u, w))


# Agar tu input deta hai:

# A B 2
# A C 3
# B D 1
# C D 5


# To graph banega:

# {
#   'A': [('B', 2), ('C', 3)],
#   'B': [('D', 1)],
#   'C': [('D', 5)],
#   'D': []
# }