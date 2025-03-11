from adaptable_pq import AdaptablePQ

def test_adaptable_pq():
    pq = AdaptablePQ()
    
    entry1 = pq.add_task("Task 1", 5)
    entry2 = pq.add_task("Task 2", 3)
    entry3 = pq.add_task("Task 3", 7)
    entry4 = pq.add_task("Task 4", 1)
    
    print(f"Queue size: {len(pq)}")
    
    task, priority = pq.peek()
    print(f"Highest priority task: {task} with priority {priority}")
    
    print("\nUpdating Task 3's priority from 7 to 0...")
    pq.update_priority("Task 3", 0)
    
    task, priority = pq.peek()
    print(f"Highest priority task: {task} with priority {priority}")
    
    print("\nRemoving Task 2...")
    pq.remove_task("Task 2")
    
    print("\nPopping tasks in priority order:")
    while len(pq) > 0:
        task, priority = pq.pop_task()
        print(f"Popped: {task} with priority {priority}")

if __name__ == "__main__":
    test_adaptable_pq() 