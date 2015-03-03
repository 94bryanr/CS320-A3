def DFS(node, array):
	#Initialize return list
	final = []
	#Starter node
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
