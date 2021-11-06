from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import requests

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# NASA Mars News Site Web Scraper
def mars_news(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title  = soup.find('div',class_="list_text").get_text()
    news_p = soup.find('div',class_="article_teaser_body").get_text()
    return news_title, news_p
    
#Mars Space Images - Featured Image
def featured_image(browser):
    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)
    full_image_button = browser.find_by_id("headerimage")
    full_image_button.click()
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
    img_result = image_soup.find('img',class_='headerimage')
    image_url=image['src']
    featured_image_url = f"https://spaceimages-mars.com/{image_url}"
    return img_url

# Mars Facts Web Scraper
def mars_facts():
    df = pd.read_html("https://galaxyfacts-mars.com/")[0]
    df.columns=["Description", "Value"]
    df.set_index("Description", inplace=True)

    return df.to_html(classes="table table-striped")

# Mars Hemispheres Web Scraper
def hemisphere(browser):
    url = "https://marshemispheres.com/"
    browser.visit(url)
    hemisphere_image_urls = []
    hemisphere_html = browser.html
    soup = BeautifulSoup(hemisphere_html,'html.parser')
    items = soup.find_all("div", class_="item")

    main_url = "https://marshemispheres.com/"

    for item in items:
        hemisphere_urls.append(f"{main_url}{item.find('a', class_='itemLink')['href']}")
        
    return hemisphere_urls

def scrape_hem(hemisphere_html):
    hemisphere_image_urls=[]
    
    for url in hemisphere_urls:
        browser.visit(url)
        hemisphere_html = browser.html
        soup = BeautifulSoup(hemisphere_html,'html.parser')
        img_url = soup.find('img', class_="wide-image")['src']
        title = soup.find('h2', class_="title").text
        hemisphere_image_urls.append({"title":title,"img_url":f"https://marshemispheres.com/{img_url}"})
        return hemisphere_image_urls
    

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = mars_news(browser)
    img_url = featured_image(browser)
    
    facts = mars_facts()
    hemisphere_image_urls = hemisphere(browser)
    data={
        "news_title":news_title,
        "news_para":news_p,
        "featured_image":img_url,
        "facts":facts,
        "hemispheres":hemisphere_image_urls
    }
   
    return data


if __name__ == "__main__":
    print(scrape_all())
      
    
    

           
        
            
       
    
    
    



    
    
    
            
    
    
   

