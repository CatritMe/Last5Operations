from utils.utils_ import read_json, search_executed, sort_executed, print_operations

data = read_json()
data = search_executed(data)
data = sort_executed(data)
printed = print_operations(data)

#Выыод нужного результата
for i in printed:
    print(f'{i}\n')