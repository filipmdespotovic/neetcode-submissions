class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}


        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        result = []
        for i in range(k):
            max_key = None
            max_count = -1

            for key in dict:
                if dict[key] > max_count:
                    max_count = dict[key]
                    max_key = key

            result.append(max_key)
            del dict[max_key]

        return result