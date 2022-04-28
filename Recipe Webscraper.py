import requests
from bs4 import BeautifulSoup
import pandas as pd

#Base URL that we're working with
baseurl = 'https://damndelicious.net/'

#Header variable has a user agent. THis is needed to prevent your IP address from being blocked for sending so many http requests
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36'
}

#Requests from summer page and iterates through all 2 pages. Looks for all recipes with a div tag and corresponding class name
productlinks = []
for x in range(1,2):
    r = requests.get(f'https://damndelicious.net/category/summer/page/{x}/')
   
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('div', class_='archives')


#Looks for each individual recipes href tag to look for its specific servings,preptime,etc
    for item in productlist:
        for link in item.find_all('a',href=True):
        
            productlinks.append(baseurl + link['href'])




#Items are then scraped and put into a list. 
dinnerlist = []
for link in productlinks:
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')
    recipename =  soup.find('h1', class_='post-title')
    Image = soup.find('img',class_='photo nopin' )
    servings = soup.select_one(".post-meta.time p:nth-child(1) span")
    preptime = soup.select_one(".post-meta.time p:nth-child(2) span")
    UrlLinks = soup.find('a',href=True)
   

    dictionary = {
        'recipe name':recipename,
        'recipe image':Image,
        'serving size':servings,
        'prep time':preptime,
        'UrlLinks':link,
    }
#We then place this into a dictionary to save our info.  
    dinnerlist.append(dictionary)
    
df = pd.DataFrame(dinnerlist)

#Prints the first 15 scraped entries from our dataframe
#print(df.head(15))

#Can specifically print certain columns
#print(recipename,'\n',servings,'\n',preptime)

#The following can convert the dataframe into an HTML table, then prints the results
# result = df.to_html()
# print(result)


#The following can convert the dataframe into a csv file. Very useful for uploading to MYSQL and creating a database table.
#df.to_csv('summer.csv')
#df_saved_file = pd.read_csv('summer.csv')
#df_saved_file