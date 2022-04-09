"""
    A Hamiltonian cycle (Hamiltonian circuit) is a graph cycle
    through a graph that visits each node exactly once.
    Determining whether such paths and cycles exist in graphs
    is the 'Hamiltonian path problem', which is NP-complete.
    Wikipedia: https://en.wikipedia.org/wiki/Hamiltonian_path
"""
from typing import List
from networkx import Graph

def is_hamiltonian_cycle(graph: Graph, path: List[int]) -> bool:
    """

    """
    used_edges = []
    if path[0] != path[-1]:
        print("Error: path does not connect first and last nodes")
        return False
    if len(path)-1 != len(graph):
        print("Error: number of nodes does not match graph size")
        return False # not a Hamiltonian cycle

    for i in range(len(path)-1):
        if (path[i], path[i+1]) in used_edges:
            print("Error: path contains duplicate edges")
            return False
        if graph.has_edge(path[i], path[i+1]) == False:
            print("Error: path does not connect nodes in order")
            return False
        else:
            used_edges.append((path[i], path[i+1]))
            continue
    print("Success: path is a Hamiltonian cycle")
    return True
