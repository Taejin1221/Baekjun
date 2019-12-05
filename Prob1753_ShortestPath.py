# Prob1753_ShortestPath.py
from math import inf

class PriorityQueue():
	def __init__(self):
		self.queue = [ None, ]
		self.size = 1


	def push(self, data):
		self.queue.append(data)
		self.size = self.size + 1
		me = self.size - 1
		mom = me // 2
		while (me != 1 and self.queue[mom] > self.queue[me]):
			self.queue[mom], self.queue[me] = self.queue[me], self.queue[mom]
			me = mom
			mom = me // 2


	def Heapify(self, me):
		leftChild = me * 2
		rightChild = me * 2 + 1

		smaller = None
	
		if (leftChild >= self.size):
			return
		elif (rightChild >= self.size):
			smaller = leftChild
		else:
			if (self.queue[leftChild] < self.queue[rightChild]):
				smaller = leftChild
			else:
				smaller = rightChild

			if (self.queue[smaller] < self.queue[me]):
				self.queue[smaller], self.queue[me] = self.queue[me], self.queue[smaller]
				self.Heapify(smaller)


	def pop(self):
		last = self.size - 1
		self.queue[1], self.queue[last] = self.queue[last], self.queue[1]

		self.size = self.size - 1

		self.Heapify(1)

		return self.queue.pop()
		

	def isEmpty(self) -> 'bool':
		if self.queue: return False
		else: return True


	def PrintQueue(self):
		print(self.queue)

if (__name__ == '__main__'):
	myQueue = PriorityQueue()
	myQueue.push(3)
	myQueue.push(5)
	myQueue.push(1)
	myQueue.push(2)
	myQueue.push(6)
	myQueue.PrintQueue()

	for i in range(5):
		print(myQueue.pop())
		myQueue.PrintQueue()


class Graph():
	VISIT = 1
	UNVISIT = 0
	V = 0
	W = 1

	def __init__(self, vertexSize):
		self.adjList = { vertex:[] for vertex in range(1, vertexSize + 1) }
		self.vertexSize = vertexSize


	def InsertEdge(self, vertex, adjVertex, weight):
		self.adjList[vertex].append((adjVertex, weight))
		self.adjList[vertex].sort()

	def PrintGraph(self):
		for curr in self.adjList:
			print('V({}) = {}'.format(curr, self.adjList[curr]))

	def DijkstraAlgorithm(self, start):
		visited = { vertex: Graph.UNVISIT \
		for vertex in range(1, self.vertexSize + 1) }
		shortestPath = { vertex: inf \
		for vertex in range(1, self.vertexSize + 1) }

		visited[start], shortestPath[start] = Graph.VISIT, 0
		for i in range(self.vertexSize - 1):
			minPath = None
			for currVertex in self.adjList:
				if (visited[currVertex] is Graph.VISIT):
					for adjVertex in self.adjList[currVertex]:
						adjVertexNum = adjVertex[Graph.V]
						if (visited[adjVertexNum] is Graph.UNVISIT):
							tempWeight = shortestPath[currVertex] + adjVertex[Graph.W]
							if (shortestPath[adjVertexNum] > tempWeight):
								shortestPath[adjVertexNum] = tempWeight
								
							if ((minPath is None) or \
								(shortestPath[minPath] > shortestPath[adjVertexNum])):
								minPath = adjVertexNum
			if (minPath is not None):
				visited[minPath] = Graph.VISIT

		for short in shortestPath:
			if shortestPath[short] is not inf:
				print(shortestPath[short])
			else:
				print('INF')

if (__name__ == '__main__'):
	vertexSize, edgeSize = map(int, input().split())
	start = int(input())

	myGraph = Graph(vertexSize)

	for _ in range(edgeSize):
		u, v, w = map(int, input().split())
		myGraph.InsertEdge(u, v, w)

	myGraph.DijkstraAlgorithm(start)

	# myGraph.PrintGraph()

	# myGraph = Graph(5)
	# myGraph.InsertEdge(5, 1, 1)
	# myGraph.InsertEdge(1, 2, 2)
	# myGraph.InsertEdge(1, 3, 3)
	# myGraph.InsertEdge(2, 3, 4)
	# myGraph.InsertEdge(2, 4, 5)
	# myGraph.InsertEdge(3, 4, 6)
	# myGraph.DijkstraAlgorithm(1)	