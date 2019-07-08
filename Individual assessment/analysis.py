import pandas as pd

# Import from excel to pandas data frame
excludedWordsDF = pd.read_csv("excludedWords.csv")
excWords = excludedWordsDF['WORDS'].tolist()
potentialWordsDF = pd.read_csv("testWords.csv")
potWords = potentialWordsDF['WORDS'].tolist()
mainData = pd.read_excel("Talent data for analysis.xlsx")
mainData = mainData.head(10)


# set up function for processing mainData
def textAnalysis(axis):
    strengths = str(mainData['Strengths'])
    devAreas = str(mainData['Development Areas'])
    marker = ""
    readyMarker = ""
# missing an iterable here to co-join the for loops or do we?????
    # analyse the strengths
    for word in strengths.split():
        potWordsCount = 0
        excWordsCount = 0
        sCheckWordsCount = 0
        word = word.lower()
        if word in excWords:
            excWordsCount += 1
        elif word in potWords:
            potWordsCount += 1
        else:
            sCheckWordsCount += 1
        fullCount = potWordsCount + sCheckWordsCount
        if fullCount != 0:
            strengthDensity = round(((potWordsCount / fullCount) * 100), 2)
        else:
            strengthDensity = 0
        mainData['Strengths Density'] = strengthDensity

    # analyse the development areas

    for word in devAreas.split():
        potWordsCount = 0
        excWordsCount = 0
        dCheckWordsCount = 0
        word = word.lower()
        if word in excWords:
            excWordsCount += 1
        elif word in potWords:
            potWordsCount += 1
        else:
            dCheckWordsCount += 1
        fullCount = potWordsCount + dCheckWordsCount
        if fullCount != 0:
            devAreaDensity = round(((potWordsCount / fullCount) * 100), 2)
        else:
            devAreaDensity = 0
        mainData['Development Areas Density'] = devAreaDensity

    # calculate talent status
    difference = strengthDensity - devAreaDensity
    if difference > 0:
        marker = "Potential Talent"
        if difference > 1.75:
            readyMarker = "Ready"
        else:
            readyMarker = "To develop"
    else:
        marker = ""
        readyMarker = ""

    mainData['Difference'] = difference
    mainData['Potential Talent?'] = marker
    mainData['Readiness'] = readyMarker

    mainData.to_excel("results.xlsx")

# need to return from the function


mainData.apply(textAnalysis, axis=1)

print("Completed")
