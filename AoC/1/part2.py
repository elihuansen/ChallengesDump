from pprint import pprint 
from collections import defaultdict

def read_input_lines(file_path):
    with open(file_path) as f:
        data = [int(x) for x in f.read().split('\n')[:-1]]
    return data
    
d = defaultdict(int)
total = 0

arr = read_input_lines('1/input.txt')

while True:
    
    for num in arr:
        total    += num
        d[total] += 1

        if d[total] > 1:
            print(total)
            exit(0)

print(':(')