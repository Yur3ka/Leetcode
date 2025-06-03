class StockSpanner:

    def __init__(self):
        self.history = []
        self.record = []
        self.length = 0

    def next(self, price: int) -> int:
        if not self.history or price < self.history[-1]:
            self.history.append(price)
            self.record.append(1)
            self.length += 1
            return 1
        else:
            temp = self.record[-1]
            while temp < self.length and price >= self.history[-temp-1]:
                temp += self.record[-temp-1]
            self.history.append(price)
            self.record.append(temp+1)
            self.length += 1
            return temp+1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)