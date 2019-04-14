import csv_reader
import re
import operator
import pprint

pp = pprint.PrettyPrinter(indent=4)

positiveReveiwTag = "Positive_Review"
negativeReveiwTag = "Negative_Review"
reviewerScoreTag = "Reviewer_Score"
positiveReviewThreshHold = "7"


def getSortedWordOccurenceDict(tag, dbObject):
    reviewText =  dbObject[tag].split(" ")
    wordsInPositiveReview =  list(filter(None, reviewText))

    occurencesDict = { }
    for word in wordsInPositiveReview:
        occurencesDict.update({ word : reviewText.count(word) })

    return sorted(occurencesDict.items(), key=operator.itemgetter(1), reverse=True)

positiveReviewWordList = []
negativeReviewWordList = []
for dbObject in csv_reader.allReviews:
    if (dbObject[reviewerScoreTag] > positiveReviewThreshHold):
        positiveReviewWordList.append(getSortedWordOccurenceDict(positiveReveiwTag, dbObject))
    else:
        negativeReviewWordList.append(getSortedWordOccurenceDict(negativeReveiwTag, dbObject))

# print(sortedDict)



pp.pprint(len(negativeReviewWordList))