# Linked list do not want pre-allocated space
# insertion is easier not need to swap values as arrays

# linked list traversal - O(n)
# Access element by value - O(n)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # here we insert data at the begining of linked list
    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    # here we insert data at the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    # in here we get the data list and add those to a linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # in here insert value at a index
    def insert_at(self,data,index):
        if index>self.length():
            raise Exception("invalid index")
        elif index == 0:
            self.insert_at_begining(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count+1 == index:
                    itr.next = Node(data,itr.next)
                    break
                itr = itr.next
                count += 1

    def insert_after(self,data,existing_value):
        pass


    # in here we remove element at index
    def remove_at(self, index):
        if index >= self.length():
            raise Exception("invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if (count + 1) == index:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def remove(self,existing_value):
        pass




    # in here return the length of the linked list
    def length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # in here print the data in linked list
    def print(self):
        if self.head is None:
            print("Empty list")
            return
        itr = self.head

        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "apple", "grapes"])
    ll.insert_at_end("papaya")
    ll.insert_at("mango",0)
    ll.print()
