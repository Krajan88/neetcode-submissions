class ListNode:
    def __init__(self, val = 0, next = None, prev = None, key = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        #hashmap where key is the key used in get/put and value is a node whose .value is the value 
        #assigned to that key, .next is the more recent element and .prev is the less recent element
        self.recency = {}
        self.dummyNode = ListNode(0,None,None,None)
        self.capacity = capacity

        
        

    def get(self, key: int) -> int:
        if key not in self.recency:
            return -1

        node = self.recency[key]

        # if it's already the tail, nothing to move
        if node.next is None:
            return node.val

        # if it's currently the head, advance head
        if node is self.head:
            self.head = node.next

        # unlink node from its current spot
        node.prev.next = node.next
        node.next.prev = node.prev

        # relink node at the tail
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return node.val
            

    def put(self, key: int, value: int) -> None:
        #changing the value of a key
        if key in self.recency:
            #edge case for updating the tail value
            if self.recency[key].next is None:
                self.recency[key].val = value

            else:
                if self.recency[key] is self.head:
                    self.head = self.head.next

                #update the value and its recency
                self.recency[key].val = value

                self.recency[key].prev.next = self.recency[key].next
                self.recency[key].next.prev = self.recency[key].prev
                

                self.tail.next = self.recency[key]
                self.recency[key].prev = self.tail
                self.recency[key].next = None
                
                self.tail = self.recency[key]

                

        #creating a new key:value pair
        else:
            #runs if recency hash is empty / first element that's added to recency
            if not self.recency:
                self.head = ListNode(value, None, self.dummyNode, key)
                self.tail = self.head
                self.recency[key] = self.head

            #adds a new 'tail' to hash
            else:
                self.tail.next = ListNode(value, None, self.tail, key)
                self.tail = self.tail.next
                self.recency[key] = self.tail



        #if the most recently added item makes the hash over its capacity, we remove the least recent.
        if len(self.recency) > self.capacity:
            self.recency.pop(self.head.key)
            self.head = self.head.next
"""
Create a least recently used cache of size capacity. If the size is exceeded by using put, remove the
most recently used key. A key is used when get or put is called on it.


"""

