class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.buckets = [ListNode(-1) for _ in range(0, 10000)]

    def hash(self, key):
        return key % 10000

    def add(self, key: int) -> None:
        head = self.buckets[self.hash(key)]
        while head.next:
            if head.next.key == key:
                return
            head = head.next
        head.next = ListNode(key)

    def remove(self, key: int) -> None:
        head = self.buckets[self.hash(key)]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
        
    def contains(self, key: int) -> bool:
        head = self.buckets[self.hash(key)]
        while head.next:
            if head.next.key == key:
                return True
            head = head.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)