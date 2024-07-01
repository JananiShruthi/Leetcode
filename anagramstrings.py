'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Approach = Sort the strings provided in the list strs. Then for each sorted string assign the original word(ow) such that sorting the ow gives the sorted string

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        anagram_list = []
        for words in strs:
            sorted_words = ''.join(sorted(words))
            if sorted_words in d.keys():
                d[sorted_words].append(words)
            else:
                d[sorted_words] = [words]

        for val in d.values():
            anagram_list.append(val)

        return anagram_list
        
