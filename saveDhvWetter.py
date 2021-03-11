import json

import getDhvWetter


def saveDhvWetter():
    wetter_list = getDhvWetter.dhv_wetter()

    #wetter_list= ['DHV-Wetter (D, Alpen-N, Alpen-S)\n\n', 'Do.: Sturmtief, regnerisch\nMit wenigen Aufhellungen\nstark bewölkt, regnerisch, stürmisch.\nWind: Starker bis stürmischer SW-Wind!\n\n', 'Fr.: Windig, durchwachsen\nWechselnd bewölkt, windig,\nmeist nur im NW etwas Regen.\nWind: Starker, im Norden stürmischer SW-Wind.\n\n', 'Sa.: Sturmtief, regnerisch\nMit wenigen Aufhellungen\nstark bewölkt, regnerisch, stürmisch.\nWind: Starker bis stürmischer SW-Wind!\n\n', '+++++++  N O R D A L P E N  +++++++\n\n', 'Do.: Sturmtief\nMit vielen As/Cs-Feldern\n"eher stark bewölkt als aufgelockert", stürmischer Föhn.\nWind: Stürmischer SW-Wind, stürmischer Föhn!\n\n', 'Fr.: Windiges Tiefdruckwetter\nÜberwiegend\nstark bewölkt, windig,\nteils einige Tropfen.\nWind: Starker westlicher Wind.\n\n', 'Sa.: Tiefdruckwetter, Föhn\nMit meist vielen As/Cs-Feldern\n"eher sehr wolkig als aufgelockert", starker Föhn.\nWind: Meist mäßiger bis starker SW-Wind, Föhn! Am Nordalpenrand deutlich weiter auflebend.\n\n', 'So.: Windige Kaltfront mit Neuschnee\nWechselnd, teils stark bewölkt mit Schneefall, windig.\nWind: Starker W/NW-Wind.\n\n', 'Mo.: Nordstau, Neuschnee\nTREND\n: Stark bewölkt mit deutlich Neuschnee, starker WNW-Wind.\nLage weiter beobachten.\n\n', '+++++++ S Ü D A L P E N +++++++\n\n', 'Do.: Hoch zieht ab, SW-Strömung\nMit etlichen\nAc/Ci-Feldern und "aufgelockert, zeitweise halbwegs freundlich".\nBassano: Feuchte Luft und meist wolkig/trübe "Bassano-Suppe". Nach Mittag KÖNNTEN einzelne Auflockerungen durchkommen, dann mäßige Thermik mit Basis um 1200mNN. Details bleiben unscharf.\nWind: Schwacher bis mäßiger SW-Wind.\n\n', 'Fr.: Tiefdruck, SW-Strömung\nWechselnd bewölkt, teils einige Tropfen.\nBassano: Sehr wolkig/trübe "Bassano-Suppe", kaum nutzbare Thermik.\nWind: Mäßiger WSW-Wind.\n\n', 'Sa.: Hochdruckeinfluss\nTREND\n: In der Nacht zu Sa. zieht eine schwach wetterwirksame Störung mit Nordströmung durch, tagsüber dann mit Hochdruckeinfluss aufgelockert bis freundlich.\nThermik: Wahrscheinlich starke, hochreichende Frühjahrsthermik, schwacher bis mäßiger SW-Wind.\nLage weiter beobachten.\n\n', 'So.: Kaltfront, starker Nordföhn\nTREND:\nWechselnd bis stark bewölkt mit Schauern (ab 900mNN oft als Schnee). Aufkommender sehr starker Nordföhn!\nLage weiter beobachten.\n\n', 'Mo.: Nordföhn\nTREND\n: Mit +/-etlichen Ac/Ci-Feldern aufgelockert, evtl. teils freundlich, Nordföhn.\nLage weiter beobachten,\nauch für Bassano noch keine belastbare Aussage möglich.\n\n', 'Hinweise:\n\n']

    wetter = {"allgemein": [],"nord": [], "süd": []}

    active = wetter["allgemein"]
    for r in wetter_list:

        if r == "+++++++  N O R D A L P E N  +++++++\n\n":
            active = wetter["nord"]
        elif r == "+++++++ S Ü D A L P E N +++++++\n\n":
            active = wetter["süd"]
        elif r == "Hinweise:\n\n":
            continue

        active.append(r)

    data = wetter


    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    saveDhvWetter()