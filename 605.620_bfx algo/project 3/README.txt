Programming Assignment 3: Longest Common Substring
Richard Ren - December 8, 2020

This program is a dynamic programming implementation of the longest common substring problem. It is written in Python 3.8.

There are 4 modules to this program: computeLCS.py, displayLCS.py, getInput.py, and main.py as the driver to execute the program. (There is an additional rngSequence.py included, independent of the main program, for the purposes of generating inputs for input testing.) The standard libraries imported include: numpy, math, time, textwrap, os.path, and re. 

This program expects input files in text format, in the same working directory as the program. The input file contains, in each line, a name and a sequence, separated by an equal sign "=". For example, a 13-base sequence named "recA" is defined as below:

recA = ACTGTGCACCTGA

To execute the program, execute main.py in the terminal. Program will first prompt an input for computation mode:

    Mode 1 - "required input comparison": this mode expects 1 input file (required file), and the program will compute LCS between each of the sequences with each other.
    Mode 2 - "required/testing comparison": this mode expects 2 input files (required + testing files), and the program will compute LCS between each of the sequences in the required file and each of the ones in the testing file.

After user inputs computation mode, program will then prompt for the testing file names.

If input testing passes for both computation mode and filename user inputs, the program will compute and construct LCS, and output the result in a separate file in the working directory, named after the input filenames with an "_output" suffix. 

If input testing fails, program will either output an error message and skip the current sequence, or output a warning message and compute anyway. Program will not terminate unexpectedly.

This program is written for Programming Assignment 3 for course 605.620, Professor Chlan.
