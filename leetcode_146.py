class Node:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def addFirst(self,node:Node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.size+=1
    def remove(self,node: Node):
        node.next.prev=node.prev
        node.prev.next=node.next
        node.prev=None
        node.next=None
        self.size-=1
    def move_to_front(self,node: Node):
        self.remove(node) 
        self.addFirst(node)
    @property
    def remove_last(self)->Node:
        if self.size==0:
            return None
        node:Node=self.tail.prev
        self.remove(node)
        return node
    class LRUCache:
        def __init__(self,capacity:int)->None:
            self.capacity=capacity
            self.key_to_node={}
            self.dll=DoublyLinkedList()
        def get(self,key:int)->int:
            if key not in self.key_to_node:
                return -1
            node:Node = self.key_to_node[key]    
            self.dll.move_to_front(node)
            return node.value
        def put(self,key:int,value:int)->None:
            if key in self.key_to_node:
                node:Node=self.key_to_node[key]
                node.value=value
                self.dll.move_to_front(node)
                return 
            if len(self.key_to_node)>=self.capacity:
                del self.key_to_node[self.dll.remove_last]
            newNode=Node(key=key,value=value)
            self.key_to_node[key]=newNode
            self.dll.addFirst(newNode)    
                
            
                        
