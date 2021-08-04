player1 = "X"
player2 = "O"
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
first_input = input()
first_input = first_input.replace("_", " ")
first_input = list(first_input)
print("---------")
print("|", first_input[0], first_input[1], first_input[2], "|")
print("|", first_input[3], first_input[4], first_input[5], "|")
print("|", first_input[6], first_input[7], first_input[8], "|")
print("---------")


def x_move():
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
    check_available_cell = (cells == teo[0]) or (cells == teo[1]) or (cells == teo[2]) or (cells == teo[3]) or \
                           (cells == teo[4]) or (cells == teo[5]) or (cells == teo[6]) or (cells == teo[7]) or \
                           (cells == teo[8])
    while check_available_cell == (player1 or player2):
        print("This cell is occupied! Choose another one!")
        cells = input("Enter the coordinates: ")
        check_available_cell = (cell1 == teo[0]) or (cell2 == teo[1]) or (cell3 == teo[2]) or (cell4 == teo[3]) or \
                               (cell5 == teo[4]) or (cell6 == teo[5]) or (cell7 == teo[6]) or (cell8 == teo[7]) or \
                               (cell9 == teo[8])
    if cells == teo[0]:
        teo[0] = "X"
    else:
        teo[0] = first_input[0]
    if cells == teo[1]:
        teo[1] = "X"
    else:
        teo[1] = first_input[1]
    if cells == teo[2]:
        teo[2] = "X"
    else:
        teo[2] = first_input[2]
    if cells == teo[3]:
        teo[3] = "X"
    else:
        teo[3] = first_input[3]
    if cells == teo[4]:
        teo[4] = "X"
    else:
        teo[4] = first_input[4]
    if cells == teo[5]:
        teo[5] = "X"
    else:
        teo[5] = first_input[5]
    if cells == teo[6]:
        teo[6] = "X"
    else:
        teo[6] = first_input[6]
    if cells == teo[7]:
        teo[7] = "X"
    else:
        teo[7] = first_input[7]
    if cells == teo[8]:
        teo[8] = "X"
    else:
        teo[8] = first_input[8]
    print("---------")
    print("|", teo[0], teo[1], teo[2], "|")
    print("|", teo[3], teo[4], teo[5], "|")
    print("|", teo[6], teo[7], teo[8], "|")
    print("---------")


x_move()
row = [[teo[0], teo[1], teo[2]], [teo[3], teo[4], teo[5]], [teo[6], teo[7], teo[8]]]
column = [[teo[0], teo[3], teo[6]], [teo[1], teo[4], teo[7]], [teo[2], teo[5], teo[8]]]
diagonal = [[teo[0], teo[4], teo[8]], [teo[2], teo[4], teo[6]]]
empty_space1 = " "
empty_space2 = "_"
count_x = teo.count(player1)
count_o = teo.count(player2)
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
if x_winnings and o_winnings:
    print("Impossible")
elif count_x > count_o and count_x % count_o != 1:
    print("Impossible")
elif count_o > count_x and count_o % count_x != 1:
    print("Impossible")
elif x_winnings:
    print("X wins")
elif o_winnings:
    print("O wins")
elif empty_space1 in teo or empty_space2 in teo:
    print("Game not finished")
elif not x_winnings and not o_winnings and empty_space1 not in teo or empty_space2 not in teo:
    print("Draw")

else:
    print("Impossible")
