import requests as re
from bs4 import BeautifulSoup
import json    

# Import allrecipes urls from external file

with open("recipes_urls.txt", "r") as recipes_urls:
    recipes_urls_string = recipes_urls.read()
    urls_list = recipes_urls_string.split("\n")

# Create a proper list of urls to iterate over and limit it to 1000 first urls

urls_list = [element.strip() for element in urls_list]
urls_list = urls_list[:-1]
urls_list = urls_list[:1000]

dict_list = {}
recipes_dictionary = {}

# Iterate over list of urls to use for recipe data scraping

recipe_id = 0

for url_num in range(len(urls_list)):
    recipe_id += 1
    url = urls_list[url_num] 
    page = re.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    dict_name = {'name': soup.find('h1', {'class' : 'headline heading-content'}).text}
    
    
    # Dictionaries of preparation time and number of servings
    
    mydivs = soup.find_all('div', class_='recipe-meta-item')
    
    
    recipe_info_container = soup.find_all('div', class_='recipe-info-section')
    recipe_info_section = recipe_info_container[0].find_all(class_ = 'recipe-meta-container two-subcol-content clearfix')
    recipe_info_section_selected = recipe_info_section[0].find_all(class_ = 'two-subcol-content-wrapper')
    
        
    prep_time_keys = recipe_info_section_selected[0].find_all(class_ = 'recipe-meta-item-header')
    prep_time_values = recipe_info_section_selected[0].find_all(class_ = 'recipe-meta-item-body')
    
    servings_keys = recipe_info_section_selected[1].find_all(class_ = 'recipe-meta-item-header')
    servings_values = recipe_info_section_selected[1].find_all(class_ = 'recipe-meta-item-body')    
         
    dict_of_prep_time = {}
    dict_of_servings = {}
    
    for i in range(len(prep_time_keys)):
        dict_of_prep_time[prep_time_keys[i].text.strip()] = prep_time_values[i].text.strip()
        
    for i in range(len(servings_keys)):   
        dict_of_servings[servings_keys[i].text.strip()] = servings_values[i].text.strip()
    
    # Ingredients 
    
    li_ingr = soup.find_all('ul', {'class': 'ingredients-section'})[0].find_all('li', {'class': 'ingredients-item'})
    
    ingredients_list = []
    for li in li_ingr:
        ingredients_list.append(li.text.strip())
    
    ingredients_string = ",".join(ingredients_list)
    
    # Nutrition information
    dict_nutrition_info = {}
    try:
        nutrition = soup.find_all(class_ = 'partial recipe-nutrition-section')
        nutrition_info = nutrition[0].find_all(class_ = 'section-body')[0].text.strip()
        dict_nutrition_info['nutrition'] = nutrition_info
    except:
        dict_nutrition_info['nutrition'] = None
  
    # Rating
    
    try:
        rating_count = soup.find_all('span', {'class' : 'rating-count'})
        rating_count[0].text.strip()
        dict_ratings = {'5 stars': rating_count[0].text.strip(),
                        '4 stars': rating_count[1].text.strip(), 
                        '3 stars': rating_count[2].text.strip(), 
                        '2 stars': rating_count[3].text.strip(),
                        '1 stars': rating_count[4].text.strip()}
    except:
        dict_ratings = {'5 stars': None,
                        '4 stars': None, 
                        '3 stars': None, 
                        '2 stars': None,
                        '1 stars': None}
    
    # Merge data info one dictionary
    
    recipe_dict = {**dict_name, **dict_of_prep_time, **dict_of_servings, **dict_ratings, **dict_nutrition_info, 'ingredients': ingredients_string}
    
    # Append information to dictionary containing information about all recipes
    
    recipes_dictionary[recipe_id] = recipe_dict
          
# Save data in JSON format
 
with open("data.json", "w") as json_data:
    json.dump(recipes_dictionary, json_data)

    

