import os
#import csv

def pwd():              # use pwd as linux has instead of cwd
    return os.getcwd()  # returns the current working directory like linux PWD command

def read_files():
    print(f'the current working directory: {pwd()}')
    i = 1
    for files in os.listdir(pwd()):
        print(f'{i})', files)
        i += 1

def run():
    print('Processing File...')
    read_files()
    read_line_by_line()
    read_entire_file()
    read_partial_data()

# Reading file from the current directory. Line by line, partial, full file.
# Function that reads entire file from a directory
def read_entire_file():
    # open function ensures a file is closed automatically
    with open("Data.txt") as f:
        # Read the entire content of a file
        data = f.read()
        return data

# Define a Function that reads a file line by line
def read_line_by_line():
    with open("Data.txt") as f:
        print('Read lines one by one')
        line = f.readline().strip()
        while line:
            print(line)
            line = f.readline()
            print('-' * 30)

# Define function that reads specific character
def read_partial_data(num_chars=3):
    with open('Data.txt') as f:
        # Read specified number of characters
        partial_data = f.read(num_chars)
        print(f'Reading the first {num_chars} chars')


if __name__ == '__main__':
    run()


