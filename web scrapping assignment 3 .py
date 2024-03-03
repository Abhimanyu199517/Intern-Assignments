#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system(' pip install selenium')


# In[4]:





# In[16]:


#1. Write a python program which searches all the product under a particular product from www.amazon.in. 
#The product to be searched will be taken as input from user. 
#For e.g. If user input is ‘guitar’. Then search for guitars.


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException 

# Opening the browser and navigating to Amazon.in
url = "https://www.amazon.in/"
driver = webdriver.Chrome()
driver.get(url)

# Locating the search bar and entering the search query
search_bar = driver.find_element(By.XPATH, '//input[@type="text"]')
search_bar.send_keys('Guitar')

# Clicking the search button
search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
search_button.click()

# Delay to ensure the page loads properly before further actions
time.sleep(2)

# Further actions can be implemented here, such as scraping the search results


# In[18]:


# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. 
#In case if any product has less than 3 pages in search results then scrape all the products available 
#under that product name. Details to be scraped are: "Brand Name", "Name of the Product", "Price", 
#"Return/Exchange", "Expected Delivery", "Availability" and “Product URL”. 
#In case, if any of the details are missing for any of the product then replace it by “-“.


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException 

# Opening the browser and navigating to Amazon.in
url = "https://www.amazon.in/"
driver = webdriver.Chrome()
driver.get(url)

# Locating the search bar and entering the search query
search_bar = driver.find_element(By.XPATH, '//input[@type="text"]')
search_bar.send_keys('Guitar')

# Clicking the search button
search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
search_button.click()

# Delay to ensure the page loads properly before further actions
time.sleep(2)


# scrape all product urts
product_urls=[] 
start=0
end=3
for page in range(start,end):#for loop for scrapping 3 page
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        product_urls.append(i.get_attribute("href"))
    try:
        nxt_button = driver.find_element(By.XPATH, '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
        nxt_button.click()
        time.sleep(2)
    except NoSuchElementException:  # If there's no next button, break the loop
        break
        
        

# creating empty list
Brand=[]
name_pr=[]
retrn=[]
price=[]
exp_del=[]
avail=[]

for url in product_urls:  # Loop for every product URL in the list
    driver.get(url)
    time.sleep(2)
    
    try:
        brand = driver.find_element(By.XPATH, '//span[@class="a-size-base po-break-word"]')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append("-")
    
    try:
        name = driver.find_element(By.XPATH, '//span[@class="a-size-large product-title-word-break"]')
        name_pr.append(name.text)
    except NoSuchElementException:
        name_pr.append("-")
    
    try:
        prices = driver.find_element(By.XPATH, '//span[@class="a-price-whole"]')
        price.append(prices.text)
    except NoSuchElementException:
        price.append("-")

    try:
        Return = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[3]/div[4]/div[24]/div[2]/div/div/div/div[2]/div/ol/li[3]/div/span/div[2]/span')
        retrn.append(Return.text)
    except NoSuchElementException:
        retrn.append("-")


    try:
        Expected = driver.find_element(By.XPATH, '//span[@class="a-text-bold"]')
        exp_del.append(Expected.text)
    except NoSuchElementException:
        exp_del.append("-")
        
    try:
        Availability = driver.find_element(By.XPATH, '//span[@class="a-size-medium a-color-success"]')
        avail.append(Availability.text)
    except NoSuchElementException:
        avail.append("-")


# Close the WebDriver
driver.quit()


# In[19]:


len(product_urls)


# In[20]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Product Brand':Brand[:30],'Product name':name_pr[:30],'Product price':price[:30],
                 'Return/Exchange':retrn[:30],'Expected Delivery':exp_del[:30],'Availability':avail[:30],
                 'Product URL':product_urls[:30]})
df


# In[ ]:





# In[44]:


#Q3. Write a python program to access the search bar and search button on images.google.com and 
#scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://images.google.com/")
    
# Locate the search bar and enter the keyword
search_bar = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
search_bar.clear()
search_bar.send_keys('fruits')
    
# Click the search button
search_button = driver.find_element(By.XPATH, '//button[@class="Tg7LZd"]')
search_button.click()
    
# Wait for the page to load
time.sleep(2)

images = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
    
# Scrape the URLs of the first 10 images
image_urls = []
for image in images[:10]:
    image_urls.append(image.get_attribute('src'))
    
# Store the image URLs in the dictionary
image_data[keyword] = image_urls

# Close the WebDriver
driver.quit()


# In[45]:


print(image_urls)


# In[46]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Fruit URLs':image_urls[:10]})
df


# In[37]:


# Find the image url for cars

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://images.google.com/")
    
# Locate the search bar and enter the keyword
search_bar = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
search_bar.clear()
search_bar.send_keys('cars')
    
# Click the search button
search_button = driver.find_element(By.XPATH, '//button[@class="Tg7LZd"]')
search_button.click()
    
# Wait for the page to load
time.sleep(2)

cars = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
    
# Scrape the URLs of the first 10 images
cars_urls = []
for car in cars[:10]:
    cars_urls.append(car.get_attribute('src'))
    
# Store the image URLs in the dictionary
image_data[keyword] = cars_urls

# Close the WebDriver
driver.quit()


# In[40]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Cars URLs':cars_urls[:10]})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


# Q4 Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details 
#for all the search results displayed on 1st page. Details to be scraped: 
#“Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,
#“Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. 
#Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_smartphones(search_query):
    base_url = f"https://www.flipkart.com/search?q={search_query}&page=1"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    smartphones = soup.find_all('div', {'class': '_1AtVbE'})

    data = []
    for smartphone in smartphones:
        try:
            brand_name = smartphone.find('div', {'class': '_4rR01T'}).text.strip()
        except:
            brand_name = '-'

        try:
            smartphone_name = smartphone.find('a', {'class': 'IRpwTa'}).text.strip()
        except:
            smartphone_name = '-'

        try:
            color = smartphone.find('a', {'class': '_1W9f5C'}).text.strip()
        except:
            color = '-'

        specs = smartphone.find_all('li', {'class': 'rgWa7D'})
        ram, storage, primary_camera, secondary_camera, display_size, battery_capacity, price = ['-'] * 7
        for spec in specs:
            spec_text = spec.text.strip()
            if 'RAM' in spec_text:
                ram = spec_text
            elif 'ROM' in spec_text:
                storage = spec_text
            elif 'MP' in spec_text:
                if 'Primary' in spec_text:
                    primary_camera = spec_text
                elif 'Secondary' in spec_text:
                    secondary_camera = spec_text
            elif 'cm' in spec_text:
                display_size = spec_text
            elif 'mAh' in spec_text:
                battery_capacity = spec_text
            elif '₹' in spec_text:
                price = spec_text

        try:
            product_url = f"https://www.flipkart.com{smartphone.find('a', {'class': 'IRpwTa'})['href']}"
        except:
            product_url = '-'

        data.append({
            'Brand Name': brand_name,
            'Smartphone Name': smartphone_name,
            'Color': color,
            'RAM': ram,
            'Storage (ROM)': storage,
            'Primary Camera': primary_camera,
            'Secondary Camera': secondary_camera,
            'Display Size': display_size,
            'Battery Capacity': battery_capacity,
            'Price': price,
            'Product URL': product_url
        })

    return data

search_query = input("Enter the smartphone you want to search for on Flipkart: ")
search_results = scrape_flipkart_smartphones(search_query)

df = pd.DataFrame(search_results)
df.to_csv(f"{search_query}_flipkart_smartphones.csv", index=False)
print(df)


# In[21]:


## Q5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

from selenium import webdriver
import time

def get_coordinates(city_name):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps")
    
    # Locate the search bar and enter the city name
    search_bar = driver.find_element_by_id("searchboxinput")
    search_bar.clear()
    search_bar.send_keys('Banglore')
    
    # Click the search button
    search_button = driver.find_element_by_id("searchbox-searchbutton")
    search_button.click()
    
    # Wait for the page to load
    time.sleep(3)
    
    # Get the current URL which contains the coordinates
    try: 
        url_string = driver.current_url
        print("URL Extracted: ", url_string)
        lat_Ing = re.findall(r'@(.*)data' ‚url string)

    
    # Extract the latitude and longitude from the URL
    latitude_longitude = url.split('@')[1].split(',')[0:2]
    latitude = float(latitude_longitude[0])
    longitude = float(latitude_longitude[1])
    
    return latitude, longitude


After searching location on google maps try:
I
url string = driver.current url

then use split function to split lat Ing and will use indexinf to find lat and long separatey.

# Example usage:
city_name = input("Enter the city name: ")
latitude, longitude = get_coordinates(city_name)
print(f"Geospatial coordinates for {city_name}:")
print(f"Latitude: {latitude}, Longitude: {longitude}")


# In[10]:


## Q6. Write a program to scrap all the available details of best gaming laptops from digit.in

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.digit.in/top-products/best-gaming-laptops-40.html")    

url=driver.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]')
for i in url:
       print(i.get_attribute('href'))
        


# In[9]:





# In[52]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Best gaming laptop':best_gaming_laptops})
df


# In[53]:


##Q7.  Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:
##“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.


import requests
from bs4 import BeautifulSoup

def scrape_forbes_billionaires():
    url = 'https://www.forbes.com/billionaires/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    billionaires = []

    for row in soup.select("TableRow_rowContainer__IC1Tv"):
        rank = row.select_one('.rank').text.strip()
        name = row.select_one('.personName').text.strip()
        net_worth = row.select_one('.netWorth').text.strip()
        age = row.select_one('.age').text.strip()
        citizenship = row.select_one('.countryOfCitizenship').text.strip()
        source = row.select_one('.source').text.strip()
        industry = row.select_one('.category').text.strip()

        billionaire = {
            'Rank': rank,
            'Name': name,
            'Net Worth': net_worth,
            'Age': age,
            'Citizenship': citizenship,
            'Source': source,
            'Industry': industry
        }

        billionaires.append(billionaire)

    return billionaires

# Scraping billionaire details
billionaires = scrape_forbes_billionaires()

# Printing the details of billionaires
for billionaire in billionaires:
    print(billionaire)


# In[ ]:


##Q8. Write a program to extract at least 500 Comments, 
##    Comment upvote and time when comment was posted from any YouTube Video.







# In[ ]:


## Q9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall
#. reviews, privates from price, dorms from price, facilities and property description.




# In[55]:





# In[ ]:





# In[11]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless mode, no browser window
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
service = Service('path_to_chrome_driver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the website to scrape
url = "https://www.digit.in/top-products/best-gaming-laptops-40.html"

# Open the website
driver.get(url)

# Wait for the content to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "TopNums")))

# Scrape the page content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all the gaming laptops listed
laptops = soup.find_all('div', class_='TopNums')

# Iterate over each laptop and extract details
for laptop in laptops:
    name = laptop.find('div', class_='TopNums-list-head').text.strip()
    specs = laptop.find('div', class_='TopNums-list-head').find_next_sibling('ul').text.strip()
    price = laptop.find('div', class_='smprc').text.strip()
    print(f"Name: {name}\nSpecifications: {specs}\nPrice: {price}\n")

# Close the browser
driver.quit()


# In[ ]:


œ

