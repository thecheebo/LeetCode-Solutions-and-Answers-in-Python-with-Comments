```https://leetcode.com/problems/merge-two-sorted-lists/solution/
```


class Solution():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        return answer
a = Solution()

b = a.ListNode(50)
c = a.ListNode(40, b)
d = a.ListNode(30, c)

e = a.ListNode(55)
f = a.ListNode(45, e)
g = a.ListNode(35, f)

a.mergeTwoLists(d,g)
