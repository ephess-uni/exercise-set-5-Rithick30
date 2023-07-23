""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser=ArgumentParser(description='ex_5_3')
    parser.add_argument('infile',help='input file')
    parser.add_argument('outfile',help='output file')
    args=parser.parse_args()

    l1 = np.loadtxt(args.infile)

    # TODO: remove the mean from l1
    l1-=l1.mean()
    y=l1.std()
    processed=l1/y
    # TODO: scale l1 so that it has a standard devitation
    # of 1.
    #
    # SAVE the processed data to a variable called `processed`


    # Here the program saves the processed data to the outfile
    np.savetxt(args.outfile, processed, fmt='%.2e')
