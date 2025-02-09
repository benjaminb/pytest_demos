# Function to create a list of 1000 elements
def create_list():
    return [i for i in range(1000)]

# Function to create a set of 1000 elements


def create_set():
    return set([i for i in range(1000)])

# Function to find an element in a collection


def find(it, el=50):
    return el in it

# Performance test for a list


def test_list(benchmark):
    # The benchmark fixture is passed as an argument
    # It measures the performance of the find function with a list
    benchmark(find, it=create_list())

# Performance test for a set


def test_set(benchmark):
    # The benchmark fixture is passed as an argument
    # It measures the performance of the find function with a set
    benchmark(find, it=create_set())
