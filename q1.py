import numpy

def findReachable(array, node, startingNode):
	reachable = []
	#Find all reachable nodes from (node) in (array)
	for x in range(array.shape[1]):
		#if node is reachable
		if array[node][x] == 1:
			#TODO: if we have not already added this node(cycle avoidance)
			#add that node to the reachable list
			reachable.append(x)
			#add all nodes that that node can reach
			reachable += findReachable(array, x, startingNode)
	return reachable

def closure(array):
	clos = numpy.zeros(array.shape)
	#iterate through each column
	for y in range(array.shape[0]):
		#get a list of reachable nodes
		reach = findReachable(array, y, y)
		print "Reach set for node {}: {}".format(y,reach)
		#set the adj matrix
		for element in reach:
			clos[y][element] = 1
	return clos


#Initialize the matrix to all 0's
a = numpy.zeros([4,4])

#a[column][row]
a[0][1] = 1
a[1][3] = 1
a[2][1] = 1

#introduce a cycle
a[3][0] = 1


print a
aPrime = closure(a)
print aPrime
