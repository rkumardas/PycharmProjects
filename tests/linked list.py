class Node :
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_node(self):
        return self.next

    def next_node(self, next_node=None):
        self.next = next_node

class list :
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next_node(self.head)
        self.head = new



    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def remove(self, data):
        temp = self.head
        prev = None
        while temp.data != data:
            prev = temp
            temp = temp.next

        if prev == None:
            self.head =temp.next
        elif temp.data == data:
            prev.next = temp.next
            return




llist = list()

#no =int(input("enten no u want to enter in list :"))

"""for i in range(no):
    llist.insert(int(input()))
"""

llist.insert(5)
llist.insert(7)
llist.insert(6)
llist.insert(9)
llist.insert(3)
llist.insert(1)

#m = bool(llist.search(8))
#print(m)
llist.printlist()
llist.remove(1)
print()
llist.printlist()

