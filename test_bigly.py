import unittest

import bigly

class clean_link_Tests(unittest.TestCase):
    def test_leaves_basic_links_alone(self):
        basic_link = 'http://httpbin.org/redirect/3'
        cleaned_link = bigly.clean_link(basic_link)
        self.assertEqual(basic_link, cleaned_link)

unittest.main()
