class Node:
    def __init__(self, key:str=None, value:int=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq=1


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def add_front(self,node:Node)->Node:
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.size+=1;
        return node
    def remove(self,node:Node):
        if self.size==0:
            return
        
        node.prev.next=node.next;
        node.next.prev=node.prev
        print("node delete successfully")
        self.size-=1
    @property
    def remove_last(self):
        if self.size==0:
            return Node
        node=self.tail.prev
        self.remove(node=node)
        return node   
            
    
class LFUCache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.key_to_node = {}
        self.freq_to_list={}
        self.min_freq=0
    def update_frequency(self,node:Node):
        old_freq= node.freq
        
        old_list=self.freq_to_list[old_freq]
        old_list.remove(node)
        
        if old_freq==self.min_freq and old_list.size==0:
            self.min_freq += 1; 
        node.freq+=1;
        new_freq=node.freq;
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq]=DoublyLinkedList()
        self.freq_to_list[new_freq].add_front(node)
    def get(self,key:int)->int:
        if key not in self.key_to_node:
            return -1;
        node:Node=self.key_to_node[key]
        self.update_frequency(node=node)
        return node.value
    def put(self,key:int,value:int)->None:
        if self.capacity==0:
            return None
        
        if key  in self.key_to_node:
            node:Node=self.key_to_node[key]
            node.value=value
            self.update_frequency(node)
            return
        if len(self.key_to_node)>=self.capacity:
            lfu_list=self.freq_to_list[self.min_freq]
            removed_node=lfu_list.remove_last
            del self.key_to_node[removed_node.key]
            
        new_node=Node(key=key,value=value)
        self.key_to_node[key]=new_node
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
        self.freq_to_list[1].add_front(new_node)
        self.min_freq = 1
               