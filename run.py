# Search methods

import search

ab = search.GPSProblem('A', 'G'
                       , search.romania)

print("Breadth first graph search result\n", "Visited Nodes:",
      search.breadth_first_graph_search(ab)[1], "\n", search.breadth_first_graph_search(ab)[0].path(), "\n")
print("Depth first graph search result\n", "Visited Nodes:",
      search.depth_first_graph_search(ab)[1], "\n", search.depth_first_graph_search(ab)[0].path(), "\n")
print("Branch and bound result\n", "Visited Nodes:",
      search.branch_and_bounding(ab)[1], "\n", search.branch_and_bounding(ab)[0].path(), "\n")
print("Heuristic branch and bound result\n", "Visited Nodes:",
      search.heuristic_branch_and_bound(ab)[1], "\n", search.heuristic_branch_and_bound(ab)[0].path(), "\n")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
