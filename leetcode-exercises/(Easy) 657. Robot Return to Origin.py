# 657. Robot Return to Origin
# Solved
# Easy - 483
# Topics
# premium lock icon
# Companies
# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        dic=Counter(moves)
        if "U" not in dic:
            dic["U"]=0
        if "D" not in dic:
            dic["D"]=0
        if "R" not in dic:
            dic["R"]=0
        if "L" not in dic:
            dic["L"]=0
        return True if (dic["R"]==dic["L"] and dic["U"]==dic["D"]) else False