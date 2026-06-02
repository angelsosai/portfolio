# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        contador=0
        lon=len(s)
        contador_b=0
        lista_a=[0]*(lon+2)
        lista_b=[0]*(lon+2)
        for i,value in enumerate(s):
            if value=="b":
                contador_b+=1
            lista_a[i+1]=i+1-contador_b
            lista_b[i+1]=contador_b
        max_a=lista_a[-2]
        minimo=lon
        for index,_ in enumerate(lista_a):
            val=max_a-lista_a[index]+lista_b[index]
            if val<minimo:
                minimo=val
            # print(index,"---",lista_a[index],lista_b[index],val)

        return minimo
        
