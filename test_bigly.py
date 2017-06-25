import unittest

import bigly

class clean_link_Tests(unittest.TestCase):
    def test_leaves_basic_links_alone(self):
        basic_link = 'http://httpbin.org/redirect/3'
        cleaned_link = bigly.clean_link(basic_link)
        self.assertEqual(basic_link, cleaned_link)

class make_absolute_Tests(unittest.TestCase):
    def test_leaves_absolute_links_alone(self):
        absolute_link = 'http://httpbin.org/redirect/2'
        link_made_absolute = bigly.make_absolute('http://bit.ly/2sabOld', absolute_link)
        self.assertEqual(absolute_link, link_made_absolute)

    def test_converts_relative_links_to_absolute_links(self):
        relative_link = '/relative-redirect/2'
        link_made_absolute = bigly.make_absolute('http://httpbin.org/redirect/3', relative_link)
        self.assertEqual('http://httpbin.org/relative-redirect/2', link_made_absolute)

unittest.main()
