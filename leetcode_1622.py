class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        # normalize val against current transforms 
        normalized = (val - self.add) * pow(self.mul, -1, self.MOD) % self.MOD
        self.seq.append(normalized)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD  # O(1)

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mul = (self.mul * m) % self.MOD    # O(1)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD
