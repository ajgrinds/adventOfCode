import csv


def parse_code(code):
    op_code = code % 100
    params = []
    num_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}
    code //= 10
    for i in range(num_params[op_code]):
        code //= 10
        if code % 10 == 1:
            params.append(1)
        elif code % 10 == 0:
            params.append(0)
        elif code % 10 == 2:
            params.append(2)
    return op_code, params


def get_val(values, i, mode, base):
    return values[get_index(values, i, mode, base)]


def get_index(values, i, mode, base):
    index = 0
    if mode == 0:
        index = values[i]
    elif mode == 1:
        index = i
    elif mode == 2:
        index = values[i] + base
    return index


def calc(system_id):
    with open('../input.csv', 'r') as f:
        reader = csv.reader(f)
        values = list(reader)[0]

    values = [int(value) for value in values]
    i = 0
    relative_base = 0
    while i < len(values):
        op_code, params = parse_code(values[i])
        try:
            if op_code == 1:
                first_param = get_val(values, i + 1, params[0], relative_base)
                second_param = get_val(values, i + 2, params[1], relative_base)
                values[get_index(values, i + 3, params[2], relative_base)] = first_param + second_param
                i += 4
            elif op_code == 2:
                first_param = get_val(values, i + 1, params[0], relative_base)
                second_param = get_val(values, i + 2, params[1], relative_base)
                values[get_index(values, i + 3, params[2], relative_base)] = first_param * second_param
                i += 4
            elif op_code == 3:
                values[get_index(values, i + 1, params[0], relative_base)] = system_id
                i += 2
            elif op_code == 4:
                print(get_val(values, i + 1, params[0], relative_base))
                i += 2
            elif op_code == 5:
                if values[get_index(values, i + 1, params[0], relative_base)] != 0:
                    i = get_val(values, i + 2, params[1], relative_base)
                else:
                    i += 3
            elif op_code == 6:
                if values[get_index(values, i + 1, params[0], relative_base)] == 0:
                    i = get_val(values, i + 2, params[1], relative_base)
                else:
                    i += 3
            elif op_code == 7:
                first_param = get_val(values, i + 1, params[0], relative_base)
                second_param = get_val(values, i + 2, params[1], relative_base)
                if first_param < second_param:
                    third_param = 1
                else:
                    third_param = 0
                values[get_index(values, i + 3, params[2], relative_base)] = third_param
                i += 4
            elif op_code == 8:
                first_param = get_val(values, i + 1, params[0], relative_base)
                second_param = get_val(values, i + 2, params[1], relative_base)
                if first_param == second_param:
                    third_param = 1
                else:
                    third_param = 0
                values[get_index(values, i + 3, params[2], relative_base)] = third_param
                i += 4
            elif op_code == 9:
                relative_base += get_val(values, i + 1, params[0], relative_base)
                i += 2
            elif op_code == 99:
                break
        except IndexError:
            values.append([0] * len(values))

    return values


# lol
#for j in range(2):
#    calc(j + 1)

from adventOfCode2019.IntCodeComputer import *
print(IntCodeMachine(_input=[1]).calc())
