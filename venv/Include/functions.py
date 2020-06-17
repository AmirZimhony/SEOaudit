import subprocess
import requests
from bs4 import BeautifulSoup
import json


def FindSeoElements(site):#to be executed on soup object of ALL PAGES
    response = requests.get(site)
    html = response.content
    bsElement=BeautifulSoup(html, "html.parser")
    with open('{}.html'.format(str(site)[8:1]), 'wb') as file:
        file.write(bsElement.prettify('utf-8'))
    title=bsElement.title
    if title==None:
        title='none'
    else: title=title.text
    h1=bsElement.h1
    if h1==None:
        h1='none'
    else: h1=h1.text
    metaDes = bsElement.find('meta', {'name': 'description', })
    if metaDes==None:
        metaDes='none'
    else: metaDes=metaDes.get('content')
    metaKeyWords = bsElement.find('meta', {'name': 'keywords', })
    if metaKeyWords==None:
        metaKeyWords='none'
    else: metaKeyWords=metaKeyWords.get('content')
    ListOfSEOElements=(title,h1,metaDes,metaKeyWords)
    return ListOfSEOElements



def CreateJsonFiles(site,i):
    path='Users\Amir\PycharmProjects\SEOaudit\json-files/'
    site2=site.replace('/:','z')
    text = 'lighthouse {} --output-path=/{}.json --output json'.format(site,path+'NYtimes'+str(i))
    subprocess.call(text, shell=True)



def ReadFromJson(i):
    path = '/Users\Amir\PycharmProjects\SEOaudit\json-files/'
    with open('{}.json'.format(path+'NYtimes'+str(i)), encoding="utf8") as j:  # open the file as doc
        data = json.load(j)
    return data['categories']['performance']['score']