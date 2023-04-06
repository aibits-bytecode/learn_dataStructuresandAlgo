class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def electronicStore():
    electronics = TreeNode("electronics")

    laptop = TreeNode("laptop")
    electronics.add_child(laptop)
    dellLaptop = TreeNode("dellLaptop")
    laptop.add_child(dellLaptop)
    alien = TreeNode("alien-ware")
    dellLaptop.add_child(alien)
    asusLaptop = TreeNode("asusLaptop")
    asusLaptop.add_child(TreeNode("viva-book"))
    laptop.add_child(asusLaptop)
    smartPhone = TreeNode("smartPhone")
    smartPhone.add_child(TreeNode("nokia"))
    electronics.add_child(smartPhone)

    return electronics


if __name__ == "__main__":
    root = electronicStore()
    print(root.print_tree())
