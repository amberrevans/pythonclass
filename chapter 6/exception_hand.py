#Amber Evans
#10-12-2020
#ex 6-9
#This program adds exception handling

def  main():
    total =0
    rnums = 0
    #Open the file for reading
    try:
        infile=opent(r'c:\data\rnums.dat','r')
    except IOError:
        print ('File does not exist')
    else:
        print ('Here is the numbers')
        rnum= infile.realine()
        while rnum!='':
            try:
                rnum= int(rnum)
            except ValueError:
                rnum= rnum.rstrip('\n')
                print ('rnum+'is not valid')
                break
            else:
                print (rnum)
                total +=rnum
                rnums\+=1
                rnum=infile.readline()
            #print (linenum+':'+rnum)
            infile.close()
            ave= total/rnum
            print (f'The average is {ave:.2f}')

main()
