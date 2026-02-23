# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Return the total number of laser beams in the bank.


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        conteo_1=bank[0].count("1")
        suma=0
        for i in range(1,len(bank)):
            conteo=bank[i].count("1")
            if conteo!=0:
                suma+=conteo*conteo_1
                conteo_1=conteo
        return suma

            