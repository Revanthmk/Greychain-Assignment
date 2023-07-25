import requests
from bs4 import BeautifulSoup # Python library to scrape the web
import re

class Scraper:
  def __init__(self):
    self.web_text = {}

  def web_scrape(self, url):
    each_page = requests.get(url) # Searching and getting the page from the URL
    soup = BeautifulSoup(each_page.content, 'html.parser') # Getting all the content from the url through Beautiful Soup
    self.web_text[url] = soup.get_text() # Getting all the text from the page
    all_links = soup.find_all('a', href=True) # Finding all links from the page
    for each_link in all_links: # Looping through each link and running the same function in a recursive manner to get all pages and subpages
      href = each_link['href']
      if href.startswith('http'): # Getting just the links
        url = href
        self.web_scrape()
  
  def search(self, search_text): 
    findings = [] 
    for url, web_text in self.web_text.items(): # getting text from the stored dictionary
      if re.search(search_text, web_text): # Searching for the search_text in the web_page
        findings.append(url) # Adding it to the findings list
    return findings