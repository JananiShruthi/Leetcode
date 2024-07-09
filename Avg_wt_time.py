'''There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. 
The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.
Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.'''

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        freetime = 0
        avg_wt = 0
        for cust in customers:
            freetime = max(freetime, cust[0]) + cust[1] # freetime is the time the chef will be available for preparing the order 
            avg_wt += freetime - cust[0]
        return avg_wt / len(customers)
