import clients.asm2205.st16.main



MENU = [
    ["[2205-16] Матвеев 2205", clients.asm2205.st16.main.main],

]


def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


try:
    while True:
        sorted(MENU)[menu()][1]()
except Exception as ex:
    print(ex, "\nbye")
