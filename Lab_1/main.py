import flag
import pattern
import graph
import diagram


def main():
    print("_" * 100 + "\n1. Флаг Польши:\n")
    flag.draw_polish_flag()

    print("\n" + "_" * 100 + "\n2. Повторяющийся узор (вариант d):\n")
    pattern.draw_pattern()

    print("\n" + "_" * 100 + "\n3. График функции y=x^0.5:\n")
    graph.draw_graph()

    print("\n" + "_" * 100 + "\n4. Диаграмма средних:\n")
    p1, p2 = diagram.calculate_averages()
    diagram.draw_diagram(p1, p2)


if __name__ == "__main__":
    main()