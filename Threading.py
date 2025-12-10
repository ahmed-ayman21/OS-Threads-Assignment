import threading
import time

def worker(name):
    for i in range(5):
        print(f"Thread {name}: iteration {i}")
        time.sleep(0.5)

# Create two threads
t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Threading example completed!")
