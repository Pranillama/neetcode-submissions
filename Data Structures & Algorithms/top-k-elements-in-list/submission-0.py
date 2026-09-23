class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] =1+count.get(n,0)

        freq =[[] for i in range(len(nums)+1)]   
        for n, c in count.items():
            freq[c].append(n)

        res =[]
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]: # for eg: if i=2 it visits the vallue with frequency 2 (occured 2 times)
                res.append(n)
                if len(res) ==k:
                    return res