import json
import datetime as dt


def read_json():
    '''Перевод из json в формат python'''
    with open("C:/Users/Skypro/Last5Operations/operations.json", "r", encoding="utf-8") as file:
        return json.load(file)

def search_executed(data):
    """Выборка успешных операций"""
    data = [elem for elem in data if elem and elem['state'] == 'EXECUTED']
    return data

def sort_executed(data):
    s_data = sorted(data, key=lambda x:x['date'], reverse=True)
    return s_data[:5]

def edit_date(date:str):
    date = date[0:10]
    date = dt.datetime.strptime(date, "%Y-%m-%d")
    new_date = date.strftime("%d.%m.%Y")
    return new_date

def secret_numb(number:str, to=False): #для карты, для счета указать тру
    if not to:
        return f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    else:
        return f'** {number[-4:]}'


def print_operations():
    pass

