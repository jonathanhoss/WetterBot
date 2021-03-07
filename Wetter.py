import requests
from bs4 import BeautifulSoup
import re
import collections.abc

def skip_first(it):
    """
    Skip the first element of an Iterator or Iterable,
    like a Generator or a list.
    This will always return a generator or raise TypeError()
    in case the argument's type is not compatible
    """
    if isinstance(it, collections.abc.Iterator):
        try:
            next(it)
            yield from it
        except StopIteration:
            return
    elif isinstance(it, collections.abc.Iterable):
        yield from skip_first(it.__iter__())
    else:
        raise TypeError(f"You must pass an Iterator or an Iterable to skip_first(), but you passed {it}")

def dhv_wetter():
    html_text = requests.get('https://www.dhv.de/wetter/').text
    soup = BeautifulSoup(html_text, 'lxml')

    wetterClass = re.compile('wetter-*')
    headerClassN = re.compile('csc-header csc-header-n*')
    headerClassS = re.compile('csc-header csc-header-n*')

    raw_text = soup.find_all("div", class_=[wetterClass, headerClassN, headerClassS])

    text = "*+++++++  A L L G E M E I N  +++++++*"

    DHVwetter = {"Allgemein":"","Nord":"","Süd":""}
    key = "Allgemein"
    nord = "+++++++  N O R D A L P E N  +++++++"
    sued = "+++++++ S Ü D A L P E N +++++++"


    DHVwetter[key] = DHVwetter[key] + text


    for block in raw_text:
        firstline = next(block.stripped_strings)
        if firstline == nord:
            key = "Nord"
        elif firstline == sued:
            key = "Süd"
        # else:
        #     firstline = ""
        
        DHVwetter[key] = DHVwetter[key] + '\n' + ("--------------------")  + '\n'
        DHVwetter[key] = DHVwetter[key] + firstline

        for line in skip_first(block.stripped_strings):
            DHVwetter[key] = DHVwetter[key] + '\n' + (line)
        

        # text = text + '\n' + ("*" + firstline + "*")
        # for line in skip_first(block.stripped_strings):
        #     text = text + '\n' + (line)
        # text = text + '\n' + ("--------------------")

    return DHVwetter["Nord"]



f = open("dhvToday.txt", "w")
f.write(dhv_wetter())
f.close