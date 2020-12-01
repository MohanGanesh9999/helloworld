class node:
    def __init__(self,v=None):
        self.value=v
        self.next=None
    def isempty(self):
        return(self.value==None)
    def append(self,v):
        if (self.isempty()):
            self.value=v
        elif(self.next==None):
            newnode=node(v)
            self.next=newnode
        else:
            (self.next).append(v)
    def printl(self):
        temp=self
        while(temp.next!=None):
            print(temp.value)
            temp=temp.next
        print(temp.value)
    def insert(self,v,x):
        if (self.isempty()):
            print("list is empty")
        elif(self.value==x):
            newnode=node(v)
            newnode.value=self.value
            self.value=v
            newnode.next=self.next
            self.next=newnode
        else:
            (self.next).insert(v,x)
    def delete(self,v):
        if(self.next.value==v):
            self.next=self.next.next
        else:
            self.next.delete(v)
    def insert1(self,v):
        if (self.isempty()):
            self.value=v
        else:
            newnode=node(v)
            (newnode.value,self.value)=(self.value,newnode.value)
            (newnode.next,self.next)=(self.next,newnode)
    def count(self):
        temp=self
        i=1
        while(temp.next!=None):
            i=i+1
            temp=temp.next
        return(i)
        
l=node(0)
for i in range(1,10):
    l.append(i)
l.insert(11,5)
l.printl()
l.delete(11)
l.printl()
l.insert1(15)
l.printl()
print("no of elements="+str(l.count()))
