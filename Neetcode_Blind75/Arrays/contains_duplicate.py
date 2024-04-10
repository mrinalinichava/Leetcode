from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d= defaultdict(int)
        for ele in nums:
            d[ele]=d[ele]+1
            if(d[ele]==2):
                return True
        return False

sol = Solution()
list = [1,1,2,3,4,5]
print(sol.containsDuplicate(list))