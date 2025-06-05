import math


def draw_graph():
    height = 9
    width = 20

    x_max = (height - 1) ** 2

    for y_level in range(height - 1, -1, -1):
        x_val = y_level ** 2

        pos = int(x_val * (width - 1) / x_max)

        line = [' '] * width
        line[pos] = '*'
        print(''.join(line))


if __name__ == "__main__":
    draw_graph()