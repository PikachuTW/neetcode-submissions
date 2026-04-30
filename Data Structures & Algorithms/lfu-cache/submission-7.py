class DoubleLinkList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node
        self.size += 1
    
    def delNode(self, node: Node):
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode
        self.size -= 1

    def delHead(self):
        node = self.head.next
        self.delNode(node)
        return node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = {} # freq -> list
        self.cache = {} # key -> node
        self.min_freq = 0

    def _incNode(self, node: Node):
        self.freq_map[node.freq].delNode(node)
        if self.freq_map.get(node.freq+1) is None:
            self.freq_map[node.freq+1] = DoubleLinkList()
        self.freq_map[node.freq+1].addNode(node)

        if self.freq_map[node.freq].size == 0:
            del self.freq_map[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node is None:
            return -1
        else:
            self._incNode(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self._incNode(node)
            return

        if len(self.cache) == self.capacity:
            head = self.freq_map[self.min_freq].delHead()
            if head:
                del self.cache[head.key]
            if self.freq_map[self.min_freq].size == 0:
                del self.freq_map[self.min_freq]

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.min_freq = 1

        if 1 not in self.freq_map:
            self.freq_map[1] = DoubleLinkList()
        self.freq_map[1].addNode(newNode)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)