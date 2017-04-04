import csv
import sys


def main():
    '''
        csvtoconfluence converts a csv file to markup for confluence
        usage: python
    '''
    inputfile = sys.argv[1]
    outputname = inputfile.replace('.csv', '.txt')

    # assumes first line is header
    firstrow = True
    with open(outputname, 'wb') as fileout:
        with open(inputfile, 'rU') as infile:
            readfile = csv.reader(infile)
            for row in readfile:
                if firstrow:
                    firstrow = False
                    for item in row:
                        fileout.write('||{0}'.format(item))
                    fileout.write('||')
                else:
                    for item in row:
                        if item == '':
                            # use blank space to avoid header style formating
                            fileout.write('|{0: <1}'.format(item))
                        else:
                            fileout.write('|{0}'.format(item))
                    fileout.write('|')
                fileout.write('\n')
    fileout.close()
    infile.close()


if __name__ == '__main__':
    main()
