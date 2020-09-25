
from util import Graph
from collections import deque
from collections import defaultdict

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
        
# lecture code
def class_earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    stack.append((starting_node, 0)) # node and distance from starting_node
    visited = set()
    # using tuple and compare and traverse to see if earlier than the earliest ancestor we have found
    earliestAncestor = (starting_node, 0) 

    while len(stack) > 0:
        curr = stack.pop() # (current node, distance from starting node)
        currNode, distance = curr[0], curr[1]
        visited.add(curr)
            
            # if key not in graph they are a terminal node
        if currNode not in graph:
            # check to see if node is earlier than current ancestor
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            # if node is earlier and lower than dual parent id
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        
        # if ancestor has more ancestors, keep traversing
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance +1))
    
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

def createGraph(edges):
    # every key added to this dictionary will have a default value of set()
    graph = defaultdict(set) 
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph

    

