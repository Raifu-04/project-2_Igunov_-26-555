def create_table(metadata, table_name, columns):
    if table_name in metadata:
        raise ValueError("Таблица уже существует")

    type_colomn = ['int', 'str', 'bool']

    for i in columns:
        if i["type"] not in type_colomn:
            raise ValueError("Поддерживаемые типы данных только int, str или bool")

    column = {"name": "ID", "type": "int"}
    columns.insert(0, column)
    
    metadata[table_name] = columns
    return metadata


def drop_table(metadata, table_name):
    if table_name in metadata:
        del metadata[table_name]
        return metadata
    else:
        raise ValueError("Такой таблицы нет")