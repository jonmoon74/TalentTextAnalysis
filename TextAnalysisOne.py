import pandas as pd

# setting the variables
wordsCount = 0
includedWordsCount = 0
dict = {}
excludedWordsCount = 0
uniqueWords = []
uniqueWordsCount = 0

# read in the excluded words list and create as a list
exclusionFile = str(input("Enter the name of the file of words to exclude: "))
excludedWordsDF = pd.read_csv(exclusionFile)
excludedWords = excludedWordsDF['WORDS'].tolist()

# read in the file for analysis and build a dictionary of the words used
# excluding those featured in the excluded words file
sourceFile = str(input("Enter the name of the source file to analyse: "))
sourceFileName = sourceFile.split(".")
sourceLead = sourceFileName[0]

with open(sourceFile, 'r') as f:
    for line in f:
        line = bytes(line, 'utf-8').decode('utf-8', 'ignore')
        for word in line.split():
            word = word.lower()
            wordsCount += 1
            if word in excludedWords:
                excludedWordsCount += 1
            elif word in dict:
                dict[word] += 1
                includedWordsCount += 1
            else:
                dict[word] = 1
                includedWordsCount += 1

df = pd.DataFrame.from_dict(dict, orient='index', columns=['Count'])
df = df.sort_values(by='Count', ascending=False)

wordsLeader = "The number of words that were "
print("\n" + wordsLeader + "excluded is: " + str(excludedWordsCount))
print(wordsLeader + "included in the analysis is: " + str(includedWordsCount))
print("The total number of words analysed is: " + str(wordsCount))

outputTitle = sourceLead + "_freq.csv"
df.to_csv(outputTitle)

for i in dict:
    if dict[i] == 1:
        uniqueWords.append(i)
        uniqueWordsCount += 1

uw = pd.Series(uniqueWords)
uwOutputTitle = "unique_words_in_" + sourceLead + ".csv"
uw.to_csv(uwOutputTitle, header=False)

print("\nWord summary data: ")
print("The number of unique words is: " + str(uniqueWordsCount))

uniquePercent = round(((uniqueWordsCount / wordsCount) * 100), 2)
excludedPercent = round(((excludedWordsCount / wordsCount) * 100), 2)
includedPercent = round(((includedWordsCount / wordsCount) * 100), 2)

pLeader = "The percentage of "
pSecond = "words in the sample is: "

print(pLeader + "unique " + pSecond + str(uniquePercent) + "%")
print(pLeader + "excluded " + pSecond + str(excludedPercent) + "%")
print(pLeader + "included " + pSecond + str(includedPercent) + "%")

topFiftyWords = df.head(50)
print("\nThe top fifty words by value are: " + str(topFiftyWords))
topFiftyOutputTitle = "Top_fifty_" + sourceLead + "words.csv"
topFiftyWords.to_csv(topFiftyOutputTitle)

if "judgement" in dict:
    jCount = dict["judgement"]
else:
    jCount = 0

if "drive" in dict:
    dCount = dict["drive"]
else:
    dCount = 0

if "influence" in dict:
    iCount = dict["influence"]
else:
    iCount = 0


jPerc = round((jCount / includedWordsCount) * 100, 2)
dPerc = round((dCount / includedWordsCount) * 100, 2)
iPerc = round((iCount / includedWordsCount) * 100, 2)


jdiTail = "% of the included word count"

print("\nJDI frequency: ")
print("Judgement was used " + str(jCount) + " times, " + str(jPerc) + jdiTail)
print("Drive was used " + str(dCount) + " times, " + str(dPerc) + jdiTail)
print("Influence was used " + str(iCount) + " times, " + str(iPerc) + jdiTail)

if "curious" in dict:
    curCount = dict["curious"]
else:
    curCount = 0

if "motivation" in dict:
    motiCount = dict["motivation"]
else:
    motiCount = 0

if "insight" in dict:
    insCount = dict["insight"]
else:
    insCount = 0

if "engagement" in dict:
    engCount = dict["engagement"]
else:
    engCount = 0

if "determination" in dict:
    detCount = dict["determination"]
else:
    detCount = 0

curPerc = round((curCount / includedWordsCount) * 100, 2)
motiPerc = round((motiCount / includedWordsCount) * 100, 2)
insPerc = round((insCount / includedWordsCount) * 100, 2)
engPerc = round((engCount / includedWordsCount) * 100, 2)
detPerc = round((detCount / includedWordsCount) * 100, 2)

print("\nThe 21st Century talent traits: ")
print("Curious was used " + str(curCount) + " times, " + str(curPerc) + jdiTail)
print("Motivation was used " + str(motiCount) + " times, " + str(motiPerc) + jdiTail)
print("Insight was used " + str(insCount) + " times, " + str(insPerc) + jdiTail)
print("Engagement was used " + str(engCount) + " times, " + str(engPerc) + jdiTail)
print("Determination was used " + str(detCount) + " times, " + str(detPerc) + jdiTail)
