from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    adjective1 = getWord("Enter a adjective: ")
    noun1 = getWord("Enter a noun: ")
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like a " + temperature1
    text += " out."   
    text += "Then I got very  " + adjective1
    text += " so I went to the store to buy a " + noun1
    return text
