
import sys

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} filename words to search")
    exit()

try:

    search_words = []
    ocurrence = []
    for x in range(len(sys.argv) - 2):
        search_words.append(sys.argv[x+2])
        ocurrence.append(0)

    file_name = sys.argv[1]

    fd = open(file_name, 'r', 1)
    for line in fd:
        parsed_line = line.rstrip('\n').split(" ")
#        print(parsed_line)
        for word in parsed_line:
            for str in search_words:
#                print(f"{word} {str}")
                if str == word:
                    ocurrence[search_words.index(str)] = ocurrence[search_words.index(str)] + 1

    fd.close()

    for words in search_words:
        print(f"{words} was found a total of {ocurrence[search_words.index(words)]}")

except IOError:
    print(f"Could not read file: {file_name}")
    exit