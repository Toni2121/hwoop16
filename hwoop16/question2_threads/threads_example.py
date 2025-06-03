import threading


def count_up():
    for i in range(1, 101):
        print(f"Up: {i}")


def count_down():
    for i in range(100, 0, -1):
        print(f"Down: {i}")


t1 = threading.Thread(target=count_up)
t2 = threading.Thread(target=count_down)

t1.start()
t2.start()

t1.join()
t2.join()
