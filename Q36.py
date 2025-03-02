
import doctest
import math

def isValidSudoku(board):
    """
    FINISHED: May 22, 2024
    
    Runtime O(1)
    Iterates through the 81 squares of a sudoku, tracking numbers into the
    9 possible columns, rows, and squares. If a matching number is found in
    any column, row, or square, returns False, else if the whole puzzle is
    searched, returns True.
    
    >>> board_1 = [
    ...     ["5","3",".",".","7",".",".",".","."],
    ...     ["6",".",".","1","9","5",".",".","."],
    ...     [".","9","8",".",".",".",".","6","."],
    ...     ["8",".",".",".","6",".",".",".","3"],
    ...     ["4",".",".","8",".","3",".",".","1"],
    ...     ["7",".",".",".","2",".",".",".","6"],
    ...     [".","6",".",".",".",".","2","8","."],
    ...     [".",".",".","4","1","9",".",".","5"],
    ...     [".",".",".",".","8",".",".","7","9"]
    ... ]
    >>> print(isValidSudoku(board_1))
    True
    >>> board_2 = [
    ...     ["8","3",".",".","7",".",".",".","."],
    ...     ["6",".",".","1","9","5",".",".","."],
    ...     [".","9","8",".",".",".",".","6","."],
    ...     ["8",".",".",".","6",".",".",".","3"],
    ...     ["4",".",".","8",".","3",".",".","1"],
    ...     ["7",".",".",".","2",".",".",".","6"],
    ...     [".","6",".",".",".",".","2","8","."],
    ...     [".",".",".","4","1","9",".",".","5"],
    ...     [".",".",".",".","8",".",".","7","9"]
    ... ]
    >>> print(isValidSudoku(board_2))
    False
    >>> board_3 = [
    ...	    [".","8","7","6","5","4","3","2","1"],
    ...	    ["2",".",".",".",".",".",".",".","."],
    ...	    ["3",".",".",".",".",".",".",".","."],
    ...	    ["4",".",".",".",".",".",".",".","."],
    ...	    ["5",".",".",".",".",".",".",".","."],
    ...	    ["6",".",".",".",".",".",".",".","."],
    ...	    ["7",".",".",".",".",".",".",".","."],
    ...	    ["8",".",".",".",".",".",".",".","."],
    ...	    ["9",".",".",".",".",".",".",".","."]
    ... ]
    >>> print(isValidSudoku(board_3))
    True
    """
    # Data is preserved in 3 groupings, each with 9 categories.
    row_data = [None]*81
    col_data = [None]*81
    squ_data = [None]*81
    
    row_num = 0
    while row_num < 9:
        col_num = 0
        while col_num < 9:
            cel_num = board[row_num][col_num]
            if cel_num.isnumeric():
                keep_looking = boardTracker (row_num, col_num, 
                                                  int(cel_num), row_data, 
                                                  col_data, squ_data)
                if not keep_looking:
                    return False
            col_num += 1
        row_num += 1
    return True

def boardTracker (row_num, col_num, cel_num, row_data, col_data, squ_data):
    """
    Helper function. When a number is found, this method will track the
    position of the number, and will check for conflicts. If a conflict is
    found, it returns False to 'isValidSudoku', leading to an overall False
    return.
    
    row_num, col_num: position values for the new number
    cel_num: the number which is actually in the cell
    """
    cel_num -= 1    # 0-based indexing, subtract "1"
    # First handle row information
    row_position = (row_num * 9) + cel_num
    if row_data[row_position] == None:
        row_data[row_position] = 1
    else:
        return False
    # Next handle columns
    col_position = (col_num * 9) + cel_num
    if col_data[col_position] == None:
        col_data[col_position] = 1
    else:
        return False
    # Lastly handle square information; top left -> 0, bot right -> 8
    squ_num = 0
    squ_num += (math.floor(col_num / 3)) # Adds 0, 1, or 2    
    squ_num += (math.floor(row_num / 3) * 3) # Adds 0, 3, or 6
    squ_position = (squ_num * 9) + cel_num
    if squ_data[squ_position] == None:
        squ_data[squ_position] = 1
    else:
        return False
    # If no 'False' returns, then keep searching
    return True

doctest.testmod()