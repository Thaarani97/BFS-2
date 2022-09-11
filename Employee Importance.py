"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
#SC -O(n)
#TC -O(n)
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        adj = {}
        for employee in employees:
            adj[employee.id] = [employee.importance,employee.subordinates]
        
        q = deque()
        q.append(id)
        total_importance = 0
        while q:
            curr_Emp = q.popleft()
            total_importance+= adj[curr_Emp][0]
            for sub in adj[curr_Emp][1]:
                q.append(sub)
        
        return total_importance