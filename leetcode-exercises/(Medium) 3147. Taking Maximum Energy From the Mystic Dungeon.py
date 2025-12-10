# 3147. Taking Maximum Energy From the Mystic Dungeon
# Solved
# Medium - 1374
# Topics
# premium lock icon
# Companies
# Hint
# IBM
# In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

# You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

# In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

# You are given an array energy and an integer k. Return the maximum possible energy you can gain.

# Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[:] - k - 1
        for i in range(len(energy), -1, -1):
            dp[i] += dp[i + k]
        return max(dp)