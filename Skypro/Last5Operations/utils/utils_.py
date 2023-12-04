import json

def get_from_json():
    with open("operations.json", "r") as file:
        operations_json = file.read()

    return json.loads(operations_json)

