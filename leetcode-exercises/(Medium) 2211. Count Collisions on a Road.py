# There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

# You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

# The number of collisions can be calculated as follows:

# When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
# When a moving car collides with a stationary car, the number of collisions increases by 1.
# After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

# Return the total number of collisions that will happen on the road.

from itertools import groupby
class Solution:
    def countCollisions(self, directions: str) -> int:
        """
        :type directions: str
        :rtype: int
        """
        choque_iz=False
        choques_totales=0
        R=False
        R_rep=0
        for valor, grupo in groupby(directions):
            AUX=len(list(grupo))
            if valor=="L" and choque_iz:
                if R:
                    choques_totales+=R_rep
                    R=False
                choques_totales+=AUX
            if valor=="R":
                R=True
                choque_iz=True
                R_rep=AUX
            if valor=="S":
                if R:
                    choques_totales+=R_rep
                    R=False
                choque_iz=True
            # print(valor,AUX,choques_totales)
            
        return choques_totales