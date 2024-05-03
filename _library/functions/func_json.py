import json

def read_json(filename, encoder = 'utf-8'):
    with open(filename, 'r', encoding=encoder) as file:
        return json.load(file)
    # print(json.dumps(settings))

# def write_json(filename, encoder = 'utf-8'):
#     with open(filename, 'w', encoding=encoder) as file:

        # json.dump
