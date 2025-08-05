# Counts the number of words in the book
def count_words(bookContents):
    bookContentsSplit = bookContents.split()
    numWords = len(bookContentsSplit)
    
    return f"Found {numWords} total words"

# Counts the number of characters in the book
# Includes spaces and symbols
def count_characters(bookContents):
    charDict = {}
    bookContentsLower = bookContents.lower()
   
    for x in range(0, len(bookContentsLower)):
        if bookContentsLower[x] not in charDict:
            newCharCount = 1
            charDict.setdefault(bookContentsLower[x], newCharCount)
        else:
            charDict[bookContentsLower[x]] += 1

    return charDict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def prettyPrint(dictChar):
   
    listSort = []
    for word, count in dictChar.items():
        if word.isalpha():
            listSort.append({"char": word,"num": count})

    listSort.sort(reverse=True, key=sort_on)

    #Print out the newly sorted list:
    for x in range(0, len(listSort)):
        print(f"{listSort[x]["char"]}: {listSort[x]["num"]}")

