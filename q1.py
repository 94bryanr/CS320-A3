import numpy

def transitiveClosure(array):
	#Initialize returned array
	closure = array
	#iterate through each node n
	for n in range(array.shape[1]):
		#dfs from n to find all reachable nodes from n
		reachable = DFS(n, array)
		#add all reachable nodes to n's edges
		for i in reachable:
			closure[n][i] = 1
	return closure

def DFS(node, array):
	#Initialize return list
	final = []
	#Remeber initial node
	S = [node]
	#Initialize E to be a list representing the explored state of each node
	E = [0] * array.shape[1]
	#While S not empty
	while len(S) != 0:
		#Take a node u from S
		u = S.pop()
		#If explored[u] = false then
		if E[u] == 0:
			#Set explored[u] true
			E[u] = 1
			#For each edge (u,v) incitent to u
			for v in range(array.shape[1]):
				if array[u][v] == 1:
					#Add v to the stack S
					final.append(v)
					S.append(v)
	#remove duplicates:
	final = list(set(final))
	#remove reference to self:
	if node in final: final.remove(node)
	return final

a = numpy.zeros([6,6])
#[from][to]
#[y][x]
a[0][1] = 1
a[0][3] = 1
a[0][4] = 1
a[1][2] = 1
a[3][5] = 1
a[4][0] = 1
a[5][4] = 1

print a
tc = transitiveClosure(a)
print "\n"
print tc
