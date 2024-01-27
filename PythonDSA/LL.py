class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self,value):
        nodeObj = Node(value)
        if self.head is None and self.tail is None:
            self.head=self.tail=nodeObj
        else:
            self.tail.next=nodeObj
            self.tail=nodeObj
    
    def prepend(self,value):
        nodeObj = Node(value)
        if self.head is None and self.tail is None:
            self.head=self.tail=nodeObj
        else:
            nodeObj.next=self.head
            self.head=nodeObj
    
    def insert(self,index,value):
        nodeObj = Node(value)
        if index > self.length()+1:
            print('index out of range')
        elif index == self.length()+1:
            self.tail.next=nodeObj
            self.tail=nodeObj
        else:
            temp = self.head
            prev = self.head
            for i in range(1,index):
                prev=temp
                temp=temp.next
                
            nodeObj.next=temp
            prev.next=nodeObj

    def pop(self):
        if self.head is None and self.tail is None:
            print('Nothing to remove')
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next != self.tail:
                temp=temp.next
            self.tail = temp
            self.tail.next = None
    
    def popFirst(self):
        if self.head is None and self.tail is None:
            print('Nothing to remove')
        elif self.head==self.tail:
            self.head=self.tail=None
        else:
            temp = self.head
            self.head = temp.next
            temp=None

    def remove(self,index):
        if index > self.length()+1:
            print('index out of range')
        elif index == self.length()+1:
            self.pop()
        elif index == 1:
            self.popFirst()
        else:
            curr=self.head
            fwd=self.head
            prev=self.head
            for i in range(1,index):
                prev=curr
                curr=curr.next
                fwd=curr.next
            prev.next=fwd

    def middleNode(self):
        if self.head==None:
            print('ll is empty')
        else:
            fast = self.head
            slow = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow.value

    def length(self):
        i=0
        temp = self.head
        while temp!=None:
            i+=1
            temp=temp.next
        return i
    
    def traverse(self):
        temp=self.head
        while temp!=None:
            print(temp.value)
            temp = temp.next

ll=LL()
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(4)
ll.prepend(5)
ll.prepend(6)
ll.prepend(7)
ll.prepend(8)
ll.insert(6,100)
ll.pop()
ll.popFirst()
ll.remove(6)
ll.traverse()
print(ll.middleNode())