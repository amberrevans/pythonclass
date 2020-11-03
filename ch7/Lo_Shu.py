#Amber Evans
#11-1-2020
#Lo Shu magic square

#This program determines if a 2D list is a Lo Shu Magic Square
#Each row, column, and diagonal must equal 15

#Define constants
ROWS, COLS = (3,3)

#Define the main function 
def main():
    #Initialize the square as 2D list
    vals = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    #populate the square
    get_square(vals)
    print ()

    #Display the square
    print ('Here is your square. Now we will determine if its Magic!')
    for row in range (ROWS):
        for col in range (COLS):
            print (vals[row][col], end ='')
        print ()

    #rnum and cnum are teh number of rows and columns that totaled 15
    #dnum is the number of diagonals that total 15
    rnum = calc_rows(vals)
    cnum = calc_cols(vals)
    dnum = calc_diags(vals)

    #If we have 8 total then we have a Lo Shu Square
    if rnum + cnum + dnum ==8:
        print ('Yep, you have a Lo Shu Magic Square')
    else:
        print ('Nope, you do not have a Magic Square')
def calc_rows(vals):
    #Calculate row totals
    numrows = 0
    for row in range (ROWS):
        rtotal = 0
        for col in range (COLS):
            rtotal += vals [row][col]
        print ('Row',row +1,'total is',rtotal)
        if rtotal ==15:
            numrows +=1
    return numrows

def calc_cols(vals):
    #Calculate column totals
    numcols = 0
    for col in range (COLS):
        ctotal = 0
        for row in range (ROWS):
            ctotal +=vals [row][col]
        print ('Column',col+1,'total is', ctotal)
        if ctotal ==15:
            numcols+=1
    return numcols

def calc_diags (vals):
    numdiags = 0
    #calculate the diagonals
    ldiag = vals[0][0] + vals [1][1] + vals [2][2]
    rdiag = vals[0][2] + vals [1][1] +vals [2][0]
    print ('Left diagonal is', ldiag)
    print ('Right diagonal is', rdiag)

    if rdiag ==15:
        numdiags+=1
    if ldiag ==15:
        numdiags+=1
    return numdiags

def get_square (vals):
    row =0
    while row <3:
        for col in range (COLS):
            print ('Enter a number for row',row,'column','',end='')
            vals[row][col] = int(input())
        row+=1
    return vals
#Call the main function
main()
