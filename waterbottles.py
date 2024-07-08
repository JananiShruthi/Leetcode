class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles 

        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            drink += exchanged
            print("[DRINK] ", drink)
            print("[exchanged] ", exchanged)
            rem_bottles = numBottles % numExchange
            print("[RMAINING BOTTLES] ", rem_bottles)
            numBottles = exchanged + rem_bottles
            print("[Num Bottles now] ", numBottles)
        return drink
