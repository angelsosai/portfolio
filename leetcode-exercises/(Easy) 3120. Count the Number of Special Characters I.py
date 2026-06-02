
# 3120. Count the Number of Special Characters I
# Solved
# Easy - 734
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lista=Counter(word)
        conteo=0
        for i in lista:
            if i.lower()==i and i.upper() in lista:
                conteo+=1
        return conteo