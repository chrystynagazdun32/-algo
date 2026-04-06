class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.heap = [] 

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i].priority > self.heap[parent].priority:
                temp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = temp
                i = parent
            else:
                break

    def _heapify_down(self, i):
        size = len(self.heap)

        while True:
            left = self._left(i)
            right = self._right(i)
            largest = i

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != i:
                temp = self.heap[i]
                self.heap[i] = self.heap[largest]
                self.heap[largest] = temp
                i = largest
            else:
                break

    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def print_heap(self):
        for node in self.heap:
            print(f"value: {node.value}, priority: {node.priority}")

pq = PriorityQueue()

pq.insert("A", 3)
pq.insert("B", 5)
pq.insert("C", 1)
pq.insert("D", 4)

print("черга:")
pq.print_heap()

print("\nмаксимум:", pq.peek().value)

removed = pq.extract_max()
print("\nвидалили:", removed.value)

print("\nпісля видалення:")
pq.print_heap()