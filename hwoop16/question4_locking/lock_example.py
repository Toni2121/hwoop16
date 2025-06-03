import threading

lock = threading.Lock()


def critical_section(name):
    with lock:
        print(f"{name} is accessing the resource")


t1 = threading.Thread(target=critical_section, args=("Thread 1",))
t2 = threading.Thread(target=critical_section, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()
