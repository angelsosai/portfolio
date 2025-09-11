# Given a 0-indexed string s, permute s to get a new string t such that:

# All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
# The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

class Solution:
    def sortVowels(self, s: str) -> str:
        lista_vo=["a","e","i","o","u","A","E","I","O","U"]
        lista_vo_pa=[]
        for i in range(len(s)):
            if s[i] in lista_vo:
                lista_vo_pa.append(s[i])
        lista_vo_pa.sort()
        aux=0
        res=""
        for i in range(len(s)):
            if s[i] in lista_vo:
                res+=lista_vo_pa[aux]
                aux+=1
            else:
                res+=s[i]
        return res
        