# Adaptable Priority Queue

This project implements an Adaptable Priority Queue in Python using the `heapq` module from the standard library.

## Overview

An adaptable priority queue is a data structure that allows:

- Adding items with priorities
- Removing items with the highest priority (lowest value)
- Updating the priority of existing items
- Removing specific items from anywhere in the queue

This implementation is based on the example from the [Python heapq documentation](https://docs.python.org/3/library/heapq.html).

## Implementation Details

The implementation uses a binary heap (via `heapq`) with the following components:

- A heap list that stores entries as `[priority, count, task]` tuples
- A dictionary that maps tasks to their entries for O(1) lookups
- A counter to break ties when priorities are equal

Key operations:

- `add_task(task, priority)`: Add a new task or update an existing one
- `remove_task(task)`: Remove a specific task from the queue
- `pop_task()`: Remove and return the highest priority task
- `peek()`: View the highest priority task without removing it
- `update_priority(task, new_priority)`: Change a task's priority

## Usage

```python
from adaptable_pq import AdaptablePQ

# Create a new priority queue
pq = AdaptablePQ()

# Add tasks with priorities
pq.add_task("Task A", 5)
pq.add_task("Task B", 3)
pq.add_task("Task C", 7)

# Update a task's priority
pq.update_priority("Task C", 1)

# Get the highest priority task (lowest number)
task, priority = pq.peek()
print(f"Highest priority: {task} with priority {priority}")

# Remove and return the highest priority task
task, priority = pq.pop_task()
print(f"Popped: {task} with priority {priority}")

# Remove a specific task
pq.remove_task("Task B")
```

## Running the Tests

To run the test file:

```
python test_adaptable_pq.py
```

## Time Complexity

- Add task: O(log n)
- Remove task: O(1) amortized (marking as removed)
- Pop task: O(log n) amortized
- Update priority: O(log n)
- Peek: O(1) amortized
