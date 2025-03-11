import heapq


class Heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def __iter__(self):
        return iter(self.heap)

    def add(self, key, value):
        heapq.heappush(self.heap, (key, value))
