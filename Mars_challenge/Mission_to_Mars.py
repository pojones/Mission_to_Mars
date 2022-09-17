{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a0ce30e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from selenium import webdriver\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd\n",
    "# import dependencies; 'browser' instance from 'splinter', the 'BeautifulSoup' object, and the driver object for chrome"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "991b0c9c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "# creates an instance of a Splinter browser\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "# specifies that we are using chrome as the browser, '**executable_path' unpacks the dictionary we've stored the path in,\n",
    "# 'headless=False' means all the browser's actions will be displayed in a chrome window"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "491f17e0",
   "metadata": {},
   "source": [
    "### Visit the Mars Nasa News Site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "380a24df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "\n",
    "#* Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "# search for elements with specific combination of tag 'div' and attribute 'list_text'. We're also telling our browser to\n",
    "# wait one second before searching for components. Optional delay is useful when dynamic pages take a while to load"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5a7ad3d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')\n",
    "# notice 'slide_elem' is the variable assigned to look for the '<div />' tag and its descendants? This is our parent element\n",
    "# meaning it holds all other elements within it, and we'll reference it when we want to filter search results even further.\n",
    "# The '.' is used for selecting classes, such as 'list_text'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8e261a81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">NASA's Curiosity Keeps Rolling As Team Operates Rover From Home</div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find('div', class_='content_title')\n",
    "# here, we chain 'find()' on to the previously assigned variable 'slide_elem', specifying a search in the variable for the \n",
    "# specific data in a '<div />' with class 'content_title'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ba46440f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Curiosity Keeps Rolling As Team Operates Rover From Home\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#* Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "65e306e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The team has learned to meet new challenges as they work remotely on the Mars mission.'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "128186b1",
   "metadata": {},
   "source": [
    "### JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c72870d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4cf39d9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3e1785a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<html class=\"fancybox-margin fancybox-lock\"><head>\n",
       "<meta charset=\"utf-8\"/>\n",
       "<meta content=\"width=device-width, initial-scale=1\" name=\"viewport\"/>\n",
       "<link href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" rel=\"stylesheet\"/>\n",
       "<!-- <link rel=\"stylesheet\" type=\"text/css\" href=\"css/font.css\"> -->\n",
       "<link href=\"css/app.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<link href=\"https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<title>Space Image</title>\n",
       "<style type=\"text/css\">.fancybox-margin{margin-right:17px;}</style></head>\n",
       "<body>\n",
       "<div class=\"header\">\n",
       "<nav class=\"navbar navbar-expand-lg\">\n",
       "<a class=\"navbar-brand\" href=\"#\"><img id=\"logo\" src=\"image/nasa.png\"/><span class=\"logo\">Jet Propulsion Laboratory</span>\n",
       "<span class=\"logo1\">California Institute of Technology</span></a>\n",
       "<button aria-controls=\"navbarNav\" aria-expanded=\"false\" aria-label=\"Toggle navigation\" class=\"navbar-toggler\" data-target=\"#navbarNav\" data-toggle=\"collapse\" type=\"button\">\n",
       "<span class=\"navbar-toggler-icon\"></span>\n",
       "</button>\n",
       "<div class=\"collapse navbar-collapse justify-content-end\" id=\"navbarNav\">\n",
       "<ul class=\"navbar-nav\">\n",
       "<li class=\"nav-item active\">\n",
       "<a class=\"nav-link\" href=\"#\"><i aria-hidden=\"true\" class=\"fa fa-bars\"></i>   MENU   <i aria-hidden=\"true\" class=\"fa fa-search\"></i></a>\n",
       "</li>\n",
       "</ul>\n",
       "</div>\n",
       "</nav>\n",
       "<div class=\"floating_text_area\">\n",
       "<h2 class=\"brand_title\">FEATURED IMAGE</h2>\n",
       "<h1 class=\"media_feature_title\">Dusty Space Cloud</h1>\n",
       "<br/>\n",
       "<a class=\"showimg fancybox-thumbs\" href=\"image/featured/mars1.jpg\" target=\"_blank\"> <button class=\"btn btn-outline-light\"> FULL IMAGE</button></a>\n",
       "</div>\n",
       "<img class=\"headerimage fade-in\" src=\"image/featured/mars1.jpg\"/></div>\n",
       "<div class=\"search sticky\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<input name=\"Search\" placeholder=\"Search\" type=\"text\"/>\n",
       "</div>\n",
       "<div class=\"col-md-6\">\n",
       "<select aria-label=\"Default select example\" class=\"form-select\" id=\"options\">\n",
       "<option onchange=\"0\" selected=\"\">Mars</option>\n",
       "<!-- <option data-filter=\"sun\" class=\"button\">Mars</option> -->\n",
       "<option class=\"button\" data-filter=\"Sun\">Sun</option>\n",
       "<option class=\"button\" data-filter=\"earth\">Earth</option>\n",
       "<option class=\"button\" data-filter=\"ida\">Ida</option>\n",
       "<option class=\"button\" data-filter=\"jupiter\">Jupiter</option>\n",
       "<option class=\"button\" data-filter=\"venus\">Venus</option>\n",
       "</select>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"container mt-5\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<h1>Images</h1>\n",
       "</div>\n",
       "<div class=\"col-md-6\" id=\"icon\">\n",
       "<div class=\"icon2\"></div>\n",
       "<div class=\"icon1\"></div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!-- first div -->\n",
       "<div class=\"div1\" id=\"filter\">\n",
       "<div class=\"thmbgroup\"><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae7</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 31, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">December 31, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 29, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes 7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes 7.jpg\"/><p class=\"thumbcontent\">December 28, 2020<br/>roctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae7.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae7.jpg\"/><p class=\"thumbcontent\">December 22, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">December 21, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">December 18, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">December 17, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes.jpg\"/><p class=\"thumbcontent\">December 16, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">December 15, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">December 11, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Sirenum Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Sirenum Fossae.jpg\"/><p class=\"thumbcontent\">November,11, 2020<br/>Sirenum Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">November,13, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">November,14, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">November,17, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles3.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles3.jpg\"/><p class=\"thumbcontent\">November,11, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Atlantis Chaos.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Atlantis Chaos.jpg\"/><p class=\"thumbcontent\">November,09, 2020<br/>Atlantis Chaos</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Proctor Crater Dunes.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Proctor Crater Dunes.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Proctor Crater Dunes</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Reull Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Reull Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Reull Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles3.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles3.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Sirenum Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Sirenum Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Sirenum Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Niger Vallis.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Niger Vallis.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Niger Vallis</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Icaria Fossae.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Icaria Fossae.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Icaria Fossae</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Ariadnes Colles4.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Ariadnes Colles4.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Ariadnes Colles</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/South Polar Cap.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/South Polar Cap.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>South Polar Cap</p></div></a><a class=\"fancybox-thumbs\" data-fancybox-group=\"thumb\" href=\"image/mars/Daedalia Planum.jpg\"><div class=\"thmb\"><img alt=\"\" class=\"thumbimg\" src=\"image/mars/Daedalia Planum.jpg\"/><p class=\"thumbcontent\">January 1, 2020<br/>Daedalia Planum</p></div></a></div>\n",
       "</div>\n",
       "<!-- first div ends -->\n",
       "<!-- second div starts -->\n",
       "<div class=\"col-md-12 grid-margin\" id=\"column\">\n",
       "<ul class=\"post-list\">\n",
       "<li class=\"post-heading\"></li>\n",
       "</ul>\n",
       "</div>\n",
       "<!-- second div starts -->\n",
       "</div>\n",
       "<div class=\"first imgcontainer mt-3\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-3\">\n",
       "<img id=\"pic\" src=\"\"/>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!-- end -->\n",
       "<div class=\"module_gallery container\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-6\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://www.jpl.nasa.gov/assets/images/content/tmp/images/jpl_photojournal(3x1).jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<h5 class=\"card-title\">JPL Photojournal</h5>\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-6\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://www.jpl.nasa.gov/assets/images/content/tmp/images/nasa_images(3x1).jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<h5 class=\"card-title\">Great images in NASA</h5>\n",
       "<p class=\"card-text\">A selection of the best-known images from a half-century of exploration and discovery</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"multi_teaser\">\n",
       "<div class=\"container\">\n",
       "<h1>You Might Also Like</h1>\n",
       "<div class=\"col-md-12 mt-5\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA24304---CatScanMars-16-640x350.gif\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/PIA23491-16-640x350.jpg\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"col-md-4\">\n",
       "<div class=\"card\">\n",
       "<img alt=\"Card image cap\" class=\"card-img-top\" src=\"https://imagecache.jpl.nasa.gov/images/640x350/C1-PIA23180-16-640x350.gif\"/>\n",
       "<div class=\"card-body\">\n",
       "<p class=\"card-text\">Access to the full library of publicly released images from various Solar System exploration programs</p>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"footer\">\n",
       "<div class=\"container\">\n",
       "<div class=\"col-md-12\">\n",
       "<div class=\"row\">\n",
       "<div class=\"col-md-3\">\n",
       "<h4>About JPL</h4>\n",
       "<ul>\n",
       "<li>About JPL</li>\n",
       "<li>JPL Vision</li>\n",
       "<li>Executive Council</li>\n",
       "<li>History</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Education</h4>\n",
       "<ul>\n",
       "<li>Intern</li>\n",
       "<li>Learn</li>\n",
       "<li>Teach</li>\n",
       "<li>News</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Our Sites</h4>\n",
       "<ul>\n",
       "<li>Asteroid Watch</li>\n",
       "<li>Basics of Spaceflight</li>\n",
       "<li>Cassini - Mission to Saturn</li>\n",
       "<li>Climate Kids</li>\n",
       "</ul>\n",
       "</div>\n",
       "<div class=\"col-md-3\">\n",
       "<h4>Galleries</h4>\n",
       "<ul>\n",
       "<li>JPL Space Images</li>\n",
       "<li>Videos</li>\n",
       "<li>Infographics</li>\n",
       "<li>Photojournal</li>\n",
       "</ul>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<!--<div class=\"showFullimage\">\n",
       "\t<button class=\"btn btn-outline-light hideimage\" onclick=hideimage()> Close</button>\n",
       "\t<img class=\"fullimage fade-in\" src=\"\">\n",
       "</div>-->\n",
       "<!-- <script src=\"js/jquery.easeScroll.js\"></script>  -->\n",
       "<script src=\"js/jquery-3.5.1.min.js\"></script>\n",
       "<!-- <script src=\"js/jquery-3.2.1.slim.min.js\"></script> -->\n",
       "<script src=\"js/demo.js\"></script>\n",
       "<!-- <script src=\"js/app.js\"></script> -->\n",
       "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\"></script>\n",
       "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\"></script>\n",
       "<script src=\"js/fancyBox/jquery.fancybox.pack.js?v=2.1.5\" type=\"text/javascript\"></script>\n",
       "<link href=\"js/fancyBox/jquery.fancybox.css?v=2.1.5\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<link href=\"js/fancyBox/helpers/jquery.fancybox-thumbs.css?v=1.0.7\" rel=\"stylesheet\" type=\"text/css\"/>\n",
       "<script src=\"js/fancyBox/helpers/jquery.fancybox-thumbs.js?v=1.0.7\" type=\"text/javascript\"></script>\n",
       "<div class=\"fancybox-overlay fancybox-overlay-fixed\" style=\"width: auto; height: auto; display: block;\"><div class=\"fancybox-wrap fancybox-desktop fancybox-type-image fancybox-opened\" style=\"width: 670px; height: auto; position: absolute; top: 273px; left: 105px; opacity: 1; overflow: visible;\" tabindex=\"-1\"><div class=\"fancybox-skin\" style=\"padding: 15px; width: auto; height: auto;\"><div class=\"fancybox-outer\"><div class=\"fancybox-inner\" style=\"overflow: visible; width: 640px; height: 350px;\"><img alt=\"\" class=\"fancybox-image\" src=\"image/featured/mars1.jpg\"/></div></div><a class=\"fancybox-item fancybox-close\" href=\"javascript:;\" title=\"Close\"></a></div></div></div></body></html>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')\n",
    "img_soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "de95acae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "88aa797d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "233401ff",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "207437b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "# create a new dataframe from the html table. 'read_html' specifically searches for and returns a list of tables found in\n",
    "# the html. By specifying index '0', we tell pandas to pull only the first table it encounters, or the first item in the \n",
    "# list. Then it turns that table into a dataframe\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "# assign columns to the dataframe for additional clarity\n",
    "df.set_index('description', inplace=True)\n",
    "# by using the 'set_index()' function, we turn the 'description' column into the dataframe's index. 'inplace=True' means\n",
    "# the updated index will remain in place without having to reassign the dataframe to a new variable\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "77d0d41b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()\n",
    "# use pandas to easily convert the dataframe into html-friendly form"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1436f828",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a535d44",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cdc0e442",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1675aaeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "# parse the resulting html with soup\n",
    "html = browser.html\n",
    "hemi_soup = soup(html, 'html.parser')\n",
    "\n",
    "# Get the links for each of the 4 hemispheres\n",
    "hemi_links = hemi_soup.find_all('h3')\n",
    "\n",
    "for hemi in hemi_links:\n",
    "    # Navigate and click the link of the hemisphere\n",
    "    img_page = browser.find_by_text(hemi.text)\n",
    "    img_page.click()\n",
    "    html= browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "    # Scrape the image link\n",
    "    img_url = 'https://astrogeology.usgs.gov/' + str(img_soup.find('img', class_='wide-image')['src'])\n",
    "    # Scrape the title\n",
    "    title = img_soup.find('h2', class_='title').text\n",
    "    # Define and append to the dictionary\n",
    "    hemi_dict = {'img_url': img_url,'title': title}\n",
    "    hemisphere_image_urls.append(hemi_dict)\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "198ce351",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://astrogeology.usgs.gov//cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2496d24e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ce88181",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}