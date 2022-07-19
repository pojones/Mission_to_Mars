#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# import dependencies; 'browser' instance from 'splinter', the 'BeautifulSoup' object, and the driver object for chrome


# In[5]:


executable_path = {'executable_path': ChromeDriverManager().install()}
# creates an instance of a Splinter browser
browser = Browser('chrome', **executable_path, headless=False)
# specifies that we are using chrome as the browser, '**executable_path' unpacks the dictionary we've stored the path in,
# 'headless=False' means all the browser's actions will be displayed in a chrome window


# In[6]:


#* Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#* Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# search for elements with specific combination of tag 'div' and attribute 'list_text'. We're also telling our browser to
# wait one second before searching for components. Optional delay is useful when dynamic pages take a while to load


# In[7]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# notice 'slide_elem' is the variable assigned to look for the '<div />' tag and its descendants? This is our parent element
# meaning it holds all other elements within it, and we'll reference it when we want to filter search results even further.
# The '.' is used for selecting classes, such as 'list_text'


# In[8]:


slide_elem.find('div', class_='content_title')
# here, we chain 'find()' on to the previously assigned variable 'slide_elem', specifying a search in the variable for the 
# specific data in a '<div />' with class 'content_title'


# In[9]:


#* Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[11]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[14]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[17]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
# create a new dataframe from the html table. 'read_html' specifically searches for and returns a list of tables found in
# the html. By specifying index '0', we tell pandas to pull only the first table it encounters, or the first item in the 
# list. Then it turns that table into a dataframe
df.columns=['description', 'Mars', 'Earth']
# assign columns to the dataframe for additional clarity
df.set_index('description', inplace=True)
# by using the 'set_index()' function, we turn the 'description' column into the dataframe's index. 'inplace=True' means
# the updated index will remain in place without having to reassign the dataframe to a new variable
df


# In[18]:


df.to_html()
# use pandas to easily convert the dataframe into html-friendly form


# In[19]:


browser.quit()


# In[ ]:




