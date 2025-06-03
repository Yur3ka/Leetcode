class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s = list(senate)
        r_count = s.count('R')
        d_count = n - r_count
        if r_count == 0:
            return "Dire"
        if d_count == 0:
            return "Radiant"
        # print(r_count)
        r_die = 0
        d_die = 0
        while d_count and r_count:
            for i in range(n):
                if s[i] == "R":
                    if r_die:
                        r_die -= 1
                        s[i] = ''
                    else:
                        d_die += 1
                        d_count -= 1
                        if d_count == 0:
                            return "Radiant"
                elif s[i] == "D":
                    if d_die:
                        d_die -= 1
                        s[i] = ''
                    else:
                        r_die += 1
                        r_count -= 1
                        if r_count == 0:
                            return "Dire"