import threading
from algorithm1 import algorithm1
from algorithm2 import algorithm2
from algorithm3 import algorithm3

def run_algorithm(algorithm, data):
    result = algorithm(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    with open('input/input.txt', 'r') as file:
        data = list(map(int, file.read().split()))

    threads = []
    for algorithm in [algorithm1, algorithm2, algorithm3]:
        thread = threading.Thread(target=run_algorithm, args=(algorithm, data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
