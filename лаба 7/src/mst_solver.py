import csv

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

def calculate_min_cable_length(file_path):
    edges = []
    vertices = set()
    
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row: continue
                v1, v2, dist = row[0].strip(), row[1].strip(), int(row[2])
                edges.append((dist, v1, v2))
                vertices.add(v1)
                vertices.add(v2)
    except FileNotFoundError:
        return -1

    if not vertices:
        return 0

    edges.sort()
    ds = DisjointSet(vertices)
    mst_weight = 0
    edges_count = 0

    for weight, v1, v2 in edges:
        if ds.union(v1, v2):
            mst_weight += weight
            edges_count += 1

    if edges_count != len(vertices) - 1:
        return -1

    return mst_weight