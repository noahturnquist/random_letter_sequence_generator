import random

#Generate a random sequence of 4 letters made up of ACTG
#5 per line
#For 15 Lines

#Letters
avl_letters = ["A", "C", "T", "G"]

#Generate the sequence
def gen_sequence(rows, cols, length, letters):
    pairs = []
    for pair in range(rows * cols):
        temp_lst = []
        for let in range(length):
            ind = random.randint(0,3)
            temp_lst.append(letters[ind])
        temp_str = "{zero}{one}{two}{three}".format(zero = temp_lst[0], one = temp_lst[1], two = temp_lst[2], three = temp_lst[3])
        print (temp_str)
        pairs.append(temp_str)
    return pairs

#Format for output
def read_gen_sequence(sequence, rows, col):
    ind = 0
    for pair in range(rows):
        temp_seq = "{one} {two} {three} {four} {five}".format(one = sequence[ind], two = sequence[ind + 1], three = sequence[ind + 2], four = sequence[ind + 3], five = sequence[ind + 4])
        print (temp_seq)
        ind += 5

#Specify # of rows and columns
row = 13
col = 5

sequence1 = gen_sequence(row, col, 4, avl_letters)
print (sequence1)
read_gen_sequence(sequence1, row, col)