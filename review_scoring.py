import re
import operator
from csv_reader import getReviewsFromCsvFile

positiveReveiwTag = "Positive_Review"
negativeReveiwTag = "Negative_Review"
reviewerScoreTag = "Reviewer_Score"
positiveReviewThreshHold = "5"
hotelNameTag = "Hotel_Name"


def getSortedWordOccurenceDict(tag, reviews, hotelName):
    positiveOccurencesDict = {}
    negativeOccurencesDict = {}
    for dbObject in reviews:
        if (hotelName == None or dbObject[hotelNameTag] == hotelName):
            if (dbObject[reviewerScoreTag] > positiveReviewThreshHold):
                reviewText = dbObject[tag].split(" ")
                wordsInPositiveReview = list(filter(None, reviewText))

                for word in wordsInPositiveReview:
                    key = word.lower()
                    oldValue = positiveOccurencesDict.get(key)
                    occurences = 0 if oldValue == None else oldValue
                    positiveOccurencesDict.update(
                        {key: occurences + reviewText.count(word)})
            else:
                reviewText = dbObject[tag].split(" ")
                wordsInNegativeReview = list(filter(None, reviewText))

                for word in wordsInNegativeReview:
                    key = word.lower()
                    oldValue = negativeOccurencesDict.get(key)
                    occurences = 0 if oldValue == None else oldValue
                    negativeOccurencesDict.update(
                        {key: occurences + reviewText.count(word)})

    return sorted(positiveOccurencesDict.items(), key=operator.itemgetter(1), reverse=True), sorted(negativeOccurencesDict.items(), key=operator.itemgetter(1), reverse=True)


def makeIsLongerThan(lengthOfWord):
    def isLongerThan(x):
        if len(x) <= lengthOfWord:
            return False
        else:
            return True
    return isLongerThan


def getTopPositiveNegativeTupple(size, reviews, resultWordLen, hotelName):
    filterFunc = makeIsLongerThan(
        3 if resultWordLen == None else resultWordLen)
    positiveReviewWordList, negativeReviewWordList = getSortedWordOccurenceDict(
        positiveReveiwTag, reviews, hotelName)

    if (size != None):
        return list(filter(filterFunc, list(d[0] for d in positiveReviewWordList)))[:size],  list(filter(filterFunc, list(d[0] for d in negativeReviewWordList)))[:size]
    else:
        return list(filter(filterFunc, list(d[0] for d in positiveReviewWordList))),  list(filter(filterFunc, list(d[0] for d in negativeReviewWordList)))


if __name__ == "__main__":
    reviews = getReviewsFromCsvFile("DB/Hotel_Reviews.csv")
    positive, nagative = getTopPositiveNegativeTupple(
        10, reviews, 5, "Hotel Arena")
