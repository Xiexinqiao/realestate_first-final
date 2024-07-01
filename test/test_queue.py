import unittest
from part1.toolbox.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('apple')
        self.assertEqual(self.queue.queue, ['apple'])
        self.queue.enqueue('banana')
        self.assertEqual(self.queue.queue, ['apple', 'banana'])

    def test_dequeue(self):
        self.queue.enqueue('apple')
        self.queue.enqueue('banana')
        self.assertEqual(self.queue.dequeue(), 'apple')
        self.assertEqual(self.queue.dequeue(), 'banana')
        self.assertEqual(self.queue.dequeue(), None)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('apple')
        self.assertFalse(self.queue.is_empty())

    def test_repr(self):
        self.queue.enqueue('apple')
        self.queue.enqueue('banana')
        self.assertEqual(repr(self.queue), "Queue(['apple', 'banana'])")

if __name__ == '__main__':
    unittest.main()
