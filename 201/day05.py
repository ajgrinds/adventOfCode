import csv


def parse_code(code):
    op_code = code % 100
    params = []
    num_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}
    code //= 10
    for i in range(num_params[op_code]):
        code //= 10
        if code % 10 == 1:
            params.append(1)
        else:
            params.append(0)
    return op_code, params


def calc(system_id):
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        values = list(reader)[0]

    values = [int(value) for value in values]
    i = 0
    while i < len(values):
        op_code, params = parse_code(values[i])
        if op_code == 1:
            if params[0] == 0:
                first_param = values[values[i + 1]]
            else:
                first_param = values[i + 1]
            if params[1] == 0:
                second_param = values[values[i + 2]]
            else:
                second_param = values[i + 2]
            if params[2] == 0:
                values[values[i + 3]] = first_param + second_param
            else:
                values[i + 3] = first_param + second_param
            i += 4
        elif op_code == 2:
            if params[0] == 0:
                first_param = values[values[i + 1]]
            else:
                first_param = values[i + 1]
            if params[1] == 0:
                second_param = values[values[i + 2]]
            else:
                second_param = values[i + 2]
            if params[2] == 0:
                values[values[i + 3]] = first_param * second_param
            else:
                values[i + 3] = first_param * second_param
            i += 4
        elif op_code == 3:
            if params[0] == 0:
                values[values[i + 1]] = system_id
            else:
                values[i + 1] = system_id
            i += 2
        elif op_code == 4:
            if params[0] == 0:
                print(values[values[i + 1]])
            else:
                print(values[i + 1])
            i += 2
        elif op_code == 5:
            if params[0] == 0:
                if values[values[i + 1]] != 0:
                    if params[1] == 0:
                        i = values[values[i + 2]]
                    else:
                        i = values[i + 2]
                else:
                    i += 3
            else:
                if values[i + 1] != 0:
                    if params[1] == 0:
                        i = values[values[i + 2]]
                    else:
                        i = values[i + 2]
                else:
                    i += 3
        elif op_code == 6:
            if params[0] == 0:
                if values[values[i + 1]] == 0:
                    if params[1] == 0:
                        i = values[values[i + 2]]
                    else:
                        i = values[i + 2]
                else:
                    i += 3
            else:
                if values[i + 1] == 0:
                    if params[1] == 0:
                        i = values[values[i + 2]]
                    else:
                        i = values[i + 2]
                else:
                    i += 3
        elif op_code == 7:
            if params[0] == 0:
                first_param = values[values[i + 1]]
            else:
                first_param = values[i + 1]
            if params[1] == 0:
                second_param = values[values[i + 2]]
            else:
                second_param = values[i + 2]
            if first_param < second_param:
                third_param = 1
            else:
                third_param = 0
            if params[2] == 0:
                values[values[i + 3]] = third_param
            else:
                values[i + 3] = third_param
            i += 4
        elif op_code == 8:
            if params[0] == 0:
                first_param = values[values[i + 1]]
            else:
                first_param = values[i + 1]
            if params[1] == 0:
                second_param = values[values[i + 2]]
            else:
                second_param = values[i + 2]
            if first_param == second_param:
                third_param = 1
            else:
                third_param = 0
            if params[2] == 0:
                values[values[i + 3]] = third_param
            else:
                values[i + 3] = third_param
            i += 4
        elif op_code == 99:
            break

    return values


# part 1
calc(1)

# part 2
calc(5)
