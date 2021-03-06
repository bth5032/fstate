def N(decay_str):
    if (' N ' in decay_str):
        return [
                decay_str.replace(" N ", " p "),
                decay_str.replace(" N ", " n "),
                decay_str.replace(" N ", " N(1440) "),
                decay_str.replace(" N ", " N(1520) "),
                decay_str.replace(" N ", " N(1535) "),
                decay_str.replace(" N ", " N(1650) "),
                decay_str.replace(" N ", " N(1675) "),
                decay_str.replace(" N ", " N(1680) "),
                decay_str.replace(" N ", " N(1685) "),
                decay_str.replace(" N ", " N(1700) "),
                decay_str.replace(" N ", " N(1710) "),
                decay_str.replace(" N ", " N(1720) "),
                decay_str.replace(" N ", " N(1860) "),
                decay_str.replace(" N ", " N(1875) "),
                decay_str.replace(" N ", " N(1880) "),
                decay_str.replace(" N ", " N(1895) "),
                decay_str.replace(" N ", " N(1900) "),
                decay_str.replace(" N ", " N(1990) "),
                decay_str.replace(" N ", " N(2000) "),
                decay_str.replace(" N ", " N(2040) "),
                decay_str.replace(" N ", " N(2060) "),
                decay_str.replace(" N ", " N(2100) "),
                decay_str.replace(" N ", " N(2120) "),
                decay_str.replace(" N ", " N(2190) "),
                decay_str.replace(" N ", " N(2220) "),
                decay_str.replace(" N ", " N(2250) "),
                decay_str.replace(" N ", " N(2600) "),
                decay_str.replace(" N ", " N(2700) "),
                decay_str.replace(" N ", " N(~3000) "),                  
               ]
    else:
        return decay_str

def Delta(decay_str):
    if (' Delta ' in decay_str):
        return [
                decay_str.replace(" Delta ", " Delta(1232) "),
                decay_str.replace(" Delta ", " Delta(1600) "),
                decay_str.replace(" Delta ", " Delta(1620) "),
                decay_str.replace(" Delta ", " Delta(1700) "),
                decay_str.replace(" Delta ", " Delta(1750) "),
                decay_str.replace(" Delta ", " Delta(1900) "),
                decay_str.replace(" Delta ", " Delta(1905) "),
                decay_str.replace(" Delta ", " Delta(1910) "),
                decay_str.replace(" Delta ", " Delta(1920) "),
                decay_str.replace(" Delta ", " Delta(1930) "),
                decay_str.replace(" Delta ", " Delta(1940) "),
                decay_str.replace(" Delta ", " Delta(1950) "),
                decay_str.replace(" Delta ", " Delta(2000) "),
                decay_str.replace(" Delta ", " Delta(2150) "),
                decay_str.replace(" Delta ", " Delta(2200) "),
                decay_str.replace(" Delta ", " Delta(2300) "),
                decay_str.replace(" Delta ", " Delta(2350) "),
                decay_str.replace(" Delta ", " Delta(2390) "),
                decay_str.replace(" Delta ", " Delta(2400) "),
                decay_str.replace(" Delta ", " Delta(2420) "),
                decay_str.replace(" Delta ", " Delta(2750) "),
                decay_str.replace(" Delta ", " Delta(2950) "),
                decay_str.replace(" Delta ", " Delta(~3000) "),                
               ]
    else:
        return decay_str

Delta


def pipii(decay_str):
    return decay_str.replace("(pipi)**I = 0(S-wave)", "pi pi")

def nporn(decay_str):
    return decay_str.replace("(N = p or n)", "")
    