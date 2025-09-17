class Solution:
    def dayOfYear(self, date: str) -> int:
        def leaf(year):
            if year % 400 == 0:
                return True
            elif year %4 == 0 and year %100 == 0:
                return False
            elif year %4 == 0:
                return True
            return False
        ans = 0
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        if leaf(year) and month > 2:
            ans += 1
        for i in range(month-1):
            ans += days[i]
        ans += day
        return ans
