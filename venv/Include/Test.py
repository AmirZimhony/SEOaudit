from bs4 import BeautifulSoup
import requests
import unittest


#define website for testing an turn it into BS object
base_site = "https://www.nytimes.com"
response = requests.get(base_site)
html = response.content
soup = BeautifulSoup(html, "html.parser")



class TestFunctions(unittest.TestCase):

    def TestSSimple(self):
        a=5
        result=a*2
        self.assertEqual(result,10)

if __name__ == '__main__':
    unittest.main()