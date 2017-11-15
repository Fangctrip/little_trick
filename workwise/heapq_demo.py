import heapq

class priorityqueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'item {} says hello'.format(self.name)
a=Item('foo')
print(a)
pq=priorityqueue()
pq.push(1,5)
pq.push(2,3)
pq.push(2,2)
pq.push(1,6)
print(pq.pop())

heapq.heappush([1,2,3],)