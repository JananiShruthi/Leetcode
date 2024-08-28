'''
The approach taken for the following code is BFS. Starting node is the start_word. The edge case: if endWord not in wordList return 0.
Pus the startWord into the queue and 1 which represents the steps to change from startWord to Endword.
Replace each of the letter in the current word with all the alphabets and see if the modified word is in the wordList. If present add to queue , level + 1. 
retur  level
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        word_set = set(wordList)
        queue = deque([(beginWord, 1)])
        seen = set(beginWord)
        if endWord not in word_set:
            print("Steps: 0")
            return 0

        while queue:
            #level_size = len(queue)
            curr_node, level = queue.popleft()
            print("Current word from the queue: ", curr_node)
            if curr_node == endWord:
                print("STEPS: ", level)
                return level
            for i in range(len(curr_node)):
                for a in alphabets:
                    new_word = curr_node[:i] + a + curr_node[i+1:]
                    #temp_str = ''.join(temp_list)
                    if (new_word in word_set) and (new_word not in seen):
                        print("Temp str: ", new_word)
                        queue.append((new_word, level +1))
                        seen.add(new_word)

        return 0
