#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[230]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
#This task will be done in following steps:
#1. First get the webpage https://www.naukri.com/
#2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
#3. Then click the search button.
#4. Then scrape the data for the first 10 jobs results you get.
#5. Finally create a dataframe of the scraped data.

#importing sleinium to execute the data 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#getting driver 
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")

#tyoing the job title 
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')

#location filter 
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')

#Searching the data
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[231]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]

#initializing the empty attributes 
title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    job_title[:10]
            
#Location finding 
location_tags=driver.find_elements(By.XPATH,'//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-location loc"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    job_location[:10]
    
#company name 
company_tags=driver.find_elements(By.XPATH,'//span[@class=" comp-dtls-wrap"]/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    company_name[:10]

#experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)    
    experience_required[:10]
    
print(len(job_title[:10]),len(job_location[:10]),len(company_name[:10]),len(experience_required[:10]))



# In[232]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Title':job_title[:10],'Lacoation':job_location[:10],'Company name':company_name[:10],'Experience':experience_required[:10]})
df


# In[166]:





# In[178]:


url=driver.find_elements(By.XPATH,'//a[@class="title "]')
url[0:3]
for i in url[0:3]:
       print(i.get_attribute('href'))


# In[179]:


job_titles=[]


# In[191]:


start=0
end=1
for page in range(start,end):
    title=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
    for i in titles:
        job_titles.append(i.text)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[1]/div[2]/div[3]/div/a[2]')
    next_button.click()
    time.sleep(1)


# In[ ]:





# In[ ]:





# In[235]:


#Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
#This task will be done in following steps:
#1. First get the webpage https://www.naukri.com/
#2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
#3. Then click the search button.
#4. Then scrape the data for the first 10 jobs results you get.
#5. Finally create a dataframe of the scraped data.


#getting driver 
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")

#tyoing the job title 
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')

#location filter 
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')

#Searching the data
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[236]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]

#initializing the empty attributes 
title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    job_title[:10]
            
#Location finding 
location_tags=driver.find_elements(By.XPATH,'//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-location loc"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    job_location[:10]
    
#company name 
company_tags=driver.find_elements(By.XPATH,'//span[@class=" comp-dtls-wrap"]/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    company_name[:10]

#experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)    
    experience_required[:10]
    
print(len(job_title[:10]),len(job_location[:10]),len(company_name[:10]),len(experience_required[:10]))

# Close the webdriver
driver.quit()


# In[237]:


# Creating the DATA FRAME from the results
    
import pandas as pd
df=pd.DataFrame({'Title':job_title[:10],'Lacoation':job_location[:10],'Company name':company_name[:10],'Experience':experience_required[:10]})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[244]:


#Q3: In this question you have to scrape data using the filters available on the webpage
#You have to use the location and salary filter.
#You have to scrape data for “Data Scientist” designation fo
#You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
#The task will be done as shown in the below steps:
#1. first get the web page https://www.shine.com/
#2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
#3. Then click the search button.
#4. Then apply the location filter and salary filter by checking the respective boxes
#5. Then scrape the data for the first 10 jobs results you get.
#6. Finally create a dataframe of the scraped data.


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")


# Job title 

job_search=driver.find_element(By.CLASS_NAME,"suggestor-input ")
job_search.send_keys('Data Scientist')

# Location filter 
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')

#clicking on search
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[245]:


# applying filter for salary range 
salary_filter = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label")
salary_filter.click()


# In[246]:


#Scarping the first 10 jobs results 


job_title=[]
job_location=[]
company_name=[]
experience_required=[]

title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    job_title[:10]
    
            
#Location finding 
location_tags=driver.find_elements(By.XPATH,'//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-location loc"]')
for i in location_tags:
    location=i.text
    job_location.append(location)
    job_location[:10]
    
#company name 
company_tags=driver.find_elements(By.XPATH,'//span[@class=" comp-dtls-wrap"]/a[1]')
for i in company_tags:
    company=i.text
    company_name.append(company)
    company_name[:10]

#experience
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp=i.text
    experience_required.append(exp)
    experience_required[:10]


    print(len(job_title),len(job_location),len(company_name),len(experience_required))
    
 # Close the webdriver
driver.quit()   
    


# In[243]:


import pandas as pd
df=pd.DataFrame({'Title':job_title[:10],'Lacoation':job_location[:10],'Company name':company_name[:10],'Experience':experience_required[:10]})
df


# In[250]:


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# Brand
# Product Description
# Price

#get the webdriver 
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

#search product 
product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('Sunglasses')

#click on search
button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button")
button.submit()

#initializing 
brand_title=[]
product_description=[]
product_price=[]

title_tags=driver.find_elements(By.CLASS_NAME, "_2WkVRV")
for i in title_tags:
    title=i.text
    brand_title.append(title)
    brand_title[:100]
            
#product description 
description_tags=driver.find_elements(By.CLASS_NAME, "IRpwTa")
for i in description_tags:
    description=i.text
    product_description.append(description)
    product_description[:100]

#price details
price_tags = driver.find_elements(By.CLASS_NAME,"_30jeq3")
for i in price_tags:
    price = i.text
    product_price.append(price)
    product_price[:100]

# Printing the lengths of the lists
print(len(brand_title[:100]), len(product_description[:100]), len(product_price[:100]))

# Close the webdriver
driver.quit()


# In[249]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_title[:40],'Product description':product_description[:40],'Price':product_price[:40]})
df


# In[ ]:





# In[ ]:





# In[213]:


#Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. 
#You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART
#1. Rating
#2. Review summary
#3. Full review
#4. You have to scrape this data for first 100reviews.



#get the webdriver 
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm0f37c2240b217?page=2")

# Initialize lists to store ratings, review summaries, and full reviews
ratings = []
review_summaries = []
full_reviews = []

# Find rating elements
rating_tags = driver.find_elements(By.CSS_SELECTOR, '._3LWZlK._1BLPMq')
for tag in rating_tags:
    rating = tag.text
    ratings.append(rating)
    ratings[:100]

# Find review summary elements
review_tags = driver.find_elements(By.CSS_SELECTOR, '._2-N8zT')
for tag in review_tags:
    review_summary = tag.text
    review_summaries.append(review_summary)
    review_summaries[:100]

# Find full review elements
full_review_tags = driver.find_elements(By.CSS_SELECTOR, '.t-ZTKy')
for tag in full_review_tags:
    full_review = tag.text
    full_reviews.append(full_review)
    full_reviews[:100]

print(len(ratings),len(review_summaries),len(full_reviews))

# Close the webdriver
driver.quit()


# In[214]:


import pandas as pd
df=pd.DataFrame({'Ratings':ratings[:100],'Review Summary':review_summaries[:100],'Full review':full_reviews[:100]})
df


# In[ ]:





# In[251]:


## Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
#You have to scrape 3 attributes of each sneaker:
#1. Brand
#2. Product Description
#3. Price
#As shown in the below image, you have to scrape the above attributes.

#get the webdriver 
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

#search with the preferred product 
product=driver.find_element(By.CLASS_NAME,"Pke_EE")
product.send_keys('Sneakers')

button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button")
button.submit()


# In[252]:


#initalizing the attributes to extranct the data 

brand_title=[]
product_description=[]
product_price=[]


title_tags=driver.find_elements(By.CLASS_NAME, "_2WkVRV")
for i in title_tags:
    title=i.text
    brand_title.append(title)
            
#product description 
description_tags=driver.find_elements(By.CLASS_NAME, "IRpwTa")
for i in description_tags:
    description=i.text
    product_description.append(description)

#price details
price_tags = driver.find_elements(By.CLASS_NAME,"_3bPFwb")
for i in price_tags:
    price = i.text
    product_price.append(price)

# Printing the lengths of the lists
print(len(brand_title), len(product_description), len(product_price))

# Close the webdriver
driver.quit()


# In[253]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_title,'Product description':product_description,'Price':product_price})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[208]:


#Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. 
#Then set CPU Type filter to “Intel Core i7” as shown in the below image:
#After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop: 
#1. Title
#2. Ratings 
#3. Price


from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the Amazon website
driver.get("https://www.amazon.in/")

search_input = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter "Laptop" in the search field and press Enter
search_input.send_keys("Laptop")
search_input.send_keys(Keys.ENTER)

# Wait for the page to load
driver.implicitly_wait(5)

# Find and click on the CPU Type filter for "Intel Core i7"
cpu_filter = driver.find_element(By.XPATH, "//span[text()='Intel Core i7']")
cpu_filter.click()


# Initialize lists to store data
brand_title = []
product_rating = []
product_price = []

# Find and extract brand title
title_tags = driver.find_elements(By.XPATH, '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
for tag in title_tags:
    title = tag.text
    brand_title.append(title)
    brand_title[:24]

# Find and extract product ratings
rating_tags = driver.find_elements(By.XPATH, '//a[@class="a-popover-trigger a-declarative"]')
for tag in rating_tags:
    rating = tag.get_attribute("title")
    product_rating.append(rating)
    product_rating[:24]

# Find and extract product prices
price_tags = driver.find_elements(By.XPATH, '//span[@class="a-price"]')
for tag in price_tags:
    price = tag.text
    product_price.append(price)
    product_price[:24]

# Printing the lengths of the lists
print(len(brand_title))
print(len(product_rating))
print(len(product_price))

# Close the webdriver
driver.quit()


# In[209]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_title[:24],'Price':product_rating[:24],'Rating':product_price[:24]})
df


# In[ ]:





# In[256]:


#Q8: Write a python program to scrape data for Top 1000 Quotes of All Time. The above task will be done in following steps:
#1. First get the webpagehttps://www.azquotes.com/ 
#2. ClickonTopQuotes
#3. Than scrap a) Quote b) Author c) Type Of Quotes

#getting the webdriver open 

driver = webdriver.Chrome()
driver.get("https://www.azquotes.com/")

#slecting the option available above the website
top_quotes_link = driver.find_element(By.XPATH, "//a[text()='Top Quotes']")
top_quotes_link.click()

#scrap a) Quote b) Author c) Type Of Quotes

quote_title = []
author_name = []
quote_type = []

quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quote_tags:
    quote=i.text
    quote_title.append(quote)
    quote_title[:100]
    
author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in author_tags:
    author=i.text
    author_name.append(author)
    author_name[:100]
    
quote_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in quote_tags:
    category =i.text
    quote_type.append(category)
    quote_type[:100]
    
print(len(quote_title[:100]),len(author_name[:100]),len(quote_type[:100]))


# In[257]:


#Creating a DATA FRAME 

import pandas as pd
df=pd.DataFrame({'Quote':quote_title[:100],'Author':author_name[:100],'Type Of Quotes':quote_type[:100]})
df


# In[ ]:





# In[ ]:





# In[258]:


#Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) from https://www.jagranjosh.com/.
#This task will be done in following steps:
#1. First get the webpagehttps://www.jagranjosh.com/
#2. Then You have to click on the GK option
#3. Then click on the List of all Prime Ministers of India
#4. Then scrap the mentioned data and make the DataFrame.


#1. First get the webpagehttps://www.jagranjosh.com/

driver = webdriver.Chrome()
driver.get("https://www.jagranjosh.com/")

#2. Then You have to click on the GK option
gk_link = driver.find_element(By.XPATH,'//a[@href="https://www.jagranjosh.com/general-knowledge"][1]')
gk_link.click()


# In[259]:


#3. Then click on the List of all Prime Ministers of India

prime_ministers_link = driver.find_element(By.XPATH, '//a[contains(text(), "Prime Ministers of India")]')
prime_ministers_link.click()

#Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks)

prime_title=[]
prime_date=[]
office=[]
prime_remarks=[]

title_tags=driver.find_elements(By.XPATH,'//table[contains(@class,"table")]//tr[position()>1]/td[2]/strong/a')
for i in title_tags:
   name=i.text
   prime_title.append(name)
   prime_title[:19]
   
prime_tags=driver.find_elements(By.XPATH,'//table[contains(@class,"table")]//tr[position()>1]/td[3]')
for j in prime_tags:
   status=j.text
   prime_date.append(status)
   prime_date[:19] 
   
office_tags=driver.find_elements(By.XPATH,'//table[contains(@class,"table")]//tr[position()>1]/td[4]/span')
for k in office_tags:
   ofc =k.text
   office.append(ofc)
   office[:19]
   
remarks_tags=driver.find_elements(By.XPATH,'//table[contains(@class,"table")]//tr[position()>1]/td[4]/span')
for i in remarks_tags:
   ofc =l.text
   prime_remarks.append(remarks)
   prime_remarks[:19]
   
print(len(prime_title),len(prime_date),len(office),len(prime_remarks))



# In[ ]:


#Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com/
#This task will be done in following steps:
#1. First get the webpage https://www.motor1.com/
#2. Then You have to type in the search bar ’50 most expensive cars’ 
#3. Then click on 50 most expensive cars in the world..
#4. Then scrap the mentioned data and make the dataframe.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.motor1.com/search/?q=50+most+expensive+card+in+the+world")


# In[ ]:


# Step 3: Click on the link to access the list of the 50 most expensive cars

car_link = driver.find_element(By.XPATH,'/html/body/div[10]/div[10]/div[2]/div[5]/a[2]')
car_link.click()


# In[ ]:


#scrap the below details 
#Car name and Price

car_name=[]
car_price=[]

name_tags = driver.find_elements(By.XPATH, '//h3[@class="subheader"]/span')
for i in name_tags:
    name = i.text
    car_name.append(name)

    
price_tags = driver.find_elements(By.XPATH, '/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[2]/p[4]/strong')
for j in price_tags:
    price = j.text
    car_price.append(price)

print(len(car_name),len(car_price))


# Close the WebDriver
driver.quit()


# In[ ]:


#Creating a DATA FRAME 

import pandas as pd
df=pd.DataFrame({'Car name':car_name[:1],'Car price':car_price[:1]})
df

