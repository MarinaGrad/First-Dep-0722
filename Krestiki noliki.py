field = [[" "] * 3 for i in range(3)]

def show():
   print()
   print(f" 0 1 2")
   for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        x,y = map(int, input("     Ваш ход: ").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':
                return x,y
            else:
                print("Клетка занята! ")
        else:
            print("Координаты вне диапазона! ")

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["x", "x", "x"]:
            return True
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["x", "x", "x"]:
            return True

        symbols = []
        for i in range(3):
            symbols.append(field[i][i])
        if symbols == ["x", "x", "x"]:
            return True

        symbols = []
        for i in range(3):
            symbols.append(field[i][2-i])
        if symbols == ["x", "x", "x"]:
            return True

    return False

num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x,y = ask()

    if num % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "0"

    if check_win():

    if num == 9:
        print("Ничья")
        break

    break

