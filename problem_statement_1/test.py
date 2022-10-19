import unittest

from app import main
class Test(unittest.TestCase):
    def test_case1(self):
        """
        Sample Basec Case, Checking the log data and giving the top 3 food menu items id
        """
        url = "logfiles/testcase1.log"
        result = main.func(url)
        self.assertEqual(result, "menuid4, menuid1, menuid3")
    def test_case2(self):
        """
        Sample Case in which there are repeated data in the log file
        """
        url = "logfiles/testcase2.log"
        result = main.func(url)
        self.assertEqual(result, "Error: Repeated Data")
    def test_case3(self):
        """
        Sample test case with more that 250 logs
        """
        url = "logfiles/testcase3.log"
        result = main.func(url)
        self.assertEqual(result, "menuid2, menuid3, menuid6")
    def test_case4(self):
        """
        Sample Case in which there are semi-repeated data i.e. the eater_id is same but menuid is different in the log file
        """
        url = "logfiles/testcase4.log"
        result = main.func(url)
        self.assertEqual(result, "menuid4, menuid1, menuid3")

if __name__ == '__main__':
    unittest.main()