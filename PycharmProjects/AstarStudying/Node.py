

class Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None



    def show_data(self):
        return self.data

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_parent(self):
        return self.parent

    def set_left_child(self, new_node):
        self.left_child = new_node

    def set_right_child(self, new_node):
        self.right_child = new_node

    def set_parent(self, new_parent):
        self.parent = new_parent

