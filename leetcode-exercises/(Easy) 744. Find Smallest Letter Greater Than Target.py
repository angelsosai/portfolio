# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            c = l + (r - l) // 2
            if letters[c] <= target:
                l = c + 1
            else:
                r = c - 1
        if l >= len(letters):
            return letters[0]
        return letters[l]
