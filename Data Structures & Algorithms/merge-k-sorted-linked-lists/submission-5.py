# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists)==1:
            return lists[0]

        dummyNode = ListNode(0,None)
        
        mergedLists = []
            
        while len(lists) > 1:
            print(len(lists))
            mergedLists = []

            for i in range (0, len(lists), 2): 
                #left has to use -1 rather than just i because if we overshoot the i, both left and right are out of range (ex. len lists = 3 and start = 0)
                left = lists[i]

                if i+1 == len(lists):
                    right = None
                else:
                    right = lists[i+1]

                mergedLists.append(self.mergeLists(left, right)) 
                

            lists = mergedLists


        return lists[0] #probably cant return it this way, id need a dummynode to keep the track of the actual min


    def mergeLists(self, l1, l2):
        #you need to keep a dummy node to keep track of what the first node for the list you return is
        dummyNode = ListNode(0,None)
        res = dummyNode

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next

            res = res.next

        if l1 is None:
            res.next = l2

        if l2 is None:
            res.next = l1

        return dummyNode.next




            
            


                

            

            

