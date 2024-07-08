class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        #direction = 1 # 1 for forward direction and -1 for the reverse 
        i = 1 # start from the first person
        while time:
            if i == 1:
                direction = 1

            if i == n:
                direction = -1

            if direction == 1:
                i += 1

            elif direction == -1:
                i -= 1

            time -= 1

            print(f"DIRECTION: {direction} PERSON {i} TIME : {time} ")

        return i
