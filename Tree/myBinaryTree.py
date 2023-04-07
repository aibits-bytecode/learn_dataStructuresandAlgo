class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # in here we are adding numbers only
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def tree_traverse(self):
        elements = []

        # first go on left tree
        # visit base node
        # go on right sub tree

        if self.left:
            elements += self.left.tree_traverse()

        elements.append(self.data)

        if self.right:
            elements += self.right.tree_traverse()

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value, )
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value, )
            else:
                return False
        raise Exception("something went wrong")

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #  1.delete node with no child

    def delete_values(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_values(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_values(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_values(min_val)
        return self

def Build_BinaryTree(elements):
    print("Building tree with : ", elements)
    bt = BinaryTree(elements[0])
    for i in range(1, len(elements)):
        bt.add_child(elements[i])
    return bt


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    bt_numbers = Build_BinaryTree(numbers)
    # print(bt_numbers.tree_traverse())
    # print(bt_numbers.search(13))
    bt_numbers.delete_values(20)
    print(bt_numbers.tree_traverse())
    # print("------------------------------------")
    #
    # countries = ["India", "SL", "Canada", "UK", "USA", "China"]
    # bt_countries = Build_BinaryTree(countries)
    # print(bt_countries.tree_traverse())
    # print(bt_countries.search("Canada"))
