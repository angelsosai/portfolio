# You are given an array apple of size n and an array capacity of size m.

# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

# Note that, apples from the same pack can be distributed into different boxes.



class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        suma=sum(apple)
        lista_=sorted(capacity)
        conteo=0
        suma_=0
        for i in range(len(capacity)-1,-1,-1):
            suma_+=lista_[i]
            if suma_>=suma:
                return conteo+1
            conteo+=1
        return conteo