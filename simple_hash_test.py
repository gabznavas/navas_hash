import unittest

from simple_hash import SimpleHash 

class TestSimpleHash(unittest.TestCase):
    def test_length(self):
        testcases = [{
            "param": b'hello world',
            "expected_len": 32 
        }]
        
        for testcase in testcases:
            s = SimpleHash()
            hash_ = s.execute(testcase.get('param'))
            self.assertEqual(len(hash_), testcase.get('expected_len'))


if __name__ == '__main__':
    unittest.main()