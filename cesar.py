class Solution:
    def cesar(self,str1,str2):
        if len(str1)!=len(str2):
            return
        value=ord(str2[0])-ord(str1[0])
        for i in range(len(str1)):
            if ((ord(str2[i])>64 and ord(str2[i])<91) or (ord(str2[i])>96 and ord(str2[i])<123)) and ((ord(str1[i])>64 and ord(str1[i])<91) or (ord(str1[i])>96 and ord(str1[i])<123)):
                transmit=ord(str2[i])-ord(str1[i])
                if transmit < 0:
                    transmit = 26 + transmit
                if transmit!=value:
                    return -1
            else:
                return
        return value
