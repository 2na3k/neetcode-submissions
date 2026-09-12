class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # brute force no pruning
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):
                sides[side] += matchsticks[i]
                if dfs(i + 1): # dfs
                    return True
                
                # only go to this place if the dfs above is failed -> back
                sides[side] -= matchsticks[i]

            return False
        return dfs(0)


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        length = sum(matchsticks) / 4

        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]
            
                if sides[side] == 0:
                    break
            return False
    
        return dfs(0)
            
        