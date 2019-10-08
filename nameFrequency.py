import pandas as pd
import statistics

names = {}
countLines = 0
totalCount = 0
namedf = pd.read_excel("NL_Names_FY19.xlsx")

for fn in namedf["Full Name"]:
    if fn in names:
        names[fn] += 1
    else:
        names[fn] = 1

countDf = pd.DataFrame.from_dict(names, orient='index', columns=['Count'])
countDf = countDf.sort_values(by='Count', ascending=False)

print(countDf.head())

for line in countDf["Count"]:
    countLines += 1
    totalCount += line

print("Count of Lines: " + str(countLines))
print("Total Frequency: " + str(totalCount))

averageFrequency = totalCount / countLines

print("The Average frequency of request is " + str(averageFrequency))

mostCommon = statistics.mode(countDf["Count"])

print("Mode value: " + str(mostCommon))
