class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        lista_aux=[]
        enteros=0
        for i in classes:
            i[0],i[1]=float(i[0]),float(i[1])
            if i[0]==i[1]:
                enteros+=1    
            else:
                impacto=(i[0]/i[1])-((i[0]+1)/(i[1]+1))
                lista_aux.append((impacto,i))
        tamao=len(lista_aux)
        if lista_aux==[]:
            return 1
        heapq.heapify(lista_aux)
        for _ in range(extraStudents):
            impacto, clase = heapq.heappop(lista_aux)
            valor1 = clase[0] + 1
            valor2 = clase[1] + 1
            nuevo_impacto = ((valor1 + 1) / (valor2 + 1)) - (valor1 / valor2)
            heapq.heappush(lista_aux, (-nuevo_impacto, [valor1, valor2]))
        return (sum([x[1][0]/x[1][1] for x in lista_aux])+enteros)/len(classes)