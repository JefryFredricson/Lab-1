from time import sleep
def generate_pattern(n):
    for i in range(n):
        print("\033[0m" + ' ' * i + "\033[47m" + ' ' + "\033[0m" ' ' * (2 * (n - i - 1)) + "\033[47m" + ' ' + "\033[0m" + ' ' * i, end = '')
        print("\033[0m" + ' ' * i + "\033[47m" + ' ' + "\033[0m" ' ' * (2 * (n - i - 1)) + "\033[47m" + ' ' + "\033[0m" + ' ' * i)
    for i in range(n):
        print("\033[0m" + ' ' * (n - i - 1) + "\033[47m" + ' ' + "\033[0m" + ' ' * (2 * i) + "\033[47m" ' ' + "\033[0m" + ' ' * (n - i - 1), end = '')
        print("\033[0m" + ' ' * (n - i - 1) + "\033[47m" + ' ' + "\033[0m" + ' ' * (2 * i) + "\033[47m" ' ' + "\033[0m" + ' ' * (n - i - 1))
while True:
    sleep(0.5)
    generate_pattern(4)