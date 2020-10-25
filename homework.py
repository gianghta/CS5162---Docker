import pathlib
import socket
import sys

from os import listdir, path

# Initial set up for path and files
mypath = pathlib.Path(__file__).parent.absolute()
output_path = path.abspath("/home/output")


all_files = listdir(mypath)
txt_files = filter(lambda x: x[-4:] == '.txt', all_files)

# Redirect stdout to result file
orig_stdout = sys.stdout
final_file = open(f'{output_path}/result.txt', 'w')
sys.stdout = final_file 

# Keep track of all the count of words in texfile
txt_num_word = {}
largest_file = ''
max_word = 0
total_num_word = 0

print(f'Everything\'s that\'s currently in {mypath}: ')
for f in all_files:
    print(f'- {f}')

for f in txt_files:
    current_file = open(f, "rt")
    data = current_file.read()
    words = data.split()
    curr_words = len(words)

    total_num_word += curr_words
    txt_num_word[f] = curr_words


    if max_word < curr_words:
        largest_file = f
        max_word = curr_words

for idx, val in txt_num_word.items():
    print(f'{idx} number of words is: {val} words')

print(f'And the total number of words in all files is: {total_num_word}')
print(f'With the largest file is {largest_file} with {max_word} words')
print()

hostname = socket.gethostname()
ip_address = socket.gethostbyname('')
print(f'Current IP Address is of {hostname}: {ip_address}')


# End writing progress
sys.stdout = orig_stdout
final_file.close()

# Print out final result
with open(f'{output_path}/result.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')