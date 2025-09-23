# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = [str(x) for x in l1]
        list2 = [str(x) for x in l2]
        h1 = str()
        h2 = str()
        for i1 in list1:
            h1 += i1
        for i2 in list2:
            h2 += i2
        num1 = int(h1)
        num2 = int(h2)        
        sum = num1 + num2
        return [x for x in str(sum)]
        
        # lis1 = list1.reverse()
        # lis2 = list2.reverse()

        lis1 = [int(x) for x in list1]
        lis2 = [int(x) for x in list2]

        return lis1, lis2

sol = Solution()
print(sol.addTwoNumbers([2,4,3],[5,6,4]))