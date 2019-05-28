#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup as bs 
from splinter import Browser
import requests


# In[7]:


executable_path = {'executable_path': './Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
response = requests.get(url)


# In[13]:


soup = bs(response.text, 'html.parser') 


# In[14]:


print(soup.prettify()) 


# In[101]:


executable_path = {'executable_path': './Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[102]:


#Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[103]:


#Title
title = soup.find_all('div', class_='content_title')
news_title=title[0].text.strip()

#Paragraph
results_paragraph = soup.find_all('div', class_="rollover_description_inner") 
news_paragraph= results_paragraph[0].text.strip()

print(news_title)
print(news_paragraph)


# In[107]:


executable_path = {'executable_path': './Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[108]:


#Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
img = soup.find('img')

#Make sure to save a complete url string for this image.

featured_image_url =url + img['src']
print(featured_image_url)


# In[109]:


executable_path = {'executable_path': './Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[125]:


#Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
tweet = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

#Save the tweet text for the weather report as a variable called mars_weather.

mars_weather=tweet[0].text
print(mars_weather)


# In[126]:


import pandas as pd


# In[189]:


#Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
url = 'https://space-facts.com/mars/' 
ptable = pd.read_html(url)
ptable[0]


# In[208]:


newdftable= pd.DataFrame({'Equatorial Diameter':['6,792 km'], 'Polar Diameter':['6,752 km'],'Mass':['6.42 x 10^23 kg (10.7% Earth)'], 'Moons':['2 (Phobos & Deimos)'],'Orbit Distance':['227,943,824 km (1.52 AU)'], 'Orbit Period':['687 days (1.9 years)'],'Surface Temperature':['-153 to 20 °C'],'First Reccord':['2nd millennium BC'],'Recorded by':['Egyptian astronomers']})


# In[210]:


#Use Pandas to convert the data to a HTML table string.
html_table = newdftable.to_html()
html_table


# In[211]:


executable_path = {'executable_path': './Desktop/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[228]:


url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
html = browser.html
soup = bs(html, 'html.parser')
title_h = soup.find('div', class_='description')


# In[229]:


print(title_h)

