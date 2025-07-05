import random
import time

def experiment(n, m, c):
    splay_tree = splay_tree()
    numbers = list(range(n))
    random.shuffle(numbers)

    # Step 1: Insert n numbers into the splay tree
    for number in numbers:
        splay_tree.insert(number)

    # Step 2: Perform m queries
    query_numbers = random.choices(numbers, k=int(c * m)) + random.choices(range(n, 2 * n), k=m - int(c * m))
    random.shuffle(query_numbers)

    start_time = time.time()
    for query in query_numbers:
        splay_tree.search(query)
    end_time = time.time()

    print(f"Total time for {m} queries: {end_time - start_time:.4f} seconds")

# Example usage
n = 1000
m = 100000
c = 0.1
experiment(n, m, c)