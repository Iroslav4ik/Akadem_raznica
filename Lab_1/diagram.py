def calculate_averages():
    with open("sequence.txt", "r") as f:
        numbers = [float(line.strip()) for line in f.readlines()]

    first_half = [abs(x) for x in numbers[:125]]
    second_half = [abs(x) for x in numbers[125:]]

    avg1 = sum(first_half) / len(first_half)
    avg2 = sum(second_half) / len(second_half)
    total = avg1 + avg2

    perc1 = int(avg1 / total * 100)
    perc2 = 100 - perc1

    return perc1, perc2


def draw_diagram(perc1, perc2):
    print(f"Первые 125: {'=' * perc1} {perc1}%")
    print(f"Вторые 125: {'=' * perc2} {perc2}%")


if __name__ == "__main__":
    p1, p2 = calculate_averages()
    draw_diagram(p1, p2)