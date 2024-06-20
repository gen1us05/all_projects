import json


class Bavarages:
    def __init__(self):
        self.file = "bavarages.json"
        self.__get_data()

    def __get_data(self):
        try:
            with open(self.file, "r") as f:
                self.bavarages = json.load(f)
        except FileNotFoundError:
            self.bavarages = []

    def __commit(self):
        with open(self.file, "w") as f:
            json.dump(self.bavarages, f, indent=4)

    def add_bavarages(self, name: str, count: int, price: float):
        for bvg in self.bavarages:
            if bvg["name"] == name.title():
                bvg['count'] += count
                bvg['price'] = price
                print("Bavarages added successfully.")
                self.__commit()
                break
        else:
            self.bavarages.append({
                "name": name.title(),
                "count": count,
                "price": price
            })
            return
        self.__commit()
        print("Bavarages added successfully.")

    def show_bavarages(self):
        if not self.bavarages:
            print("Bavarages not found.")
        else:
            print("Name\tCount\tPrice")
            for bvg in self.bavarages:
                print(f"{bvg['name']}\t{bvg['count']}  \t{bvg['price']}$")

    def get_bavarage_price(self, name: str):
        for bvg in self.bavarages:
            if bvg["name"] == name.title():
                print(f"{name.title()} price: {bvg['price']} $")
                return bvg["price"]
        return "Not found."

    def most_expensive_bavarage(self):
        count = 0
        top = []
        for bvg in self.bavarages:
            if bvg["price"] > count:
                count = bvg["price"]
                top.append(f"{bvg['name']} {bvg['price']} $")
        print("The most expensive Bavarages:")
        print(*top[::-1], sep="\n")

    def buy_bavarage(self, name: str, count: int):
        for bvg in self.bavarages:
            if bvg["name"] == name.title():
                if bvg["count"] >= count >= 3:
                    print(f"{count} {bvg['name']} price: {bvg['price'] * count} $ to actually buy "
                          f"do you want? (Yes/No)")
                    sure = input("Yes or No: ").lower()
                    if sure == "yes":
                        bvg["count"] -= count
                        self.__commit()
                        print("Bavarages successfully purchased.")
                else:
                    print("Not enough bavarages.")
                return
        print("No bavarages found.")


def menu():
    b = Bavarages()
    while True:
        print()
        print("1. Add Bavarage")
        print("2. Show All Bavarages")
        print("3. Show Bavarage Price")
        print("4. Most Expensive Bavarages")
        print("5. Buy Bavarage")
        n = input("Chose one menu: ")

        if n == "1":
            name = input("Bavarage name: ")
            count = int(input("Bavarage count: "))
            price = float(input("Bavarage price: "))
            b.add_bavarages(name, count, price)
        elif n == "2":
            b.show_bavarages()
        elif n == "3":
            name = input("Enter Bavarage Name: ")
            b.get_bavarage_price(name)
        elif n == "4":
            # name = input("Ichimlik nomini kiriting: ")
            b.most_expensive_bavarage()
        elif n == "5":
            name = input("Enter Bavarage Name: ")
            count = int(input("Enter Bavarage Count: "))
            b.buy_bavarage(name, count)

        print("Do you want to continue? (Yes/No)")
        choice = input("Yes or No: ").lower()
        if choice == "no":
            print("Thank you for using our services!")
            break


if __name__ == '__main__':
    menu()
