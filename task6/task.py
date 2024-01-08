import numpy as np
import json
import sys

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def flatten(exp):
    flat_list = []
    for obj in exp:
        if isinstance(obj, int):
            flat_list.append(obj)
        else:
            flat_list.extend(obj)
    return flat_list

def task(expA, expB):
    expA_flat = flatten(expA)
    expB_flat = flatten(expB)

    n = len(expA_flat)
    m = 2

    x = [0] * n
    for obj in range(n):
        x[obj] += expA_flat[obj] + expB_flat[obj]

    X = sum(x) / n
    S = sum([(Xi - X) ** 2 for Xi in x])

    return round(12 * S / m / m / (n ** 3 - n), 2)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Введите две json-строки, содержащие ранжировки.")

    a_file, b_file = sys.argv[1], sys.argv[2]
    a, b = read_json_from_file(a_file), read_json_from_file(b_file)
    print(task(a, b))

#a = "[1,[2,3],4,[5,6,7],8,9,10]"
#b = "[[1,2],[3,4,5],6,7,9,[8,10]]"
#c = "[3,[1,4],2,6,[5,7,8],[9,10]]"