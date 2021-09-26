import requests as re
from bs4 import BeautifulSoup

# Create empty list to contain collected URLs

recipes_links = []

# Collect recipes URLs

for i in range(2,51):
    params = '?page=' + str(i) + '&sort=Title'
    page_url = 'https://www.allrecipes.com/recipes/' + params
    page = re.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a', class_='tout__titleLink', href = True)
   
    # Filter links to return only those leaeding to particular recipes
    for link in links:
        if '/recipe/' in link.get('href'):
            recipe_link = 'https://www.allrecipes.com/' + link.get('href')
            recipes_links.append(recipe_link)

# Write recipes urls into file
with open('recipes_urls.txt', 'w') as opened_file:
    for element in recipes_links:    
        opened_file.write(element + '\n')