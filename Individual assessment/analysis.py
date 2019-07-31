import pandas as pd

# Import from excel to pandas data frame
excludedWordsDF = pd.read_csv("excludedWords.csv")
excWords = excludedWordsDF['WORDS'].tolist()
potentialWordsDF = pd.read_csv("testWords.csv")
potWords = potentialWordsDF['WORDS'].tolist()
mainData = pd.read_excel("Talent data for analysis.xlsx")
# remove next line for published version
mainData = mainData.head(10)

mainData.set_index('Reference ID', inplace=True)

index = mainData.index

for RID in index:
    strengths = str(mainData.loc[RID, 'Strengths'])
    devAreas = str(mainData.loc[RID, 'Development Areas'])
    marker = ""
    readyMarker = ""
    spotWordsCount = 0
    sexcWordsCount = 0
    sCheckWordsCount = 0
    dpotWordsCount = 0
    dexcWordsCount = 0
    dCheckWordsCount = 0
    # print("devAreas: " + devAreas)

    # analyse the strengths
    for word in strengths.split():
        word = word.lower()
        if word in excWords:
            sexcWordsCount += 1
        elif word in potWords:
            spotWordsCount += 1
        else:
            sCheckWordsCount += 1
        sfullCount = spotWordsCount + sCheckWordsCount
        if sfullCount != 0:
            strengthDensity = round(((spotWordsCount / sfullCount) * 100), 2)
        else:
            strengthDensity = 0
        mainData.loc[RID, 'Strengths Density'] = strengthDensity

    # analyse the development areas

    for word in devAreas.split():
        word = word.lower()
        if word in excWords:
            dexcWordsCount += 1
        elif word in potWords:
            dpotWordsCount += 1
        else:
            dCheckWordsCount += 1
        dfullCount = dpotWordsCount + dCheckWordsCount
        if dfullCount != 0:
            devAreaDensity = round(((dpotWordsCount / dfullCount) * 100), 2)
        else:
            devAreaDensity = 0
        mainData.loc[RID, 'Development Areas Density'] = devAreaDensity

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

    mainData.loc[RID, 'Difference'] = difference
    mainData.loc[RID, 'Potential Talent?'] = marker
    mainData.loc[RID, 'Readiness'] = readyMarker


# mainData.to_excel("results.xlsx")

print(mainData)

print("Completed")
