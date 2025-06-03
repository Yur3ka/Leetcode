class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        store = set()
        for _,v in count.items():
            if v in store:
                return False
            store.add(v)
        return True