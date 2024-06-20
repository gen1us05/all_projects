import threading
import time
from datetime import datetime

def read_file(file_path):
    with open(file_path, 'r') as file:
        time.sleep(3)
        data = file.read(5)
        print(f"Data read from {file_path}: {data}")

def main():
    file_path1 = 'data/file1.txt'
    file_path2 = 'data/file1.txt'
    file_path3 = 'data/file1.txt'
    file_path4 = 'data/file2.txt'
    file_path5 = 'data/file2.txt'
    file_path6 = 'data/file2.txt'
    file_path7 = 'data/file2.txt'

    # Create threads
    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path3,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))
    thread5 = threading.Thread(target=read_file, args=(file_path5,))
    thread6 = threading.Thread(target=read_file, args=(file_path6,))
    thread7 = threading.Thread(target=read_file, args=(file_path7,))

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()

    # # Wait for both threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()

    print("Main thread continues execution.")

if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
