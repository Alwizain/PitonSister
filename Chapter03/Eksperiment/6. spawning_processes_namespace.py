import multiprocessing
from myFunc import fungsiKu

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=fungsiKu, args=(i,))
        process.start()
        process.join()