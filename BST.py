from BNode import bnode
class binary_search_tree:
    def __init__(self):
        self.root = None

    def _rec_search(self, key, cur_node):
        if cur_node:
            if int(cur_node.entry[1]) == key:
                print(f"US: {cur_node.entry[0]}\nJapanese: {cur_node.entry[2]}")
                return True
            else:
                if int(cur_node.entry[1]) > key:
                    return self._rec_search(key, cur_node.left)
                if int(cur_node.entry[1]) < key:
                    return self._rec_search(key, cur_node.right)
        else:
            print("Error: Pokemon does not exist")
            return False

    def add(self, entry):
        if self.root == None:
            self.root = bnode(entry)
        elif int(self.root.entry[1]) == int(entry[1]):
            print("Error: Duplicate Pokedex ID")
        elif int(self.root.entry[1]) < int(entry[1]):
            if self.root.right == None:
                self.root.right = bnode(entry)
            else:
                self._rec_add(entry, self.root.right)
        elif int(self.root.entry[1]) > int(entry[1]):
            if self.root.left == None:
                self.root.left = bnode(entry)
            else:
                self._rec_add(entry, self.root.left)
        else:
            raise RuntimeError

    def _rec_add(self, entry, cur_node):
        if int(cur_node.entry[1]) > int(entry[1]):
            if cur_node.left == None:
                cur_node.left = bnode(entry)
            else:
                self._rec_add(entry, cur_node.left)
        elif int(cur_node.entry[1]) < int(entry[1]):
            if cur_node.right == None:
                cur_node.right = bnode(entry)
            else:
                self._rec_add(entry, cur_node.right)
        elif int(cur_node.entry[1]) == int(entry[1]):
            print("Error: Duplicate Pokedex ID")
        else:
            raise RuntimeError

    def remove(self, current_node, key):
        if current_node is None:
            return current_node
        if key < int(current_node.entry[1]):
            current_node.left = self.remove(current_node.left, key)
        elif key > int(current_node.entry[1]):
            current_node.right = self.remove(current_node.right, key)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            temp = self.minNode(current_node.right)
            current_node[1] = temp[1]
            current_node.right = self.remove(current_node.right, int(temp[1]))
        return current_node


    def minNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def copy(self, current_node):
        if current_node is None:
            return None
        root_copy = bnode(current_node)
        root_copy.left = self.copy(current_node.left)
        root_copy.right = self.copy(current_node.right)
        return root_copy

    def pre_order(self, cur_node):
        if cur_node != None:
            print(f"US: {cur_node.entry[0]} Pokedex ID: {cur_node.entry[1]} Japanese: {cur_node.entry[2]}")
            self.pre_order(cur_node.left)
            self.pre_order(cur_node.right)

    def in_order(self, cur_node):
        if cur_node != None:
            self.in_order(cur_node.left)
            print(f"US: {cur_node.entry[0]} Pokedex ID: {cur_node.entry[1]} Japanese: {cur_node.entry[2]}")
            self.in_order(cur_node.right)

    def post_order(self, cur_node):
        if cur_node != None:
            self.post_order(cur_node.left)
            self.post_order(cur_node.right)
            print(f"US: {cur_node.entry[0]} Pokedex ID: {cur_node.entry[1]} Japanese: {cur_node.entry[2]}")