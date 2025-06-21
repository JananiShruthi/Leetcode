class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.count = 1
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        if self.stack[-1][0] > price:
            self.stack.append((price, 1))
        else:
            #l = []
            while self.stack and self.stack[-1][0] <= price:
                #self.count += 1
                p, c = self.stack.pop()
                self.count += c
                #l.append(self.stack.pop())
            #self.stack.extend(l)
            self.stack.append((price, self.count))
        return self.count

        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
