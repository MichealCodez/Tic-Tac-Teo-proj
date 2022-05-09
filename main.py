def board():
    print('---------')
    print(f'| {cells[0]} {cells[1]} {cells[2]} |\n'
          f'| {cells[3]} {cells[4]} {cells[5]} |\n'
          f'| {cells[6]} {cells[7]} {cells[8]} |')
    print('---------')


def win(player):
    winner = [''.join(row1) == player, ''.join(row2) == player, ''.join(row3) == player,
              ''.join(column1) == player, ''.join(column2) == player, ''.join(column3) == player,
              ''.join(diagonal[0]) == player, ''.join(diagonal[1]) == player]
    return winner


def coord(coordinate, p):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    coordinates = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
    j = any(x for x in coordinate if x in alphabet)

    if j:
        return enter_num
    elif coordinate in coordinates:
        a = coordinates.index(coordinate)
        cel = list(cells)
        if cel[a] not in emp:
            return cell_occupied
        else:
            cel[a] = p
            return ''.join(cel)
    elif coordinate not in coordinates:
        return ic


cells = "         "

cell_occupied = 'This cell is occupied! Choose another one!'
enter_num = 'You should enter numbers!'
outside_coordinate = 'Coordinates should be from 1 to 3!'
ic = 'Coordinates should be from 1 to 3!'
messages = [cell_occupied, enter_num, outside_coordinate, ic]
player1 = 'XXX'
player2 = 'OOO'
emp = [' ', '_']

row1 = [cells[0], cells[1], cells[2]]
row2 = [cells[3], cells[4], cells[5]]
row3 = [cells[6], cells[7], cells[8]]

column1 = [cells[0], cells[3], cells[6]]
column2 = [cells[1], cells[4], cells[7]]
column3 = [cells[2], cells[5], cells[8]]

diagonal = [[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]
board()
result = ''
play_list = ['O']
c = input('Enter the coordinates:')
while result not in ['X wins', 'O wins', 'Draw']:
    if play_list[-1] == 'O':
        play = 'X'
    else:
        play = 'O'
    play_list.append(play)
    cd = coord(c, play)
    while cd in messages:
        print(cd)
        c = input('Enter the coordinates:')
        cd = coord(c, play)
    cells = cd
    row1 = [cells[0], cells[1], cells[2]]
    row2 = [cells[3], cells[4], cells[5]]
    row3 = [cells[6], cells[7], cells[8]]

    column1 = [cells[0], cells[3], cells[6]]
    column2 = [cells[1], cells[4], cells[7]]
    column3 = [cells[2], cells[5], cells[8]]

    diagonal = [[cells[0], cells[4], cells[8]], [cells[2], cells[4], cells[6]]]
    board()

    if any(win(player1)):
        result = 'X wins'
        print(result)
        break
    elif any(win(player2)):
        result = 'O wins'
        print(result)
        break
    elif ' ' not in cells:
        result = 'Draw'
        print(result)
        break
    else:
        result = 'continue'
