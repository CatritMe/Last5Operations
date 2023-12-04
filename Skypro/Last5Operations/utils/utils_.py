import json
import datetime as dt


def read_json():
    """Перевод из json в формат python"""
    with open("C:/Users/Skypro/Last5Operations/operations.json", "r", encoding="utf-8") as file:
        return json.load(file)

def search_executed(data):
    """Выборка успешных операций"""
    data = [elem for elem in data if elem and elem['state'] == 'EXECUTED']
    return data

def sort_executed(data):
    """Сортировка по дате и выбор 5 последних"""
    s_data = sorted(data, key=lambda x:x['date'], reverse=True)
    return s_data[:5]

def edit_date(date:str):
    """Преобразование даты"""
    date = date[0:10]
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    new_date = date.strftime("%d.%m.%Y")
    return new_date

def secret_numb(number:str, to=False):
    """Скрытие номера карты/счета"""
    if not to:
        return f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    else:
        return f'** {number[-4:]}'

def print_operations(data):
    """Компановка в нужный вид"""
    operations = []
    for operation in data:
        date = edit_date(operation['date'])
        to_name = ''.join(c if not c.isdigit() else '' for c in operation['to'])
        number_to = ''.join(c if c.isdigit() else '' for c in operation['to'])
        if 'Счет' in to_name:
            secreted_to = secret_numb(number_to, to=True)
        else:
            secreted_to = secret_numb(number_to)
        if 'from' in operation:
            from_name = ''.join(c if not c.isdigit() else '' for c in operation['from'])
            number_from = ''.join(c if c.isdigit() else '' for c in operation['from'])
            if 'Счет' in from_name:
                secreted = secret_numb(number_from, to=True)
            else:
                secreted = secret_numb(number_from)
            operations.append(f"{date} {operation['description']}\n{from_name} {secreted} -> {to_name} {secreted_to}\n"
                              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")

        else:
            operations.append(
                f"{date} {operation['description']}\n{to_name} {secreted_to}\n"
                f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    return operations
