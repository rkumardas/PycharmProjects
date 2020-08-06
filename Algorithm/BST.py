class Node:
    def __init__(self, dt=None):
        self.dt = dt
        self.l_next = None
        self.r_next = None

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = Node(key)

    def _insert(self, key, curr_node):

        if key < curr_node.dt:
            if curr_node.l_next:
                self._insert(key, curr_node.l_next)
            else:
                curr_node.l_next = Node(key)
        elif key > curr_node.dt:
            if curr_node.r_next:
                self._insert(key, curr_node.r_next)
            else:
                curr_node.r_next = Node(key)
        else:
            print ("duplicate")

    def _print_tree(self, node):

        if node is not None:
            self._print_tree(node.l_next)
            print(node.dt, end=" ")
            self._print_tree(node.r_next)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def find(self, node):
        temp = self.root
        while temp:
            if node < temp.dt:
                temp = temp.l_next
            elif node > temp.dt:
                temp = temp.r_next
            elif node == temp.dt:

                return temp
        return print("not in tree")
    def Delete(self, key):
        if self.root:
            self._Delete(key, self.root)
        else:
            print("empty tree")

    def _Delete(self, key, cur_node):
        if key > cur_node.dt:
            cur_node.r_next = self._Delete(key, cur_node.r_next)
        elif key < cur_node.dt:
            cur_node.l_next = self._Delete(key, cur_node.l_next)
        else:
            if cur_node.dt is not key:
                print("not in tree")

            elif cur_node.l_next and cur_node.r_next:
                node = self.find_min(cur_node.r_next)
                cur_node.dt = node.dt
                self._Delete(node.dt, cur_node.r_next)

            else:
                if cur_node.l_next is None:
                    temp = cur_node.r_next

                elif cur_node.r_next is None:
                    temp = cur_node.l_next

                return temp
        return cur_node

    def find_min (self, node):
        while node.l_next:
            node = node.l_next
        return node

d = [44,17,88,32,65,97,28,54,82,29,76]

if __name__  == "__main__":

    tree =Bst()
    for i in d:
        tree.insert(i)

    tree.print_tree()
    print("find ", tree.find(5))
    print("\n-------------")
    tree.Delete(32)
    tree.Delete(65)
    print("-------------")
    tree.print_tree()
