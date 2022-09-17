#* import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
# import dependencies; 'browser' instance from 'splinter', the 'BeautifulSoup' object, and the driver object for chrome

#* Initiate headless driver for deployment
def scrape_all():
    #* set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    # creates an instance of a Splinter browser
    browser = Browser('chrome', **executable_path, headless=True)
    # specifies that we are using chrome as the browser, '**executable_path' unpacks the dictionary we've stored the path in,
    # 'headless=False' means all the browser's actions will be displayed in a chrome window

    news_title, news_paragraph = mars_news(browser)
    # set the 'news_title' and 'news_paragraph' browser

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "hemispheres": hemispheres(browser)}

    browser.quit()
    return data

def mars_news(browser):
    #* Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    #* Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    # search for elements with specific combination of tag 'div' and attribute 'list_text'. We're also telling our browser to
    # wait one second before searching for components. Optional delay is useful when dynamic pages take a while to load

    #* convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # notice 'slide_elem' is the variable assigned to look for the '<div />' tag and its descendants? This is our parent element
        # meaning it holds all other elements within it, and we'll reference it when we want to filter search results even further.
        # The '.' is used for selecting classes, such as 'list_text'
        #slide_elem.find('div', class_='content_title')
        # here, we chain 'find()' on to the previously assigned variable 'slide_elem', specifying a search in the variable for the 
        # specific data in a '<div />' with class 'content_title'

        #* Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        #* Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return news_title, news_p

def featured_image(browser):
    #* Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    #* Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    try:       
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    try:
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
        # create a new dataframe from the html table. 'read_html' specifically searches for and returns a list of tables found in
        # the html. By specifying index '0', we tell pandas to pull only the first table it encounters, or the first item in the 
        # list. Then it turns that table into a dataframe
    except BaseException:
        return None

    df.columns=['Description', 'Mars', 'Earth']
    # assign columns to the dataframe for additional clarity
    df.set_index('Description', inplace=True)
    # by using the 'set_index()' function, we turn the 'description' column into the dataframe's index. 'inplace=True' means
    # the updated index will remain in place without having to reassign the dataframe to a new variable

    return df.to_html(classes="table table-striped")
    # use pandas to easily convert the dataframe into html-friendly form

def hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    # visit url

    hemisphere_image_urls = []
    # create a list for hemisphere image urls

    for i in range(4):
        #browser.find_by_css('a.product-item h3')[i].click()
        #element = browser.links.find_by_text('Sample').first
        #img_url = element['href']
        #title = browser.find_by_css("h2.title").text

        # visit the initial site
        html = browser.html
        img_soup = soup(html, 'html.parser')

        # grab the link at range number
        img_box = img_soup.find('div', class_='collapsible results').find_all('div', class_='item')
        image_link = img_box[i].find('a').get('href')
        image_title = img_box[i].find('h3').text

        # visit the new link
        new_img_url_href = url + image_link
        browser.visit(new_img_url_href)
        html = browser.html
        img_soup = soup(html, 'html.parser')

        # grab the href for the jpg
        new_img_url = img_soup.find('div', class_='downloads').find('a').get('href')
        img_url = url + new_img_url

        hemispheres = {}
        hemispheres["img_url"] = img_url
        hemispheres["title"] = image_title
        hemisphere_image_urls.append(hemispheres)
        browser.back()
    return hemisphere_image_urls

if __name__=="__main__":
# if running as a script
    print(scrape_all)
    # print scraped data