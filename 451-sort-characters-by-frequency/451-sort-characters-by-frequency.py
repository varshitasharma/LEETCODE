class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        freq = collections.defaultdict(int)
        
        for ch in s:
            freq[ch] += 1
        for ch, count in freq.items():
            heap.append((-count, ch))
        
        heapq.heapify(heap)
        s = ''
        while heap:
            occur, ch = heappop(heap)
            s += ch*(-occur)
        return s
            
        