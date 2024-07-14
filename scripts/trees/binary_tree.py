from matplotlib import pyplot as plt
from PyQt6.QtWidgets import QMessageBox

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.values = set() # ! Almacenar valores únicos para evitar duplicados

    def insert(self, parent_node, side, value, parent_widget=None):
        if parent_node is None:
            self.show_error("Error: El nodo padre no puede ser None", parent_widget)
            return

        if value == 0 or value in self.values:
            self.show_error("Error: Valor inválido o ya existente", parent_widget)
            return

        new_node = TreeNode(value)

        if side.lower() == "left":
            if parent_node.left is None:
                parent_node.left = new_node
                self.values.add(value)
            else:
                self.show_error("Error: El nodo izquierdo ya está ocupado", parent_widget)
        elif side.lower() == "right":
            if parent_node.right is None:
                parent_node.right = new_node
                self.values.add(value)
            else:
                self.show_error("Error: El nodo derecho ya está ocupado", parent_widget)
        else:
            self.show_error("Error: El lado debe ser 'left' o 'right'", parent_widget)

    def delete_node(self, value, parent_widget=None):
        self.root, deleted = self._delete_node_rec(self.root, value)
        if deleted:
            self.values.remove(value)
        else:
            self.show_error(f"Error: El nodo con valor {value} no existe", parent_widget)

    def _delete_node_rec(self, node, value):
        if node is None:
            return node, False

        if value < node.data:
            node.left, deleted = self._delete_node_rec(node.left, value)
            return node, deleted
        elif value > node.data:
            node.right, deleted = self._delete_node_rec(node.right, value)
            return node, deleted
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            min_larger_node = self._get_min(node.right)
            node.data = min_larger_node.data
            node.right, _ = self._delete_node_rec(node.right, min_larger_node.data)
            return node, True

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def clear(self):
        self.root = None
        self.values.clear()

    def pre_order(self, node, result):
        if node:
            result.append(node.data)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)

    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append(node.data)
            self.in_order(node.right, result)

    def post_order(self, node, result):
        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.data)

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def draw_tree(self, ax, node, x=0, y=0, dx=1):
        if node:
            ax.text(x, y, str(node.data), ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='black'))
            if node.left:
                ax.plot([x, x-dx], [y, y-1], 'k-')
                self.draw_tree(ax, node.left, x-dx, y-1, dx/2)
            if node.right:
                ax.plot([x, x+dx], [y, y-1], 'k-')
                self.draw_tree(ax, node.right, x+dx, y-1, dx/2)

    def show_error(self, message, parent_widget):
        if parent_widget:
            error_dialog = QMessageBox(parent_widget)
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setText(message)
            error_dialog.setWindowTitle("Error")
            error_dialog.exec()
        else:
            print(message)
