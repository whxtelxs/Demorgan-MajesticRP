import time
import os
from plyer import notification

def countdown(seconds):
    for i in range(seconds, 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Осталось {i} секунды...")
        time.sleep(1)

    notification.notify(
        title='Demorgan MajesticRP',
        message=f'Время вышло, задание можно завершить.',
        app_icon=None,
    )
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        print("Demorgan MajesticRP by lis")
        print("Выберите опцию:")
        print("1. Шкрябать туалеты 🪠")
        print("2. Мыть полы 🧼")
        print("3. Собирать мусор 🧹")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        try:
            choice = int(choice)
            if choice == 1:
                countdown(35)
            elif choice == 2:
                countdown(55)
            elif choice == 3:
                countdown(75)
            elif choice == 0:
                print("Программа завершена.")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError as e:
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main_menu()
