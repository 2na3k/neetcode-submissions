class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # do the dfs

        mapping = {
            i: [] for i in range(numCourses)
        }

        for crs, pre in prerequisites:
            mapping[crs].append(pre)
        
        visited = set()

        # do the dfs through the course
        def dfs(crs):
            if crs in visited:
                return False    # Cyclic graph -> can't
            if mapping[crs] == []:
                return True     # good case, just keep it
            

            visited.add(crs)
            for pre in mapping[crs]:
                if not dfs(pre):
                    return False
            
            # still not understand this part yet, dunno
            visited.remove(crs)
            mapping[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True