player1 = "X"
player2 = "O"
empty_space1 = " "
empty_space2 = "_"
cell1 = "1 1"
cell2 = "1 2"
cell3 = "1 3"
cell4 = "2 1"
cell5 = "2 2"
cell6 = "2 3"
cell7 = "3 1"
cell8 = "3 2"
cell9 = "3 3"
legal_cells = cell1 or cell2 or cell3 or cell4 or cell5 or cell6 or cell7 or cell8 or cell9
cells_row1 = [cell1, cell2, cell3]
cells_row2 = [cell4, cell5, cell6]
cells_row3 = [cell7, cell8, cell9]
teo = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
first_input = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("---------")
print("|", first_input[0], first_input[1], first_input[2], "|")
print("|", first_input[3], first_input[4], first_input[5], "|")
print("|", first_input[6], first_input[7], first_input[8], "|")
print("---------")


def x_moves():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    cells = input("Enter the coordinates: ")
    cells = list(cells)
    cells_check = any(item in cells for item in alphabet)
    while cells_check:
        print("You should enter numbers!")
        cells = input("Enter the coordinates: ")
        cells = list(cells)
        cells_check = any(item in cells for item in alphabet)
    cells = list(cells)
    check1 = int(cells[0]) < 1 or int(cells[0]) > 3
    check2 = int(cells[2]) < 1 or int(cells[2]) > 3
    while check1 or check2:
        print("Coordinates should be from 1 to 3!")
        cells = input("Enter the coordinates: ")
        check1 = int(cells[0]) < 1 or int(cells[0]) > 3
        check2 = int(cells[2]) < 1 or int(cells[2]) > 3
    cells = "".join(cells)
    x = cells == teo[0]
    y = first_input[0] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[0]
        y = first_input[0] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[1]
    y = first_input[1] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[1]
        y = first_input[1] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[2]
    y = first_input[2] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[2]
        y = first_input[2] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[3]
    y = first_input[3] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[3]
        y = first_input[3] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[4]
    y = first_input[4] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[4]
        y = first_input[4] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[5]
    y = first_input[5] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[5]
        y = first_input[5] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[6]
    y = first_input[6] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[6]
        y = first_input[6] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[7]
    y = first_input[7] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[7]
        y = first_input[7] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[8]
    y = first_input[8] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[8]
        y = first_input[8] != " "
        if x and y:
            z = 1
        else:
            z = 0

    if cells == teo[0]:
        first_input[0] = "X"
    elif cells == teo[1]:
        first_input[1] = "X"
    elif cells == teo[2]:
        first_input[2] = "X"
    elif cells == teo[3]:
        first_input[3] = "X"
    elif cells == teo[4]:
        first_input[4] = "X"
    elif cells == teo[5]:
        first_input[5] = "X"
    elif cells == teo[6]:
        first_input[6] = "X"
    elif cells == teo[7]:
        first_input[7] = "X"
    elif cells == teo[8]:
        first_input[8] = "X"

    print("---------")
    print("|", first_input[0], first_input[1], first_input[2], "|")
    print("|", first_input[3], first_input[4], first_input[5], "|")
    print("|", first_input[6], first_input[7], first_input[8], "|")
    print("---------")


def o_moves():
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    cells = input("Enter the coordinates: ")
    cells = list(cells)
    cells_check = any(item in cells for item in alphabet)
    while cells_check:
        print("You should enter numbers!")
        cells = input("Enter the coordinates: ")
        cells = list(cells)
        cells_check = any(item in cells for item in alphabet)
    cells = list(cells)
    check1 = int(cells[0]) < 1 or int(cells[0]) > 3
    check2 = int(cells[2]) < 1 or int(cells[2]) > 3
    while check1 or check2:
        print("Coordinates should be from 1 to 3!")
        cells = input("Enter the coordinates: ")
        check1 = int(cells[0]) < 1 or int(cells[0]) > 3
        check2 = int(cells[2]) < 1 or int(cells[2]) > 3
    cells = "".join(cells)
    x = cells == teo[0]
    y = first_input[0] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[0]
        y = first_input[0] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[1]
    y = first_input[1] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[1]
        y = first_input[1] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[2]
    y = first_input[2] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[2]
        y = first_input[2] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[3]
    y = first_input[3] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[3]
        y = first_input[3] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[4]
    y = first_input[4] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[4]
        y = first_input[4] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[5]
    y = first_input[5] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[5]
        y = first_input[5] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[6]
    y = first_input[6] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[6]
        y = first_input[6] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[7]
    y = first_input[7] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[7]
        y = first_input[7] != " "
        if x and y:
            z = 1
        else:
            z = 0
    x = cells == teo[8]
    y = first_input[8] != " "
    if x and y:
        z = 1
    else:
        z = 0
    while z == 1:
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        x = cells == teo[8]
        y = first_input[8] != " "
        if x and y:
            z = 1
        else:
            z = 0

    if cells == teo[0]:
        first_input[0] = "O"
    elif cells == teo[1]:
        first_input[1] = "O"
    elif cells == teo[2]:
        first_input[2] = "O"
    elif cells == teo[3]:
        first_input[3] = "O"
    elif cells == teo[4]:
        first_input[4] = "O"
    elif cells == teo[5]:
        first_input[5] = "O"
    elif cells == teo[6]:
        first_input[6] = "O"
    elif cells == teo[7]:
        first_input[7] = "O"
    elif cells == teo[8]:
        first_input[8] = "O"

    print("---------")
    print("|", first_input[0], first_input[1], first_input[2], "|")
    print("|", first_input[3], first_input[4], first_input[5], "|")
    print("|", first_input[6], first_input[7], first_input[8], "|")
    print("---------")


row = [[first_input[0], first_input[1], first_input[2]], [first_input[3], first_input[4], first_input[5]],
       [first_input[6], first_input[7], first_input[8]]]
column = [[first_input[0], first_input[3], first_input[6]], [first_input[1], first_input[4], first_input[7]],
          [first_input[2], first_input[5], first_input[8]]]
diagonal = [[first_input[0], first_input[4], first_input[8]], [first_input[2], first_input[4], first_input[6]]]
count_x = first_input.count(player1)
count_o = first_input.count(player2)
if count_x == 0:
    count_x = 1
elif count_o == 0:
    count_o = 1
x_wins_row1 = player1 == row[0][0] == row[0][1] == row[0][2]
o_wins_row1 = player2 == row[0][0] == row[0][1] == row[0][2]
x_wins_row2 = player1 == row[1][0] == row[1][1] == row[1][2]
o_wins_row2 = player2 == row[1][0] == row[1][1] == row[1][2]
x_wins_row3 = player1 == row[2][0] == row[2][1] == row[2][2]
o_wins_row3 = player2 == row[2][0] == row[2][1] == row[2][2]

x_wins_diagonal1 = player1 == diagonal[0][0] == diagonal[0][1] == diagonal[0][2]
o_wins_diagonal1 = player2 == diagonal[0][0] == diagonal[0][1] == diagonal[0][2]
x_wins_diagonal2 = player1 == diagonal[1][0] == diagonal[1][1] == diagonal[1][2]
o_wins_diagonal2 = player2 == diagonal[1][0] == diagonal[1][1] == diagonal[1][2]

x_wins_column1 = player1 == column[0][0] == column[0][1] == column[0][2]
o_wins_column1 = player2 == column[0][0] == column[0][1] == column[0][2]
x_wins_column2 = player1 == column[1][0] == column[1][1] == column[1][2]
o_wins_column2 = player2 == column[1][0] == column[1][1] == column[1][2]
x_wins_column3 = player1 == column[2][0] == column[2][1] == column[2][2]
o_wins_column3 = player2 == column[2][0] == column[2][1] == column[2][2]

x_winnings = x_wins_row1 or x_wins_row2 or x_wins_row3 or x_wins_diagonal1 or x_wins_diagonal2 or x_wins_column1 \
             or x_wins_column2 or x_wins_column3
o_winnings = o_wins_row1 or o_wins_row2 or o_wins_row3 or o_wins_diagonal1 or o_wins_diagonal2 or o_wins_column1 \
             or o_wins_column2 or o_wins_column3
winnings = x_winnings or o_winnings
draw = not x_winnings and not o_winnings and empty_space1 not in first_input
while not winnings and not draw:
    x_moves()
    o_moves()
    x_moves()
    o_moves()
    x_moves()
    if x_winnings:
        print("X wins")
        break
    o_moves()
    if o_winnings:
        print("O wins")
        break
    x_moves()
    if x_winnings:
        print("X wins")
        break
    o_moves()
    if o_winnings:
        print("O wins")
        break
    x_moves()
    if x_winnings:
        print("X wins")
        break
    else:
        print("Draw")
        break
print("Game over")
