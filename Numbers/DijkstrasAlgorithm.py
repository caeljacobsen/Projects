# Create a program that finds the shortest path through a graph using its edges.

#Graph Object
#Doesn't do traversals

class Graph(object):
	"""
		This is an object that defines a weighted graph's representation for use by traversal algorithms.
		This class can add and remove nodes and edges to prepare for traversal by any traversal algorithm.
		Note: This does not implement the traversals
	"""
	def __init__(self):
		self.nodes = set()
		self.edges = {}
		self.distances = {}
		
	#Create a new node/vertex
	def addNode(self, value):
		self.nodes.add(value)
		
	#removes a node and all references to that node
	def removeNode(self, value):
		for edge in self.edges[value]:
			removeEdge(value, edge)
			
	#Bidirectional edges
	def addEdge(self, originNode, destNode, distance):
		self._addEdge(originNode, destNode, distance)	
		self._addEdge(destNode, originNode, distance)
	
	#Actual edge creation method	
	def _addEdge(self, originNode, destNode, distance):
		self.edges.setdefault(originNode, [])	#set up default direction
		self.edges[originNode].append(destNode) #add destination to origin node's list
		self.distances[(originNode, destNode)] = distance # Add distance between two nodes to distance list
	
	#Helper to remove a bidirectional
	def removeEdge(self, originNode, destNode):
		self._removeEdge(originNode, destNode)
		self._removeEdge(destNode, originNode)
		
	#actual removal of the edge
	def _removeEdge(self, originNode, destNode):
		self.edges[originNode].remove(destNode)
		self.distances.pop( (originNode, destNode) ) 
	#remove the edge that looks like so
	
# Install
def dijkstra(graph, start):
	"""
	Implements Dijkstra's Graph Traversal Algorithm for determining the best path in a graph
	"""
	visited = {start: 0}	# Visited contains the distance from all nodes that have been visited
							# Each time we visit a node we'll add it to visited and add the distance/weight as a value to the key
	currentNode = start		# Current node is start
	path = {}	# Will contain our path as we determine it
	nodes = set(graph.nodes) #get set of graph nodes
	
	while nodes:
		minNode = None		# start with no lowestNode
		for node in nodes:	
			if node in visited:	#If the node we're examining has been visited
				if minNode is None:	
					minNode = node	#set the node if we have none set
				elif visited[node] < visited[minNode]:
					minNode = node	#otherwise if we're optimal and it's distance is lowest, visit it
		if minNode is None:
			break	# if we have no node, then something is wrong
		nodes.remove(minNode)	#our nodes list can get rid of our current node
		curWeight = visited[minNode] 
		
		# check the potential routes we can take
		for edge in graph.edges[minNode]:
			weight = curWeight + graph.distances[(minNode, edge)]
			# if we haven't visited it already, or it's lower than the other visited edges
			if edge not in visited or weight < visited[edge]:
				#it's the new edge
				visited[edge] = weight
				path[edge] = minNode
	#once complete return the two paths
	return visited, path
	
def getShortestPath(graph, start, end):
	"""
	Uses the Dijkstras Algorithm to find the best path traversal in a weighted graph
	Returns the optimal route
	"""
	distances, paths = dijkstra(graph, start)
	route = [end]
	
	#while we're looking for the beginning of the path
	while end != start:
		# append the paths from end that head to start
		route.append(paths[end])
		end = paths[end]
		
	route.reverse()
	return route
	
if __name__ == '__main__':
	g = Graph()
	g.nodes = set(range(1, 7))
	g.addEdge(1, 2, 7)
	g.addEdge(1, 3, 9)
	g.addEdge(1, 6, 14)
	g.addEdge(2, 3, 10)
	g.addEdge(2, 4, 15)
	g.addEdge(3, 4, 11)
	g.addEdge(3, 6, 2)
	g.addEdge(4, 5, 6)
	g.addEdge(5, 6, 9)
	print(getShortestPath(g, 1, 5))
	assert(getShortestPath(g, 1, 5) == [1, 3, 6, 5])
	print(getShortestPath(g, 5, 1))
	assert(getShortestPath(g, 5, 1) == [5, 6, 3, 1])
	print(getShortestPath(g, 2, 5))
	assert(getShortestPath(g, 2, 5) == [2, 3, 6, 5])
	print(getShortestPath(g, 1, 4))
	assert(getShortestPath(g, 1, 4) == [1, 3, 4])
	print("Success")