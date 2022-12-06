
import os
import queue

q = queue.Queue(maxsize=3) # queue of max_ids
class queue_of_three:
    xs = []
    def __init__(self):
        self.xs = []
    def put(self, x):
        if len(self.xs) == 3:
            self.xs[0] = self.xs[1]
            self.xs[1] = self.xs[2]
            self.xs[2] = x
        else:
            self.xs.append(x)
    def get(self):
        return self.xs

NL = os.linesep # new line characters.
nl_len = len(NL) # length of NL characters.
s = 0 # sum.
m = 0 # max.
i = 1 # elf ID.

# replaced by queue.
q_max = queue_of_three()
q_ids = queue_of_three()

with open("input.txt") as myfile:
    for line in myfile:
        # end the current addition.
        if line == NL:
            # look whether the current sum is a new max.
            if s > m:
                m = s

                # replaced by queue.
                q_max.put(m)
                q_ids.put(i)

            s = 0 # resset the current sum.
            i = i + 1 # increment elf ID.
            continue
        # remove NL from end, convert string to number, add to current sum.
        num_str = line[:-nl_len]
        num_int = int(num_str)
        s = s + num_int

max_ids   = q_ids.get()
max_cals  = q_max.get()
total_cal = sum(max_cals)
print(f"Elves with most calories are #{max_ids}, they have {total_cal} callories ({max_cals}).")

