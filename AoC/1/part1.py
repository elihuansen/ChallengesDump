from pprint import pprint

def read_input_lines(file_path):
    with open(file_path) as f:
        data = f.read().split('\n')[:-1]
    return data

print(sum(int(x) for x in read_input_lines('1/input.txt')))
