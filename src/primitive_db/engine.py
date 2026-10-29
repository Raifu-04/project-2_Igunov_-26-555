import shlex
import prompt
from primitive_db.utils import load_metadata, save_metadata
from primitive_db.core import create_table, drop_table

def welcome():
    print("\n***")
    print("<command> create <имя_таблицы> <столбец1>:<тип> ... - создать таблицу")
    print("<command> drop <имя_таблицы> - удалить таблицу")
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")
    print()

def run():
    json_file = "db_meta.json"
    metadata = load_metadata(json_file)

    welcome()

    while True:
        command = prompt.string(">>> Введите команду: ")

        try:
            args = shlex.split(command)
        except ValueError as e:
            print(f"Ошибка формата: {e}")
            continue

        if not args:
            continue

        cmd = args[0].lower()

        if cmd == "exit":
            print("Выход из программы...")
            break
            
        elif cmd == "help":
            welcome()
            
        elif cmd == "drop":
            if len(args) < 2:
                print("Ошибка: укажите имя таблицы.")
                continue
            
            table_name = args[1]
            try:
                metadata = drop_table(metadata, table_name)
                save_metadata(json_file, metadata)
                print(f"Таблица '{table_name}' удалена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif cmd == "create":
            if len(args) < 3:
                print("Ошибка: укажите имя таблицы и столбцы.")
                continue
                
            table_name = args[1]
            columns_raw = args[2:] 
            
            columns = []
            for col in columns_raw:
                parts = col.split(':')
                if len(parts) == 2:
                    columns.append({"name": parts[0], "type": parts[1]})
                else:
                    print(f"Ошибка в столбце '{col}'. Используйте формат имя:тип")
                    break
            else:
                try:
                    metadata = create_table(metadata, table_name, columns)
                    save_metadata(json_file, metadata)
                    print(f"Таблица '{table_name}' создана.")
                except ValueError as e:
                    print(f"Ошибка: {e}")
        else:
            print("Неизвестная команда. Введите 'help' для справки.")
