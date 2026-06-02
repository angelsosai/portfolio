# Write an API that generates fancy sequences using the append, addAll, and multAll operations.

# Implement the Fancy class:

# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.


import numpy as np

class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.sec = np.array([])

    def append(self, val: int) -> None:
        self.sec = np.append(self.sec, val % self.MOD )

    def addAll(self, inc: int) -> None:
        self.sec = self.sec+(inc % self.MOD)
        # print(self.sec)
        


    def multAll(self, m: int) -> None:
        self.sec=self.sec * (m% self.MOD)
        self.sec=self.sec % self.MOD

    def getIndex(self, idx: int) -> int:
        # print(self.sec)
        try:
            # print(self.sec[idx])
            return int(self.sec[idx] % self.MOD)
        except:
            return -1

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)