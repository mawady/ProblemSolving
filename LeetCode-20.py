# https://leetcode.com/problems/valid-parentheses/
"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mtc = {'(' : ')', '{' : '}', '[' : ']'}
        stack = list()
        for elm in s:
            if elm in mtc:
                stack.append(elm)
            elif len(stack) == 0:
                return False
            elif len(stack) > 0 and elm != mtc[stack.pop()]:
                return False
        if len(stack) != 0:
            return False
        return True

if __name__ == '__main__':
    s = "()[]{}"
    print(f"s:{s}")
    print(f"output:{Solution().isValid(s)}")