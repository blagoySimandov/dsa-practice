import heapq
import itertools

from dataclasses import dataclass, field

# python doesn't yet support any and iterator as built-in types
from typing import Any, Iterator


# inspired by https://docs.python.org/3/library/heapq.html
@dataclass(order=True)
class PrioritizedItem:
    priority: int | float
    count: int = field(compare=True)  # tie braker when two items have the same priority
    item: Any = field(compare=False)
    REMOVED: bool = field(default=False, compare=False)


class AdaptablePQ:
    def __init__(self):
        self.heap: list[PrioritizedItem] = []
        self.entry_finder: dict[Any, PrioritizedItem] = {}
        self.counter = itertools.count()

    def __len__(self) -> int:
        return len(self.entry_finder)

    def __str__(self) -> str:
        active_entries = [entry for entry in self.heap if not entry.REMOVED]
        return str(active_entries)

    def __iter__(self) -> Iterator[PrioritizedItem]:
        return (entry for entry in self.heap if not entry.REMOVED)

    def add(self, task: Any, priority: int | float = 0) -> PrioritizedItem:
        if task in self.entry_finder:
            self.remove(task)

        count = next(self.counter)
        entry = PrioritizedItem(priority=priority, count=count, item=task)
        self.entry_finder[task] = entry
        heapq.heappush(self.heap, entry)
        return entry

    def remove(self, task: Any) -> None:
        entry = self.entry_finder.pop(task)
        entry.REMOVED = True

    def pop(self) -> tuple[Any, int | float]:
        while self.heap:
            entry = heapq.heappop(self.heap)
            if not entry.REMOVED:
                del self.entry_finder[entry.item]
                return entry.item, entry.priority
        raise IndexError("pop from an empty priority queue")

    def peek(self) -> tuple[Any, int | float]:
        while self.heap:
            entry = self.heap[0]
            if entry.REMOVED:
                heapq.heappop(self.heap)
            else:
                return entry.item, entry.priority
        raise IndexError("peek from an empty priority queue")

    def update_priority(self, task: Any, new_priority: int) -> PrioritizedItem:
        if task not in self.entry_finder:
            raise KeyError(f"Task {task} not found")
        self.remove(task)
        return self.add(task, new_priority)


class AdaptablePQUnsortedList:
    def __init__(self):
        self.items: list[PrioritizedItem] = []
        self.entry_finder: dict[Any, PrioritizedItem] = {}
        self.counter = itertools.count()

    def __len__(self) -> int:
        return len(self.entry_finder)

    def __str__(self) -> str:
        active_entries = [entry for entry in self.items if not entry.REMOVED]
        return str(active_entries)

    def __iter__(self) -> Iterator[PrioritizedItem]:
        return (entry for entry in self.items if not entry.REMOVED)

    def add(self, task: Any, priority: int | float = 0) -> PrioritizedItem:
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = PrioritizedItem(priority=priority, count=count, item=task)
        self.entry_finder[task] = entry
        self.items.append(entry)
        return entry

    def remove(self, task: Any) -> None:
        entry = self.entry_finder.pop(task)
        entry.REMOVED = True

    def pop(self) -> tuple[Any, int | float]:
        if not self.items:
            raise IndexError("pop from an empty priority queue")

        min_idx = -1
        min_entry = None

        for i, entry in enumerate(self.items):
            if not entry.REMOVED and (min_entry is None or entry < min_entry):
                min_idx = i
                min_entry = entry

        if min_entry is None:
            self.items = []
            raise IndexError("pop from an empty priority queue")

        self.items.pop(min_idx)
        del self.entry_finder[min_entry.item]
        return min_entry.item, min_entry.priority

    def peek(self) -> tuple[Any, int | float]:
        if not self.items:
            raise IndexError("peek from an empty priority queue")

        min_entry = None

        for entry in self.items:
            if not entry.REMOVED and (min_entry is None or entry < min_entry):
                min_entry = entry

        if min_entry is None:
            raise IndexError("peek from an empty priority queue")

        return min_entry.item, min_entry.priority

    def update_priority(self, task: Any, new_priority: int) -> PrioritizedItem:
        if task not in self.entry_finder:
            raise KeyError(f"task {task} not found")
        self.remove(task)
        return self.add(task, new_priority)


class SimplePQ:
    def __init__(self):
        self.heap: list[PrioritizedItem] = []
        self.counter = itertools.count()

    def __len__(self) -> int:
        return len(self.heap)

    def __str__(self) -> str:
        return str(self.heap)

    def __iter__(self) -> Iterator[PrioritizedItem]:
        return iter(self.heap)

    def add(self, task: Any, priority: int | float = 0) -> PrioritizedItem:
        count = next(self.counter)
        entry = PrioritizedItem(priority=priority, count=count, item=task)
        heapq.heappush(self.heap, entry)
        return entry

    def pop(self) -> tuple[Any, int | float]:
        if not self.heap:
            raise IndexError("pop from an empty priority queue")
        entry = heapq.heappop(self.heap)
        return entry.item, entry.priority

    def peek(self) -> tuple[Any, int | float]:
        if not self.heap:
            raise IndexError("peek from an empty priority queue")
        entry = self.heap[0]
        return entry.item, entry.priority
