#set word list of 5-letter words
#maybe we need to trim data into set type
wordSet = []
f = open("./words.txt", "r")
for line in f.readlines():
    wordSet.append(line.rstrip())
wordSet = tuple(wordSet)
f.close()