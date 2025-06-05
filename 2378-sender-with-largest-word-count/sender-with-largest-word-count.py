class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = defaultdict(int)
        for i in range(len(messages)):
            words = messages[i].split()
            # for word in words:
            count[senders[i]] += len(words)
        res_send = ''
        res_word = 0
        for k,v in count.items():
            # print(k,v)
            if v >= res_word:
                # print(v,res_word)
                if v > res_word:
                    res_send = k
                else:
                    res_send = max(k,res_send)
                res_word = v
        return res_send