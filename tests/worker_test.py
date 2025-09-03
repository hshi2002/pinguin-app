import unittest
from app.worker import ping

class WorkerTestCase(unittest.TestCase):
    def test_ping_valid(self):
        result = ping("127.0.0.1")
        self.assertIsNotNone(result)

    def test_ping_invalid(self):
        result = ping("256.256.256.256")  # invalid IP
        self.assertIsNone(result)
