class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # Количество воды в мл
        self.coffee_beans = 200  # Количество кофейных зерен в граммах
        self.money = 0  # Сумма денег в монетоприемнике в рублях

    def print_menu(self):
        print("\nМеню кофемашины:")
        print("1. Эспрессо - 30 рублей")
        print("2. Латте - 50 рублей")
        print("3. Капучино - 40 рублей")
        print("4. Добавить воду")
        print("5. Добавить кофейные зерна")
        print("6. Вернуть деньги")
        print("0. Выход")

    def make_espresso(self):
        if self.water < 50 or self.coffee_beans < 10:
            print("Ошибка: недостаточно ингредиентов.")
            return
        print("Готовится эспрессо. Пожалуйста, подождите.")
        self.water -= 50
        self.coffee_beans -= 10
        self.money += 30
        print("Ваш эспрессо готов. Приятного кофепития!")

    def make_latte(self):
        if self.water < 100 or self.coffee_beans < 20:
            print("Ошибка: недостаточно ингредиентов.")
            return
        print("Готовится латте. Пожалуйста, подождите.")
        self.water -= 100
        self.coffee_beans -= 20
        self.money += 50
        print("Ваш латте готов. Приятного кофепития!")

    def make_cappuccino(self):
        if self.water < 70 or self.coffee_beans < 15:
            print("Ошибка: недостаточно ингредиентов.")
            return
        print("Готовится капучино. Пожалуйста, подождите.")
        self.water -= 70
        self.coffee_beans -= 15
        self.money += 40
        print("Ваш капучино готов. Приятного кофепития!")

    def add_water(self):
        self.water += 200
        print("Добавлена вода (200 мл).")

    def add_coffee_beans(self):
        self.coffee_beans += 50
        print("Добавлены кофейные зерна (50 грамм).")

    def return_money(self):
        print(f"Ваша сдача: {self.money} рублей.")
        self.money = 0

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите опцию (0-6): ")
            if choice == "1":
                self.make_espresso()
            elif choice == "2":
                self.make_latte()
            elif choice == "3":
                self.make_cappuccino()
            elif choice == "4":
                self.add_water()
            elif choice == "5":
                self.add_coffee_beans()
            elif choice == "6":
                self.return_money()
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите опцию от 0 до 6.")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()
