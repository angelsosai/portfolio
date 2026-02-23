# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".


from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8:
            return []
        lst_h = [1, 2, 4, 8,16,32]
        # print(lst_h[:4])
        lista=[]
        for i in range(min(turnedOn,3)+1):
            # print(i,turnedOn-i)
            for m in list(combinations(lst_h, turnedOn-i)):
                minutos=sum(m)
                if minutos<60:
                    for h in list(combinations(lst_h[:4], i)):
                        horas=sum(h)
                        if horas<12:
                            lista.append(str(horas)+":"+str(minutos).zfill(2))
                            # print(horas)  
            # print(list(combinations(lst_h, turnedOn-i)),list(combinations(lst_h[:4], i)))
        return lista    