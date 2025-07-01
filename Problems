# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def listtonode(dalist):
    head = ListNode(dalist[0])
    for d in dalist[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(d)
    return head
# def print(data):
#     if data is None:
#         print("Linked List is empty")
#         return
#     itr=data
#     llstr=''
#     while itr:
#         llstr+=str(itr)+'-->'
#         itr=itr
#     print(llstr)
def print_linked_list(head):
    """
    Prints the elements of a singly-linked list.
    Takes the head of the linked list directly as input.
    """
    if head is None:
        print("Linked List is empty")
        return
    
    itr = head
    ll_str = ""
    while itr:
        ll_str += str(itr.data)
        if itr.next:
            ll_str += " --> "
        itr = itr.next
    print(ll_str)

class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dumhead = ListNode()
        curentnode = dumhead
        p1 = listtonode(list1)
        p2 = listtonode(list2)


        while p1 is not None and p2 is not None:

            if p1.data <= p2.data:
                curentnode.next = p1
                p1 =p1.next
            else:
                curentnode.next = p2
                p2 = p2.next
            curentnode=curentnode.next
        if p1 is None:
            curentnode.next = p1
        if p2 is None:
            curentnode.next = p2
        return dumhead.next

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7,8]
ll = ListNode()
sol = Solution()
resu = sol.mergeTwoLists(list1,list2)
print_linked_list(resu)