import pprint
import csv_reader
from review_scoring import getTopPositiveNegativeTupple

pp = pprint.PrettyPrinter(indent=4)


reviews = csv_reader.getReviewsFromCsvFile("DB/Hotel_Reviews.csv")
# print(len(reviews))

topSize = 10
positive, nagative = getTopPositiveNegativeTupple(topSize, reviews, 3)
print("Top " + str(topSize) + " Positive reviews words: ")
pp.pprint(positive)
print("Top " + str(topSize) + " Negative reviews words: ")
pp.pprint(nagative)
