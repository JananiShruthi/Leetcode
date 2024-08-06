class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
    
        # Sorting by frequency in descending order
        cnt_sorted = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        print("Sorted dict: ", dict(cnt_sorted))
        
        min_cost = 0
        push = 1
        threshold = 8
        current_index = 0
        
        for key, val in cnt_sorted:
            print("Index: ", current_index)
            if current_index < threshold:
                min_cost += val * push
            else:
                push += 1
                threshold += 8
                min_cost += val * push

            current_index += 1
            print(f"Min cost for {key} is {min_cost}")
        
        print("Final Minimum cost: ", min_cost)
        return min_cost
