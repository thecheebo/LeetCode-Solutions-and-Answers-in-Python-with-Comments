from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        #impossible = [1]

        #print(graph)
        def dfs(node):
            stack.append(node)


            for neighbor in graph[node]:
                if neighbor in stack:
                    return False

                if visited[neighbor] == False:
                    visited[neighbor] = True
                    possible = dfs(neighbor)
                    if possible == False:
                        return False
            visited[node] = True  
            possible_schedule.appendleft(node)   

            stack.pop()

            return True


        visited = [False] * numCourses
        possible_schedule = deque([])

        for i in range(numCourses):
            stack = []
            if visited[i] == False:
                possible = dfs(i)
            if possible == False:
                return []


        return possible_schedule 