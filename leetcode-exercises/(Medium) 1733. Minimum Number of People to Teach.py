# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.



class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        minimo=float("inf")
        dic={}
        aux=0
        for i in languages:
            dic[aux+1]={}
            for j in i:
                dic[aux+1][j]=1
            aux+=1
        lista_aux=[]
        for j in friendships:
                aux=False
                for m in dic[j[1]].keys():
                    print(j,m,dic[j[0]])
                    if m in dic[j[0]]:
                        aux=True
                        break
                if not aux:
                    lista_aux.append([j[0],j[1]])
        #print(lista_aux)
        for i in range(n):
            contador=0
            for j in lista_aux:
                if i+1 not in dic[j[0]]:
                    contador+=1
                    dic[j[0]][i+1]=1
                # print(contador,j[0],dic[i+1])
                if i+1 not in dic[j[1]]:
                    contador+=1
                    dic[j[1]][i+1]=1
                # print(contador)
            if contador<minimo:
                minimo=contador
            # print(contador,minimo,i,dic)
        return minimo
        