# min heap
# children are always smaller than parents

class Heap:
	def __init__(self):
		self.heap = [0]
		self.size = 0

	def percUp(self, i):
		while i//2 > 0: 
			if self.heap[i] < self.heap[i//2]: # if current node < its parent
				# temp = self.heap[i//2]
				# self.heap[i//2] = self.heap[i]
				# self.heap[i] = temp
				self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
			i = i//2

	def insert(self, k):
		self.heap.append(k)
		self.size += 1

		self.percUp(self.size) # sort 

	def percDown(self, i):
		while (i * 2) <= self.size: # check for children
			min_child = self.minChild(i) # get the smaller child index of parent @ i
			if self.heap[min_child] < self.heap[i]:
				# switch
				self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
			i = min_child

	def minChild(self, i):
		if i * 2 + 1 > self.size:
			return i*2
		if self.heap[i*2] < self.heap[i*2 + 1]: # if it's a tie between the two children, return the right-most child to preserve heap properties/order
			return i*2 
		return i*2 + 1

	def popMin(self): 
		out = self.heap[1]
		self.heap[1] = self.heap[-1]
		self.size -= 1
		self.heap.pop()
		# print self.heap
		self.percDown(1)
		return out

	def build(self, l):
		self.size = len(l)
		i = len(l)//2 # i will be at second to last level of tree, parent of last element
		self.heap = [0] + l[:] # make sure to create a copy of l! Don't want edits to original list to mess with heap...
		
		while i > 0: # percDown all the heap elements
			self.percDown(i)
			i -= 1

h = Heap()
print h.heap
h.insert(10)
h.insert(1)
print h.heap
l = [0,9,3,44,1,2,99,93]
h.build(l)
print h.heap
print h.popMin()
print h.popMin()