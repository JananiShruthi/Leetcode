class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output_str = ""
        if len(str1) > len(str2):
            t = str2
            s = str1
        else:
            t = str1
            s = str2
        
        pref = ""
        for st in t:
            pref += st
            if str1 == pref * (len(str1) // len(pref)) and str2 == pref * (len(str2) // len(pref)):
                if (len(output_str) < len(pref)):
                    output_str = pref
        return output_str
