with open('input.txt', 'r') as f:
    image = int(f.read())

width = 25
height = 6

pixels = []
while image != 0:
    pixels.insert(0, image % 10)
    image //= 10

layers = []
for i in range(0, len(pixels), width * height):
    layers.append(pixels[i:i + width * height])

zeros = []
for i in layers:
    zeros.append((i.count(0)))

# part 1
print(layers[zeros.index(min(zeros))].count(1) * layers[zeros.index(min(zeros))].count(2))

current_image = layers[0]
for layer in layers:
    for i, pix in enumerate(layer):
        if current_image[i] == 2 and pix != 2:
            current_image[i] = pix

answer = [[], [], [], [], []]
for i in range(0, len(current_image), width):
    for j in range(5):
        answer[j].append(current_image[i + j * 5:i + j * 5 + 5])


def process_letter(letter):
    processed = ""
    if letter[0].count(1) == 1:
        if letter[5].count(1) == 4:
            processed = 'L'
        else:
            processed = 'A'
    elif letter[0].count(1) == 2:
        if letter[5].count(1) == 1:
            processed = 'Y'
        elif letter[5].count(1) == 2:
            if letter[2].count(1) == 1:
                if letter[2][3] == 1:
                    processed = 'J'
                else:
                    processed = 'C'
            elif letter[3].count(1) == 2:
                if letter[3][3] == 1:
                    processed = 'U'
                else:
                    processed = 'K'
            else:
                processed = 'H'
        elif letter[5].count(1) == 3:
            processed = 'G'
    elif letter[0].count(1) == 3:
        if letter[5].count(1) == 1:
            processed = 'P'
        elif letter[5].count(1) == 2:
            processed = 'R'
        elif letter[5].count(1) == 3:
            processed = 'B'
    elif letter[0].count(1) == 4:
        if letter[5].count(1) == 4:
            if letter[2].count(1) == 3:
                processed = 'E'
            else:
                processed = 'Z'
        elif letter[5].count(1) == 1:
            processed = 'F'
    return processed


# part 2
print("".join([process_letter(x) for x in answer]))
