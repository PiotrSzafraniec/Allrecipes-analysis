# Allrecipes analysis

The aim of the project is to show a simple process of cleaning data scraped from the internet, necessary for further analysis.

Allrecipes scraper directory contains the following:
- allrecipes_url_scraper.py - used to scrape the list of URLs, later used for scraping data in allrecipes_recipe_scraper.py
- allrecipes_recipe_scraper.py - proper scraper used to collect data about recipes from www.allrecipes.com
- data.json - data collected through scraping process

Allrecipes analysis - part 1 preparing data directory contains the following:
- data.json - data collected with use of allrecipes_recipe_scraper.py - it is the starting point of the project
- herbs_britannica.txt - file containing list of herbs collected from Encyclopedia Britannica
- Allrecipes analysis - part 1 preparing data.ipynb - Jupyter Notebook file containing the actual analysis and data cleaning process
- allrecipes_data.csv - exported data after the cleaning process

In part 2 of the project we will be concentrating on exploratory analysis of the data resulting from part 1 - allrecipes_data.csv.
