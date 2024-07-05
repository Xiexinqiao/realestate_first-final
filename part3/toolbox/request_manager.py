# toolbox/request_manager.py

from queue import Queue

class RequestManager:
    def __init__(self):
        self.request_queue = Queue()

    def add_request(self, client):
        self.request_queue.put(client)

    def process_request(self):
        if not self.request_queue.empty():
            return self.request_queue.get()
        return None
