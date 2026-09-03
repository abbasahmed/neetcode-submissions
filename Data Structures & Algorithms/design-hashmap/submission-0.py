class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.buckets = [ListNode(-1, None) for _ in range(10007)]

    def hash(self, key):
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        head = self.buckets[hashkey]

        while head.next is not None:
            if head.key == key:
                head.val = value
                return 
            head = head.next
        if head.key == key:
            head.val = value
        else:
            new_node = ListNode(key, value)
            head.next = new_node
        

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        head = self.buckets[hashkey]
        while head is not None:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        head = self.buckets[hashkey]
        while head.next is not None:
            if head.next.key == key:
                temp = head.next.next
                head.next = temp
                return
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)