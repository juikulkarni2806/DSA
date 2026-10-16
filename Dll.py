class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp

    def insert(self, new_node, position):

        if position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head=new_node
        else:
            p=1
            temp=self.head
            while(p!=position-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
            temp.next.prev=new_node
            new_node.prev=temp    
            

        
        

    def reverse (self):
        curr=self.head
        prev=None
        while(curr):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev

    def findmid_del(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("MiddleNode: ",temp.data)
        prev.next=temp.next
        temp=None
    
    def delfirst_last(self):
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None


        
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
list1=DLL()            
n1=Node(10)
n2=Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))
list1.append(Node(51))
#list1.print()
list1.insert(Node(60),2)
# list1.reverse()
list1.print()
# list1.findmid_del()
# list1.print()
# list1.delfirst_last()
# list1.print()