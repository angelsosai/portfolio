# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


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