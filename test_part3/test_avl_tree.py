import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # 将父级目录加入执行目录列表

import unittest
from part3.toolbox.avl_tree import AVLTree
class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl_tree = AVLTree()

    def test_insert(self):
        self.avl_tree.insert(10, "Value 10")
        self.avl_tree.insert(20, "Value 20")
        self.avl_tree.insert(30, "Value 30")
        self.assertEqual(self.avl_tree.in_order_traversal(self.avl_tree.root), ["Value 10", "Value 20", "Value 30"])

    def test_insert_and_balance_left_left(self):
        self.avl_tree.insert(30, "Value 30")
        self.avl_tree.insert(20, "Value 20")
        self.avl_tree.insert(10, "Value 10")
        self.assertEqual(self.avl_tree.in_order_traversal(self.avl_tree.root), ["Value 10", "Value 20", "Value 30"])

    def test_insert_and_balance_right_right(self):
        self.avl_tree.insert(10, "Value 10")
        self.avl_tree.insert(20, "Value 20")
        self.avl_tree.insert(30, "Value 30")
        self.assertEqual(self.avl_tree.in_order_traversal(self.avl_tree.root), ["Value 10", "Value 20", "Value 30"])

    def test_insert_and_balance_left_right(self):
        self.avl_tree.insert(30, "Value 30")
        self.avl_tree.insert(10, "Value 10")
        self.avl_tree.insert(20, "Value 20")
        self.assertEqual(self.avl_tree.in_order_traversal(self.avl_tree.root), ["Value 10", "Value 20", "Value 30"])

    def test_insert_and_balance_right_left(self):
        self.avl_tree.insert(10, "Value 10")
        self.avl_tree.insert(30, "Value 30")
        self.avl_tree.insert(20, "Value 20")
        self.assertEqual(self.avl_tree.in_order_traversal(self.avl_tree.root), ["Value 10", "Value 20", "Value 30"])

    # 可以继续添加更多测试用例，测试删除、查找等操作...

if __name__ == '__main__':
    unittest.main()
