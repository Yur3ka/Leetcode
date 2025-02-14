class ProductOfNumbers:

    def __init__(self):
        self.seq = []
        self.prod = []
        self.length = 0
        self.last_zero = -1
    def add(self, num: int) -> None:
        self.seq.append(num)
        self.length += 1
        if num == 0:
            self.last_zero = self.length
            self.prod.append(0)
        elif num == 1:
            self.prod.append(1)
        else:
            for i in range(max(self.last_zero,0),self.length-1):
                self.prod[i] *= num
            self.prod.append(num)
    def getProduct(self, k: int) -> int:
        if self.length - k < self.last_zero:
            return 0
        else:
            return self.prod[self.length-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)