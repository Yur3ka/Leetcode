class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        key_claimed = set()
        boxes = set()
        ans = 0
        for box in initialBoxes:
            if status[box] == 1:
                ans += candies[box]
                for key in keys[box]:
                    key_claimed.add(key)
                for b in containedBoxes[box]:
                    boxes.add(b)
            else:
                boxes.add(box)
        new_open = True
        while new_open:
            new_open = False
            for box in list(boxes):
                if box in key_claimed:
                    new_open = True
                    ans += candies[box]
                    boxes.remove(box)
                    key_claimed.remove(box)
                    for key in keys[box]:
                        key_claimed.add(key)
                    for b in containedBoxes[box]:
                        boxes.add(b)
                elif status[box] == 1:
                    new_open = True
                    ans += candies[box]
                    boxes.remove(box)
                    for key in keys[box]:
                        key_claimed.add(key)
                    for b in containedBoxes[box]:
                        boxes.add(b)
        return ans