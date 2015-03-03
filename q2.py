import numpy
# Graphs represented by numpy multidimensional arrays, ie:
a = numpy.zeros([9,9])
# Set the edges
# [from][to]
a[0][1] = 1
a[0][2] = 1
a[1][0] = 1
a[1][2] = 1
a[2][0] = 1
a[2][1] = 1

def findCycle(array):
	exploredNodes = []
	# Starter node
	visitStack = [0]
	# Initialize exploredState to be a list representing the explored state of each node
	exploredState = [0] * array.shape[1]
	while len(visitStack) != 0:
		# Take a node boundaryNode from visitStack
		boundaryNode = visitStack.pop()
		# If explored[boundaryNode] = false then
		if exploredState[boundaryNode] == 0:
			# Set explored[boundaryNode] true
			exploredState[boundaryNode] = 1
			exploredNodes.append(boundaryNode)
			# For each edge (u,v) incitent to boundaryNode
			for v in range(array.shape[1]):
				if array[boundaryNode][v] == 1:
					# Add v to the stack visitStack
					visitStack.append(v)
		elif exploredState[boundaryNode] == 1 and boundaryNode != exploredNodes[len(exploredNodes)-2]:
			# We have found a cycle
			exploredNodes.append(boundaryNode)
			# Remove non-cyclic portion
			while exploredNodes[0] != boundaryNode: exploredNodes.remove(0)
			return exploredNodes
	# No cycle found
	return []

# Example
print findCycle(a)
