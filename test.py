import unittest
from web_scraper import Scraper

class TestWebScraper(unittest.TestCase): # define a class that inherits from unittest.TestCase
    def test_scrape(self): # Test method for scrape class from Scraper
        url = 'https://blog.hubspot.com/website/simple-website-examples'
        scraper = Scraper() # Creating the instance
        scraper.web_scrape(url) # call the web_scrape method from the instance
        self.assertIn(url, scraper.web_text) # check if the url is present in web_text attribute in the instance
        self.assertGreater(len(scraper.data[url]), 0) # check if the length og the data for given URL is greater than 0

    def test_search(self):
        url = 'https://blog.hubspot.com/website/simple-website-examples' 
        search_text = 'Cocokind'
        scraper = Scraper() # Creating a new instance
        scraper.web_scrape(url) # Calling the web_scrape method of the instance
        results = scraper.search(search_text) # Calling the search method of the instance
        self.assertIsInstance(results, list) # Checking if the results are a list
        for result in results:
            self.assertIn(search_text, scraper.data[result]) # Checking if the search_text is in the data for the result

if __name__ == '__main__':
    unittest.main()