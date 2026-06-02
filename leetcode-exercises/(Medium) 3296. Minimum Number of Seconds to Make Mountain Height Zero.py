# 3296. Minimum Number of Seconds to Make Mountain Height Zero
# Solved
# Medium • 1640
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer mountainHeight denoting the height of a mountain.

# You are also given an integer array workerTimes representing the work time of workers in seconds.

# The workers work simultaneously to reduce the height of the mountain. For worker i:

# To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
# To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
# To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
# Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

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