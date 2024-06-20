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
        self.bavarages.append({
            "name": name.title(),
            "count": count,
            "price": price
        })
        self.__commit()
        print("Ichimliklar muvofaqiyatli qo'shildi.")

    def show_bavarages(self):
        if not self.bavarages:
            print("Ichimliklar topilmadi.")
        else:
            print("Nomi\tSoni\tNarxi")
            for bvg in self.bavarages:
                print(f"{bvg['name']}\t{bvg['count']}  \t{bvg['price']}$")

    def get_bavarage_price(self, name: str):
        for bvg in self.bavarages:
            if bvg["name"] == name.title():
                print(f"{name.title()} ning narxi: {bvg['price']} $")
                return bvg["price"]
        return "Topilmadi."

    def most_expensive_bavarage(self):
        count = 0
        top = []
        for bvg in self.bavarages:
            if bvg["price"] > count:
                count = bvg["price"]
                top.append(f"{bvg['name']} {bvg['price']} $")
        print("Eng qimmat ichimliklar:")
        print(*top[::-1], sep="\n")

    def buy_bavarage(self, name: str, count: int):
        for bvg in self.bavarages:
            if bvg["name"] == name.title():
                if bvg["count"] >= count >= 3:
                    print(f"{count}ta {bvg['name']} ning narxi: {bvg['price'] * count} $ rostan sotib olishni "
                          f"istaysizmi? (ha/yo'q)")
                    sure = input("Ha yoki Yo'q: ").lower()
                    if sure == "ha":
                        bvg["count"] -= count
                        self.__commit()
                        print("Ichimliklar muvofaqiyatli sotib olindi.")
                else:
                    print("Ichimliklar yetarli emas.")
                return
        print("Ichimliklar topilmadi.")


def menu():
    b = Bavarages()
    while True:
        print()
        print("1. Ichimlik qo'shish")
        print("2. Barcha ichimliklarni ko'rish")
        print("3. Ichimliklar narxini ko'rish")
        print("4. Eng qimmat ichimliklar")
        print("5. Sotib olish")
        n = input("4ta menyudan birini tanlang: ")

        if n == "1":
            name = input("Ichimlik nomini kiriting: ")
            count = int(input("Sonini kiriting: "))
            price = float(input("Narxini kiriting: "))
            b.add_bavarages(name, count, price)
        elif n == "2":
            b.show_bavarages()
        elif n == "3":
            name = input("Ichimlik nomini kiriting: ")
            b.get_bavarage_price(name)
        elif n == "4":
            # name = input("Ichimlik nomini kiriting: ")
            b.most_expensive_bavarage()
        elif n == "5":
            name = input("Ichimlik nomini kiriting: ")
            count = int(input("Sonini kiriting: "))
            b.buy_bavarage(name, count)

        print("Davom etishni hohlaysizmi? (ha/yo'q)")
        choice = input("Ha yoki Yo'q: ").lower()
        if choice != "ha":
            print("Hizmatlarimizdan foydalanganingiz uchun rahmat!")
            break


if __name__ == '__main__':
    menu()
