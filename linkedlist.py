class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head =None
    
    def InsertAtBeg(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def InsertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)
    def  InsertValues(self, data_list):
        self.head=None
        for data in data_list:
            self.InsertAtEnd(data)
    
    def lengthofll(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove(self,index):
        if index<0 or index>=self.lengthofll():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def InsertatIndex(self,index,data):
        if index<0 or index>self.lengthofll():
            raise Exception("Invalid Index")
        if index==0:
            self.InsertAtBeg(data)
        count =0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll= LinkedList()
    ll.InsertValues([23,456,68,98])
    ll.insert_after_value(456,786)
    ll.print()
    ll.remove_by_value(68)
    ll.print()