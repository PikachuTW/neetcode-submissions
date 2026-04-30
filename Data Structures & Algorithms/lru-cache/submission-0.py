class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pushFront(self, node: Node):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node

    def popLast(self):
        last = self.tail.prev
        last.delete()
        return last

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def delete(self):
        prevNode = self.prev
        nextNode = self.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> node
        self.linklist = DoublyLinkedList()
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache.get(key)
        node.delete()
        self.linklist.pushFront(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            node.delete()
            self.linklist.pushFront(node)
            return


        newNode = Node(key, value)
        self.linklist.pushFront(newNode)
        self.cache[key] = newNode
        self.size += 1
        if self.size > self.capacity:
            last = self.linklist.popLast()
            del self.cache[last.key]
            self.size-= 1


