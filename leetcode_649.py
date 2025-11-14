class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        indices = {}
        party = []

        for i, val in enumerate(senate):
            if val not in indices:
                indices[val] = [i]
            else:
                indices[val].append(i)
            party.append(val)
        
        if len(set(party)) == 1:
            if senate[0] == 'R':
                return 'Radiant'
            else:
                return 'Dire'

        print(f"Indices: ", indices)
        loop_condition = True
        n = len(party)
        while loop_condition:
            print(f"Party: ", party)
            for i in range(n):
                if party[i] == 'R':
                    if len(indices['D']) > 0:
                        ban_list = indices['D']
                        idx = -1
                        for x in ban_list:
                            if x > i:
                                idx = x
                                break
                        if idx == -1:
                            idx = ban_list[0]
                        ban_list.remove(idx)
                        party[idx] = -1
                    else:
                        return 'Radiant'
                elif party[i] == 'D':
                    if len(indices['R']) > 0:
                        ban_list = indices['R']
                        idx = -1
                        for x in ban_list:
                            if x > i:
                                idx = x
                                break
                        if idx == -1:
                            idx = ban_list[0]
                        ban_list.remove(idx)
                        party[idx] = -1
                    else:
                        return 'Dire'
            if ('R' in party) and ('D' in party):
                loop_condition = True
            elif ('R' in party):
                return 'Radiant'
            elif ('D' in party):
                return 'Dire'

##########################################################################################

#  ChatGPT solu

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        n = len(senate)

        # Fill queues with initial indices
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        # Simulate
        while R and D:
            r_i = R.popleft()
            d_i = D.popleft()

            # whoever is smaller bans the other
            if r_i < d_i:
                # R bans D, so R gets new index + n (cycle)
                R.append(r_i + n)
            else:
                # D bans R
                D.append(d_i + n)

        return "Radiant" if R else "Dire"
