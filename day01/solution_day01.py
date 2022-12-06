
import os

NL = os.linesep # new line characters.
nl_len = len(NL) # length of NL characters.
s = 0 # sum.
m = 0 # max.
i = 1 # elf ID.
max_id = 0 # elf ID associated with the max.
with open("input_day01.txt") as myfile:
    for line in myfile:
        # end the current addition.
        if line == NL:
            # look whether the current sum is a new max.
            if s > m:
                m = s
                max_id = i
            s = 0 # resset the current sum.
            i = i + 1 # increment elf ID.
            continue
        # remove NL from end, convert string to number, add to current sum.
        num_str = line[:-nl_len]
        num_int = int(num_str)
        s = s + num_int

print(f"Elf #{max_id} has {m} callories")

