class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        result = []
        for num in range(100, 999, 2):
            d1, d2, d3 = num//100, (num//10) % 10, num %10
            candidate_freq = Counter([d1, d2, d3])
            if all(candidate_freq[d] <= freq[d] for d in candidate_freq):
                result.append(num)
        return result
