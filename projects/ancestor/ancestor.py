
from util import Graph


def earliest_ancestor(ancestors, starting_node):
    # base case is return -1 because no parents/ancestor
    """
    Input (family tree, individual id)
    Ouput ( ID of the earliest ancestor)
    """
    # initialize graph and add vertexes
    tree = Graph()
    for (node1, node2) in ancestors:
        tree.add_vertex(node1)
        tree.add_vertex(node2)
    
    for (node1, node2) in ancestors:
        tree.add_edge(node1, node2)
    
    early_anc = -1
    longest_path = 1
    
    for node in tree.vertices:
        path = tree.dfs(node, starting_node)

        if path:
            if len(path) > longest_path:
                longest_path = len(path)
                early_anc = node
            elif not path and longest_path == 1:
                early_anc = -1
    
    return early_anc
        


    

