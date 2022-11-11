import os
import unittest

import xml.etree.ElementTree as ET


XMLTV_FILEPATH = os.path.join(os.path.dirname(__file__), 'milwaukee.xmltv')


class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        #  with open(XMLTV_FILEPATH) as f:
        #      print(f.read())
        tree = ET.parse(XMLTV_FILEPATH)
        root = tree.getroot()
        print(root)


if __name__ == '__main__':
    unittest.main()
