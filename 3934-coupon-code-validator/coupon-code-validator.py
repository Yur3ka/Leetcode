class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_code = defaultdict(list)
        def valid(s):
            if not s:
                return False
            for char in s:
                if not(char.isalnum() or char == '_'):
                    return False
            return True
        for i in range(len(code)):
            if isActive[i] == True and valid(code[i]):
                valid_code[businessLine[i]].append(code[i])

        res = []
        for cat in ["electronics", "grocery", "pharmacy", "restaurant"]:
            if valid_code[cat]:
                res.extend(sorted(valid_code[cat]))
        
        return res