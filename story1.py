from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    adjective1 = getWord("Enter a adjective: ")
    noun1 = getWord("Enter a noun: ")
    adjective2 = getWord("Enter a adjective: ")
    noun2 = getWord("Enter a noun: ")
    adjective3 = getWord("Enter a adjective: ")
    noun3 = getWord("Enter a person: ")
    adjective4 = getWord("Enter a adjective: ")
    noun4 = getWord("Enter a thing: ")
    name1= getWord("Enter a name: ")
    noun5 = getWord("Enter a air vehical: ")
    ocean1 = getOcean("Enter a ocean: ")
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like  " + temperature1
    text += " out."   
    text += " Then I got very  " + adjective1
    text += " so I went to the store to buy a " + noun1
    text += " it was very " + adjective2
    text += " . Then I continued on with my day until I found a " + noun2
    text += " on the street."
    text += " This made me feel very " + adjective3
    text += " . Soon after that I ran into my favorite celberty " + noun3
    text += " . Then I went home just to find out that my mom was " + adjective4
    text += " . I just went to my room and my mom would let me leave so I got a "
    text += " to brake out of my window"
    text += " . I climbed down and then I bumped into" + name1
    text += " He told me we have to go."
    text += " We get into a " + noun5
    text += " . Then we started over the " +getOcean
    
    return text
