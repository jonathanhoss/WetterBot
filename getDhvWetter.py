import requests
from bs4 import BeautifulSoup
import re

def dhv_wetter():
    # Get HTML from Website and make soup
    html_text = requests.get('https://www.dhv.de/wetter/').text
    soup = BeautifulSoup(html_text, 'lxml')

    # CSS Classes for Targets 
    wetterClass = re.compile('wetter-*')
    headerClass = re.compile('csc-header csc-header-n*')

    # Get targets from soup
    targets = soup.find_all("div", class_=[wetterClass, headerClass])


    #f = open("dhvToday.txt", "w")
    wetter_list = []
    

    # loop through targets
    for tag in targets:
        # in tag is inside wrapper : wetterClass  ==> prevent that headerClass is displayed twice
        if tag.find_parent(attrs={'class':wetterClass}):
            continue

        bericht = ""
        for line in tag.stripped_strings:
            bericht = bericht + line + "\n"
            #f.write(line + "\n")

        wetter_list.append(bericht + "\n")    
        #f.write("--- --- ---" + "\n")

    #f.close
    #print(wetter_list)
    return(wetter_list)


if __name__ == '__main__':
    dhv_wetter()