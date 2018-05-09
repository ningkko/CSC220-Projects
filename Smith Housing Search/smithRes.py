import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
import re

def getLinks():
    url = "https://www.smith.edu/reslife/houses.php"
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata, 'lxml')
    links = soup.find_all(href=re.compile('houses_'))
    newUrls = []
    for link in links[:6]:
        housesUrl = parse.urljoin(url, link['href'])
        newUrls.append(housesUrl)

    resUrl = []
    for url in newUrls:
        wbdata = requests.get(url).text
        soup = BeautifulSoup(wbdata, 'lxml')
        links = soup.select("div > ul > li > a")
        for link in links:
            fullUrl = parse.urljoin(url, link['href'])
            resUrl.append(fullUrl)

    return resUrl

def getTable(resUrl):
    infoFile = open('housedata.json', 'w')
    for url in resUrl:
        wbdata = requests.get(url).text
        soup = BeautifulSoup(wbdata, 'lxml')
        table = soup.select('table.table > tr')
        houseName = soup.select('div > h1')
        houseName = houseName[0].get_text()
        houseinfo = []
        houseDict = {}
        for line in table:
            data = line.get_text().split('\n')
            for info in data:
                if info != '':
                    houseinfo.append(info)
        houseDict['name'] = houseName
        for n in range(0, len(houseinfo), 2):
            houseDict[houseinfo[n]] = houseinfo[n+1]
        json.dump(houseDict, infoFile)


def main():
    resUrl = getLinks()
    getTable(resUrl)

main()
