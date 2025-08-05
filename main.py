from stats import *
import sys

# Gets the contents of a book (with relative pathing)
def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        #print(fileContents)
    return fileContents

# Main function call
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookFilePath = sys.argv[1]
        contents = get_book_text(bookFilePath)
        outputWordCount = count_words(contents)
        outputCharCount = count_characters(contents)

        #Output statements

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookFilePath}...")
        print("----------- Word Count ----------")
        print(outputWordCount)
        print("--------- Character Count -------")
        prettyPrint(outputCharCount)
        print("============= END ===============")
    

# Run overall program
main()
