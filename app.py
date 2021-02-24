import json
from difflib import get_close_matches

data = json.load(open("data.json"))


# function returns the definition of the word
def translate(w):
    # Ignore Uppercase letters
    w = w.lower()

    # check to see if the users input is in the database
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    # fimd a word that is closely matches a word in data
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return " the word doesn't exist. Please double check it."


# user inputs word to be defined
word = input("Enter Word you would like to define: ")
output = translate(word)

# Prints the definition of the users input
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
