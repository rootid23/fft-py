
#Iteration

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        #graph
        #from , nbrs [2,3] , import

        val_dict = {}
        graph = {}
        for idx in range (len(employees)):
            emp = employees[idx]

            frm = emp.id
            imp = emp.importance
            nbrs = emp.subordinates

            val_dict[frm] = imp

            if(frm not in graph) :
                graph[frm] = []
            graph[frm] += nbrs

        emp = graph[id]
        total_imp = 0
        total_imp += val_dict[id]

        lst = []
        lst += graph[id]
        visited = set()
        while True:
            if(not lst) : break
            nbr = lst.pop()
            if(nbr not in visited) :
                visited.add(nbr)
                total_imp += val_dict[nbr]
                lst += graph[nbr]

        return total_imp


def getImportance(self, employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    dic ={}
    for empInfor in employees:
        dic[empInfor.id] = empInfor

    def cal_imp(id):
        return dic[id].importance + sum([cal_imp(empInfor) for empInfor in dic[id].subordinates])

    return cal_imp(id)



#Recursion
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        index= {e.id: (e.importance,e.subordinates) for e in employees}
        def calc(id):
            imp,sub=index[id]
            return imp+sum(map(calc,sub))
        return calc(id)

#Recursion w/ lambda
class Solution(object):
    def getImportance(self, employees, id):
        employees.sort(key=lambda x: x.id)
        res = 0
        subs = [employees[id-1]]
        for sub in subs:
            res += sub.importance
            subs += [employees[x-1]  for x in sub.subordinates ]
        return res


#Employee Importance
#You are given a data structure of employee information, which includes the
#employee's unique id, his importance value and his direct subordinates' id.
#For example, employee 1 is the leader of employee 2, and employee 2 is the
#leader of employee 3. They have importance value 15, 10 and 5, respectively.
#Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has
#[2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is
#also a subordinate of employee 1, the relationship is not direct.
#Now given the employee information of a company, and an employee id, you need
#to return the total importance value of this employee and all his
#subordinates.
#Example 1:
#Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
#Output: 11
#Explanation:
#Employee 1 has importance value 5, and he has two direct subordinates:
#employee 2 and employee 3. They both have importance value 3. So the total
#importance value of employee 1 is 5 + 3 + 3 = 11.
#Note:
#One employee has at most one direct leader and may have several subordinates.
#The maximum number of employees won't exceed 2000.
