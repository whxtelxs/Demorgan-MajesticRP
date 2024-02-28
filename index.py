import time
import ctypes
import os

# Функция для отправки уведомления
def send_notification(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x1000)

# Функция для обратного отсчета
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    send_notification("Demorgan MajesticRP", "Время вышло, задание можно завершить.")

# Основной цикл программы
def main():
    while True:
        print("Demorgan MajesticRP by lis")
        print("Выберите опцию:")
        print("1. Шкрябать туалеты 🪠")
        print("2. Мыть полы 🧼")
        print("3. Собирать мусор 🧹")
        print("0. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            countdown(35)
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            countdown(55)
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            countdown(75)
        elif choice == '4':
            break
        else:
            print("Неверный пункт меню. Попробуйте еще раз.")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
