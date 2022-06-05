# https://leetcode.com/problems/isomorphic-strings/
"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true


Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct_s = dict()
        for idx, val in enumerate(s):
            if val not in dct_s:
                dct_s[val] = list()
            dct_s[val].append(idx)
        dct_t = dict()
        for idx, val in enumerate(t):
            if val not in dct_t:
                dct_t[val] = list()
            dct_t[val].append(idx)
        
        # print(dct_t.values())
        # print(dct_s.values())

        for val_s, val_t in zip(dct_s.values(), dct_t.values()):
            # print(val_s)
            # print(val_t)
            print(set(val_s) & set(val_t))
            if set(val_s) != set(val_t):
                return False
        return True
        
if __name__ == '__main__':
    s = "badc"
    t = "baba"
    print(f"s: {s}")
    print(f"t: {t}")
    print(f"output:{Solution().isIsomorphic(s,t)}")