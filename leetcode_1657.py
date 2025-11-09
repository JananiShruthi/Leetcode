class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = {}
        d2 = {}
        for letter in word1:
            if letter not in d1:
                d1[letter] = 1
            else:
                d1[letter] += 1

        for letter in word2:
            if letter not in d2:
                d2[letter] = 1
            else:
                d2[letter] += 1

        print(f"d1: {d1}\n d2: {d2}")
        
        op1 = True
        op2 = True
        for key, val in d1.items():
            if key not in d2.keys():
                return False

        d1_vals = sorted(list(d1.values()))
        d2_vals = sorted(list(d2.values()))
        print(f"d1_vals: {d1_vals}\n d2_vals: {d2_vals}")
        if (d1_vals == d2_vals):
            print("Yes right?")
            return True
        else:
            return False

        # op1 = True
        # op2 = True
        # # Check if operation 1 is possible:
        # for key, val in d1.items():
        #     if key in d2 and val == d2[key]:
        #         op1 = True
        #     else:
        #         op1 = False
        #         break
        # if op1 == True:
        #     return True
        # else:
        #     # Check if operation 2 is possible        
        #     key_list_2 = d2.keys()
        #     val_list_2 = d2.values()
            
        #     for key, val in d1.items():
        #         if (key not in key_list_2) or (val not in val_list_2):
        #             return False

        # return op2
