class SplayTree:
    def __init__(self):
        self.root = None
        self.search_counter = 0  # Counter for search operations

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)
        self.root = self._splay(self.root, key)

    def search(self, key):
        self.root = self._splay(self.root, key)
        self.search_counter += 1  # Increment counter on each search
        return self.root is not None and self.root.key == key

    def delete(self, key):
        if self.is_empty():
            raise Exception("Cannot delete from an empty tree")

        self.root = self._splay(self.root, key)
        if self.root.key != key:
            return

        if self.root.left is None:
            self.root = self.root.right
        else:
            temp = self.root
            self.root = self._splay(self.root.left, self._find_max(self.root.left).key)
            self.root.right = temp.right

    def _find_max(self, root):
        while root.right is not None:
            root = root.right
        return root

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key > key:
            if root.left is None:
                return root

            if root.left.key > key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif root.left.key < key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self._rotate_left(root.left)

            return root if root.left is None else self._rotate_right(root)
        else:
            if root.right is None:
                return root

            if root.right.key > key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self._rotate_right(root.right)
            elif root.right.key < key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)

            return root if root.right is None else self._rotate_left(root)

    def _insert_rec(self, root, key):
        if root is None:
            return self.Node(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        else:
            raise Exception("Duplicate key")
        return root

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
