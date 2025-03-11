import heapq
import itertools

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple, Optional, Iterator

#https://docs.python.org/3/library/heapq.html
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    count: int = field(compare=True)
    item: Any = field(compare=False)
    REMOVED: bool = field(default=False, compare=False)


class AdaptablePQ:
    def __init__(self):
        self.heap: List[PrioritizedItem] = []
        self.entry_finder: Dict[Any, PrioritizedItem] = {}
        self.counter = itertools.count()

    def __len__(self) -> int:
        return len(self.entry_finder)

    def __str__(self) -> str:
        active_entries = [entry for entry in self.heap if not entry.REMOVED]
        return str(active_entries)

    def __iter__(self) -> Iterator[PrioritizedItem]:
        return (entry for entry in self.heap if not entry.REMOVED)

    def add_task(self, task: Any, priority: int = 0) -> PrioritizedItem:
        if task in self.entry_finder:
            self.remove_task(task)
        
        count = next(self.counter)
        entry = PrioritizedItem(priority=priority, count=count, item=task)
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)
        return entry

    def remove_task(self, task: Any) -> None:
        entry = self.entry_finder.pop(task)
        entry.REMOVED = True

    def pop_task(self) -> Tuple[Any, int]:
        while self.heap:
            entry = heapq.heappop(self.heap)
            if not entry.REMOVED:
                del self.entry_finder[entry.item]
                return entry.item, entry.priority
        raise IndexError('pop from an empty priority queue')
    
    def peek(self) -> Tuple[Any, int]:
        while self.heap:
            entry = self.heap[0]
            if entry.REMOVED:
                heapq.heappop(self.heap)
            else:
                return entry.item, entry.priority
        raise IndexError('peek from an empty priority queue')
    
    def update_priority(self, task: Any, new_priority: int) -> PrioritizedItem:
        if task not in self.entry_finder:
            raise KeyError(f'Task {task} not found')
        self.remove_task(task)
        return self.add_task(task, new_priority) 