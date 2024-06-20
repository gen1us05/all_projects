import time


def example(start, stop, step):
    start = 1
    while start <= stop:
        time.sleep(1)
        yield start
        start += step

if __name__ == '__main__':
    a = example(2, 20, 3)
    for i in a:
        print(i)
