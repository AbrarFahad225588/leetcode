from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: list[int] = []
        dq: deque[int] = deque()
        for i in range(len(nums)):
            while dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if dq and i>= k-1:
                res.append(nums[dq[0]])
        return res
    
    
    
if __name__=='__main__':
    sol=Solution()
    list= [1,3,-1,-3,5,3,6,7]
    k=3
    res=sol.maxSlidingWindow(list,k)    
    print(res)        
                
                