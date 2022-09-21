class Solution:
    def myAtoi(self, s: str) -> int:
        neg,length = False, len(s)
        num=i= 0
        s = s.strip()
        for ch in s:
            if ch == '-' and i==0: neg = True
            elif ch == '+' and i==0: neg = False
            elif ch.isdigit():
                num = num*10 + int(ch)
                if num>=2**31: 
                    num = 2**31  
                    if not neg: num-=1
                    break
            else: break  
            i+=1
        return -num if neg else num
                            
                        
                        
                        
                