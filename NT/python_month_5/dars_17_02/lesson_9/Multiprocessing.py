import multiprocessing
import time
from datetime import datetime
from data.base import Database

def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        time.sleep(3)
        file.write(data + "\n")
        print(f"Data written to {file_path}")

def insert_data(table, query):
    time.sleep(3)
    print(table + " " + Database.connect(query, "insert"))

def select_date(table, query):
    time.sleep(3)
    print("\n")
    print(f"{table}: {Database.connect(query, "select")}\n")

def read_and_write(table1, table2):
    query = f"""SELECT * FROM {table1}"""
    data_table1 = Database.connect(query, "select")
    for i in data_table1:
        insert_query = f"""INSERT INTO {table2}(title, price) VALUES('{i[1]}', {i[2]})"""
        process1 = multiprocessing.Process(target=insert_data, args=(table2, insert_query))
        process1.start()
        process1.join()


def main():
    table1 = "book_clone"
    table2 = "book"
    process1 = multiprocessing.Process(target=read_and_write, args=(table1, table2))
    process1.start()
    process1.join()


    # book_table = 'book_clone'
    # author_table = 'author'
    # data_book = {"column": ('title', 'price'), "values": ('Python', 20)}
    # data_author = {"column": ('first_name', 'last_name', 'birth_date'), "values": ('John', 'Smith', '2003-11-25')}
    # query_1 = f"""INSERT INTO book_clone(title, price) VALUES('{data_book["values"][0]}', {data_book["values"][1]})"""
    # query_2 = f"""INSERT INTO author(first_name, last_name, birth_date) VALUES('{data_author["values"][0]}', '{data_author["values"][1]}', '{data_author["values"][2]}')"""
    # query_select_1 = """SELECT * FROM book;"""
    # query_select_2 = """SELECT * FROM author;"""
    # query_select_3 = """SELECT * FROM author;"""
    # query_select_4 = """SELECT * FROM author;"""
    #
    # # Create processes
    # process2 = multiprocessing.Process(target=insert_data, args=(book_table, query_1))
    # process3 = multiprocessing.Process(target=insert_data, args=(book_table, query_1))
    #
    # #
    # # # Start processes
    # process2.start()
    # process3.start()
    # # process4.start()
    # # process2.start()
    #
    # # Wait for both processes to finish
    # # process1.join()
    # #
    # process2.join()
    # process3.join()
    # # process4.join()
    # # process5.join()
    #
    #
    # # process1 = multiprocessing.Process(target=select_date, args=(book_table, query_select_1))
    # # process2 = multiprocessing.Process(target=select_date, args=(author_table, query_select_2))
    # # process3 = multiprocessing.Process(target=select_date, args=(book_table, query_select_3))
    # # process4 = multiprocessing.Process(target=select_date, args=(author_table, query_select_4))
    # #
    # # process1.start()
    # # process2.start()
    # # process3.start()
    # # process4.start()
    # #
    # # process1.join()
    # # process2.join()
    # # process3.join()
    # # process4.join()

# print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
    # query = f"SELECT * FROM book"
    # for i in Database.connect(query, 'select'):
    #     print(i)




