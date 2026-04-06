class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def build_tree(self):
        self.root = self.Node(5)

        self.root.left = self.Node(4)
        self.root.left.left = self.Node(2)
        self.root.left.left.left = self.Node(18)
        self.root.left.left.left.left = self.Node(9)
        self.root.left.left.right = self.Node(3)

        self.root.right = self.Node(7)
        self.root.right.right = self.Node(8)
        self.root.right.right.left = self.Node(99)
        self.root.right.right.right = self.Node(95)
        self.root.right.right.right.right = self.Node(88)

    def print_top_view_scheme(self):
        print("                              99")
        print("                             /")
        print("                3           8")
        print("                 \\         / \\")
        print("            18    4 - 5 - 7   95 - 88")
        print("            / \\  /")
        print("           9   2")

tree = BinaryTree()
tree.build_tree()
tree.print_top_view_scheme()  