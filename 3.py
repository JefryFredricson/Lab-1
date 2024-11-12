import math

def plot_function():
    height = 9
    width = 20
    for y in range(height, -1, -1):
        line = "\033[0m" + ""
        for x in range(width + 1):
            if y == math.ceil(2 * x / width * height):
                line += "\033[47m" + " "
            else:
                line += "\033[0m" + " "
        print(line)

plot_function()