
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
teo = input()

print("---------")
print("|", teo[0], teo[1], teo[2], "|")
print("|", teo[3], teo[4], teo[5], "|")
print("|", teo[6], teo[7], teo[8], "|")
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
    cells1 = int(cells[0])
    cells2 = int(cells[1])
    while (cells1 or cells2 < 1) or (cells1 or cells2 > 3):
        print("Coordinates should be from 1 to 3!")

    while cells != legal_cells:
        print("Coordinates should be from 1 to 3!")

row = [[teo[0], teo[1], teo[2]], [teo[3], teo[4], teo[5]], [teo[6], teo[7], teo[8]]]
column = [[teo[0], teo[3], teo[6]], [teo[1], teo[4], teo[7]], [teo[2], teo[5], teo[8]]]
diagonal = [[teo[0], teo[4], teo[8]], [teo[2], teo[4], teo[6]]]
empty_space1 = " "
empty_space2 = "_"
count_x = teo.count(player1)
count_o = teo.count(player2)

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
