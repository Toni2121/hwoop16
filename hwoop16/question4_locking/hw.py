import threading
from time import sleep

lock = threading.Lock()


def print_capital_cities(cities):
    with lock:
        for city in cities:
            print(f"Capital: {city}")
            sleep(0.1)


if __name__ == "__main__":
    cities1 = ["Paris", "Berlin", "Madrid"]
    cities2 = ["Rome", "London", "Athens"]

    t1 = threading.Thread(target=print_capital_cities, args=(cities1,))
    t2 = threading.Thread(target=print_capital_cities, args=(cities2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
