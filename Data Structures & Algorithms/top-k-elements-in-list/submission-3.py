class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        most_frequent = []

        for number in nums:
#            count.update({number:nums.count(number)})
            count[number] = 1 + count.get(number,0)
            
        while k != 0:
            max_key = max(count, key = count.get)
            most_frequent.append(max_key)
            count.pop(max_key)
            k-=1
        
        return most_frequent