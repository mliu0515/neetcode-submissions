class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        reverseMap = defaultdict(set)
        for i in nums:
            curFreq = freqMap.get(i, 0)
            if curFreq > 0:
                reverseMap[curFreq].discard(i)
            reverseMap[curFreq + 1].add(i)
            freqMap[i] =  curFreq + 1  

        print(reverseMap)
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in reverseMap:
                for n in reverseMap[freq]:
                    res.append(n)
                    if len(res) == k:
                        return res
        
        return res
        