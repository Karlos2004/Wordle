#set word list of 5-letter words
#maybe we need to trim data into set type
wordSet = set()
f = open("./words.txt", "r")
for line in f.readlines():
    wordSet.add(line.rstrip())
f.close()