import json

data = json.load(open("/Users/amartyaghosh/Code/python/Dictionary/data.json"))

def translate(word):
    #word = word.lower()
    if word in data :
        return (data[ word ])
    else:
        return ("Word not found, please check the word ")

#input_word = input("Enter a word : ").lower()
input_word = input("Enter a word : ").lower()
print (translate(input_word))