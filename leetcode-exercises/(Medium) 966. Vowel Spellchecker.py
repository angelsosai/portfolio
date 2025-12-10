
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

# For a given query word, the spell checker handles two categories of spelling mistakes:

# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["Yel´.
# lOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:

# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vocales = "aeiouAEIOU"
        wordlist_1=wordlist.copy()
        wordlist_1_l=wordlist.copy()
        lista=[""]*len(queries)
        for v in range(len(wordlist)):
            wordlist_1_l[v]=wordlist[v].lower()
            for i in vocales:
                wordlist[v]=wordlist[v].lower().replace(i, "*")
        # print(wordlist)
        for v in range(len(queries)):
            c=queries[v].lower()
            # print(c,wordlist_1_l)
            if queries[v] in wordlist_1:
                lista[v]=queries[v]
            elif c in wordlist_1_l:
                lista[v]=wordlist_1[wordlist_1_l.index(c)]
            else:
                for i in vocales:
                    queries[v]=queries[v].lower().replace(i, "*")
        aux=0
        for i in queries:
            if i in wordlist and lista[aux]=="":
                lista[aux]=wordlist_1[wordlist.index(i)]
            aux+=1
        return lista