class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(list)
        self.price = []
        self.rented = set()
        self.encode = {}
        
        for shop, movie, price in entries:
            self.movies[movie].append([price,shop])
            self.encode[(shop,movie)] = price
        for k,v in self.movies.items():
            v.sort()

    def search(self, movie: int) -> List[int]:
        res = []
        for i in range(len(self.movies[movie])):
            if len(res) == 5:
                break
            if (self.movies[movie][i][1],movie) not in self.rented:
                res.append(self.movies[movie][i][1])
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.encode[(shop,movie)]
        self.rented.add((shop,movie))
        heapq.heappush(self.price,[price,shop,movie])


    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove((shop,movie))

    def report(self) -> List[List[int]]:
        res = []
        temp = []
        used = set()
        while self.price:
            if len(res) == 5:
                break
            curr = heapq.heappop(self.price)
            if (curr[1],curr[2]) not in used and (curr[1],curr[2]) in self.rented:
                res.append([curr[1],curr[2]])
                temp.append(curr)
                used.add((curr[1],curr[2]))
        for item in temp:
            heapq.heappush(self.price,item)
        print(res)
        return res

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()