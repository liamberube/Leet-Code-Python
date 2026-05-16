# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_ended, l2_ended = False, False
        liste = []
        fut = 0
        while True:
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            else:
                l1_ended = True
                val1 = 0
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next
            else:
                l2_ended = True
                val2 = 0
            
            liste.append((val1 + val2 + fut) % 10)
            fut = (val1 + val2 + fut) //10
            if l1_ended and l2_ended:
                list_node = None
                if liste[-1] == 0:
                    liste = liste[:-1]
                for i in liste[::-1]:
                    list_node = ListNode(i, list_node)
                return list_node

#Test data
l1_pre = [2,4,3]
l2_pre = [5,6,4]
list_node = None
for i in l1_pre[::-1]:
    list_node = ListNode(i, list_node)
l1 = list_node
list_node = None
for i in l2_pre[::-1]:
    list_node = ListNode(i, list_node)
l2 = list_node

nexts = 0
ln = list_node
while nexts != None:
    ln = ln.next
    nexts = ln

a = Solution()
ln = a.addTwoNumbers(l1, l2)
nexts = 0
while nexts != None:
    print(ln.val)
    ln = ln.next
    nexts = ln