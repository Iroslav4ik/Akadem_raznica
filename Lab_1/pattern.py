def draw_pattern():

    for row in range(2):
        line = ""
        for col in range(192):

            if row % 2 == 0:

                if col % 6 < 5:
                    line += "█"
                else:
                    line += " "

            else:

                if col < 3:
                    line += " "
                elif (col - 3) % 6 < 5:
                    line += "█"
                else:
                    line += " "
        print(line)

if __name__ == "__main__":
    draw_pattern()