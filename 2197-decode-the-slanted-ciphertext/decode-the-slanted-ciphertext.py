class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        decr = []
        k = len(encodedText)//rows
        for i in range(rows):
            decr.append(encodedText[i*k:(i+1)*k])
        ans = []
        for  i in range(k):
            x,y = 0,i
            while x< rows and y< k:
                ans.append(decr[x][y])
                print(x,y)
                x += 1
                y += 1
                
        res = ''.join(ans)
        res =res.rstrip()

        return res