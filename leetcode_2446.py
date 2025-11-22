class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h*60 + m

        s1, e1 = to_minutes(event1[0]), to_minutes(event1[1])
        s2, e2 = to_minutes(event2[0]), to_minutes(event2[1])

        return not (e1 < s2 or e2 < s1)
