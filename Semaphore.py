import threading
import time

semaphore = threading.Semaphore(2)

def access_resource(name):
    print(f"{name} waiting...")
    with semaphore:
        print(f"{name} acquired semaphore")
        time.sleep(1)
        print(f"{name} released semaphore")

threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semaphore example completed!")
