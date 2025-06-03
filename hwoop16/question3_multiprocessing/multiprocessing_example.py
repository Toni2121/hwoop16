from multiprocessing import Process


def count_up():
    for i in range(1, 101):
        print(f"Up: {i}")


def count_down():
    for i in range(100, 0, -1):
        print(f"Down: {i}")


if __name__ == '__main__':
    p1 = Process(target=count_up)
    p2 = Process(target=count_down)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
