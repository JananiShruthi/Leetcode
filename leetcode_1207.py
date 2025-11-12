class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        values = [val for val in c.values()]
        return len(values) == len(set(values))
