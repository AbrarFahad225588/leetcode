
import heapq
from typing import List


class Solution:
    def topKFrequent(self,words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        heap = []
        class Word:
            def __init__(self, count, word):
                self.count = count
                self.word = word
            def __lt__(self, other):
                return self.count < other.count or (self.count == other.count and self.word > other.word)
        for word, count in word_count.items():
            heapq.heappush(heap, Word(count, word))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [item.word for item in heap]
        result.sort(key=lambda x: (-word_count[x], x))
        return result
if __name__ == "__main__":
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 2
    Solution().topKFrequent(words, k)
