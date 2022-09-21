class Solution:
    def myAtoi(self, s: str) -> int:
        neg,length = False, len(s)
        num= 0
        for i in range(length):
            if s[i].isalpha() or s[i] == '.': return 0
            if s[i] == ' ': continue
            else:
                # print(s[i])
                if s[i] == '-':
                    for j in range(i+1,length):
                        if s[j].isdigit(): num = num*10 + int(s[j])
                        else: break
                    if num > pow(2,31): num = pow(2,31)
                    return -num
                        
                elif s[i] == '+' or s[i].isdigit() :
                    # print(s[i])
                    if s[i] == '+': i+=1
                    for j in range(i,length):
                        if s[j].isdigit(): num = num*10 + int(s[j])
                        else: break
                        # print(s[j], num)
                    # print(num)
                    if num> pow(2,31)-1: num = pow(2,31)-1
                    return num 
        return num
                            
                        
                        
                        
                