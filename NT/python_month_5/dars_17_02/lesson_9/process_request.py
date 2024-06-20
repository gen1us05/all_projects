import multiprocessing
import requests
import json

def make_request(url):
    response = requests.get(url)
    # with open("main_page.html", "w") as file:
    #     file.write(response.text)
    print(f"Response from {url}: {response.text}")

def main():
    urls = ['https://example.com/', 'https://kun.uz/', 'https://python.org/', ]
    # file_path = "main_page.html"

    # Create processes
    processes = [multiprocessing.Process(target=make_request, args=(url,)) for url in urls]

    # Start processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    main()