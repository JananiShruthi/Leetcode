class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # final = [s.split(separator) for s in words]
        final = []
        for s in words:
            final += s.split(separator)

        f1 = [s for s in final if s != '']
        return f1
