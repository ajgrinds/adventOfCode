def load_csv():
    import csv
    with open('input.csv', 'r') as f:
        return list(map(lambda x: int(x), list(csv.reader(f))[0]))


class NeedInputError(Exception):
    pass


class MachineState:
    def __init__(self, stack: list, pointer: int = 0, relative_base: int = 0):
        self.stack = stack
        self.pointer = pointer
        self.relative_base = relative_base

    @property
    def value(self):
        return self.stack[self.pointer]

    @value.setter
    def value(self, val):
        self.stack[self.pointer] = val

    def move_pointer(self, val=1):
        if len(self.stack) < self.pointer - 1:
            self.stack.append([0] * (self.pointer-len(self.stack)))
        self.pointer += val
        return self.pointer


class IntCodeMachine:
    def __init__(self, _input: list = None, current_state: MachineState = None):
        if current_state is None:
            self.current_state = MachineState(stack=load_csv())
        else:
            self.current_state = current_state
        if _input is None:
            self.input = []
        else:
            self.input = list(map(int, _input))
        self.output = []
        self.running = False

    def get_val(self, mode):
        return self.current_state.stack[self.get_index(mode=mode)]

    def get_index(self, mode):
        index = 0
        if mode == 0:
            index = self.current_state.value
        elif mode == 1:
            index = self.current_state.pointer
        elif mode == 2:
            index = self.current_state.value + self.current_state.relative_base
        while index > len(self.current_state.stack) - 1:
            self.current_state.stack.extend([0] * len(self.current_state.stack))
        self.current_state.move_pointer()
        return index

    def parse_code(self):
        code = self.current_state.value
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
        self.current_state.move_pointer()
        return op_code, params

    def process_code(self):
        op_code, params = self.parse_code()
        if op_code == 1:
            self.current_state.stack[self.get_index(mode=params[2])] = self.get_val(mode=params[0]) + self.get_val(
                mode=params[1])
        elif op_code == 2:
            self.current_state.stack[self.get_index(mode=params[2])] = self.get_val(mode=params[0]) * self.get_val(
                mode=params[1])
        elif op_code == 3:
            if not self.input:
                self.current_state.move_pointer(-1)
                raise NeedInputError
            self.current_state.stack[self.get_index(mode=params[0])] = self.input.pop(0)
        elif op_code == 4:
            self.output.append(self.get_val(mode=params[0]))
        elif op_code == 5:
            if self.current_state.stack[self.get_index(mode=params[0])] != 0:
                self.current_state.pointer = self.get_val(mode=params[1])
            else:
                self.current_state.move_pointer()
        elif op_code == 6:
            if self.current_state.stack[self.get_index(mode=params[0])] == 0:
                self.current_state.pointer = self.get_val(mode=params[1])
            else:
                self.current_state.move_pointer()
        elif op_code == 7:
            self.current_state.stack[self.get_index(mode=params[2])] = 1 if self.get_val(mode=params[0]) < self.get_val(mode=params[1]) else 0
        elif op_code == 8:
            self.current_state.stack[self.get_index(mode=params[2])] = 1 if self.get_val(mode=params[0]) == self.get_val(mode=params[1]) else 0
        elif op_code == 9:
            self.current_state.relative_base += self.get_val(mode=params[0])
        elif op_code == 99:
            self.running = False
            return 99

    def calc(self):
        self.running = True
        try:
            while self.running:
                self.process_code()
            temp = self.output
            self.output = []
            return True, temp
        except NeedInputError:
            temp = self.output
            self.output = []
            return False, temp

    def send_input(self, _input):
        try:
            self.input.extend(_input)
        except TypeError:
            self.input.append(_input)
