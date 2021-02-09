def horizontal_check(board):
    '''
    the function checks if there
    are identical numbers on the horizontals
    >>> horizontal_check(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ","46  83  *","3      **","  8  2***","  2  ****"])
    True
    '''
    for line in board:
        check_set = set()
        for elem in line:
            if elem != '*':
                if elem in check_set:
                    return False
                if elem != ' ':
                    check_set.add(elem)
    return True

def vertical_trans(board):
    '''
    inverts the table by 90 degrees
    ie the verticals are thus converted
    to horizontal for further verification
    >>> vertical_trans(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ","46  83  *","3      **","  8  2***","  2  ****"])
    ['**** 43  ', '***  6   ', '** 4   82', '*1       ', '  31 8   ', '****93 2*', '****   **', '****5 ***', '**** ****']
    '''
    index = 0
    new_str = ''
    new_brd = []
    while index != len(board):
        for line in board:
            new_str += line[index]
        new_brd.append(new_str)
        new_str = ''
        index += 1
    return new_brd

def block(board):
    '''
    creates a table with the corresponding blocks for further verification
    >>> block(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ","46  83  *","3      **","  8  2***","  2  ****"])
    [' 43   2  ', '  6  8  2', ' 4       ', '1    83  ', '  31 9 5 ']
    '''
    new_board = []
    side_len = len(board)
    sc_board = vertical_trans(board)[0:side_len-4]
    board = board[4:]

    start = side_len - 5
    end = side_len
    start_1 = 1
    end_1 = 5

    for line,line_1 in zip(sc_board,reversed(board)):
        y_line = line[start:end]
        x_line = line_1[start_1:end_1]
        start,end = start - 1,end - 1
        start_1,end_1 = start_1 + 1,end_1 + 1
        new_board.append(y_line + x_line)
    return new_board
