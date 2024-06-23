class Solution:
    values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s.upper()
        num = 0
        temp = 0
        length = len(s)-1
        sum_list = []
        for i,v in enumerate(s):
            if i < length and s[i+1] == v:
                temp += roman_dict[v]
                continue 
            temp += roman_dict[v]
            if i>0 and roman_dict[v] > roman_dict[s[i-1]]:
                
                temp -= roman_dict[s[i-1]]*2
            sum_list.append(temp)
            num += temp           

            temp = 0
            
        return int(num)
