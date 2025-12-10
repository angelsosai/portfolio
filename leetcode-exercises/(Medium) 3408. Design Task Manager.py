# There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

# Implement the TaskManager class:

# TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

# void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

# void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

# void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

# int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

# Note that a user may be assigned multiple tasks.




import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.lista=[()]*len(tasks)
        self.dic={}
        for i in range(len(tasks)):
            self.lista[i]=(-tasks[i][2],-tasks[i][1],tasks[i][0])
            self.dic[tasks[i][1]]=self.lista[i]
        heapq.heapify(self.lista)
        # print(list(self.dic.values()))
        
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.lista,(-priority,-taskId,userId))
        self.dic[taskId]=(-priority,-taskId,userId)
        # print(self.lista)
        
    def edit(self, taskId: int, newPriority: int) -> None:
        self.dic[taskId]=(-newPriority,-taskId,self.dic[taskId][2])
        aux=list(self.dic.values())
        # print(aux)
        heapq.heapify(aux)
        self.lista=aux

    def rmv(self, taskId: int) -> None:
        del self.dic[taskId]
        aux=list(self.dic.values())
        heapq.heapify(aux)
        self.lista=aux


    def execTop(self) -> int:
        try:
            r=heappop(self.lista)
            del self.dic[-r[1]]
            return r[2]
        except IndexError:
            return -1
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()