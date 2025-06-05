class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dictionary = defaultdict(set)
        for i in range(len(s1)):
            dictionary[s1[i]].add(s2[i])
            dictionary[s2[i]].add(s1[i])
        smallest = [""] * 26
        for i in range(26):
            if smallest[i] != "":
                continue
            current = chr(ord('a')+i)
            sml = current
            visited = set()
            queue = [current]
            while queue:
                temp = queue.pop()
                if temp in visited:
                    continue
                visited.add(temp)
                sml = min(sml,temp)
                for adj in dictionary[temp]:
                    queue.append(adj)
            for char in visited:
                smallest[ord(char)-ord('a')] = sml
        ans = []
        for char in baseStr:
            ans.append(smallest[ord(char)-ord('a')])
        return ''.join(ans)