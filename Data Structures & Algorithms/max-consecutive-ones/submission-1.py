class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 2 super duper pointer. weirder shit
        n, res = len(nums), 0

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                cnt +=1 
            res = max(res,cnt)
        
        return res


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count