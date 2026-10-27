import prompt

print("Первая попытка запустить проект!")

def welcome():
    print("\n***")

    while True:
        print('<command> exit - выйти из программы')
        print('<command> help - справочная информация')

        command = prompt.string("Введите команду: ")

        if command == "exit":
            print("Выход из программы...")
            break
        elif command == "help":
            print("\n")
            continue
        else:
            print("Данной команды нет. Попробуйте ещё раз")
            print("\n")
