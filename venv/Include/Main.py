
# Load the packages
from Include import functions
import xlsxwriter
import requests
from bs4 import BeautifulSoup
import subprocess
import time


workbook = xlsxwriter.Workbook('NYTimes.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Site')
worksheet.write(1,0,'Title')
worksheet.write(2,0,'H1')
worksheet.write(3,0,'Meta-Description')
worksheet.write(4,0,'Performance')
# Defining the url of the site
base_site = "https://www.nytimes.com"
base_len=len(base_site)
# Making a get request
response = requests.get(base_site)
response.status_code

# Extracting the HTML
html = response.content

soup = BeautifulSoup(html, "html.parser")
with open('{}.html'.format(str(base_site)[8:1]), 'wb') as file:
    file.write(soup.prettify('utf-8'))
links = soup.find_all('a',{'class':'css-1wjnrbv'})  #Subjective part of code: the desired class is different for each website
importantLinks=[]
for link in links:
    importantLinks.append((link['href']))
importantLinks = list(dict.fromkeys(importantLinks))
PerformanceAnswers=dict.fromkeys(importantLinks)
importantLinks.insert(0,base_site)#importantLinks now has URLs of all the important links + homepage
length=len(importantLinks)
for i in range(length):
    functions.CreateJsonFiles(importantLinks[i],i)
for i in range(length):
    site=importantLinks[i]
    SEOelements=functions.FindSeoElements(site)
    worksheet.write(0, i+1,site)
    worksheet.write(1, i+1, SEOelements[0])
    worksheet.write(2, i+1, SEOelements[1])
    worksheet.write(3, i+1, SEOelements[2])
    worksheet.write(4, i+1, functions.ReadFromJson(i))
    time.sleep(1)
workbook.close()
