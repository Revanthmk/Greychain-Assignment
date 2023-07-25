from flask import Flask, request, jsonify
# importing the created scraper
from web_scraper import Scraper

# Creating the app
app = Flask(__name__)
scraper = Scraper() # Creating the instance

# Defining route for the /scrape end point
@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url'] # Getting url from the payload
    scraper.scrape(url) # Running the scrape function
    return jsonify({'message': 'Done'.format(url)}) # Return a JSON file saying that is scraping is done

# Defining route for the /search end point
@app.route('/search', methods=['POST'])
def search():
    search_text = request.json['search_text']# Getting search_text from the payload
    results = scraper.search(search_text)# Running the search function
    return jsonify({'results': results})# Return a JSON file showing the results

if __name__ == '__main__':
    app.run()