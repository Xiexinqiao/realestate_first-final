import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1])) # 将父级目录加入执行目录列表
import unittest
from part3.toolbox.request_manager import RequestManager

class TestRequestManager(unittest.TestCase):
    def setUp(self):
        self.request_manager = RequestManager()

    def test_add_request(self):
        client = "client1"
        self.request_manager.add_request(client)
        self.assertEqual(self.request_manager.request_queue.qsize(), 1)

    def test_process_request(self):
        client = "client1"
        self.request_manager.add_request(client)
        self.assertEqual(self.request_manager.process_request(), client)

    def test_process_request_empty_queue(self):
        self.assertIsNone(self.request_manager.process_request())

if __name__ == "__main__":
    unittest.main()
