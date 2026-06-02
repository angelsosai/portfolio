import heapq
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maximo=max(workerTimes)
        tam=len(workerTimes)
        cont = defaultdict(int)
        valores = defaultdict(int)
        valores_i = defaultdict(int)
        heap = []
        for x,y in enumerate(workerTimes):
            heap.append((y,x))
            cont[x] += 0
            valores_i[x] += y
            valores[x] += 0
        heapq.heapify(heap)
        valor_=0
        # print(heap,cont)
        # heapq.heappush(lista, 2)
        while valor_<mountainHeight:
            valor=heapq.heappop(heap)
            cont[valor[1]]+=1
            valores[valor[1]]+=cont[valor[1]]*valores_i[valor[1]]
            heapq.heappush(heap, ((cont[valor[1]]+1)*valores_i[valor[1]]+ valores[valor[1]],valor[1]))
            # print(heap,cont,valores,valor_)
            valor_+=1
        # print(heapq.heappop(workerTimes))
        # print(workerTimes)
        return max(valores.values())