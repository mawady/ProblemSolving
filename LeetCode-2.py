# https://leetcode.com/problems/add-two-numbers/
"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fill_ln(l: list) -> ListNode:
    head = None
    current = None
    for elm in l:
        if head == None:
            current = ListNode(elm)
            head = current
        else:
            current.next = ListNode(elm)
            current = current.next
    return head

def add_ln(ln1: ListNode, ln2: ListNode):
    head = None
    current = None
    carry = 0
    while(ln1 or ln2 or carry):
        val1 = ln1.val if ln1 else  0
        val2 = ln2.val if ln2 else  0
        val = val1 + val2 + carry
        if val >= 0:
            rem = (val%10)
            carry = int(val/10)
            if head == None:
                current = ListNode(val=rem)
                head = current
            else:
                current.next = ListNode(val=rem)
                current = current.next
        ln1 = ln1.next if ln1!=None else None
        ln2 = ln2.next if ln2!=None else None
    return head

def print_ln(ln: ListNode):
    str_ptr = ""
    while(ln):
        str_ptr += f"({ln.val})"
        ln = ln.next
        str_ptr += f" "
    print(str_ptr)



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return add_ln(l1,l2)
if __name__ == '__main__':
    # l1 = [0]
    # l2 = [0]
    # l1 = [2,4,3]
    # l2 = [5,6,4]
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]


    print(f"l1:{l1}")
    ln1 = fill_ln(l1)
    print_ln(ln1)
    print(f"l2:{l2}")
    ln2 = fill_ln(l2)
    print_ln(ln2)
    ln3 = add_ln(ln1,ln2)
    print_ln(ln3)
    print(f"output:{Solution().addTwoNumbers(ln1,ln2)}")