import json
import saveDhvWetter

foehn_diagramm = "http://www.wetteralarm.at/uploads/pics/uwz-at_foehn_de.png"


def loadJson():
    with open('data.json', encoding='utf-8') as fh:
        data = json.load(fh)
    return(data)

def stringifyWetter(wetterList):
    text = ""
    for field in wetterList:
        text = text + field
    return text


def sample_responses(input_text):
    user_message = str(input_text).lower()
    navigation = '\n /allgemein \n /nord \n /sued \n /foehn \n'

        
    if user_message in ("nord", "/nord"):
        wetter = loadJson()
        return stringifyWetter(wetter["nord"]) + navigation

    if user_message in ("süd", "sued", "/süd", "/sued"):
        wetter = loadJson()
        return stringifyWetter(wetter["süd"]) + navigation

    if user_message in ("allgemein", "/allgemein"):
        wetter = loadJson()
        return stringifyWetter(wetter["allgemein"]) + navigation

    if user_message in ("foehn", "/foehn", "föhn"):
        return foehn_diagramm + "\n"  + navigation

    if user_message in ("update", "/update"):
        saveDhvWetter.saveDhvWetter()
        return "Wetter wurde geupdatet"