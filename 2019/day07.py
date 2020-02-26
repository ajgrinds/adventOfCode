import csv
import itertools
import copy


with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    array = list(reader)[0]

array = [int(value) for value in array]


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


def calc(current_state, _input):
    i = current_state[1]
    values = current_state[0]
    _output = []
    while i < len(values):
        op_code, params = parse_code(values[i])
        if op_code == 1:
            first_param = values[values[i + 1]] if params[0] == 0 else values[i + 1]
            second_param = values[values[i + 2]] if params[1] == 0 else values[i + 2]
            if params[2] == 0:
                values[values[i + 3]] = first_param + second_param
            else:
                values[i + 3] = first_param + second_param
            i += 4
        elif op_code == 2:
            first_param = values[values[i + 1]] if params[0] == 0 else values[i + 1]
            second_param = values[values[i + 2]] if params[1] == 0 else values[i + 2]
            if params[2] == 0:
                values[values[i + 3]] = first_param * second_param
            else:
                values[i + 3] = first_param * second_param
            i += 4
        elif op_code == 3:
            if not _input:
                return (values, i), _output
            if params[0] == 0:
                values[values[i + 1]] = _input[0]
                _input.pop(0)
            else:
                values[i + 1] = _input[0]
                _input.pop(0)
            i += 2
        elif op_code == 4:
            if params[0] == 0:
                _output.append(values[values[i + 1]])
            else:
                _output.append(values[i + 1])
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
            first_param = values[values[i + 1]] if params[0] == 0 else values[i + 1]
            second_param = values[values[i + 2]] if params[1] == 0 else values[i + 2]
            third_param = 1 if first_param < second_param else 0
            if params[2] == 0:
                values[values[i + 3]] = third_param
            else:
                values[i + 3] = third_param
            i += 4
        elif op_code == 8:
            first_param = values[values[i + 1]] if params[0] == 0 else values[i + 1]
            second_param = values[values[i + 2]] if params[1] == 0 else values[i + 2]
            third_param = 1 if first_param == second_param else 0
            if params[2] == 0:
                values[values[i + 3]] = third_param
            else:
                values[i + 3] = third_param
            i += 4
        elif op_code == 99:
            return "done", _output


part_1 = []

for x in list(itertools.permutations([0, 1, 2, 3, 4])):
    current_input = [[a] for a in x]
    last_output = [0]
    for j in range(5):
        current_input[j].extend(last_output)
        last_output = calc([copy.deepcopy(array), 0], current_input[j])[1]
    part_1.extend(last_output)

print(max(part_1))


part_2 = []
for x in list(itertools.permutations([5, 6, 7, 8, 9])):
    current_states = [(array, 0) for i in range(5)]
    current_input = [[a] if x.index(a) != 0 else [a, 0] for a in x]
    j = 0
    while current_states[j] != "done":
        current_states[j], output = calc(copy.deepcopy(current_states[j]), current_input[j])
        if j == 4:
            current_input[0].extend(output)
            j = 0
        else:
            j += 1
            current_input[j].extend(output)
    part_2.extend(current_input[j])

print(max(part_2))

