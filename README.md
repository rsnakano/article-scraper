# Article Scraper

Neat little web scraper to get text from sites. Made with BeautifulSoup 4 and Python. 

## Note

This is a very simple web scraper that was hacked together in a couple of hours and will get the all of the p tags of the whole site html so 
other non-article content might be scraped as well.

## How to Use

Clone the repo, install the dependencies, run the `.py` file, paste the URL, and the scraper will generate an `article.html` file that your browser can 
render free from restrictions.

Alternatively, the terminal will also display the text with minimal formatting, but certain text enclosed in other tags (a tags, most likely) may not appear,
so it isn't recommended to use over the article.html file. 
