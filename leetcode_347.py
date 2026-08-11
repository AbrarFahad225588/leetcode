from typing import List
import heapq
# class Solution:

#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         map = {}

#         for i in nums:
#             map[i]=map.get(i,0)+1

      
#         heap=[]
#         # for key,freq in map.items():
#         #     heapq.heappush(heap,(-freq,key))
#         # ls=[]
#         # for _ in range(k):
#         #     k,v=heapq.heappop(heap)
#         #     ls.append(v)
#         # print(ls) 
        
#         # optimal solution 2
#         for c,f in map.items():
#             heapq.heappush(heap,(f,c))
#             print(len(heap))
#             if len(heap) > k:
#                 # print("yes")
#                 heapq.heappop(heap)
#         # print(heap)
#         ls=[v for c,v in heap]
#         print(ls)        
                
           
                
# from typing import List
# import heapq


# class Solution:

#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         # 1. Frequency count
#         freq = {}

#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1

#         # 2. Min heap
#         heap = []

#         # 3. Process every number
#         for num, count in freq.items():

#             heapq.heappush(heap, (count, num))

#             # Heap size k এর বেশি হলে
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         # 4. Extract numbers
#         print( [num for count, num in heap])


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums :
            freq[i]=freq.get(i,0)+1
        
        soret=sorted(freq,reverse=True)
        
        print(soret)    

if __name__ == "__main__":

    s = Solution()

    s.topKFrequent([1,1,1,2,3],2)