class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # can be solved using hashmap
        ### we will counting the number of occurances of each letter in a word 
        # and that will be the key for the hashmap, and the list of words that follow that
        # that counter of letter from the key are the values for that key 
        # time complextity - O(m*n)
        # where m in the number of words in the list
        # n is the lenght of the word###

        hashmap = {}

        for string in strs:

            count = [0] *26
            #assigning all values of the list as 0 for a....z
            #each string is having a list of 26 0s being created

            for character in string:
                count[ord(character) - ord("a")] += 1
                # whenever new character is encountered, increment the character count from the 
                # list associated with each word

            hashmap[tuple(count)].append(string)

        return hashmap.values()



# sorting solutions 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = defaultdict(list)

        for s in strs:

            sorted_strings = ''.join(sorted(s))
            #sort each word

            result[sorted_strings].append(s)
            #use the sorted word as key and append the original word corresponding to the sorted
            # version 

        return list(result.values())



