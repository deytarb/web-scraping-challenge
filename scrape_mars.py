# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests
import lxml
import os

#define browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# Mars Recent News
def scrape():

    mars_data = {}

    URL="https://redplanetscience.com/"
    browser.visit(URL)
    html= browser.html
    soup= BeautifulSoup(html,"html.parser")
    listtext= soup.find(class_='list_text')
    News_title= listtext.find(class_="content_title").get_text()
    News_summary= listtext.find(class_="article_teaser_body").get_text()

    mars_data["News_title"] = News_title
    mars_data["News_summary"] = News_summary

    time.sleep(1)

# JPL Mars Space Images

    URL="https://spaceimages-mars.com/"
    browser.visit(URL)
    html= browser.html
    soup2= BeautifulSoup(html,"html.parser")
    listtext= soup2.find_all('img')[1]["src"]

    img_url = URL + listtext

    mars_data["img_url"] = img_url

    time.sleep(1)

# Mars Hemisphere Images
    table = pd.read_html('https://galaxyfacts-mars.com/')
    print(table[0])
    df = table[0]
    renamed_df = df.rename(columns={0: 'Feature', 1: 'Mars', 2: 'Earth'})
    renamed_df.head(9)
    df = renamed_df.set_index("Feature", inplace=False)
    df.head(9)
    df.to_html(classes="mars_information")

# Mars Hemisphere Images
    Cerberus = "https://marshemispheres.com/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"
    Schiaparelli = "https://marshemispheres.com/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"
    Syrtis = "https://marshemispheres.com/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"
    Valles = "https://marshemispheres.com/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": Cerberus},
        {"title": "Schiaparelli Hemisphere", "img_url": Schiaparelli},
        {"title": "Syrtis Major Hemisphere", "img_url": Syrtis},
        {"title": "Valles Marineris Hemisphere", "img_url": Valles}, 
    ]
    mars_data["hemisphere_images"] = hemisphere_image_urls

    # Return the dictionary
    return mars_data





