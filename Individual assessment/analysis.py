#  Imports and setup
import pandas as pd

# Import from excel to pandas data frame
excludedWordsDF = pd.read_csv("excludedWords.csv")
excWords = excludedWordsDF['WORDS'].tolist()
potentialWordsDF = pd.read_csv("testWords.csv")
potWords = potentialWordsDF['WORDS'].tolist()
mainData = pd.read_excel("Talent data for analysis.xlsx")


# run the analysis
def strengthsResults(textData):
    potWordsCount = 0
    excWordsCount = 0
    checkWordsCount = 0
    for word in textData.split():
        word = word.lower()
        if word in excWords:
            excWordsCount += 1
        elif word in potWords:
            potWordsCount += 1
        else:
            checkWordsCount += 1
    fullCount = potWordsCount + checkWordsCount
    strengthsOut = (excWordsCount, potWordsCount, fullCount)
    return strengthsOut


def devAreaResults(textData2):
    potWordsCount = 0
    excWordsCount = 0
    checkWordsCount = 0
    for word in textData2.split():
        word = word.lower()
        if word in excWords:
            excWordsCount += 1
        elif word in potWords:
            potWordsCount += 1
        else:
            checkWordsCount += 1
    fullCount = potWordsCount + checkWordsCount
    devAreasOut = (excWordsCount, potWordsCount, fullCount)
    return devAreasOut


def calcFields(strengthsOut, devAreasOut):
    marker = ""
    readyMarker = ""
    strengthDensity = round(((strengthsOut[1] / strengthsOut[2]) * 100), 2)
    devAreaDensity = round(((devAreasOut[1] / devAreasOut[2]) * 100), 2)
    difference = strengthDensity - devAreaDensity
    if difference > 0:
        marker = "Potential Talent"
        if difference > 1.75:
            readyMarker = "Ready"
        else:
            readyMarker = "To develop"

    calcOut = (strengthDensity, devAreaDensity, difference, marker, readyMarker)
    mainData['Strengths Density'] = calcOut[0]
    mainData['Developement Areas Density'] = calcOut[1]
    mainData['Difference'] = calcOut[2]
    mainData['Potential Talent?'] = calcOut[3]
    mainData['Readiness'] = calcOut[4]
    return calcOut


for index in mainData.head():
    calcFields(strengthsResults(str(mainData['Strengths'])), devAreaResults(str(mainData['Development Areas'])))

# output the result to Excel
mainData.to_excel("Individual Analysis Outputs.xlsx")
