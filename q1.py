import numpy
# Graphs represented by numpy multidimensional arrays, ie:
a = numpy.zeros([6,6])
# Set the edges
# [from][to]
a[0][1] = 1
a[0][3] = 1
a[0][4] = 1
a[1][2] = 1
a[3][5] = 1
a[4][0] = 1
a[5][4] = 1

def transitiveClosure(array):
	finalClosureArray = array
	# Iterate through each node in the graph
	for node in range(array.shape[1]):
		reachable = DFS(node, array)
		# Add all reachable nodes to n's edges
		for reachedNode in reachable:
			finalClosureArray[node][reachedNode] = 1
	return finalClosureArray

def DFS(node, array):
	final = []
	# Stack of nodes to visit
	visitStack = [node]
	# List representing explored state of each node
	explored = [0] * array.shape[1]
	while len(visitStack) != 0:
		boundaryNode = visitStack.pop()
		# If boundaryNode hasnt been explored
		if explored[boundaryNode] == 0:
			explored[boundaryNode] = 1
			# For each neighbor of boundaryNode 
			for possibleNeighbor in range(array.shape[1]):
				if array[boundaryNode][possibleNeighbor] == 1:
					#Add neighbor to the visitStack
					final.append(possibleNeighbor)
					visitStack.append(possibleNeighbor)
	# Remove duplicates
	final = list(set(final))
	# Remove reference to self
	if node in final: final.remove(node)
	return final

# Example
print transitiveClosure(a)
