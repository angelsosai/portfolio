
# 3713. Longest Balanced Substring I


# You are given a string s consisting of lowercase English letters.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.


class Solution:
    def longestBalanced(self, s: str) -> int:
        p=""
        maximo=1
        for i in range(len(s)):
            p=""
            p+=s[i]
            leng=1
            m={
                s[i]:1}
            for j in range(i+1,len(s)):
                leng+=1
                p+=s[j]
                if s[j] not in m:
                    m[s[j]]=1
                else:
                    m[s[j]]+=1
                
                aux=True
                valor=m[s[j]]
                for i in m:
                    # print(m[i],valor,m[0])
                    if m[i]!=valor:
                        aux=False
                        break
                # print(p,aux,leng)
                if aux:
                    if leng>maximo:
                        maximo=leng
        return maximo

