# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel=0
        cons=0
        lista=["a","e","i","o","u"]
        dic_v={}
        dic_c={}
        for i in s:
            if i in lista:
                if i in dic_v:
                    dic_v[i]+=1
                else:
                    dic_v[i]=1
                if dic_v[i]>vowel:
                    vowel=dic_v[i]
            else:
                if i in dic_c:
                    dic_c[i]+=1
                else:
                    dic_c[i]=1
                if dic_c[i]>cons:
                    cons=dic_c[i]
        return vowel+cons